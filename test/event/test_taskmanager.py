
from __future__ import annotations

# gamut
from gamut.event._future import Future
from gamut.event._task import Task, TaskStatus
from gamut.event._taskmanager import TaskManager, TaskManagerIgnoredException
# pytest
import pytest
# python
import gc
from typing import Generator
import warnings


class Result:
    pass


@pytest.fixture
def task_manager() -> Generator[TaskManager, None, None]:
    with TaskManager() as task_manager:
        yield task_manager


def test_close() -> None:
    task_manager = TaskManager()
    assert task_manager.is_open is True
    
    task_manager.close()
    assert task_manager.is_open is False


def test_current() -> None:
    assert TaskManager.get_current() is None
    
    with TaskManager() as task_manager:
        assert TaskManager.get_current() is task_manager

    assert TaskManager.get_current() is None
    

def test_current_multiple() -> None:
    task_manager = TaskManager()
    with task_manager:
        with pytest.raises(RuntimeError) as excinfo:
            with task_manager:
                pass
        assert str(excinfo.value) == 'there is already an active task manager'
        

def test_current_exit_out_of_order() -> None:
    inactive_task_manager = TaskManager()
    with TaskManager() as active_task_manager:
        with pytest.raises(RuntimeError) as excinfo:
            inactive_task_manager.__exit__()
        assert str(excinfo.value) == 'active task manager isn''t this one'
        assert TaskManager.get_current() is active_task_manager
        

def test_run_task(task_manager: TaskManager) -> None:
    async def func() -> Result:
        return Result()
        
    task = Task(func())
    task_manager.queue(task)
    
    task_manager.run()
    assert task.status is TaskStatus.COMPLETE
    
    
@pytest.mark.parametrize("run_wait_count", [1, 2, 10])
def test_run_task_wait_on_future(
    task_manager: TaskManager,
    run_wait_count: int
) -> None:
    future: Future[Result, Task[Result]] = Future()
    async def func() -> Result:
        return await future
        
    task = Task(func())
    task_manager.queue(task)
    
    for i in range(run_wait_count):
        task_manager.run()
        assert task.status is TaskStatus.WORKING
        
    for task in Task.sort(future.resolve(Result())):
        task_manager.queue(task)
    task_manager.run()
    assert task.status is TaskStatus.COMPLETE


def test_run_completed_task(task_manager: TaskManager) -> None:
    async def func() -> Result:
        return Result()
        
    task = Task(func())
    task_manager.queue(task)
    
    task_manager.run()
    assert task.status is TaskStatus.COMPLETE
    
    task_manager.queue(task)
    task_manager.run()

    
def test_run_error(task_manager: TaskManager) -> None:
    exception = Exception('test')
    async def func() -> Result:
        raise exception
        
    task = Task(func())
    task_manager.queue(task)
    
    with pytest.raises(Exception) as excinfo:
        task_manager.run()
    assert excinfo.value is exception


def test_run_ignored_error(task_manager: TaskManager) -> None:
    async def func() -> Result:
        raise TaskManagerIgnoredException('test')
        
    task = Task(func())
    task_manager.queue(task)
    
    task_manager.run()
    assert task.status is TaskStatus.ERROR
    
    
def test_run_order(task_manager: TaskManager) -> None:
    order: list[int] = []
    async def func(id: int) -> Result:
        order.append(id)
        return Result()
        
    task_manager.queue(Task(func(1)))
    task_manager.queue(Task(func(2)))
    task_manager.queue(Task(func(3)))
    task_manager.queue(Task(func(4)))
    
    task_manager.run()
    
    assert order == [1, 2, 3, 4]
    
    
def test_run_unblocked_order(task_manager: TaskManager) -> None:
    order: list[int] = []
    future_1: Future[Result, Task[Result]] = Future()
    future_2: Future[Result, Task[Result]] = Future()
    async def func(id: int, future: Future[Result, Task[Result]]) -> Result:
        result = await future
        order.append(id)
        return result
        
    task_manager.queue(Task(func(1, future_1)))
    task_manager.queue(Task(func(3, future_2)))
    task_manager.queue(Task(func(2, future_1)))
    task_manager.queue(Task(func(4, future_2)))
    
    task_manager.run()
    for task in Task.sort(future_1.resolve(Result())):
        task_manager.queue(task)
    for task in Task.sort(future_2.resolve(Result())):
        task_manager.queue(task)

    task_manager.run()
    
    assert order == [1, 2, 3, 4]
    

@pytest.mark.filterwarnings('ignore: coroutine '
                            '\'test_queue_closed.<locals>.func\' was never '
                            'awaited')
@pytest.mark.filterwarnings('ignore: task expired while still working')
def test_queue_closed(task_manager: TaskManager) -> None:
    async def func() -> Result:
        return Result()
    task_manager.close()
    
    with pytest.raises(RuntimeError) as excinfo:
        task_manager.queue(Task(func()))
    assert str(excinfo.value) == 'task manager is closed'
    

def test_run_closed(task_manager: TaskManager) -> None:
    task_manager.close()
    
    with pytest.raises(RuntimeError) as excinfo:
        task_manager.run()
    assert str(excinfo.value) == 'task manager is closed'
