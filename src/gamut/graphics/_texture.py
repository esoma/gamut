
__all__ = [
    'Texture',
    'TextureDataType',
    'TEXTURE_DATA_TYPES',
    'TEXTURE_DATA_TYPE_TO_GL_DATA_TYPE',
]

# python
from typing import Any, Final, Union
# pyglm
import glm
# pyopengl
import OpenGL.GL


class Texture:
    pass


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


TEXTURE_DATA_TYPES = set(TEXTURE_DATA_TYPE_TO_GL_DATA_TYPE.keys())
