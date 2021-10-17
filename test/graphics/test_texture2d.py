
# gamut
from gamut.graphics import Texture2d, TextureComponents, TextureDataType
# python
from ctypes import c_byte, c_float, c_int, c_short, c_ubyte, c_uint, c_ushort
from ctypes import sizeof as c_sizeof
from typing import Any, Final
# pytest
import pytest

TEXTURE_COMPONENTS_COUNT: Final = {
    TextureComponents.R: 1,
    TextureComponents.RG: 2,
    TextureComponents.RGB: 3,
    TextureComponents.RGBA: 4,
    TextureComponents.D: 1,
    TextureComponents.DS: 1
}


TEXTURE_DATA_TYPE_SIZE: Final = {
    TextureDataType.UNSIGNED_BYTE: c_sizeof(c_ubyte),
    TextureDataType.BYTE: c_sizeof(c_byte),
    TextureDataType.UNSIGNED_SHORT: c_sizeof(c_ushort),
    TextureDataType.SHORT: c_sizeof(c_short),
    TextureDataType.UNSIGNED_INT: c_sizeof(c_uint),
    TextureDataType.INT: c_sizeof(c_int),
    TextureDataType.FLOAT: c_sizeof(c_float),
}


@pytest.mark.parametrize("width", [-100, -1, 0])
def test_width_out_of_range(width: int) -> None:
    with pytest.raises(ValueError) as excinfo:
        Texture2d(width, 1, TextureComponents.R, TextureDataType.BYTE, b'')
    assert str(excinfo.value) == 'width must be > 0'


@pytest.mark.parametrize("width", [None, object(), 'test', 1.0])
def test_width_invalid(width: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Texture2d(width, 1, TextureComponents.R, TextureDataType.BYTE, b'')
    assert str(excinfo.value) == 'width must be an int'


@pytest.mark.parametrize("height", [-100, -1, 0])
def test_height_out_of_range(height: int) -> None:
    with pytest.raises(ValueError) as excinfo:
        Texture2d(1, height, TextureComponents.R, TextureDataType.BYTE, b'')
    assert str(excinfo.value) == 'height must be > 0'


@pytest.mark.parametrize("height", [None, object(), 'test', 1.0])
def test_height_invalid(height: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Texture2d(1, height, TextureComponents.R, TextureDataType.BYTE, b'')
    assert str(excinfo.value) == 'height must be an int'


@pytest.mark.parametrize("components", [None, object(), 'test', 1.0, 1])
def test_invalid_components(components: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Texture2d(1, 1, components, TextureDataType.BYTE, b'')
    assert str(excinfo.value) == (
        'components must be <enum \'TextureComponents\'>'
    )


@pytest.mark.parametrize("data_type", [None, object(), 'test', 1.0, 1])
def test_invalid_data_type(data_type: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Texture2d(1, 1, TextureComponents.R, data_type, b'')
    assert str(excinfo.value) == (
        'data_type must be <enum \'TextureDataType\'>'
    )


@pytest.mark.parametrize("data", [None, object(), 'test', 1.0, 1])
def test_invalid_data(data: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Texture2d(1, 1, TextureComponents.R, TextureDataType.BYTE, data)
    assert str(excinfo.value) == 'data must be bytes'


@pytest.mark.parametrize("data", [b'', b'\x00\x00'])
def test_too_much_or_not_enough_data(data: bytes) -> None:
    with pytest.raises(ValueError) as excinfo:
        Texture2d(1, 1, TextureComponents.R, TextureDataType.BYTE, data)
    assert str(excinfo.value) == 'too much or not enough data'


@pytest.mark.parametrize("components", [
    c for c in TextureComponents
    if c != TextureComponents.DS
])
@pytest.mark.parametrize("data_type", list(TextureDataType))
def test_components_data_type_combinations(
    components: TextureComponents,
    data_type: TextureDataType
) -> None:
    data = (
        b'\x00' *
        TEXTURE_COMPONENTS_COUNT[components] *
        TEXTURE_DATA_TYPE_SIZE[data_type]
    )
    texture = Texture2d(1, 1, components, data_type, data)
    assert texture.components == components
    assert texture.size == (1, 1)
    assert texture.is_open

def test_depth_stencil() -> None:
    data = b'\x00' * TEXTURE_DATA_TYPE_SIZE[TextureDataType.UNSIGNED_INT]
    texture = Texture2d(
        1, 1,
        TextureComponents.DS,
        TextureDataType.UNSIGNED_INT,
        data
    )
    assert texture.components == TextureComponents.DS
    assert texture.size == (1, 1)
    assert texture.is_open


@pytest.mark.parametrize("data_type", [
    dt for dt in TextureDataType
    if dt != TextureDataType.UNSIGNED_INT
])
def test_depth_stencil_invalid_data_types(data_type: TextureDataType) -> None:
    data = b'\x00' * TEXTURE_DATA_TYPE_SIZE[data_type]
    with pytest.raises(ValueError) as excinfo:
        texture = Texture2d(
            1, 1,
            TextureComponents.DS,
            data_type,
            data
        )
    assert str(excinfo.value) == (
        f'data_type must be {TextureDataType.UNSIGNED_INT} when components is '
        f'{TextureComponents.DS}'
    )


def test_close() -> None:
    texture = Texture2d(
        1, 1,
        TextureComponents.R,
        TextureDataType.BYTE,
        b'\x00'
    )
    assert texture.is_open

    texture.close()
    assert not texture.is_open
