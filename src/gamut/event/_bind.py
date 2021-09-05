
from __future__ import annotations

__all__ = ['Bind', 'BindKind', 'BindClosed']

# gamut
from ._event import Event, add_sent_callback, remove_sent_callback
from ._future import Future
from ._task import Task
from ._taskmanager import TaskManager, TaskManagerIgnoredException
# python
from enum import Enum
from typing import (Any, Callable, Coroutine, Generic, Optional, Type, TypeVar,
                    final)
from weakref import WeakSet


class BindClosed(TaskManagerIgnoredException):
    pass


class BindKind(Enum):
    ON = object()
    ONCE = object()
    MUTEX = object()

    _ONCE_USED = object()
    _CLOSED = object()


E = TypeVar('E', bound=Event)


BindCallback = Callable[[E], Coroutine[Future[E, Task[E]], None, Any]]


@final
class Bind(Generic[E]):
    """Bind objects allow for callbacks to be bound to Events. The callbacks
    are always coroutines that may await other Events or Futures.

    There are three kinds of binds as defined by BindKind:
        - ON: whenever the Event is sent the callback will be executed
        - ONCE: only the first time the Event is sent the callback will be
            executed
        - MUTEX: whenever the Event is sent the callback will be executed, but
            not if the callback is already executing via this bind

    Binds may be closed either manually using the "close" method or by using
    the Bind as a context manager. Once the Bind is closed it cannot be
    re-opened. A closed bind will no longer execute its callback when the
    Event is sent.
    """

    __slots__ = [
        '_event', '_callback', '_kind', '_tasks', '_bound_on_send',
        '__weakref__',
    ]

    def __init__(
        self,
        event: Type[E],
        callback: BindCallback[E],
        kind: BindKind
    ) -> None:
        assert kind is not BindKind._CLOSED
        # https://github.com/python/mypy/issues/9005
        self._kind: BindKind = kind
        # the following attributes are deleted when the kind is _CLOSED
        self._event = event
        self._callback = callback
        self._tasks: WeakSet[Task[Any]] = WeakSet()
        # since events store a weakref to the callback we need to keep a strong
        # reference to the bound version of this method, this creates a small
        # but manageable cycle that should be being broken by the close method
        # anyway
        self._bound_on_send = self._on_send
        add_sent_callback(event, self._bound_on_send)

    def __del__(self) -> None:
        self.close()

    def __enter__(self) -> Bind[E]:
        if self._kind == BindKind._CLOSED:
            raise RuntimeError('bind is already closed')
        return self

    def __exit__(self, *args: Any) -> None:
        self.close()

    def _on_send(
        self,
        task_manager: TaskManager,
        event: E
    ) -> Optional[Task[E]]:
        if self._kind == BindKind._ONCE_USED:
            return None
        if self._kind == BindKind.MUTEX and self._tasks:
            return None
        task = Task(self._callback(event))
        self._tasks.add(task)
        if self._kind == BindKind.ONCE:
            self._kind = BindKind._ONCE_USED
        return task

    def close(self) -> None:
        if self._kind == BindKind._CLOSED:
            return

        remove_sent_callback(self._event, self._on_send)
        self._kind = BindKind._CLOSED
        if self._tasks:
            task_manager = TaskManager.get_current()
            if not task_manager:
                raise RuntimeError(
                    'unable to close bind with unfinished tasks without an '
                    'active task manager'
                )
            for task in self._tasks:
                task.throw(BindClosed())
                task_manager.queue(task)

        del self._event
        del self._callback
        del self._tasks
        del self._bound_on_send

    @property
    def is_open(self) -> bool:
        return self._kind != BindKind._CLOSED

    @property
    def kind(self) -> BindKind:
        if self._kind == BindKind._CLOSED:
            raise RuntimeError('bind is closed')
        elif self._kind == BindKind._ONCE_USED:
            return BindKind.ONCE
        return self._kind

    @classmethod
    def on(cls, event: Type[E], callback: BindCallback[E]) -> Bind[E]:
        return Bind(event, callback, BindKind.ON)

    @classmethod
    def once(cls, event: Type[E], callback: BindCallback[E]) -> Bind[E]:
        return Bind(event, callback, BindKind.ONCE)

    @classmethod
    def mutex(cls, event: Type[E], callback: BindCallback[E]) -> Bind[E]:
        return Bind(event, callback, BindKind.MUTEX)
