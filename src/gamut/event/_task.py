
from __future__ import annotations

__all__ = ['Task', 'TaskStatus']

# python
from enum import Enum
from typing import Any, Coroutine, Generic, Iterable, Optional, TypeVar, final
from warnings import warn

# gamut
from ._future import Future

T = TypeVar('T')


last_order: int = 0
def next_order() -> int:
    global last_order
    last_order += 1
    return last_order


class TaskStatus(Enum):
    WORKING = object()
    COMPLETE = object()
    ERROR = object()


@final
class Task(Generic[T]):
    """Task objects are containers for the execution of a coroutine which await
    on Future objects.

    Tasks have three states:
        - TaskStatus.WORKING: the task's coroutine has not finished executing
        - TaskStatus.COMPLETE: the task's coroutine has finished executing and
            its return value is available via the "result" property
        - TaskStatus.ERROR: the task's coroutine has finished executing because
            an error occured and the error is available via the "exception"
            property

    The "run" method may only be used when the Task is in the working status.
    After the "run" method is executed the Task may have changed to the
    complete or error status.

    The "queue" method may be used to queue the Task for execution in the
    Task's TaskManager. THe "queue_batch" method is used to queue many Tasks
    at once in an internally specified order.

    The "throw" method may be used to induce an exception to be thrown by the
    Task's coroutine. Note that this method will also automatically queue up
    the Task. The Task must be in the working status.
    """

    __slots__ = [
        '_result', '_execution', '_status', '_thrown_exception',
        '_exception_to_throw', '_order',
        '__weakref__',
    ]

    _result: T
    _thrown_exception: Exception

    def __init__(self, coro: Coroutine[Future[T, Task[T]], Any, T]) -> None:
        # the order, relative to other tasks in which to unblock multiple tasks
        # on multiple futures
        self._order: int = 0
        # _execution stores the generator based on the coroutine we iterate
        # over to complete the task
        self._execution = coro.__await__()
        # status should only transition from WORKING to COMPLETE or ERROR
        self._status = TaskStatus.WORKING
        # if the status is ERROR then this will be populated, otherwise it
        # should always be None
        self._exception_to_throw: Optional[Exception] = None

    def __del__(self) -> None:
        if self._status == TaskStatus.WORKING:
            warn(f'task expired while still working: {self!r}')

    def __repr__(self) -> str:
        return f'<gamut.Task {id(self)} status={self._status}>'

    def run(self) -> None:
        if self._status != TaskStatus.WORKING:
            raise RuntimeError('task has nothing more to do')

        try:
            if self._exception_to_throw:
                exception_to_throw = self._exception_to_throw
                self._exception_to_throw = None
                try:
                    self._execution.throw(exception_to_throw)
                except StopIteration as ex:
                    self._status = TaskStatus.COMPLETE
                    self._result = ex.value
                    return
                assert False
        except Exception as ex:
            self._status = TaskStatus.ERROR
            self._thrown_exception = ex
            raise

        try:
            future: Future[T, Task[T]] = next(self._execution)
        except StopIteration as ex:
            self._status = TaskStatus.COMPLETE
            self._result = ex.value
            return
        except Exception as ex:
            self._status = TaskStatus.ERROR
            self._thrown_exception = ex
            raise

        self._order = next_order()
        future.block(self)

    @classmethod
    def sort(self, tasks: Iterable[Task[T]]) -> Iterable[Task[T]]:
        return sorted(tasks, key=lambda t: t._order)

    def throw(self, exception: Exception) -> None:
        if self._status != TaskStatus.WORKING:
            raise RuntimeError('task has nothing more to do')

        self._exception_to_throw = exception

    @property
    def status(self) -> TaskStatus:
        return self._status

    @property
    def result(self) -> T:
        return self._result

    @property
    def exception(self) -> Exception:
        return self._thrown_exception
