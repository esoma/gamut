
from __future__ import annotations

__all__ = [
    'BlendFactor',
    'BlendFunction',
    'DepthTest',
    'execute_shader',
    'FaceCull',
    'PrimitiveMode',
    'Shader',
    'ShaderAttribute',
    'ShaderUniform',
    'use_shader',
]

# gamut
from ._buffer import (BufferView, BufferViewMap,
                      use_buffer_view_as_element_indexes,
                      use_buffer_view_map_with_shader)
from ._color import Color
from ._rendertarget import (TextureRenderTarget,
                            TextureRenderTargetDepthStencil, use_render_target,
                            WindowRenderTarget)
from ._texture import bind_texture, Texture
# gamut
from gamut._glcontext import release_gl_context, require_gl_context
# python
from ctypes import c_void_p
from enum import Enum
from typing import (Any, Final, Generic, Optional, overload, Sequence, Type,
                    TypeVar, Union)
from weakref import ref
# pyglm
import glm
from glm import array as glm_array
from glm import int32
from glm import value_ptr as glm_value_ptr
# pyopengl
import OpenGL.GL
from OpenGL.GL import (GL_ACTIVE_ATTRIBUTE_MAX_LENGTH, GL_ACTIVE_ATTRIBUTES,
                       GL_ACTIVE_UNIFORM_MAX_LENGTH, GL_ACTIVE_UNIFORMS,
                       GL_BLEND, GL_CULL_FACE, GL_CURRENT_PROGRAM,
                       GL_DEPTH_TEST, GL_FALSE, glBlendColor, glBlendEquation,
                       glBlendFuncSeparate, GLchar, glCullFace,
                       glDeleteProgram, glDepthFunc, glDepthMask, glDisable,
                       glDrawArrays, glDrawArraysInstanced, glDrawElements,
                       glDrawElementsInstanced, glEnable, GLenum,
                       glGetActiveUniform, glGetIntegerv, glGetUniformLocation,
                       GLint, GLsizei)
from OpenGL.GL.shaders import (GL_COMPILE_STATUS, GL_FRAGMENT_SHADER,
                               GL_LINK_STATUS, GL_VERTEX_SHADER,
                               glAttachShader, glCompileShader,
                               glCreateProgram, glCreateShader, glDeleteShader,
                               glGetActiveAttrib, glGetAttribLocation,
                               glGetProgramInfoLog, glGetProgramiv,
                               glGetShaderInfoLog, glGetShaderiv,
                               glLinkProgram, glShaderSource, glUseProgram)

T = TypeVar('T',
    glm.float32, glm.vec2, glm.vec3, glm.vec4,
    glm.double, glm.dvec2, glm.dvec3, glm.dvec4,
    int32, glm.ivec2, glm.ivec3, glm.ivec4,
    glm.uint32, glm.uvec2, glm.uvec3, glm.uvec4,
    glm.bool_,
    glm.mat2x2, glm.mat2x3, glm.mat2x4,
    glm.mat3x2, glm.mat3x3, glm.mat3x4,
    glm.mat4x2, glm.mat4x3, glm.mat4x4,
    glm.dmat2x2, glm.dmat2x3, glm.dmat2x4,
    glm.dmat3x2, glm.dmat3x3, glm.dmat3x4,
    glm.dmat4x2, glm.dmat4x3, glm.dmat4x4,
    Texture,
)


class PrimitiveMode(Enum):
    POINT = OpenGL.GL.GL_POINTS
    LINE = OpenGL.GL.GL_LINES
    LINE_STRIP = OpenGL.GL.GL_LINE_STRIP
    LINE_LOOP = OpenGL.GL.GL_LINE_LOOP
    TRIANGLE = OpenGL.GL.GL_TRIANGLES
    TRIANGLE_STRIP = OpenGL.GL.GL_TRIANGLE_STRIP
    TRIANGLE_FAN = OpenGL.GL.GL_TRIANGLE_FAN


class DepthTest(Enum):
    NEVER = int(OpenGL.GL.GL_NEVER)
    ALWAYS = int(OpenGL.GL.GL_ALWAYS)
    LESS = int(OpenGL.GL.GL_LESS)
    LESS_EQUAL = int(OpenGL.GL.GL_LEQUAL)
    GREATER = int(OpenGL.GL.GL_GREATER)
    GREATER_EQUAL = int(OpenGL.GL.GL_GEQUAL)
    EQUAL = int(OpenGL.GL.GL_EQUAL)
    NOT_EQUAL = int(OpenGL.GL.GL_NOTEQUAL)


class BlendFactor(Enum):
    ZERO = int(OpenGL.GL.GL_ZERO)
    ONE = int(OpenGL.GL.GL_ONE)
    SOURCE_COLOR = int(OpenGL.GL.GL_SRC_COLOR)
    ONE_MINUS_SOURCE_COLOR = int(OpenGL.GL.GL_ONE_MINUS_SRC_COLOR)
    DESTINATION_COLOR = int(OpenGL.GL.GL_DST_COLOR)
    ONE_MINUS_DESTINATION_COLOR = int(OpenGL.GL.GL_ONE_MINUS_DST_COLOR)
    SOURCE_ALPHA = int(OpenGL.GL.GL_SRC_ALPHA)
    ONE_MINUS_SOURCE_ALPHA = int(OpenGL.GL.GL_ONE_MINUS_SRC_ALPHA)
    DESTINATION_ALPHA = int(OpenGL.GL.GL_DST_ALPHA)
    ONE_MINUS_DESTINATION_ALPHA = int(OpenGL.GL.GL_ONE_MINUS_DST_ALPHA)
    BLEND_COLOR = int(OpenGL.GL.GL_CONSTANT_COLOR)
    ONE_MINUS_BLEND_COLOR = int(OpenGL.GL.GL_ONE_MINUS_CONSTANT_COLOR)
    BLEND_ALPHA = int(OpenGL.GL.GL_CONSTANT_COLOR)
    ONE_MINUS_BLEND_ALPHA = int(OpenGL.GL.GL_ONE_MINUS_CONSTANT_ALPHA)


class BlendFunction(Enum):
    ADD = int(OpenGL.GL.GL_FUNC_ADD)
    SUBTRACT = int(OpenGL.GL.GL_FUNC_SUBTRACT)
    SUBTRACT_REVERSED = int(OpenGL.GL.GL_FUNC_REVERSE_SUBTRACT)
    MIN = int(OpenGL.GL.GL_MIN)
    MAX = int(OpenGL.GL.GL_MAX)


class FaceCull(Enum):
    NONE = 0
    FRONT = int(OpenGL.GL.GL_FRONT)
    BACK = int(OpenGL.GL.GL_BACK)


class Shader:

    def __init__(
        self, *,
        vertex: Optional[bytes] = None,
        fragment: Optional[bytes] = None,
    ):
        self._gl_context = require_gl_context()

        if vertex is None and fragment is None:
            raise TypeError('vertex or fragment must be provided')
        if vertex is not None and not isinstance(vertex, bytes):
            raise TypeError('vertex must be bytes')
        if fragment is not None and not isinstance(fragment, bytes):
            raise TypeError('fragment must be bytes')

        stages: list[int] = []

        def add_stage(name: str, code: bytes, type: int) -> None:
            gl = glCreateShader(type)
            stages.append(gl)
            glShaderSource(gl, code)
            glCompileShader(gl)
            if not glGetShaderiv(gl, GL_COMPILE_STATUS):
                raise RuntimeError(
                    f'{name} stage failed to compile:\n' +
                    glGetShaderInfoLog(gl).decode('utf8')
                )

        try:
            if vertex is not None:
                add_stage('vertex', vertex, GL_VERTEX_SHADER)
            if fragment is not None:
                add_stage('fragment', fragment, GL_FRAGMENT_SHADER)

            self._gl = glCreateProgram()
            for stage in stages:
                glAttachShader(self._gl, stage)
            glLinkProgram(self._gl)

            if glGetProgramiv(self._gl, GL_LINK_STATUS) == GL_FALSE:
                raise RuntimeError(
                    'Failed to link:\n' +
                    glGetProgramInfoLog(self._gl).decode('utf8')
                )
        finally:
            for stage in stages:
                glDeleteShader(stage)

        attributes: list[ShaderAttribute] = []
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
            attributes.append(ShaderAttribute(
                name.decode('utf8').rstrip('[0]'),
                GL_TYPE_TO_PY[type.value],
                size.value,
                location
            ))
        self._attributes = tuple(attributes)

        uniforms: list[ShaderUniform] = []
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
            uniforms.append(ShaderUniform(
                name.decode('utf8').rstrip('[0]'),
                GL_TYPE_TO_PY[type.value],
                size.value,
                location
            ))
        self._uniforms = tuple(uniforms)

        self._inputs: dict[str, Union[ShaderAttribute, ShaderUniform]] = {
            **{attribute.name: attribute for attribute in attributes},
            **{uniform.name: uniform for uniform in uniforms},
        }

        self._next_texture_index = 0

    def __del__(self) -> None:
        self.close()

    def __getitem__(self, name: str) -> Union[ShaderAttribute, ShaderUniform]:
        return self._inputs[name]

    def _ensure_open(self) -> None:
        if self._gl is None:
            raise RuntimeError('shader is closed')

    def _set_uniform(
        self,
        uniform: ShaderUniform[Any],
        value: Union[
            glm.float32, glm.array[glm.float32],
            glm.vec2, glm.array[glm.vec2],
            glm.vec3, glm.array[glm.vec3],
            glm.vec4, glm.array[glm.vec4],
            glm.double, glm.array[glm.double],
            glm.dvec2, glm.array[glm.dvec2],
            glm.dvec3, glm.array[glm.dvec3],
            glm.dvec4, glm.array[glm.dvec4],
            int32, glm.array[int32],
            glm.ivec2, glm.array[glm.ivec2],
            glm.ivec3, glm.array[glm.ivec3],
            glm.ivec4, glm.array[glm.ivec4],
            glm.uint32, glm.array[glm.uint32],
            glm.uvec2, glm.array[glm.uvec2],
            glm.uvec3, glm.array[glm.uvec3],
            glm.uvec4, glm.array[glm.uvec4],
            glm.bool_,
            glm.mat2x2, glm.array[glm.mat2x2],
            glm.mat2x3, glm.array[glm.mat2x3],
            glm.mat2x4, glm.array[glm.mat2x4],
            glm.mat3x2, glm.array[glm.mat3x2],
            glm.mat3x3, glm.array[glm.mat3x3],
            glm.mat3x4, glm.array[glm.mat3x4],
            glm.mat4x2, glm.array[glm.mat4x2],
            glm.mat4x3, glm.array[glm.mat4x3],
            glm.mat4x4, glm.array[glm.mat4x4],
            glm.dmat2x2, glm.array[glm.dmat2x2],
            glm.dmat2x3, glm.array[glm.dmat2x3],
            glm.dmat2x4, glm.array[glm.dmat2x4],
            glm.dmat3x2, glm.array[glm.dmat3x2],
            glm.dmat3x3, glm.array[glm.dmat3x3],
            glm.dmat3x4, glm.array[glm.dmat3x4],
            glm.dmat4x2, glm.array[glm.dmat4x2],
            glm.dmat4x3, glm.array[glm.dmat4x3],
            glm.dmat4x4, glm.array[glm.dmat4x4],
            Texture, Sequence[Texture],
        ],
    ) -> None:
        assert glGetIntegerv(GL_CURRENT_PROGRAM) == self._gl
        assert uniform in self._uniforms
        input_value: Any = None

        if uniform.type is Texture:
            if uniform.size > 1:
                try:
                    length = len(value) # type: ignore
                    value_iter = iter(value) # type: ignore
                except TypeError:
                    raise ValueError(
                        f'expected sequence of {Texture} for {uniform.name} '
                        f'(got {type(value)})'
                    )
                if length != uniform.size:
                    raise ValueError(
                        f'expected sequence of length {uniform.size} '
                        f'for {uniform.name} '
                        f'(got sequence of length {length})'
                    )
                texture_values: list[int] = []
                for texture in value_iter:
                    if not isinstance(texture, Texture):
                        raise ValueError(
                            f'expected sequence of {Texture} '
                            f'for {uniform.name} '
                            f'(found {texture} in sequence)'
                        )
                    bind_texture(texture, self._next_texture_index)
                    texture_values.append(self._next_texture_index)
                    self._next_texture_index += 1
                value = glm_array.from_numbers(int32, *texture_values)
                input_value = value.ptr
            else:
                if not isinstance(value, Texture):
                    raise ValueError(
                        f'expected {Texture} for {uniform.name} '
                        f'(got {type(value)})'
                    )
                bind_texture(value, self._next_texture_index)
                value = int32(self._next_texture_index)
                self._next_texture_index += 1
                input_value = value.value
        else:
            if uniform.size > 1:
                if not isinstance(value, glm_array):
                    raise ValueError(
                        f'expected {glm.array} for {uniform.name} '
                        f'(got {type(value)})'
                    )
                if not issubclass(value.element_type, uniform._set_type):
                    raise ValueError(
                        f'expected array of {uniform._set_type} '
                        f'for {uniform.name} '
                        f'(got array of {value.element_type})'
                    )
                if len(value) != uniform.size:
                    raise ValueError(
                        f'expected array of length {uniform.size} '
                        f'for {uniform.name} '
                        f'(got array of length {len(value)})'
                    )
                input_value = value.ptr
            else:
                assert uniform.size == 1
                if not isinstance(value, uniform._set_type):
                    raise ValueError(
                        f'expected {uniform._set_type} for {uniform.name} '
                        f'(got {type(value)})'
                    )
                if uniform._set_type in POD_UNIFORM_TYPES:
                    input_value = value.value
                else:
                    input_value = glm_value_ptr(value)

        uniform._setter(uniform.location, uniform.size, input_value)

    def close(self) -> None:
        global shader_in_use
        if shader_in_use and shader_in_use() is self:
            glUseProgram(0)
            shader_in_use = None
        if hasattr(self, "_gl") and self._gl is not None:
            glDeleteProgram(self._gl)
            self._gl = None
        self._gl_context = release_gl_context(self._gl_context)


    @property
    def attributes(self) -> tuple[ShaderAttribute, ...]:
        self._ensure_open()
        return self._attributes

    @property
    def uniforms(self) -> tuple[ShaderUniform, ...]:
        self._ensure_open()
        return self._uniforms

    @property
    def is_open(self) -> bool:
        return self._gl is not None


class ShaderAttribute(Generic[T]):

    def __init__(
        self,
        name: str,
        type: Type[T],
        size: int,
        location: int
    ) -> None:
        self._name = name
        self._type: Type[T] = type
        self._size = size
        self._location = location

    @property
    def name(self) -> str:
        return self._name

    @property
    def type(self) -> Type[T]:
        return self._type

    @property
    def size(self) -> int:
        return self._size

    @property
    def location(self) -> int:
        return self._location


class ShaderUniform(Generic[T]):

    def __init__(
        self,
        name: str,
        type: Type[T],
        size: int,
        location: int
    ) -> None:
        self._name = name
        self._type: Type[T] = type
        self._size = size
        self._location = location
        self._setter = TYPE_TO_UNIFORM_SETTER[self._type]
        self._set_type: Any = int32 if type is Texture else type

    @property
    def name(self) -> str:
        return self._name

    @property
    def type(self) -> Type[T]:
        return self._type

    @property
    def size(self) -> int:
        return self._size

    @property
    def location(self) -> int:
        return self._location


shader_in_use: Optional[ref[Shader]] = None


def use_shader(shader: Shader) -> None:
    global shader_in_use
    shader._next_texture_index = 0
    shader._ensure_open()
    if shader_in_use and shader_in_use() is shader:
        return
    glUseProgram(shader._gl)
    shader_in_use = ref(shader)


@overload
def execute_shader(
    render_target: Union[TextureRenderTarget, WindowRenderTarget],
    shader: Shader,
    primitive_mode: PrimitiveMode,
    buffer_view_map: BufferViewMap,
    uniforms: dict[str, Union[
        glm.float32, glm.array[glm.float32],
        glm.vec2, glm.array[glm.vec2],
        glm.vec3, glm.array[glm.vec3],
        glm.vec4, glm.array[glm.vec4],
        glm.double, glm.array[glm.double],
        glm.dvec2, glm.array[glm.dvec2],
        glm.dvec3, glm.array[glm.dvec3],
        glm.dvec4, glm.array[glm.dvec4],
        int32, glm.array[int32],
        glm.ivec2, glm.array[glm.ivec2],
        glm.ivec3, glm.array[glm.ivec3],
        glm.ivec4, glm.array[glm.ivec4],
        glm.uint32, glm.array[glm.uint32],
        glm.uvec2, glm.array[glm.uvec2],
        glm.uvec3, glm.array[glm.uvec3],
        glm.uvec4, glm.array[glm.uvec4],
        glm.bool_,
        glm.mat2x2, glm.array[glm.mat2x2],
        glm.mat2x3, glm.array[glm.mat2x3],
        glm.mat2x4, glm.array[glm.mat2x4],
        glm.mat3x2, glm.array[glm.mat3x2],
        glm.mat3x3, glm.array[glm.mat3x3],
        glm.mat3x4, glm.array[glm.mat3x4],
        glm.mat4x2, glm.array[glm.mat4x2],
        glm.mat4x3, glm.array[glm.mat4x3],
        glm.mat4x4, glm.array[glm.mat4x4],
        glm.dmat2x2, glm.array[glm.dmat2x2],
        glm.dmat2x3, glm.array[glm.dmat2x3],
        glm.dmat2x4, glm.array[glm.dmat2x4],
        glm.dmat3x2, glm.array[glm.dmat3x2],
        glm.dmat3x3, glm.array[glm.dmat3x3],
        glm.dmat3x4, glm.array[glm.dmat3x4],
        glm.dmat4x2, glm.array[glm.dmat4x2],
        glm.dmat4x3, glm.array[glm.dmat4x3],
        glm.dmat4x4, glm.array[glm.dmat4x4],
        Texture, Sequence[Texture],
    ]],
    *,
    blend_source: BlendFactor = BlendFactor.ZERO,
    blend_destination: BlendFactor = BlendFactor.ONE,
    blend_source_alpha: Optional[BlendFactor] = None,
    blend_destination_alpha: Optional[BlendFactor] = None,
    blend_function: BlendFunction = BlendFunction.ADD,
    blend_color: Optional[Color] = None,
    depth_test: DepthTest = DepthTest.ALWAYS,
    depth_write: bool = False,
    face_cull: FaceCull = FaceCull.NONE,
    instances: int = 1,
    index_range: Optional[tuple[int, int]] = None,
) -> None:
    ...


@overload
def execute_shader(
    render_target: Union[TextureRenderTarget, WindowRenderTarget],
    shader: Shader,
    primitive_mode: PrimitiveMode,
    buffer_view_map: BufferViewMap,
    uniforms: dict[str, Union[
        glm.float32, glm.array[glm.float32],
        glm.vec2, glm.array[glm.vec2],
        glm.vec3, glm.array[glm.vec3],
        glm.vec4, glm.array[glm.vec4],
        glm.double, glm.array[glm.double],
        glm.dvec2, glm.array[glm.dvec2],
        glm.dvec3, glm.array[glm.dvec3],
        glm.dvec4, glm.array[glm.dvec4],
        int32, glm.array[int32],
        glm.ivec2, glm.array[glm.ivec2],
        glm.ivec3, glm.array[glm.ivec3],
        glm.ivec4, glm.array[glm.ivec4],
        glm.uint32, glm.array[glm.uint32],
        glm.uvec2, glm.array[glm.uvec2],
        glm.uvec3, glm.array[glm.uvec3],
        glm.uvec4, glm.array[glm.uvec4],
        glm.bool_,
        glm.mat2x2, glm.array[glm.mat2x2],
        glm.mat2x3, glm.array[glm.mat2x3],
        glm.mat2x4, glm.array[glm.mat2x4],
        glm.mat3x2, glm.array[glm.mat3x2],
        glm.mat3x3, glm.array[glm.mat3x3],
        glm.mat3x4, glm.array[glm.mat3x4],
        glm.mat4x2, glm.array[glm.mat4x2],
        glm.mat4x3, glm.array[glm.mat4x3],
        glm.mat4x4, glm.array[glm.mat4x4],
        glm.dmat2x2, glm.array[glm.dmat2x2],
        glm.dmat2x3, glm.array[glm.dmat2x3],
        glm.dmat2x4, glm.array[glm.dmat2x4],
        glm.dmat3x2, glm.array[glm.dmat3x2],
        glm.dmat3x3, glm.array[glm.dmat3x3],
        glm.dmat3x4, glm.array[glm.dmat3x4],
        glm.dmat4x2, glm.array[glm.dmat4x2],
        glm.dmat4x3, glm.array[glm.dmat4x3],
        glm.dmat4x4, glm.array[glm.dmat4x4],
        Texture, Sequence[Texture],
    ]],
    *,
    blend_source: BlendFactor = BlendFactor.ZERO,
    blend_destination: BlendFactor = BlendFactor.ONE,
    blend_source_alpha: Optional[BlendFactor] = None,
    blend_destination_alpha: Optional[BlendFactor] = None,
    blend_function: BlendFunction = BlendFunction.ADD,
    blend_color: Optional[Color] = None,
    depth_test: DepthTest = DepthTest.ALWAYS,
    depth_write: bool = False,
    face_cull: FaceCull = FaceCull.NONE,
    instances: int = 1,
    index_buffer_view: Optional[Union[
        BufferView[glm.uint8],
        BufferView[glm.uint16],
        BufferView[glm.uint32],
    ]] = None,
) -> None:
    ...


def execute_shader(
    render_target: Union[TextureRenderTarget, WindowRenderTarget],
    shader: Shader,
    primitive_mode: PrimitiveMode,
    buffer_view_map: BufferViewMap,
    uniforms: dict[str, Union[
        glm.float32, glm.array[glm.float32],
        glm.vec2, glm.array[glm.vec2],
        glm.vec3, glm.array[glm.vec3],
        glm.vec4, glm.array[glm.vec4],
        glm.double, glm.array[glm.double],
        glm.dvec2, glm.array[glm.dvec2],
        glm.dvec3, glm.array[glm.dvec3],
        glm.dvec4, glm.array[glm.dvec4],
        int32, glm.array[int32],
        glm.ivec2, glm.array[glm.ivec2],
        glm.ivec3, glm.array[glm.ivec3],
        glm.ivec4, glm.array[glm.ivec4],
        glm.uint32, glm.array[glm.uint32],
        glm.uvec2, glm.array[glm.uvec2],
        glm.uvec3, glm.array[glm.uvec3],
        glm.uvec4, glm.array[glm.uvec4],
        glm.bool_,
        glm.mat2x2, glm.array[glm.mat2x2],
        glm.mat2x3, glm.array[glm.mat2x3],
        glm.mat2x4, glm.array[glm.mat2x4],
        glm.mat3x2, glm.array[glm.mat3x2],
        glm.mat3x3, glm.array[glm.mat3x3],
        glm.mat3x4, glm.array[glm.mat3x4],
        glm.mat4x2, glm.array[glm.mat4x2],
        glm.mat4x3, glm.array[glm.mat4x3],
        glm.mat4x4, glm.array[glm.mat4x4],
        glm.dmat2x2, glm.array[glm.dmat2x2],
        glm.dmat2x3, glm.array[glm.dmat2x3],
        glm.dmat2x4, glm.array[glm.dmat2x4],
        glm.dmat3x2, glm.array[glm.dmat3x2],
        glm.dmat3x3, glm.array[glm.dmat3x3],
        glm.dmat3x4, glm.array[glm.dmat3x4],
        glm.dmat4x2, glm.array[glm.dmat4x2],
        glm.dmat4x3, glm.array[glm.dmat4x3],
        glm.dmat4x4, glm.array[glm.dmat4x4],
        Texture, Sequence[Texture]
    ]],
    *,
    blend_source: BlendFactor = BlendFactor.ZERO,
    blend_destination: BlendFactor = BlendFactor.ONE,
    blend_source_alpha: Optional[BlendFactor] = None,
    blend_destination_alpha: Optional[BlendFactor] = None,
    blend_function: BlendFunction = BlendFunction.ADD,
    blend_color: Optional[Color] = None,
    depth_test: DepthTest = DepthTest.ALWAYS,
    depth_write: bool = False,
    face_cull: FaceCull = FaceCull.NONE,
    instances: int = 1,
    index_range: Optional[tuple[int, int]] = None,
    index_buffer_view: Optional[Union[
        BufferView[glm.uint8],
        BufferView[glm.uint16],
        BufferView[glm.uint32],
    ]] = None,
) -> None:
    if index_buffer_view is None and index_range is None:
        raise TypeError('index_buffer_view or index_range must be supplied')
    if index_buffer_view is not None and index_range is not None:
        raise TypeError(
            'both index_buffer_view and index_range cannot be supplied'
        )
    for uniform_name in uniforms:
        input: Optional[Union[ShaderAttribute, ShaderUniform]] = None
        try:
            input = shader[uniform_name]
        except KeyError:
            pass
        if not isinstance(input, ShaderUniform):
            raise ValueError(
                f'shader does not accept a uniform called "{uniform_name}"'
            )
    uniform_values: list[tuple[ShaderUniform, Any]] = []
    for uniform in shader.uniforms:
        try:
            value = uniforms[uniform.name]
        except KeyError:
            raise ValueError(f'missing uniform: {uniform.name}')
        uniform_values.append((uniform, value))
    if instances < 0:
        raise ValueError('instances must be 0 or more')
    elif instances == 0:
        return

    if depth_test == DepthTest.NEVER:
        return
    if not depth_write and depth_test == DepthTest.ALWAYS:
        glDisable(GL_DEPTH_TEST)
    else:
        if isinstance(render_target, TextureRenderTarget):
            if (render_target.depth_stencil ==
                TextureRenderTargetDepthStencil.NONE):
                raise ValueError(
                    f'cannot execute shader with {depth_test=} and '
                    f'{depth_write=} on TextureRenderTarget without a depth '
                    f'buffer'
                )
        glEnable(GL_DEPTH_TEST)
        glDepthMask(bool(depth_write))
        glDepthFunc(depth_test.value)

    if blend_source_alpha is None:
        blend_source_alpha = blend_source
    if blend_destination_alpha is None:
        blend_destination_alpha = blend_destination
    if blend_color is None:
        blend_color = Color(1, 1, 1, 1)

    if (blend_source == BlendFactor.ONE and
        blend_source_alpha == BlendFactor.ONE and
        blend_destination == BlendFactor.ZERO and
        blend_destination_alpha == BlendFactor.ZERO):
        glDisable(GL_BLEND)
    else:
        glEnable(GL_BLEND)
        glBlendFuncSeparate(
            blend_source.value,
            blend_destination.value,
            blend_source_alpha.value,
            blend_destination_alpha.value
        )
        glBlendEquation(blend_function.value)
        glBlendColor(*blend_color)

    if face_cull == FaceCull.NONE:
        glDisable(GL_CULL_FACE)
    else:
        glEnable(GL_CULL_FACE)
        glCullFace(face_cull.value)

    use_render_target(render_target, True, False)
    use_shader(shader)

    for uniform, value in uniform_values:
        shader._set_uniform(uniform, value)
    use_buffer_view_map_with_shader(buffer_view_map, shader)

    if index_buffer_view is None:
        assert index_range is not None
        if instances > 1:
            glDrawArraysInstanced(
                primitive_mode.value,
                index_range[0],
                index_range[1],
                instances
            )
        else:
            glDrawArrays(
                primitive_mode.value,
                index_range[0],
                index_range[1]
            )
    else:
        index_gl_type = use_buffer_view_as_element_indexes(index_buffer_view)
        if instances > 1:
            glDrawElementsInstanced(
                primitive_mode.value,
                len(index_buffer_view),
                index_gl_type,
                c_void_p(0),
                instances,
            )
        else:
            glDrawElements(
                primitive_mode.value,
                len(index_buffer_view),
                index_gl_type,
                c_void_p(0),
            )


POD_UNIFORM_TYPES: Final = {
    glm.float32,
    glm.double,
    int32,
    glm.uint32,
    glm.bool_,
}


def wrap_uniform_matrix(f: Any) -> Any:
    def _(location: Any, count: Any, value: Any) -> None:
        f(location, count, GL_FALSE, value)
    return _


TYPE_TO_UNIFORM_SETTER: Final[dict[Any, Any]] = {
    glm.float32: OpenGL.GL.glUniform1fv,
    glm.vec2: OpenGL.GL.glUniform2fv,
    glm.vec3: OpenGL.GL.glUniform3fv,
    glm.vec4: OpenGL.GL.glUniform4fv,

    glm.double: OpenGL.GL.glUniform1dv,
    glm.dvec2: OpenGL.GL.glUniform2dv,
    glm.dvec3: OpenGL.GL.glUniform3dv,
    glm.dvec4: OpenGL.GL.glUniform4dv,

    int32: OpenGL.GL.glUniform1iv,
    glm.ivec2: OpenGL.GL.glUniform2iv,
    glm.ivec3: OpenGL.GL.glUniform3iv,
    glm.ivec4: OpenGL.GL.glUniform4iv,

    glm.uint32: OpenGL.GL.glUniform1uiv,
    glm.uvec2: OpenGL.GL.glUniform2uiv,
    glm.uvec3: OpenGL.GL.glUniform3uiv,
    glm.uvec4: OpenGL.GL.glUniform4uiv,

    glm.bool_: OpenGL.GL.glUniform1iv,

    glm.mat2x2: wrap_uniform_matrix(OpenGL.GL.glUniformMatrix2fv),
    glm.mat2x3: wrap_uniform_matrix(OpenGL.GL.glUniformMatrix2x3fv),
    glm.mat2x4: wrap_uniform_matrix(OpenGL.GL.glUniformMatrix2x4fv),
    glm.mat3x2: wrap_uniform_matrix(OpenGL.GL.glUniformMatrix3x2fv),
    glm.mat3x3: wrap_uniform_matrix(OpenGL.GL.glUniformMatrix3fv),
    glm.mat3x4: wrap_uniform_matrix(OpenGL.GL.glUniformMatrix3x4fv),
    glm.mat4x2: wrap_uniform_matrix(OpenGL.GL.glUniformMatrix4x2fv),
    glm.mat4x3: wrap_uniform_matrix(OpenGL.GL.glUniformMatrix4x3fv),
    glm.mat4x4: wrap_uniform_matrix(OpenGL.GL.glUniformMatrix4fv),

    glm.dmat2x2: wrap_uniform_matrix(OpenGL.GL.glUniformMatrix2dv),
    glm.dmat2x3: wrap_uniform_matrix(OpenGL.GL.glUniformMatrix2x3dv),
    glm.dmat2x4: wrap_uniform_matrix(OpenGL.GL.glUniformMatrix2x4dv),
    glm.dmat3x2: wrap_uniform_matrix(OpenGL.GL.glUniformMatrix3x2dv),
    glm.dmat3x3: wrap_uniform_matrix(OpenGL.GL.glUniformMatrix3dv),
    glm.dmat3x4: wrap_uniform_matrix(OpenGL.GL.glUniformMatrix3x4dv),
    glm.dmat4x2: wrap_uniform_matrix(OpenGL.GL.glUniformMatrix4x2dv),
    glm.dmat4x3: wrap_uniform_matrix(OpenGL.GL.glUniformMatrix4x3dv),
    glm.dmat4x4: wrap_uniform_matrix(OpenGL.GL.glUniformMatrix4dv),

    Texture: OpenGL.GL.glUniform1iv,
}


GL_TYPE_TO_PY: Final = {
    OpenGL.GL.GL_FLOAT: glm.float32,
    OpenGL.GL.GL_FLOAT_VEC2: glm.vec2,
    OpenGL.GL.GL_FLOAT_VEC3: glm.vec3,
    OpenGL.GL.GL_FLOAT_VEC4: glm.vec4,

    OpenGL.GL.GL_DOUBLE: glm.double,
    OpenGL.GL.GL_DOUBLE_VEC2: glm.dvec2,
    OpenGL.GL.GL_DOUBLE_VEC3: glm.dvec3,
    OpenGL.GL.GL_DOUBLE_VEC4: glm.dvec4,

    OpenGL.GL.GL_INT: int32,
    OpenGL.GL.GL_INT_VEC2: glm.ivec2,
    OpenGL.GL.GL_INT_VEC3: glm.ivec3,
    OpenGL.GL.GL_INT_VEC4: glm.ivec4,

    OpenGL.GL.GL_UNSIGNED_INT: glm.uint32,
    OpenGL.GL.GL_UNSIGNED_INT_VEC2: glm.uvec2,
    OpenGL.GL.GL_UNSIGNED_INT_VEC3: glm.uvec3,
    OpenGL.GL.GL_UNSIGNED_INT_VEC4: glm.uvec4,

    OpenGL.GL.GL_BOOL: glm.bool_,

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

    OpenGL.GL.GL_SAMPLER_1D: Texture,
    OpenGL.GL.GL_INT_SAMPLER_1D: Texture,
    OpenGL.GL.GL_UNSIGNED_INT_SAMPLER_1D: Texture,
    OpenGL.GL.GL_SAMPLER_2D: Texture,
    OpenGL.GL.GL_INT_SAMPLER_2D: Texture,
    OpenGL.GL.GL_UNSIGNED_INT_SAMPLER_2D: Texture,
    OpenGL.GL.GL_SAMPLER_3D: Texture,
    OpenGL.GL.GL_INT_SAMPLER_3D: Texture,
    OpenGL.GL.GL_UNSIGNED_INT_SAMPLER_3D: Texture,
    OpenGL.GL.GL_SAMPLER_CUBE: Texture,
    OpenGL.GL.GL_INT_SAMPLER_CUBE: Texture,
    OpenGL.GL.GL_UNSIGNED_INT_SAMPLER_CUBE: Texture,
    OpenGL.GL.GL_SAMPLER_2D_RECT: Texture,
    OpenGL.GL.GL_INT_SAMPLER_2D_RECT: Texture,
    OpenGL.GL.GL_UNSIGNED_INT_SAMPLER_2D_RECT: Texture,
    OpenGL.GL.GL_SAMPLER_1D_ARRAY: Texture,
    OpenGL.GL.GL_INT_SAMPLER_1D_ARRAY: Texture,
    OpenGL.GL.GL_UNSIGNED_INT_SAMPLER_1D_ARRAY: Texture,
    OpenGL.GL.GL_SAMPLER_2D_ARRAY: Texture,
    OpenGL.GL.GL_INT_SAMPLER_2D_ARRAY: Texture,
    OpenGL.GL.GL_UNSIGNED_INT_SAMPLER_2D_ARRAY: Texture,
    OpenGL.GL.GL_SAMPLER_CUBE_MAP_ARRAY: Texture,
    OpenGL.GL.GL_INT_SAMPLER_CUBE_MAP_ARRAY: Texture,
    OpenGL.GL.GL_UNSIGNED_INT_SAMPLER_CUBE_MAP_ARRAY: Texture,
    OpenGL.GL.GL_SAMPLER_BUFFER: Texture,
    OpenGL.GL.GL_INT_SAMPLER_BUFFER: Texture,
    OpenGL.GL.GL_UNSIGNED_INT_SAMPLER_BUFFER: Texture,
    OpenGL.GL.GL_SAMPLER_2D_MULTISAMPLE: Texture,
    OpenGL.GL.GL_INT_SAMPLER_2D_MULTISAMPLE: Texture,
    OpenGL.GL.GL_UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE: Texture,
    OpenGL.GL.GL_SAMPLER_2D_MULTISAMPLE_ARRAY: Texture,
    OpenGL.GL.GL_INT_SAMPLER_2D_MULTISAMPLE_ARRAY: Texture,
    OpenGL.GL.GL_UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE_ARRAY: Texture,
    OpenGL.GL.GL_SAMPLER_1D_SHADOW: Texture,
    OpenGL.GL.GL_SAMPLER_2D_SHADOW: Texture,
    OpenGL.GL.GL_SAMPLER_CUBE_SHADOW: Texture,
    OpenGL.GL.GL_SAMPLER_2D_RECT_SHADOW: Texture,
    OpenGL.GL.GL_SAMPLER_1D_ARRAY_SHADOW: Texture,
    OpenGL.GL.GL_SAMPLER_2D_ARRAY_SHADOW: Texture,
}
