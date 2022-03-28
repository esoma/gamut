
from __future__ import annotations

__init__ = ['Gltf']

# gamut
import gamut.math
# python
import ctypes
import json
import struct
from typing import BinaryIO, Final
from weakref import ref
# numpy
from numpy import frombuffer as np_array_from_buffer
from numpy import ndarray as np_array
from numpy import uint8 as np_uint8
from numpy.lib.stride_tricks import as_strided as np_as_strided


class GltfError(ValueError):
        pass


class GltfAccessor:

    def __init__(
        self,
        buffer_view: GltfBufferView,
        data_type: Any,
        count: int,
        offset: int
    ):
        self._buffer_view = buffer_view
        self._data_type = data_type
        try:
            self._data_size = self._data_type.get_size()
        except AttributeError:
            self._data_size = ctypes.sizeof(self._data_type)
        self._count = count
        self._offset = offset
        self._array: Any = None

    def _get_array(self) -> None:
        assert self._array is None
        array_type = DATA_TYPE_TO_ARRAY_TYPE[self._data_type]
        data = self._buffer_view.get_data(self._data_size)
        self._array = array_type.from_buffer(data)

    @property
    def array(self) -> (
        gamut.math.I8Array | gamut.math.U8Array |
        gamut.math.I16Array | gamut.math.U16Array |
        gamut.math.I32Array | gamut.math.U32Array |
        gamut.math.FArray |
        gamut.math.I8Vector2Array | gamut.math.U8Vector2Array |
        gamut.math.I16Vector2Array | gamut.math.U16Vector2Array |
        gamut.math.I32Vector2Array | gamut.math.U32Vector2Array |
        gamut.math.FVector2Array |
        gamut.math.I8Vector3Array | gamut.math.U8Vector3Array |
        gamut.math.I16Vector3Array | gamut.math.U16Vector3Array |
        gamut.math.I32Vector3Array | gamut.math.U32Vector3Array |
        gamut.math.FVector3Array |
        gamut.math.I8Vector4Array | gamut.math.U8Vector4Array |
        gamut.math.I16Vector4Array | gamut.math.U16Vector4Array |
        gamut.math.I32Vector4Array | gamut.math.U32Vector4Array |
        gamut.math.FVector4Array |
        gamut.math.FMatrix2Array |
        gamut.math.FMatrix3Array |
        gamut.math.FMatrix4Array
    ):
        if self._array is None:
            self._get_array()
        assert self._array is not None
        return self._array

    @classmethod
    def _parse(cls, gltf: Gltf, data: dict) -> GltfAccessor:
        data_type = GLTF_DATA_TYPE_TO_DATA_TYPE[(
            data["componentType"],
            data["type"]
        )]
        count = int(data["count"])

        buffer_view_index = data.get("bufferView")
        if buffer_view_index is None:
            buffer_view = None
        else:
            buffer_view = gltf.buffer_views[buffer_view_index]

        offset = int(data.get("offset", 0))
        normalized = bool(data.get("normalized", False))
        if normalized:
            raise NotImplementedError('Normalized accessors not supported.')
        if "sparse" in data:
            raise NotImplementedError('Sparse accessors not supported.')

        return GltfAccessor(buffer_view, data_type, count, offset)



class GltfBuffer:

    def __init__(self, gltf: Gltf, uri: str | None, length: int, index: int):
        self._gltf = ref(gltf)
        self._uri = uri
        self._length = length
        self._index = index
        self._data: np_array | None = None

    def _get_data(self) -> None:
        print(self._uri, self._index)
        if self._uri is None and self._index == 0:
            gltf = self._gltf()
            if gltf is None:
                raise GltfError('Gltf object for the buffer has been deleted')
            self._data = gltf._bin[:self._length]
            return
        raise NotImplementedError('!')

    @property
    def data(self) -> np_array:
        if self._data is None:
            self._get_data()
        assert isinstance(self._data, np_array)
        return self._data

    @classmethod
    def _parse(cls, gltf: Gltf, data: dict, index: int) -> GltfBuffer:
        length = int(data["byteLength"])
        try:
            uri = str(data["uri"])
        except KeyError:
            uri = None
        return GltfBuffer(gltf, uri, length, index)


class GltfBufferView:

    def __init__(
        self,
        buffer: GltfBuffer,
        length: int,
        offset: int,
        stride: int | None
    ):
        self._buffer = buffer
        self._length = length
        self._offset = offset
        self._stride = stride
        self._end = self._offset + self._length

    def get_data(self, element_size: int) -> np_array:
        if self._stride is not None and element_size > self._stride:
            raise ValueError('element size cannot be larger than stride')
        return np_as_strided(
            self._buffer.data[self._offset:self._end],
            shape=(self._length // element_size, element_size),
            strides=(element_size if self._stride is None else self._stride, 1)
        )

    @classmethod
    def _parse(cls, gltf: Gltf, data: dict) -> GltfBuffer:
        buffer_index = data["buffer"]
        buffer = gltf.buffers[buffer_index]
        length = data["byteLength"]
        offset = int(data.get("byteOffset", 0))
        try:
            stride = int(data["stride"])
        except KeyError:
            stride = None
        return GltfBufferView(buffer, length, offset, stride)


class Gltf:

    Accessor = GltfAccessor
    Buffer = GltfBuffer
    BufferView = GltfBufferView
    Error = GltfError

    def __init__(self, file: BinaryIO):
        self._bin: np_array | None = None
        self.accessors: list[GltfAccessor] = []
        self.buffers: list[GltfBuffer] = []
        self.buffer_views: list[GltfBufferView] = []

        glb_args = self._parse_glb_header(file)
        if glb_args is None:
            pass
        else:
            self._load_glb(file, *glb_args)

    def _parse_glb_header(self, file: BinaryIO) -> tuple[int, int] | None:
        i = file.tell()
        header = file.read(12)
        if len(header) == 12:
            if header[:4] == b'glTF':
                return struct.unpack('<II', header[4:])
        file.seek(i)
        return None

    def _load_glb(self, file: BinaryIO, version: int, length: int) -> None:
        if version != 2:
            raise self.Error(
                f'only compatible with GLTF version 2, got {version}'
            )
        # eliminate the header length, which we've already read
        remaining_bytes = length - 12
        while remaining_bytes:
            chunk_header = file.read(8)
            if len(chunk_header) != 8:
                raise self.Error(f'unexpected eof in chunk header')
            remaining_bytes -= 8

            chunk_length = struct.unpack('<I', chunk_header[:4])[0]
            chunk_type = chunk_header[4:]

            i = file.tell()
            if chunk_type == b'JSON':
                self._load_glb_json_chunk(file, chunk_length)
            elif chunk_type == b'BIN\x00':
                self._load_glb_bin_chunk(file, chunk_length)
            else:
                raise self.Error(f'unexpected chunk type: {chunk_type}')
            assert file.tell() == i + chunk_length
            remaining_bytes -= chunk_length

    def _load_glb_json_chunk(self, file: BinaryIO, length: int) -> None:
        json_file = PartialFile(file, length)
        data = json.load(json_file)
        self._parse_json(data)

    def _load_glb_bin_chunk(self, file: BinaryIO, length: int) -> None:
        self._bin = np_array_from_buffer(file.read(length), dtype=np_uint8)

    def _parse_json(self, data: dict) -> None:
        self._parse_json_buffers(data)
        self._parse_json_buffer_views(data)
        self._parse_json_accessors(data)

    def _parse_json_buffers(self, data: dict) -> None:
        try:
            json_buffers = data["buffers"]
        except KeyError:
            return
        for i, json_buffer in enumerate(json_buffers):
            self.buffers.append(self.Buffer._parse(self, json_buffer, i))

    def _parse_json_buffer_views(self, data: dict) -> None:
        try:
            json_buffer_views = data["bufferViews"]
        except KeyError:
            return
        for json_buffer_view in json_buffer_views:
            self.buffer_views.append(self.BufferView._parse(
                self,
                json_buffer_view
            ))

    def _parse_json_accessors(self, data: dict) -> None:
        try:
            json_accessors = data["accessors"]
        except KeyError:
            return
        for json_accessor in json_accessors:
            self.accessors.append(self.Accessor._parse(
                self,
                json_accessor
            ))


class PartialFile:

    def __init__(self, file: BinaryIO, length: int) -> None:
        self._file = file
        self._remaining_length = length

    def read(self, n: int = 0) -> bytes:
        if self._remaining_length == 0:
            return b''

        if n == 0 or n > self._remaining_length:
            length = self._remaining_length
        else:
            length = n
        self._remaining_length -= length
        return self._file.read(length)


GLTF_DATA_TYPE_TO_DATA_TYPE: Final = {
    (5120, "SCALAR"): ctypes.c_int8,
    (5121, "SCALAR"): ctypes.c_uint8,
    (5122, "SCALAR"): ctypes.c_int16,
    (5123, "SCALAR"): ctypes.c_uint16,
    (5125, "SCALAR"): ctypes.c_uint32,
    (5126, "SCALAR"): ctypes.c_float,
    (5120, "VEC2"): gamut.math.I8Vector2,
    (5121, "VEC2"): gamut.math.U8Vector2,
    (5122, "VEC2"): gamut.math.I16Vector2,
    (5123, "VEC2"): gamut.math.U16Vector2,
    (5125, "VEC2"): gamut.math.U32Vector2,
    (5126, "VEC2"): gamut.math.FVector2,
    (5120, "VEC3"): gamut.math.I8Vector3,
    (5121, "VEC3"): gamut.math.U8Vector3,
    (5122, "VEC3"): gamut.math.I16Vector3,
    (5123, "VEC3"): gamut.math.U16Vector3,
    (5125, "VEC3"): gamut.math.U32Vector3,
    (5126, "VEC3"): gamut.math.FVector3,
    (5120, "VEC4"): gamut.math.I8Vector4,
    (5121, "VEC4"): gamut.math.U8Vector4,
    (5122, "VEC4"): gamut.math.I16Vector4,
    (5123, "VEC4"): gamut.math.U16Vector4,
    (5125, "VEC4"): gamut.math.U32Vector4,
    (5126, "VEC4"): gamut.math.FVector4,
    (5126, "MAT2"): gamut.math.FMatrix2,
    (5126, "MAT3"): gamut.math.FMatrix3,
    (5126, "MAT4"): gamut.math.FMatrix4
}


DATA_TYPE_TO_ARRAY_TYPE: Final = {
    ctypes.c_int8: gamut.math.I8Array,
    ctypes.c_uint8: gamut.math.U8Array,
    ctypes.c_int16: gamut.math.I16Array,
    ctypes.c_uint16: gamut.math.U16Array,
    ctypes.c_uint32: gamut.math.U32Array,
    ctypes.c_float: gamut.math.FArray,
    gamut.math.I8Vector2: gamut.math.I8Vector2Array,
    gamut.math.U8Vector2: gamut.math.U8Vector2Array,
    gamut.math.I16Vector2: gamut.math.I16Vector2Array,
    gamut.math.U16Vector2: gamut.math.U16Vector2Array,
    gamut.math.U32Vector2: gamut.math.U32Vector2Array,
    gamut.math.FVector2: gamut.math.FVector2Array,
    gamut.math.I8Vector3: gamut.math.I8Vector3Array,
    gamut.math.U8Vector3: gamut.math.U8Vector3Array,
    gamut.math.I16Vector3: gamut.math.I16Vector3Array,
    gamut.math.U16Vector3: gamut.math.U16Vector3Array,
    gamut.math.U32Vector3: gamut.math.U32Vector3Array,
    gamut.math.FVector3: gamut.math.FVector3Array,
    gamut.math.I8Vector4: gamut.math.I8Vector4Array,
    gamut.math.U8Vector4: gamut.math.U8Vector4Array,
    gamut.math.I16Vector4: gamut.math.I16Vector4Array,
    gamut.math.U16Vector4: gamut.math.U16Vector4Array,
    gamut.math.U32Vector4: gamut.math.U32Vector4Array,
    gamut.math.FVector4: gamut.math.FVector4Array,
    gamut.math.FMatrix2: gamut.math.FMatrix2Array,
    gamut.math.FMatrix3: gamut.math.FMatrix3Array,
    gamut.math.FMatrix4: gamut.math.FMatrix4Array,
}
