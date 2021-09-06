
from __future__ import annotations

__all__ = ['Application']

# gamut
from ._event import Event
from ._task import Task, TaskStatus
from ._taskmanager import TaskManager
# python
from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

R = TypeVar('R')


class Application(ABC, Generic[R]):

    class Start(Event):
        application: Application[Any]

    class End(Event):
        application: Application[Any]

    def run(self) -> R:
        with TaskManager() as task_manager:
            main_task: Task[R] = Task(self.__main())
            task_manager.queue(main_task)

            while True:
                task_manager.run()
                if main_task.status == TaskStatus.COMPLETE:
                    return main_task.result
                assert main_task.status == TaskStatus.WORKING

    async def __main(self) -> R:
        await self.Start(self).asend()
        result = await self.main()
        await self.End(self).asend()
        return result

    @abstractmethod
    async def main(self) -> R:
        raise NotImplementedError()
