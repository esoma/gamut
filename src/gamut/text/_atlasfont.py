from __future__ import annotations

__all__ = ['AtlasFont', 'AtlasGlyph']

# gamut
from ._break import break_never, BreakMethod
from ._face import (FontSize, PositionedGlyph, RenderedGlyph,
                    RenderedGlyphFormat)
from ._font import Font
# gamut
from gamut.graphics import (Buffer, BufferView, create_quad_position_array,
                            create_quad_uv_array, Pack2d, PrimitiveMode,
                            Texture2d, TextureComponents)
from gamut.math import (DVector2, FMatrix4, FVector2, FVector3, FVector4,
                        FVector4Array, IVector2, UVector2)
# python
# DVector4
from ctypes import c_uint8
from typing import Final, Iterable, Optional, Union
from weakref import ref
# pillow
from PIL import Image as PilImage

GLYPH_FORMAT_TO_PIL_MODE: Final = {
    RenderedGlyphFormat.ALPHA: 'L',
    RenderedGlyphFormat.SDF: 'L',
    RenderedGlyphFormat.LCD: 'RGB',
    RenderedGlyphFormat.LCD_V: 'RGB',
}


GLYPH_FORMAT_TO_TEXTURE_MODE: Final = {
    RenderedGlyphFormat.ALPHA: TextureComponents.R,
    RenderedGlyphFormat.SDF: TextureComponents.R,
    RenderedGlyphFormat.LCD: TextureComponents.RGB,
    RenderedGlyphFormat.LCD_V: TextureComponents.RGB,
}


class AtlasFont(Font):

    def __init__(
        self,
        size: FontSize,
        format: RenderedGlyphFormat,
        *,
        texture_size: UVector2 = UVector2(512, 512),
        padding: int = 1,
    ):
        super().__init__(size)
        self._format = format
        if not isinstance(texture_size, UVector2):
            raise TypeError('texture size must be UVector2')
        self._texture_size = texture_size
        self._padding = padding
        self._glyph_map: dict[int, AtlasGlyph] = {}
        self._textures: list[Texture2d] = []
        self._pack = Pack2d(self._texture_size)
        self._pack_to_glyph: dict[int, int] = {}

    def __getitem__(self, glyph_index: int) -> AtlasGlyph:
        try:
            return self._glyph_map[glyph_index]
        except KeyError:
            try:
                return self._map_glyph(glyph_index)
            except ValueError as ex:
                if (len(ex.args) == 1 and
                    ex.args[0] == 'face does not contain the specified glyph'):
                    raise IndexError(glyph_index)
                raise

    def _update_texture(self, texture_index: int) -> None:
        canvas = PilImage.new(
            GLYPH_FORMAT_TO_PIL_MODE[self._format],
            tuple(self._texture_size),
            color=0
        )
        for pack_index, packed in self._pack.map.items():
            if packed.bin != texture_index:
                continue
            glyph_index = self._pack_to_glyph[pack_index]
            rendered_glyph = self.render_glyph(glyph_index)
            if rendered_glyph.size[0] == 0 or rendered_glyph.size[1] == 0:
                continue
            glyph_canvas = PilImage.frombytes(
                GLYPH_FORMAT_TO_PIL_MODE[self._format],
                tuple(rendered_glyph.size),
                rendered_glyph.data
            )
            canvas.paste(
                glyph_canvas,
                tuple(packed.position + UVector2(self._padding))
            )
        texture = Texture2d(
            self._texture_size,
            GLYPH_FORMAT_TO_TEXTURE_MODE[self._format],
            c_uint8,
            canvas.tobytes()
        )
        try:
            self._textures[texture_index] = texture
        except IndexError:
            assert len(self._textures) == texture_index
            self._textures.append(texture)

    def _map_glyph(self, glyph_index: int) -> AtlasGlyph:
        assert glyph_index not in self._glyph_map
        rendered_glyph = self.render_glyph(glyph_index)
        pack_index = self._pack.add(UVector2(
            rendered_glyph.size[0] + (self._padding * 2),
            rendered_glyph.size[1] + (self._padding * 2)
        ))
        self._pack_to_glyph[pack_index] = glyph_index
        self._pack.pack()
        packed = self._pack.map[pack_index]
        self._update_texture(packed.bin)
        atlas_glyph = AtlasGlyph(
            self,
            IVector2(rendered_glyph.bearing[0], -rendered_glyph.bearing[1]),
            packed.bin,
            UVector2(
                packed.position[0] + self._padding,
                packed.position[1] + self._padding
            ),
            rendered_glyph.size,
            data=rendered_glyph.data
        )
        self._glyph_map[glyph_index] = atlas_glyph
        return atlas_glyph

    def render_glyph(
        self,
        character: Union[str, int],
        *,
        format: Optional[RenderedGlyphFormat] = None
    ) -> RenderedGlyph:
        if format is None:
            format = self._format
        return super().render_glyph(character, format=format)

    def buffer_positioned_glyphs(
        self,
        positioned_glyphs: Iterable[PositionedGlyph],
    ) -> dict[
        Texture2d,
        tuple[BufferView[DVector4], BufferView[DVector2]]
    ]:
        # iterate over all the positioned glyphs once so we can make sure all
        # glyphs have been rendered to the atlas before continuing
        #
        # this should be optimized to do a bulk update, so we're not creating
        # a ton of useless textures
        glyphs = [
            (positioned_glyph, self[positioned_glyph.glyph_index])
            for positioned_glyph in positioned_glyphs
        ]

        texture_buffers: dict[Texture2d, tuple[bytes, bytes]] = {}
        for positioned_glyph, atlas_glyph in glyphs:
            try:
                pos, uvs = texture_buffers[atlas_glyph.texture]
            except KeyError:
                pos = bytearray()
                uvs = bytearray()
                texture_buffers[atlas_glyph.texture] = (pos, uvs)
            # generate the vertex positions
            transform = atlas_glyph.transform_with_position(positioned_glyph)
            glyph_position = create_quad_position_array(
                PrimitiveMode.TRIANGLE,
                left=0, bottom=0,
            )
            pos += FVector4Array(
                *(transform @ p for p in glyph_position)
            )
            # generate the vertex uvs
            top_left_uv, bottom_right_uv = atlas_glyph.uv
            uvs += create_quad_uv_array(
                PrimitiveMode.TRIANGLE,
                left=top_left_uv.x,
                right=bottom_right_uv.x,
                bottom=bottom_right_uv.y,
                top=top_left_uv.y
            )

        return {
            texture: (
                BufferView(Buffer(bytes(pos)), FVector4),
                BufferView(Buffer(bytes(uvs)), FVector2),
            )
            for texture, (pos, uvs) in texture_buffers.items()
        }

    def buffer_text(
        self,
        text: str,
        *,
        break_method: BreakMethod = break_never,
        max_line_size: Optional[int] = None
    ) -> dict[
        Texture2d,
        tuple[BufferView[DVector4], BufferView[DVector2]]
    ]:
        return self.buffer_positioned_glyphs(self.layout_text(
            text,
            break_method=break_method,
            max_line_size=max_line_size,
        ))

    @property
    def format(self) -> RenderedGlyphFormat:
        return self._format

    @property
    def texture_size(self) -> UVector2:
        return self._texture_size

    @property
    def textures(self) -> tuple[Texture2d, ...]:
        return tuple(self._textures)


class AtlasGlyph:

    def __init__(
        self,
        font: AtlasFont,
        bearing: IVector2,
        texture_index: int,
        position: UVector2,
        size: UVector2,
        *,
        data: Optional[bytes] = None,
    ):
        self._font = ref(font)
        if not isinstance(bearing, IVector2):
            raise TypeError('bearing must be IVector2')
        self._bearing = bearing
        self._texture_index = texture_index
        if not isinstance(position, UVector2):
            raise TypeError('position must be UVector2')
        self._position = position
        if not isinstance(size, UVector2):
            raise TypeError('size must be UVector2')
        self._size = size

    def __repr__(self) -> str:
        font = self._font()
        if not font:
            return '<gamut.text.AtlasGlyph (orphaned)>'
        else:
            return (
                f'<gamut.text.AtlasGlyph texture={self.texture} '
                f'position={tuple(self._position)}>'
            )

    @property
    def font(self) -> AtlasFont:
        font = self._font()
        if font is None:
            raise RuntimeError('font no longer exists')
        return font

    @property
    def texture_index(self) -> int:
        return self._texture_index

    @property
    def texture(self) -> Texture2d:
        return self.font._textures[self._texture_index]

    @property
    def bearing(self) -> IVector2:
        return self._bearing

    @property
    def position(self) -> UVector2:
        return self._position

    @property
    def size(self) -> UVector2:
        return self._size

    @property
    def uv(self) -> tuple[DVector2, DVector2]:
        tex_size = DVector2(*self.font.texture_size)
        position = DVector2(*self._position)
        top_left = position / tex_size
        bottom_right = (position + DVector2(*self._size)) / tex_size
        return top_left, bottom_right

    def transform_with_position(self, positioned: PositionedGlyph) -> FMatrix4:
        return FMatrix4(1).translate(
            FVector3(positioned.position[0], -positioned.position[1], 0) -
            FVector3(0, self._size[1], 0) +
            FVector3(self._bearing.x, self._bearing.y, 0)
        ).scale(
            FVector3(self._size.x, self._size.y, 1)
        )
