
from __future__ import annotations
# gamut
from gamut.event import Event, OrEvents
from gamut.event._task import Task, TaskStatus
from gamut.event._taskmanager import TaskManager
# python
from itertools import product
from typing import Generator, Type
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
