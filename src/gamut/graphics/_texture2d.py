
from __future__ import annotations

__all__ = ['TextureComponents', 'TextureDataType', 'TextureView', 'Texture2d']

# gamut
from gamut._glcontext import get_gl_context, GlContext
# python
from ctypes import (c_byte, c_float, c_int, c_short, c_ubyte, c_uint, c_ushort,
                    c_void_p)
from ctypes import POINTER as c_pointer
from ctypes import cast as c_cast
from ctypes import sizeof as c_sizeof
from enum import Enum
from typing import Final, Optional
# pyopengl
from OpenGL.GL import (GL_BYTE, GL_DEPTH_COMPONENT, GL_DEPTH_STENCIL, GL_FLOAT,
                       GL_INT, GL_PIXEL_PACK_BUFFER, GL_READ_ONLY, GL_RED,
                       GL_RG, GL_RGB, GL_RGBA, GL_SHORT, GL_STREAM_READ,
                       GL_TEXTURE_2D, GL_UNSIGNED_BYTE, GL_UNSIGNED_INT,
                       GL_UNSIGNED_INT_24_8, GL_UNSIGNED_SHORT, glBindBuffer,
                       glBindTexture, glBufferData, glDeleteTextures,
                       glGenBuffers, glGenerateMipmap, glGenTextures,
                       glMapBuffer, glTexImage2D, glUnmapBuffer)


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
        width = int(width)
        height = int(height)
        data = bytes(data)
        if width < 1:
            raise ValueError('width must be > 0')
        if height < 1:
            raise ValueError('height must be > 0')

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

        self._gl_context: Optional[GlContext] = get_gl_context()
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
        # operation error on some platforms
        if components != TextureComponents.DS:
            glGenerateMipmap(GL_TEXTURE_2D)

    def close(self) -> None:
        self._gl_context = None
        if hasattr(self, '_gl') and self._gl is not None:
            glDeleteTextures(1, [self._gl])
            self._gl = None

    @property
    def components(self) -> TextureComponents:
        return self._components

    @property
    def size(self) -> tuple[int, int]:
        return self._size

    @property
    def is_open(self) -> bool:
        return self._gl is not None


class TextureView:

    def __init__(self, texture: Texture2d, data_type: TextureDataType):
        self._texture = texture
        self._gl_context: Optional[GlContext] = get_gl_context()
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
        self._map: Optional[c_void_p] = c_void_p(glMapBuffer(
            GL_PIXEL_PACK_BUFFER,
            GL_READ_ONLY
        ))

    def close(self) -> None:
        if hasattr(self, '_map') and self._map is not None:
            glBindBuffer(GL_PIXEL_PACK_BUFFER, self._gl)
            glUnmapBuffer(GL_PIXEL_PACK_BUFFER)
        if hasattr(self, '_gl') and self._gl is not None:
            glDeleteTextures(1, [self._gl])
            self._gl = None
        self._gl_context = None

    def __len__(self) -> int:
        return self._length

    @property
    def bytes(self) -> bytes:
        if self._map is None:
            raise RuntimeError('closed')
        return bytes(c_cast(
            self._map,
            c_pointer(c_byte * self._length),
        ).contents)

    @property
    def texture(self) -> Texture2d:
        return self._texture
