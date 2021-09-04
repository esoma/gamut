
from __future__ import annotations

__all__ = ['Future']

# python
from typing import Generator, Generic, Hashable, TypeVar, final
from warnings import warn

T = TypeVar('T')
B = TypeVar('B', bound=Hashable)


@final
class Future(Generic[T, B]):
    """Future objects are containers for a result that will be available in the
    future.

    Futures have two states: "not ready" and "ready" which can be accessed with
    the "is_ready" property.

    Futures start in the "not ready" state. In this state awaiting on the
    Future will forever yield the Future instance itself. The Future may track
    objects that it is blocking the execution of (typically an coroutine that
    is waiting on the future) using the "block" method.

    The Future may be moved to the "ready" state by using the "resolve" method
    which sets the "result" property and returns the set of objects that were
    waiting on the Future. Once the Future is in the "ready" state awaiting on
    it will instead return the value of the "result".

    Once a Future has been moved to the "ready" state it may not block any new
    objects or be resolved again. It is effectivley done with.
    """

    __slots__ = ['_blocking', '_is_ready', '_result']

    # note that result shouldn't be set until _is_ready is True so that any
    # any access prior will produce an AttributeError
    _result: T

    def __init__(self) -> None:
        self._is_ready = False
        self._blocking: set[B] = set()

    def __await__(self) -> Generator[Future[T, B], None, T]:
        while not self._is_ready:
            yield self
        return self._result

    def __del__(self) -> None:
        if not self._is_ready:
            warn(f'future expired before being resolved: {self!r}')
            if self._blocking:
                warn(f'future expired while blocking: {self!r}')

    def __repr__(self) -> str:
        if self._is_ready:
            return f'<gamut.Future result={self.result!r}>'
        else:
            return f'<gamut.Future is_ready=False>'

    def resolve(self, value: T) -> set[B]:
        if self._is_ready:
            raise RuntimeError('future is already resolved')
        self._is_ready = True
        self._result = value

        blocking = self._blocking
        del self._blocking
        return blocking

    def block(self, blockable: B) -> None:
        if self._is_ready:
            raise RuntimeError('future is already resolved')
        self._blocking.add(blockable)

    @property
    def is_ready(self) -> bool:
        return self._is_ready

    @property
    def result(self) -> T:
        return self._result
