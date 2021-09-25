
from __future__ import annotations

__all__ = [
    'GamutApplication',
    'GamutApplicationEnd',
    'GamutApplicationStart',
    'GamutApplicationEvent',
]

# gamut
from gamut._sdl import sdl_event_callback_map
from gamut.event import (Application, ApplicationEnd, ApplicationEvent,
                         ApplicationStart, Bind)
from gamut.event import Event as BaseEvent
from gamut.peripheral import Keyboard, Mouse
# python
from ctypes import byref as c_byref
from typing import Any, ContextManager, Optional, TypeVar
# pysdl2
from sdl2 import (SDL_Event, SDL_GetError, SDL_Init, SDL_INIT_EVENTS,
                  SDL_PollEvent, SDL_QuitSubSystem, SDL_WaitEvent)

R = TypeVar('R')


class GamutApplicationEvent(ApplicationEvent, application=...):
    application: GamutApplication[Any]


class GamutApplicationStart(GamutApplicationEvent, ApplicationStart,
                            application=...):
    pass


class GamutApplicationEnd(GamutApplicationEvent, ApplicationEnd,
                          application=...):
    pass


class GamutApplication(Application[R]):

    Event: type[GamutApplicationEvent]
    Start: type[GamutApplicationStart]
    End: type[GamutApplicationEnd]

    def __init__(self) -> None:
        super().__init__()
        class Event(GamutApplicationEvent, self.Event): # type: ignore
            pass
        self.Event = Event
        class Start( # type: ignore
            GamutApplicationStart,
            Event,
            self.Start, # type: ignore
        ):
            pass
        self.Start = Start
        class End( # type: ignore
            GamutApplicationEnd,
            Event,
            self.End # type: ignore
        ):
            pass
        self.End = End

        self._mouse = Mouse('primary')
        self._keyboard = Keyboard('primary')

    def run_context(self) -> ContextManager:
        return GamutApplicationRunContext((
            Bind.on(self.Start, self._connect_peripherals),
            Bind.on(self.End, self._disconnect_peripherals),
        ))

    async def poll(self, block: bool = True) -> Optional[BaseEvent]:
        event = await super().poll()
        if event:
            return event
        return self._poll_sdl(block=block)

    @property
    def mouse(self) -> Mouse:
        return self._mouse

    @property
    def keyboard(self) -> Keyboard:
        return self._keyboard

    def _poll_sdl(self, block: bool) -> Optional[BaseEvent]:
        event = SDL_Event()
        if block:
            if SDL_WaitEvent(c_byref(event)) != 1:
                raise RuntimeError(SDL_GetError().decode('utf8'))
        else:
            if SDL_PollEvent(c_byref(event)) != 1:
                return None
        try:
            callback = sdl_event_callback_map[event.type]
        except KeyError:
            return None
        return callback(event, self._mouse, self._keyboard)

    async def _connect_peripherals(self, event: GamutApplicationStart) -> None:
        self._mouse.connect().send()
        self._keyboard.connect().send()

    async def _disconnect_peripherals(
        self,
        event: GamutApplicationStart
    ) -> None:
        self._keyboard.disconnect().send()
        self._mouse.disconnect().send()


class GamutApplicationRunContext:

    def __init__(self, binds: tuple[Bind, ...]) -> None:
        self._binds = binds

    def __enter__(self) -> None:
        if SDL_Init(SDL_INIT_EVENTS) != 0:
            raise RuntimeError(SDL_GetError().decode('utf8'))
        for bind in self._binds:
            bind.__enter__()

    def __exit__(self, *args: Any) -> None:
        for bind in self._binds:
            bind.__exit__(*args)
        SDL_QuitSubSystem(SDL_INIT_EVENTS)
