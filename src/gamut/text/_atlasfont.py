

from __future__ import annotations

__all__ = ['AtlasFont', 'AtlasGlyph']


# gamut
from ._face import FontSize, RenderedGlyph, RenderedGlyphFormat
from ._font import Font
# gamut
from gamut.graphics import Texture2d
# python
from typing import Optional, Union
from weakref import ref


class AtlasFont(Font):

    def __init__(
        self,
        size: FontSize,
        format: RenderedGlyphFormat,
        *,
        texture_size: tuple[int, int] = (256, 256),
    ):
        super().__init__(size)
        self._format = format
        self._texture_size = texture_size
        self._glyph_map: dict[int, AtlasGlyph] = {}
        self._textures: list[Texture2d] = []

    def __getitem__(self, glyph_index: int) -> AtlasGlyph:
        try:
            return self._glyph_map[glyph_index]
        except KeyError:
            return self._map_glyph(glyph_index)

    def _map_glyph(self, glyph_index: int) -> AtlasGlyph:
        assert glyph_index not in self._glyph_map
        rendered_glyph = self.render_glyph(glyph_index)
        atlas_glyph = AtlasGlyph(
            self,
            rendered_glyph.bearing,
            0,
            (0, 0),
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
