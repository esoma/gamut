

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
# python
from typing import Final, Iterable, Optional, Union
from weakref import ref
from PIL import Image as PilImage
# pyglm
from glm import array as glm_array
from glm import ivec2, mat4, scale, translate, uint8, vec2, vec3, vec4

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
        texture_size: tuple[int, int] = (512, 512),
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
            if rendered_glyph.size[0] == 0 or rendered_glyph.size[1] == 0:
                continue
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
            (rendered_glyph.bearing[0], -rendered_glyph.bearing[1]),
            packed.bin,
            (
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
        return super().render_glyph(character, format=self._format)

    def buffer_positioned_glyphs(
        self,
        positioned_glyphs: Iterable[PositionedGlyph],
    ) -> dict[
        Texture2d,
        tuple[BufferView[vec4], BufferView[vec2]]
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
            glyph_position = glm_array(
                *(transform * p for p in glyph_position)
            )
            pos += glyph_position.to_bytes()
            # generate the vertex uvs
            top_left_uv, bottom_right_uv = atlas_glyph.uv
            uvs += create_quad_uv_array(
                PrimitiveMode.TRIANGLE,
                left=top_left_uv.x,
                right=bottom_right_uv.x,
                bottom=bottom_right_uv.y,
                top=top_left_uv.y
            ).to_bytes()

        return {
            texture: (
                BufferView(Buffer(bytes(pos)), vec4),
                BufferView(Buffer(bytes(uvs)), vec2),
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
        tuple[BufferView[vec4], BufferView[vec2]]
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
    def texture_size(self) -> ivec2:
        return ivec2(self._texture_size)

    @property
    def textures(self) -> tuple[Texture2d, ...]:
        return tuple(self._textures)


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
    def texture_index(self) -> int:
        return self._texture_index

    @property
    def texture(self) -> Texture2d:
        return self.font._textures[self._texture_index]

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
        bottom_right = (vec2(self._position) + vec2(self._size)) / tex_size
        return top_left, bottom_right

    def transform_with_position(self, positioned: PositionedGlyph) -> mat4:
        return scale(
            translate(
                mat4(1),
                vec3(positioned.position[0], -positioned.position[1], 0) -
                vec3(0, self._size[1], 0) +
                vec3(*self._bearing, 0)
            ),
            vec3(*self._size, 1)
        )
