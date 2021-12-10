
from __future__ import annotations

__all__ = ['Texture2d']

# gamut
from ._texture import (MipmapSelection, Texture, TEXTURE_COMPONENTS_COUNT,
                       TEXTURE_DATA_TYPE_TO_GL_DATA_TYPE, TEXTURE_DATA_TYPES,
                       TEXTURE_FILTER_TO_GL_MAG_FILTER,
                       TEXTURE_FILTER_TO_GL_MIN_FILTER, TextureComponents,
                       TextureDataType, TextureFilter, TextureWrap)
# gamut
from gamut._glcontext import (get_gl_context, release_gl_context,
                              require_gl_context)
from gamut.glmhelp import F32Vector4, I32Vector2, ivec2_exact, vec4_exact
# python
from typing import Any, Optional
# pyglm
from glm import ivec2, uint32
from glm import value_ptr as glm_value_ptr
from glm import vec4
# pyopengl
from OpenGL.GL import (GL_TEXTURE0, GL_TEXTURE_2D, GL_TEXTURE_BORDER_COLOR,
                       GL_TEXTURE_MAG_FILTER, GL_TEXTURE_MIN_FILTER,
                       GL_TEXTURE_WRAP_S, GL_TEXTURE_WRAP_T,
                       GL_UNSIGNED_INT_24_8, glActiveTexture, glBindTexture,
                       glGenerateMipmap, glGenTextures, glTexImage2D,
                       glTexParameterfv, glTexParameteri)


class Texture2d(Texture):

    def __init__(
        self,
        size: I32Vector2,
        components: TextureComponents,
        data_type: type[TextureDataType],
        data: bytes,
        *,
        mipmap_selection: MipmapSelection = MipmapSelection.NONE,
        minify_filter: TextureFilter = TextureFilter.NEAREST,
        magnify_filter: TextureFilter = TextureFilter.NEAREST,
        wrap: tuple[TextureWrap, TextureWrap] = (
            TextureWrap.REPEAT,
            TextureWrap.REPEAT
        ),
        wrap_color: F32Vector4 = vec4(0, 0, 0, 0)
    ):
        self._gl: Optional[Any] = None
        self._gl_context = require_gl_context()
        # check size
        try:
            self._size = ivec2_exact(size)
        except TypeError:
            raise TypeError('size must be a sequence of two integers')
        if self._size.x < 1:
            raise ValueError('width must be > 0')
        if self._size.y < 1:
            raise ValueError('height must be > 0')
        # depth/stencil textures cannot have mipmaps, raises an invalid
        # operation error on some platforms, probably a noop on others
        if (mipmap_selection != MipmapSelection.NONE and
            components == TextureComponents.DS):
            raise ValueError('depth/stencil texture cannot have mipmaps')
        # check data type
        try:
            gl_data_type = TEXTURE_DATA_TYPE_TO_GL_DATA_TYPE[data_type]
        except KeyError:
            data_types = ', '.join(sorted((
                str(t) for t in TEXTURE_DATA_TYPES
            )))
            raise TypeError(f'data_type must be {data_types}')
        # decompose and check wrap
        try:
            wrap_s, wrap_t = wrap
            if (not isinstance(wrap_s, TextureWrap) or
                not isinstance(wrap_t, TextureWrap)):
                raise ValueError()
        except (ValueError, TypeError):
            raise TypeError('wrap must be a pair of texture wrap objects')
        try:
            wrap_color = vec4_exact(wrap_color)
        except TypeError:
            raise TypeError('wrap_color must be a sequence of four floats')
        # check components and get the number of components for the given
        if components == TextureComponents.DS:
            if data_type != uint32:
                raise ValueError(
                    f'data_type must be {uint32} when '
                    f'components is {TextureComponents.DS}'
                )
            gl_data_type = GL_UNSIGNED_INT_24_8
        try:
            component_count = TEXTURE_COMPONENTS_COUNT[components]
        except KeyError:
            raise TypeError(f'components must be {TextureComponents}')
        self._components = components
        # check filters
        try:
            gl_min_filter = TEXTURE_FILTER_TO_GL_MIN_FILTER[
                (mipmap_selection, minify_filter)
            ]
        except KeyError:
            if not isinstance(mipmap_selection, MipmapSelection):
                raise TypeError(f'mipmap_selection must be {MipmapSelection}')
            assert not isinstance(minify_filter, TextureFilter)
            raise TypeError(f'minify_filter must be {TextureFilter}')
        try:
            gl_mag_filter = TEXTURE_FILTER_TO_GL_MAG_FILTER[magnify_filter]
        except KeyError:
            raise TypeError(f'magnify_filter must be {TextureFilter}')
        # ensure the length of the data buffer is what we expect give the size,
        # component count and data type
        expected_data_length = (
            self._size.x * self._size.y *
            component_count *
            c_sizeof(data_type)
        )
        data = bytes(data)
        if len(data) != expected_data_length:
            raise ValueError('too much or not enough data')
        # generate the texture and store copy the data to it
        self._gl = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, self._gl)
        glTexImage2D(
            GL_TEXTURE_2D,
            0,
            components.value,
            self._size.x, self._size.y,
            0,
            components.value, gl_data_type, data
        )
        # we only need to generate mipmaps if we're using a mipmap selection
        # that would actually check the mipmaps
        if mipmap_selection != MipmapSelection.NONE:
            glGenerateMipmap(GL_TEXTURE_2D)
        # set the min/max filter parameters
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, gl_min_filter)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, gl_mag_filter)
        # set the wrapping parameters
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, wrap_s.value)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, wrap_t.value)
        glTexParameterfv(
            GL_TEXTURE_2D,
            GL_TEXTURE_BORDER_COLOR,
            glm_value_ptr(wrap_color)
        )

    def __del__(self) -> None:
        self.close()

    def __repr__(self) -> str:
        return (
            f'<gamut.graphics.Texture2d '
            f'{self._size.x}x{self._size.y} '
            f'{self.components}>'
        )

    def _bind(self, index: int) -> None:
        assert index >= 0
        glActiveTexture(GL_TEXTURE0 + index)
        glBindTexture(GL_TEXTURE_2D, self._gl)

    def close(self) -> None:
        if self._gl is not None:
            get_gl_context().delete_texture(self._gl)
            self._gl = None
        self._gl_context = release_gl_context(self._gl_context)

    @property
    def components(self) -> TextureComponents:
        return self._components

    @property
    def size(self) -> ivec2:
        return ivec2(self._size)

    @property
    def is_open(self) -> bool:
        return self._gl is not None


Texture2d.__module__ = 'gamut.graphics'
