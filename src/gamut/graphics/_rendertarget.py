
from __future__ import annotations

__all__ = [
    'clear_render_target',
    'read_color_from_render_target',
    'read_depth_from_render_target',
    'read_stencil_from_render_target',
    'TextureRenderTarget',
    'TextureRenderTargetDepthStencil',
    'use_render_target',
    'WindowRenderTarget',
]

# gamut
from ._color import Color
from ._texture2d import Texture2d
# gamut
from gamut._glcontext import get_gl_context
from gamut._window import get_sdl_window_from_window, Window
# python
from ctypes import byref as c_byref
from ctypes import c_int
from enum import Enum
from typing import Optional, Sequence, Union
# pyopengl
from OpenGL.GL import (GL_COLOR_ATTACHMENT0, GL_COLOR_BUFFER_BIT,
                       GL_DEPTH24_STENCIL8, GL_DEPTH_ATTACHMENT,
                       GL_DEPTH_BUFFER_BIT, GL_DEPTH_COMPONENT,
                       GL_DEPTH_COMPONENT24, GL_DEPTH_STENCIL_ATTACHMENT,
                       GL_DRAW_FRAMEBUFFER, GL_FLOAT, GL_FRAMEBUFFER,
                       GL_FRAMEBUFFER_COMPLETE, GL_INT, GL_READ_FRAMEBUFFER,
                       GL_RENDERBUFFER, GL_RGBA, GL_STENCIL_BUFFER_BIT,
                       GL_STENCIL_INDEX, GL_TEXTURE_2D, glBindFramebuffer,
                       glBindRenderbuffer, glCheckFramebufferStatus, glClear,
                       glClearColor, glClearDepthf, glClearStencil,
                       glFramebufferRenderbuffer, glFramebufferTexture2D,
                       glGenFramebuffers, glGenRenderbuffers, glReadPixels,
                       glRenderbufferStorage, glViewport)
# pysdl2
from sdl2 import SDL_GL_GetDrawableSize, SDL_GL_MakeCurrent


class TextureRenderTargetDepthStencil(Enum):
    NONE = 0
    DEPTH = 1
    DEPTH_STENCIL = 2


class TextureRenderTarget:

    def __init__(
        self,
        colors: Sequence[Texture2d],
        depth_stencil: Union[TextureRenderTargetDepthStencil, Texture2d] =
            TextureRenderTargetDepthStencil.NONE
    ):
        assert isinstance(depth_stencil, TextureRenderTargetDepthStencil)

        self._gl_context = get_gl_context()

        self._colors = colors
        self._ds_gl: Optional[int] = None

        if not colors:
            raise ValueError('at least 1 color texture must be supplied')
        sizes = {t.size for t in colors}
        if len(sizes) != 1:
            raise ValueError('all textures must have the same size')
        self._size = list(sizes)[0]

        self._gl = glGenFramebuffers(1)
        glBindFramebuffer(GL_FRAMEBUFFER, self._gl)
        for i, color_texture in enumerate(colors):
            glFramebufferTexture2D(
                GL_FRAMEBUFFER,
                GL_COLOR_ATTACHMENT0 + i,
                GL_TEXTURE_2D,
                color_texture._gl,
                0
            )

        if depth_stencil != TextureRenderTargetDepthStencil.NONE:
            if depth_stencil == TextureRenderTargetDepthStencil.DEPTH_STENCIL:
                sized_internal_format = GL_DEPTH24_STENCIL8
                attachment = GL_DEPTH_STENCIL_ATTACHMENT
            else:
                assert depth_stencil == TextureRenderTargetDepthStencil.DEPTH
                sized_internal_format = GL_DEPTH_COMPONENT24
                attachment = GL_DEPTH_ATTACHMENT
            self._ds_gl = glGenRenderbuffers(1)
            glBindRenderbuffer(GL_RENDERBUFFER, self._ds_gl)
            glRenderbufferStorage(
                GL_RENDERBUFFER,
                sized_internal_format,
                *self._size
            )
            glFramebufferRenderbuffer(
                GL_FRAMEBUFFER,
                attachment,
                GL_RENDERBUFFER,
                self._ds_gl
            )
        if glCheckFramebufferStatus(GL_FRAMEBUFFER) != GL_FRAMEBUFFER_COMPLETE:
            raise RuntimeError('framebuffer incomplete')

    @property
    def colors(self) -> Sequence[Texture2d]:
        return self._colors

    @property
    def size(self) -> tuple[int, int]:
        return self._size


class WindowRenderTarget:

    def __init__(self, window: Window) -> None:
        self._window = window
        self._gl_context = get_gl_context()

    @property
    def size(self) -> tuple[int, int]:
        sdl_window = get_sdl_window_from_window(self._window)
        x = c_int()
        y = c_int()
        SDL_GL_GetDrawableSize(sdl_window, c_byref(x), c_byref(y))
        return (x.value, y.value)

    @property
    def window(self) -> Window:
        return self._window


def use_render_target(
    render_target: Union[TextureRenderTarget, WindowRenderTarget],
    write: bool,
    read: bool
) -> None:
    if write and read:
        target = GL_FRAMEBUFFER
    elif write:
        target = GL_DRAW_FRAMEBUFFER
    elif read:
        target = GL_READ_FRAMEBUFFER
    else:
        return
    if isinstance(render_target, WindowRenderTarget):
        sdl_window = get_sdl_window_from_window(render_target.window)
        SDL_GL_MakeCurrent(
            sdl_window,
            render_target._gl_context._sdl_gl_context
        )
        glBindFramebuffer(target, 0)
        glViewport(0, 0, *render_target.size)
    elif isinstance(render_target, TextureRenderTarget):
        glBindFramebuffer(GL_FRAMEBUFFER, render_target._gl)
        glViewport(0, 0, *render_target.size)
    else:
        raise TypeError(
            f'expected {TextureRenderTarget!r} or {WindowRenderTarget!r}'
        )


def read_color_from_render_target(
    render_target: Union[TextureRenderTarget, WindowRenderTarget],
    x: int, y: int,
    width: int, height: int,
) -> list[list[Color]]:
    use_render_target(render_target, False, True)
    pixels = glReadPixels(x, y, width, height, GL_RGBA, GL_FLOAT)
    return [
        [Color(*column) for column in row]
        for row in pixels
    ]


def read_depth_from_render_target(
    render_target: Union[TextureRenderTarget, WindowRenderTarget],
    x: int, y: int,
    width: int, height: int,
) -> list[list[float]]:
    use_render_target(render_target, False, True)
    pixels = glReadPixels(x, y, width, height, GL_DEPTH_COMPONENT, GL_FLOAT)
    return [
        [column for column in row]
        for row in pixels
    ]


def read_stencil_from_render_target(
    render_target: Union[TextureRenderTarget, WindowRenderTarget],
    x: int, y: int,
    width: int, height: int,
) -> list[list[int]]:
    use_render_target(render_target, False, True)
    pixels = glReadPixels(x, y, width, height, GL_STENCIL_INDEX, GL_INT)
    return [
        [column for column in row]
        for row in pixels
    ]


def clear_render_target(
    render_target: Union[TextureRenderTarget, WindowRenderTarget],
    *,
    color: Optional[Color] = None,
    depth: Optional[float] = None,
    stencil: Optional[int] = None
) -> None:
    use_render_target(render_target, True, False)

    mask = 0
    if color is not None:
        glClearColor(color.red, color.blue, color.green, 1.0)
        mask |= GL_COLOR_BUFFER_BIT
    if depth is not None:
        glClearDepthf(depth)
        mask |= GL_DEPTH_BUFFER_BIT
    if stencil is not None:
        glClearStencil(stencil)
        mask |= GL_STENCIL_BUFFER_BIT
    if mask:
        glClear(mask)
