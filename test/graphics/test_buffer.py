
from __future__ import annotations
# gamut
from gamut import Application, Window
from gamut._glcontext import get_gl_context
from gamut.graphics import (Buffer, BufferFrequency, BufferNature, BufferView,
                            BufferViewMap, Shader)
from gamut.graphics._buffer import use_buffer_view_map_with_shader
from gamut.math import (DArray, DMatrix2x2, DMatrix2x2Array, DMatrix2x3,
                        DMatrix2x3Array, DMatrix2x4, DMatrix2x4Array,
                        DMatrix3x2, DMatrix3x2Array, DMatrix3x3,
                        DMatrix3x3Array, DMatrix3x4, DMatrix3x4Array,
                        DMatrix4x2, DMatrix4x2Array, DMatrix4x3,
                        DMatrix4x3Array, DMatrix4x4, DMatrix4x4Array, DVector2,
                        DVector2Array, DVector3, DVector3Array, DVector4,
                        DVector4Array, FArray, FMatrix2x2, FMatrix2x2Array,
                        FMatrix2x3, FMatrix2x3Array, FMatrix2x4,
                        FMatrix2x4Array, FMatrix3x2, FMatrix3x2Array,
                        FMatrix3x3, FMatrix3x3Array, FMatrix3x4,
                        FMatrix3x4Array, FMatrix4x2, FMatrix4x2Array,
                        FMatrix4x3, FMatrix4x3Array, FMatrix4x4,
                        FMatrix4x4Array, FVector2, FVector2Array, FVector3,
                        FVector3Array, FVector4, FVector4Array, I8Array,
                        I8Vector2, I8Vector2Array, I8Vector3, I8Vector3Array,
                        I8Vector4, I8Vector4Array, I16Array, I16Vector2,
                        I16Vector2Array, I16Vector3, I16Vector3Array,
                        I16Vector4, I16Vector4Array, I32Array, I32Vector2,
                        I32Vector2Array, I32Vector3, I32Vector3Array,
                        I32Vector4, I32Vector4Array, U8Array, U8Vector2,
                        U8Vector2Array, U8Vector3, U8Vector3Array, U8Vector4,
                        U8Vector4Array, U16Array, U16Vector2, U16Vector2Array,
                        U16Vector3, U16Vector3Array, U16Vector4,
                        U16Vector4Array, U32Array, U32Vector2, U32Vector2Array,
                        U32Vector3, U32Vector3Array, U32Vector4,
                        U32Vector4Array, U64Vector2)
# python
import ctypes
import gc
from struct import unpack as c_unpack
import threading
from typing import Any, Final, Optional
# pytest
import pytest


def get_size_of(t: Any) -> int:
    try:
        return t.get_size()
    except AttributeError:
        return ctypes.sizeof(t)


VIEW_DATA_TYPES: Final = (
    ctypes.c_float, ctypes.c_double,
    ctypes.c_int8, ctypes.c_uint8,
    ctypes.c_int16, ctypes.c_uint16,
    ctypes.c_int32, ctypes.c_uint32,
    FVector2, DVector2,
    I8Vector2, I16Vector2, I32Vector2,
    U8Vector2, U16Vector2, U32Vector2,
    FVector3, DVector3,
    I8Vector3, I16Vector3, I32Vector3,
    U8Vector3, U16Vector3, U32Vector3,
    FVector4, DVector4,
    I8Vector4, I16Vector4, I32Vector4,
    U8Vector4, U16Vector4, U32Vector4,
    FMatrix2x2, DMatrix2x2,
    FMatrix2x3, DMatrix2x3,
    FMatrix2x4, DMatrix2x4,
    FMatrix3x2, DMatrix3x2,
    FMatrix3x3, DMatrix3x3,
    FMatrix3x4, DMatrix3x4,
    FMatrix4x2, DMatrix4x2,
    FMatrix4x3, DMatrix4x3,
    FMatrix4x4, DMatrix4x4,
)


CTYPES_TO_STRUCT_NAME: Final[dict[Any, str]] = {
    ctypes.c_float: 'f',
    ctypes.c_double: 'd',
    ctypes.c_int8: 'b',
    ctypes.c_uint8: 'B',
    ctypes.c_int16: 'h',
    ctypes.c_uint16: 'H',
    ctypes.c_int32: 'i',
    ctypes.c_uint32: 'I',
}


def test_empty_buffer() -> None:
    buffer = Buffer()
    assert len(buffer) == 0


@pytest.mark.parametrize("length", [-100, -1])
def test_initialize_length_invalid_value(length: int) -> None:
    with pytest.raises(ValueError) as excinfo:
        Buffer(length)
    assert str(excinfo.value) == 'data must be 0 or more'


@pytest.mark.parametrize("length", [0, 1, 2, 10, 1000])
def test_initialize_length(length: int) -> None:
    buffer = Buffer(length)
    assert len(buffer) == length


@pytest.mark.parametrize("length", [0, 1, 2, 10, 1000])
def test_length(length: int) -> None:
    buffer = Buffer(b'\x00' * length)
    assert len(buffer) == length


def test_default_access() -> None:
    buffer = Buffer(b'')
    assert buffer.frequency == BufferFrequency.STATIC
    assert buffer.nature == BufferNature.DRAW


@pytest.mark.parametrize("data", [object(), 1.0])
def test_data_invalid(data: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Buffer(data)
    assert str(excinfo.value) == 'data must be bytes or an integer'


@pytest.mark.parametrize("frequency", list(BufferFrequency))
@pytest.mark.parametrize("nature", list(BufferNature))
def test_frequency_nature_combinations(
    frequency: BufferFrequency,
    nature: BufferNature
) -> None:
    buffer = Buffer(b'', frequency=frequency, nature=nature)
    assert buffer.frequency is frequency
    assert buffer.nature is nature


@pytest.mark.parametrize("frequency", [None, 0, 'abc'])
def test_frequency_invalid(frequency: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Buffer(0, frequency=frequency)
    assert str(excinfo.value) == 'frequency must be <enum \'BufferFrequency\'>'


@pytest.mark.parametrize("nature", [None, 0, 'abc'])
def test_nature_invalid(nature: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Buffer(0, nature=nature)
    assert str(excinfo.value) == 'nature must be <enum \'BufferNature\'>'


@pytest.mark.parametrize("data", [
    b'',
    b'\x00\x01\x02\x03\x04',
])
def test_bytes(data: bytes) -> None:
    buffer = Buffer(data)
    assert buffer.bytes == data
    buffer.bytes = b'\x00\x00'
    assert buffer.bytes == b'\x00\x00'
    assert len(buffer) == 2
    buffer.bytes = b''
    assert buffer.bytes == b''
    assert len(buffer) == 0
    with pytest.raises(TypeError) as excinfo:
        buffer.bytes = object() # type: ignore
    assert str(excinfo.value) == 'data must be bytes'


@pytest.mark.parametrize("data", [None, object(), 1.0])
def test_replace_invalid_data_type(data: Any) -> None:
    buffer = Buffer(b'\x00\x01\x02\x03')
    with pytest.raises(TypeError) as excinfo:
        buffer.replace(0, data)
    assert str(excinfo.value) == 'data must be bytes or a Buffer'


@pytest.mark.parametrize("offset", ['abcd', (1,), (1, 2, 3)])
def test_replace_invalid_offset_type(offset: Any) -> None:
    buffer = Buffer(b'\x00\x01\x02\x03')
    with pytest.raises(TypeError) as excinfo:
        buffer.replace(offset, b'\x00')
    assert str(excinfo.value) == 'offset must be int'


@pytest.mark.parametrize("offset", [-100, -1])
def test_replace_invalid_offset_value(offset: Any) -> None:
    buffer = Buffer(b'\x00\x01\x02\x03')
    with pytest.raises(ValueError) as excinfo:
        buffer.replace(offset, b'\x00')
    assert str(excinfo.value) == 'offset must be 0 or more'


@pytest.mark.parametrize("data_offset", ['abcd', (1,), (1, 2, 3)])
def test_replace_invalid_data_offset_type(data_offset: Any) -> None:
    buffer = Buffer(b'\x00\x01\x02\x03')
    with pytest.raises(TypeError) as excinfo:
        buffer.replace(0, b'\x00', data_offset=data_offset)
    assert str(excinfo.value) == 'data offset must be int'


@pytest.mark.parametrize("data_offset", [-100, -1])
def test_replace_invalid_data_offset_value(data_offset: Any) -> None:
    buffer = Buffer(b'\x00\x01\x02\x03')
    with pytest.raises(ValueError) as excinfo:
        buffer.replace(0, b'\x00', data_offset=data_offset)
    assert str(excinfo.value) == 'data offset must be 0 or more'


@pytest.mark.parametrize("length", ['abcd', (1,), (1, 2, 3)])
def test_replace_invalid_length_type(length: Any) -> None:
    buffer = Buffer(b'\x00\x01\x02\x03')
    with pytest.raises(TypeError) as excinfo:
        buffer.replace(0, b'\x00', length=length)
    assert str(excinfo.value) == 'length must be int'


@pytest.mark.parametrize("length", [-100, -1])
def test_replace_invalid_data_offset_value(length: Any) -> None:
    buffer = Buffer(b'\x00\x01\x02\x03')
    with pytest.raises(ValueError) as excinfo:
        buffer.replace(0, b'\x00', length=length)
    assert str(excinfo.value) == 'length must be 0 or more'


@pytest.mark.parametrize("data_offset, length, data", [
    (0, 3, b'\x00' * 2),
    (3, 1, b'\x00' * 2),
])
def test_replace_read_overflow(
    data_offset: int,
    length: int,
    data: bytes
) -> None:
    buffer = Buffer(b'\x00\x01\x02\x03')
    with pytest.raises(ValueError) as excinfo:
        buffer.replace(0, data, data_offset=data_offset, length=length)
    assert str(excinfo.value) == (
        'requested offset, length and data would read beyond the end of the '
        'buffer'
    )


@pytest.mark.parametrize("offset, data", [
    (0, b'\x00' * 5),
    (1, b'\x00' * 4),
    (2, b'\x00' * 3),
    (3, b'\x00' * 2),
    (4, b'\x00'),
    (5, b''),
])
def test_replace_write_overflow(offset: int, data: bytes) -> None:
    buffer = Buffer(b'\x00\x01\x02\x03')
    with pytest.raises(ValueError) as excinfo:
        buffer.replace(offset, data)
    assert str(excinfo.value) == (
        'requested offset and data would write beyond the end of the buffer'
    )


@pytest.mark.parametrize("offset, data, data_offset, length", [
    (0, b'\x05', None, None),
    (0, b'\x05' * 2, None, None),
    (0, b'\x05' * 3, None, None),
    (0, b'\x05' * 4, None, None),
    (1, b'\x05' * 3, None, None),
    (2, b'\x05' * 2, None, None),
    (3, b'\x05' * 1, None, None),
    (4, b'', None, None),
    (0, b'\x05' * 4, 0, None),
    (0, b'\x05' * 4, 1, None),
    (0, b'\x05' * 4, 2, None),
    (0, b'\x05' * 4, None, 1),
    (0, b'\x05' * 4, None, 2),
])
@pytest.mark.parametrize("data_type", [bytes, Buffer])
def test_replace(
    offset: int,
    data: bytes,
    data_offset: int | None,
    length: int | None,
    data_type: type[bytes] | type[Buffer]
) -> None:
    typed_data = data_type(data)

    if data_offset is None:
        effective_data_offset = 0
    else:
        effective_data_offset = data_offset
    if length is None:
        effective_length = len(data) - effective_data_offset
    else:
        effective_length = length

    original_data = b'\x00\x01\x02\x03'
    expected_data = (
        original_data[:offset] +
        data[effective_data_offset:effective_data_offset + effective_length] +
        original_data[offset + effective_length:]
    )
    buffer = Buffer(original_data)
    buffer.replace(offset, typed_data, data_offset=data_offset, length=length)
    assert buffer.bytes == expected_data


@pytest.mark.parametrize("data", [None, object(), 1.0])
def test_clear_invalid_data_type(data: Any) -> None:
    buffer = Buffer(b'\x00\x01\x02\x03')
    with pytest.raises(TypeError) as excinfo:
        buffer.clear(data)
    assert str(excinfo.value) == 'data must be bytes'


@pytest.mark.parametrize("data", [b'', b'\x00\x01'])
def test_clear_invalid_data_length(data: Any) -> None:
    buffer = Buffer(b'\x00\x01\x02\x03')
    with pytest.raises(TypeError) as excinfo:
        buffer.clear(data)
    assert str(excinfo.value) == 'data must be a single byte'


@pytest.mark.parametrize("range", ['abcd', (1,), (1, 2, 3)])
def test_clear_invalid_range_type(range: Any) -> None:
    buffer = Buffer(b'\x00\x01\x02\x03')
    with pytest.raises(TypeError) as excinfo:
        buffer.clear(b'\x00', range=range)
    assert str(excinfo.value) == 'range must be U64Vector2'


@pytest.mark.parametrize("range", [U64Vector2(0, 5), U64Vector2(5, 6)])
def test_clear_invalid_range_beyond_length(range: U64Vector2) -> None:
    buffer = Buffer(b'\x00\x01\x02\x03')
    with pytest.raises(ValueError) as excinfo:
        buffer.clear(b'\x00', range=range)
    assert str(excinfo.value) == (
        'range must be between 0 and the length of the buffer'
    )


@pytest.mark.parametrize("range", [
    U64Vector2(0, 0),
    U64Vector2(1, 0),
    U64Vector2(4, 0)
])
def test_clear_invalid_range_start_after_end(range: U64Vector2) -> None:
    buffer = Buffer(b'\x00\x01\x02\x03')
    with pytest.raises(ValueError) as excinfo:
        buffer.clear(b'\x00', range=range)
    assert str(excinfo.value) == 'range end must come after start'


@pytest.mark.parametrize("data", [b'\x00', b'\x01'])
@pytest.mark.parametrize("range", [None, U64Vector2(0, 4)])
def test_clear_full(data: bytes, range: U64Vector2) -> None:
    buffer = Buffer(b'\x00\x01\x02\x03')
    buffer.clear(data, range=range)
    assert buffer.bytes == data * 4


@pytest.mark.parametrize("data", [b'\x00', b'\x01'])
@pytest.mark.parametrize("range", [
    U64Vector2(0, 1),
    U64Vector2(1, 2),
    U64Vector2(2, 4),
    U64Vector2(1, 3)
])
def test_clear_range(data: bytes, range: U64Vector2) -> None:
    original_data = b'\x00\x01\x02\x03'
    expected_data = (
        original_data[:range[0]] +
        (data * (range[1] - range[0])) +
        original_data[range[1]:]
    )
    buffer = Buffer(original_data)
    buffer.clear(data, range=range)
    assert buffer.bytes == expected_data


@pytest.mark.parametrize("data_type", VIEW_DATA_TYPES)
def test_view_init(data_type: Any) -> None:
    buffer = Buffer()
    view = BufferView(buffer, data_type)
    assert view.buffer is buffer
    assert view.type is data_type
    assert view.stride == get_size_of(data_type)
    assert view.offset == 0
    assert view.instancing_divisor is None
    assert len(view) == 0


@pytest.mark.parametrize("array, data_type", [
    [FVector2Array(FVector2(-1), FVector2(1)), FVector2],
    [DVector2Array(DVector2(-1), DVector2(1)), DVector2],
    [I8Vector2Array(I8Vector2(-1), I8Vector2(1)), I8Vector2],
    [U8Vector2Array(U8Vector2(0), U8Vector2(1)), U8Vector2],
    [I16Vector2Array(I16Vector2(-1), I16Vector2(1)), I16Vector2],
    [U16Vector2Array(U16Vector2(0), U16Vector2(1)), U16Vector2],
    [I32Vector2Array(I32Vector2(-1), I32Vector2(1)), I32Vector2],
    [U32Vector2Array(U32Vector2(0), U32Vector2(1)), U32Vector2],
    [FVector3Array(FVector3(-1), FVector3(1)), FVector3],
    [DVector3Array(DVector3(-1), DVector3(1)), DVector3],
    [I8Vector3Array(I8Vector3(-1), I8Vector3(1)), I8Vector3],
    [U8Vector3Array(U8Vector3(0), U8Vector3(1)), U8Vector3],
    [I16Vector3Array(I16Vector3(-1), I16Vector3(1)), I16Vector3],
    [U16Vector3Array(U16Vector3(0), U16Vector3(1)), U16Vector3],
    [I32Vector3Array(I32Vector3(-1), I32Vector3(1)), I32Vector3],
    [U32Vector3Array(U32Vector3(0), U32Vector3(1)), U32Vector3],
    [FVector4Array(FVector4(-1), FVector4(1)), FVector4],
    [DVector4Array(DVector4(-1), DVector4(1)), DVector4],
    [I8Vector4Array(I8Vector4(-1), I8Vector4(1)), I8Vector4],
    [U8Vector4Array(U8Vector4(0), U8Vector4(1)), U8Vector4],
    [I16Vector4Array(I16Vector4(-1), I16Vector4(1)), I16Vector4],
    [U16Vector4Array(U16Vector4(0), U16Vector4(1)), U16Vector4],
    [I32Vector4Array(I32Vector4(-1), I32Vector4(1)), I32Vector4],
    [U32Vector4Array(U32Vector4(0), U32Vector4(1)), U32Vector4],
    [FMatrix2x2Array(FMatrix2x2(-1), FMatrix2x2(1)), FMatrix2x2],
    [DMatrix2x2Array(DMatrix2x2(-1), DMatrix2x2(1)), DMatrix2x2],
    [FMatrix2x3Array(FMatrix2x3(-1), FMatrix2x3(1)), FMatrix2x3],
    [DMatrix2x3Array(DMatrix2x3(-1), DMatrix2x3(1)), DMatrix2x3],
    [FMatrix2x4Array(FMatrix2x4(-1), FMatrix2x4(1)), FMatrix2x4],
    [DMatrix2x4Array(DMatrix2x4(-1), DMatrix2x4(1)), DMatrix2x4],
    [FMatrix3x2Array(FMatrix3x2(-1), FMatrix3x2(1)), FMatrix3x2],
    [DMatrix3x2Array(DMatrix3x2(-1), DMatrix3x2(1)), DMatrix3x2],
    [FMatrix3x3Array(FMatrix3x3(-1), FMatrix3x3(1)), FMatrix3x3],
    [DMatrix3x3Array(DMatrix3x3(-1), DMatrix3x3(1)), DMatrix3x3],
    [FMatrix3x4Array(FMatrix3x4(-1), FMatrix3x4(1)), FMatrix3x4],
    [DMatrix3x4Array(DMatrix3x4(-1), DMatrix3x4(1)), DMatrix3x4],
    [FMatrix4x2Array(FMatrix4x2(-1), FMatrix4x2(1)), FMatrix4x2],
    [DMatrix4x2Array(DMatrix4x2(-1), DMatrix4x2(1)), DMatrix4x2],
    [FMatrix4x3Array(FMatrix4x3(-1), FMatrix4x3(1)), FMatrix4x3],
    [DMatrix4x3Array(DMatrix4x3(-1), DMatrix4x3(1)), DMatrix4x3],
    [FMatrix4x4Array(FMatrix4x4(-1), FMatrix4x4(1)), FMatrix4x4],
    [DMatrix4x4Array(DMatrix4x4(-1), DMatrix4x4(1)), DMatrix4x4],
    [FArray(-1, 1), ctypes.c_float],
    [DArray(-1, 1), ctypes.c_double],
    [I8Array(-1, 1), ctypes.c_int8],
    [U8Array(0, 1), ctypes.c_uint8],
    [I16Array(-1, 1), ctypes.c_int16],
    [U16Array(0, 1), ctypes.c_uint16],
    [I32Array(-1, 1), ctypes.c_int32],
    [U32Array(0, 1), ctypes.c_uint32]
])
@pytest.mark.parametrize("instancing_divisor", [None, 1])
def test_view_from_array(
    array: Any,
    data_type: Any,
    instancing_divisor: Any,
) -> None:
    view = BufferView.from_array(array, instancing_divisor=instancing_divisor)
    assert view.buffer.bytes == bytes(array)
    assert view.type is data_type
    assert view.stride == get_size_of(data_type)
    assert view.offset == 0
    assert view.instancing_divisor == instancing_divisor
    assert list(view) == list(array)


@pytest.mark.parametrize("data_type", VIEW_DATA_TYPES)
def test_view_empty_buffer(data_type: Any) -> None:
    view = BufferView(Buffer(), data_type)
    assert len(view) == 0
    assert list(view) == []


@pytest.mark.parametrize("stride", [(1, 2), 'abc'])
def test_view_stride_invalid(stride: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        BufferView(Buffer(), ctypes.c_int8, stride=stride)
    assert str(excinfo.value) == 'stride must be an int'


@pytest.mark.parametrize("stride", [-100, -1, 0])
def test_view_non_positive_stride(stride: int) -> None:
    with pytest.raises(ValueError) as excinfo:
        BufferView(Buffer(), ctypes.c_float, stride=stride)
    assert str(excinfo.value) == 'stride must be greater than 0'


@pytest.mark.parametrize("offset", [(1, 2), 'abc'])
def test_view_offset_invalid(offset: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        BufferView(Buffer(), ctypes.c_int8, offset=offset)
    assert str(excinfo.value) == 'offset must be an int'


@pytest.mark.parametrize("offset", [-100, -1])
def test_view_negative_offset(offset: int) -> None:
    with pytest.raises(ValueError) as excinfo:
        BufferView(Buffer(), ctypes.c_float, offset=offset)
    assert str(excinfo.value) == 'offset must be 0 or greater'


@pytest.mark.parametrize("instancing_divisor", [(1, 2), 'abc'])
def test_view_instancing_divisor_invalid(instancing_divisor: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        BufferView(
            Buffer(),
            ctypes.c_int8,
            instancing_divisor=instancing_divisor
        )
    assert str(excinfo.value) == 'instancing divisor must be an int'


@pytest.mark.parametrize("instancing_divisor", [-100, -1, 0])
def test_view_non_positive_instancing_divisor(instancing_divisor: int) -> None:
    with pytest.raises(ValueError) as excinfo:
        BufferView(
            Buffer(),
            ctypes.c_float,
            instancing_divisor=instancing_divisor
        )
    assert str(excinfo.value) == 'instancing divisor must be greater than 0'


@pytest.mark.parametrize("data_type", VIEW_DATA_TYPES)
@pytest.mark.parametrize("add_stride", [None, 1, 2, 4])
@pytest.mark.parametrize("offset", [0, 1, 2, 4])
@pytest.mark.parametrize("instancing_divisor", [None, 1, 2])
def test_view_read(
    data_type: Any,
    add_stride: Optional[int],
    offset: int,
    instancing_divisor: Optional[int]
) -> None:
    data = bytes(range(200))
    stride = get_size_of(data_type)
    if add_stride is not None:
        stride += add_stride
    expected_length = ((len(data) - offset) // stride)
    expected_python_data: list[Any] = []
    for i in range(expected_length):
        data_start = offset + (stride * i)
        data_bytes = data[data_start:data_start + get_size_of(data_type)]
        try:
            struct_name = CTYPES_TO_STRUCT_NAME[data_type]
            expected_python_data.append(c_unpack(struct_name, data_bytes)[0])
        except KeyError:
            expected_python_data.append(data_type.from_buffer(data_bytes))

    view = BufferView(
        Buffer(data),
        data_type,
        stride=stride,
        offset=offset,
        instancing_divisor=instancing_divisor
    )
    assert len(view) == expected_length
    assert list(view) == expected_python_data


def test_view_map_read_only_mapping() -> None:
    bv_1 = BufferView(Buffer(), ctypes.c_float)
    bv_2 = BufferView(Buffer(), ctypes.c_float)
    map = {
        "vbo_1": bv_1,
        "vbo_2": bv_2,
    }
    bvm = BufferViewMap(map)

    assert len(bvm) == 2
    assert bvm["vbo_1"] is bv_1
    assert bvm["vbo_2"] is bv_2
    with pytest.raises(KeyError):
        bvm["vbo_3"]

    with pytest.raises(TypeError):
        bvm["vbo_1"] = BufferView(Buffer(), ctypes.c_float) # type: ignore

    map.clear()
    assert len(bvm) == 2
    assert bvm["vbo_1"] is bv_1
    assert bvm["vbo_2"] is bv_2


@pytest.mark.parametrize("mapping", [None, 1, [1, 2, 3]])
def test_buffer_view_map_mapping_invalid(mapping: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        BufferViewMap(mapping)
    assert str(excinfo.value) == 'mapping must be a dict'


@pytest.mark.parametrize("key", [None, 1, (1, 2, 3)])
def test_buffer_view_map_key_invalid(key: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        BufferViewMap({key: BufferView(Buffer(), ctypes.c_uint8)})
    assert str(excinfo.value) == f'invalid key {key!r}, expected str'


@pytest.mark.parametrize("value", [None, 1, (1, 2, 3)])
def test_buffer_view_map_value_invalid(value: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        BufferViewMap({"a": value})
    assert str(excinfo.value) == (
        f'invalid value for key {"a"!r}, expected gamut.graphics.BufferView'
    )


@pytest.mark.parametrize("view_map", [None, object(), 'abc'])
def test_use_buffer_view_map_with_shader_view_map_invalid(
    view_map: Any
) -> None:
    shader = Shader(vertex=b'''
    #version 140
    void main()
    {
        gl_Position = vec4(0, 0, 0, 1);
    }
    ''')
    with pytest.raises(TypeError) as excinfo:
        use_buffer_view_map_with_shader(view_map, shader)
    assert str(excinfo.value) == (
        'view_map must be gamut.graphics.BufferViewMap'
    )


@pytest.mark.parametrize("shader", [None, object(), 'abc'])
def test_use_buffer_view_map_with_shader_shader_invalid(
    shader: Any
) -> None:
    with pytest.raises(TypeError) as excinfo:
        use_buffer_view_map_with_shader(BufferViewMap({}), shader)
    assert str(excinfo.value) == 'shader must be a gamut.graphics.Shader'


@pytest.mark.parametrize("view_data_type", VIEW_DATA_TYPES)
@pytest.mark.parametrize("shader_data_type", ['float', 'double', 'int'])
@pytest.mark.parametrize("instancing_divisor", [None, 1])
def test_use_buffer_view_map_with_shader(
    view_data_type: Any,
    shader_data_type: str,
    instancing_divisor: Optional[int],
) -> None:
    _ = Window()
    glsl_version = '140'
    if shader_data_type == 'double':
        glsl_version = '410 core'
        if get_gl_context().version < (4, 1):
            pytest.xfail()

    bvm = BufferViewMap({
        "attr": BufferView(
            Buffer(),
            view_data_type,
            instancing_divisor=instancing_divisor
        )
    })
    shader = Shader(vertex=f"""
    #version {glsl_version}
    in {shader_data_type} attr;
    void main()
    {{
        gl_Position = vec4(attr, 0, 0, 1);
    }}
    """.encode('utf-8'))
    use_buffer_view_map_with_shader(bvm, shader)


def test_buffer_thread_transfer_to_app() -> None:
    buffer: Optional[Buffer] = Buffer(b'123')

    class App(Application):
        async def main(self) -> None:
            nonlocal buffer
            assert buffer is not None
            assert buffer.bytes == b'123'
            buffer = None
            gc.collect()

    app = App()
    app.run()
    assert buffer is None


def test_buffer_view_map_transfer_to_app() -> None:
    bvm: Optional[BufferViewMap] = BufferViewMap({
        "attr": BufferView(Buffer(), ctypes.c_uint8)
    })
    shader = Shader(vertex=f"""
    #version 140
    in float attr;
    void main()
    {{
        gl_Position = vec4(attr, 0, 0, 1);
    }}
    """.encode('utf-8'))
    assert bvm is not None
    use_buffer_view_map_with_shader(bvm, shader)

    class App(Application):
        async def main(self) -> None:
            nonlocal bvm
            bvm = None
            gc.collect()

    app = App()
    app.run()
    assert bvm is None


def test_buffer_thread_transfer_to_main() -> None:
    buffer: Optional[Buffer] = None

    class App(Application):
        async def main(self) -> None:
            nonlocal buffer
            buffer = Buffer(b'123')

    app = App()
    app.run()
    assert buffer is not None
    assert buffer.bytes == b'123'
    buffer = None
    gc.collect()


def test_buffer_view_map_transfer_to_main() -> None:
    bvm: Optional[BufferViewMap] = None

    class App(Application):
        async def main(self) -> None:
            nonlocal bvm
            bvm = BufferViewMap({
                "attr": BufferView(Buffer(), ctypes.c_uint8)
            })
            shader = Shader(vertex=f"""
            #version 140
            in float attr;
            void main()
            {{
                gl_Position = vec4(attr, 0, 0, 1);
            }}
            """.encode('utf-8'))
            use_buffer_view_map_with_shader(bvm, shader)

    app = App()
    app.run()
    assert bvm is not None
    bvm = None
    gc.collect()


def test_buffer_thread_destroyed_outside_render_thread() -> None:
    keep_alive_buffer = Buffer()
    buffer: Optional[Buffer] = Buffer(b'123')

    def thread_main() -> None:
        nonlocal buffer
        buffer = None
        gc.collect()

    thread = threading.Thread(target=thread_main)
    thread.start()
    thread.join()

    assert buffer is None


def test_buffer_view_map_thread_destroyed_outside_render_thread() -> None:
    keep_alive_buffer = Buffer()
    bvm: Optional[BufferViewMap] = BufferViewMap({
        "attr": BufferView(Buffer(), ctypes.c_uint8)
    })
    shader = Shader(vertex=f"""
    #version 140
    in float attr;
    void main()
    {{
        gl_Position = vec4(attr, 0, 0, 1);
    }}
    """.encode('utf-8'))
    assert bvm is not None
    use_buffer_view_map_with_shader(bvm, shader)

    def thread_main() -> None:
        nonlocal bvm
        bvm = None
        gc.collect()

    thread = threading.Thread(target=thread_main)
    thread.start()
    thread.join()

    assert bvm is None
