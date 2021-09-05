
from __future__ import annotations
# gamut
from gamut.event._future import Future
# python
import gc
# pytest
import pytest


class Blockable:
    pass


class Result:
    def __str__(self) -> str:
        return 'not the repr'

    def __repr__(self) -> str:
        return '<Result>'


@pytest.mark.filterwarnings('ignore: future expired before being resolved')
def test_initial_state() -> None:
    future: Future[Result, Blockable] = Future()

    assert next(future.__await__()) is future
    assert future.is_ready is False
    with pytest.raises(AttributeError):
        future.result


@pytest.mark.parametrize("blocked_count", [0, 1, 2, 10])
def test_resolve(blocked_count: int) -> None:
    result = Result()
    blocked = [Blockable() for i in range(blocked_count)]

    future: Future[Result, Blockable] = Future()
    for blockable in blocked:
        future.block(blockable)

    unblocked = future.resolve(result)
    assert future.is_ready is True
    assert future.result is result

    with pytest.raises(StopIteration) as excinfo:
        next(future.__await__())
    assert excinfo.value.value is result

    assert len(unblocked) == len(blocked)
    assert isinstance(unblocked, set)
    for blockable in blocked:
        assert blockable in unblocked


def test_repeated_blocking() -> None:
    blockable = Blockable()

    future: Future[Result, Blockable] = Future()
    future.block(blockable)
    future.block(blockable)

    unblocked = future.resolve(Result())

    assert len(unblocked) == 1
    assert blockable in unblocked


def test_already_resolved() -> None:
    future: Future[Result, Blockable] = Future()
    future.resolve(Result())

    with pytest.raises(RuntimeError):
        future.resolve(Result())

    with pytest.raises(RuntimeError):
        future.block(Blockable())


def test_expires_without_being_resolved() -> None:
    with pytest.warns(UserWarning) as warnings:
        Future()
        gc.collect()

    assert len(warnings) == 1
    assert str(warnings[0].message).startswith(
        'future expired before being resolved: '
    )


def test_expires_without_being_resolved_while_blocking() -> None:
    future: Future[Result, Blockable] = Future()
    future.block(Blockable())

    with pytest.warns(UserWarning) as warnings:
        del future
        gc.collect()

    assert len(warnings) == 2
    assert str(warnings[0].message).startswith(
        'future expired before being resolved: '
    )
    assert str(warnings[1].message).startswith(
        'future expired while blocking: '
    )


def test_not_ready_repr() -> None:
    future: Future[Result, Blockable] = Future()
    assert repr(future) == '<gamut.Future is_ready=False>'


def test_ready_repr() -> None:
    future: Future[Result, Blockable] = Future()
    future.resolve(Result())

    assert repr(future) == '<gamut.Future result=<Result>>'
