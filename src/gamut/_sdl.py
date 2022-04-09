
from __future__ import annotations

__all__ = [
    'sdl_event_callback_map',
    'SDL_KEYBOARD_KEY',
    'SDL_MOUSE_KEY',
    'sdl_window_event_callback_map',
]

# gamut
from gamut.event import Event
# python
# DVector4
from typing import Any, Callable, Final, Optional, TYPE_CHECKING
# pysdl2
from sdl2 import SDL_WINDOWEVENT

if TYPE_CHECKING:
    # gamut
    from gamut.peripheral import Controller, Keyboard, Mouse


def sdl_window_event_callback(
    sdl_event: Any,
    mice: dict[Any, Mouse],
    keyboards: dict[Any, Keyboard],
    controllers: dict[Any, Controller]
) -> Optional[Event]:
    assert sdl_event.type == SDL_WINDOWEVENT
    try:
        callback = sdl_window_event_callback_map[sdl_event.window.event]
    except KeyError:
        return None
    return callback(sdl_event, mice, keyboards, controllers)


sdl_event_callback_map: dict[
    int,
    Callable[[
        Any,
        dict[Any, Mouse],
        dict[Any, Keyboard],
        dict[Any, Controller]
    ], Optional[Event]]
] = {
    SDL_WINDOWEVENT: sdl_window_event_callback,
}

sdl_window_event_callback_map: dict[
    int,
        Callable[[
        Any,
        dict[Any, Mouse],
        dict[Any, Keyboard],
        dict[Any, Controller]
    ], Optional[Event]]
] = {}

SDL_MOUSE_KEY: Final = "sdl_mouse"
SDL_KEYBOARD_KEY: Final = "sdl_keyboard"
