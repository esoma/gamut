
from __future__ import annotations

__all__ = ['get_gl_context', 'GlContext']

# python
from time import sleep
from typing import Any, Optional
from weakref import ref
# pyopengl
from OpenGL.GL import GL_PACK_ALIGNMENT, GL_UNPACK_ALIGNMENT, glPixelStorei
# pysdl2
from sdl2 import (SDL_CreateWindow, SDL_DestroyWindow, SDL_GetError,
                  SDL_GL_CONTEXT_PROFILE_CORE, SDL_GL_CONTEXT_PROFILE_MASK,
                  SDL_GL_CreateContext, SDL_GL_DeleteContext,
                  SDL_GL_SetAttribute, SDL_GL_STENCIL_SIZE, SDL_Init,
                  SDL_INIT_EVENTS, SDL_INIT_VIDEO, SDL_QuitSubSystem,
                  SDL_WINDOW_HIDDEN, SDL_WINDOW_OPENGL)

singleton: Optional[ref[GlContext]] = None


class SdlVideo:

    def __init__(self) -> None:
        self._is_closed = True

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

        self._is_closed = False

    def __del__(self) -> None:
        if not self._is_closed:
            SDL_QuitSubSystem(SDL_INIT_VIDEO)
            self._is_closed = True


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
        self._sdl_video = SdlVideo()
        SDL_GL_SetAttribute(SDL_GL_STENCIL_SIZE, 1)
        self._sdl_window = SDL_CreateWindow(
            b'', 0, 0, 0, 0,
            SDL_WINDOW_HIDDEN | SDL_WINDOW_OPENGL
        )
        if self._sdl_window is None:
            raise RuntimeError(SDL_GetError().decode('utf8'))

        if SDL_GL_SetAttribute(
            SDL_GL_CONTEXT_PROFILE_MASK,
            SDL_GL_CONTEXT_PROFILE_CORE
        ) != 0:
            raise RuntimeError(SDL_GetError().decode('utf8'))
        self._sdl_gl_context = SDL_GL_CreateContext(self._sdl_window)
        if self._sdl_gl_context is None:
            raise RuntimeError(SDL_GetError().decode('utf8'))
        assert isinstance(self._sdl_gl_context, int)

        glPixelStorei(GL_PACK_ALIGNMENT, 1)
        glPixelStorei(GL_UNPACK_ALIGNMENT, 1)

    def __del__(self) -> None:
        if self._sdl_window is not None:
            SDL_DestroyWindow(self._sdl_window)
            self._sdl_window = None
        if self._sdl_gl_context is not None:
            SDL_GL_DeleteContext(self._sdl_gl_context)
            self._sdl_gl_context = None

    @property
    def is_open(self) -> bool:
        return self._sdl_gl_context is not None

    @property
    def sdl_gl_context(self) -> int:
        assert self._sdl_gl_context is not None
        return self._sdl_gl_context


def get_gl_context() -> GlContext:
    global singleton
    if singleton is not None:
        gl_context = singleton()
        if gl_context is not None:
            return gl_context
    gl_context = GlContext()
    singleton = ref(gl_context)
    return gl_context
