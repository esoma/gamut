
from __future__ import annotations

__all__ = [
    'BlendFactor',
    'BlendFunction',
    'DepthTest',
    'execute_shader',
    'FaceCull',
    'IndexBuffer',
    'PrimitiveMode',
    'Shader',
    'ShaderAttribute',
    'ShaderExecutionResult',
    'ShaderUniform',
    'UniformMap',
    'use_shader',
]

# gamut
from ._buffer import (BufferView, BufferViewMap,
                      use_buffer_view_as_element_indexes,
                      use_buffer_view_map_with_shader)
from ._rendertarget import (TextureRenderTarget,
                            TextureRenderTargetDepthStencil, use_render_target,
                            WindowRenderTarget)
from ._texture import bind_texture, Texture
# gamut
from gamut._glcontext import (get_gl_context, release_gl_context,
                              require_gl_context)
from gamut.math import (BArray, DArray, DMatrix2x2, DMatrix2x2Array,
                        DMatrix2x3, DMatrix2x3Array, DMatrix2x4,
                        DMatrix2x4Array, DMatrix3x2, DMatrix3x2Array,
                        DMatrix3x3, DMatrix3x3Array, DMatrix3x4,
                        DMatrix3x4Array, DMatrix4x2, DMatrix4x2Array,
                        DMatrix4x3, DMatrix4x3Array, DMatrix4x4,
                        DMatrix4x4Array, DVector2, DVector2Array, DVector3,
                        DVector3Array, DVector4, DVector4Array, FArray,
                        FMatrix2x2, FMatrix2x2Array, FMatrix2x3,
                        FMatrix2x3Array, FMatrix2x4, FMatrix2x4Array,
                        FMatrix3x2, FMatrix3x2Array, FMatrix3x3,
                        FMatrix3x3Array, FMatrix3x4, FMatrix3x4Array,
                        FMatrix4x2, FMatrix4x2Array, FMatrix4x3,
                        FMatrix4x3Array, FMatrix4x4, FMatrix4x4Array, FVector2,
                        FVector2Array, FVector3, FVector3Array, FVector4,
                        FVector4Array, I32Array, I32Vector2, I32Vector2Array,
                        I32Vector3, I32Vector3Array, I32Vector4,
                        I32Vector4Array, U32Array, U32Vector2, U32Vector2Array,
                        U32Vector3, U32Vector3Array, U32Vector4,
                        U32Vector4Array)
# python
import ctypes
from ctypes import c_void_p
from enum import Enum
from typing import (Any, Final, Generic, Optional, overload, Sequence, Type,
                    TypeVar, Union)
from weakref import ref
# pyopengl
import OpenGL.GL
from OpenGL.GL import (GL_ACTIVE_ATTRIBUTE_MAX_LENGTH, GL_ACTIVE_ATTRIBUTES,
                       GL_ACTIVE_UNIFORM_MAX_LENGTH, GL_ACTIVE_UNIFORMS,
                       GL_ANY_SAMPLES_PASSED, GL_BLEND, GL_CULL_FACE,
                       GL_DEPTH_TEST, GL_FALSE, GL_QUERY_RESULT, glBeginQuery,
                       glBlendColor, glBlendEquation, glBlendFuncSeparate,
                       GLchar, glCullFace, glDepthFunc, glDisable,
                       glDrawArrays, glDrawArraysInstanced, glDrawElements,
                       glDrawElementsInstanced, glEnable, glEndQuery, GLenum,
                       glGenQueries, glGetActiveUniform, glGetQueryObjectuiv,
                       glGetUniformLocation, GLint, glPointSize, GLsizei)
from OpenGL.GL.shaders import (GL_COMPILE_STATUS, GL_FRAGMENT_SHADER,
                               GL_GEOMETRY_SHADER, GL_LINK_STATUS,
                               GL_VERTEX_SHADER, glAttachShader,
                               glCompileShader, glCreateProgram,
                               glCreateShader, glDeleteShader,
                               glGetActiveAttrib, glGetAttribLocation,
                               glGetProgramInfoLog, glGetProgramiv,
                               glGetShaderInfoLog, glGetShaderiv,
                               glLinkProgram, glShaderSource, glUseProgram)

T = TypeVar('T',
    ctypes.c_float, FVector2, FVector3, FVector4,
    ctypes.c_double, DVector2, DVector3, DVector4,
    ctypes.c_int32, I32Vector2, I32Vector3, I32Vector4,
    ctypes.c_uint32, U32Vector2, U32Vector3, U32Vector4,
    ctypes.c_bool,
    FMatrix2x2, FMatrix2x3, FMatrix2x4,
    FMatrix3x2, FMatrix3x3, FMatrix3x4,
    FMatrix4x2, FMatrix4x3, FMatrix4x4,
    DMatrix2x2, DMatrix2x3, DMatrix2x4,
    DMatrix3x2, DMatrix3x3, DMatrix3x4,
    DMatrix4x2, DMatrix4x3, DMatrix4x4,
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


class ShaderExecutionResult:

    def __init__(self):
        self._gl_context: Any = None
        self._gl: Any = None
        self._query_targets: set[Any] = set()

    def __del__(self):
        if self._gl is not None:
            get_gl_context().delete_query(self._gl)
            self._gl = None
        if self._gl_context is not None:
            self._gl_context = release_gl_context(self._gl_context)

    def _begin_query(self, *, occluded: bool = False) -> None:
        if occluded:
            self._gl_context = require_gl_context()
            self._gl = glGenQueries(1)[0]
            if occluded:
                glBeginQuery(GL_ANY_SAMPLES_PASSED, self._gl)
                self._query_targets.add(GL_ANY_SAMPLES_PASSED)

    def _end_query(self) -> None:
        for query_target in self._query_targets:
            glEndQuery(query_target)

    @property
    def occluded(self) -> bool:
        if GL_ANY_SAMPLES_PASSED not in self._query_targets:
            raise RuntimeError('occlusion information not queried')
        occluded = GLint()
        glGetQueryObjectuiv(self._gl, GL_QUERY_RESULT, occluded)
        return occluded.value == 0


class Shader:

    def __init__(
        self, *,
        vertex: Optional[bytes] = None,
        geometry: Optional[bytes] = None,
        fragment: Optional[bytes] = None,
        ignored_attributes: set[str] | None = None,
        ignored_uniforms: set[str] | None = None,
    ):
        self._gl_context = require_gl_context()

        if vertex is None and geometry is None and fragment is None:
            raise TypeError('vertex, geometry and fragment must be provided')
        if vertex is not None and not isinstance(vertex, bytes):
            raise TypeError('vertex must be bytes')
        if geometry is not None and not isinstance(geometry, bytes):
            raise TypeError('geometry must be bytes')
        if fragment is not None and not isinstance(fragment, bytes):
            raise TypeError('fragment must be bytes')

        if geometry is not None and vertex is None:
            raise TypeError('geometry shader requires vertex shader')

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
            if geometry is not None:
                add_stage('geometry', geometry, GL_GEOMETRY_SHADER)
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
                name.decode('utf8').removesuffix('[0]'),
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
                name.decode('utf8').removesuffix('[0]'),
                GL_TYPE_TO_PY[type.value],
                size.value,
                location
            ))
        self._uniforms = tuple(uniforms)

        self._inputs: dict[str, Union[ShaderAttribute, ShaderUniform]] = {
            **{attribute.name: attribute for attribute in attributes},
            **{uniform.name: uniform for uniform in uniforms},
        }

        self._ignored_attributes = (
            set(ignored_attributes)
            if ignored_attributes else set()
        )
        self._ignored_uniforms = (
            set(ignored_uniforms)
            if ignored_uniforms else set()
        )

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
            ctypes.c_float, FArray,
            FVector2, FVector2Array,
            FVector3, FVector3Array,
            FVector4, FVector4Array,
            ctypes.c_double, DArray,
            DVector2, DVector2Array,
            DVector3, DVector3Array,
            DVector4, DVector4Array,
            ctypes.c_int32, I32Array,
            I32Vector2, I32Vector2Array,
            I32Vector3, I32Vector3Array,
            I32Vector4, I32Vector4Array,
            ctypes.c_uint32, U32Array,
            U32Vector2, U32Vector2Array,
            U32Vector3, U32Vector3Array,
            U32Vector4, U32Vector4Array,
            ctypes.c_bool,
            FMatrix2x2, FMatrix2x2Array,
            FMatrix2x3, FMatrix2x3Array,
            FMatrix2x4, FMatrix2x4Array,
            FMatrix3x2, FMatrix3x2Array,
            FMatrix3x3, FMatrix3x3Array,
            FMatrix3x4, FMatrix3x4Array,
            FMatrix4x2, FMatrix4x2Array,
            FMatrix4x3, FMatrix4x3Array,
            FMatrix4x4, FMatrix4x4Array,
            DMatrix2x2, DMatrix2x2Array,
            DMatrix2x3, DMatrix2x3Array,
            DMatrix2x4, DMatrix2x4Array,
            DMatrix3x2, DMatrix3x2Array,
            DMatrix3x3, DMatrix3x3Array,
            DMatrix3x4, DMatrix3x4Array,
            DMatrix4x2, DMatrix4x2Array,
            DMatrix4x3, DMatrix4x3Array,
            DMatrix4x4, DMatrix4x4Array,
            Texture, Sequence[Texture],
        ],
    ) -> None:
        assert uniform in self._uniforms
        input_value: Any = None
        cache_key: Any = value
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
                value = I32Array(*texture_values)
                input_value = value.pointer
            else:
                if not isinstance(value, Texture):
                    raise ValueError(
                        f'expected {Texture} for {uniform.name} '
                        f'(got {type(value)})'
                    )
                bind_texture(value, self._next_texture_index)
                value = ctypes.c_int32(self._next_texture_index)
                self._next_texture_index += 1
                input_value = value.value
        else:
            if uniform.size > 1:
                array_type = PY_TYPE_TO_ARRAY[uniform.type]
                if not isinstance(value, array_type):
                    raise ValueError(
                        f'expected {array_type} for {uniform.name} '
                        f'(got {type(value)})'
                    )
                if len(value) != uniform.size:
                    raise ValueError(
                        f'expected array of length {uniform.size} '
                        f'for {uniform.name} '
                        f'(got array of length {len(value)})'
                    )
                input_value = value.pointer
            else:
                assert uniform.size == 1
                if not isinstance(value, uniform._set_type):
                    raise ValueError(
                        f'expected {uniform._set_type} for {uniform.name} '
                        f'(got {type(value)})'
                    )
                if uniform._set_type in POD_UNIFORM_TYPES:
                    input_value = value.value
                    cache_key = value.value
                else:
                    input_value = value.pointer
        uniform._set(uniform.location, uniform.size, input_value, cache_key)

    def close(self) -> None:
        global shader_in_use
        if shader_in_use and shader_in_use() is self:
            shader_in_use = None
        if hasattr(self, "_gl") and self._gl is not None:
            get_gl_context().delete_shader(self._gl)
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
    def ignored_attributes(self) -> set[str]:
        return set(self._ignored_attributes)

    @property
    def ignored_uniforms(self) -> set[str]:
        return set(self._ignored_uniforms)

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

    def __repr__(self) -> str:
        return f'<gamut.graphics.ShaderAttribute {self.name!r}>'

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
        self._set_type: Any = ctypes.c_int32 if type is Texture else type
        self._cache: Any = None

    def __repr__(self) -> str:
        return f'<gamut.graphics.ShaderUniform {self.name!r}>'

    def _set(
        self,
        location: int,
        size: int,
        gl_value: Any,
        cache_key: Any
    ) -> None:
        if self._cache == cache_key:
            return
        self._setter(location, size, gl_value)
        self._cache = cache_key

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
    uniforms: UniformMap,
    *,
    blend_source: BlendFactor = BlendFactor.ZERO,
    blend_destination: BlendFactor = BlendFactor.ONE,
    blend_source_alpha: Optional[BlendFactor] = None,
    blend_destination_alpha: Optional[BlendFactor] = None,
    blend_function: BlendFunction = BlendFunction.ADD,
    blend_color: Optional[FVector4 | DVector4] = None,
    color_write: tuple[bool, bool, bool, bool] = (True, True, True, True),
    depth_test: DepthTest = DepthTest.ALWAYS,
    depth_write: bool = False,
    face_cull: FaceCull = FaceCull.NONE,
    instances: int = 1,
    index_range: Optional[tuple[int, int]] = None,
    query_occluded: bool = False,
) -> ShaderExecutionResult:
    ...


@overload
def execute_shader(
    render_target: Union[TextureRenderTarget, WindowRenderTarget],
    shader: Shader,
    primitive_mode: PrimitiveMode,
    buffer_view_map: BufferViewMap,
    uniforms: UniformMap,
    *,
    blend_source: BlendFactor = BlendFactor.ZERO,
    blend_destination: BlendFactor = BlendFactor.ONE,
    blend_source_alpha: Optional[BlendFactor] = None,
    blend_destination_alpha: Optional[BlendFactor] = None,
    blend_function: BlendFunction = BlendFunction.ADD,
    blend_color: Optional[FVector4 | DVector4] = None,
    color_write: tuple[bool, bool, bool, bool] = (True, True, True, True),
    depth_test: DepthTest = DepthTest.ALWAYS,
    depth_write: bool = False,
    face_cull: FaceCull = FaceCull.NONE,
    instances: int = 1,
    index_buffer_view: Optional[IndexBuffer] = None,
    query_occluded: bool = False,
) -> ShaderExecutionResult:
    ...


def execute_shader(
    render_target: Union[TextureRenderTarget, WindowRenderTarget],
    shader: Shader,
    primitive_mode: PrimitiveMode,
    buffer_view_map: BufferViewMap,
    uniforms: UniformMap,
    *,
    blend_source: BlendFactor = BlendFactor.ONE,
    blend_destination: BlendFactor = BlendFactor.ZERO,
    blend_source_alpha: Optional[BlendFactor] = None,
    blend_destination_alpha: Optional[BlendFactor] = None,
    blend_function: BlendFunction = BlendFunction.ADD,
    blend_color: Optional[FVector4 | DVector4] = None,
    color_write: tuple[bool, bool, bool, bool] = (True, True, True, True),
    depth_test: DepthTest = DepthTest.ALWAYS,
    depth_write: bool = False,
    face_cull: FaceCull = FaceCull.NONE,
    instances: int = 1,
    index_range: Optional[tuple[int, int]] = None,
    index_buffer_view: Optional[Union[
        BufferView[ctypes.c_uint8],
        BufferView[ctypes.c_uint16],
        BufferView[ctypes.c_uint32],
    ]] = None,
    query_occluded: bool = False,
) -> ShaderExecutionResult:
    gl_context = get_gl_context()
    # XXX
    glPointSize(8)
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
            if uniform_name in shader.ignored_uniforms:
                continue
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
        gl_context.set_depth_mask(bool(depth_write))
        glDepthFunc(depth_test.value)

    if len(color_write) != 4:
        raise ValueError('color write must be a sequence of 4')
    gl_context.set_color_mask(*(bool(c) for c in color_write))

    if blend_source_alpha is None:
        blend_source_alpha = blend_source
    if blend_destination_alpha is None:
        blend_destination_alpha = blend_destination
    if blend_color is None:
        blend_color = FVector4(1)

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

    result = ShaderExecutionResult()
    try:
        result._begin_query(occluded=query_occluded)
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
            index_gl_type = use_buffer_view_as_element_indexes(
                index_buffer_view
            )
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
    finally:
        result._end_query()
    return result


POD_UNIFORM_TYPES: Final = {
    ctypes.c_float,
    ctypes.c_double,
    ctypes.c_int32,
    ctypes.c_uint32,
    ctypes.c_bool,
}


def wrap_uniform_matrix(f: Any) -> Any:
    def _(location: Any, count: Any, value: Any) -> None:
        f(location, count, GL_FALSE, value)
    return _


TYPE_TO_UNIFORM_SETTER: Final[dict[Any, Any]] = {
    ctypes.c_float: OpenGL.GL.glUniform1fv,
    FVector2: OpenGL.GL.glUniform2fv,
    FVector3: OpenGL.GL.glUniform3fv,
    FVector4: OpenGL.GL.glUniform4fv,

    ctypes.c_double: OpenGL.GL.glUniform1dv,
    DVector2: OpenGL.GL.glUniform2dv,
    DVector3: OpenGL.GL.glUniform3dv,
    DVector4: OpenGL.GL.glUniform4dv,

    ctypes.c_int32: OpenGL.GL.glUniform1iv,
    I32Vector2: OpenGL.GL.glUniform2iv,
    I32Vector3: OpenGL.GL.glUniform3iv,
    I32Vector4: OpenGL.GL.glUniform4iv,

    ctypes.c_uint32: OpenGL.GL.glUniform1uiv,
    U32Vector2: OpenGL.GL.glUniform2uiv,
    U32Vector3: OpenGL.GL.glUniform3uiv,
    U32Vector4: OpenGL.GL.glUniform4uiv,

    ctypes.c_bool: OpenGL.GL.glUniform1iv,

    FMatrix2x2: wrap_uniform_matrix(OpenGL.GL.glUniformMatrix2fv),
    FMatrix2x3: wrap_uniform_matrix(OpenGL.GL.glUniformMatrix2x3fv),
    FMatrix2x4: wrap_uniform_matrix(OpenGL.GL.glUniformMatrix2x4fv),
    FMatrix3x2: wrap_uniform_matrix(OpenGL.GL.glUniformMatrix3x2fv),
    FMatrix3x3: wrap_uniform_matrix(OpenGL.GL.glUniformMatrix3fv),
    FMatrix3x4: wrap_uniform_matrix(OpenGL.GL.glUniformMatrix3x4fv),
    FMatrix4x2: wrap_uniform_matrix(OpenGL.GL.glUniformMatrix4x2fv),
    FMatrix4x3: wrap_uniform_matrix(OpenGL.GL.glUniformMatrix4x3fv),
    FMatrix4x4: wrap_uniform_matrix(OpenGL.GL.glUniformMatrix4fv),

    DMatrix2x2: wrap_uniform_matrix(OpenGL.GL.glUniformMatrix2dv),
    DMatrix2x3: wrap_uniform_matrix(OpenGL.GL.glUniformMatrix2x3dv),
    DMatrix2x4: wrap_uniform_matrix(OpenGL.GL.glUniformMatrix2x4dv),
    DMatrix3x2: wrap_uniform_matrix(OpenGL.GL.glUniformMatrix3x2dv),
    DMatrix3x3: wrap_uniform_matrix(OpenGL.GL.glUniformMatrix3dv),
    DMatrix3x4: wrap_uniform_matrix(OpenGL.GL.glUniformMatrix3x4dv),
    DMatrix4x2: wrap_uniform_matrix(OpenGL.GL.glUniformMatrix4x2dv),
    DMatrix4x3: wrap_uniform_matrix(OpenGL.GL.glUniformMatrix4x3dv),
    DMatrix4x4: wrap_uniform_matrix(OpenGL.GL.glUniformMatrix4dv),

    Texture: OpenGL.GL.glUniform1iv,
}


PY_TYPE_TO_ARRAY: Final = {
    ctypes.c_float: FArray,
    FVector2: FVector2Array,
    FVector3: FVector3Array,
    FVector4: FVector4Array,

    ctypes.c_double: DArray,
    DVector2: DVector2Array,
    DVector3: DVector3Array,
    DVector4: DVector4Array,

    ctypes.c_int32: I32Array,
    I32Vector2: I32Vector2Array,
    I32Vector3: I32Vector3Array,
    I32Vector4: I32Vector4Array,

    ctypes.c_uint32: U32Array,
    U32Vector2: U32Vector2Array,
    U32Vector3: U32Vector3Array,
    U32Vector4: U32Vector4Array,

    ctypes.c_bool: BArray,

    FMatrix2x2: FMatrix2x2Array,
    FMatrix3x3: FMatrix3x3Array,
    FMatrix4x4: FMatrix4x4Array,
    FMatrix2x3: FMatrix2x3Array,
    FMatrix2x4: FMatrix2x4Array,
    FMatrix3x2: FMatrix3x2Array,
    FMatrix3x4: FMatrix3x4Array,
    FMatrix4x2: FMatrix4x2Array,
    FMatrix4x3: FMatrix4x3Array,

    DMatrix2x2: DMatrix2x2Array,
    DMatrix3x3: DMatrix3x3Array,
    DMatrix4x4: DMatrix4x4Array,
    DMatrix2x3: DMatrix2x3Array,
    DMatrix2x4: DMatrix2x4Array,
    DMatrix3x2: DMatrix3x2Array,
    DMatrix3x4: DMatrix3x4Array,
    DMatrix4x2: DMatrix4x2Array,
    DMatrix4x3: DMatrix4x3Array,
}


GL_TYPE_TO_PY: Final = {
    OpenGL.GL.GL_FLOAT: ctypes.c_float,
    OpenGL.GL.GL_FLOAT_VEC2: FVector2,
    OpenGL.GL.GL_FLOAT_VEC3: FVector3,
    OpenGL.GL.GL_FLOAT_VEC4: FVector4,

    OpenGL.GL.GL_DOUBLE: ctypes.c_double,
    OpenGL.GL.GL_DOUBLE_VEC2: DVector2,
    OpenGL.GL.GL_DOUBLE_VEC3: DVector3,
    OpenGL.GL.GL_DOUBLE_VEC4: DVector4,

    OpenGL.GL.GL_INT: ctypes.c_int32,
    OpenGL.GL.GL_INT_VEC2: I32Vector2,
    OpenGL.GL.GL_INT_VEC3: I32Vector3,
    OpenGL.GL.GL_INT_VEC4: I32Vector4,

    OpenGL.GL.GL_UNSIGNED_INT: ctypes.c_uint32,
    OpenGL.GL.GL_UNSIGNED_INT_VEC2: U32Vector2,
    OpenGL.GL.GL_UNSIGNED_INT_VEC3: U32Vector3,
    OpenGL.GL.GL_UNSIGNED_INT_VEC4: U32Vector4,

    OpenGL.GL.GL_BOOL: ctypes.c_bool,

    OpenGL.GL.GL_FLOAT_MAT2: FMatrix2x2,
    OpenGL.GL.GL_FLOAT_MAT3: FMatrix3x3,
    OpenGL.GL.GL_FLOAT_MAT4: FMatrix4x4,
    OpenGL.GL.GL_FLOAT_MAT2x3: FMatrix2x3,
    OpenGL.GL.GL_FLOAT_MAT2x4: FMatrix2x4,
    OpenGL.GL.GL_FLOAT_MAT3x2: FMatrix3x2,
    OpenGL.GL.GL_FLOAT_MAT3x4: FMatrix3x4,
    OpenGL.GL.GL_FLOAT_MAT4x2: FMatrix4x2,
    OpenGL.GL.GL_FLOAT_MAT4x3: FMatrix4x3,

    OpenGL.GL.GL_DOUBLE_MAT2: DMatrix2x2,
    OpenGL.GL.GL_DOUBLE_MAT3: DMatrix3x3,
    OpenGL.GL.GL_DOUBLE_MAT4: DMatrix4x4,
    OpenGL.GL.GL_DOUBLE_MAT2x3: DMatrix2x3,
    OpenGL.GL.GL_DOUBLE_MAT2x4: DMatrix2x4,
    OpenGL.GL.GL_DOUBLE_MAT3x2: DMatrix3x2,
    OpenGL.GL.GL_DOUBLE_MAT3x4: DMatrix3x4,
    OpenGL.GL.GL_DOUBLE_MAT4x2: DMatrix4x2,
    OpenGL.GL.GL_DOUBLE_MAT4x3: DMatrix4x3,

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


IndexBuffer = Union[
    BufferView[ctypes.c_uint8],
    BufferView[ctypes.c_uint16],
    BufferView[ctypes.c_uint32],
]

UniformMap = dict[str, Union[
    ctypes.c_float, 'FArray',
    FVector2, 'FVector2Array',
    FVector3, 'FVector3Array',
    FVector4, 'FVector4Array',
    ctypes.c_double, 'DArray',
    DVector2, 'DVector2Array',
    DVector3, 'DVector3Array',
    DVector4, 'DVector4Array',
    ctypes.c_int32, 'I32Array',
    I32Vector2, 'I32Vector2Array',
    I32Vector3, 'I32Vector3Array',
    I32Vector4, 'I32Vector4Array',
    ctypes.c_uint32, 'U32Array',
    U32Vector2, 'U32Vector2Array',
    U32Vector3, 'U32Vector3Array',
    U32Vector4, 'U32Vector4Array',
    ctypes.c_bool,
    FMatrix2x2, 'FMatrix2x2Array',
    FMatrix2x3, 'FMatrix2x3Array',
    FMatrix2x4, 'FMatrix2x4Array',
    FMatrix3x2, 'FMatrix3x2Array',
    FMatrix3x3, 'FMatrix3x3Array',
    FMatrix3x4, 'FMatrix3x4Array',
    FMatrix4x2, 'FMatrix4x2Array',
    FMatrix4x3, 'FMatrix4x3Array',
    FMatrix4x4, 'FMatrix4x4Array',
    DMatrix2x2, 'DMatrix2x2Array',
    DMatrix2x3, 'DMatrix2x3Array',
    DMatrix2x4, 'DMatrix2x4Array',
    DMatrix3x2, 'DMatrix3x2Array',
    DMatrix3x3, 'DMatrix3x3Array',
    DMatrix3x4, 'DMatrix3x4Array',
    DMatrix4x2, 'DMatrix4x2Array',
    DMatrix4x3, 'DMatrix4x3Array',
    DMatrix4x4, 'DMatrix4x4Array',
    Texture, Sequence[Texture]
]]
