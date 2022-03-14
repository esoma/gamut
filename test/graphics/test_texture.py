
from __future__ import annotations

__all__ = ['TextureTest']

# gamut
from gamut import Application
from gamut.graphics import (Buffer, MipmapSelection, Texture,
                            TextureComponents, TextureDataType, TextureFilter,
                            TextureType, TextureView, TextureWrap)
from gamut.graphics._texture import (TEXTURE_DATA_TYPES,
                                     TEXTURE_DATA_TYPES_SORTED)
from gamut.math import IVector1, IVector2, IVector3
# python
import ctypes
from ctypes import sizeof as c_sizeof
from math import prod
import struct
import threading
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


TEXTURE_DATA_TYPE_MAX: Final = {
    ctypes.c_uint8: 255,
    ctypes.c_int8: 127,
    ctypes.c_uint16: 65535,
    ctypes.c_int16: 32767,
    ctypes.c_uint32: 4294967295,
    ctypes.c_int32: 2147483647,
    ctypes.c_float: 1.0,
}


TEXTURE_DATA_TYPE_STRUCT: Final = {
    ctypes.c_uint8: 'B',
    ctypes.c_int8: 'b',
    ctypes.c_uint16: 'H',
    ctypes.c_int16: 'h',
    ctypes.c_uint32: 'I',
    ctypes.c_int32: 'i',
    ctypes.c_float: 'f',
}


class TextureTest:

    size_length: int
    wrap_length: int
    data_multiplier: int = 1

    @classmethod
    def create_texture(
        cls,
        size: IVector1 | IVector2 | IVector3,
        components: TextureComponents,
        data_type: type[TextureDataType],
        data: bytes,
        *,
        anisotropy: float | None = None,
        mipmap_selection: MipmapSelection | None = None,
        minify_filter: TextureFilter | None = None,
        magnify_filter: TextureFilter | None = None,
        wrap: tuple[TextureWrap] |
              tuple[TextureWrap, TextureWrap] |
              tuple[TextureWrap, TextureWrap, TextureWrap] |
              None = None,
        wrap_color: F32Vector4 | None = None
    ) -> Texture:
        raise NotImplementedError()

    @pytest.fixture
    def size_type(self) -> Any:
        return {
            1: IVector1,
            2: IVector2,
            3: IVector3
        }[self.size_length]

    @pytest.fixture
    def size(self, size_type) -> Any:
        return size_type(*(1 for _ in range(self.size_length)))

    @pytest.mark.parametrize("size", [None, 0, '1', '12', '123'])
    def test_size_invalid(self, size: Any, size_type: Any) -> None:
        with pytest.raises(TypeError) as excinfo:
            self.create_texture(size, TextureComponents.R, ctypes.c_int8, b'')
        assert str(excinfo.value) == (
            f'size must be {size_type.__name__}'
        )

    @pytest.mark.parametrize("width", [-100, -1, 0])
    def test_width_out_of_range(
        self,
        width: int,
        size: Any,
        size_type: Any
    ) -> None:
        size = list(size)
        size[0] = width
        size = size_type(*size)
        with pytest.raises(ValueError) as excinfo:
            self.create_texture(size, TextureComponents.R, ctypes.c_int8, b'')
        assert str(excinfo.value) == 'width must be > 0'

    @pytest.mark.parametrize("height", [-100, -1, 0])
    def test_height_out_of_range(
        self,
        height: int,
        size: Any,
        size_type: Any
    ) -> None:
        if self.size_length < 2:
            pytest.skip('texture has no height')
        size = list(size)
        size[1] = height
        size = size_type(*size)
        with pytest.raises(ValueError) as excinfo:
            self.create_texture(size, TextureComponents.R, ctypes.c_int8, b'')
        assert str(excinfo.value) == 'height must be > 0'

    @pytest.mark.parametrize("depth", [-100, -1, 0])
    def test_depth_out_of_range(
        self,
        depth: int,
        size: Any,
        size_type: Any
    ) -> None:
        if self.size_length < 3:
            pytest.skip('texture has no depth')
        size = list(size)
        size[2] = depth
        size = size_type(*size)
        with pytest.raises(ValueError) as excinfo:
            self.create_texture(size, TextureComponents.R, ctypes.c_int8, b'')
        assert str(excinfo.value) == 'depth must be > 0'

    @pytest.mark.parametrize("data_type", [None, object(), 'test', 1.0, 1])
    def test_invalid_data_type(self, data_type: Any, size: Any) -> None:
        with pytest.raises(TypeError) as excinfo:
            self.create_texture(size, TextureComponents.R, data_type, b'')
        data_types = ', '.join(sorted((str(t) for t in TEXTURE_DATA_TYPES)))
        assert str(excinfo.value) == f'data_type must be {data_types}'

    @pytest.mark.parametrize("data", [None, object(), 1.0])
    def test_invalid_data(self, data: Any, size: Any) -> None:
        with pytest.raises(TypeError) as excinfo:
            self.create_texture(size, TextureComponents.R, ctypes.c_int8, data)
        assert str(excinfo.value) == (
            f'cannot convert {type(data).__name__!r} object to bytes'
        )

    def test_not_enough_data(self, size: Any) -> None:
        expected_data_length = prod(size)
        data = b'\x00' * (expected_data_length - 1) * self.data_multiplier
        with pytest.raises(ValueError) as excinfo:
            self.create_texture(size, TextureComponents.R, ctypes.c_int8, data)
        assert str(excinfo.value) == 'too much or not enough data'

    def test_too_much_data(self, size: Any) -> None:
        expected_data_length = prod(size)
        data = b'\x00' * (expected_data_length + 1) * self.data_multiplier
        with pytest.raises(ValueError) as excinfo:
            self.create_texture(size, TextureComponents.R, ctypes.c_int8, data)
        assert str(excinfo.value) == 'too much or not enough data'

    @pytest.mark.parametrize("components", [
        c for c in TextureComponents
        if c != TextureComponents.DS
    ])
    @pytest.mark.parametrize("data_type", TEXTURE_DATA_TYPES_SORTED)
    def test_components_data_type_combinations(
        self,
        size: Any,
        components: TextureComponents,
        data_type: type[TextureDataType]
    ) -> None:
        data = (
            b'\x00' *
            TEXTURE_COMPONENTS_COUNT[components] *
            c_sizeof(data_type) *
            self.data_multiplier
        )
        texture = self.create_texture(size, components, data_type, data)
        assert texture.components == components
        assert texture.size == size
        assert texture.is_open

    @pytest.mark.parametrize("mipmap_selection", [1, 'hello', object()])
    def test_mipmap_selection_invalid(
        self,
        size: Any,
        mipmap_selection: Any
    ) -> None:
        with pytest.raises(TypeError) as excinfo:
            self.create_texture(
                size, TextureComponents.R, ctypes.c_int8,
                b'\x00' * self.data_multiplier,
                mipmap_selection=mipmap_selection
            )
        assert str(excinfo.value) == (
            'mipmap_selection must be <enum \'MipmapSelection\'>'
        )

    @pytest.mark.parametrize("minify_filter", [1, 'hello', object()])
    def test_minify_filter_invalid(
        self,
        size: Any,
        minify_filter: Any
    ) -> None:
        with pytest.raises(TypeError) as excinfo:
            self.create_texture(
                size, TextureComponents.R, ctypes.c_int8,
                b'\x00' * self.data_multiplier,
                minify_filter=minify_filter
            )
        assert str(excinfo.value) == (
            'minify_filter must be <enum \'TextureFilter\'>'
        )

    @pytest.mark.parametrize("magnify_filter", [1, 'hello', object()])
    def test_magnify_filter_invalid(
        self,
        size: Any,
        magnify_filter: Any
    ) -> None:
        with pytest.raises(TypeError) as excinfo:
            self.create_texture(
                size, TextureComponents.R, ctypes.c_int8,
                b'\x00' * self.data_multiplier,
                magnify_filter=magnify_filter
            )
        assert str(excinfo.value) == (
            'magnify_filter must be <enum \'TextureFilter\'>'
        )


    @pytest.mark.parametrize("mipmap_selection", list(MipmapSelection))
    @pytest.mark.parametrize("minify_filter", list(TextureFilter))
    @pytest.mark.parametrize("magnify_filter", list(TextureFilter))
    def test_min_mag_mip(
        self,
        size: Any,
        mipmap_selection: MipmapSelection,
        minify_filter: TextureFilter,
        magnify_filter: TextureFilter,
    ) -> None:
        data = b'\x00' * self.data_multiplier
        texture = self.create_texture(
            size,
            TextureComponents.R,
            ctypes.c_uint8,
            data,
            mipmap_selection=mipmap_selection,
            minify_filter=minify_filter,
            magnify_filter=magnify_filter
        )
        assert texture.components == TextureComponents.R
        assert texture.size == size
        assert texture.is_open

    @pytest.mark.parametrize("wrap", [
        0, 1,
        (0, 1, 2, 4),
        tuple(),
    ] + list(TextureWrap))
    def test_wrap_invalid_length(self, size: Any, wrap: Any) -> None:
        with pytest.raises(TypeError) as excinfo:
            self.create_texture(
                size,
                TextureComponents.R,
                ctypes.c_uint8,
                b'\x00' * self.data_multiplier,
                wrap=wrap,
            )
        assert str(excinfo.value) == (
            f'wrap must be {self.wrap_length} {TextureWrap}'
        )

    @pytest.mark.parametrize("wrap_type", [
        0, 'sdf'
    ])
    def test_wrap_invalid_type(self, size: Any, wrap_type: Any) -> None:
        wrap: Any = tuple(wrap_type for _ in range(self.wrap_length))
        with pytest.raises(TypeError) as excinfo:
            self.create_texture(
                size,
                TextureComponents.R,
                ctypes.c_uint8,
                b'\x00' * self.data_multiplier,
                wrap=wrap,
            )
        assert str(excinfo.value) == f'wrap items must be {TextureWrap}'

    @pytest.mark.parametrize("wrap_color", [
        0, 1,
        'ab',
        (1,), (1, 2, 3),
    ])
    def test_wrap_color_invalid(self, size: Any, wrap_color: Any) -> None:
        with pytest.raises(TypeError) as excinfo:
            self.create_texture(
                size,
                TextureComponents.R,
                ctypes.c_uint8,
                b'\x00' * self.data_multiplier,
                wrap_color=wrap_color,
            )
        assert str(excinfo.value) == 'wrap color must be FVector4'

    @pytest.mark.parametrize("wrap_s", list(TextureWrap))
    @pytest.mark.parametrize("wrap_t", list(TextureWrap))
    @pytest.mark.parametrize("wrap_r", list(TextureWrap))
    def test_wrap(
        self,
        size: Any,
        wrap_s: TextureWrap,
        wrap_t: TextureWrap,
        wrap_r: TextureWrap,
    ) -> None:
        data = b'\x00' * self.data_multiplier
        wrap: Any = (wrap_s, wrap_t, wrap_r)[:self.wrap_length]
        texture = self.create_texture(
            size,
            TextureComponents.R,
            ctypes.c_uint8,
            data,
            wrap=wrap,
        )
        assert texture.components == TextureComponents.R
        assert texture.size == size
        assert texture.is_open

    @pytest.mark.parametrize("anisotropy", ['abc', object()])
    def test_anisotropy_invalid(self, size: Any, anisotropy: Any) -> None:
        with pytest.raises(TypeError) as excinfo:
            self.create_texture(
                size,
                TextureComponents.R,
                ctypes.c_int8,
                b'',
                anisotropy=anisotropy
            )
        assert str(excinfo.value) == f'anisotropy must be float'

    @pytest.mark.parametrize("anisotropy", [-1000, 0, 1.0, 1.5, 16, 999999])
    def test_anisotropy_values(self, size: Any, anisotropy: Any) -> None:
        data = b'\x00' * self.data_multiplier
        self.create_texture(
            size,
            TextureComponents.R,
            ctypes.c_int8,
            data,
            anisotropy=anisotropy
        )

    def test_depth_stencil(self, size: Any) -> None:
        data = b'\x00' * c_sizeof(ctypes.c_uint32) * self.data_multiplier
        texture = self.create_texture(
            size,
            TextureComponents.DS,
            ctypes.c_uint32,
            data
        )
        assert texture.components == TextureComponents.DS
        assert texture.size == size
        assert texture.is_open

    @pytest.mark.parametrize("data_type", [
        dt for dt in TEXTURE_DATA_TYPES_SORTED
        if dt != ctypes.c_uint32
    ])
    def test_depth_stencil_invalid_data_types(
        self,
        size: Any,
        data_type: type[TextureDataType]
    ) -> None:
        data = b'\x00' * c_sizeof(data_type) * self.data_multiplier
        with pytest.raises(ValueError) as excinfo:
            self.create_texture(
                size,
                TextureComponents.DS,
                data_type,
                data
            )
        assert str(excinfo.value) == (
            f'data_type must be {ctypes.c_uint32} when components is '
            f'{TextureComponents.DS}'
        )

    def test_close(self, size: Any) -> None:
        texture = self.create_texture(
            size,
            TextureComponents.R,
            ctypes.c_int8,
            b'\x00' * self.data_multiplier
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
        self,
        size: Any,
        components: TextureComponents,
        input_data_type: type[TextureDataType],
        output_data_type: type[TextureDataType],
        size_type: Any
    ) -> None:
        size = size_type(*(c * 2 for c in size))
        pixel_count = prod(size) * self.data_multiplier
        pixels = [i / pixel_count for i in range(pixel_count)]

        component_count = TEXTURE_COMPONENTS_COUNT[components] * pixel_count
        input_max = TEXTURE_DATA_TYPE_MAX[input_data_type]
        input_data = struct.pack(
            '=' + TEXTURE_DATA_TYPE_STRUCT[input_data_type] * component_count,
            *(input_max.__class__(p * input_max)
              for p in pixels
              for i in range(TEXTURE_COMPONENTS_COUNT[components])
            )
        )

        expected_output = [
            p
            for p in pixels
            for i in range(TEXTURE_COMPONENTS_COUNT[components])
        ]

        texture = self.create_texture(
            size,
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
                '=' +
                TEXTURE_DATA_TYPE_STRUCT[output_data_type] * component_count,
                view.bytes
            )
        ]
        assert len(output) == len(expected_output)
        assert all(
            o == pytest.approx(e, abs=.025)
            for o, e in zip(output, expected_output)
        )

    @pytest.mark.parametrize("output_data_type", [
        dt for dt in TEXTURE_DATA_TYPES_SORTED
        if dt != ctypes.c_uint32
    ])
    def test_texture_view_depth_stencil_invalid_output_data_type(
        self,
        size: Any,
        output_data_type: type[TextureDataType],
        size_type: Any
    ) -> None:
        components = TextureComponents.DS
        input_data_type = ctypes.c_uint32
        size = size_type(*(c * 2 for c in size))
        pixel_count = prod(size) * self.data_multiplier
        pixels = [i / pixel_count for i in range(pixel_count)]

        component_count = TEXTURE_COMPONENTS_COUNT[components] * pixel_count
        input_max = TEXTURE_DATA_TYPE_MAX[input_data_type]
        input_data = struct.pack(
            '=' + TEXTURE_DATA_TYPE_STRUCT[input_data_type] * component_count,
            *(int(p * input_max)
              for p in pixels
              for i in range(TEXTURE_COMPONENTS_COUNT[components])
            )
        )

        texture = self.create_texture(
            size,
            components,
            input_data_type,
            input_data
        )

        with pytest.raises(ValueError) as excinfo:
            TextureView(texture, output_data_type)
        assert str(excinfo.value) == (
            f'data_type must be {ctypes.c_uint32} when components is '
            f'{TextureComponents.DS}'
        )

    def test_create_texture_view_texture_closed(self, size: Any) -> None:
        texture = self.create_texture(
            size,
            TextureComponents.R,
            ctypes.c_int8,
            b'\x00' * self.data_multiplier
        )
        texture.close()
        with pytest.raises(RuntimeError) as excinfo:
            TextureView(texture, ctypes.c_int8)
        assert str(excinfo.value) == 'texture is closed'


    def test_texture_view_texture_closed(self, size: Any) -> None:
        texture = self.create_texture(
            size,
            TextureComponents.R,
            ctypes.c_int8,
            b'\x00' * self.data_multiplier
        )
        view = TextureView(texture, ctypes.c_int8)

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
    def test_texture_view_non_texture(self, texture: Any) -> None:
        with pytest.raises(TypeError) as excinfo:
            TextureView(texture, ctypes.c_int8)
        assert str(excinfo.value) == (
            'texture must be <class \'gamut.graphics._texture.Texture\'>'
        )

    @pytest.mark.parametrize("data_type", [None, object(), 'test', 1.0])
    def test_texture_view_non_data_type(
        self,
        size: Any,
        data_type: Any
    ) -> None:
        texture = self.create_texture(
            size,
            TextureComponents.R,
            ctypes.c_int8,
            b'\x00' * self.data_multiplier
        )
        with pytest.raises(TypeError) as excinfo:
            TextureView(texture, data_type)
        data_types = ", ".join(sorted((str(t) for t in TEXTURE_DATA_TYPES)))
        assert str(excinfo.value) == f'data_type must be {data_types}'

    def test_texture_view_close(self, size: Any) -> None:
        texture = self.create_texture(
            size,
            TextureComponents.R,
            ctypes.c_int8,
            b'\x00' * self.data_multiplier
        )
        view = TextureView(texture, ctypes.c_int8)
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

    def test_thread_transfer_to_app(self, size: Any) -> None:
        texture = self.create_texture(
            size,
            TextureComponents.DS,
            ctypes.c_uint32,
            b'\x00' * c_sizeof(ctypes.c_uint32) * self.data_multiplier
        )

        class App(Application):
            async def main(self) -> None:
                texture.close()

        app = App()
        app.run()
        assert not texture.is_open

    def test_thread_transfer_to_main(self, size: Any) -> None:
        texture: Texture | None = None

        class App(Application):
            async def main(self_) -> None:
                nonlocal texture
                texture = self.create_texture(
                    size,
                    TextureComponents.DS,
                    ctypes.c_uint32,
                    b'\x00' * c_sizeof(ctypes.c_uint32) * self.data_multiplier
                )

        app = App()
        app.run()
        assert texture is not None
        assert texture.is_open
        texture.close()
        assert not texture.is_open

    def test_thread_closed_outside_render_thread(self, size: Any) -> None:
        keep_alive_buffer = Buffer()
        texture = self.create_texture(
            size,
            TextureComponents.DS,
            ctypes.c_uint32,
            b'\x00' * c_sizeof(ctypes.c_uint32) * self.data_multiplier
        )

        def thread_main() -> None:
            texture.close()

        thread = threading.Thread(target=thread_main)
        thread.start()
        thread.join()

        assert not texture.is_open


class TextureTestType(TextureTest):

    texture_type: TextureType

    @classmethod
    def create_texture(
        cls,
        size: IVector1 | IVector2 | IVector3,
        components: TextureComponents,
        data_type: type[TextureDataType],
        data: bytes,
        *,
        anisotropy: float | None = None,
        mipmap_selection: MipmapSelection | None = None,
        minify_filter: TextureFilter | None = None,
        magnify_filter: TextureFilter | None = None,
        wrap: tuple[TextureWrap] |
              tuple[TextureWrap, TextureWrap] |
              tuple[TextureWrap, TextureWrap, TextureWrap] |
              None = None,
        wrap_color: F32Vector4 | None = None
    ) -> Texture:
        return Texture(
            cls.texture_type,
            size=size,
            components=components,
            data_type=data_type,
            data=data,
            anisotropy=anisotropy,
            mipmap_selection=mipmap_selection,
            minify_filter=minify_filter,
            magnify_filter=magnify_filter,
            wrap=wrap,
            wrap_color=wrap_color
        )


class TestTextureTypeNormal2d(TextureTestType):
    texture_type = TextureType.NORMAL_2D
    size_length = 2
    wrap_length = 2


class TestTextureTypeArray2d(TextureTestType):
    texture_type = TextureType.ARRAY_2D
    size_length = 3
    wrap_length = 2


class TestTextureTypeNormalCube(TextureTestType):
    texture_type = TextureType.NORMAL_CUBE
    size_length = 2
    wrap_length = 3
    data_multiplier = 6
