
__all__ = [
    'bind_texture',
    'MipmapSelection',
    'Texture',
    'TextureComponents',
    'TextureDataType',
    'TextureFilter',
    'TextureWrap',
    'TEXTURE_COMPONENTS_COUNT',
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


class TextureComponents(Enum):
    R = OpenGL.GL.GL_RED
    RG = OpenGL.GL.GL_RG
    RGB = OpenGL.GL.GL_RGB
    RGBA = OpenGL.GL.GL_RGBA
    D = OpenGL.GL.GL_DEPTH_COMPONENT
    DS = OpenGL.GL.GL_DEPTH_STENCIL


TEXTURE_COMPONENTS_COUNT: Final = {
    TextureComponents.R: 1,
    TextureComponents.RG: 2,
    TextureComponents.RGB: 3,
    TextureComponents.RGBA: 4,
    TextureComponents.D: 1,
    TextureComponents.DS: 1
}


class MipmapSelection(Enum):
    NONE = 0
    NEAREST = 1
    LINEAR = 2


class TextureFilter(Enum):
    NEAREST = 0
    LINEAR = 1


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


class TextureWrap(Enum):
    CLAMP_TO_EDGE = OpenGL.GL.GL_CLAMP_TO_EDGE
    CLAMP_TO_COLOR = OpenGL.GL.GL_CLAMP_TO_BORDER
    REPEAT = OpenGL.GL.GL_REPEAT
    REPEAT_MIRRORED = OpenGL.GL.GL_MIRRORED_REPEAT
    REPEAT_MIRRORED_THEN_CLAMP_TO_EDGE = OpenGL.GL.GL_MIRROR_CLAMP_TO_EDGE


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
