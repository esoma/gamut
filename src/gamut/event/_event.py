
from __future__ import annotations

__all__ = ['Event']

# gamut
from ._future import Future
from ._task import Task
from ._taskmanager import TaskManager
# python
import inspect
from typing import (Any, Callable, ClassVar, Generator, Generic, Optional,
                    overload, Sequence, Union, Type, TypeVar)
from weakref import WeakSet


T = TypeVar('T')


# there is some hackery going on here
# see: https://github.com/python/typing/issues/715
class EventType(type):
    """The EventType metaclass serves to make the Event class itself awaitable.
    """

    _all: WeakSet[Type[EventType]] = WeakSet()

    def __new__(cls, name, bases, attrs, **kwds): # type: ignore
        cls = super().__new__(cls, name, bases, attrs, **kwds) # type: ignore
        cls._future = None
        cls._sent_callbacks = WeakSet() # type: ignore
        cls._all.add(cls)
        return cls
    
    def __await__(cls: Type[T]) -> Generator[Future[T, Task[T]], None, T]:
        if cls._future is None: # type: ignore
            cls._future = Future() # type: ignore
        return cls._future.__await__() # type: ignore
    

def reset_events() -> None:
    """Effectivley "resets" all Events. Any Tasks that are waiting on any
    Event will be broken and any registered sent callbacks are lost. This is
    made for testing purposes.
    """
    for event in EventType._all:
        event._future = None
        event._sent_callbacks = WeakSet()
        
        
def add_sent_callback(
    event: Type[E],
    callback: EventSentCallback[E]
) -> None:
    event._sent_callbacks.add(callback)
    
    
def remove_sent_callback(
    event: Type[E],
    callback: EventSentCallback[E]
) -> None:
    try:
        event._sent_callbacks.remove(callback)
    except KeyError:
        pass


class Event(metaclass=EventType):
    """Events are distinct global units which may be awaited on.
    
    The Event class itself is what is awaited on and it will return an instance
    of that Event (or a subclass) which was sent.
    
    Event instances may be sent using the "send" and "asend" methods. When an
    Event is sent it will wake up any tasks that were waiting on that Event or
    a parent class.
    
    The "send" method will only queue up the Task in the active TaskManager.
    On the other hand the "asend" method may be awaited so that the results of
    that Event being sent are processed before continuing the execution.
    
    Event use annotations to define which additional fields they have:
    
    class SubEvent(Event):
        my_attribute: int
    sub_event = SubEvent(1)
    assert sub_event.my_attribute == 1
    
    Attributes may be made "static" in subclasses:
    
    class SubEvent100(SubEvent, my_attribute=100):
        pass
    sub_event_100 = SubEvent()
    assert sub_event_100.my_attribute == 100
    """

    _fields: ClassVar[dict[str, Any]] = {}

    class _NonStaticType(type):
        def __repr__(cls) -> str:
            return '<NonStatic>'

    class _NonStatic(metaclass=_NonStaticType):
        pass

    def __init_subclass__(cls, **kwargs: Any) -> None:
        # we need to build the _fields data structure for this specific class,
        # start by generating it from the annotations that were specified in
        # this class definition
        #
        # we don't want to copy any fields from our base classes yet because
        # there are incompatibility checks to detect
        fields: dict[str, Any] = {
            k: cls._NonStatic
            for k in cls.__annotations__
            if k not in cls._fields
        }
        # now we can apply static values to any base class fields
        # note that we don't pull in the base class field values from the base
        # classes yet, this is to ensure we're capturing the information
        # declared in this specific class definition first
        original_kwargs = dict(kwargs)
        for k, v in cls._fields.items():
            try:
                fields[k] = kwargs.pop(k)
            except KeyError:
                pass
        # now we travel the class inheritance graph, ignoring this class since
        # we've already procesed it
        for mro_cls in inspect.getmro(cls):
            if mro_cls is cls or not issubclass(mro_cls, Event):
                continue
            # we copy any fields from our parent classes in mro
            for field, value in mro_cls._fields.items():
                if value is not cls._NonStatic and field in original_kwargs:
                    raise TypeError(
                        f'got an unexpected keyword argument \'{field}\''
                    )    
                # if the field is static we need to make sure that doesn't
                # conflict with any base classes, for example a base class
                # may say the value is statically set to 5, but ours says it is
                # set to 6
                current_value = fields.get(field, cls._NonStatic)
                if current_value is not cls._NonStatic:
                    if value is not cls._NonStatic and current_value != value:
                        raise TypeError(
                            f'incompatible Event fields: "{field}" is locked '
                            f'to {current_value}, but {mro_cls} has the same '
                            f'field locked to {value}'
                        )
                else:
                    fields[field] = value
        cls._fields = fields
        super().__init_subclass__(**kwargs)

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        for field, arg in self._fields.items():
            if arg is self._NonStatic:
                try:
                    arg = kwargs.pop(field)
                    if args:
                        raise TypeError(
                            f'got multiple values for argument ''{field}'''
                        )
                except KeyError:
                    try:
                        arg, *args = args # type: ignore
                    except ValueError:
                        try:
                            arg = getattr(self.__class__, field)
                        except AttributeError:
                            raise TypeError(
                                f'missing argument {field!r}'
                            ) from None
            setattr(self, field, arg)
        super().__init__(*args, **kwargs)

    def __repr__(self) -> str:
        s = ' '.join(
            f'{"*" if v is not self._NonStatic else ""}{k}={getattr(self, k)}'
            for k, v in self._fields.items()
        )
        return f'<{type(self).__name__} {s}>'

    def send(self: E) -> None:
        task_manager = TaskManager.get_current()
        if task_manager is None:
            raise RuntimeError('no active task manager')

        tasks: list[Task[E]] = []
        for cls in inspect.getmro(self.__class__):
            if not issubclass(cls, Event):
                continue
            future = cls._future
            if future is not None:
                tasks += future.resolve(self)
            for sent_callback in cls._sent_callbacks:
                task = sent_callback(task_manager, self)
                if task is not None:
                    tasks.append(task)
            cls._future = None

        for task in Task.sort(tasks):
            task_manager.queue(task)
                
    async def asend(self) -> None:
        task_manager = TaskManager.get_current()
        self.send()
        assert task_manager is not None
        
        future: Future[None, Task[None]] = Future()
        async def wait_for_send_to_complete() -> None:
            assert task_manager is not None
            for task in Task.sort(future.resolve(None)):
                task_manager.queue(task)
       
        task = Task(wait_for_send_to_complete())
        task_manager.queue(task)
        await future


E = TypeVar('E', bound=Event)


EventSentCallback = Callable[[TaskManager, E], Optional[Task[E]]]
