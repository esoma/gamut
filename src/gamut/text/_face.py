
from __future__ import annotations

__all__ = [
    'Face',
    'FontSize',
    'PositionedGlyph',
    'RenderedGlyph',
    'RenderedGlyphFormat'
]

# gamut
from ._break import break_never, BreakMethod
# gamut
from gamut.math import DVector2, IVector2, UVector2
# python
from abc import ABC, abstractmethod
from enum import Enum
from io import BytesIO
from pathlib import Path
from typing import BinaryIO, Generator, Optional, Sequence, Union
# freetype-py
from freetype import (FT_ENCODING_UNICODE, FT_Exception, FT_RENDER_MODE_LCD,
                      FT_RENDER_MODE_LCD_V, FT_RENDER_MODE_LIGHT,
                      FT_RENDER_MODE_SDF)
from freetype import Face as FtFace
# uharfbuzz
from uharfbuzz import Buffer as HbBuffer
from uharfbuzz import Face as HbFace
from uharfbuzz import Font as HbFont
from uharfbuzz import shape as hb_shape


class RenderedGlyphFormat(Enum):
    ALPHA = FT_RENDER_MODE_LIGHT
    SDF = FT_RENDER_MODE_SDF
    LCD = FT_RENDER_MODE_LCD
    LCD_V = FT_RENDER_MODE_LCD_V


class Face:

    def __init__(self, file: Union[str, Path, BinaryIO]):
        if isinstance(file, (str, Path)):
            with open(file, 'rb') as f:
                fdata = f.read()
                self._ft_face = FtFace(BytesIO(fdata))
                self._hb_face = HbFace(fdata)
        else:
            self._ft_face = FtFace(file)
            self._hb_face = HbFace(file.read())

        self._hb_font = HbFont(self._hb_face)

        self._name = repr(file)
        if self._ft_face.family_name:
            self._name = self._ft_face.family_name.decode('ascii')
        if self._ft_face.postscript_name:
            self._name = self._ft_face.postscript_name.decode('ascii')

        self._ft_face.select_charmap(FT_ENCODING_UNICODE)

    def __repr__(self) -> str:
        return f'<gamut.text.Face {self._name!r}>'

    def get_glyph_index(self, character: str) -> int:
        if len(character) != 1:
            raise TypeError('only a single character may be entered')
        return self._ft_face.get_char_index(character) # type: ignore

    def request_point_size(
        self,
        width: Optional[float] = None,
        height: Optional[float] = None,
        dpi: UVector2 = UVector2(72, 72),
    ) -> FontSize:
        if width is None and height is None:
            raise TypeError('width or height must be specified')
        if not isinstance(dpi, UVector2):
            raise TypeError('dpi must be UVector2')
        return PointFontSize(
            self,
            0 if width is None else (width * 64),
            0 if height is None else (height * 64),
            dpi
        )

    def request_pixel_size(
        self,
        width: Optional[int] = None,
        height: Optional[int] = None,
    ) -> FontSize:
        if width is None and height is None:
            raise TypeError('width or height must be specified')
        return PixelFontSize(
            self,
            0 if width is None else width,
            0 if height is None else height
        )

    def render_glyph(
        self,
        character: Union[str, int],
        size: FontSize,
        *,
        format: RenderedGlyphFormat = RenderedGlyphFormat.ALPHA
    ) -> RenderedGlyph:
        if isinstance(character, str) and len(character) != 1:
            raise TypeError('only a single character may be rendered')
        if size.face is not self:
            raise ValueError('size is not compatible with this face')
        size._use()
        if isinstance(character, str):
            self._ft_face.load_char(character, 0)
        else:
            try:
                self._ft_face.load_glyph(character, 0)
            except FT_Exception as ex:
                raise ValueError('face does not contain the specified glyph')
        ft_glyph = self._ft_face.glyph
        print(ft_glyph.bitmap.width)
        print(ft_glyph.bitmap.rows)
        ft_glyph.render(format.value)
        width = ft_glyph.bitmap.width
        height = ft_glyph.bitmap.rows
        data = bytes(ft_glyph.bitmap.buffer)
        if format == RenderedGlyphFormat.LCD:
            width = width // 3
            data = b''.join((
                bytes((
                    data[x * 3 + (y * ft_glyph.bitmap.pitch)],
                    data[x * 3 + 1 + (y * ft_glyph.bitmap.pitch)],
                    data[x * 3 + 2 + (y * ft_glyph.bitmap.pitch)],
                ))
                for y in range(height)
                for x in range(width)
            ))
        elif format == RenderedGlyphFormat.LCD_V:
            height = height // 3
            data = b''.join((
                bytes((
                    data[x + (y * 3 * ft_glyph.bitmap.pitch)],
                    data[x + ((y * 3 + 1) * ft_glyph.bitmap.pitch)],
                    data[x + ((y * 3 + 2) * ft_glyph.bitmap.pitch)],
                ))
                for y in range(height)
                for x in range(width)
            ))
        return RenderedGlyph(
            data,
            UVector2(width, height),
            IVector2(ft_glyph.bitmap_left, -ft_glyph.bitmap_top),
            format,
        )

    def layout_text(
        self,
        text: str,
        size: FontSize,
        *,
        break_method: BreakMethod = break_never,
        max_line_size: Optional[int] = None
    ) -> Generator[PositionedGlyph, None, None]:
        self._hb_font.scale = size._scale
        pen_position_x = 0.0
        pen_position_y = size._line_size[1]
        for chunk in break_method(text):
            chunk_pen_position_x = pen_position_x
            chunk_pen_position_y = pen_position_y
            hb_buffer = HbBuffer()
            hb_buffer.direction = 'LTR'
            hb_buffer.add_str(chunk.text)
            hb_shape(self._hb_font, hb_buffer, {})
            chunk_glyphs: list[PositionedGlyph] = []
            for info, pos in zip(
                hb_buffer.glyph_infos,
                hb_buffer.glyph_positions
            ):
                c = chunk.text[info.cluster]
                chunk_glyphs.append(PositionedGlyph(
                    c,
                    info.codepoint,
                    DVector2(
                        pen_position_x + (pos.x_offset / 64.0),
                        pen_position_y + (pos.y_offset / 64.0),
                    ),
                ))
                pen_position_x += pos.x_advance / 64.0
                pen_position_y += pos.y_advance / 64.0
            if max_line_size is not None and pen_position_x > max_line_size:
                if chunk_pen_position_x == 0.0:
                    pen_position_x = 0.0
                else:
                    for chunk_glyph in chunk_glyphs:
                        chunk_glyph.position = DVector2(
                            chunk_glyph.position[0] - chunk_pen_position_x,
                            chunk_glyph.position[1] + size._line_size[1]
                        )
                    pen_position_x -= chunk_pen_position_x
                pen_position_y += size._line_size[1]
            elif chunk.force_newline:
                pen_position_x = 0
                pen_position_y += size._line_size[1]
            yield from chunk_glyphs

    @property
    def fixed_sizes(self) -> Sequence[FontSize]:
        return tuple(
            FixedFontSize(self, i)
            for i, _ in
            enumerate(self._ft_face.available_sizes)
        )

    @property
    def name(self) -> str:
        return self._name


class PositionedGlyph:

    def __init__(
        self,
        character: str,
        glyph_index: int,
        position: DVector2,
    ):
        self.character = character
        self.glyph_index = glyph_index
        self.position = position

    def __repr__(self) -> str:
        return (
            f'<gamut.text.PositionedGlyph {self.character!r} @ '
            f'{tuple(self.position)}>'
        )


class RenderedGlyph:

    def __init__(
        self,
        data: bytes,
        size: UVector2,
        bearing: IVector2,
        format: RenderedGlyphFormat
    ):
        self._data = data
        self._size = size
        self._bearing = bearing
        self._format = format

    @property
    def data(self) -> bytes:
        return self._data

    @property
    def size(self) -> UVector2:
        return self._size

    @property
    def bearing(self) -> IVector2:
        return self._bearing

    @property
    def format(self) -> RenderedGlyphFormat:
        return self._format


class FontSize(ABC):

    def __init__(self, face: Face):
        self._face = face
        self._use()
        self._nominal_size = UVector2(
            self._face._ft_face.size.x_ppem,
            self._face._ft_face.size.y_ppem,
        )
        self._scale = (
            self._face._ft_face.size.x_scale *
            self._face._ft_face.units_per_EM +
            (1 << 15) >> 16,
            self._face._ft_face.size.y_scale *
            self._face._ft_face.units_per_EM +
            (1 << 15) >> 16,
        )
        self._line_size = (
            0.0, # how
            self._face._ft_face.size.height / 64.0,
        )

    def __repr__(self) -> str:
        return (
            f'<gamut.text.FontSize for {self._face.name!r} of '
            f'{self.nominal_size}>'
        )

    @abstractmethod
    def _use(self) -> None:
        ...

    @property
    def face(self) -> Face:
        return self._face

    @property
    def nominal_size(self) -> UVector2:
        return self._nominal_size


class PointFontSize(FontSize):

    def __init__(
        self,
        face: Face,
        width: Optional[float],
        height: Optional[float],
        dpi: UVector2
    ):
        self._args = (width, height, dpi.x, dpi.y)
        super().__init__(face)

    def _use(self) -> None:
        self.face._ft_face.set_char_size(*self._args)


class PixelFontSize(FontSize):

    def __init__(
        self,
        face: Face,
        width: Optional[int],
        height: Optional[int],
    ):
        self._args = (width, height)
        super().__init__(face)

    def _use(self) -> None:
        self.face._ft_face.set_pixel_sizes(*self._args)


class FixedFontSize(FontSize):

    def __init__(
        self,
        face: Face,
        index: int,
    ):
        self._index = index
        super().__init__(face)

    def _use(self) -> None:
        self.face._ft_face.select_size(self._index)
