
from __future__ import annotations

__all__ = [
    'Application',
    'ApplicationEnd',
    'ApplicationEvent',
    'ApplicationStart',
]

# gamut
from ._bind import Bind
from ._event import Event as BaseEvent
from ._task import Task, TaskStatus
from ._taskmanager import TaskManager
# python
from abc import ABC, abstractmethod
from typing import Any, Generic, Optional, TypeVar

R = TypeVar('R')


class ApplicationEvent(BaseEvent, application=...):
    application: Application[Any]


class ApplicationStart(ApplicationEvent, application=...):
    pass


class ApplicationEnd(ApplicationEvent, application=...):
    pass


class Application(ABC, Generic[R]):

    Event: type[ApplicationEvent]
    Start: type[ApplicationStart]
    End: type[ApplicationEnd]

    def __init__(self) -> None:
        super().__init__()
        class Event(ApplicationEvent, application=self):
            pass
        self.Event = Event
        class Start(Event, ApplicationStart):
            pass
        self.Start = Start
        class End(Event, ApplicationEnd):
            pass
        self.End = End
        class _OutOfEvents(Event):
            pass
        self._OutOfEvents = _OutOfEvents

    def run(self) -> R:
        with (
            TaskManager() as task_manager,
            Bind.mutex(self._OutOfEvents, self.__poll)
        ):
            main_task: Task[R] = Task(self.__main())
            task_manager.queue(main_task)

            while True:
                task_manager.run()
                if main_task.status == TaskStatus.COMPLETE:
                    return main_task.result
                assert main_task.status == TaskStatus.WORKING
                self._OutOfEvents().send()

    async def __main(self) -> R:
        await self.Start().asend()
        result = await self.main()
        await self.End().asend()
        return result

    @abstractmethod
    async def main(self) -> R:
        raise NotImplementedError()

    async def __poll(self, _: BaseEvent) -> None:
        event = await self.poll()
        if event:
            await event.asend()

    async def poll(self) -> Optional[BaseEvent]:
        return None
