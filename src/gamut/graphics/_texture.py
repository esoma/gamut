
__all__ = [
    'bind_texture',
    'MipmapSelection',
    'Texture',
    'TextureDataType',
    'TextureFilter',
    'TEXTURE_DATA_TYPES',
    'TEXTURE_DATA_TYPES_SORTED',
    'TEXTURE_DATA_TYPE_TO_GL_DATA_TYPE',
    'TEXTURE_FILTER_TO_GL_MAG_FILTER',
    'TEXTURE_FILTER_TO_GL_MIN_FILTER',
]

# python
from abc import ABC, abstractmethod
from enum import Enum
from typing import Any, Final, Union
# pyglm
import glm
# pyopengl
import OpenGL.GL


class TextureFilter(Enum):
    NEAREST = 0
    LINEAR = 1


class MipmapSelection(Enum):
    NONE = 0
    NEAREST = 1
    LINEAR = 2


TEXTURE_FILTER_TO_GL_MIN_FILTER: Final = {
    (MipmapSelection.NONE, TextureFilter.NEAREST): OpenGL.GL.GL_NEAREST,
    (MipmapSelection.NONE, TextureFilter.LINEAR): OpenGL.GL.GL_LINEAR,
    (MipmapSelection.NEAREST, TextureFilter.NEAREST):
        OpenGL.GL.GL_NEAREST_MIPMAP_NEAREST,
    (MipmapSelection.NEAREST, TextureFilter.LINEAR):
        OpenGL.GL.GL_NEAREST_MIPMAP_LINEAR,
    (MipmapSelection.LINEAR, TextureFilter.NEAREST):
        OpenGL.GL.GL_LINEAR_MIPMAP_NEAREST,
    (MipmapSelection.LINEAR, TextureFilter.LINEAR):
        OpenGL.GL.GL_LINEAR_MIPMAP_LINEAR,
}


TEXTURE_FILTER_TO_GL_MAG_FILTER: Final = {
    TextureFilter.NEAREST: OpenGL.GL.GL_NEAREST,
    TextureFilter.LINEAR: OpenGL.GL.GL_LINEAR,
}


class Texture(ABC):

    @abstractmethod
    def _bind(self, index: int) -> None:
        ...


TextureDataType = Union[
    glm.uint8, glm.int8,
    glm.uint16, glm.int16,
    glm.uint32, glm.int32,
    glm.float32
]


TEXTURE_DATA_TYPE_TO_GL_DATA_TYPE: Final[dict[type[TextureDataType], Any]] = {
    glm.uint8: OpenGL.GL.GL_UNSIGNED_BYTE,
    glm.int8: OpenGL.GL.GL_BYTE,
    glm.uint16: OpenGL.GL.GL_UNSIGNED_SHORT,
    glm.int16: OpenGL.GL.GL_SHORT,
    glm.uint32: OpenGL.GL.GL_UNSIGNED_INT,
    glm.int32: OpenGL.GL.GL_INT,
    glm.float32: OpenGL.GL.GL_FLOAT,
}


TEXTURE_DATA_TYPES_SORTED: Final = list(
    TEXTURE_DATA_TYPE_TO_GL_DATA_TYPE.keys()
)
TEXTURE_DATA_TYPES: Final = set(TEXTURE_DATA_TYPES_SORTED)


def bind_texture(texture: Texture, index: int) -> None:
    texture._bind(index)
