
# gamut
from gamut import Application, Window
from gamut._glcontext import get_gl_context
from gamut.graphics import (Buffer, BufferFrequency, BufferNature, BufferView,
                            BufferViewMap, Shader)
from gamut.graphics._buffer import use_buffer_view_map_with_shader
# python
import gc
from struct import unpack as c_unpack
import threading
from typing import Any, Final, Optional
# pyglm
import glm
# pytest
import pytest

VIEW_DATA_TYPES: Final = (
    glm.float32, glm.double,
    glm.int8, glm.uint8,
    glm.int16, glm.uint16,
    glm.int32, glm.uint32,
    glm.vec2, glm.dvec2,
    glm.i8vec2, glm.i16vec2, glm.ivec2,
    glm.u8vec2, glm.u16vec2, glm.uvec2,
    glm.vec3, glm.dvec3,
    glm.i8vec3, glm.i16vec3, glm.ivec3,
    glm.u8vec3, glm.u16vec3, glm.uvec3,
    glm.vec4, glm.dvec4,
    glm.i8vec4, glm.i16vec4, glm.ivec4,
    glm.u8vec4, glm.u16vec4, glm.uvec4,
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


def test_empty_buffer() -> None:
    buffer = Buffer()
    assert len(buffer) == 0


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
    assert str(excinfo.value) == 'data must be bytes'


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
        Buffer(None, frequency=frequency)
    assert str(excinfo.value) == 'frequency must be <enum \'BufferFrequency\'>'


@pytest.mark.parametrize("nature", [None, 0, 'abc'])
def test_nature_invalid(nature: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Buffer(None, nature=nature)
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
    assert str(excinfo.value) == 'data must be bytes'


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


@pytest.mark.parametrize("offset, data", [
    (0, b'\x00' * 5),
    (1, b'\x00' * 4),
    (2, b'\x00' * 3),
    (3, b'\x00' * 2),
    (4, b'\x00'),
    (5, b''),
])
def test_replace_invalid_offset_data_combo(offset: int, data: bytes) -> None:
    buffer = Buffer(b'\x00\x01\x02\x03')
    with pytest.raises(ValueError) as excinfo:
        buffer.replace(offset, data)
    assert str(excinfo.value) == (
        'requested offset and data would write beyond the end of the buffer'
    )


@pytest.mark.parametrize("offset, data", [
    (0, b'\x05'),
    (0, b'\x05' * 2),
    (0, b'\x05' * 3),
    (0, b'\x05' * 4),
    (1, b'\x05' * 3),
    (2, b'\x05' * 2),
    (3, b'\x05' * 1),
    (4, b''),
])
def test_replace(offset: int, data: bytes) -> None:
    original_data = b'\x00\x01\x02\x03'
    expected_data = (
        original_data[:offset] +
        data +
        original_data[offset + len(data):]
    )
    buffer = Buffer(original_data)
    buffer.replace(offset, data)
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
    assert str(excinfo.value) == 'range must be a uvec2'


@pytest.mark.parametrize("range", [(0, 5), (5, 6)])
def test_clear_invalid_range_beyond_length(range: tuple[int, int]) -> None:
    buffer = Buffer(b'\x00\x01\x02\x03')
    with pytest.raises(ValueError) as excinfo:
        buffer.clear(b'\x00', range=range)
    assert str(excinfo.value) == (
        'range must be between 0 and the length of the buffer'
    )


@pytest.mark.parametrize("range", [(0, 0), (1, 0), (4, 0)])
def test_clear_invalid_range_start_after_end(range: tuple[int, int]) -> None:
    buffer = Buffer(b'\x00\x01\x02\x03')
    with pytest.raises(ValueError) as excinfo:
        buffer.clear(b'\x00', range=range)
    assert str(excinfo.value) == 'range end must come after start'



@pytest.mark.parametrize("data", [b'\x00', b'\x01'])
@pytest.mark.parametrize("range", [None, (0, 4)])
def test_clear_full(data: bytes, range: tuple[int, int]) -> None:
    buffer = Buffer(b'\x00\x01\x02\x03')
    buffer.clear(data, range=range)
    assert buffer.bytes == data * 4


@pytest.mark.parametrize("data", [b'\x00', b'\x01'])
@pytest.mark.parametrize("range", [(0, 1), (1, 2), (2, 4), (1, 3)])
def test_clear_range(data: bytes, range: tuple[int, int]) -> None:
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
    assert view.stride == glm.sizeof(data_type)
    assert view.offset == 0
    assert view.instancing_divisor is None
    assert len(view) == 0


@pytest.mark.parametrize("data_type", VIEW_DATA_TYPES)
def test_view_empty_buffer(data_type: Any) -> None:
    view = BufferView(Buffer(), data_type)
    assert len(view) == 0
    assert list(view) == []


@pytest.mark.parametrize("stride", [(1, 2), 'abc'])
def test_view_stride_invalid(stride: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        BufferView(Buffer(), glm.int8, stride=stride)
    assert str(excinfo.value) == 'stride must be an int'


@pytest.mark.parametrize("stride", [-100, -1, 0])
def test_view_non_positive_stride(stride: int) -> None:
    with pytest.raises(ValueError) as excinfo:
        BufferView(Buffer(), glm.float32, stride=stride)
    assert str(excinfo.value) == 'stride must be greater than 0'


@pytest.mark.parametrize("offset", [(1, 2), 'abc'])
def test_view_offset_invalid(offset: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        BufferView(Buffer(), glm.int8, offset=offset)
    assert str(excinfo.value) == 'offset must be an int'


@pytest.mark.parametrize("offset", [-100, -1])
def test_view_negative_offset(offset: int) -> None:
    with pytest.raises(ValueError) as excinfo:
        BufferView(Buffer(), glm.float32, offset=offset)
    assert str(excinfo.value) == 'offset must be 0 or greater'


@pytest.mark.parametrize("instancing_divisor", [(1, 2), 'abc'])
def test_view_instancing_divisor_invalid(instancing_divisor: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        BufferView(Buffer(), glm.int8, instancing_divisor=instancing_divisor)
    assert str(excinfo.value) == 'instancing divisor must be an int'


@pytest.mark.parametrize("instancing_divisor", [-100, -1, 0])
def test_view_non_positive_instancing_divisor(instancing_divisor: int) -> None:
    with pytest.raises(ValueError) as excinfo:
        BufferView(
            Buffer(),
            glm.float32,
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
    stride = glm.sizeof(data_type)
    if add_stride is not None:
        stride += add_stride
    expected_length = ((len(data) - offset) // stride)
    expected_python_data: list[Any] = []
    for i in range(expected_length):
        data_start = offset + (stride * i)
        data_bytes = data[data_start:data_start + glm.sizeof(data_type)]
        try:
            struct_name = GLM_POD_TO_STRUCT_NAME[data_type]
            expected_python_data.append(c_unpack(struct_name, data_bytes))
        except KeyError:
            expected_python_data.append(data_type.from_bytes(data_bytes))

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
    bv_1 = BufferView(Buffer(), glm.float32)
    bv_2 = BufferView(Buffer(), glm.float32)
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
        bvm["vbo_1"] = BufferView(Buffer(), glm.float32) # type: ignore

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
        BufferViewMap({key: BufferView(Buffer(), glm.uint8)})
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
        "attr": BufferView(Buffer(), glm.uint8)
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
                "attr": BufferView(Buffer(), glm.uint8)
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
        "attr": BufferView(Buffer(), glm.uint8)
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
