
from __future__ import annotations

__all__ = [
    'Buffer',
    'BufferFrequency',
    'BufferNature',
    'BufferView',
    'BufferViewMap',
    'use_buffer_view_map_with_shader',
    'use_buffer_view_as_element_indexes',
]

# gamut
from gamut._glcontext import release_gl_context, require_gl_context
# python
from ctypes import POINTER as c_pointer
from ctypes import c_byte, c_void_p
from ctypes import cast as c_cast
from enum import Enum
from struct import unpack as c_unpack
from typing import (Any, Final, Generator, Generic, Optional, TYPE_CHECKING,
                    TypeVar, Union)
from weakref import ref, WeakKeyDictionary
# numpy
from numpy import array as np_array
# pyglm
import glm
from glm import sizeof as glm_sizeof
# pyopengl
import OpenGL.GL
from OpenGL.GL import (GL_ARRAY_BUFFER, GL_COPY_READ_BUFFER, GL_DOUBLE,
                       GL_DYNAMIC_COPY, GL_DYNAMIC_DRAW, GL_DYNAMIC_READ,
                       GL_ELEMENT_ARRAY_BUFFER, GL_FALSE, GL_READ_ONLY,
                       GL_STATIC_COPY, GL_STATIC_DRAW, GL_STATIC_READ,
                       GL_STREAM_COPY, GL_STREAM_DRAW, GL_STREAM_READ,
                       glBindBuffer, glBindVertexArray, glBufferData,
                       glDeleteBuffers, glDeleteVertexArrays,
                       glEnableVertexAttribArray, glGenBuffers,
                       glGenVertexArrays, glMapBuffer, glUnmapBuffer,
                       glVertexAttribDivisor, glVertexAttribIPointer,
                       glVertexAttribLPointer, glVertexAttribPointer)

if TYPE_CHECKING:
    # gamut
    from ._shader import Shader


class BufferFrequency(Enum):
    STREAM = 0
    STATIC = 1
    DYNAMIC = 2


class BufferNature(Enum):
    DRAW = 0
    READ = 1
    COPY = 2


FREQUENCY_NATURE_TO_GL_ACCESS: Final = {
    (BufferFrequency.STREAM, BufferNature.DRAW): GL_STREAM_DRAW,
    (BufferFrequency.STREAM, BufferNature.READ): GL_STREAM_READ,
    (BufferFrequency.STREAM, BufferNature.COPY): GL_STREAM_COPY,
    (BufferFrequency.STATIC, BufferNature.DRAW): GL_STATIC_DRAW,
    (BufferFrequency.STATIC, BufferNature.READ): GL_STATIC_READ,
    (BufferFrequency.STATIC, BufferNature.COPY): GL_STATIC_COPY,
    (BufferFrequency.DYNAMIC, BufferNature.DRAW): GL_DYNAMIC_DRAW,
    (BufferFrequency.DYNAMIC, BufferNature.READ): GL_DYNAMIC_READ,
    (BufferFrequency.DYNAMIC, BufferNature.COPY): GL_DYNAMIC_COPY,
}


GLM_POD_TO_STRUCT_NAME: Final[dict[Any, str]] = {
    glm.float32: 'f',
    glm.double: 'd',
    glm.int8: 'b',
    glm.uint8: 'B',
    glm.int16: 'h',
    glm.uint16: 'H',
    glm.int32: 'i',
    glm.uint32: 'I',
}


class Buffer:

    def __init__(
        self,
        data: Optional[bytes] = None,
        *,
        frequency: BufferFrequency = BufferFrequency.STATIC,
        nature: BufferNature = BufferNature.DRAW,
    ):
        self._gl_context = require_gl_context()

        self._gl = glGenBuffers(1)
        gl_access = FREQUENCY_NATURE_TO_GL_ACCESS[(frequency, nature)]
        glBindBuffer(GL_ARRAY_BUFFER, self._gl)
        glBufferData(GL_ARRAY_BUFFER, data, gl_access)

        self._map: Optional[c_void_p] = None

        self._length = len(data) if data is not None else 0
        self._frequency = frequency
        self._nature = nature

    def __del__(self) -> None:
        if hasattr(self, '_map') and self._map is not None:
            glBindBuffer(GL_COPY_READ_BUFFER, self._gl)
            glUnmapBuffer(GL_COPY_READ_BUFFER)
            self._map = None
        if hasattr(self, '_gl') and self._gl is not None:
            glDeleteBuffers(1, np_array([self._gl]))
            self._gl = None
        self._gl_context = release_gl_context(self._gl_context)

    def __len__(self) -> int:
        return self._length

    def _ensure_mapped(self) -> None:
        assert self._length > 0
        if self._map is not None:
            return
        glBindBuffer(GL_COPY_READ_BUFFER, self._gl)
        self._map = c_void_p(glMapBuffer(
            GL_COPY_READ_BUFFER,
            GL_READ_ONLY
        ))

    @property
    def bytes(self) -> bytes:
        if self._length == 0:
            return b''
        self._ensure_mapped()
        assert self._map is not None
        return bytes(c_cast(
            self._map,
            c_pointer(c_byte * self._length),
        ).contents)

    @property
    def frequency(self) -> BufferFrequency:
        return self._frequency

    @property
    def nature(self) -> BufferNature:
        return self._nature


BVT = TypeVar('BVT',
    glm.float32, glm.double,
    glm.int8, glm.uint8,
    glm.int16, glm.uint16,
    glm.int32, glm.uint32,
    glm.vec2, glm.dvec2, glm.ivec2, glm.uvec2,
    glm.vec3, glm.dvec3, glm.ivec3, glm.uvec3,
    glm.vec4, glm.dvec4, glm.ivec4, glm.uvec4,
    glm.mat2x2, glm.dmat2x2, glm.imat2x2, glm.umat2x2,
    glm.mat2x3, glm.dmat2x3, glm.imat2x3, glm.umat2x3,
    glm.mat2x4, glm.dmat2x4, glm.imat2x4, glm.umat2x4,
    glm.mat3x2, glm.dmat3x2, glm.imat3x2, glm.umat3x2,
    glm.mat3x3, glm.dmat3x3, glm.imat3x3, glm.umat3x3,
    glm.mat3x4, glm.dmat3x4, glm.imat3x4, glm.umat3x4,
    glm.mat4x2, glm.dmat4x2, glm.imat4x2, glm.umat4x2,
    glm.mat4x3, glm.dmat4x3, glm.imat4x3, glm.umat4x3,
    glm.mat4x4, glm.dmat4x4, glm.imat4x4, glm.umat4x4,
)


class BufferView(Generic[BVT]):

    def __init__(
        self,
        buffer: Buffer,
        data_type: type[BVT],
        *,
        stride: Optional[int] = None,
        offset: int = 0,
        instancing_divisor: Optional[int] = None,
    ) -> None:
        self._buffer = buffer
        self._data_type: type[BVT] = data_type
        if stride is None:
            stride = glm_sizeof(data_type)
        if stride < 1:
            raise ValueError('stride must be greater than 0')
        self._stride = stride
        if offset < 0:
            raise ValueError('offset must be 0 or greater')
        self._offset = offset
        if instancing_divisor is not None and instancing_divisor < 1:
            raise ValueError('instancing divisor must be greater than 0')
        self._instancing_divisor = instancing_divisor

    def __len__(self) -> int:
        return (len(self._buffer) - self._offset) // self._stride

    def __iter__(self) -> Generator[BVT, None, None]:
        if len(self._buffer) == 0:
            return
        self._buffer._ensure_mapped()
        assert self._buffer._map is not None

        for i in range(len(self)):
            assert self._buffer._map.value is not None
            data_bytes = bytes(c_cast(
                self._buffer._map.value + self._offset + (self._stride * i),
                c_pointer(c_byte * glm_sizeof(self._data_type)),
            ).contents)
            try:
                struct_name = GLM_POD_TO_STRUCT_NAME[self._data_type]
                data = c_unpack(struct_name, data_bytes)
            except KeyError:
                data = self._data_type.from_bytes(data_bytes) # type: ignore
            yield data # type: ignore

    @property
    def buffer(self) -> Buffer:
        return self._buffer

    @property
    def type(self) -> type[BVT]:
        return self._data_type

    @property
    def stride(self) -> int:
        return self._stride

    @property
    def offset(self) -> int:
        return self._offset

    @property
    def instancing_divisor(self) -> Optional[int]:
        return self._instancing_divisor


class BufferViewMap:

    def __init__(self, mapping: dict[str, BufferView], /) -> None:
        self._mapping = mapping.copy()
        self._shader_mapping: WeakKeyDictionary[Shader, GlVertexArray] = (
            WeakKeyDictionary()
        )

    def __len__(self) -> int:
        return len(self._mapping)

    def __getitem__(self, key: str) -> BufferView:
        return self._mapping[key]

    def _get_gl_vertex_array_for_shader(self, shader: Shader) -> GlVertexArray:
        try:
            return self._shader_mapping[shader]
        except KeyError:
            pass
        gl_vertex_array = self._shader_mapping[shader] = GlVertexArray(
            shader,
            self._mapping
        )
        return gl_vertex_array


gl_vertex_array_in_use: Optional[ref[GlVertexArray]] = None


GL_INT_TYPES: Final = set([
    OpenGL.GL.GL_BYTE, OpenGL.GL.GL_UNSIGNED_BYTE,
    OpenGL.GL.GL_SHORT, OpenGL.GL.GL_UNSIGNED_SHORT,
    OpenGL.GL.GL_INT, OpenGL.GL.GL_UNSIGNED_INT,
])


class GlVertexArray:

    def __init__(self, shader: Shader, mapping: dict[str, BufferView]) -> None:
        self._gl_context = require_gl_context()
        self._gl = glGenVertexArrays(1)
        self.use()
        for attribute in shader.attributes:
            buffer_view: Optional[BufferView] = None
            try:
                buffer_view = mapping[attribute.name]
            except KeyError:
                locations = 1
            else:
                glBindBuffer(GL_ARRAY_BUFFER, buffer_view.buffer._gl)
                attr_gl_type = (
                    BUFFER_VIEW_TYPE_TO_VERTEX_ATTRIB_POINTER[attribute.type]
                )[0]
                view_gl_type, count, locations = (
                    BUFFER_VIEW_TYPE_TO_VERTEX_ATTRIB_POINTER[buffer_view.type]
                )
            for location_offset in range(locations):
                location = attribute.location + location_offset
                if buffer_view is not None:
                    if (
                        attr_gl_type == GL_DOUBLE and
                        view_gl_type == GL_DOUBLE
                    ):
                        glVertexAttribLPointer(
                            location,
                            count,
                            view_gl_type,
                            buffer_view.stride,
                            c_void_p(buffer_view.offset)
                        )
                    elif (
                        attr_gl_type in GL_INT_TYPES and
                        view_gl_type in GL_INT_TYPES
                    ):
                        glVertexAttribIPointer(
                            location,
                            count,
                            view_gl_type,
                            buffer_view.stride,
                            c_void_p(buffer_view.offset)
                        )
                    else:
                        glVertexAttribPointer(
                            location,
                            count,
                            view_gl_type,
                            GL_FALSE,
                            buffer_view.stride,
                            c_void_p(buffer_view.offset)
                        )
                    glEnableVertexAttribArray(location)
                    if buffer_view.instancing_divisor is not None:
                        glVertexAttribDivisor(
                            location,
                            buffer_view.instancing_divisor
                        )
                else:
                    raise ValueError(f'missing attribute: {attribute.name}')

    def use(self) -> None:
        global gl_vertex_array_in_use
        if gl_vertex_array_in_use and gl_vertex_array_in_use() is self:
            return
        glBindVertexArray(self._gl)
        gl_vertex_array_in_use = ref(self)

    def __del__(self) -> None:
        global gl_vertex_array_in_use
        if gl_vertex_array_in_use and gl_vertex_array_in_use() is self:
            glBindVertexArray(0)
            gl_vertex_array_in_use = None
        if self._gl:
            glDeleteVertexArrays(1, np_array([self._gl]))
            self._gl = None
        self._gl_context = release_gl_context(self._gl_context)


BUFFER_VIEW_TYPE_TO_VERTEX_ATTRIB_POINTER: Final = {
    glm.float32: (OpenGL.GL.GL_FLOAT, 1, 1),
    glm.double: (OpenGL.GL.GL_DOUBLE, 1, 1),
    glm.int8: (OpenGL.GL.GL_BYTE, 1, 1),
    glm.uint8: (OpenGL.GL.GL_UNSIGNED_BYTE, 1, 1),
    glm.int16: (OpenGL.GL.GL_SHORT, 1, 1),
    glm.uint16: (OpenGL.GL.GL_UNSIGNED_SHORT, 1, 1),
    glm.int32: (OpenGL.GL.GL_INT, 1, 1),
    glm.uint32: (OpenGL.GL.GL_UNSIGNED_INT, 1, 1),
    glm.vec2: (OpenGL.GL.GL_FLOAT, 2, 1),
    glm.dvec2: (OpenGL.GL.GL_DOUBLE, 2, 1),
    glm.ivec2: (OpenGL.GL.GL_INT, 2, 1),
    glm.uvec2: (OpenGL.GL.GL_UNSIGNED_INT, 2, 1),
    glm.vec3: (OpenGL.GL.GL_FLOAT, 3, 1),
    glm.dvec3: (OpenGL.GL.GL_DOUBLE, 3, 1),
    glm.ivec3: (OpenGL.GL.GL_INT, 3, 1),
    glm.uvec3: (OpenGL.GL.GL_UNSIGNED_INT, 3, 1),
    glm.vec4: (OpenGL.GL.GL_FLOAT, 4, 1),
    glm.dvec4: (OpenGL.GL.GL_DOUBLE, 4, 1),
    glm.ivec4: (OpenGL.GL.GL_INT, 4, 1),
    glm.uvec4: (OpenGL.GL.GL_UNSIGNED_INT, 4, 1),
    glm.mat2x2: (OpenGL.GL.GL_FLOAT, 2, 2),
    glm.dmat2x2: (OpenGL.GL.GL_DOUBLE, 2, 2),
    glm.imat2x2: (OpenGL.GL.GL_INT, 2, 2),
    glm.umat2x2: (OpenGL.GL.GL_UNSIGNED_INT, 2, 2),
    glm.mat2x3: (OpenGL.GL.GL_FLOAT, 2, 3),
    glm.dmat2x3: (OpenGL.GL.GL_DOUBLE, 2, 3),
    glm.imat2x3: (OpenGL.GL.GL_INT, 2, 3),
    glm.umat2x3: (OpenGL.GL.GL_UNSIGNED_INT, 2, 3),
    glm.mat2x4: (OpenGL.GL.GL_FLOAT, 2, 4),
    glm.dmat2x4: (OpenGL.GL.GL_DOUBLE, 2, 4),
    glm.imat2x4: (OpenGL.GL.GL_INT, 2, 4),
    glm.umat2x4: (OpenGL.GL.GL_UNSIGNED_INT, 2, 4),
    glm.mat3x2: (OpenGL.GL.GL_FLOAT, 3, 2),
    glm.dmat3x2: (OpenGL.GL.GL_DOUBLE, 3, 2),
    glm.imat3x2: (OpenGL.GL.GL_INT, 3, 2),
    glm.umat3x2: (OpenGL.GL.GL_UNSIGNED_INT, 3, 2),
    glm.mat3x3: (OpenGL.GL.GL_FLOAT, 3, 3),
    glm.dmat3x3: (OpenGL.GL.GL_DOUBLE, 3, 3),
    glm.imat3x3: (OpenGL.GL.GL_INT, 3, 3),
    glm.umat3x3: (OpenGL.GL.GL_UNSIGNED_INT, 3, 3),
    glm.mat3x4: (OpenGL.GL.GL_FLOAT, 3, 4),
    glm.dmat3x4: (OpenGL.GL.GL_DOUBLE, 3, 4),
    glm.imat3x4: (OpenGL.GL.GL_INT, 3, 4),
    glm.umat3x4: (OpenGL.GL.GL_UNSIGNED_INT, 3, 4),
    glm.mat4x2: (OpenGL.GL.GL_FLOAT, 4, 2),
    glm.dmat4x2: (OpenGL.GL.GL_DOUBLE, 4, 2),
    glm.imat4x2: (OpenGL.GL.GL_INT, 4, 2),
    glm.umat4x2: (OpenGL.GL.GL_UNSIGNED_INT, 4, 2),
    glm.mat4x3: (OpenGL.GL.GL_FLOAT, 4, 3),
    glm.dmat4x3: (OpenGL.GL.GL_DOUBLE, 4, 3),
    glm.imat4x3: (OpenGL.GL.GL_INT, 4, 3),
    glm.umat4x3: (OpenGL.GL.GL_UNSIGNED_INT, 4, 3),
    glm.mat4x4: (OpenGL.GL.GL_FLOAT, 4, 4),
    glm.dmat4x4: (OpenGL.GL.GL_DOUBLE, 4, 4),
    glm.imat4x4: (OpenGL.GL.GL_INT, 4, 4),
    glm.umat4x4: (OpenGL.GL.GL_UNSIGNED_INT, 4, 4),
}


def use_buffer_view_map_with_shader(
    view_map: BufferViewMap,
    shader: Shader
) -> None:
    gl_vertex_array = view_map._get_gl_vertex_array_for_shader(shader)
    gl_vertex_array.use()


INDEX_TYPES: Final = {glm.uint8, glm.uint16, glm.uint32}


def use_buffer_view_as_element_indexes(
    view: Union[
        BufferView[glm.uint8],
        BufferView[glm.uint16],
        BufferView[glm.uint32]
    ]
) -> Any:
    if view.type not in INDEX_TYPES:
        raise ValueError(
            f'view buffer with type {view.type} cannot be used for indexing'
        )
    if view.stride != glm_sizeof(view.type):
        raise ValueError(
            'view buffer with a stride different from its type cannot be used '
            'for indexing'
        )
    if view.offset != 0:
        raise ValueError(
            'view buffer with an offset other than 0 cannot be used for '
            'indexing'
        )
    if view.instancing_divisor is not None:
        raise ValueError(
            'view buffer with instancing_divisor cannot be used for indexing'
        )
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, view.buffer._gl)
    return BUFFER_VIEW_TYPE_TO_VERTEX_ATTRIB_POINTER[view.type][0]
