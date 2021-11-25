

from __future__ import annotations

__all__ = ['AtlasFont', 'AtlasGlyph']


# gamut
from ._face import FontSize, RenderedGlyph, RenderedGlyphFormat
from ._font import Font
# gamut
from gamut.graphics import Pack2d, Texture2d, TextureComponents
# python
from typing import Final, Optional, Union
from weakref import ref
from PIL import Image as PilImage
from PIL.ImageOps import flip as pil_flip
# pyglm
from glm import ivec2, uint8, vec2

GLYPH_FORMAT_TO_PIL_MODE: Final = {
    RenderedGlyphFormat.ALPHA: 'L',
    RenderedGlyphFormat.SDF: 'L',
    RenderedGlyphFormat.LCD: 'RGB',
    RenderedGlyphFormat.LCD_V: 'RGB',
}


class AtlasFont(Font):

    def __init__(
        self,
        size: FontSize,
        format: RenderedGlyphFormat,
        *,
        texture_size: tuple[int, int] = (256, 256),
        padding: int = 1,
    ):
        super().__init__(size)
        self._format = format
        self._texture_size = texture_size
        self._padding = padding
        self._glyph_map: dict[int, AtlasGlyph] = {}
        self._textures: list[Texture2d] = []
        self._pack = Pack2d(texture_size)
        self._pack_to_glyph: dict[int, int] = {}

    def __getitem__(self, glyph_index: int) -> AtlasGlyph:
        try:
            return self._glyph_map[glyph_index]
        except KeyError:
            return self._map_glyph(glyph_index)

    def _update_texture(self, texture_index: int) -> None:
        canvas = PilImage.new('L', self._texture_size, color=0)
        for pack_index, packed in self._pack.map.items():
            if packed.bin != texture_index:
                continue
            glyph_index = self._pack_to_glyph[pack_index]
            rendered_glyph = self.render_glyph(glyph_index)
            glyph_canvas = PilImage.frombytes(
                'L',
                rendered_glyph.size,
                rendered_glyph.data
            )
            canvas.paste(
                glyph_canvas,
                tuple(packed.position + ivec2(self._padding, self._padding))
            )
        texture = Texture2d(
            *self._texture_size,
            TextureComponents.R,
            uint8,
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
        pack_index = self._pack.add((
            rendered_glyph.size[0] + (self._padding * 2),
            rendered_glyph.size[1] + (self._padding * 2)
        ))
        self._pack_to_glyph[pack_index] = glyph_index
        self._pack.pack()
        packed = self._pack.map[pack_index]
        self._update_texture(packed.bin)
        atlas_glyph = AtlasGlyph(
            self,
            rendered_glyph.bearing,
            packed.bin,
            packed.position + ivec2(self._padding, self._padding),
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
        return super().render_glyph(character, format=self._format)

    @property
    def format(self) -> RenderedGlyphFormat:
        return self._format

    @property
    def texture_size(self) -> ivec2:
        return ivec2(self._texture_size)


class AtlasGlyph:

    def __init__(
        self,
        font: AtlasFont,
        bearing: tuple[int, int],
        texture_index: int,
        position: tuple[int, int],
        size: tuple[int, int],
        *,
        data: Optional[bytes] = None,
    ):
        self._font = ref(font)
        self._bearing = bearing
        self._texture_index = texture_index
        self._position = position
        self._size = size

    def __repr__(self) -> str:
        font = self._font()
        if not font:
            return '<gamut.text.AtlasGlyph (orphaned)>'
        else:
            return (
                f'<gamut.text.AtlasGlyph texture={self.texture} '
                f'position={self._position}>'
            )

    @property
    def font(self) -> AtlasFont:
        font = self._font()
        if font is None:
            raise RuntimeError('font no longer exists')
        return font

    @property
    def texture(self) -> Texture2d:
        return self._font()._textures[self._texture_index]

    @property
    def bearing(self) -> ivec2:
        return ivec2(self._bearing)

    @property
    def position(self) -> ivec2:
        return ivec2(self._position)

    @property
    def size(self) -> ivec2:
        return ivec2(self._size)
        
    @property
    def uv(self) -> tuple[vec2, vec2]:
        tex_size = vec2(self.font.texture_size)
        top_left = vec2(self._position) / tex_size
        bottom_right = vec2(self._position + self._size) / tex_size
        return top_left, bottom_right
