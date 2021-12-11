
from __future__ import annotations

__all__ = ['TextureView']

# gamut
from ._texture import (get_texture_gl_target, GL_TEXTURE_CUBE_MAP_TARGETS,
                       Texture, TEXTURE_COMPONENTS_COUNT,
                       TEXTURE_DATA_TYPE_TO_GL_DATA_TYPE, TEXTURE_DATA_TYPES,
                       TextureComponents, TextureDataType, TextureType)
# gamut
from gamut._glcontext import release_gl_context, require_gl_context
# python
from ctypes import POINTER as c_pointer
from ctypes import c_byte, c_void_p
from ctypes import cast as c_cast
from ctypes import sizeof as c_sizeof
from math import prod
from typing import Any
# pyglm
from glm import uint32
# pyopengl
from OpenGL.GL import (GL_PIXEL_PACK_BUFFER, GL_READ_ONLY, GL_STREAM_READ,
                       GL_UNSIGNED_INT_24_8, glBindBuffer, glBindTexture,
                       glBufferData, glDeleteBuffers, glGenBuffers,
                       glGetTexImage, glMapBuffer, glUnmapBuffer)


class TextureView:

    def __init__(self, texture: Texture, data_type: type[TextureDataType]):
        self._gls: Any = None
        self._maps: list[c_void_p] | None = None
        self._gl_context = require_gl_context()
        # check texture
        if not isinstance(texture, Texture):
            raise TypeError(f'texture must be {Texture}')
        if not texture.is_open:
            raise RuntimeError('texture is closed')
        self._texture: Texture | None = texture
        # check data type
        try:
            gl_data_type = TEXTURE_DATA_TYPE_TO_GL_DATA_TYPE[data_type]
        except KeyError:
            data_types = ', '.join(sorted((
                str(t) for t in TEXTURE_DATA_TYPES
            )))
            raise TypeError(f'data_type must be {data_types}')
        if texture.components == TextureComponents.DS:
            if data_type != uint32:
                raise ValueError(
                    f'data_type must be {uint32} when '
                    f'components is {TextureComponents.DS}'
                )
            gl_data_type = GL_UNSIGNED_INT_24_8
        # calculate the length
        texture_size = texture.size
        self._length = self._buffer_size = (
            prod(texture_size) *
            TEXTURE_COMPONENTS_COUNT[texture.components] *
            c_sizeof(data_type)
        )
        # special calculations for cube maps
        texture_gl_target = get_texture_gl_target(texture)
        glBindTexture(texture_gl_target, self._texture._gl)
        buffer_targets: tuple[Any, ...]
        if texture.type == TextureType.NORMAL_CUBE:
            self._length *= 6
            buffer_targets = GL_TEXTURE_CUBE_MAP_TARGETS
        else:
            buffer_targets = (texture_gl_target,)
        # generate the buffers to load data into
        if len(buffer_targets) == 1:
            self._gls = [glGenBuffers(1)]
        else:
            self._gls = glGenBuffers(len(buffer_targets))
        self._maps = []
        for gl, buffer_target in zip(self._gls, buffer_targets):
            glBindBuffer(GL_PIXEL_PACK_BUFFER, gl)
            glBufferData(
                GL_PIXEL_PACK_BUFFER,
                self._buffer_size,
                c_void_p(0),
                GL_STREAM_READ,
            )
            glGetTexImage(
                buffer_target,
                0,
                texture.components.value,
                gl_data_type,
                0
            )
            self._maps.append(
                c_void_p(glMapBuffer(GL_PIXEL_PACK_BUFFER, GL_READ_ONLY))
            )

    def __del__(self) -> None:
        self.close()

    def _ensure_open(self, *, include_texture: bool = True) -> None:
        if self._gls is None:
            raise RuntimeError('texture view is closed')
        assert self._texture is not None
        if include_texture and not self._texture.is_open:
            raise RuntimeError('texture is closed')

    def close(self) -> None:
        if self._maps is not None:
            assert self._gls is not None
            for gl in self._gls[:len(self._maps)]:
                glBindBuffer(GL_PIXEL_PACK_BUFFER, gl)
                glUnmapBuffer(GL_PIXEL_PACK_BUFFER)
            self._maps = None
        if self._gls is not None:
            glDeleteBuffers(len(self._gls), self._gls)
            self._gls = None
        self._texture = None
        self._gl_context = release_gl_context(self._gl_context)

    def __len__(self) -> int:
        self._ensure_open()
        return self._length

    @property
    def bytes(self) -> bytes:
        self._ensure_open()
        assert self._maps is not None
        return b''.join(
            bytes(c_cast(map, c_pointer(c_byte * self._buffer_size)).contents)
            for map in self._maps
        )

    @property
    def texture(self) -> Texture:
        self._ensure_open(include_texture=False)
        assert self._texture is not None
        return self._texture

    @property
    def is_open(self) -> bool:
        return self._gls is not None
