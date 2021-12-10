
from __future__ import annotations

__all__ = ['TextureView']

# gamut
from ._texture2d import Texture2d
from ._texture import (TEXTURE_COMPONENTS_COUNT,
                       TEXTURE_DATA_TYPE_TO_GL_DATA_TYPE, TEXTURE_DATA_TYPES,
                       TextureComponents, TextureDataType)
# gamut
from gamut._glcontext import release_gl_context, require_gl_context
# python
from ctypes import POINTER as c_pointer
from ctypes import c_byte, c_void_p
from ctypes import cast as c_cast
from ctypes import sizeof as c_sizeof
from typing import Any
# pyglm
from glm import uint32
# pyopengl
from OpenGL.GL import (GL_PIXEL_PACK_BUFFER, GL_READ_ONLY, GL_STREAM_READ,
                       GL_TEXTURE_2D, GL_UNSIGNED_INT_24_8, glBindBuffer,
                       glBindTexture, glBufferData, glDeleteBuffers,
                       glGenBuffers, glGetTexImage, glMapBuffer, glUnmapBuffer)


class TextureView:

    def __init__(self, texture: Texture2d, data_type: type[TextureDataType]):
        self._gl: Any = None
        self._map: c_void_p | None = None
        self._gl_context = require_gl_context()
        # check texture
        if not isinstance(texture, Texture2d):
            raise TypeError(f'texture must be {Texture2d}')
        if not texture.is_open:
            raise RuntimeError('texture is closed')
        self._texture: Texture2d | None = texture
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
        self._length = (
            texture_size.x * texture_size.y *
            TEXTURE_COMPONENTS_COUNT[texture.components] *
            c_sizeof(data_type)
        )
        # generate the buffer to load data into
        self._gl = glGenBuffers(1)
        glBindBuffer(GL_PIXEL_PACK_BUFFER, self._gl)
        glBufferData(
            GL_PIXEL_PACK_BUFFER,
            self._length,
            c_void_p(0),
            GL_STREAM_READ,
        )
        glBindTexture(GL_TEXTURE_2D, self._texture._gl)
        glGetTexImage(
            GL_TEXTURE_2D,
            0,
            texture.components.value,
            gl_data_type,
            0
        )
        self._map = c_void_p(glMapBuffer(GL_PIXEL_PACK_BUFFER, GL_READ_ONLY))

    def __del__(self) -> None:
        self.close()

    def _ensure_open(self, *, include_texture: bool = True) -> None:
        if self._gl is None:
            raise RuntimeError('texture view is closed')
        assert self._texture is not None
        if include_texture and not self._texture.is_open:
            raise RuntimeError('texture is closed')

    def close(self) -> None:
        if self._map is not None:
            assert self._gl
            glBindBuffer(GL_PIXEL_PACK_BUFFER, self._gl)
            glUnmapBuffer(GL_PIXEL_PACK_BUFFER)
            self._map = None
        if self._gl is not None:
            glDeleteBuffers(1, [self._gl])
            self._gl = None
        self._texture = None
        self._gl_context = release_gl_context(self._gl_context)

    def __len__(self) -> int:
        self._ensure_open()
        return self._length

    @property
    def bytes(self) -> bytes:
        self._ensure_open()
        assert self._map is not None
        return bytes(c_cast(
            self._map,
            c_pointer(c_byte * self._length),
        ).contents)

    @property
    def texture(self) -> Texture2d:
        self._ensure_open(include_texture=False)
        assert self._texture is not None
        return self._texture

    @property
    def is_open(self) -> bool:
        return self._gl is not None
