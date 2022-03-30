
from __future__ import annotations

__all__ = ['Texture2d', 'Texture2dArray']

# gamut
from ._texture import (MipmapSelection, Texture, TextureComponents,
                       TextureDataType, TextureFilter, TextureType,
                       TextureWrap)
# gamut
from gamut.math import FVector3, UVector2, UVector3


class Texture2d(Texture):

    def __init__(
        self,
        size: UVector2,
        components: TextureComponents,
        data_type: type[TextureDataType],
        data: bytes,
        *,
        anisotropy: float | None = None,
        mipmap_selection: MipmapSelection | None = None,
        minify_filter: TextureFilter | None = None,
        magnify_filter: TextureFilter | None = None,
        wrap: tuple[TextureWrap, TextureWrap] | None = None,
        wrap_color: FVector3 | None = None
    ):
        super().__init__(
            TextureType.NORMAL_2D,
            size=size,
            components=components,
            data_type=data_type,
            data=data,
            anisotropy=anisotropy,
            mipmap_selection=mipmap_selection,
            minify_filter=minify_filter,
            magnify_filter=magnify_filter,
            wrap=wrap,
            wrap_color=wrap_color,
        )

    @property
    def size(self) -> UVector2:
        size = super().size
        assert isinstance(size, UVector2)
        return size

    @property
    def wrap(self) -> tuple[TextureWrap, TextureWrap]:
        return super().wrap


Texture2d.__module__ = 'gamut.graphics'



class Texture2dArray(Texture):

    def __init__(
        self,
        size: UVector3,
        components: TextureComponents,
        data_type: type[TextureDataType],
        data: bytes,
        *,
        anisotropy: float | None = None,
        mipmap_selection: MipmapSelection | None = None,
        minify_filter: TextureFilter | None = None,
        magnify_filter: TextureFilter | None = None,
        wrap: tuple[TextureWrap, TextureWrap] | None = None,
        wrap_color: FVector3 | None = None
    ):
        super().__init__(
            TextureType.ARRAY_2D,
            size=size,
            components=components,
            data_type=data_type,
            data=data,
            anisotropy=anisotropy,
            mipmap_selection=mipmap_selection,
            minify_filter=minify_filter,
            magnify_filter=magnify_filter,
            wrap=wrap,
            wrap_color=wrap_color,
        )

    @property
    def size(self) -> UVector3:
        size = super().size
        assert isinstance(size, UVector3)
        return size

    @property
    def wrap(self) -> tuple[TextureWrap, TextureWrap]:
        return super().wrap


Texture2dArray.__module__ = 'gamut.graphics'
