
from __future__ import annotations

__all__ = [
    'BoundWindowClose',
    'BoundWindowHidden',
    'BoundWindowMoved',
    'BoundWindowResized',
    'BoundWindowShown',
    'sdl_window_event_callback',
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
from gamut.event import Event as _Event
# python
from ctypes import byref as c_byref
from ctypes import c_int
from typing import Any, Callable, ClassVar, Optional
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


class WindowEvent(_Event):
    window: Window


class WindowClose(WindowEvent):
    pass


class WindowHidden(WindowEvent):
    pass


class WindowMoved(WindowEvent):
    position: tuple[int, int]


class WindowResized(WindowEvent):
    size: tuple[int, int]


class WindowShown(WindowEvent):
    pass


class BoundWindowEvent(WindowEvent, window=...):
    pass


class BoundWindowClose(BoundWindowEvent, WindowClose, window=...):
    pass


class BoundWindowHidden(BoundWindowEvent, WindowHidden, window=...):
    pass


class BoundWindowMoved(BoundWindowEvent, WindowMoved, window=...):
    pass


class BoundWindowResized(BoundWindowEvent, WindowResized, window=...):
    pass


class BoundWindowShown(BoundWindowEvent, WindowShown, window=...):
    pass


class Window:

    _id_map: ClassVar[WeakValueDictionary[int, Window]] = WeakValueDictionary()

    Event: type[BoundWindowEvent]
    Close: type[BoundWindowClose]
    Hidden: type[BoundWindowHidden]
    Moved: type[BoundWindowMoved]
    Resized: type[BoundWindowResized]
    Shown: type[BoundWindowShown]

    def __init__(self) -> None:
        self._gl_context: Optional[GlContext] = get_gl_context()
        self._sdl = SDL_CreateWindow(
            b'',
            SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED,
            100, 100,
            SDL_WINDOW_HIDDEN | SDL_WINDOW_OPENGL
        )

        class Event(BoundWindowEvent, window=self):
            pass
        self.Event = Event
        class Close(BoundWindowClose, Event):
            pass
        self.Close = Close
        class Hidden(BoundWindowHidden, Event):
            pass
        self.Hidden = Hidden
        class Moved(BoundWindowMoved, Event):
            pass
        self.Moved = Moved
        class Resized(BoundWindowResized, Event):
            pass
        self.Resized = Resized
        class Shown(BoundWindowShown, Event):
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


def sdl_window_event_callback(sdl_event: Any) -> Optional[WindowEvent]:
    try:
        event_callback = sdl_event_callback_map[sdl_event.window.event]
    except KeyError:
        return None
    try:
        window = Window._id_map[sdl_event.window.windowID]
    except KeyError:
        return None
    return event_callback(window, sdl_event)


def sdl_window_event_close_callback(
    window: Window,
    sdl_event: Any
) -> WindowClose:
    return window.Close()


def sdl_window_event_hidden_callback(
    window: Window,
    sdl_event: Any
) -> WindowHidden:
    return window.Hidden()


def sdl_window_event_moved_callback(
    window: Window,
    sdl_event: Any
) -> WindowMoved:
    return window.Moved((sdl_event.window.data1, sdl_event.window.data2))


def sdl_window_event_resized_callback(
    window: Window,
    sdl_event: Any
) -> WindowResized:
    glViewport(0, 0, sdl_event.window.data1, sdl_event.window.data2)
    return window.Resized((sdl_event.window.data1, sdl_event.window.data2))


def sdl_window_event_shown_callback(
    window: Window,
    sdl_event: Any
) -> WindowShown:
    return window.Shown()


sdl_event_callback_map: dict[Any, Callable[[Window, Any], WindowEvent]] = {
    SDL_WINDOWEVENT_CLOSE: sdl_window_event_close_callback,
    SDL_WINDOWEVENT_HIDDEN: sdl_window_event_hidden_callback,
    SDL_WINDOWEVENT_MOVED: sdl_window_event_moved_callback,
    SDL_WINDOWEVENT_SIZE_CHANGED: sdl_window_event_resized_callback,
    SDL_WINDOWEVENT_SHOWN: sdl_window_event_shown_callback,
}
