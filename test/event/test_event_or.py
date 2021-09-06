
from __future__ import annotations
# gamut
from gamut.event import Event, OrEvents
from gamut.event._task import Task, TaskStatus
from gamut.event._taskmanager import TaskManager
# python
import gc
from itertools import product
from typing import Any, Generator, Type
# pytest
import pytest


class EventA(Event):
    pass

class EventB(Event):
    pass

class EventC(Event):
    pass

class EventD(Event):
    pass


@pytest.fixture
def task_manager() -> Generator[TaskManager, None, None]:
    with TaskManager() as task_manager:
        yield task_manager


@pytest.mark.parametrize("or_events,event_class", [
    *product(
        [
            EventA | EventB, OrEvents([EventA], [EventB]),
            EventB | EventA, OrEvents([EventB], [EventA])
        ],
        [EventA, EventB]
    ),
    *product(
        [
            (EventA | EventB) | EventC, OrEvents([EventA, EventB], [EventC]),
            EventA | (EventB | EventC), OrEvents([EventA], [EventB, EventC]),
        ],
        [EventA, EventB, EventC]
    ),
    *product(
        [
            (EventA | EventB) | (EventC | EventD),
            OrEvents([EventA, EventB], [EventC, EventD])
        ],
        [EventA, EventB, EventC, EventD]
    )
])
def test_send(
    task_manager: TaskManager,
    or_events: OrEvents[type[Event], type[Event]],
    event_class: Type[Event]
) -> None:
    async def func() -> Event:
        return await or_events
    task = Task(func())
    task_manager.queue(task)

    task_manager.run()
    assert task.status == TaskStatus.WORKING

    event = event_class()
    event.send()

    task_manager.run()
    assert task.status == TaskStatus.COMPLETE
    assert task.result is event


def test_created_inside_coro(task_manager: TaskManager) -> None:
    events: list[Event] = []
    async def func() -> None:
        events.append(await (EventA | EventB))
        events.append(await (EventA | EventB))
    task = Task(func())
    task_manager.queue(task)
    del func
    del task

    gc.collect()
    task_manager.run()
    assert not events

    event_1 = EventA()
    event_1.send()
    gc.collect()
    task_manager.run()
    assert len(events) == 1
    assert events[0] == event_1

    event_2 = EventA()
    event_2.send()
    gc.collect()
    task_manager.run()
    assert len(events) == 2
    assert events[0] == event_1
    assert events[1] == event_2


def test_created_inside_other_coro(task_manager: TaskManager) -> None:
    events: list[Event] = []
    async def other_func() -> None:
        events.append(await (EventA | EventB))
        events.append(await (EventA | EventB))
    async def func(other_func: Any) -> None:
        await other_func()
    task = Task(func(other_func))
    task_manager.queue(task)
    del other_func
    del func
    del task

    gc.collect()
    task_manager.run()
    assert not events

    event_1 = EventA()
    event_1.send()
    gc.collect()
    task_manager.run()
    assert len(events) == 1
    assert events[0] == event_1

    event_2 = EventA()
    event_2.send()
    gc.collect()
    task_manager.run()
    assert len(events) == 2
    assert events[0] == event_1
    assert events[1] == event_2


def test_event_or_invalid_type() -> None:
    with pytest.raises(TypeError) as excinfo:
        Event | 1 # type: ignore
    assert str(excinfo.value) == (
        f'unsupported operand type(s) for |: '
        f'\'Event\' and \'int\''
    )


def test_or_events_or_invalid_type() -> None:
    with pytest.raises(TypeError) as excinfo:
        (EventA | EventB) | 1 # type: ignore
    assert str(excinfo.value) == (
        f'unsupported operand type(s) for |: '
        f'\'OrEvents\' and \'int\''
    )
