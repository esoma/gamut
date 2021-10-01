
from __future__ import annotations

__all__ = [
    'get_window_from_sdl_id',
    'Window',
    'WindowClose',
    'WindowEvent',
    'WindowHidden',
    'WindowMoved',
    'WindowResized',
    'WindowShown'
]

# gamut
from gamut._glcontext import get_gl_context, GlContext
from gamut._sdl import sdl_window_event_callback_map
from gamut.event import Event as _Event
# python
from ctypes import byref as c_byref
from ctypes import c_int
from typing import Any, ClassVar, Optional, TYPE_CHECKING
from weakref import WeakValueDictionary
# pyopengl
from OpenGL.GL import glViewport
# pysdl2
from sdl2 import (SDL_CreateWindow, SDL_DestroyWindow, SDL_GetWindowFlags,
                  SDL_GetWindowID, SDL_GetWindowSize, SDL_GetWindowTitle,
                  SDL_HideWindow, SDL_SetWindowBordered,
                  SDL_SetWindowFullscreen, SDL_SetWindowPosition,
                  SDL_SetWindowSize, SDL_SetWindowTitle, SDL_ShowWindow,
                  SDL_WINDOW_BORDERLESS, SDL_WINDOW_FULLSCREEN_DESKTOP,
                  SDL_WINDOW_HIDDEN, SDL_WINDOW_OPENGL, SDL_WINDOWEVENT_CLOSE,
                  SDL_WINDOWEVENT_HIDDEN, SDL_WINDOWEVENT_MOVED,
                  SDL_WINDOWEVENT_SHOWN, SDL_WINDOWEVENT_SIZE_CHANGED,
                  SDL_WINDOWPOS_CENTERED)

if TYPE_CHECKING:
    # gamut
    from gamut.peripheral import Keyboard, Mouse


class WindowEvent(_Event, window=...):
    window: Window


class WindowClose(WindowEvent, window=...):
    pass


class WindowHidden(WindowEvent, window=...):
    pass


class WindowMoved(WindowEvent, window=...):
    position: tuple[int, int]


class WindowResized(WindowEvent, window=...):
    size: tuple[int, int]


class WindowShown(WindowEvent, window=...):
    pass


class Window:

    _id_map: ClassVar[WeakValueDictionary[int, Window]] = WeakValueDictionary()

    Event: type[WindowEvent]
    Close: type[WindowClose]
    Hidden: type[WindowHidden]
    Moved: type[WindowMoved]
    Resized: type[WindowResized]
    Shown: type[WindowShown]

    def __init__(self) -> None:
        self._gl_context: Optional[GlContext] = get_gl_context()
        self._sdl = SDL_CreateWindow(
            b'',
            SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED,
            100, 100,
            SDL_WINDOW_HIDDEN | SDL_WINDOW_OPENGL
        )

        class Event(WindowEvent, window=self):
            pass
        self.Event = Event
        class Close(WindowClose, Event):
            pass
        self.Close = Close
        class Hidden(WindowHidden, Event):
            pass
        self.Hidden = Hidden
        class Moved(WindowMoved, Event):
            pass
        self.Moved = Moved
        class Resized(WindowResized, Event):
            pass
        self.Resized = Resized
        class Shown(WindowShown, Event):
            pass
        self.Shown = Shown

        Window._id_map[SDL_GetWindowID(self._sdl)] = self

    def __del__(self) -> None:
        self.close()

    def __repr__(self) -> str:
        if self._sdl is None:
            return f'<gamut.Window [closed]>'
        else:
            return f'<gamut.Window {self.title!r}>'

    def _ensure_open(self) -> None:
        if self._sdl is None:
            raise RuntimeError('window is closed')

    def close(self) -> None:
        self._gl_context = None
        if self._sdl is not None:
            SDL_DestroyWindow(self._sdl)
            self._sdl = None

    @property
    def is_bordered(self) -> bool:
        self._ensure_open()
        return not SDL_GetWindowFlags(self._sdl) & SDL_WINDOW_BORDERLESS

    @is_bordered.setter
    def is_bordered(self, is_bordered: bool) -> None:
        self._ensure_open()
        SDL_SetWindowBordered(self._sdl, bool(is_bordered))

    @property
    def is_fullscreen(self) -> bool:
        self._ensure_open()
        return bool(
            SDL_GetWindowFlags(self._sdl) &
            SDL_WINDOW_FULLSCREEN_DESKTOP
        )

    @is_fullscreen.setter
    def is_fullscreen(self, is_fullscreen: bool) -> None:
        self._ensure_open()
        SDL_SetWindowFullscreen(
            self._sdl,
            SDL_WINDOW_FULLSCREEN_DESKTOP if is_fullscreen else 0
        )

    @property
    def is_visible(self) -> bool:
        self._ensure_open()
        return not SDL_GetWindowFlags(self._sdl) & SDL_WINDOW_HIDDEN

    @is_visible.setter
    def is_visible(self, is_visible: bool) -> None:
        self._ensure_open()
        if is_visible:
            SDL_ShowWindow(self._sdl)
        else:
            SDL_HideWindow(self._sdl)

    def recenter(self) -> None:
        self._ensure_open()
        SDL_SetWindowPosition(
            self._sdl,
            SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED
        )

    def resize(self, width: int, height: int) -> None:
        self._ensure_open()
        SDL_SetWindowSize(self._sdl, int(width), int(height))

    @property
    def size(self) -> tuple[int, int]:
        self._ensure_open()
        x = c_int()
        y = c_int()
        SDL_GetWindowSize(self._sdl, c_byref(x), c_byref(y))
        return (x.value, y.value)

    @property
    def title(self) -> str:
        self._ensure_open()
        title: bytes = SDL_GetWindowTitle(self._sdl)
        return title.decode('utf8')

    @title.setter
    def title(self, title: str) -> None:
        self._ensure_open()
        SDL_SetWindowTitle(self._sdl, str(title).encode('utf8'))


def get_window_from_sdl_id(id: int) -> Window:
    return Window._id_map[id]


def sdl_window_event_close_callback(
    sdl_event: Any,
    mouse: Mouse,
    keyboard: Keyboard
) -> Optional[WindowClose]:
    try:
        window = get_window_from_sdl_id(sdl_event.window.windowID)
    except KeyError:
        return None
    return window.Close()

assert SDL_WINDOWEVENT_CLOSE not in sdl_window_event_callback_map
sdl_window_event_callback_map[SDL_WINDOWEVENT_CLOSE] = (
    sdl_window_event_close_callback
)


def sdl_window_event_hidden_callback(
    sdl_event: Any,
    mouse: Mouse,
    keyboard: Keyboard
) -> Optional[WindowHidden]:
    try:
        window = get_window_from_sdl_id(sdl_event.window.windowID)
    except KeyError:
        return None
    return window.Hidden()

assert SDL_WINDOWEVENT_HIDDEN not in sdl_window_event_callback_map
sdl_window_event_callback_map[SDL_WINDOWEVENT_HIDDEN] = (
    sdl_window_event_hidden_callback
)


def sdl_window_event_moved_callback(
    sdl_event: Any,
    mouse: Mouse,
    keyboard: Keyboard
) -> Optional[WindowMoved]:
    try:
        window = get_window_from_sdl_id(sdl_event.window.windowID)
    except KeyError:
        return None
    return window.Moved((sdl_event.window.data1, sdl_event.window.data2))

assert SDL_WINDOWEVENT_MOVED not in sdl_window_event_callback_map
sdl_window_event_callback_map[SDL_WINDOWEVENT_MOVED] = (
    sdl_window_event_moved_callback
)



def sdl_window_event_resized_callback(
    sdl_event: Any,
    mouse: Mouse,
    keyboard: Keyboard
) -> Optional[WindowResized]:
    try:
        window = get_window_from_sdl_id(sdl_event.window.windowID)
    except KeyError:
        return None
    glViewport(0, 0, sdl_event.window.data1, sdl_event.window.data2)
    return window.Resized((sdl_event.window.data1, sdl_event.window.data2))

assert SDL_WINDOWEVENT_SIZE_CHANGED not in sdl_window_event_callback_map
sdl_window_event_callback_map[SDL_WINDOWEVENT_SIZE_CHANGED] = (
    sdl_window_event_resized_callback
)


def sdl_window_event_shown_callback(
    sdl_event: Any,
    mouse: Mouse,
    keyboard: Keyboard
) -> Optional[WindowShown]:
    try:
        window = get_window_from_sdl_id(sdl_event.window.windowID)
    except KeyError:
        return None
    return window.Shown()

assert SDL_WINDOWEVENT_SHOWN not in sdl_window_event_callback_map
sdl_window_event_callback_map[SDL_WINDOWEVENT_SHOWN] = (
    sdl_window_event_shown_callback
)
