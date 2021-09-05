
from __future__ import annotations

__all__ = ['Application', 'ApplicationEnd', 'ApplicationStart']

# gamut
from ._event import Event
from ._task import Task, TaskStatus
from ._taskmanager import TaskManager
# python
from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

R = TypeVar('R')


class ApplicationStart(Event):
    application: Application[Any]


class ApplicationEnd(Event):
    application: Application[Any]


class Application(ABC, Generic[R]):

    Start = ApplicationStart
    End = ApplicationEnd

    def run(self, *args: Any, **kwargs: Any) -> R:
        with TaskManager() as task_manager:
            main_task: Task[R] = Task(self.__main(*args, **kwargs))
            task_manager.queue(main_task)

            while True:
                task_manager.run()
                if main_task.status == TaskStatus.COMPLETE:
                    return main_task.result
                elif main_task.status == TaskStatus.ERROR:
                    raise main_task.exception
                assert main_task.status == TaskStatus.WORKING

    async def __main(self, *args: Any, **kwargs: Any) -> R:
        await self.Start(self).asend()
        result = await self.main(*args, **kwargs)
        await self.End(self).asend()
        return result

    @abstractmethod
    async def main(self, *args: Any, **kwargs: Any) -> R:
        raise NotImplementedError()
