
from __future__ import annotations

__all__ = ['TextureCube']

# gamut
from ._texture import (MipmapSelection, Texture, TextureComponents,
                       TextureDataType, TextureFilter, TextureType,
                       TextureWrap)
# gamut
from gamut.math import FVector4, UVector2


class TextureCube(Texture):

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
        wrap: tuple[TextureWrap, TextureWrap, TextureWrap] | None = None,
        wrap_color: FVector4 | None = None
    ):
        super().__init__(
            TextureType.NORMAL_CUBE,
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


TextureCube.__module__ = 'gamut.graphics'
