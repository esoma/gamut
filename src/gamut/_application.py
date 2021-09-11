
from __future__ import annotations

__all__ = [
    'BoundGamutApplicationEnd',
    'BoundGamutApplicationEvent',
    'BoundGamutApplicationStart',
    'GamutApplication',
    'GamutApplicationEnd',
    'GamutApplicationStart',
    'GamutApplicationEvent',
]

# gamut
from gamut.event import (Application, ApplicationEnd, ApplicationEvent,
                         ApplicationStart, BoundApplicationEnd,
                         BoundApplicationEvent, BoundApplicationStart)
from gamut.event import Event as BaseEvent
from gamut._window import sdl_window_event_callback
# python
from ctypes import byref as c_byref
from functools import cached_property
from typing import Any, Callable, Optional, TypeVar
# pysdl2
from sdl2 import (SDL_CreateWindow, SDL_DestroyWindow, SDL_Event, SDL_GetError,
                  SDL_GL_CreateContext, SDL_GL_DeleteContext, SDL_PollEvent,
                  SDL_WaitEvent, SDL_WINDOW_HIDDEN, SDL_WINDOW_OPENGL,
                  SDL_WINDOWEVENT)

R = TypeVar('R')


event_callback_map = {
    SDL_WINDOWEVENT: sdl_window_event_callback,
}


class GamutApplicationEvent(ApplicationEvent):
    application: GamutApplication[Any]


class GamutApplicationStart(ApplicationStart):
    pass


class GamutApplicationEnd(ApplicationEnd):
    pass


class BoundGamutApplicationEvent(
    BoundApplicationEvent,
    GamutApplicationEvent,
    application=...
):
    pass


class BoundGamutApplicationStart(
    BoundGamutApplicationEvent,
    BoundApplicationStart,
    GamutApplicationStart,
    application=...
):
    pass


class BoundGamutApplicationEnd(
    BoundGamutApplicationEvent,
    BoundApplicationEnd,
    GamutApplicationEnd,
    application=...
):
    pass


class GamutApplication(Application[R]):

    Event: type[BoundGamutApplicationEvent]
    Start: type[BoundGamutApplicationStart]
    End: type[BoundGamutApplicationEnd]

    def __init__(self) -> None:
        super().__init__()
        class Event(BoundGamutApplicationEvent, self.Event): # type: ignore
            pass
        self.Event = Event
        class Start(
            BoundGamutApplicationStart,
            Event,
            self.Start # type: ignore
        ):
            pass
        self.Start = Start
        class End(
            Event,
            BoundGamutApplicationEnd,
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
