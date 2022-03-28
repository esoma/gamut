
from __future__ import annotations

__init__ = ['Gltf']

# gamut
from gamut.graphics import Image, MipmapSelection, TextureFilter, TextureWrap
import gamut.math
from gamut.math import FMatrix4, FVector2, UVector2
# python
import ctypes
from io import BytesIO
import json
from pathlib import Path
import struct
import sys
from typing import BinaryIO, Callable, Final
from urllib.request import urlopen
# numpy
from numpy import frombuffer as np_array_from_buffer
from numpy import uint8 as np_uint8
from numpy.lib.stride_tricks import as_strided as np_as_strided

GltfFilePathCallback = Callable[[Path, int | None], memoryview]


def file_path_callback_disallowed(
    path: Path,
    length: int | None
) -> memoryview:
    raise RuntimeError('no external file loading allowed')


class GltfError(RuntimeError):
        pass


class GltfAccessor:

    def __init__(
        self,
        buffer_view: GltfBufferView | None,
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

        if self._buffer_view is None:
            py_data_type = DATA_TYPE_TO_PY_DATA_TYPE.get(
                self._data_type,
                self._data_type
            )
            self._array = array_type(*(
                py_data_type(0) for _ in range(self._count)
            ))
            return

        data = self._buffer_view.get_data(self._data_size, offset=self._offset)
        if len(data) < self._count:
            raise GltfError('buffer overflow')
        self._array = array_type.from_buffer(data[:self._count])
        assert len(self._array) == self._count

    @property
    def data(self) -> (
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

        offset = int(data.get("byteOffset", 0))
        normalized = bool(data.get("normalized", False))
        if normalized:
            raise NotImplementedError('normalized accessors not supported')
        if data.get("sparse") is not None:
            raise NotImplementedError('sparse accessors not supported')

        return GltfAccessor(buffer_view, data_type, count, offset)


class GltfBuffer:

    def __init__(
        self,
        file_path_callback: GltfFilePathCallback,
        uri: str | None,
        length: int,
        index: int
    ):
        self._file_path_callback = file_path_callback
        self._uri = uri
        self._length = length
        self._index = index
        self._data: memoryview | None = None

    def _get_glb_bin_data(self, bin: memoryview | None) -> None:
        assert self._data is None
        if self._uri is not None or self._index != 0:
            return
        if bin is None:
            raise GltfError('buffer expects embedded binary data')
        self._data = memoryview(bin[:self._length])
        if len(self._data) < self._length:
            raise GltfError('buffer overflow')
        assert len(self._data) == self._length

    def _get_data(self) -> None:
        assert self._data is None
        # if this was the first glb buffer it would have already been loaded
        if self._uri is None:
            raise GltfError('buffer has no URI')

        if self._uri.startswith('data:'):
            with urlopen(self._uri) as response:
                self._data = memoryview(response.read(self._length))
                if len(self._data) < self._length:
                    raise GltfError('buffer overflow')
                assert len(self._data) == self._length
            return

        self._data = self._file_path_callback(Path(self._uri), self._length)
        if not isinstance(self._data, memoryview):
            raise GltfError('file path callback did not return memoryview')
        if len(self._data) != self._length:
            raise GltfError(
                'file path callback returned data with a different length '
                'than expected'
            )

    @property
    def data(self) -> memoryview:
        if self._data is None:
            self._get_data()
        assert isinstance(self._data, memoryview)
        return self._data

    @classmethod
    def _parse(
        cls,
        file_path_callback: GltfFilePathCallback,
        data: dict,
        index: int
    ) -> GltfBuffer:
        length = int(data["byteLength"])
        try:
            uri = str(data["uri"])
        except KeyError:
            uri = None
        return GltfBuffer(file_path_callback, uri, length, index)


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

    def get_data(self, element_size: int, *, offset: int = 0) -> memoryview:
        if element_size <= 0:
            raise ValueError('element size must be more than 0')
        if offset < 0:
            raise ValueError('offset must be 0 or more')
        if self._stride is not None and element_size > self._stride:
            raise ValueError('element size cannot be larger than stride')
        stride = element_size if self._stride is None else self._stride
        return memoryview(np_as_strided(
            self._buffer.data[self._offset + offset:self._end],
            shape=((self._length - offset) // stride, element_size),
            strides=(stride, 1)
        ))

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


GltfCameraCreateProjection = Callable[[UVector2], FMatrix4]


class GltfCamera:

    def __init__(self, create_projection: GltfCameraCreateProjection):
        self._create_projection = create_projection

    def get_projection(self, viewport_size: UVector2) -> FMatrix4:
        return self._create_projection(viewport_size)

    @classmethod
    def _parse(cls, data: dict) -> GltfCamera:
        type = data["type"]
        if type == 'orthographic':
            return cls._parse_orthographic(data)
        elif type == 'perspective':
            return cls._parse_perspective(data)

    @classmethod
    def _parse_orthographic(cls, data: dict) -> GltfCamera:
        d = data["orthographic"]
        xmag = float(d["xmag"])
        ymag = float(d["ymag"])
        zfar = float(d["zfar"])
        znear = float(d["znear"])

        def _(viewport_size: UVector2) -> FMatrix4:
            size = FVector2(*viewport_size)
            return FMatrix4.orthographic(
                size.x * xmag * -.5, size.x * xmag * .5,
                size.y * ymag * -.5, size.y * ymag * .5,
                znear, zfar
            )
        return GltfCamera(_)

    @classmethod
    def _parse_perspective(cls, data: dict) -> GltfCamera:
        d = data["perspective"]
        try:
            aspect = float(d["aspectRatio"])
        except KeyError:
            aspect = None
        fov = float(d["yfov"])
        zfar = float(d.get("zfar", FVector2.get_limits()[1]))
        znear = float(d["znear"])

        def _(viewport_size: UVector2) -> FMatrix4:
            l_aspect = aspect
            if l_aspect is None:
                l_aspect = viewport_size.x / viewport_size.y
            return FMatrix4.perspective(fov, l_aspect, znear, zfar)
        return GltfCamera(_)


class GltfImage:

    def __init__(
        self,
        file_path_callback: GltfFilePathCallback,
        uri: str | None,
        buffer_view: GltfBufferView | None
    ):
        self._file_path_callback = file_path_callback
        self._uri = uri
        self._buffer_view = buffer_view
        self._data: Image | None = None

    def _get_data(self) -> None:
        assert self._data is None
        if self._uri is not None:
            assert self._buffer_view is None
            if self._uri.startswith('data:'):
                with urlopen(self._uri) as response:
                    image_data = response.read()
            else:
                image_data = self._file_path_callback(Path(self._uri), None)
        else:
            image_data = self._buffer_view.get_data(1)
        self._data = Image(BytesIO(image_data))

    @property
    def data(self) -> Image:
        if self._data is None:
            self._get_data()
            assert self._data is not None
        return self._data

    @classmethod
    def _parse(cls, gltf: Gltf, data: dict) -> GltfImage:
        uri = data.get("uri")
        buffer_view_index = data.get("bufferView")
        buffer_view = None

        if uri is not None and buffer_view_index is not None:
            raise GltfError('cannot reference both a URI and buffer view')
        if buffer_view_index is not None:
            buffer_view = gltf.buffer_views[int(buffer_view_index)]

        return GltfImage(gltf._file_path_callback, uri, buffer_view)


class GltfSampler:

    def __init__(
        self,
        mipmap_selection: MipmapSelection,
        minify_filter: TextureFilter,
        magnify_filter: TextureFilter,
        wrap: tuple[TextureWrap, TextureWrap]
    ):
        self.mipmap_selection = mipmap_selection
        self.minify_filter = minify_filter
        self.magnify_filter = magnify_filter
        self.wrap = wrap

    @classmethod
    def _parse(cls, data: dict) -> GltfSampler:
        magnify_filter = GLTF_MAG_FILTER_TO_TEXTURE_FILTER[data["magFilter"]]
        minify_filter, mipmap_selection = (
            GLTF_MIN_FILTER_TO_TEXTURE_FILTER_MIPMAP_SELECTION[
                data["minFilter"]
            ]
        )
        wrap_s = GLTF_WRAP_TO_TEXTURE_WRAP[data.get("wrapS")]
        wrap_t = GLTF_WRAP_TO_TEXTURE_WRAP[data.get("wrapT")]
        return GltfSampler(
            mipmap_selection,
            minify_filter, magnify_filter,
            (wrap_s, wrap_t)
        )


class Gltf:

    Accessor = GltfAccessor
    Buffer = GltfBuffer
    BufferView = GltfBufferView
    Camera = GltfCamera
    Image = GltfImage
    Error = GltfError
    Sampler = GltfSampler

    def __init__(
        self,
        file: BinaryIO,
        *,
        file_path_callback: GltfFilePathCallback =
            file_path_callback_disallowed,
    ):
        if sys.byteorder != 'little':
            raise RuntimeError('gltf only works on little endian platforms')

        self._file_path_callback = file_path_callback
        self._json_loaded = False
        self._bin: memoryview | None = None
        self.accessors: list[GltfAccessor] = []
        self.buffers: list[GltfBuffer] = []
        self.buffer_views: list[GltfBufferView] = []
        self.cameras: list[GltfCamera] = []
        self.images: list[GltfImage] = []
        self.samplers: list[GltfSampler] = []

        glb_args = self._parse_glb_header(file)
        if glb_args is None:
            self._load_gltf(file)
        else:
            self._load_glb(file, *glb_args)

    def _parse_glb_header(self, file: BinaryIO) -> tuple[int, int] | None:
        i = file.tell()
        header = file.read(12)
        if len(header) == 12:
            if header[:4] == b'glTF':
                return struct.unpack('II', header[4:])
        file.seek(i)
        return None

    def _load_gltf(self, file: BinaryIO) -> None:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            raise GltfError('file does not appear to be a GLTF')
        try:
            asset_data = data["asset"]
        except KeyError:
            raise self.Error(f'file does not appear to be a GLTF')
        version = str(asset_data["version"]).split('.')
        if version[0] != '2':
            raise self.Error(
                f'only compatible with GLTF version 2, got {".".join(version)}'
            )
        self._parse_json(data)

    def _load_glb(self, file: BinaryIO, version: int, length: int) -> None:
        if version != 2:
            raise self.Error(
                f'only compatible with GLTF version 2, got {version}'
            )
        # eliminate the header length, which we've already read
        remaining_bytes = length - 12
        while remaining_bytes > 0:
            chunk_header = file.read(8)
            if len(chunk_header) != 8:
                raise self.Error(f'unexpected eof in chunk header')
            remaining_bytes -= 8

            chunk_length = struct.unpack('I', chunk_header[:4])[0]
            if chunk_length > remaining_bytes:
                raise self.Error(f'chunk overflows beyond gltf data')
            chunk_type = chunk_header[4:]

            i = file.tell()
            if chunk_type == b'JSON':
                self._load_glb_json_chunk(file, chunk_length)
            elif chunk_type == b'BIN\x00':
                self._load_glb_bin_chunk(file, chunk_length)
            else:
                raise self.Error(f'unexpected chunk type: {chunk_type!r}')
            assert file.tell() == i + chunk_length
            remaining_bytes -= chunk_length
        # load bin data into the buffers
        for buffer in self.buffers:
            buffer._get_glb_bin_data(self._bin)

    def _load_glb_json_chunk(self, file: BinaryIO, length: int) -> None:
        json_file = PartialFile(file, length)
        data = json.load(json_file)
        self._parse_json(data)

    def _load_glb_bin_chunk(self, file: BinaryIO, length: int) -> None:
        if self._bin is not None:
            raise self.Error(f'GLTF contains multiple BIN chunks')
        self._bin = memoryview(
            np_array_from_buffer(file.read(length), dtype=np_uint8)
        )

    def _parse_json(self, data: dict) -> None:
        if self._json_loaded:
            raise self.Error(f'GLTF contains multiple JSON chunks')

        self._json_loaded = True
        self._parse_json_buffers(data)
        self._parse_json_buffer_views(data)
        self._parse_json_accessors(data)
        self._parse_json_cameras(data)
        self._parse_json_images(data)
        self._parse_json_samplers(data)

    def _parse_json_buffers(self, data: dict) -> None:
        try:
            json_buffers = data["buffers"]
        except KeyError:
            return
        for i, json_buffer in enumerate(json_buffers):
            self.buffers.append(self.Buffer._parse(
                self._file_path_callback,
                json_buffer,
                i
            ))

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
            self.accessors.append(self.Accessor._parse(self, json_accessor))

    def _parse_json_cameras(self, data: dict) -> None:
        try:
            json_cameras = data["cameras"]
        except KeyError:
            return
        for json_camera in json_cameras:
            self.cameras.append(self.Camera._parse(json_camera))

    def _parse_json_images(self, data: dict) -> None:
        try:
            json_images = data["images"]
        except KeyError:
            return
        for json_image in json_images:
            self.images.append(self.Image._parse(self, json_image))

    def _parse_json_samplers(self, data: dict) -> None:
        try:
            json_samplers = data["samplers"]
        except KeyError:
            return
        for json_sampler in json_samplers:
            self.samplers.append(self.Sampler._parse(json_sampler))


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


DATA_TYPE_TO_PY_DATA_TYPE: Final = {
    ctypes.c_int8: int,
    ctypes.c_uint8: int,
    ctypes.c_int16: int,
    ctypes.c_uint16: int,
    ctypes.c_uint32: int,
    ctypes.c_float: float,
}


GLTF_MAG_FILTER_TO_TEXTURE_FILTER: Final = {
    9728: TextureFilter.NEAREST,
    9729: TextureFilter.LINEAR,
}


GLTF_MIN_FILTER_TO_TEXTURE_FILTER_MIPMAP_SELECTION: Final = {
    9728: (TextureFilter.NEAREST, MipmapSelection.NONE),
    9729: (TextureFilter.LINEAR, MipmapSelection.NONE),
    9984: (TextureFilter.NEAREST, MipmapSelection.NEAREST),
    9985: (TextureFilter.LINEAR, MipmapSelection.NEAREST),
    9986: (TextureFilter.NEAREST, MipmapSelection.LINEAR),
    9987: (TextureFilter.LINEAR, MipmapSelection.LINEAR),
}


GLTF_WRAP_TO_TEXTURE_WRAP: Final = {
    33071: TextureWrap.CLAMP_TO_EDGE,
    33648: TextureWrap.REPEAT_MIRRORED,
    10497: TextureWrap.REPEAT,
    None: TextureWrap.REPEAT,
}
