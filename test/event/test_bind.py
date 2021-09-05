
from __future__ import annotations
# gamut
from gamut.event import Bind, BindClosed, BindKind, Event
from gamut.event._taskmanager import TaskManager
# python
import gc
from typing import Generator
import weakref
# pytest
import pytest


@pytest.fixture
def task_manager() -> Generator[TaskManager, None, None]:
    with TaskManager() as task_manager:
        yield task_manager


def test_instantiate_on() -> None:
    async def callback(event: Event) -> None:
        return None
    bind = Bind.on(Event, callback)
    assert bind.kind is BindKind.ON


def test_instantiate_once() -> None:
    async def callback(event: Event) -> None:
        return None
    bind = Bind.once(Event, callback)
    assert bind.kind is BindKind.ONCE


def test_instantiate_mutex() -> None:
    async def callback(event: Event) -> None:
        return None
    bind = Bind.mutex(Event, callback)
    assert bind.kind is BindKind.MUTEX


@pytest.mark.parametrize("bind_kind", [
    BindKind.ON,
    BindKind.ONCE,
    BindKind.MUTEX
])
def test_close(bind_kind: BindKind) -> None:
    async def callback(event: Event) -> None:
        return None
    bind = Bind(Event, callback, bind_kind)
    assert bind.is_open
    assert bind.kind is bind_kind

    for _ in range(2):
        bind.close()
        assert not bind.is_open
        with pytest.raises(RuntimeError) as excinfo:
            bind.kind
        assert str(excinfo.value) == 'bind is closed'


@pytest.mark.parametrize("bind_kind", [
    BindKind.ON,
    BindKind.ONCE,
    BindKind.MUTEX
])
def test_context_maanger_close(bind_kind: BindKind) -> None:
    async def callback(event: Event) -> None:
        return None
    with Bind(Event, callback, bind_kind) as bind:
        assert bind.is_open
        assert bind.kind is bind_kind

    assert not bind.is_open
    with pytest.raises(RuntimeError) as excinfo:
        bind.kind
    assert str(excinfo.value) == 'bind is closed'


@pytest.mark.parametrize("bind_kind", [
    BindKind.ON,
    BindKind.ONCE,
    BindKind.MUTEX
])
def test_context_manager_already_closed(bind_kind: BindKind) -> None:
    async def callback(event: Event) -> None:
        return None
    bind = Bind(Event, callback, bind_kind)
    bind.close()

    with pytest.raises(RuntimeError) as excinfo:
        with bind:
            pass
    assert str(excinfo.value) == 'bind is already closed'


@pytest.mark.parametrize("simultaneous_event_count", [1, 2, 5, 10])
def test_on_event(
    task_manager: TaskManager,
    simultaneous_event_count: int
) -> None:
    callbacks: list[Event] = []
    async def callback(event: Event) -> None:
        callbacks.append(event)
    bind = Bind.on(Event, callback)

    task_manager.run()
    assert not callbacks

    events = [Event() for _ in range(simultaneous_event_count)]
    for event in events:
        event.send()
    task_manager.run()
    assert callbacks == events


@pytest.mark.parametrize("simultaneous_event_count", [1, 2, 5, 10])
def test_once_event(
    task_manager: TaskManager,
    simultaneous_event_count: int
) -> None:
    callbacks: list[Event] = []
    async def callback(event: Event) -> None:
        callbacks.append(event)
    bind = Bind.once(Event, callback)

    task_manager.run()
    assert not callbacks

    events = [Event() for _ in range(simultaneous_event_count)]
    for event in events:
        event.send()
        task_manager.run()
    assert callbacks == events[:1]


@pytest.mark.parametrize("simultaneous_event_count", [1, 2, 5, 10])
def test_mutex_event(
    task_manager: TaskManager,
    simultaneous_event_count: int
) -> None:
    callbacks: list[Event] = []
    async def callback(event: Event) -> None:
        callbacks.append(event)
    bind = Bind.mutex(Event, callback)

    task_manager.run()
    assert not callbacks

    for _ in range(5):
        callbacks.clear()
        events = [Event() for _ in range(simultaneous_event_count)]
        for event in events:
            event.send()
        task_manager.run()
        assert callbacks == events[:1]


@pytest.mark.parametrize("bind_kind", [
    BindKind.ON,
    BindKind.ONCE,
    BindKind.MUTEX
])
def test_closed_before_event(
    task_manager: TaskManager,
    bind_kind: BindKind
) -> None:
    callbacks: list[Event] = []
    async def callback(event: Event) -> None:
        callbacks.append(event)
    bind = Bind(Event, callback, bind_kind)

    task_manager.run()
    assert not callbacks

    bind.close()
    Event().send()
    task_manager.run()
    assert callbacks == []


@pytest.mark.parametrize("bind_kind", [
    BindKind.ON,
    BindKind.ONCE,
    BindKind.MUTEX
])
def test_closed_after_event_before_ran(
    task_manager: TaskManager,
    bind_kind: BindKind
) -> None:
    callbacks: list[Event] = []
    async def callback(event: Event) -> None:
        callbacks.append(event)
    bind = Bind(Event, callback, bind_kind)

    task_manager.run()
    assert not callbacks

    Event().send()
    bind.close()
    task_manager.run()
    assert not callbacks


@pytest.mark.filterwarnings('ignore: future expired before being resolved')
@pytest.mark.filterwarnings('ignore: future expired while blocking')
@pytest.mark.parametrize("bind_kind", [
    BindKind.ON,
    BindKind.ONCE,
    BindKind.MUTEX
])
def test_closed_while_running(
    task_manager: TaskManager,
    bind_kind: BindKind
) -> None:
    exceptions: list[BaseException] = []
    class SomeEvent(Event):
        pass
    async def callback(event: Event) -> None:
        try:
            await SomeEvent
        except BaseException as ex:
            exceptions.append(ex)
    bind = Bind(Event, callback, bind_kind)

    Event().send()
    task_manager.run()
    assert not exceptions

    bind.close()
    task_manager.run()
    assert len(exceptions) == 1
    assert isinstance(exceptions[0], BindClosed)


@pytest.mark.parametrize("bind_kind", [
    BindKind.ON,
    BindKind.ONCE,
    BindKind.MUTEX
])
def test_gc(bind_kind: BindKind) -> None:
    async def callback(event: Event) -> None:
        return None
    bind = Bind(Event, callback, bind_kind)
    weak_bind = weakref.ref(bind)
    del bind
    gc.collect()
    assert weak_bind() is None
