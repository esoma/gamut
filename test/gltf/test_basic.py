
# gamut
from gamut.gltf import Gltf
from gamut.graphics import Image, MipmapSelection, TextureFilter, TextureWrap
import gamut.math
from gamut.math import FMatrix4, FVector2, UVector2
# python
from base64 import b64encode
from io import BytesIO
import json
from pathlib import Path
import struct
from typing import Any
# pytest
import pytest


def to_glb(data: dict, *, bin: bytes | None = None) -> bytes:
    json_data = json.dumps(data).encode('utf-8')
    bin_chunk_length = 0
    if bin is not None:
        bin_chunk_length = 8 + len(bin)

    data = b'glTF'
    data += struct.pack('II', 2, 20 + len(json_data) + bin_chunk_length)
    data += struct.pack('I', len(json_data))
    data += b'JSON'
    data += json_data
    if bin is not None:
        data += struct.pack('I', len(bin))
        data += b'BIN\x00'
        data += bin

    return BytesIO(data)


def to_gltf(data: dict) -> bytes:
    data["asset"] = {"version": '2'}
    return BytesIO(json.dumps(data).encode('utf-8'))


def test_empty_file() -> None:
    with pytest.raises(Gltf.Error) as ex:
        Gltf(BytesIO(b''))
    assert str(ex.value) == 'file does not appear to be a GLTF'


def test_empty_json_file() -> None:
    with pytest.raises(Gltf.Error) as ex:
        Gltf(BytesIO(b'{}'))
    assert str(ex.value) == 'file does not appear to be a GLTF'


@pytest.mark.parametrize("version", ['0', '1', '3', '1.2', '0.2', '3.2'])
def test_incompatible_gltf_version(version: str) -> None:
    with pytest.raises(Gltf.Error) as ex:
        Gltf(BytesIO(json.dumps({
            "asset": {"version": version}
        }).encode('utf-8')))
    assert str(ex.value) == (
        f'only compatible with GLTF version 2, got {version}'
    )


@pytest.mark.parametrize("version", [0, 1, 3])
def test_incompatible_glb_version(version: int) -> None:
    data = b'glTF'
    data += struct.pack('II', version, 0)
    with pytest.raises(Gltf.Error) as ex:
        Gltf(BytesIO(data))
    assert str(ex.value) == (
        f'only compatible with GLTF version 2, got {version}'
    )


def test_glb_unexpected_eof() -> None:
    data = b'glTF'
    data += struct.pack('II', 2, 13)
    with pytest.raises(Gltf.Error) as ex:
        Gltf(BytesIO(data))
    assert str(ex.value) == f'unexpected eof in chunk header'


def test_glb_unexpected_chunk_type() -> None:
    data = b'glTF'
    data += struct.pack('II', 2, 20)
    data += struct.pack('I', 0)
    data += b'XXXX'
    with pytest.raises(Gltf.Error) as ex:
        Gltf(BytesIO(data))
    assert str(ex.value) == f'unexpected chunk type: {b"XXXX"!r}'


def test_glb_multiple_json_chunks() -> None:
    data = b'glTF'
    data += struct.pack('II', 2, 32)
    data += struct.pack('I', 2)
    data += b'JSON{}'
    data += struct.pack('I', 2)
    data += b'JSON{}'
    with pytest.raises(Gltf.Error) as ex:
        Gltf(BytesIO(data))
    assert str(ex.value) == f'GLTF contains multiple JSON chunks'


def test_glb_multiple_bin_chunks() -> None:
    data = b'glTF'
    data += struct.pack('II', 2, 32)
    data += struct.pack('I', 2)
    data += b'BIN\x00{}'
    data += struct.pack('I', 2)
    data += b'BIN\x00{}'
    with pytest.raises(Gltf.Error) as ex:
        Gltf(BytesIO(data))
    assert str(ex.value) == f'GLTF contains multiple BIN chunks'


def test_glb_chunk_overflow() -> None:
    data = b'glTF'
    data += struct.pack('II', 2, 21)
    data += struct.pack('I', 2)
    data += b'JSON{}'
    with pytest.raises(Gltf.Error) as ex:
        Gltf(BytesIO(data))
    assert str(ex.value) == f'chunk overflows beyond gltf data'


@pytest.mark.parametrize("converter", [to_gltf, to_glb])
def test_no_data(converter: Any) -> None:
    data = converter({})
    gltf = Gltf(data)
    assert gltf.accessors == []
    assert gltf.buffers == []
    assert gltf.buffer_views == []


def test_glb_buffer_no_bin() -> None:
    data = to_glb({"buffers": [{"byteLength": 0}]})
    with pytest.raises(Gltf.Error) as ex:
        gltf = Gltf(data)
    assert str(ex.value) == f'buffer expects embedded binary data'


def test_gltf_buffer_no_bin() -> None:
    data = to_gltf({"buffers": [{"byteLength": 0}]})
    gltf = Gltf(data)
    with pytest.raises(Gltf.Error) as ex:
        gltf.buffers[0].data
    assert str(ex.value) == f'buffer has no URI'


@pytest.mark.parametrize("expected_data", [b'1234', b'1'])
def test_gltf_buffer_bin(expected_data: bytes) -> None:
    data = to_glb({"buffers": [
        {"byteLength": len(expected_data)},
    ]}, bin=b'1234')
    gltf = Gltf(data)
    assert gltf.buffers[0].data == expected_data


def test_gltf_buffer_bin_overflow() -> None:
    data = to_glb({"buffers": [
        {"byteLength": 5},
    ]}, bin=b'1234')
    with pytest.raises(Gltf.Error) as ex:
        gltf = Gltf(data)
    assert str(ex.value) == f'buffer overflow'


@pytest.mark.parametrize("converter", [to_gltf, to_glb])
@pytest.mark.parametrize("uri, expected_data", [
    (
        'data:;base64,MTIzNDU=',
        b'12345',
    ),
    (
        'data:;base64,MTIzNDU=',
        b'1',
    ),
])
def test_buffer_data_uri(
    converter: Any,
    uri: str,
    expected_data: bytes,
) -> None:
    data = converter({"buffers": [
        {"byteLength": len(expected_data), "uri": uri},
    ]})
    gltf = Gltf(data)
    assert bytes(gltf.buffers[0].data) == expected_data


@pytest.mark.parametrize("converter", [to_gltf, to_glb])
def test_buffer_data_uri_overflow(converter: Any) -> None:
    uri = 'data:;base64,MTIzNDU='
    data = converter({"buffers": [{"byteLength": 6, "uri": uri}]})
    gltf = Gltf(data)
    with pytest.raises(Gltf.Error) as ex:
        gltf.buffers[0].data
    assert str(ex.value) == f'buffer overflow'


@pytest.mark.parametrize("converter", [to_gltf, to_glb])
def test_buffer_data_file_not_allowed(converter: Any) -> None:
    uri = '\x00'
    data = converter({"buffers": [{"byteLength": 1, "uri": uri}]})
    gltf = Gltf(data)
    with pytest.raises(RuntimeError) as ex:
        gltf.buffers[0].data
    assert str(ex.value) == f'no external file loading allowed'


@pytest.mark.parametrize("converter", [to_gltf, to_glb])
def test_buffer_data_file(converter: Any) -> None:
    def file_path_callback(file: Path, length: int | None) -> memoryview:
        assert isinstance(file, Path)
        assert isinstance(length, int)
        assert str(file) == 'uri'
        assert length == 3
        return memoryview(b'123')

    uri = 'uri'
    data = converter({"buffers": [{"byteLength": '3', "uri": uri}]})
    gltf = Gltf(data, file_path_callback=file_path_callback)
    assert gltf.buffers[0].data == b'123'


@pytest.mark.parametrize("converter", [to_gltf, to_glb])
def test_buffer_data_file_bad_return_type(converter: Any) -> None:
    def file_path_callback(file: Path, length: int) -> Any:
        return None

    uri = 'uri'
    data = converter({"buffers": [{"byteLength": '3', "uri": uri}]})
    gltf = Gltf(data, file_path_callback=file_path_callback)
    with pytest.raises(Gltf.Error) as ex:
        gltf.buffers[0].data
    assert str(ex.value) == f'file path callback did not return memoryview'


@pytest.mark.parametrize("converter", [to_gltf, to_glb])
def test_buffer_data_file_bad_return_length(converter: Any) -> None:
    def file_path_callback(file: Path, length: int) -> Any:
        return memoryview(b'1')

    uri = 'uri'
    data = converter({"buffers": [{"byteLength": '3', "uri": uri}]})
    gltf = Gltf(data, file_path_callback=file_path_callback)
    with pytest.raises(Gltf.Error) as ex:
        gltf.buffers[0].data
    assert str(ex.value) == (
        'file path callback returned data with a different length than '
        'expected'
    )


@pytest.mark.parametrize("converter", [to_gltf, to_glb])
def test_buffer_data_view_get_data(converter: Any) -> None:
    uri = 'data:;base64,MTIzNDU2'
    data = converter({
        "buffers": [{"byteLength": 6, "uri": uri}],
        "bufferViews": [
            {"buffer": 0, "byteLength": 6},
            {"buffer": 0, "byteLength": 3, "byteOffset": 1},
            {"buffer": 0, "byteLength": 6, "stride": 2},
        ],
    })
    gltf = Gltf(data)

    with pytest.raises(ValueError) as ex:
        gltf.buffer_views[0].get_data(0)
    assert str(ex.value) == 'element size must be more than 0'
    with pytest.raises(ValueError) as ex:
        gltf.buffer_views[0].get_data(1, offset=-1)
    assert str(ex.value) == 'offset must be 0 or more'
    with pytest.raises(ValueError) as ex:
        gltf.buffer_views[2].get_data(3)
    assert str(ex.value) == 'element size cannot be larger than stride'

    assert isinstance(gltf.buffer_views[0].get_data(1), memoryview)
    assert bytes(gltf.buffer_views[0].get_data(1)) == b'123456'
    assert bytes(gltf.buffer_views[1].get_data(1)) == b'234'
    assert bytes(gltf.buffer_views[2].get_data(1)) == b'135'
    assert bytes(gltf.buffer_views[0].get_data(1, offset=1)) == b'23456'
    assert bytes(gltf.buffer_views[1].get_data(1, offset=1)) == b'34'
    assert bytes(gltf.buffer_views[2].get_data(1, offset=1)) == b'24'
    assert bytes(gltf.buffer_views[0].get_data(2)) == b'123456'
    assert bytes(gltf.buffer_views[1].get_data(2)) == b'23'
    assert bytes(gltf.buffer_views[2].get_data(2)) == b'123456'
    assert bytes(gltf.buffer_views[0].get_data(2, offset=1)) == b'2345'
    assert bytes(gltf.buffer_views[1].get_data(2, offset=1)) == b'34'
    assert bytes(gltf.buffer_views[2].get_data(2, offset=1)) == b'2345'
    assert bytes(gltf.buffer_views[0].get_data(3)) == b'123456'
    assert bytes(gltf.buffer_views[1].get_data(3)) == b'234'
    assert bytes(gltf.buffer_views[0].get_data(3, offset=1)) == b'234'
    assert bytes(gltf.buffer_views[1].get_data(3, offset=1)) == b''
    assert bytes(gltf.buffer_views[0].get_data(4)) == b'1234'
    assert bytes(gltf.buffer_views[1].get_data(4)) == b''
    assert bytes(gltf.buffer_views[0].get_data(4, offset=1)) == b'2345'
    assert bytes(gltf.buffer_views[0].get_data(5)) == b'12345'
    assert bytes(gltf.buffer_views[0].get_data(6, offset=1)) == b''
    assert bytes(gltf.buffer_views[0].get_data(6)) == b'123456'
    assert bytes(gltf.buffer_views[0].get_data(7)) == b''


@pytest.mark.parametrize("array, gltf_component_type, gltf_type", [
    (
        gamut.math.I8Array(0, 1, 2, 3, 4, 5),
        5120,
        "SCALAR",
    ),
    (
        gamut.math.U8Array(0, 1, 2, 3, 4, 5),
        5121,
        "SCALAR",
    ),
    (
        gamut.math.I16Array(0, 1, 2, 3, 4, 5),
        5122,
        "SCALAR",
    ),
    (
        gamut.math.U16Array(0, 1, 2, 3, 4, 5),
        5123,
        "SCALAR",
    ),
    (
        gamut.math.U32Array(0, 1, 2, 3, 4, 5),
        5125,
        "SCALAR",
    ),
    (
        gamut.math.FArray(0, 1, 2, 3, 4, 5),
        5126,
        "SCALAR",
    ),
    (
        gamut.math.I8Vector2Array(
            gamut.math.I8Vector2(0, 1),
            gamut.math.I8Vector2(2, 3),
            gamut.math.I8Vector2(4, 5),
        ),
        5120,
        "VEC2",
    ),
    (
        gamut.math.U8Vector2Array(
            gamut.math.U8Vector2(0, 1),
            gamut.math.U8Vector2(2, 3),
            gamut.math.U8Vector2(4, 5),
        ),
        5121,
        "VEC2",
    ),
    (
        gamut.math.I16Vector2Array(
            gamut.math.I16Vector2(0, 1),
            gamut.math.I16Vector2(2, 3),
            gamut.math.I16Vector2(4, 5),
        ),
        5122,
        "VEC2",
    ),
    (
        gamut.math.U16Vector2Array(
            gamut.math.U16Vector2(0, 1),
            gamut.math.U16Vector2(2, 3),
            gamut.math.U16Vector2(4, 5),
        ),
        5123,
        "VEC2",
    ),
    (
        gamut.math.U32Vector2Array(
            gamut.math.U32Vector2(0, 1),
            gamut.math.U32Vector2(2, 3),
            gamut.math.U32Vector2(4, 5),
        ),
        5125,
        "VEC2",
    ),
    (
        gamut.math.FVector2Array(
            gamut.math.FVector2(0, 1),
            gamut.math.FVector2(2, 3),
            gamut.math.FVector2(4, 5),
        ),
        5126,
        "VEC2",
    ),
    (
        gamut.math.I8Vector3Array(
            gamut.math.I8Vector3(0, 1, 6),
            gamut.math.I8Vector3(2, 3, 7),
            gamut.math.I8Vector3(4, 5, 8),
        ),
        5120,
        "VEC3",
    ),
    (
        gamut.math.U8Vector3Array(
            gamut.math.U8Vector3(0, 1, 6),
            gamut.math.U8Vector3(2, 3, 7),
            gamut.math.U8Vector3(4, 5, 8),
        ),
        5121,
        "VEC3",
    ),
    (
        gamut.math.I16Vector3Array(
            gamut.math.I16Vector3(0, 1, 6),
            gamut.math.I16Vector3(2, 3, 7),
            gamut.math.I16Vector3(4, 5, 8),
        ),
        5122,
        "VEC3",
    ),
    (
        gamut.math.U16Vector3Array(
            gamut.math.U16Vector3(0, 1, 6),
            gamut.math.U16Vector3(2, 3, 7),
            gamut.math.U16Vector3(4, 5, 8),
        ),
        5123,
        "VEC3",
    ),
    (
        gamut.math.U32Vector3Array(
            gamut.math.U32Vector3(0, 1, 6),
            gamut.math.U32Vector3(2, 3, 7),
            gamut.math.U32Vector3(4, 5, 8),
        ),
        5125,
        "VEC3",
    ),
    (
        gamut.math.FVector3Array(
            gamut.math.FVector3(0, 1, 6),
            gamut.math.FVector3(2, 3, 7),
            gamut.math.FVector3(4, 5, 8),
        ),
        5126,
        "VEC3",
    ),
    (
        gamut.math.I8Vector4Array(
            gamut.math.I8Vector4(0, 1, 6, 9),
            gamut.math.I8Vector4(2, 3, 7, 10),
            gamut.math.I8Vector4(4, 5, 8, 11),
        ),
        5120,
        "VEC4",
    ),
    (
        gamut.math.U8Vector4Array(
            gamut.math.U8Vector4(0, 1, 6, 9),
            gamut.math.U8Vector4(2, 3, 7, 10),
            gamut.math.U8Vector4(4, 5, 8, 11),
        ),
        5121,
        "VEC4",
    ),
    (
        gamut.math.I16Vector4Array(
            gamut.math.I16Vector4(0, 1, 6, 9),
            gamut.math.I16Vector4(2, 3, 7, 10),
            gamut.math.I16Vector4(4, 5, 8, 11),
        ),
        5122,
        "VEC4",
    ),
    (
        gamut.math.U16Vector4Array(
            gamut.math.U16Vector4(0, 1, 6, 9),
            gamut.math.U16Vector4(2, 3, 7, 10),
            gamut.math.U16Vector4(4, 5, 8, 11),
        ),
        5123,
        "VEC4",
    ),
    (
        gamut.math.U32Vector4Array(
            gamut.math.U32Vector4(0, 1, 6, 9),
            gamut.math.U32Vector4(2, 3, 7, 10),
            gamut.math.U32Vector4(4, 5, 8, 11),
        ),
        5125,
        "VEC4",
    ),
    (
        gamut.math.FVector4Array(
            gamut.math.FVector4(0, 1, 6, 9),
            gamut.math.FVector4(2, 3, 7, 10),
            gamut.math.FVector4(4, 5, 8, 11),
        ),
        5126,
        "VEC4",
    ),
    (
        gamut.math.FMatrix2Array(
            gamut.math.FMatrix2(0, 1, 6, 9),
            gamut.math.FMatrix2(2, 3, 7, 10),
            gamut.math.FMatrix2(4, 5, 8, 11),
        ),
        5126,
        "MAT2",
    ),
    (
        gamut.math.FMatrix3Array(
            gamut.math.FMatrix3(0, 1, 6, 9, 12, 15, 18, 21, 24),
            gamut.math.FMatrix3(2, 3, 7, 10, 13, 16, 19, 22, 25),
            gamut.math.FMatrix3(4, 5, 8, 11, 14, 17, 20, 23, 26),
        ),
        5126,
        "MAT3",
    ),
    (
        gamut.math.FMatrix4Array(
            gamut.math.FMatrix4(
                0, 1, 6, 9,
                12, 15, 18, 21,
                24, 27, 30, 33,
                36, 39, 42, 45,
            ),
            gamut.math.FMatrix4(
                2, 3, 7, 10,
                13, 16, 19, 22,
                25, 28, 31, 34,
                37, 40, 43, 46,
            ),
            gamut.math.FMatrix4(
                4, 5, 8, 11,
                14, 17, 20, 23,
                26, 29, 32, 35,
                38, 41, 44, 47,
            ),
        ),
        5126,
        "MAT4",
    ),
])
@pytest.mark.parametrize("converter", [to_gltf, to_glb])
def test_accessor_of_buffer_view(
    converter: Any,
    array: Any,
    gltf_component_type: int,
    gltf_type: str
) -> None:
    array_byte_length = len(bytes(array))
    uri_data = b64encode(array).decode('ascii')
    data = converter({
        "buffers": [{
            "byteLength": array_byte_length,
            "uri": f'data:;base64,{uri_data}'
        }],
        "bufferViews": [{
            "buffer": 0,
            "byteLength": array_byte_length
        }],
        "accessors": [{
            "componentType": gltf_component_type,
            "type": gltf_type,
            "count": len(array),
            "bufferView": 0,
        }],
    })
    gltf = Gltf(data)

    assert isinstance(gltf.accessors[0].data, type(array))
    assert gltf.accessors[0].data == array


@pytest.mark.parametrize(
    "array_type, component_type, gltf_component_type, gltf_type", [
    (gamut.math.I8Array, int, 5120, "SCALAR"),
    (gamut.math.U8Array, int, 5121, "SCALAR"),
    (gamut.math.I16Array, int, 5122, "SCALAR"),
    (gamut.math.U16Array, int, 5123, "SCALAR"),
    (gamut.math.U32Array, int, 5125, "SCALAR"),
    (gamut.math.FArray, float, 5126, "SCALAR"),
    (gamut.math.I8Vector2Array, gamut.math.I8Vector2, 5120, "VEC2"),
    (gamut.math.U8Vector2Array, gamut.math.U8Vector2, 5121, "VEC2"),
    (gamut.math.I16Vector2Array, gamut.math.I16Vector2, 5122, "VEC2"),
    (gamut.math.U16Vector2Array, gamut.math.U16Vector2, 5123, "VEC2"),
    (gamut.math.U32Vector2Array, gamut.math.U32Vector2, 5125, "VEC2"),
    (gamut.math.FVector2Array, gamut.math.FVector2, 5126, "VEC2"),
    (gamut.math.I8Vector3Array, gamut.math.I8Vector3, 5120, "VEC3"),
    (gamut.math.U8Vector3Array, gamut.math.U8Vector3, 5121, "VEC3"),
    (gamut.math.I16Vector3Array, gamut.math.I16Vector3, 5122, "VEC3"),
    (gamut.math.U16Vector3Array, gamut.math.U16Vector3, 5123, "VEC3"),
    (gamut.math.U32Vector3Array, gamut.math.U32Vector3, 5125, "VEC3"),
    (gamut.math.FVector3Array, gamut.math.FVector3, 5126, "VEC3"),
    (gamut.math.I8Vector4Array, gamut.math.I8Vector4, 5120, "VEC4"),
    (gamut.math.U8Vector4Array, gamut.math.U8Vector4, 5121, "VEC4"),
    (gamut.math.I16Vector4Array, gamut.math.I16Vector4, 5122, "VEC4"),
    (gamut.math.U16Vector4Array, gamut.math.U16Vector4, 5123, "VEC4"),
    (gamut.math.U32Vector4Array, gamut.math.U32Vector4, 5125, "VEC4"),
    (gamut.math.FVector4Array, gamut.math.FVector4, 5126, "VEC4"),
    (gamut.math.FMatrix2Array, gamut.math.FMatrix2, 5126, "MAT2"),
    (gamut.math.FMatrix3Array, gamut.math.FMatrix3, 5126, "MAT3"),
    (gamut.math.FMatrix4Array, gamut.math.FMatrix4, 5126, "MAT4"),
])
@pytest.mark.parametrize("converter", [to_gltf, to_glb])
def test_accessor_empty(
    converter: Any,
    array_type: Any,
    component_type: Any,
    gltf_component_type: int,
    gltf_type: str
) -> None:
    data = converter({
        "accessors": [{
            "componentType": gltf_component_type,
            "type": gltf_type,
            "count": 2,
        }],
    })
    gltf = Gltf(data)

    assert isinstance(gltf.accessors[0].data, array_type)
    assert gltf.accessors[0].data == array_type(
        component_type(0),
        component_type(0)
    )


@pytest.mark.parametrize("converter", [to_gltf, to_glb])
def test_accessor_buffer_overflow(converter: Any) -> None:
    data = converter({
        "buffers": [{
            "byteLength": 0,
            "uri": f'data:;base64,'
        }],
        "bufferViews": [{
            "buffer": 0,
            "byteLength": 0
        }],
        "accessors": [{
            "componentType": 5120,
            "type": 'SCALAR',
            "count": 1,
            "bufferView": 0,
        }],
    })
    gltf = Gltf(data)

    with pytest.raises(Gltf.Error) as ex:
        gltf.accessors[0].data
    assert str(ex.value) == 'buffer overflow'


@pytest.mark.parametrize("converter", [to_gltf, to_glb])
def test_accessor_normalized(converter: Any) -> None:
    data = converter({
        "buffers": [{
            "byteLength": 0,
            "uri": f'data:;base64,'
        }],
        "bufferViews": [{
            "buffer": 0,
            "byteLength": 0
        }],
        "accessors": [{
            "componentType": 5120,
            "type": 'SCALAR',
            "count": 1,
            "bufferView": 0,
            "normalized": True,
        }],
    })

    with pytest.raises(NotImplementedError) as ex:
        Gltf(data)
    assert str(ex.value) == 'normalized accessors not supported'


@pytest.mark.parametrize("converter", [to_gltf, to_glb])
def test_accessor_sparse(converter: Any) -> None:
    data = converter({
        "buffers": [{
            "byteLength": 0,
            "uri": f'data:;base64,'
        }],
        "bufferViews": [{
            "buffer": 0,
            "byteLength": 0
        }],
        "accessors": [{
            "componentType": 5120,
            "type": 'SCALAR',
            "count": 1,
            "bufferView": 0,
            "sparse": {},
        }],
    })

    with pytest.raises(NotImplementedError) as ex:
        Gltf(data)
    assert str(ex.value) == 'sparse accessors not supported'


@pytest.mark.parametrize("converter", [to_gltf, to_glb])
def test_ortho_camera(converter: Any) -> None:
    data = converter({
        "cameras": [{
            "type": 'orthographic',
            "orthographic": {
                "xmag": .8,
                "ymag": 1.2,
                "zfar": 10,
                "znear": 1,
            },
        }],
    })
    gltf = Gltf(data)

    p = gltf.cameras[0].get_projection(UVector2(100, 60))
    assert p == FMatrix4.orthographic(
        -40, 40,
        -36, 36,
        1, 10
    )


@pytest.mark.parametrize("converter", [to_gltf, to_glb])
def test_perspective_camera_well_defined(converter: Any) -> None:
    data = converter({
        "cameras": [{
            "type": 'perspective',
            "perspective": {
                "aspectRatio": 2,
                "yfov": .4,
                "zfar": 10,
                "znear": 1,
            },
        }],
    })
    gltf = Gltf(data)

    p = gltf.cameras[0].get_projection(UVector2(100, 60))
    assert p == FMatrix4.perspective(.4, 2, 1, 10)


@pytest.mark.parametrize("converter", [to_gltf, to_glb])
def test_perspective_camera_no_aspect_ratio(converter: Any) -> None:
    data = converter({
        "cameras": [{
            "type": 'perspective',
            "perspective": {
                "yfov": .4,
                "zfar": 10,
                "znear": 1,
            },
        }],
    })
    gltf = Gltf(data)

    p = gltf.cameras[0].get_projection(UVector2(100, 60))
    assert p == FMatrix4.perspective(.4, 100 / 60, 1, 10)


@pytest.mark.parametrize("converter", [to_gltf, to_glb])
def test_perspective_camera_no_zfar(converter: Any) -> None:
    data = converter({
        "cameras": [{
            "type": 'perspective',
            "perspective": {
                "aspectRatio": 2,
                "yfov": .4,
                "znear": 1,
            },
        }],
    })
    gltf = Gltf(data)

    p = gltf.cameras[0].get_projection(UVector2(100, 60))
    assert p == FMatrix4.perspective(.4, 2, 1, FVector2.get_limits()[1])


@pytest.mark.parametrize("converter", [to_gltf, to_glb])
def test_image_uri_and_buffer_view(converter: Any) -> None:
    data = converter({
        "images": [{
            "mimeType": 'image/png',
            "uri": 'somefile',
            "bufferView": 0,
        }],
    })
    with pytest.raises(Gltf.Error) as ex:
        gltf = Gltf(data)
    assert str(ex.value) == 'cannot reference both a URI and buffer view'


@pytest.mark.parametrize("converter", [to_gltf, to_glb])
@pytest.mark.parametrize("file_name, mime_type", [
    ('gamut_rgba16.png', 'image/png'),
    ('gamut.jpg', 'image/jpg'),
])
def test_image_data_uri(
    resources: Path,
    file_name: str,
    mime_type: str,
    converter: Any
) -> None:
    with open(resources / file_name, 'rb') as f:
        image_bytes = f.read()
    image = Image(BytesIO(image_bytes))
    image_b64 = b64encode(image_bytes).decode('utf-8')
    uri = f'data:;base64,{image_b64}'
    data = converter({
        "images": [{
            "mimeType": mime_type,
            "uri": uri
        }],
    })
    gltf = Gltf(data)

    assert isinstance(gltf.images[0].data, Image)
    assert gltf.images[0].data.to_bytes() == image.to_bytes()


@pytest.mark.parametrize("converter", [to_gltf, to_glb])
@pytest.mark.parametrize("file_name, mime_type", [
    ('gamut_rgba16.png', 'image/png'),
    ('gamut.jpg', 'image/jpg'),
])
def test_image_path_uri_disallowed(
    resources: Path,
    file_name: str,
    mime_type: str,
    converter: Any
) -> None:
    data = converter({
        "images": [{
            "mimeType": mime_type,
            "uri": 'somefile'
        }],
    })
    gltf = Gltf(data)

    with pytest.raises(RuntimeError) as ex:
        gltf.images[0].data
    assert str(ex.value) == 'no external file loading allowed'


@pytest.mark.parametrize("converter", [to_gltf, to_glb])
@pytest.mark.parametrize("file_name, mime_type", [
    ('gamut_rgba16.png', 'image/png'),
    ('gamut.jpg', 'image/jpg'),
])
def test_image_path_uri(
    resources: Path,
    file_name: str,
    mime_type: str,
    converter: Any
) -> None:
    with open(resources / file_name, 'rb') as f:
        image_bytes = f.read()
    image = Image(BytesIO(image_bytes))

    def file_path_callback(file: Path, length: int | None) -> memoryview:
        assert isinstance(file, Path)
        assert length is None
        assert str(file) == 'somefile'
        return memoryview(image_bytes)

    data = converter({
        "images": [{
            "mimeType": mime_type,
            "uri": 'somefile'
        }],
    })
    gltf = Gltf(data, file_path_callback=file_path_callback)

    assert isinstance(gltf.images[0].data, Image)
    assert gltf.images[0].data.to_bytes() == image.to_bytes()


@pytest.mark.parametrize("converter", [to_gltf, to_glb])
@pytest.mark.parametrize("file_name, mime_type", [
    ('gamut_rgba16.png', 'image/png'),
    ('gamut.jpg', 'image/jpg'),
])
def test_image_buffer_view(
    resources: Path,
    file_name: str,
    mime_type: str,
    converter: Any
) -> None:
    with open(resources / file_name, 'rb') as f:
        image_bytes = f.read()
    image = Image(BytesIO(image_bytes))
    image_b64 = b64encode(image_bytes).decode('utf-8')
    uri = f'data:;base64,{image_b64}'
    data = converter({
        "buffers": [{
            "byteLength": len(image_bytes),
            "uri": uri
        }],
        "bufferViews": [{
            "buffer": 0,
            "byteLength": len(image_bytes)
        }],
        "images": [{
            "mimeType": mime_type,
            "bufferView": 0
        }],
    })
    gltf = Gltf(data)

    assert isinstance(gltf.images[0].data, Image)
    assert gltf.images[0].data.to_bytes() == image.to_bytes()


@pytest.mark.parametrize("gltf_mag_filter, mag_filter", [
    (9728, TextureFilter.NEAREST),
    (9729, TextureFilter.LINEAR),
])
@pytest.mark.parametrize("gltf_min_filter, min_filter, mipmap", [
    (9728, TextureFilter.NEAREST, MipmapSelection.NONE),
    (9729, TextureFilter.LINEAR, MipmapSelection.NONE),
    (9984, TextureFilter.NEAREST, MipmapSelection.NEAREST),
    (9985, TextureFilter.LINEAR, MipmapSelection.NEAREST),
    (9986, TextureFilter.NEAREST, MipmapSelection.LINEAR),
    (9987, TextureFilter.LINEAR, MipmapSelection.LINEAR),
])
@pytest.mark.parametrize("gltf_wrap_s, wrap_s", [
    (33071, TextureWrap.CLAMP_TO_EDGE),
    (33648, TextureWrap.REPEAT_MIRRORED),
    (10497, TextureWrap.REPEAT),
])
@pytest.mark.parametrize("gltf_wrap_t, wrap_t", [
    (33071, TextureWrap.CLAMP_TO_EDGE),
    (33648, TextureWrap.REPEAT_MIRRORED),
    (10497, TextureWrap.REPEAT),
])
@pytest.mark.parametrize("converter", [to_gltf, to_glb])
def test_sampler(
    gltf_mag_filter: int,
    mag_filter: TextureFilter,
    gltf_min_filter: int,
    min_filter: TextureFilter,
    mipmap: MipmapSelection,
    gltf_wrap_s: int,
    wrap_s: TextureWrap,
    gltf_wrap_t: int,
    wrap_t: TextureWrap,
    converter: Any
) -> None:
    data = converter({
        "samplers": [{
            "magFilter": gltf_mag_filter,
            "minFilter": gltf_min_filter,
            "wrapS": gltf_wrap_s,
            "wrapT": gltf_wrap_t,
        }],
    })
    gltf = Gltf(data)
    assert gltf.samplers[0].magnify_filter == mag_filter
    assert gltf.samplers[0].minify_filter == min_filter
    assert gltf.samplers[0].mipmap_selection == mipmap
    assert gltf.samplers[0].wrap == (wrap_s, wrap_t)


@pytest.mark.parametrize("converter", [to_gltf, to_glb])
def test_sampler_wrap_defaults(converter: Any) -> None:
    data = converter({
        "samplers": [{
            "magFilter": 9728,
            "minFilter": 9728,
        }],
    })
    gltf = Gltf(data)
    assert gltf.samplers[0].wrap == (TextureWrap.REPEAT, TextureWrap.REPEAT)
