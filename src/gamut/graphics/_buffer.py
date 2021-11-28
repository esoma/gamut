
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
from gamut._glcontext import (get_gl_context, release_gl_context,
                              require_gl_context)
from gamut._glmhelp import uvec2_exact
# python
from ctypes import POINTER as c_pointer
from ctypes import c_byte, c_void_p
from ctypes import cast as c_cast
from enum import Enum
from struct import unpack as c_unpack
from typing import (Any, Final, Generator, Generic, Optional, TYPE_CHECKING,
                    TypeVar, Union)
from weakref import ref, WeakKeyDictionary
# pyglm
import glm
from glm import sizeof as glm_sizeof
# pyglm-typing
from glm_typing import U32Vector2
# pyopengl
import OpenGL.GL
from OpenGL.GL import (GL_ARRAY_BUFFER, GL_COPY_READ_BUFFER, GL_DOUBLE,
                       GL_DYNAMIC_COPY, GL_DYNAMIC_DRAW, GL_DYNAMIC_READ,
                       GL_ELEMENT_ARRAY_BUFFER, GL_FALSE, GL_R8, GL_READ_ONLY,
                       GL_RED, GL_STATIC_COPY, GL_STATIC_DRAW, GL_STATIC_READ,
                       GL_STREAM_COPY, GL_STREAM_DRAW, GL_STREAM_READ,
                       GL_UNSIGNED_BYTE, glBindBuffer, glBindVertexArray,
                       glBufferData, glClearBufferSubData,
                       glEnableVertexAttribArray, glGenBuffers,
                       glGenVertexArrays, glMapBuffer, glUnmapBuffer,
                       glVertexAttribDivisor, glVertexAttribIPointer,
                       glVertexAttribLPointer, glVertexAttribPointer)

if TYPE_CHECKING:
    # gamut
    from ._shader import Shader


_bytes = bytes


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
        self._gl: Any = None
        self._gl_context = require_gl_context()
        # check data
        if data is not None:
            try:
                data = bytes(data)
            except TypeError:
                raise TypeError('data must be bytes')
        self._length = len(data) if data is not None else 0
        # check frequency/nature
        try:
            self._gl_access = FREQUENCY_NATURE_TO_GL_ACCESS[
                (frequency, nature)
            ]
        except KeyError:
            if not isinstance(frequency, BufferFrequency):
                raise TypeError(f'frequency must be {BufferFrequency}')
            assert not isinstance(nature, BufferNature)
            raise TypeError(f'nature must be {BufferNature}')
        self._frequency = frequency
        self._nature = nature
        # create the gl buffer
        self._gl = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self._gl)
        glBufferData(GL_ARRAY_BUFFER, data, self._gl_access)

    def __del__(self) -> None:
        if self._gl is not None:
            get_gl_context().delete_buffer(self._gl)
            self._gl = None
        self._gl_context = release_gl_context(self._gl_context)

    def __len__(self) -> int:
        return self._length

    @property
    def bytes(self) -> bytes:
        if self._length == 0:
            return b''
        glBindBuffer(GL_COPY_READ_BUFFER, self._gl)
        map = c_void_p(glMapBuffer(
            GL_COPY_READ_BUFFER,
            GL_READ_ONLY
        ))
        try:
            result = bytes(c_cast(
                map,
                c_pointer(c_byte * self._length),
            ).contents)
        finally:
            glUnmapBuffer(GL_COPY_READ_BUFFER)
        return result

    @bytes.setter
    def bytes(self, data: bytes) -> None:
        try:
            data = bytes(data)
        except TypeError:
            raise TypeError('data must be bytes')
        glBindBuffer(GL_ARRAY_BUFFER, self._gl)
        glBufferData(GL_ARRAY_BUFFER, data, self._gl_access)
        self._length = len(data) if data is not None else 0

    def replace(self, offset: int, data: _bytes) -> None:
        # check offset
        try:
            offset = int(offset)
        except (ValueError, TypeError):
            raise TypeError('offset must be int')
        if offset < 0:
            raise ValueError('offset must be 0 or more')
        # check data
        try:
            data = bytes(data)
        except TypeError:
            raise TypeError('data must be bytes')
        # ensure the requested write doesn't go beyond the end of the existing
        # buffer
        if offset + len(data) > self._length:
            raise ValueError(
                'requested offset and data would write beyond the end of the '
                'buffer'
            )
        # replace the data
        if len(data) == 0:
            return
        glBindBuffer(GL_ARRAY_BUFFER, self._gl)
        glClearBufferSubData(
            GL_ARRAY_BUFFER,
            GL_R8,
            offset,
            len(data),
            GL_RED,
            GL_UNSIGNED_BYTE,
            data
        )

    def clear(
        self,
        data: _bytes = b'\x00',
        *,
        range: Optional[U32Vector2] = None
    ) -> None:
        # check data
        try:
            data = bytes(data)
        except TypeError:
            raise TypeError('data must be bytes')
        if len(data) != 1:
            raise TypeError('data must be a single byte')
        # check range
        if range is not None:
            try:
                start, end = uvec2_exact(range)
            except TypeError:
                raise TypeError('range must be a uvec2')
            assert start >= 0
            assert end >= 0
            if start > self._length or end > self._length:
                raise ValueError(
                    'range must be between 0 and the length of the buffer'
                )
            if start >= end:
                raise ValueError('range end must come after start')
        else:
            start = 0
            end = self._length
        # clear the range part of the buffer
        glBindBuffer(GL_ARRAY_BUFFER, self._gl)
        glClearBufferSubData(
            GL_ARRAY_BUFFER,
            GL_R8,
            start,
            end - start,
            GL_RED,
            GL_UNSIGNED_BYTE,
            data
        )

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
        # check stride
        if stride is None:
            stride = glm_sizeof(data_type)
        else:
            try:
                stride = int(stride)
            except (ValueError, TypeError):
                raise TypeError('stride must be an int')
        if stride < 1:
            raise ValueError('stride must be greater than 0')
        self._stride = stride
        # check offset
        try:
            offset = int(offset)
        except (ValueError, TypeError):
            raise TypeError('offset must be an int')
        if offset < 0:
            raise ValueError('offset must be 0 or greater')
        self._offset = offset
        # check instancing divisor
        if instancing_divisor is not None:
            try:
                instancing_divisor = int(instancing_divisor)
            except (ValueError, TypeError):
                raise TypeError('instancing divisor must be an int')
            if instancing_divisor < 1:
                raise ValueError('instancing divisor must be greater than 0')
        self._instancing_divisor = instancing_divisor

    def __len__(self) -> int:
        return (len(self._buffer) - self._offset) // self._stride

    def __iter__(self) -> Generator[BVT, None, None]:
        if len(self._buffer) == 0:
            return
        buffer_bytes = self._buffer.bytes
        for i in range(len(self)):
            start_index = self._offset + (self._stride * i)
            end_index = start_index + glm_sizeof(self._data_type)
            chunk = buffer_bytes[start_index:end_index]
            try:
                struct_name = GLM_POD_TO_STRUCT_NAME[self._data_type]
                data = c_unpack(struct_name, chunk)
            except KeyError:
                data = self._data_type.from_bytes(chunk) # type: ignore
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
        try:
            self._mapping = dict(mapping)
        except TypeError:
            raise TypeError('mapping must be a dict')
        for key, value in self._mapping.items():
            if not isinstance(key, str):
                raise TypeError(f'invalid key {key!r}, expected str')
            if not isinstance(value, BufferView):
                raise TypeError(
                    f'invalid value for key {key!r}, '
                    f'expected gamut.graphics.BufferView'
                )
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
        except (TypeError, KeyError):
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
        try:
            attributes = shader.attributes
        except AttributeError:
            raise TypeError('shader must be a gamut.graphics.Shader')
        attribute_names = {a.name for a in shader.attributes}
        for name in mapping:
            if name not in attribute_names:
                raise ValueError(
                    f'shader does not accept an attribute called "{name}"'
                )
        for attribute in shader.attributes:
            try:
                buffer_view = mapping[attribute.name]
            except KeyError:
                raise ValueError(f'missing attribute: {attribute.name}')
            glBindBuffer(GL_ARRAY_BUFFER, buffer_view.buffer._gl)
            attr_gl_type = (
                BUFFER_VIEW_TYPE_TO_VERTEX_ATTRIB_POINTER[attribute.type]
            )[0]
            view_gl_type, count, locations = (
                BUFFER_VIEW_TYPE_TO_VERTEX_ATTRIB_POINTER[buffer_view.type]
            )
            for location_offset in range(locations):
                location = attribute.location + location_offset
                offset = (
                    buffer_view.offset +
                    ((buffer_view.stride // locations) * location_offset)
                )
                if (
                    attr_gl_type == GL_DOUBLE and
                    view_gl_type == GL_DOUBLE
                ):
                    glVertexAttribLPointer(
                        location,
                        count,
                        view_gl_type,
                        buffer_view.stride,
                        c_void_p(offset)
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
                        c_void_p(offset)
                    )
                else:
                    glVertexAttribPointer(
                        location,
                        count,
                        view_gl_type,
                        GL_FALSE,
                        buffer_view.stride,
                        c_void_p(offset)
                    )
                glEnableVertexAttribArray(location)
                if buffer_view.instancing_divisor is not None:
                    glVertexAttribDivisor(
                        location,
                        buffer_view.instancing_divisor
                    )


    def use(self) -> None:
        global gl_vertex_array_in_use
        if gl_vertex_array_in_use and gl_vertex_array_in_use() is self:
            return
        glBindVertexArray(self._gl)
        gl_vertex_array_in_use = ref(self)

    def __del__(self) -> None:
        global gl_vertex_array_in_use
        if self._gl:
            if gl_vertex_array_in_use and gl_vertex_array_in_use() is self:
                gl_vertex_array_in_use = None
            get_gl_context().delete_vertex_array(self._gl)
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
    try:
        get_gl_vertex_array = view_map._get_gl_vertex_array_for_shader
    except AttributeError:
        raise TypeError('view_map must be gamut.graphics.BufferViewMap')
    gl_vertex_array = get_gl_vertex_array(shader)
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
