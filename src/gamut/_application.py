
from __future__ import annotations

__all__ = [
    'GamutApplication',
    'GamutApplicationEnd',
    'GamutApplicationStart',
    'GamutApplicationEvent',
]

# gamut
from gamut._window import sdl_window_event_callback
from gamut.event import (Application, ApplicationEnd, ApplicationEvent,
                         ApplicationStart)
from gamut.event import Event as BaseEvent
# python
from ctypes import byref as c_byref
from typing import Any, Optional, TypeVar
# pysdl2
from sdl2 import (SDL_Event, SDL_GetError, SDL_PollEvent, SDL_WaitEvent,
                  SDL_WINDOWEVENT)

R = TypeVar('R')


event_callback_map = {
    SDL_WINDOWEVENT: sdl_window_event_callback,
}


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

    async def poll(self, block: bool = True) -> Optional[BaseEvent]:
        event = await super().poll()
        if event:
            return event
        return self._poll_sdl(block=block)

    def _poll_sdl(self, block: bool) -> Optional[BaseEvent]:
        event = SDL_Event()
        if block:
            if SDL_WaitEvent(c_byref(event)) != 1:
                raise RuntimeError(SDL_GetError().decode('utf8'))
        else:
            if SDL_PollEvent(c_byref(event)) != 1:
                return None
        try:
            event_callback = event_callback_map[event.type]
        except KeyError:
            return None
        return event_callback(event)
