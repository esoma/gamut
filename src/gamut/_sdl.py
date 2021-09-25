
from __future__ import annotations

__all__ = [
    'sdl_event_callback_map',
    'sdl_window_event_callback_map',
]

# gamut
from gamut.event import Event
# python
from typing import Any, Callable, Optional, TYPE_CHECKING
# pysdl2
from sdl2 import SDL_WINDOWEVENT

if TYPE_CHECKING:
    # gamut
    from gamut.peripheral import Keyboard, Mouse


def sdl_window_event_callback(
    sdl_event: Any,
    mouse: Mouse,
    keyboard: Keyboard
) -> Optional[Event]:
    assert sdl_event.type == SDL_WINDOWEVENT
    try:
        callback = sdl_window_event_callback_map[sdl_event.window.event]
    except KeyError:
        return None
    return callback(sdl_event, mouse, keyboard)


sdl_event_callback_map: dict[
    int,
    Callable[[Any, Mouse, Keyboard], Optional[Event]]
] = {
    SDL_WINDOWEVENT: sdl_window_event_callback,
}

sdl_window_event_callback_map: dict[
    int,
    Callable[[Any, Mouse, Keyboard], Optional[Event]]
] = {}
