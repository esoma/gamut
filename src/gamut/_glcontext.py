
from __future__ import annotations

__all__ = [
    'get_gl_context',
    'GlContext',
    'require_gl_context',
    'release_gl_context',
]

# python
from time import sleep
from typing import Any, Optional
# pyopengl
from OpenGL.GL import (GL_PACK_ALIGNMENT, GL_UNPACK_ALIGNMENT, GL_VERSION,
                       glGetString, glPixelStorei)
# pysdl2
from sdl2 import (SDL_CreateWindow, SDL_DestroyWindow, SDL_GetError,
                  SDL_GL_CONTEXT_MAJOR_VERSION, SDL_GL_CONTEXT_MINOR_VERSION,
                  SDL_GL_CONTEXT_PROFILE_CORE, SDL_GL_CONTEXT_PROFILE_MASK,
                  SDL_GL_CreateContext, SDL_GL_DeleteContext,
                  SDL_GL_SetAttribute, SDL_GL_STENCIL_SIZE, SDL_Init,
                  SDL_INIT_EVENTS, SDL_INIT_VIDEO, SDL_QuitSubSystem,
                  SDL_WINDOW_HIDDEN, SDL_WINDOW_OPENGL)

singleton: Optional[GlContext] = None
refs: int = 0


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
        init_sdl_video()
        SDL_GL_SetAttribute(SDL_GL_STENCIL_SIZE, 1)

        self._sdl_window = SDL_CreateWindow(
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
        if self._sdl_gl_context is not None:
            SDL_GL_DeleteContext(self._sdl_gl_context)
            self._sdl_gl_context = None
        if self._sdl_window is not None:
            SDL_DestroyWindow(self._sdl_window)
            self._sdl_window = None
        deinit_sdl_video()

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


def release_gl_context(gl_context_marker: Any) -> Any:
    global singleton
    global refs
    if gl_context_marker != 1:
        return False
    assert singleton is not None
    assert refs > 0
    refs -= 1
    if refs == 0:
        singleton.close()
        singleton = None
    return False


def require_gl_context() -> Any:
    global refs
    global singleton
    if singleton is None:
        assert refs == 0
        singleton = GlContext()
    refs += 1
    return True


def get_gl_context() -> GlContext:
    if singleton is None:
        raise RuntimeError('no gl context')
    return singleton


def init_sdl_video() -> None:
    # when rapidly initializing and quitting the video subsystem (as in
    # testing it has been observed in linux while using xvfb that sometimes
    # it will fail to initialize
    #
    # so we will try a couple times, waiting in between each try if there
    # is no available video device
    for i in range(10):
        if SDL_Init(SDL_INIT_VIDEO) == 0:
            break
        # video initialization implies events initialization, but SDL_Init
        # doesn't quit the events subsystem if SDL_Init has an error, so
        # we must manually do so
        # https://github.com/libsdl-org/SDL/issues/4826
        SDL_QuitSubSystem(SDL_INIT_EVENTS)
        if SDL_GetError() != b'No available video device':
            raise RuntimeError(SDL_GetError().decode('utf8'))
        sleep(.1)
    else:
        raise RuntimeError(SDL_GetError().decode('utf8'))


def deinit_sdl_video() -> None:
    SDL_QuitSubSystem(SDL_INIT_VIDEO)
