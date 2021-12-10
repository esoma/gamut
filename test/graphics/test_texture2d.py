
# gamut
from gamut import Application
from gamut.graphics import (Buffer, MipmapSelection, Texture2d,
                            TextureComponents, TextureDataType, TextureFilter,
                            TextureView, TextureWrap)
from gamut.graphics._texture import (TEXTURE_DATA_TYPES,
                                     TEXTURE_DATA_TYPES_SORTED)
# python
from ctypes import sizeof as c_sizeof
import struct
import threading
from typing import Any, Final, Optional
# pyglm
import glm
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


TEXTURE_DATA_TYPE_MAX: Final = {
    glm.uint8: 255,
    glm.int8: 127,
    glm.uint16: 65535,
    glm.int16: 32767,
    glm.uint32: 4294967295,
    glm.int32: 2147483647,
    glm.float32: 1.0,
}


TEXTURE_DATA_TYPE_STRUCT: Final = {
    glm.uint8: 'B',
    glm.int8: 'b',
    glm.uint16: 'H',
    glm.int16: 'h',
    glm.uint32: 'I',
    glm.int32: 'i',
    glm.float32: 'f',
}


@pytest.mark.parametrize("size", [None, 0, (1,), (1, 2, 3)])
def test_size_invalid(size: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Texture2d(size, TextureComponents.R, glm.int8, b'')
    assert str(excinfo.value) == 'size must be a sequence of 2 integers'


@pytest.mark.parametrize("width", [-100, -1, 0])
def test_width_out_of_range(width: int) -> None:
    with pytest.raises(ValueError) as excinfo:
        Texture2d((width, 1), TextureComponents.R, glm.int8, b'')
    assert str(excinfo.value) == 'width must be > 0'


@pytest.mark.parametrize("height", [-100, -1, 0])
def test_height_out_of_range(height: int) -> None:
    with pytest.raises(ValueError) as excinfo:
        Texture2d((1, height), TextureComponents.R, glm.int8, b'')
    assert str(excinfo.value) == 'height must be > 0'


@pytest.mark.parametrize("components", [None, object(), 'test', 1.0, 1])
def test_invalid_components(components: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Texture2d((1, 1), components, glm.int8, b'')
    assert str(excinfo.value) == (
        'components must be <enum \'TextureComponents\'>'
    )


@pytest.mark.parametrize("data_type", [None, object(), 'test', 1.0, 1])
def test_invalid_data_type(data_type: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Texture2d((1, 1), TextureComponents.R, data_type, b'')
    data_types = ', '.join(sorted((str(t) for t in TEXTURE_DATA_TYPES)))
    assert str(excinfo.value) == f'data_type must be {data_types}'


@pytest.mark.parametrize("data", [None, object(), 1.0])
def test_invalid_data(data: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Texture2d((1, 1), TextureComponents.R, glm.int8, data)
    assert str(excinfo.value) == (
        f'cannot convert {type(data).__name__!r} object to bytes'
    )


@pytest.mark.parametrize("data", [b'', b'\x00\x00'])
def test_too_much_or_not_enough_data(data: bytes) -> None:
    with pytest.raises(ValueError) as excinfo:
        Texture2d((1, 1), TextureComponents.R, glm.int8, data)
    assert str(excinfo.value) == 'too much or not enough data'


@pytest.mark.parametrize("components", [
    c for c in TextureComponents
    if c != TextureComponents.DS
])
@pytest.mark.parametrize("data_type", TEXTURE_DATA_TYPES_SORTED)
def test_components_data_type_combinations(
    components: TextureComponents,
    data_type: type[TextureDataType]
) -> None:
    data = (
        b'\x00' *
        TEXTURE_COMPONENTS_COUNT[components] *
        c_sizeof(data_type)
    )
    texture = Texture2d((1, 1), components, data_type, data)
    assert texture.components == components
    assert texture.size == (1, 1)
    assert texture.is_open


@pytest.mark.parametrize("mipmap_selection", [1, 'hello', object()])
def test_mipmap_selection_invalid(mipmap_selection: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Texture2d(
            (1, 1), TextureComponents.R, glm.int8, b'\x00',
            mipmap_selection=mipmap_selection
        )
    assert str(excinfo.value) == (
        'mipmap_selection must be <enum \'MipmapSelection\'>'
    )


@pytest.mark.parametrize("minify_filter", [1, 'hello', object()])
def test_minify_filter_invalid(minify_filter: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Texture2d(
            (1, 1), TextureComponents.R, glm.int8, b'\x00',
            minify_filter=minify_filter
        )
    assert str(excinfo.value) == (
        'minify_filter must be <enum \'TextureFilter\'>'
    )


@pytest.mark.parametrize("magnify_filter", [1, 'hello', object()])
def test_magnify_filter_invalid(magnify_filter: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Texture2d(
            (1, 1), TextureComponents.R, glm.int8, b'\x00',
            magnify_filter=magnify_filter
        )
    assert str(excinfo.value) == (
        'magnify_filter must be <enum \'TextureFilter\'>'
    )


@pytest.mark.parametrize("mipmap_selection", list(MipmapSelection))
@pytest.mark.parametrize("minify_filter", list(TextureFilter))
@pytest.mark.parametrize("magnify_filter", list(TextureFilter))
def test_min_mag_mip(
    mipmap_selection: MipmapSelection,
    minify_filter: TextureFilter,
    magnify_filter: TextureFilter,
) -> None:
    data = b'\x00'
    texture = Texture2d(
        (1, 1),
        TextureComponents.R,
        glm.uint8,
        data,
        mipmap_selection=mipmap_selection,
        minify_filter=minify_filter,
        magnify_filter=magnify_filter
    )
    assert texture.components == TextureComponents.R
    assert texture.size == (1, 1)
    assert texture.is_open


@pytest.mark.parametrize("wrap", [
    0, 1,
    (0, 1, 2),
    (0,)
] + list(TextureWrap))
def test_wrap_invalid_length(wrap: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        texture = Texture2d(
            (1, 1),
            TextureComponents.R,
            glm.uint8,
            b'\x00',
            wrap=wrap,
        )
    assert str(excinfo.value) == f'wrap must be 2 {TextureWrap}'


@pytest.mark.parametrize("wrap", [
    (0, 1),
    ('asd', 'bsdfsd')
])
def test_wrap_invalid_type(wrap: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        texture = Texture2d(
            (1, 1),
            TextureComponents.R,
            glm.uint8,
            b'\x00',
            wrap=wrap,
        )
    assert str(excinfo.value) == f'wrap items must be {TextureWrap}'


@pytest.mark.parametrize("wrap_color", [
    0, 1,
    'ab',
    (1,), (1, 2, 3),
])
def test_wrap_color_invalid(wrap_color: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        texture = Texture2d(
            (1, 1),
            TextureComponents.R,
            glm.uint8,
            b'\x00',
            wrap_color=wrap_color,
        )
    assert str(excinfo.value) == 'wrap_color must be a sequence of four floats'


@pytest.mark.parametrize("wrap_s", list(TextureWrap))
@pytest.mark.parametrize("wrap_t", list(TextureWrap))
def test_wrap(wrap_s: TextureWrap, wrap_t: TextureWrap) -> None:
    data = b'\x00'
    texture = Texture2d(
        (1, 1),
        TextureComponents.R,
        glm.uint8,
        data,
        wrap=(wrap_s, wrap_t),
    )
    assert texture.components == TextureComponents.R
    assert texture.size == (1, 1)
    assert texture.is_open


def test_depth_stencil() -> None:
    data = b'\x00' * c_sizeof(glm.uint32)
    texture = Texture2d(
        (1, 1),
        TextureComponents.DS,
        glm.uint32,
        data
    )
    assert texture.components == TextureComponents.DS
    assert texture.size == (1, 1)
    assert texture.is_open


@pytest.mark.parametrize("data_type", [
    dt for dt in TEXTURE_DATA_TYPES_SORTED
    if dt != glm.uint32
])
def test_depth_stencil_invalid_data_types(
    data_type: type[TextureDataType]
) -> None:
    data = b'\x00' * c_sizeof(data_type)
    with pytest.raises(ValueError) as excinfo:
        texture = Texture2d(
            (1, 1),
            TextureComponents.DS,
            data_type,
            data
        )
    assert str(excinfo.value) == (
        f'data_type must be {glm.uint32} when components is '
        f'{TextureComponents.DS}'
    )


def test_close() -> None:
    texture = Texture2d(
        (1, 1),
        TextureComponents.R,
        glm.int8,
        b'\x00'
    )
    assert texture.is_open

    texture.close()
    assert not texture.is_open


@pytest.mark.parametrize("components", [
    c for c in TextureComponents
    if c != TextureComponents.DS
])
@pytest.mark.parametrize("input_data_type", TEXTURE_DATA_TYPES_SORTED)
@pytest.mark.parametrize("output_data_type", TEXTURE_DATA_TYPES_SORTED)
def test_texture_view(
    components: TextureComponents,
    input_data_type: type[TextureDataType],
    output_data_type: type[TextureDataType],
) -> None:
    pixels = [0.25, 0.5, 0.0, 1.0]
    width = 2
    height = 2

    component_count = TEXTURE_COMPONENTS_COUNT[components] * width * height
    input_max = TEXTURE_DATA_TYPE_MAX[input_data_type]
    input_data = struct.pack(
        TEXTURE_DATA_TYPE_STRUCT[input_data_type] * component_count,
        *(int(p * input_max)
          for p in pixels
          for i in range(TEXTURE_COMPONENTS_COUNT[components])
        )
    )

    expected_output = [
        p
        for p in pixels
        for i in range(TEXTURE_COMPONENTS_COUNT[components])
    ]

    texture = Texture2d(
        (width, height),
        components,
        input_data_type,
        input_data
    )
    view = TextureView(texture, output_data_type)
    assert view.texture is texture
    assert len(view) == (
        len(expected_output) *
        c_sizeof(output_data_type)
    )

    output_max = TEXTURE_DATA_TYPE_MAX[output_data_type]
    output = [
        c / output_max
        for c in
        struct.unpack(
            TEXTURE_DATA_TYPE_STRUCT[output_data_type] * component_count,
            view.bytes
        )
    ]
    assert len(output) == len(expected_output)
    assert all(
        pytest.approx(o, e)
        for o, e in zip(output, expected_output)
    )


def test_texture_view_depth_stencil() -> None:
    components = TextureComponents.DS
    input_data_type = glm.uint32
    output_data_type = glm.uint32
    pixels = [0.25, 0.5, 0.0, 1.0]
    width = 2
    height = 2

    component_count = TEXTURE_COMPONENTS_COUNT[components] * width * height
    input_max = TEXTURE_DATA_TYPE_MAX[input_data_type]
    input_data = struct.pack(
        TEXTURE_DATA_TYPE_STRUCT[input_data_type] * component_count,
        *(int(p * input_max)
          for p in pixels
          for i in range(TEXTURE_COMPONENTS_COUNT[components])
        )
    )

    expected_output = [
        p
        for p in pixels
        for i in range(TEXTURE_COMPONENTS_COUNT[components])
    ]

    texture = Texture2d((
        width, height),
        components,
        input_data_type,
        input_data
    )
    view = TextureView(texture, output_data_type)
    assert view.texture is texture
    assert len(view) == (
        len(expected_output) *
        c_sizeof(output_data_type)
    )

    output_max = TEXTURE_DATA_TYPE_MAX[output_data_type]
    output = [
        c / output_max
        for c in
        struct.unpack(
            TEXTURE_DATA_TYPE_STRUCT[output_data_type] * component_count,
            view.bytes
        )
    ]
    assert len(output) == len(expected_output)
    assert all(
        pytest.approx(o, e)
        for o, e in zip(output, expected_output)
    )


@pytest.mark.parametrize("output_data_type", [
    dt for dt in TEXTURE_DATA_TYPES_SORTED
    if dt != glm.uint32
])
def test_texture_view_depth_stencil_invalid_output_data_type(
    output_data_type: type[TextureDataType]
) -> None:
    components = TextureComponents.DS
    input_data_type = glm.uint32
    pixels = [0.25, 0.5, 0.0, 1.0]
    width = 2
    height = 2

    component_count = TEXTURE_COMPONENTS_COUNT[components] * width * height
    input_max = TEXTURE_DATA_TYPE_MAX[input_data_type]
    input_data = struct.pack(
        TEXTURE_DATA_TYPE_STRUCT[input_data_type] * component_count,
        *(int(p * input_max)
          for p in pixels
          for i in range(TEXTURE_COMPONENTS_COUNT[components])
        )
    )

    texture = Texture2d(
        (width, height),
        components,
        input_data_type,
        input_data
    )

    with pytest.raises(ValueError) as excinfo:
        TextureView(texture, output_data_type)
    assert str(excinfo.value) == (
        f'data_type must be {glm.uint32} when components is '
        f'{TextureComponents.DS}'
    )


def test_create_texture_view_texture_closed() -> None:
    texture = Texture2d(
        (1, 1),
        TextureComponents.R,
        glm.int8,
        b'\x00'
    )
    texture.close()
    with pytest.raises(RuntimeError) as excinfo:
        TextureView(texture, glm.int8)
    assert str(excinfo.value) == 'texture is closed'


def test_texture_view_texture_closed() -> None:
    texture = Texture2d(
        (1, 1),
        TextureComponents.R,
        glm.int8,
        b'\x00'
    )
    view = TextureView(texture, glm.int8)

    texture.close()
    assert view.is_open
    assert view.texture is texture

    with pytest.raises(RuntimeError) as excinfo:
        len(view)
    assert str(excinfo.value) == 'texture is closed'

    with pytest.raises(RuntimeError) as excinfo:
        view.bytes
    assert str(excinfo.value) == 'texture is closed'


@pytest.mark.parametrize("texture", [None, object(), 'test', 1.0])
def test_texture_view_non_texture(texture: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        TextureView(texture, glm.int8)
    assert str(excinfo.value) == (
        'texture must be <class \'gamut.graphics.Texture2d\'>'
    )


@pytest.mark.parametrize("data_type", [None, object(), 'test', 1.0])
def test_texture_view_non_data_type(data_type: Any) -> None:
    texture = Texture2d(
        (1, 1),
        TextureComponents.R,
        glm.int8,
        b'\x00'
    )
    with pytest.raises(TypeError) as excinfo:
        TextureView(texture, data_type)
    data_types = ", ".join(sorted((str(t) for t in TEXTURE_DATA_TYPES)))
    assert str(excinfo.value) == f'data_type must be {data_types}'


def test_texture_view_close() -> None:
    texture = Texture2d(
        (1, 1),
        TextureComponents.R,
        glm.int8,
        b'\x00'
    )
    view = TextureView(texture, glm.int8)
    assert view.is_open

    view.close()
    assert not view.is_open

    with pytest.raises(RuntimeError) as excinfo:
        view.texture
    assert str(excinfo.value) == 'texture view is closed'

    with pytest.raises(RuntimeError) as excinfo:
        len(view)
    assert str(excinfo.value) == 'texture view is closed'

    with pytest.raises(RuntimeError) as excinfo:
        view.bytes
    assert str(excinfo.value) == 'texture view is closed'


def test_texture2d_thread_transfer_to_app() -> None:
    texture = Texture2d(
        (1, 1),
        TextureComponents.DS,
        glm.uint32,
        b'\x00' * c_sizeof(glm.uint32)
    )

    class App(Application):
        async def main(self) -> None:
            texture.close()

    app = App()
    app.run()
    assert not texture.is_open


def test_texture2d_thread_transfer_to_main() -> None:
    texture: Optional[Texture2d] = None

    class App(Application):
        async def main(self) -> None:
            nonlocal texture
            texture = Texture2d(
                (1, 1),
                TextureComponents.DS,
                glm.uint32,
                b'\x00' * c_sizeof(glm.uint32)
            )

    app = App()
    app.run()
    assert texture is not None
    assert texture.is_open
    texture.close()
    assert not texture.is_open


def test_texture2d_thread_closed_outside_render_thread() -> None:
    keep_alive_buffer = Buffer()
    texture = Texture2d(
        (1, 1),
        TextureComponents.DS,
        glm.uint32,
        b'\x00' * c_sizeof(glm.uint32)
    )

    def thread_main() -> None:
        texture.close()

    thread = threading.Thread(target=thread_main)
    thread.start()
    thread.join()

    assert not texture.is_open
