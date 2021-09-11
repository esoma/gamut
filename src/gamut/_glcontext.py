
from __future__ import annotations

__all__ = ['get_gl_context', 'GlContext']

# python
from typing import Any, Optional
from weakref import ref
# pysdl2
from sdl2 import (SDL_CreateWindow, SDL_DestroyWindow, SDL_GetError,
                  SDL_GL_CONTEXT_PROFILE_CORE, SDL_GL_CONTEXT_PROFILE_MASK,
                  SDL_GL_CreateContext, SDL_GL_DeleteContext,
                  SDL_GL_SetAttribute, SDL_WINDOW_HIDDEN, SDL_WINDOW_OPENGL)

_singleton: Optional[ref[GlContext]] = None


class GlContext:
    """The GlContext object encapsulates the lifetime of an OpenGL context.
    Anything that utilizes the OpenGL context directly should carry a reference
    to the GlContext object in order to keep the context alive.

    Typically there is only one GlContext which can be automatically created
    using the "get_gl_context" function.
    """

    _sdl_window: Any
    _sdl_gl_context: Any

    def __init__(self) -> None:
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

    def __del__(self) -> None:
        if self._sdl_window is not None:
            SDL_DestroyWindow(self._sdl_window)
            self._sdl_window = None
        if self._sdl_gl_context is not None:
            SDL_GL_DeleteContext(self._sdl_gl_context)
            self._sdl_gl_context = None

    @property
    def sdl_gl_context(self) -> Any:
        return self._sdl_gl_context


def get_gl_context() -> GlContext:
    global _singleton
    if _singleton is not None:
        gl_context = _singleton()
        if gl_context is not None:
            return gl_context
    gl_context = GlContext()
    _singleton = ref(gl_context)
    return gl_context
