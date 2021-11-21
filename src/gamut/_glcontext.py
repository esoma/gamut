
from __future__ import annotations

__all__ = [
    'get_gl_context',
    'GlContext',
    'require_gl_context',
    'release_gl_context',
]

# gamut
from ._sdl import sdl_event_callback_map
# python
from ctypes import byref as c_byref
from queue import Empty as QueueEmpty
from queue import Queue
from threading import Condition
from threading import RLock
from threading import get_ident as identify_thread
from typing import Any, Callable, Optional, TYPE_CHECKING, TypeVar
# numpy
from numpy import array as np_array
# pyopengl
from OpenGL.GL import (GL_COPY_READ_BUFFER, GL_PACK_ALIGNMENT,
                       GL_UNPACK_ALIGNMENT, GL_VERSION, glBindBuffer,
                       glDeleteBuffers, glDeleteProgram, glDeleteTextures,
                       glDeleteVertexArrays, glGetString, glPixelStorei,
                       glUnmapBuffer)
from OpenGL.GL.framebufferobjects import (glDeleteFramebuffers,
                                          glDeleteRenderbuffers)
# pysdl2
from sdl2 import (SDL_CreateWindow, SDL_DestroyWindow, SDL_Event, SDL_GetError,
                  SDL_GL_CONTEXT_MAJOR_VERSION, SDL_GL_CONTEXT_MINOR_VERSION,
                  SDL_GL_CONTEXT_PROFILE_CORE, SDL_GL_CONTEXT_PROFILE_MASK,
                  SDL_GL_CreateContext, SDL_GL_DeleteContext,
                  SDL_GL_MakeCurrent, SDL_GL_SetAttribute, SDL_GL_STENCIL_SIZE,
                  SDL_Init, SDL_INIT_VIDEO, SDL_PushEvent, SDL_QuitSubSystem,
                  SDL_USEREVENT, SDL_WINDOW_HIDDEN, SDL_WINDOW_OPENGL)

singleton: Optional[GlContext] = None
refs_lock = RLock()
refs: int = 0


R = TypeVar('R')


if TYPE_CHECKING:
    # gamut
    from gamut.peripheral import Controller, Keyboard, Mouse


class GlContext:
    """The GlContext object encapsulates the lifetime of an OpenGL context.
    Anything that utilizes the OpenGL context directly should carry a reference
    to the GlContext object in order to keep the context alive.

    Typically there is only one GlContext which can be automatically created
    using the "get_gl_context" function.
    """

    _sdl_window: Any
    _sdl_gl_context: Optional[int]

    def __init__(self) -> None:
        self._sdl_video_thread = identify_thread()
        self._rendering_thread: Optional[int] = identify_thread()

        self._gc: Queue[Callable[[], None]] = Queue()

        self._execute = Condition()
        self._execute_function: Optional[Callable[[], Any]] = None
        self._execute_complete = False
        self._execute_result: Any = None
        self._execute_error: Optional[BaseException] = None

        init_sdl_video()
        SDL_GL_SetAttribute(SDL_GL_STENCIL_SIZE, 1)

        self._sdl_gl_window = self._sdl_window = SDL_CreateWindow(
            b'', 0, 0, 0, 0,
            SDL_WINDOW_HIDDEN | SDL_WINDOW_OPENGL
        )
        if self._sdl_window is None:
            raise RuntimeError(SDL_GetError().decode('utf8'))

        for major, minor in [
            (4, 3), (4, 2), (4, 1), (4, 0),
            (3, 3), (3, 2), (3, 1),
        ]:
            if SDL_GL_SetAttribute(SDL_GL_CONTEXT_MAJOR_VERSION, major) != 0:
                raise RuntimeError(SDL_GetError().decode('utf8'))
            if SDL_GL_SetAttribute(SDL_GL_CONTEXT_MINOR_VERSION, minor) != 0:
                raise RuntimeError(SDL_GetError().decode('utf8'))
            if SDL_GL_SetAttribute(
                SDL_GL_CONTEXT_PROFILE_MASK,
                SDL_GL_CONTEXT_PROFILE_CORE
            ) != 0:
                raise RuntimeError(SDL_GetError().decode('utf8'))
            self._sdl_gl_context = SDL_GL_CreateContext(self._sdl_window)
            if self._sdl_gl_context is not None:
                break
        if self._sdl_gl_context is None:
            raise RuntimeError(SDL_GetError().decode('utf8'))
        assert isinstance(self._sdl_gl_context, int)
        glPixelStorei(GL_PACK_ALIGNMENT, 1)
        glPixelStorei(GL_UNPACK_ALIGNMENT, 1)

        gl_version = glGetString(GL_VERSION).decode('utf8')
        self._version: tuple[int, int] = tuple( # type: ignore
            int(v)
            for v in gl_version.split(' ')[0].split('.')[:2]
        )

    def close(self) -> None:
        assert self._execute_function is None
        if identify_thread() != self._sdl_video_thread:
            raise RuntimeError('shutdown outside main thread')
        self.gc_collect()
        if self._sdl_gl_context is not None:
            assert self._rendering_thread == identify_thread()
            SDL_GL_MakeCurrent(self._sdl_window, 0)
            SDL_GL_DeleteContext(self._sdl_gl_context)
            self._sdl_gl_context = None
            self._sdl_gl_window = None
        if self._sdl_window is not None:
            SDL_DestroyWindow(self._sdl_window)
            self._sdl_window = None
        deinit_sdl_video()

    def set_sdl_window(self, sdl_window: Any) -> None:
        assert identify_thread() == self._rendering_thread
        if self._sdl_gl_window != sdl_window:
            SDL_GL_MakeCurrent(sdl_window, self._sdl_gl_context)
            self._sdl_gl_window = sdl_window

    def unset_sdl_window(self, sdl_window: Any) -> None:
        if identify_thread() == self._rendering_thread:
            if self._sdl_gl_window == sdl_window:
                SDL_GL_MakeCurrent(self._sdl_window, self._sdl_gl_context)
                self._sdl_gl_window = self._sdl_window

    def release_rendering_thread(self) -> None:
        self._rendering_thread = None
        self._sdl_gl_window = None
        SDL_GL_MakeCurrent(self._sdl_window, 0)

    def obtain_rendering_thread(self) -> None:
        self._rendering_thread = identify_thread()
        self._sdl_gl_window = self._sdl_window
        SDL_GL_MakeCurrent(self._sdl_window, self._sdl_gl_context)

    @property
    def is_open(self) -> bool:
        return self._sdl_gl_context is not None

    @property
    def sdl_gl_context(self) -> int:
        assert self._sdl_gl_context is not None
        return self._sdl_gl_context

    @property
    def version(self) -> tuple[int, int]:
        return self._version

    @property
    def sdl_video_thread(self) -> int:
        return self._sdl_video_thread

    def gc_collect(self) -> None:
        assert identify_thread() == self._rendering_thread
        while True:
            try:
                gc = self._gc.get_nowait()
            except QueueEmpty:
                return
            gc()

    def _collect_garbage(self, func: Callable[[], None]) -> None:
        if identify_thread() == self._rendering_thread:
            func()
        else:
            self._gc.put(func)

    def unmap_gl_buffer(self, gl_buffer_name: Any) -> None:
        def _unmap_gl_buffer() -> None:
            glBindBuffer(GL_COPY_READ_BUFFER, gl_buffer_name)
            glUnmapBuffer(GL_COPY_READ_BUFFER)
        self._collect_garbage(_unmap_gl_buffer)

    def delete_buffer(self, gl_buffer_name: Any) -> None:
        def _delete_buffer() -> None:
            glDeleteBuffers(1, np_array([gl_buffer_name]))
        self._collect_garbage(_delete_buffer)

    def delete_vertex_array(self, gl_vertex_array_name: Any) -> None:
        def _delete_vertex_array() -> None:
            glDeleteVertexArrays(1, np_array([gl_vertex_array_name]))
        self._collect_garbage(_delete_vertex_array)

    def delete_render_buffer(self, gl_render_buffer_name: Any) -> None:
        def _delete_render_buffer() -> None:
            glDeleteRenderbuffers(1, np_array([gl_render_buffer_name]))
        self._collect_garbage(_delete_render_buffer)

    def delete_frame_buffer(self, gl_frame_buffer_name: Any) -> None:
        def _delete_frame_buffer() -> None:
            glDeleteFramebuffers(1, np_array([gl_frame_buffer_name]))
        self._collect_garbage(_delete_frame_buffer)

    def delete_shader(self, gl_shader_name: Any) -> None:
        def _delete_shader() -> None:
            glDeleteProgram(gl_shader_name)
        self._collect_garbage(_delete_shader)

    def delete_texture(self, gl_texture_name: Any) -> None:
        def _delete_texture() -> None:
            glDeleteTextures(np_array([gl_texture_name]))
        self._collect_garbage(_delete_texture)

    def execute(self, func: Callable[[], R]) -> R:
        if identify_thread() == self._sdl_video_thread:
            return func()
        else:
            with self._execute:
                self._execute_function = func
                self._execute_complete = False
                self._execute_error = None
                self._execute_result = None
                sdl_event = SDL_Event()
                sdl_event.type = SDL_USEREVENT
                SDL_PushEvent(c_byref(sdl_event))
                while not self._execute_complete:
                    self._execute.wait()
                self._execute_function = None
                self._execute_complete = False
                if self._execute_error is not None:
                    raise self._execute_error
                return self._execute_result # type: ignore


def sdl_user_event_callback(
    sdl_event: Any,
    mice: dict[Any, Mouse],
    keyboards: dict[Any, Keyboard],
    controllers: dict[Any, Controller]
) -> None:
    try:
        gl_context = get_gl_context()
    except RuntimeError:
        return

    with gl_context._execute:
        if gl_context._execute_function is not None:
            try:
                gl_context._execute_result = gl_context._execute_function()
            except BaseException as ex:
                gl_context._execute_error = ex
            gl_context._execute_complete = True
            gl_context._execute.notify()


assert SDL_USEREVENT not in sdl_event_callback_map
sdl_event_callback_map[SDL_USEREVENT] = sdl_user_event_callback


def release_gl_context(gl_context_marker: Any) -> Any:
    global singleton
    global refs
    if gl_context_marker != 1:
        return False
    with refs_lock:
        assert singleton is not None
        assert refs > 0
        refs -= 1
        if refs == 0:
            singleton.close()
            assert refs == 0
            singleton = None
    return False


def require_gl_context() -> Any:
    global refs
    global singleton
    with refs_lock:
        if singleton is None:
            assert refs == 0
            singleton = GlContext()
        refs += 1
    return True


def get_gl_context() -> GlContext:
    with refs_lock:
        if singleton is None:
            raise RuntimeError('no gl context')
        return singleton


def init_sdl_video() -> None:
    if SDL_Init(SDL_INIT_VIDEO) != 0:
        raise RuntimeError(SDL_GetError().decode('utf8'))


def deinit_sdl_video() -> None:
    SDL_QuitSubSystem(SDL_INIT_VIDEO)
