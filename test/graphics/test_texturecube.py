
from __future__ import annotations
# gamut
from .test_texture import TextureTest
# gamut
from gamut.glmhelp import F32Vector4, I32Vector1, I32Vector2, I32Vector3
from gamut.graphics import (MipmapSelection, TextureComponents, TextureCube,
                            TextureDataType, TextureFilter, TextureWrap)
# python
from typing import Any, cast


class TestTextureCube(TextureTest):

    size_length = 2
    wrap_length = 3
    data_multiplier = 6

    @classmethod
    def create_texture(
        cls,
        size: I32Vector1 | I32Vector2 | I32Vector3,
        components: TextureComponents,
        data_type: type[TextureDataType],
        data: bytes,
        *,
        mipmap_selection: MipmapSelection | None = None,
        minify_filter: TextureFilter | None = None,
        magnify_filter: TextureFilter | None = None,
        wrap: tuple[TextureWrap] |
              tuple[TextureWrap, TextureWrap] |
              tuple[TextureWrap, TextureWrap, TextureWrap] |
              None = None,
        wrap_color: F32Vector4 | None = None
    ) -> TextureCube:
        return TextureCube(
            cast(Any, size),
            components,
            data_type,
            data,
            mipmap_selection=mipmap_selection,
            minify_filter=minify_filter,
            magnify_filter=magnify_filter,
            wrap=cast(Any, wrap),
            wrap_color=wrap_color
        )
