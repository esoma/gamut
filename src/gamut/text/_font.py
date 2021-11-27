
from __future__ import annotations

__all__ = ['Font']


# gamut
from ._break import break_never, BreakMethod
from ._face import (Face, FontSize, PositionedGlyph, RenderedGlyph,
                    RenderedGlyphFormat)
# python
from typing import Generator, Optional, Union


class Font:

    def __init__(self, size: FontSize):
        self._size = size

    def __repr__(self) -> str:
        return (
            f'<gamut.text.Font {self._size.face.name!r} of '
            f'{tuple(self._size.nominal_size)}>'
        )

    def get_glyph_index(self, character: str) -> int:
        return self._size.face.get_glyph_index(character)

    def render_glyph(
        self,
        character: Union[str, int],
        *,
        format: RenderedGlyphFormat = RenderedGlyphFormat.ALPHA
    ) -> RenderedGlyph:
        return self._size.face.render_glyph(
            character,
            self._size,
            format=format
        )

    def layout_text(
        self,
        text: str,
        *,
        break_method: BreakMethod = break_never,
        max_line_size: Optional[int] = None
    ) -> Generator[PositionedGlyph, None, None]:
        return self._size.face.layout_text(
            text,
            self._size,
            break_method=break_method,
            max_line_size=max_line_size,
        )

    @property
    def size(self) -> FontSize:
        return self._size

    @property
    def face(self) -> Face:
        return self._size.face
