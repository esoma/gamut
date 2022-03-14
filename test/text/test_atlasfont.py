
# gamut
from gamut.graphics import BufferView, Texture2d
from gamut.math import IVector2, Vector2
from gamut.text import AtlasFont, AtlasGlyph, Face, RenderedGlyphFormat
# python
import gc
import os
from pathlib import Path
from typing import Final
# pyglm
import glm
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
@pytest.mark.parametrize("format", list(RenderedGlyphFormat))
def test_init(file: str, format: RenderedGlyphFormat) -> None:
    face = Face(file)
    size = face.request_pixel_size(height=12)
    font = AtlasFont(size, format)
    assert font.face is face
    assert font.size is size
    assert font.format is format
    assert isinstance(font.texture_size, IVector2)
    assert font.texture_size == IVector2(512, 512)
    assert isinstance(font.textures, tuple)
    assert len(font.textures) == 0


@pytest.mark.parametrize("file", FONTS)
@pytest.mark.parametrize("glyph_index", [-1000, -1, 999999])
def test_get_invalid_glyph_index(file: str, glyph_index: int) -> None:
    face = Face(file)
    size = face.request_pixel_size(height=12)
    font = AtlasFont(size, RenderedGlyphFormat.ALPHA)
    with pytest.raises(IndexError) as excinfo:
        font[glyph_index]
    assert str(excinfo.value) == f'{glyph_index}'


@pytest.mark.parametrize("file", FONTS)
@pytest.mark.parametrize("character", 'aZ ')
@pytest.mark.parametrize("format", list(RenderedGlyphFormat))
def test_get(file: str, character: str, format: RenderedGlyphFormat) -> None:
    face = Face(file)
    size = face.request_pixel_size(height=12)
    font = AtlasFont(size, format)
    glyph_index = font.get_glyph_index(character)

    atlas_glyph = font[glyph_index]
    assert isinstance(atlas_glyph, AtlasGlyph)
    assert atlas_glyph.font is font
    assert atlas_glyph.texture_index == 0
    assert atlas_glyph.texture is font.textures[0]

    atlas_glyph_bearing = atlas_glyph.bearing
    assert isinstance(atlas_glyph.bearing, IVector2)
    atlas_glyph_bearing += IVector2(1, 1)
    assert atlas_glyph.bearing != atlas_glyph_bearing

    atlas_glyph_position = atlas_glyph.position
    assert isinstance(atlas_glyph.position, IVector2)
    atlas_glyph_position += IVector2(1, 1)
    assert atlas_glyph.position != atlas_glyph_position

    atlas_glyph_size = atlas_glyph.size
    assert isinstance(atlas_glyph.size, IVector2)
    atlas_glyph_size += IVector2(1, 1)
    assert atlas_glyph.size != atlas_glyph_size

    uv_top_left, uv_bottom_right = atlas_glyph.uv
    assert isinstance(uv_top_left, Vector2)
    assert isinstance(uv_bottom_right, Vector2)
    assert atlas_glyph.uv[0] is not uv_top_left
    assert atlas_glyph.uv[1] is not uv_bottom_right
    uv_top_left += Vector2(1, 1)
    uv_bottom_right += Vector2(1, 1)
    assert atlas_glyph.uv[0] != uv_top_left
    assert atlas_glyph.uv[1] != uv_bottom_right

    assert repr(atlas_glyph) == (
        f'<gamut.text.AtlasGlyph texture={atlas_glyph.texture} '
        f'position={tuple(atlas_glyph.position)}>'
    )


@pytest.mark.parametrize("file", FONTS)
def test_orphaned_atlas_glyph(file: str) -> None:
    face = Face(file)
    size = face.request_pixel_size(height=12)
    font = AtlasFont(size, RenderedGlyphFormat.ALPHA)
    glyph_index = font.get_glyph_index('a')
    atlas_glyph = font[glyph_index]
    assert atlas_glyph.font is font

    del font
    gc.collect()

    with pytest.raises(RuntimeError) as excinfo:
        atlas_glyph.font
    assert str(excinfo.value) == 'font no longer exists'

    assert repr(atlas_glyph) == '<gamut.text.AtlasGlyph (orphaned)>'


@pytest.mark.parametrize("file", FONTS)
@pytest.mark.parametrize("texture_size", [
    IVector2(16, 16),
    IVector2(128, 128),
    IVector2(256, 256),
])
def test_buffer_positioned_glyphs(
    file: str,
    texture_size: IVector2
) -> None:
    face = Face(file)
    size = face.request_pixel_size(height=12)
    font = AtlasFont(
        size,
        RenderedGlyphFormat.ALPHA,
        texture_size=texture_size
    )
    positioned_glyphs = font.layout_text('hello world')
    map = font.buffer_positioned_glyphs(positioned_glyphs)
    assert map
    assert isinstance(map, dict)
    for texture, buffers in map.items():
        assert isinstance(texture, Texture2d)
        assert texture in font.textures
        assert isinstance(buffers, tuple)
        assert len(buffers) == 2
        pos, uv = buffers
        assert isinstance(pos, BufferView)
        assert pos.type is glm.vec4
        assert isinstance(uv, BufferView)
        assert uv.type is glm.vec2


@pytest.mark.parametrize("file", FONTS)
@pytest.mark.parametrize("texture_size", [
    IVector2(16, 16),
    IVector2(128, 128),
    IVector2(256, 256),
])
def test_buffer_text(
    file: str,
    texture_size: IVector2
) -> None:
    face = Face(file)
    size = face.request_pixel_size(height=12)
    font = AtlasFont(
        size,
        RenderedGlyphFormat.ALPHA,
        texture_size=texture_size
    )
    map = font.buffer_text('hello world')
    assert map
    assert isinstance(map, dict)
    for texture, buffers in map.items():
        assert isinstance(texture, Texture2d)
        assert texture in font.textures
        assert isinstance(buffers, tuple)
        assert len(buffers) == 2
        pos, uv = buffers
        assert isinstance(pos, BufferView)
        assert pos.type is glm.vec4
        assert isinstance(uv, BufferView)
        assert uv.type is glm.vec2
