
from __future__ import annotations

__all__ = ['TextureComponents', 'TextureDataType', 'TextureView', 'Texture2d']

# gamut
from gamut._glcontext import release_gl_context, require_gl_context
# python
from ctypes import (c_byte, c_float, c_int, c_short, c_ubyte, c_uint, c_ushort,
                    c_void_p)
from ctypes import POINTER as c_pointer
from ctypes import cast as c_cast
from ctypes import sizeof as c_sizeof
from enum import Enum
from typing import Final, Optional
# numpy
from numpy import array as np_array
# pyopengl
from OpenGL.GL import (GL_BYTE, GL_DEPTH_COMPONENT, GL_DEPTH_STENCIL, GL_FLOAT,
                       GL_INT, GL_PIXEL_PACK_BUFFER, GL_READ_ONLY, GL_RED,
                       GL_RG, GL_RGB, GL_RGBA, GL_SHORT, GL_STREAM_READ,
                       GL_TEXTURE_2D, GL_UNSIGNED_BYTE, GL_UNSIGNED_INT,
                       GL_UNSIGNED_INT_24_8, GL_UNSIGNED_SHORT, glBindBuffer,
                       glBindTexture, glBufferData, glDeleteBuffers,
                       glDeleteTextures, glGenBuffers, glGenerateMipmap,
                       glGenTextures, glGetTexImage, glMapBuffer, glTexImage2D,
                       glUnmapBuffer)


class TextureComponents(Enum):
    R = GL_RED
    RG = GL_RG
    RGB = GL_RGB
    RGBA = GL_RGBA
    D = GL_DEPTH_COMPONENT
    DS = GL_DEPTH_STENCIL


class TextureDataType(Enum):
    UNSIGNED_BYTE = GL_UNSIGNED_BYTE
    BYTE = GL_BYTE
    UNSIGNED_SHORT = GL_UNSIGNED_SHORT
    SHORT = GL_SHORT
    UNSIGNED_INT = GL_UNSIGNED_INT
    INT = GL_INT
    FLOAT = GL_FLOAT


TEXTURE_COMPONENTS_COUNT: Final = {
    TextureComponents.R: 1,
    TextureComponents.RG: 2,
    TextureComponents.RGB: 3,
    TextureComponents.RGBA: 4,
    TextureComponents.D: 1,
    TextureComponents.DS: 1
}


TEXTURE_DATA_TYPE_SIZE: Final = {
    TextureDataType.UNSIGNED_BYTE: c_sizeof(c_ubyte),
    TextureDataType.BYTE: c_sizeof(c_byte),
    TextureDataType.UNSIGNED_SHORT: c_sizeof(c_ushort),
    TextureDataType.SHORT: c_sizeof(c_short),
    TextureDataType.UNSIGNED_INT: c_sizeof(c_uint),
    TextureDataType.INT: c_sizeof(c_int),
    TextureDataType.FLOAT: c_sizeof(c_float),
}


class Texture2d:

    def __init__(
        self,
        width: int, height: int,
        components: TextureComponents,
        data_type: TextureDataType,
        data: bytes
    ):
        self._gl_context = require_gl_context()

        if not isinstance(width, int):
            raise TypeError('width must be an int')
        if not isinstance(height, int):
            raise TypeError('height must be an int')
        if not isinstance(components, TextureComponents):
            raise TypeError(f'components must be {TextureComponents}')
        if not isinstance(data_type, TextureDataType):
            raise TypeError(f'data_type must be {TextureDataType}')
        if not isinstance(data, bytes):
            raise TypeError(f'data must be bytes')

        if width < 1:
            raise ValueError('width must be > 0')
        if height < 1:
            raise ValueError('height must be > 0')

        expected_data_length = (
            width * height *
            TEXTURE_COMPONENTS_COUNT[components] *
            TEXTURE_DATA_TYPE_SIZE[data_type]
        )
        if len(data) != expected_data_length:
            raise ValueError('too much or not enough data')

        self._size = (width, height)
        self._components = components

        gl_data_type = data_type.value
        if components == TextureComponents.DS:
            if data_type != TextureDataType.UNSIGNED_INT:
                raise ValueError(
                    f'data_type must be {TextureDataType.UNSIGNED_INT} when '
                    f'components is {TextureComponents.DS}'
                )
            gl_data_type = GL_UNSIGNED_INT_24_8

        self._gl = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, self._gl)
        glTexImage2D(
            GL_TEXTURE_2D,
            0,
            components.value,
            width, height,
            0,
            components.value, gl_data_type, data
        )
        # depth/stencil textures cannot have mipmaps, raises an invalid
        # operation error on some platforms, probably a noop on others
        if components != TextureComponents.DS:
            glGenerateMipmap(GL_TEXTURE_2D)

    def __del__(self) -> None:
        self.close()

    def close(self) -> None:
        if hasattr(self, '_gl') and self._gl is not None:
            glDeleteTextures(np_array([self._gl]))
            self._gl = None
        self._gl_context = release_gl_context(self._gl_context)

    @property
    def components(self) -> TextureComponents:
        return self._components

    @property
    def size(self) -> tuple[int, int]:
        return self._size

    @property
    def is_open(self) -> bool:
        return self._gl is not None


Texture2d.__module__ = 'gamut.graphics'


class TextureView:

    def __init__(self, texture: Texture2d, data_type: TextureDataType):
        self._gl_context = require_gl_context()

        if not isinstance(texture, Texture2d):
            raise TypeError(f'texture must be {Texture2d}')
        if not isinstance(data_type, TextureDataType):
            raise TypeError(f'data_type must be {TextureDataType}')

        if not texture.is_open:
            raise RuntimeError('texture is closed')

        gl_data_type = data_type.value
        if texture.components == TextureComponents.DS:
            if data_type != TextureDataType.UNSIGNED_INT:
                raise ValueError(
                    f'data_type must be {TextureDataType.UNSIGNED_INT} when '
                    f'components is {TextureComponents.DS}'
                )
            gl_data_type = GL_UNSIGNED_INT_24_8

        self._texture: Optional[Texture2d] = texture
        self._gl = glGenBuffers(1)

        self._length = (
            texture.size[0] * texture.size[1] *
            TEXTURE_COMPONENTS_COUNT[texture.components] *
            TEXTURE_DATA_TYPE_SIZE[data_type]
        )

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
        self._map: Optional[c_void_p] = c_void_p(glMapBuffer(
            GL_PIXEL_PACK_BUFFER,
            GL_READ_ONLY
        ))

    def __del__(self) -> None:
        self.close()

    def _ensure_open(self, *, include_texture: bool = True) -> None:
        if self._gl is None:
            raise RuntimeError('texture view is closed')
        assert self._texture is not None
        if include_texture and not self._texture.is_open:
            raise RuntimeError('texture is closed')

    def close(self) -> None:
        if hasattr(self, '_map') and self._map is not None:
            assert self._gl
            glBindBuffer(GL_PIXEL_PACK_BUFFER, self._gl)
            glUnmapBuffer(GL_PIXEL_PACK_BUFFER)
            self._map = None
        if hasattr(self, '_gl') and self._gl is not None:
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
