
from __future__ import annotations

__all__ = [
    'EventLoop',
    'EventLoopEnd',
    'EventLoopEvent',
    'EventLoopStart',
]

# gamut
from ._bind import Bind
from ._event import Event as BaseEvent
from ._task import Task, TaskStatus
from ._taskmanager import TaskManager
# python
# DVector4
from abc import ABC, abstractmethod
from queue import Empty as QueueEmpty
from queue import Queue
from typing import Any, ContextManager, Generic, Optional, TypeVar

R = TypeVar('R')


class EventLoopEvent(BaseEvent, event_loop=...):
    event_loop: EventLoop[Any]


class EventLoopStart(EventLoopEvent, event_loop=...):
    pass


class EventLoopEnd(EventLoopEvent, event_loop=...):
    pass


class EventLoop(ABC, Generic[R]):

    Event: type[EventLoopEvent]
    Start: type[EventLoopStart]
    End: type[EventLoopEnd]

    def __init__(self) -> None:
        super().__init__()
        self._event_queue: Queue[BaseEvent] = Queue()
        class Event(EventLoopEvent, event_loop=self):
            pass
        self.Event = Event
        class Start(Event, EventLoopStart):
            pass
        self.Start = Start
        class End(Event, EventLoopEnd):
            pass
        self.End = End
        class _OutOfEvents(Event):
            pass
        self._OutOfEvents = _OutOfEvents

    def run_context(self) -> ContextManager:
        return DoNothingContextManager()

    def run(self) -> R:
        self._event_queue = Queue()
        with (
            TaskManager() as task_manager,
            Bind.mutex(self._OutOfEvents, self.__poll),
            self.run_context()
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

    async def poll(self, block: bool = True) -> Optional[BaseEvent]:
        try:
            return self._event_queue.get(block=block)
        except QueueEmpty:
            return None

    def queue_event(self, event: BaseEvent) -> None:
        self._event_queue.put(event)


class DoNothingContextManager:

    def __enter__(self) -> None:
        return None

    def __exit__(self, *args: Any) -> None:
        return None
