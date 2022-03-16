
# gamut
from gamut.math import IVector2, UVector2, Vector2
from gamut.text import (BreakChunk, Face, Font, PositionedGlyph,
                        RenderedGlyphFormat)
# python
import os
from pathlib import Path
from typing import Any, Final, Generator, Optional, Union
# pytest
import pytest

DIR: Final = Path(__file__).parent
FONTS_DIR: Final = DIR / 'fonts'
FONTS: Final = [
    str(FONTS_DIR / file_name)
    for file_name in os.listdir(FONTS_DIR)
    if not file_name.endswith('.txt')
]


@pytest.mark.parametrize("file", FONTS)
def test_init(file: str) -> None:
    face = Face(file)
    size = face.request_point_size(height=12)
    font = Font(size)
    assert font.size is size
    assert font.face is face


@pytest.mark.parametrize("file", FONTS)
@pytest.mark.parametrize("height", [10, 20])
def test_repr(file: str, height: int) -> None:
    face = Face(file)
    size = face.request_point_size(height=height)
    font = Font(size)
    assert repr(font) == (
        f'<gamut.text.Font {face.name!r} of {tuple(size.nominal_size)}>'
    )


@pytest.mark.parametrize("file", FONTS)
@pytest.mark.parametrize("height", [10, 20])
@pytest.mark.parametrize("character", [
    'a', 'z',
    'A', 'Z',
    '\n',
    '食',
    '\u2028'
])
def test_get_glyph_index(file: str, height: int, character: str) -> None:
    face = Face(file)
    size = face.request_point_size(height=height)
    font = Font(size)
    glyph_index = font.get_glyph_index(character)
    assert isinstance(glyph_index, int)
    assert glyph_index == face.get_glyph_index(character)


@pytest.mark.parametrize("file", FONTS)
@pytest.mark.parametrize("height", [10, 20])
@pytest.mark.parametrize("character", [
    '', 'aZ', '食食',
])
def test_get_glyph_index_invalid_length(
    file: str,
    height: int,
    character: str
) -> None:
    face = Face(file)
    size = face.request_point_size(height=height)
    font = Font(size)
    with pytest.raises(TypeError) as excinfo:
        font.get_glyph_index(character)
    assert str(excinfo.value) == 'only a single character may be entered'


@pytest.mark.parametrize("max_line_size", [
    None, 0, 5, 100, 1000
])
def test_layout_text_no_wrap(max_line_size: Optional[int]) -> None:
    face = Face(FONTS_DIR / 'OpenSans-Regular.ttf')
    size = face.request_pixel_size(height=16)
    font = Font(size)
    positioned_glyphs = list(font.layout_text(
        'hello world',
        max_line_size=max_line_size,
    ))
    def check_glyph(
        glyph: PositionedGlyph,
        character: str,
        glyph_index: int,
        x: float,
        y: float,
    ) -> None:
        assert glyph.character == character
        assert glyph.glyph_index == glyph_index
        assert isinstance(glyph.position, Vector2)
        assert glyph.position.x == pytest.approx(x, abs=1e-1)
        assert glyph.position.y == pytest.approx(y, abs=1e-1)
    assert len(positioned_glyphs) == 11
    check_glyph(positioned_glyphs[0], 'h', 75, 0.0, 22.0)
    check_glyph(positioned_glyphs[1], 'e', 72, 9.8125, 22.0)
    check_glyph(positioned_glyphs[2], 'l', 79, 18.7969, 22.0)
    check_glyph(positioned_glyphs[3], 'l', 79, 22.8281, 22.0)
    check_glyph(positioned_glyphs[4], 'o', 82, 26.8594, 22.0)
    check_glyph(positioned_glyphs[5], ' ', 3, 36.4844, 22.0)
    check_glyph(positioned_glyphs[6], 'w', 90, 40.6406, 22.0)
    check_glyph(positioned_glyphs[7], 'o', 82, 53.0312, 22.0)
    check_glyph(positioned_glyphs[8], 'r', 85, 62.6562, 22.0)
    check_glyph(positioned_glyphs[9], 'l', 79, 69.1875, 22.0)
    check_glyph(positioned_glyphs[10], 'd', 71, 73.2188, 22.0)


@pytest.mark.parametrize("max_line_size, positions", [
    (0, [(0.0, 22.0), (0.0, 44.0), (0.0, 66.0), (0.0, 88.0)]),
    (1, [(0.0, 22.0), (0.0, 44.0), (0.0, 66.0), (0.0, 88.0)]),
    (10, [(0.0, 22.0), (0.0, 44.0), (0.0, 66.0), (0.0, 88.0)]),
    (20, [(0.0, 22.0), (8.8906, 22.0), (0.0, 44.0), (7.6562, 44.0)]),
    (30, [(0.0, 22.0), (8.8906, 22.0), (18.6719, 22.0), (0.0, 44.0)]),
    (40, [(0.0, 22.0), (8.8906, 22.0), (18.6719, 22.0), (26.3281, 22.0)]),
    (None, [(0.0, 22.0), (8.8906, 22.0), (18.6719, 22.0), (26.3281, 22.0)]),
])
def test_layout_text_wrap(
    max_line_size: Optional[int],
    positions: list[tuple[float, float]],
) -> None:

    def break_character(text: str) -> Generator[BreakChunk, None, None]:
        for c in text:
            yield BreakChunk(c)

    face = Face(FONTS_DIR / 'OpenSans-Regular.ttf')
    size = face.request_pixel_size(height=16)
    font = Font(size)
    positioned_glyphs = list(font.layout_text(
        'abcd',
        break_method=break_character,
        max_line_size=max_line_size,
    ))
    def check_glyph(
        glyph: PositionedGlyph,
        character: str,
        glyph_index: int,
        x: float,
        y: float,
    ) -> None:
        assert glyph.character == character
        assert glyph.glyph_index == glyph_index
        assert isinstance(glyph.position, Vector2)
        assert glyph.position.x == pytest.approx(x, abs=1e-1)
        assert glyph.position.y == pytest.approx(y, abs=1e-1)
    assert len(positioned_glyphs) == 4
    check_glyph(positioned_glyphs[0], 'a', 68, *positions[0])
    check_glyph(positioned_glyphs[1], 'b', 69, *positions[1])
    check_glyph(positioned_glyphs[2], 'c', 70, *positions[2])
    check_glyph(positioned_glyphs[3], 'd', 71, *positions[3])


@pytest.mark.parametrize("max_line_size", [
    None, 0, 1, 10, 100, 1000,
])
def test_layout_text_wrap_force(
    max_line_size: Optional[int],
) -> None:

    def break_always(text: str) -> Generator[BreakChunk, None, None]:
        for c in text:
            yield BreakChunk(c, force_newline=True)

    face = Face(FONTS_DIR / 'OpenSans-Regular.ttf')
    size = face.request_pixel_size(height=16)
    font = Font(size)
    positioned_glyphs = list(font.layout_text(
        'abcd',
        break_method=break_always,
        max_line_size=max_line_size,
    ))
    def check_glyph(
        glyph: PositionedGlyph,
        character: str,
        glyph_index: int,
        x: float,
        y: float,
    ) -> None:
        assert glyph.character == character
        assert glyph.glyph_index == glyph_index
        assert isinstance(glyph.position, Vector2)
        assert glyph.position.x == pytest.approx(x, abs=1e-1)
        assert glyph.position.y == pytest.approx(y, abs=1e-1)
    assert len(positioned_glyphs) == 4
    check_glyph(positioned_glyphs[0], 'a', 68, 0.0, 22.0)
    check_glyph(positioned_glyphs[1], 'b', 69, 0.0, 44.0)
    check_glyph(positioned_glyphs[2], 'c', 70, 0.0, 66.0)
    check_glyph(positioned_glyphs[3], 'd', 71, 0.0, 88.0)


@pytest.mark.parametrize("file", FONTS)
@pytest.mark.parametrize("character", ['', 'ab'])
def test_render_glyph_invalid_character(file: str, character: str) -> None:
    face = Face(file)
    size = face.request_pixel_size(height=10)
    font = Font(size)
    with pytest.raises(TypeError) as excinfo:
        font.render_glyph(character)
    assert str(excinfo.value) == 'only a single character may be rendered'



@pytest.mark.parametrize("file", FONTS)
@pytest.mark.parametrize("glyph_index", [-1000, -1, 999999])
def test_render_glyph_invalid_index(file: str, glyph_index: int) -> None:
    face = Face(file)
    size = face.request_pixel_size(height=10)
    font = Font(size)
    with pytest.raises(ValueError) as excinfo:
        font.render_glyph(glyph_index)
    assert str(excinfo.value) == 'face does not contain the specified glyph'


@pytest.mark.parametrize("file", FONTS)
@pytest.mark.parametrize("character", ['a', 'Z', '1'])
@pytest.mark.parametrize("use_glyph_index", [False, True])
@pytest.mark.parametrize("format", [None] + list(RenderedGlyphFormat))
def test_render_glyph(
    file: str,
    character: str,
    use_glyph_index: bool,
    format: Optional[RenderedGlyphFormat],
) -> None:
    face = Face(file)
    size = face.request_pixel_size(height=10)
    font = Font(size)
    input: Union[str, int]
    if use_glyph_index:
        input = font.get_glyph_index(character)
    else:
        input = character
    kwargs: dict[str, Any] = {}
    if format is not None:
        kwargs["format"] = format
    else:
        format = RenderedGlyphFormat.ALPHA
    rendered_glyph = font.render_glyph(input, **kwargs)

    assert isinstance(rendered_glyph.data, bytes)
    assert rendered_glyph.data
    assert len(rendered_glyph.data) == (
        rendered_glyph.size.x *
        rendered_glyph.size.y * (
            3
            if format in (RenderedGlyphFormat.LCD, RenderedGlyphFormat.LCD_V)
            else
            1
        )
    )

    assert isinstance(rendered_glyph.size, UVector2)
    assert rendered_glyph.size.x > 0
    assert rendered_glyph.size.y > 0
    rendered_glyph_size = rendered_glyph.size
    rendered_glyph_size += UVector2(1, 1)
    assert rendered_glyph.size != rendered_glyph_size

    assert isinstance(rendered_glyph.bearing, IVector2)
    rendered_glyph_bearing = rendered_glyph.bearing
    rendered_glyph_bearing += IVector2(1, 1)
    assert rendered_glyph.bearing != rendered_glyph_bearing

    assert rendered_glyph.format is format
