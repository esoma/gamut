
from __future__ import annotations

__all__ = ['Shader']

# gamut
from gamut._glcontext import get_gl_context, GlContext
# python
from typing import Final, Optional
# pyglm
import glm
# pyopengl
import OpenGL.GL
from OpenGL.GL import (GL_ACTIVE_ATTRIBUTE_MAX_LENGTH, GL_ACTIVE_ATTRIBUTES,
                       GL_ACTIVE_UNIFORM_MAX_LENGTH, GL_ACTIVE_UNIFORMS,
                       GL_FALSE, GLchar, glDeleteProgram, GLenum,
                       glGetActiveUniform, glGetUniformLocation, GLint,
                       GLsizei)
from OpenGL.GL.shaders import (GL_COMPILE_STATUS, GL_FRAGMENT_SHADER,
                               GL_LINK_STATUS, GL_VERTEX_SHADER,
                               glAttachShader, glCompileShader,
                               glCreateProgram, glCreateShader, glDeleteShader,
                               glGetActiveAttrib, glGetAttribLocation,
                               glGetProgramInfoLog, glGetProgramiv,
                               glGetShaderInfoLog, glGetShaderiv,
                               glLinkProgram, glShaderSource)


class Shader:

    def __init__(
        self, *,
        vertex: Optional[bytes] = None,
        fragment: Optional[bytes] = None,
    ):
        if vertex is None and fragment is None:
            raise TypeError('vertex or fragment must be provided')
        if vertex is not None and not isinstance(vertex, bytes):
            raise TypeError('vertex must be bytes')
        if fragment is not None and not isinstance(fragment, bytes):
            raise TypeError('fragment must be bytes')

        self._gl_context: Optional[GlContext] = get_gl_context()

        stages: list[int] = []

        def add_stage(code: bytes, type: int) -> None:
            gl = glCreateShader(type)
            stages.append(gl)
            glShaderSource(gl, code)
            glCompileShader(gl)
            if not glGetShaderiv(gl, GL_COMPILE_STATUS):
                raise RuntimeError(glGetShaderInfoLog(gl).decode('utf8'))

        try:
            if vertex is not None:
                add_stage(vertex, GL_VERTEX_SHADER)
            if fragment is not None:
                add_stage(fragment, GL_FRAGMENT_SHADER)

            self._gl = glCreateProgram()
            for stage in stages:
                glAttachShader(self._gl, stage)
            glLinkProgram(self._gl)

            if glGetProgramiv(self._gl, GL_LINK_STATUS) == GL_FALSE:
                raise RuntimeError(glGetProgramInfoLog(self._gl))
        finally:
            for stage in stages:
                glDeleteShader(stage)

        attributes = []
        max_attr_length = glGetProgramiv(
            self._gl,
            GL_ACTIVE_ATTRIBUTE_MAX_LENGTH
        )
        attribute_count = glGetProgramiv(self._gl, GL_ACTIVE_ATTRIBUTES)
        for i in range(attribute_count):
            length = GLsizei()
            size = GLint()
            type = GLenum()
            name = (GLchar * max_attr_length)()
            glGetActiveAttrib(
                self._gl, i, max_attr_length,
                length, size, type, name
            )
            name = name.value[:length.value]
            location = glGetAttribLocation(self._gl, name)
            attributes.append((
                name.decode('utf8').rstrip('[0]'),
                GL_TYPE_TO_PY[type.value],
                size.value,
                location
            ))
        self._attributes = tuple(attributes)

        uniforms = []
        max_uni_length = glGetProgramiv(
            self._gl,
            GL_ACTIVE_UNIFORM_MAX_LENGTH
        )
        uniform_count = glGetProgramiv(self._gl, GL_ACTIVE_UNIFORMS)
        for i in range(uniform_count):
            length = GLsizei()
            size = GLint()
            type = GLenum()
            name = (GLchar * max_uni_length)()
            glGetActiveUniform(
                self._gl, i, max_uni_length,
                length, size, type, name
            )
            name = name.value[:length.value]
            location = glGetUniformLocation(self._gl, name)
            uniforms.append((
                name.decode('utf8').rstrip('[0]'),
                GL_TYPE_TO_PY[type.value],
                size.value,
                location
            ))
        self._uniforms = tuple(uniforms)

    def __del__(self) -> None:
        self.close()

    def _ensure_open(self) -> None:
        if self._gl is None:
            raise RuntimeError('shader is closed')

    def close(self) -> None:
        if hasattr(self, "_gl") and self._gl is not None:
            assert self._gl_context is not None
            if self._gl_context.is_open:
                glDeleteProgram(self._gl)
            self._gl = None
        self._gl_context = None

    @property
    def attributes(self) -> tuple:
        self._ensure_open()
        return self._attributes

    @property
    def uniforms(self) -> tuple:
        self._ensure_open()
        return self._uniforms

    @property
    def is_open(self) -> bool:
        return self._gl is not None


GL_TYPE_TO_PY: Final = {
    OpenGL.GL.GL_FLOAT: glm.vec1,
    OpenGL.GL.GL_FLOAT_VEC2: glm.vec2,
    OpenGL.GL.GL_FLOAT_VEC3: glm.vec3,
    OpenGL.GL.GL_FLOAT_VEC4: glm.vec4,

    OpenGL.GL.GL_DOUBLE: glm.dvec1,
    OpenGL.GL.GL_DOUBLE_VEC2: glm.dvec2,
    OpenGL.GL.GL_DOUBLE_VEC3: glm.dvec3,
    OpenGL.GL.GL_DOUBLE_VEC4: glm.dvec4,

    OpenGL.GL.GL_INT: glm.ivec1,
    OpenGL.GL.GL_INT_VEC2: glm.ivec2,
    OpenGL.GL.GL_INT_VEC3: glm.ivec3,
    OpenGL.GL.GL_INT_VEC4: glm.ivec4,

    OpenGL.GL.GL_UNSIGNED_INT: glm.uvec1,
    OpenGL.GL.GL_UNSIGNED_INT_VEC2: glm.uvec2,
    OpenGL.GL.GL_UNSIGNED_INT_VEC3: glm.uvec3,
    OpenGL.GL.GL_UNSIGNED_INT_VEC4: glm.uvec4,

    OpenGL.GL.GL_BOOL: glm.bvec1,
    OpenGL.GL.GL_BOOL_VEC2: glm.bvec2,
    OpenGL.GL.GL_BOOL_VEC3: glm.bvec3,
    OpenGL.GL.GL_BOOL_VEC4: glm.bvec4,

    OpenGL.GL.GL_FLOAT_MAT2: glm.mat2x2,
    OpenGL.GL.GL_FLOAT_MAT3: glm.mat3x3,
    OpenGL.GL.GL_FLOAT_MAT4: glm.mat4x4,
    OpenGL.GL.GL_FLOAT_MAT2x3: glm.mat2x3,
    OpenGL.GL.GL_FLOAT_MAT2x4: glm.mat2x4,
    OpenGL.GL.GL_FLOAT_MAT3x2: glm.mat3x2,
    OpenGL.GL.GL_FLOAT_MAT3x4: glm.mat3x4,
    OpenGL.GL.GL_FLOAT_MAT4x2: glm.mat4x2,
    OpenGL.GL.GL_FLOAT_MAT4x3: glm.mat4x3,

    OpenGL.GL.GL_DOUBLE_MAT2: glm.dmat2x2,
    OpenGL.GL.GL_DOUBLE_MAT3: glm.dmat3x3,
    OpenGL.GL.GL_DOUBLE_MAT4: glm.dmat4x4,
    OpenGL.GL.GL_DOUBLE_MAT2x3: glm.dmat2x3,
    OpenGL.GL.GL_DOUBLE_MAT2x4: glm.dmat2x4,
    OpenGL.GL.GL_DOUBLE_MAT3x2: glm.dmat3x2,
    OpenGL.GL.GL_DOUBLE_MAT3x4: glm.dmat3x4,
    OpenGL.GL.GL_DOUBLE_MAT4x2: glm.dmat4x2,
    OpenGL.GL.GL_DOUBLE_MAT4x3: glm.dmat4x3,

    OpenGL.GL.GL_SAMPLER_2D: glm.ivec1,
}
