
from __future__ import annotations

__all__ = ['TaskManager', 'TaskManagerIgnoredException']

# gamut
from ._task import Task, TaskStatus
# python
from collections import deque
from typing import Any, ClassVar, final, Optional, TypeVar

T = TypeVar('T')


class TaskManagerIgnoredException(Exception):
    """Exceptions of this type will be ignored by the TaskManager when they
    are raised within a Task it is executing.
    """


@final
class TaskManager:
    """TaskManager objects maintain set of queued up Tasks that should be
    executed.

    A TaskManager has two states "open" and "closed". A TaskManager start in
    the "open" state and may be used normally. Once a TaskManager is "closed"
    using the "close" method it may no longer be used.

    The TaskManager has the concept of a "current" TaskManager. This is a
    global state managed by using the TaskManager as a context manager. Only
    one TaskManager may be the "current" one. This "current" TaskManager is
    accessible via the "get_current" class method.

    The "run" method executes all tasks in the order that they were queued.
    Tasks may be queued multiple times in any state. After the Task is no
    longer in the working state it will simply be passed over.
    """

    __slots__ = ['_queue']

    _current: ClassVar[Optional[TaskManager]] = None

    def __init__(self) -> None:
        self._queue: Optional[deque[Task[Any]]] = deque()

    def __del__(self) -> None:
        self.close()

    def __enter__(self) -> TaskManager:
        if self.__class__._current:
            raise RuntimeError('there is already an active task manager')

        self.__class__._current = self
        return self

    def __exit__(self, *args: Any) -> Any:
        if self.__class__._current is not self:
            raise RuntimeError('active task manager isn''t this one')

        self.__class__._current = None

    def close(self) -> None:
        self._queue = None

    def queue(self, task: Task[T]) -> None:
        if self._queue is None:
            raise RuntimeError('task manager is closed')

        self._queue.append(task)

    def run(self) -> None:
        if self._queue is None:
            raise RuntimeError('task manager is closed')

        while True:
            try:
                task = self._queue.popleft()
            except IndexError:
                return
            if task.status == TaskStatus.WORKING:
                try:
                    task.run()
                except TaskManagerIgnoredException:
                    pass

    @property
    def is_open(self) -> bool:
        return self._queue is not None

    @classmethod
    def get_current(cls) -> Optional[TaskManager]:
        return cls._current
