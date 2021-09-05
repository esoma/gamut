
from __future__ import annotations
# gamut
from gamut.event import Event
from gamut.event._task import Task, TaskStatus
from gamut.event._taskmanager import TaskManager
# python
from typing import Generator, Type, Union
# pytest
import pytest


class EventA(Event):
    pass

class EventB(Event):
    pass


@pytest.fixture
def task_manager() -> Generator[TaskManager, None, None]:
    with TaskManager() as task_manager:
        yield task_manager


@pytest.mark.parametrize("event_class", [EventA, EventB])
def test_two_events(
    task_manager: TaskManager,
    event_class: Type[Event]
) -> None:
    async def func() -> Union[EventA, EventB]:
        return await (EventA | EventB)
    task = Task(func())
    task_manager.queue(task)

    task_manager.run()
    assert task.status == TaskStatus.WORKING

    event = event_class()
    event.send()

    task_manager.run()
    assert task.status == TaskStatus.COMPLETE
    assert task.result is event
