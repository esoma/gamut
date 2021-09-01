
from __future__ import annotations

# gamut
from gamut.event._future import Future
from gamut.event._task import Task, TaskStatus
# pytest
import pytest
# python
import gc
from typing import Any, Generator, TypeVar
import warnings


T = TypeVar('T')


class Result:
    pass


@pytest.mark.filterwarnings('ignore: coroutine '
                            '\'test_initial_state.<locals>.func\' was never '
                            'awaited')
@pytest.mark.filterwarnings('ignore: task expired while still working')
def test_initial_state() -> None:
    async def func() -> Result:
        return Result()
    
    task = Task(func())
    
    assert task.status is TaskStatus.WORKING
    with pytest.raises(AttributeError):
        task.result
    with pytest.raises(AttributeError):
        task.exception


def test_run_with_immediate_return() -> None:
    result = Result()
    async def func() -> Result:
        return result
    
    task = Task(func())
    
    task.run()
    assert task.status is TaskStatus.COMPLETE
    assert task.result is result
    with pytest.raises(AttributeError):
        task.exception


@pytest.mark.parametrize("block_count", [0, 1, 2, 10])
def test_run_await_future(block_count: int) -> None:
    future: Future[Result, Task[Result]] = Future()
    async def func() -> Result:
        return await future
        
    task = Task(func())
    
    for i in range(block_count):
        task.run()
        assert task.status == TaskStatus.WORKING
        with pytest.raises(AttributeError):
            task.result
        with pytest.raises(AttributeError):
            task.exception
        
    result = Result()
    future.resolve(result)
    task.run()
    assert task.status is TaskStatus.COMPLETE
    assert task.result is result
    with pytest.raises(AttributeError):
        task.exception


def test_run_complete() -> None:    
    result = Result()
    async def func() -> Result:
        return result
    
    task = Task(func())
    task.run()
    
    with pytest.raises(RuntimeError) as excinfo:
        task.run()
    assert str(excinfo.value) == 'task has nothing more to do'
    
    
def test_run_raises_exception() -> None:
    exception = Exception('test')
    async def func() -> Result:
        raise exception
    
    task = Task(func())
    
    with pytest.raises(Exception) as excinfo:
        task.run()
    assert excinfo.value is exception
        
    assert task.status is TaskStatus.ERROR
    with pytest.raises(AttributeError):
        task.result
    assert task.exception is exception
    
    
def test_throw() -> None:
    async def func() -> Result:
        return Result()
    
    task = Task(func())
    
    exception = Exception('test')
    task.throw(exception)
    assert task.status is TaskStatus.WORKING
    with pytest.raises(AttributeError):
        task.result
    with pytest.raises(AttributeError):
        task.exception
    
    with pytest.raises(Exception) as excinfo:
        task.run()
    assert excinfo.value is exception
        
    # https://github.com/python/mypy/issues/9005
    assert task.status is TaskStatus.ERROR # type: ignore  
    with pytest.raises(AttributeError):
        task.result
    assert task.exception is exception
    
    
def test_throw_already_complete() -> None:
    async def func() -> Result:
        return Result()
    
    task = Task(func())
    task.run()
    
    with pytest.raises(RuntimeError) as excinfo:
        task.throw(Exception())
    assert str(excinfo.value) == 'task has nothing more to do'
    
    
def test_throw_already_error() -> None:
    async def func() -> Result:
        return Result()
    
    task = Task(func())
    task.throw(Exception())
    try:
        task.run()
    except Exception:
        pass
    
    with pytest.raises(RuntimeError) as excinfo:
        task.throw(Exception())
    assert str(excinfo.value) == 'task has nothing more to do'
    

@pytest.mark.filterwarnings('ignore: future expired before being resolved')
@pytest.mark.filterwarnings('ignore: future expired while blocking')    
@pytest.mark.filterwarnings('ignore: task expired while still working')
@pytest.mark.parametrize("task_count", [0, 1, 2, 10])
def test_sort(task_count: int) -> None:
    future: Future[Result, Task[Result]] = Future()
    async def func() -> Result:
        return await future

    tasks = [Task(func()) for i in range(task_count)]
    for task in tasks:
        task.run()
        
    sorted_tasks = list(Task.sort(reversed(tasks)))
    assert len(sorted_tasks) == task_count
    assert all(
        expected is result
        for expected, result in zip(tasks, sorted_tasks)
    )
