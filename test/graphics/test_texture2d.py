
from __future__ import annotations
# gamut
from .test_texture import TextureTest
# gamut
from gamut.graphics import (MipmapSelection, Texture2d, Texture2dArray,
                            TextureComponents, TextureDataType, TextureFilter,
                            TextureWrap)
from gamut.math import FVector4, UVector1, UVector2, UVector3
# python
from typing import Any, cast


class TestTexture2d(TextureTest):

    size_length = 2
    wrap_length = 2

    @classmethod
    def create_texture(
        cls,
        size: UVector1 | UVector2 | UVector3,
        components: TextureComponents,
        data_type: type[TextureDataType],
        data: bytes,
        *,
        anisotropy: float | None = None,
        mipmap_selection: MipmapSelection | None = None,
        minify_filter: TextureFilter | None = None,
        magnify_filter: TextureFilter | None = None,
        wrap: tuple[TextureWrap] |
              tuple[TextureWrap, TextureWrap] |
              tuple[TextureWrap, TextureWrap, TextureWrap] |
              None = None,
        wrap_color: FVector4 | None = None
    ) -> Texture2d:
        return Texture2d(
            cast(Any, size),
            components,
            data_type,
            data,
            anisotropy=anisotropy,
            mipmap_selection=mipmap_selection,
            minify_filter=minify_filter,
            magnify_filter=magnify_filter,
            wrap=cast(Any, wrap),
            wrap_color=wrap_color
        )


class TestTexture2dArray(TextureTest):

    size_length = 3
    wrap_length = 2

    @classmethod
    def create_texture(
        cls,
        size: UVector1 | UVector2 | UVector3,
        components: TextureComponents,
        data_type: type[TextureDataType],
        data: bytes,
        *,
        anisotropy: float | None = None,
        mipmap_selection: MipmapSelection | None = None,
        minify_filter: TextureFilter | None = None,
        magnify_filter: TextureFilter | None = None,
        wrap: tuple[TextureWrap] |
              tuple[TextureWrap, TextureWrap] |
              tuple[TextureWrap, TextureWrap, TextureWrap] |
              None = None,
        wrap_color: FVector4 | None = None
    ) -> Texture2dArray:
        return Texture2dArray(
            cast(Any, size),
            components,
            data_type,
            data,
            anisotropy=anisotropy,
            mipmap_selection=mipmap_selection,
            minify_filter=minify_filter,
            magnify_filter=magnify_filter,
            wrap=cast(Any, wrap),
            wrap_color=wrap_color
        )
