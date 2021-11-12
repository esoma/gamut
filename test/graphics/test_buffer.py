
# gamut
from gamut import Window
from gamut._glcontext import get_gl_context
from gamut.graphics import (Buffer, BufferFrequency, BufferNature, BufferView,
                            BufferViewMap, Shader)
from gamut.graphics._buffer import use_buffer_view_map_with_shader
# python
from struct import unpack as c_unpack
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


@pytest.mark.parametrize("frequency", list(BufferFrequency))
@pytest.mark.parametrize("nature", list(BufferNature))
def test_frequency_nature_combinations(
    frequency: BufferFrequency,
    nature: BufferNature
) -> None:
    buffer = Buffer(b'', frequency=frequency, nature=nature)
    assert buffer.frequency is frequency
    assert buffer.nature is nature


@pytest.mark.parametrize("data", [
    b'',
    b'\x00\x01\x02\x03\x04',
])
def test_bytes(data: bytes) -> None:
    buffer = Buffer(data)
    assert buffer.bytes == data


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


@pytest.mark.parametrize("stride", [-100, -1, 0])
def test_view_non_positive_stride(stride: int) -> None:
    with pytest.raises(ValueError) as excinfo:
        BufferView(Buffer(), glm.float32, stride=stride)
    assert str(excinfo.value) == 'stride must be greater than 0'


@pytest.mark.parametrize("offset", [-100, -1])
def test_view_negative_offset(offset: int) -> None:
    with pytest.raises(ValueError) as excinfo:
        BufferView(Buffer(), glm.float32, offset=offset)
    assert str(excinfo.value) == 'offset must be 0 or greater'


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
