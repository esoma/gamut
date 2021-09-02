
from __future__ import annotations

# gamut
from gamut.event._task import Task, TaskStatus
from gamut.event._taskmanager import TaskManager
from gamut.event import Event
# pytest
import pytest
# python
from typing import Generator, Type


class EventSub(Event):
    pass
    
class EventSubSub1(EventSub):
    pass
    
class EventSubSub2(EventSub):
    pass
    
class EventSubSubCombined(EventSubSub1, EventSubSub2):
    pass


@pytest.fixture
def task_manager() -> Generator[TaskManager, None, None]:
    with TaskManager() as task_manager:
        yield task_manager


@pytest.mark.parametrize("receive_class, send_class", [
    [Event, Event],
    [Event, EventSub],
    [Event, EventSubSub1],
    [Event, EventSubSub2],
    [Event, EventSubSubCombined],
    [EventSub, EventSub],
    [EventSub, EventSubSub1],
    [EventSub, EventSubSub2],
    [EventSub, EventSubSubCombined],
    [EventSubSub1, EventSubSub1],
    [EventSubSub1, EventSubSubCombined],
    [EventSubSub2, EventSubSub2],
    [EventSubSub2, EventSubSubCombined],
    [EventSubSubCombined, EventSubSubCombined],
])
def test_send(
    task_manager: TaskManager,
    receive_class: Type[Event],
    send_class: Type[Event],
) -> None:
    async def func() -> Event:
        return await receive_class
    task = Task(func())
    task_manager.queue(task)
    
    task_manager.run()
    assert task.status is TaskStatus.WORKING

    event = send_class()
    event.send()
    
    task_manager.run()
    # https://github.com/python/mypy/issues/9005
    assert task.status is TaskStatus.COMPLETE # type: ignore  
    assert task.result is event


@pytest.mark.parametrize("receive_class, send_class", [
    [Event, Event],
    [Event, EventSub],
    [Event, EventSubSub1],
    [Event, EventSubSub2],
    [Event, EventSubSubCombined],
    [EventSub, EventSub],
    [EventSub, EventSubSub1],
    [EventSub, EventSubSub2],
    [EventSub, EventSubSubCombined],
    [EventSubSub1, EventSubSub1],
    [EventSubSub1, EventSubSubCombined],
    [EventSubSub2, EventSubSub2],
    [EventSubSub2, EventSubSubCombined],
    [EventSubSubCombined, EventSubSubCombined],
])
def test_asend(
    task_manager: TaskManager,
    receive_class: Type[Event],
    send_class: Type[Event],
) -> None:
    order: list[int] = []
    
    async def func() -> Event:
        event = await receive_class
        order.append(1)
        return event
    task = Task(func())
    task_manager.queue(task)
    
    task_manager.run()
    assert task.status is TaskStatus.WORKING
    
    event = send_class()
    async def func2() -> None:
        await event.asend()
        order.append(2)
    task2 = Task(func2())
    task_manager.queue(task2)
    
    task_manager.run()
    # https://github.com/python/mypy/issues/9005
    assert task.status is TaskStatus.COMPLETE # type: ignore  
    assert task.result is event
    assert task2.status is TaskStatus.COMPLETE
    assert task2.result is None
    assert order == [1, 2]


@pytest.mark.filterwarnings('ignore: future expired before being resolved')
@pytest.mark.filterwarnings('ignore: future expired while blocking')
@pytest.mark.filterwarnings('ignore: task expired while still working')
@pytest.mark.parametrize("receive_class, send_class", [
    [EventSub, Event],
    [EventSubSub1, Event],
    [EventSubSub2, Event],
    [EventSubSub1, EventSub],
    [EventSubSub2, EventSub],
    [EventSubSub1, EventSubSub2],
    [EventSubSub2, EventSubSub1],
    [EventSubSubCombined, Event],
    [EventSubSubCombined, EventSub],
    [EventSubSubCombined, EventSubSub1],
    [EventSubSubCombined, EventSubSub2],
])
def test_send_not_awaited(
    task_manager: TaskManager,
    receive_class: Type[Event],
    send_class: Type[Event],
) -> None:
    async def func() -> Event:
        return await receive_class
    task = Task(func())
    task_manager.queue(task)
    
    task_manager.run()
    assert task.status is TaskStatus.WORKING

    event = send_class()
    event.send()
    
    task_manager.run()
    assert task.status is TaskStatus.WORKING


@pytest.mark.filterwarnings('ignore: future expired before being resolved')
@pytest.mark.filterwarnings('ignore: future expired while blocking')
@pytest.mark.filterwarnings('ignore: task expired while still working')
@pytest.mark.parametrize("receive_class, send_class", [
    [EventSub, Event],
    [EventSubSub1, Event],
    [EventSubSub2, Event],
    [EventSubSub1, EventSub],
    [EventSubSub2, EventSub],
    [EventSubSub1, EventSubSub2],
    [EventSubSub2, EventSubSub1],
    [EventSubSubCombined, Event],
    [EventSubSubCombined, EventSub],
    [EventSubSubCombined, EventSubSub1],
    [EventSubSubCombined, EventSubSub2],
])
def test_asend_not_awaited(
    task_manager: TaskManager,
    receive_class: Type[Event],
    send_class: Type[Event],
) -> None:
    order: list[int] = []
    
    async def func() -> Event:
        event = await receive_class
        order.append(1)
        return event
    task = Task(func())
    task_manager.queue(task)
    
    task_manager.run()
    assert task.status is TaskStatus.WORKING
    
    event = send_class()
    async def func2() -> None:
        await event.asend()
        order.append(2)
    task2 = Task(func2())
    task_manager.queue(task2)
    
    task_manager.run()
    assert task.status is TaskStatus.WORKING
    assert task2.status is TaskStatus.COMPLETE
    assert task2.result is None
    assert order == [2]
