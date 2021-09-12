
from __future__ import annotations

__all__ = [
    'Mouse',
    'MouseConnected',
    'MouseDisconnected',
    'MouseEvent',
]

# gamut
from ._peripheral import (Peripheral, PeripheralConnected,
                          PeripheralDisconnected, PeripheralEvent)
# gamut
from gamut._sdl import sdl_event_callback_map, sdl_window_event_callback_map
from gamut._window import get_window_from_sdl_id, Window
# python
from typing import Any, Optional
# pysdl2
from sdl2 import SDL_MOUSEMOTION, SDL_TOUCH_MOUSEID, SDL_WINDOWEVENT_LEAVE


class MouseEvent(PeripheralEvent, peripheral=...):
    peripheral: Mouse

    @property
    def mouse(self) -> Mouse:
        return self.peripheral


class MouseConnected(MouseEvent, PeripheralConnected, peripheral=...):
    pass


class MouseDisconnected(MouseEvent, PeripheralDisconnected, peripheral=...):
    pass


class MouseMoved(MouseEvent, peripheral=...):
    position: Optional[tuple[int, int]]
    window: Optional[Window]


class Mouse(Peripheral):

    Event: type[MouseEvent]
    Connected: type[MouseConnected]
    Disconnected: type[MouseDisconnected]
    Moved: type[MouseMoved]

    def __init__(self, name: str):
        super().__init__(name)
        class Event(MouseEvent, self.Event): # type: ignore
            pass
        self.Event = Event
        class Connected( # type: ignore
            MouseConnected,
            Event,
            self.Connected, # type: ignore
        ):
            pass
        self.Connected = Connected
        class Disconnected( # type: ignore
            MouseDisconnected,
            Event,
            self.Disconnected, # type: ignore
        ):
            pass
        self.Disconnected = Disconnected
        class Moved(MouseMoved, Event):
            pass
        self.Moved = Moved

        self._position: Optional[tuple[int, int]] = None
        self._window: Optional[Window] = None

    @property
    def position(self) -> Optional[tuple[int, int]]:
        return self._position

    @property
    def window(self) -> Optional[Window]:
        return self._window


def sdl_window_event_leave(sdl_event: Any, mouse: Mouse) -> MouseMoved:
    assert mouse._window is not None
    assert mouse._position is not None
    mouse._position = None
    mouse._window = None
    return mouse.Moved(mouse._position, mouse._window)

assert SDL_WINDOWEVENT_LEAVE not in sdl_window_event_callback_map
sdl_window_event_callback_map[SDL_WINDOWEVENT_LEAVE] = sdl_window_event_leave


def sdl_mouse_motion_event_callback(
    sdl_event: Any,
    mouse: Mouse
) -> Optional[MouseMoved]:
    if sdl_event.motion.which == SDL_TOUCH_MOUSEID:
        return None
    try:
        window = get_window_from_sdl_id(sdl_event.motion.windowID)
    except KeyError:
        return None
    mouse._position = (sdl_event.motion.x, sdl_event.motion.y)
    mouse._window = window
    return mouse.Moved(mouse._position, mouse._window)

assert SDL_MOUSEMOTION not in sdl_event_callback_map
sdl_event_callback_map[SDL_MOUSEMOTION] = sdl_mouse_motion_event_callback
