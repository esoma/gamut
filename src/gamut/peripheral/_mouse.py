
from __future__ import annotations

__all__ = [
    'Mouse',
    'MouseButton',
    'MouseButtonEvent',
    'MouseButtonPressed',
    'MouseButtonReleased',
    'MouseConnected',
    'MouseDisconnected',
    'MouseEvent',
    'MouseMoved',
]

# gamut
from ._peripheral import (Peripheral, PeripheralConnected,
                          PeripheralDisconnected, PeripheralEvent)
# gamut
from gamut._sdl import sdl_event_callback_map, sdl_window_event_callback_map
from gamut._window import get_window_from_sdl_id, Window
# python
from typing import Any, Optional
from weakref import ref
# pysdl2
from sdl2 import SDL_MOUSEMOTION, SDL_TOUCH_MOUSEID, SDL_WINDOWEVENT_LEAVE


class MouseEvent(PeripheralEvent, peripheral=...):
    peripheral: Mouse

    @property
    def mouse(self) -> Mouse:
        return self.peripheral


class MouseButtonEvent(MouseEvent, peripheral=..., button=...):
    button: MouseButton
    is_pressed: bool


class MouseButtonPressed(MouseButtonEvent,
    peripheral=..., button=..., is_pressed=True
):
    pass


class MouseButtonReleased(MouseButtonEvent,
    peripheral=..., button=..., is_pressed=False
):
    pass


class MouseConnected(MouseEvent, PeripheralConnected, peripheral=...):
    pass


class MouseDisconnected(MouseEvent, PeripheralDisconnected, peripheral=...):
    pass


class MouseMoved(MouseEvent, peripheral=...):
    position: Optional[tuple[int, int]]
    window: Optional[Window]


class BaseMouseButton:

    left: BaseMouseButton
    middle: BaseMouseButton
    right: BaseMouseButton
    front: BaseMouseButton
    back: BaseMouseButton

    def __init_subclass__(cls, mouse: Optional[Mouse] = None):
        super().__init_subclass__()
        cls.left = cls('left', mouse=mouse)
        cls.middle = cls('middle', mouse=mouse)
        cls.right = cls('right', mouse=mouse)
        cls.front = cls('front', mouse=mouse)
        cls.back = cls('back', mouse=mouse)

    def __init__(self, name: str, mouse: Optional[Mouse] = None):
        self._name = name
        self._mouse: Optional[ref[Mouse]] = ref(mouse) if mouse else None

    def __repr__(self) -> str:
        identifier = repr(self._name)
        if self._mouse:
            mouse = self._mouse()
            if mouse:
                identifier = f'{identifier} for {mouse!r}'
        return f'<gamut.peripheral.MouseButton {identifier}>'

    @property
    def name(self) -> str:
        return self._name


class MouseButton(BaseMouseButton):

    left: MouseButton
    middle: MouseButton
    right: MouseButton
    front: MouseButton
    back: MouseButton

    Event: type[MouseButtonEvent]
    Pressed: type[MouseButtonPressed]
    Released: type[MouseButtonReleased]

    def __init__(self, name: str, mouse: Optional[Mouse] = None):
        super().__init__(name, mouse=mouse)
        if mouse:
            class EventWithMouse( # type: ignore
                MouseButtonEvent,
                mouse.Event, # type: ignore
                button=self
            ):
                pass
            self.Event = EventWithMouse
            class PressedWithMouse( # type: ignore
                MouseButtonPressed,
                EventWithMouse
            ):
                pass
            self.Pressed = PressedWithMouse
            class ReleasedWithMouse( # type: ignore
                MouseButtonReleased,
                EventWithMouse
            ):
                pass
            self.Released = ReleasedWithMouse
        else:
            class EventNoMouse(MouseButtonEvent,
                peripheral=..., button=self
            ):
                pass
            self.Event = EventNoMouse
            class PressedNoMouse(MouseButtonPressed, EventNoMouse,
                peripheral=...
            ):
                pass
            self.Pressed = PressedNoMouse
            class ReleasedNoMouse(MouseButtonReleased, EventNoMouse,
                peripheral=...
            ):
                pass
            self.Released = ReleasedNoMouse


class PressableMouseButton(MouseButton):

    left: PressableMouseButton
    middle: PressableMouseButton
    right: PressableMouseButton
    front: PressableMouseButton
    back: PressableMouseButton

    def __init__(self, name: str, mouse: Mouse):
        super().__init__(name, mouse=mouse)
        self._is_pressed = False

    @property
    def is_pressed(self) -> bool:
        return self._is_pressed


class Mouse(Peripheral):

    Event: type[MouseEvent]
    Connected: type[MouseConnected]
    Disconnected: type[MouseDisconnected]
    Moved: type[MouseMoved]

    Button: type[PressableMouseButton]

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
        class Moved(MouseMoved, Event): # type: ignore
            pass
        self.Moved = Moved

        class Button(PressableMouseButton, mouse=self):
            pass
        self.Button = Button

        self._position: Optional[tuple[int, int]] = None
        self._window: Optional[Window] = None

    def __repr__(self) -> str:
        return f'<gamut.peripheral.Mouse {self._name!r}>'

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
