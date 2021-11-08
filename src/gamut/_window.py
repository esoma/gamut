
from __future__ import annotations

__all__ = [
    'get_sdl_window_from_window',
    'get_window_from_sdl_id',
    'Window',
    'WindowBufferSynchronization',
    'WindowClose',
    'WindowEvent',
    'WindowHidden',
    'WindowMoved',
    'WindowResized',
    'WindowShown'
]

# gamut
from gamut._glcontext import release_gl_context, require_gl_context
from gamut._sdl import sdl_window_event_callback_map
from gamut.event import Event as _Event
# python
from ctypes import byref as c_byref
from ctypes import c_int
from enum import Enum
import sys
from typing import Any, ClassVar, Optional, TYPE_CHECKING
from weakref import WeakValueDictionary
# pyopengl
from OpenGL.GL import GL_DRAW_FRAMEBUFFER, glBindFramebuffer, glViewport
# pysdl2
from sdl2 import (SDL_CreateWindow, SDL_DestroyWindow, SDL_GetError,
                  SDL_GetWindowFlags, SDL_GetWindowID, SDL_GetWindowSize,
                  SDL_GetWindowTitle, SDL_GL_SetSwapInterval,
                  SDL_GL_SwapWindow, SDL_HideWindow, SDL_SetWindowBordered,
                  SDL_SetWindowFullscreen, SDL_SetWindowPosition,
                  SDL_SetWindowSize, SDL_SetWindowTitle, SDL_ShowWindow,
                  SDL_WINDOW_BORDERLESS, SDL_WINDOW_FULLSCREEN_DESKTOP,
                  SDL_WINDOW_HIDDEN, SDL_WINDOW_OPENGL, SDL_WINDOWEVENT_CLOSE,
                  SDL_WINDOWEVENT_HIDDEN, SDL_WINDOWEVENT_MOVED,
                  SDL_WINDOWEVENT_SHOWN, SDL_WINDOWEVENT_SIZE_CHANGED,
                  SDL_WINDOWPOS_CENTERED)

if TYPE_CHECKING:
    # gamut
    from gamut.peripheral import Controller, Keyboard, Mouse


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


class WindowBufferSynchronization(Enum):
    IMMEDIATE = 0
    VSYNC = 1
    ADAPTIVE_VSYNC = -1


class Window:

    _id_map: ClassVar[WeakValueDictionary[int, Window]] = WeakValueDictionary()

    Event: type[WindowEvent]
    Close: type[WindowClose]
    Hidden: type[WindowHidden]
    Moved: type[WindowMoved]
    Resized: type[WindowResized]
    Shown: type[WindowShown]

    def __init__(self) -> None:
        self._gl_context = require_gl_context()

        self._sdl = SDL_CreateWindow(
            b'',
            SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED,
            100, 100,
            SDL_WINDOW_HIDDEN | SDL_WINDOW_OPENGL
        )
        if not self._sdl:
            raise RuntimeError(SDL_GetError().decode('utf8'))

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

        sdl_window_id = SDL_GetWindowID(self._sdl)
        if sdl_window_id == 0:
            raise RuntimeError(SDL_GetError().decode('utf8'))
        Window._id_map[sdl_window_id] = self

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
        if self._sdl is not None:
            SDL_DestroyWindow(self._sdl)
            self._sdl = None
        self._gl_context = release_gl_context(self._gl_context)

    def flip_buffer(
        self,
        synchronization: WindowBufferSynchronization =
            WindowBufferSynchronization.IMMEDIATE
    ) -> None:
        assert synchronization.value in [-1, 0, 1]
        while True:
            if SDL_GL_SetSwapInterval(synchronization.value) == 0:
                break
            # not all systems support adaptive vsync, so try regular vsync
            # instead
            if synchronization == WindowBufferSynchronization.ADAPTIVE_VSYNC:
                synchronization = WindowBufferSynchronization.VSYNC
            else:
                # not all systems are double buffered, so setting any swap
                # interval will result in an error
                # we don't actually need to swap the window in this case
                return
        # according to SDL docs:
        # On macOS, make sure you bind 0 to the draw framebuffer before
        # swapping the window, otherwise nothing will happen. If you aren't
        # using glBindFramebuffer(), this is the default and you won't have to
        # do anything extra.
        if sys.platform == 'darwin':
            glBindFramebuffer(GL_DRAW_FRAMEBUFFER, 0)
        SDL_GL_SwapWindow(self._sdl)

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


def get_sdl_window_from_window(window: Window) -> Any:
    window._ensure_open()
    return window._sdl


def sdl_window_event_close_callback(
    sdl_event: Any,
    mice: dict[Any, Mouse],
    keyboards: dict[Any, Keyboard],
    controllers: dict[Any, Controller]
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
    mice: dict[Any, Mouse],
    keyboards: dict[Any, Keyboard],
    controllers: dict[Any, Controller]
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
    mice: dict[Any, Mouse],
    keyboards: dict[Any, Keyboard],
    controllers: dict[Any, Controller]
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
    mice: dict[Any, Mouse],
    keyboards: dict[Any, Keyboard],
    controllers: dict[Any, Controller]
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
    mice: dict[Any, Mouse],
    keyboards: dict[Any, Keyboard],
    controllers: dict[Any, Controller]
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
