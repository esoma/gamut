
from __future__ import annotations

__all__ = ['Event', 'OrEvents']

# gamut
from ._future import Future
from ._task import Task
from ._taskmanager import TaskManager
# python
import inspect
from typing import (Any, Callable, ClassVar, Generator, Generic, get_origin,
                    Optional, overload, Type, TypeVar, Union)
from weakref import WeakSet

# there is a lot of hackery going on in this set of classes regarding the
# typing system, see:
# see: https://github.com/DVector4/typing/issues/715

# roughly, all these type ignores and strange use of TypeVars are because we
# know that the only class using EventType is Event


T = TypeVar('T')
T2 = TypeVar('T2')
T3 = TypeVar('T3')
E = TypeVar('E', bound='Event')
ET = TypeVar('ET', bound='Type[Event]')
ET2 = TypeVar('ET2', bound='Type[Event]')
ET3 = TypeVar('ET3', bound='Type[Event]')


class EventType(type):
    """The EventType metaclass serves a few purposes for the Event class:

    - it makes the Event class itself awaitable
    - it makes the Event class itself OR-able to create OrEvents objects
    - it does some minor setup
    """

    _all: WeakSet[Type[EventType]] = WeakSet()

    def __new__(cls, name, bases, attrs, **kwds): # type: ignore
        cls = super().__new__(cls, name, bases, attrs, **kwds)
        cls._future = None
        cls._sent_callbacks = WeakSet()
        cls._all.add(cls)
        return cls

    @overload # type: ignore
    def __or__(cls: ET, other: ET2) -> OrEvents[ET, ET2]: # type: ignore
        ...

    @overload
    def __or__( # type: ignore
        cls: ET,
        other: OrEvents[T2, T3] # type: ignore
    ) -> OrEvents[ET, Union[T2, T3]]: # type: ignore
        ...

    @overload
    def __or__(cls: T, other: T2) -> Union[T, T2]:
        ...

    def __or__(cls, other): # type: ignore
        try:
            other_is_event = issubclass(other, Event)
        except TypeError:
            other_is_event = False
        if other_is_event:
            class _(metaclass=OrEvents, events=[cls, other]):
                pass
            return _
        elif isinstance(other, OrEvents):
            class _(metaclass=OrEvents, events=[cls, *other._events]):
                pass
            return _
        return Union[cls, other]

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


class OrEvents(Generic[ET, ET2], type):
    """OrEvents provide a way to await on multiple Events, only catching the
    first one that is sent.

    Typically this is not instantiated directly by
    the user, instead the bitwise OR operator is used to create one:

    EventAorB = EventA | EventB

    This class also acts like a typing Union, so that ORing Events together
    may still be used with isinstance.
    """

    def __new__(cls, name, bases, attrs, events): # type: ignore
        cls = super().__new__(cls, name, bases, attrs)
        cls._bound_sent: EventSentCallback
        cls._events: set[Type[Event]] = set(events)
        cls._future: Optional[Future[
            Union[T, T2],
            Task[Union[T, T2]]
        ]] = None
        return cls

    def __instancecheck__(cls, instance: Any) -> bool:
        return isinstance(instance, tuple(cls._events))

    @overload # type: ignore
    def __or__(cls, other: ET3) -> OrEvents[Union[ET, ET2], ET3]:
        ...

    @overload
    def __or__( # type: ignore
        cls,
        other: OrEvents[T, T2] # type: ignore
    ) -> OrEvents[Union[ET, ET2], Union[T, T2]]: # type: ignore
        ...

    @overload
    def __or__(cls, other: T2) -> Union[ET, ET2, T2]:
        ...

    def __or__(cls, other): # type: ignore
        try:
            other_is_event = issubclass(other, Event)
        except TypeError:
            other_is_event = False
        if other_is_event:
            class _(metaclass=OrEvents, events=[*cls._events, other]):
                pass
            return _
        elif isinstance(other, OrEvents):
            class _(metaclass=OrEvents, events=[*cls._events, *other._events]):
                pass
            return _
        union = Union[other]
        for event in cls._events:
            union = Union[event, union]
        return union

    def __await__(
        cls: OrEvents[Type[T], Type[T2]] # type: ignore
    ) -> Generator[
        Future[Union[T, T2], Task[Union[T, T2]]],
        None,
        Union[T, T2]
    ]:
        if cls._future is None:
            cls._future = Future()
            # since events store a weakref to the callback we need to keep a
            # strong reference to the bound version of this method, this
            # creates a small but manageable cycle that is broken by _sent
            # itself
            cls._bound_sent = cls._sent
            for event in cls._events:
                add_sent_callback(event, cls._bound_sent)
        return cls._future.__await__()

    def _sent(
        cls,
        task_manager: TaskManager,
        event: Event
    ) -> Optional[Task[Event]]:
        # this is basically equivalent to calling remove_sent_callback,
        # except that we don't cause an error by mutating the set which is
        # currently being iterated over
        assert isinstance(event, tuple(cls._events))
        del cls._bound_sent
        task = Task(cls._resolve(event)) # type: ignore
        return task

    async def _resolve(
        cls: OrEvents[Type[T], Type[T2]], # type: ignore
        event: Union[T, T2]
    ) -> None:
        task_manager = TaskManager.get_current()
        assert task_manager is not None
        assert cls._future is not None
        future = cls._future
        cls._future = None
        tasks = future.resolve(event)
        for task in Task.sort(tasks):
            task_manager.queue(task)


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
    _prototype_fields: ClassVar[list[str]] = []

    class _NonStaticType(type):
        def __repr__(cls) -> str:
            return '<NonStatic>'

    class _NonStatic(metaclass=_NonStaticType):
        pass

    def __init_subclass__(cls, **kwargs: Any) -> None: # type: ignore
        # we need to build the _fields data structure for this specific class,
        # start by generating it from the fields in the base classes
        #
        # we don't want to copy the actual value yet from the base classes so
        # that we can do error checking, this is just to get the order correct
        fields: dict[str, Any] = {}
        prototype_fields: list[str] = []
        for base in cls.__bases__:
            if not issubclass(base, Event):
                continue
            for key in base._fields:
                fields[key] = cls._NonStatic
        # now we can add any of the annotations defined directly on this class
        # so that they come after any base fields
        fields.update({
            k: cls._NonStatic
            for k, v in cls.__annotations__.items()
            if k not in fields
            if get_origin(v) is not ClassVar
            if not (isinstance(v, str) and v.startswith((
                'ClassVar',
                'typing.ClassVar',
                'typing_extensions.ClassVar',
            )))
        })
        # now we can apply static values to any class fields
        original_kwargs = dict(kwargs)
        for k in fields:
            try:
                kwarg_value = kwargs.pop(k)
            except KeyError:
                continue
            if kwarg_value is ...:
                prototype_fields.append(k)
            else:
                fields[k] = kwarg_value
        # now we travel the class inheritance graph, ignoring this class since
        # we've already procesed it
        for mro_cls in inspect.getmro(cls):
            if mro_cls is cls or not issubclass(mro_cls, Event):
                continue
            # we copy any field values from our parent classes in mro
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
        # check if there are any prototype fields for the parent classes that
        # weren't provided
        required_kwargs: list[str] = []
        for base in cls.__bases__:
            if not issubclass(base, Event):
                continue
            required_kwargs += base._prototype_fields
        missing_kwargs: list[str] = [
            f for f in required_kwargs
            if f not in original_kwargs
            if fields[f] is cls._NonStatic
        ]
        if missing_kwargs:
            missing_kwargs.sort()
            raise TypeError(
                f'missing required keyword-only argument(s): ' +
                ', '.join(missing_kwargs)
            )

        cls._fields = fields
        cls._prototype_fields = prototype_fields
        super().__init_subclass__(**kwargs)

    def __init__(self, *args: Any, **kwargs: Any) -> None: # type: ignore
        if self._prototype_fields:
            raise TypeError('cannot instantiate a prototype event')
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
        name = f'{type(self).__module__}.{type(self).__qualname__}'
        if name == 'gamut.event._event.Event':
            name = 'gamut.event.Event'
        fields = ' '.join(
            f'{"*" if v is not self._NonStatic else ""}'
            f'{k}={getattr(self, k)!r}'
            for k, v in self._fields.items()
        )
        if fields:
            fields = ' ' + fields
        return f'<{name}{fields}>'

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


EventSentCallback = Callable[[TaskManager, E], Optional[Task[E]]]
