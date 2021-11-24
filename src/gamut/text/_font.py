
from __future__ import annotations

__all__ = ['Font']

# gamut
from ._break import break_never, BreakMethod
# python
from abc import ABC, abstractmethod
from io import BytesIO
from pathlib import Path
from typing import BinaryIO, Final, Generator, Optional, Sequence, Union
# freetype-py
from freetype import FT_ENCODING_UNICODE
from freetype import Face as FtFace
# uharfbuzz
from uharfbuzz import Buffer as HbBuffer
from uharfbuzz import Face as HbFace
from uharfbuzz import Font as HbFont
from uharfbuzz import shape as hb_shape

UBRK_LINE_HARD: Final = 100


class Font:

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
        return f'<gamut.text.Font {self._name!r}>'

    def request_point_size(
        self,
        width: Optional[float] = None,
        height: Optional[float] = None,
        dpi: tuple[int, int] = (72, 72),
    ) -> FontSize:
        if width is None and height is None:
            raise TypeError('width or height must be specified')
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
        size: FontSize
    ) -> RenderedGlyph:
        if isinstance(character, str) and len(character) != 1:
            raise ValueError('only a single character may be rendered')
        if size.font is not self:
            raise ValueError('size is not compatible with this font')
        size._use()
        if isinstance(character, str):
            self._ft_face.load_char(character)
        else:
            self._ft_face.load_glyph(character)
        ft_glyph = self._ft_face.glyph
        return RenderedGlyph(
            bytes(ft_glyph.bitmap.buffer),
            (ft_glyph.bitmap.pitch, ft_glyph.bitmap.rows),
            (ft_glyph.bitmap_left, -ft_glyph.bitmap_top),
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
        pen_position_x = 0
        pen_position_y = size._line_size[1]
        for chunk in break_method(text):
            chunk_pen_position_x = pen_position_x
            chunk_pen_position_y = pen_position_y
            hb_buffer = HbBuffer()
            hb_buffer.direction = 'LTR'
            hb_buffer.add_str(chunk.text)
            hb_shape(self._hb_font, hb_buffer, {
                "kern": True,
                "liga": True,
            })
            chunk_glyphs: list[PositionedGlyph] = []
            for info, pos in zip(
                hb_buffer.glyph_infos,
                hb_buffer.glyph_positions
            ):
                c = chunk.text[info.cluster]
                chunk_glyphs.append(PositionedGlyph(
                    c,
                    info.codepoint,
                    (
                        pen_position_x + (pos.x_offset / 64.0),
                        pen_position_y + (pos.y_offset / 64.0),
                    ),
                ))
                pen_position_x += pos.x_advance / 64.0
                pen_position_y += pos.y_advance / 64.0
            if max_line_size is not None and pen_position_x > max_line_size:
                for chunk_glyph in chunk_glyphs:
                    chunk_glyph.position = (
                        chunk_glyph.position[0] - chunk_pen_position_x,
                        chunk_glyph.position[1]
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
        position: tuple[int, int],
    ):
        self.character = character
        self.glyph_index = glyph_index
        self.position = position

    def __repr__(self) -> str:
        return (
            f'<gamut.text.PositionedGlyph {self.character!r} @ '
            f'{self.position}>'
        )


class RenderedGlyph:

    def __init__(
        self,
        data: bytes,
        size: tuple[int, int],
        bearing: tuple[int, int],
    ):
        self._data = data
        self._size = size
        self._bearing = bearing

    @property
    def data(self) -> bytes:
        return self._data

    @property
    def size(self) -> tuple[int, int]:
        return self._size

    @property
    def bearing(self) -> tuple[int, int]:
        return self._bearing


class FontSize(ABC):

    def __init__(self, font: Font):
        self._font = font
        self._use()
        self._nominal_size = (
            self._font._ft_face.size.x_ppem,
            self._font._ft_face.size.y_ppem,
        )
        self._scale = (
            self._font._ft_face.size.x_scale *
            self._font._ft_face.units_per_EM +
            (1 << 15) >> 16,
            self._font._ft_face.size.y_scale *
            self._font._ft_face.units_per_EM +
            (1 << 15) >> 16,
        )
        self._line_size = (
            0.0, # how
            self._font._ft_face.size.height / 64.0,
        )

    def __repr__(self) -> str:
        return (
            f'<gamut.text.FontSize for {self._font.name!r} of '
            f'{self.nominal_size}>'
        )

    @abstractmethod
    def _use(self) -> None:
        ...

    @property
    def font(self) -> Font:
        return self._font

    @property
    def nominal_size(self) -> tuple[int, int]:
        return self._nominal_size


class PointFontSize(FontSize):

    def __init__(
        self,
        font: Font,
        width: Optional[float],
        height: Optional[float],
        dpi: tuple[int, int]
    ):
        self._args = (width, height, dpi)
        super().__init__(font)

    def _use(self) -> None:
        self.font._ft_face.set_char_size(*self._args)


class PixelFontSize(FontSize):

    def __init__(
        self,
        font: Font,
        width: Optional[int],
        height: Optional[int],
    ):
        self._args = (width, height)
        super().__init__(font)

    def _use(self) -> None:
        self.font._ft_face.set_pixel_sizes(*self._args)


class FixedFontSize(FontSize):

    def __init__(
        self,
        font: Font,
        index: int,
    ):
        self._index = index
        super().__init__(font)

    def _use(self) -> None:
        self.font._ft_face.select_size(self._index)
