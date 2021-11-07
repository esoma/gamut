
from __future__ import annotations

__all__ = ['Buffer', 'BufferFrequency', 'BufferNature', 'BufferView']

# gamut
from gamut._glcontext import get_gl_context, GlContext
# python
from ctypes import POINTER as c_pointer
from ctypes import c_byte, c_void_p
from ctypes import cast as c_cast
from enum import Enum
from struct import unpack as c_unpack
from typing import Any, Final, Generator, Generic, Optional, TypeVar
# numpy
from numpy import array as np_array
# pyglm
import glm
from glm import sizeof as glm_sizeof
# pyopengl
from OpenGL.GL import (GL_ARRAY_BUFFER, GL_COPY_READ_BUFFER, GL_DYNAMIC_COPY,
                       GL_DYNAMIC_DRAW, GL_DYNAMIC_READ, GL_READ_ONLY,
                       GL_STATIC_COPY, GL_STATIC_DRAW, GL_STATIC_READ,
                       GL_STREAM_COPY, GL_STREAM_DRAW, GL_STREAM_READ,
                       glBindBuffer, glBufferData, glDeleteBuffers,
                       glGenBuffers, glMapBuffer, glUnmapBuffer)


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
        self._gl_context: Optional[GlContext] = get_gl_context()

        self._gl = glGenBuffers(1)
        gl_access = FREQUENCY_NATURE_TO_GL_ACCESS[(frequency, nature)]
        glBindBuffer(GL_ARRAY_BUFFER, self._gl)
        glBufferData(GL_ARRAY_BUFFER, data, gl_access)

        self._map: Optional[c_void_p] = None

        self._length = len(data) if data is not None else 0
        self._frequency = frequency
        self._nature = nature

    def __del__(self) -> None:
        self.close()

    def __len__(self) -> int:
        self._ensure_open()
        return self._length

    def _ensure_open(self) -> None:
        if self._gl is None:
            raise RuntimeError('buffer is closed')

    def _ensure_mapped(self) -> None:
        assert self.is_open
        assert self._length > 0
        if self._map is not None:
            return
        glBindBuffer(GL_COPY_READ_BUFFER, self._gl)
        self._map = c_void_p(glMapBuffer(
            GL_COPY_READ_BUFFER,
            GL_READ_ONLY
        ))

    def close(self) -> None:
        if hasattr(self, '_map') and self._map is not None:
            assert self._gl_context
            if self._gl_context.is_open:
                glBindBuffer(GL_COPY_READ_BUFFER, self._gl)
                glUnmapBuffer(GL_COPY_READ_BUFFER)
            self._map = None
        if hasattr(self, '_gl') and self._gl is not None:
            assert self._gl_context
            if self._gl_context.is_open:
                glDeleteBuffers(1, np_array([self._gl]))
            self._gl = None
        self._gl_context = None

    @property
    def bytes(self) -> bytes:
        self._ensure_open()
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
        self._ensure_open()
        return self._frequency

    @property
    def nature(self) -> BufferNature:
        self._ensure_open()
        return self._nature

    @property
    def is_open(self) -> bool:
        return self._gl is not None


BVT = TypeVar('BVT',
    glm.float32, glm.double, glm.int32, glm.uint32,
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
        offset: int = 0
    ) -> None:
        buffer._ensure_open()

        self._buffer: Optional[Buffer] = buffer
        self._data_type: type[BVT] = data_type
        if stride is None:
            stride = glm_sizeof(data_type)
        if stride < 1:
            raise ValueError('stride must be greater than 0')
        self._stride = stride
        if offset < 0:
            raise ValueError('offset must be 0 or greater')
        self._offset = offset

    def __del__(self) -> None:
        self.close()

    def __len__(self) -> int:
        self._ensure_open(include_buffer=False)
        assert self._buffer is not None
        return (len(self._buffer) - self._offset) // self._stride

    def __iter__(self) -> Generator[BVT, None, None]:
        self._ensure_open()
        assert self._buffer is not None
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

    def _ensure_open(self, *, include_buffer: bool = True) -> None:
        if self._buffer is None:
            raise RuntimeError('buffer view is closed')
        assert self._buffer is not None
        if include_buffer and not self._buffer.is_open:
            raise RuntimeError('buffer is closed')

    def close(self) -> None:
        self._buffer = None

    @property
    def buffer(self) -> Buffer:
        self._ensure_open(include_buffer=False)
        assert self._buffer is not None
        return self._buffer

    @property
    def type(self) -> type[BVT]:
        self._ensure_open(include_buffer=False)
        return self._data_type

    @property
    def stride(self) -> int:
        self._ensure_open(include_buffer=False)
        return self._stride

    @property
    def offset(self) -> int:
        self._ensure_open(include_buffer=False)
        return self._offset

    @property
    def is_open(self) -> bool:
        return self._buffer is not None
