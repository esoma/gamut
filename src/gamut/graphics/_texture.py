
from __future__ import annotations

__all__ = [
    'bind_texture',
    'MipmapSelection',
    'Texture',
    'TextureComponents',
    'TextureDataType',
    'TextureFilter',
    'TextureWrap',
    'TEXTURE_COMPONENTS_COUNT',
    'TEXTURE_DATA_TYPES',
    'TEXTURE_DATA_TYPES_SORTED',
    'TEXTURE_DATA_TYPE_TO_GL_DATA_TYPE',
    'TEXTURE_FILTER_TO_GL_MAG_FILTER',
    'TEXTURE_FILTER_TO_GL_MIN_FILTER',
    'TextureType',
]

# gamut
from gamut._glcontext import (get_gl_context, release_gl_context,
                              require_gl_context)
from gamut.glmhelp import (F32Vector4, I32Vector1, I32Vector2, I32Vector3,
                           ivec1_exact, ivec2_exact, ivec3_exact, vec4_exact)
# python
from ctypes import sizeof as c_sizeof
from enum import Enum
from math import prod
from typing import Any, Final, Union
# pyglm
import glm
from glm import ivec1, ivec2, ivec3, uint32
from glm import value_ptr as glm_value_ptr
from glm import vec4
# pyopengl
import OpenGL.GL
from OpenGL.GL import (GL_TEXTURE0, GL_TEXTURE_2D, GL_TEXTURE_2D_ARRAY,
                       GL_TEXTURE_BORDER_COLOR, GL_TEXTURE_MAG_FILTER,
                       GL_TEXTURE_MIN_FILTER, GL_TEXTURE_WRAP_R,
                       GL_TEXTURE_WRAP_S, GL_TEXTURE_WRAP_T,
                       GL_UNSIGNED_INT_24_8, glActiveTexture, glBindTexture,
                       glGenerateMipmap, glGenTextures, glTexImage2D,
                       glTexImage3D, glTexParameterfv, glTexParameteri)


class Texture:

    def __init__(
        self,
        type: TextureType,
        *,
        size: I32Vector1 | I32Vector2 | I32Vector3,
        components: TextureComponents,
        data_type: type[TextureDataType],
        data: bytes,
        mipmap_selection: MipmapSelection | None = None,
        minify_filter: TextureFilter | None = None,
        magnify_filter: TextureFilter | None = None,
        wrap: tuple[TextureWrap] |
              tuple[TextureWrap, TextureWrap] |
              tuple[TextureWrap, TextureWrap, TextureWrap] |
              None = None,
        wrap_color: F32Vector4 | None = None
    ):
        self._gl: Any = None
        self._gl_context = require_gl_context()
        # check the type
        if type == TextureType.NORMAL_2D:
            size_length = 2
            wrap_length = 2
            self._gl_target = GL_TEXTURE_2D
        elif type == TextureType.ARRAY_2D:
            size_length = 3
            wrap_length = 2
            self._gl_target = GL_TEXTURE_2D_ARRAY
        # set defaults
        if mipmap_selection is None:
            mipmap_selection = MipmapSelection.NONE
        if minify_filter is None:
            minify_filter = TextureFilter.NEAREST
        if magnify_filter is None:
            magnify_filter = TextureFilter.NEAREST
        if wrap is None:
            wrap = tuple( # type: ignore
                TextureWrap.REPEAT for _ in range(wrap_length)
            )
            assert wrap is not None
        if wrap_color is None:
            wrap_color = vec4(0, 0, 0, 0)
        # check the size
        try:
            if size_length == 1:
                size = ivec1_exact(size)
            elif size_length == 2:
                size = ivec2_exact(size)
            else:
                assert size_length == 3
                size = ivec3_exact(size)
        except TypeError:
            raise TypeError(
                f'size must be a sequence of {size_length} integers'
            )
        for value, name in zip(size, ['width', 'height', 'depth']):
            if value < 1:
                raise ValueError(f'{name} must be > 0')
        self._size = size
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
        # check wrap
        try:
            if len(wrap) != wrap_length:
                raise TypeError()
        except TypeError:
            raise TypeError(f'wrap must be {wrap_length} {TextureWrap}')
        for wrap_value in wrap:
            if not isinstance(wrap_value, TextureWrap):
                raise TypeError(f'wrap items must be {TextureWrap}')
        # check wrap color
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
            prod(size) *
            component_count *
            c_sizeof(data_type)
        )
        data = bytes(data)
        if len(data) != expected_data_length:
            raise ValueError('too much or not enough data')
        # generate the texture and store copy the data to it
        self._gl = glGenTextures(1)
        glBindTexture(self._gl_target, self._gl)
        if type == TextureType.NORMAL_2D:
            assert isinstance(size, ivec2)
            glTexImage2D(
                self._gl_target,
                0,
                components.value,
                size.x, size.y,
                0,
                components.value, gl_data_type, data
            )
        else:
            assert type == TextureType.ARRAY_2D
            assert isinstance(size, ivec3)
            glTexImage3D(
                self._gl_target,
                0,
                components.value,
                size.x, size.y, size.z,
                0,
                components.value, gl_data_type, data
            )
        # we only need to generate mipmaps if we're using a mipmap selection
        # that would actually check the mipmaps
        if mipmap_selection != MipmapSelection.NONE:
            glGenerateMipmap(self._gl_target)
        # set the min/max filter parameters
        glTexParameteri(self._gl_target, GL_TEXTURE_MIN_FILTER, gl_min_filter)
        glTexParameteri(self._gl_target, GL_TEXTURE_MAG_FILTER, gl_mag_filter)
        # set the wrapping parameters
        for wrap_value, wrap_name in zip(wrap, GL_TEXTURE_WRAP_NAMES):
            glTexParameteri(self._gl_target, wrap_name, wrap_value.value)
        glTexParameterfv(
            self._gl_target,
            GL_TEXTURE_BORDER_COLOR,
            glm_value_ptr(wrap_color)
        )

    def __del__(self) -> None:
        self.close()

    def __repr__(self) -> str:
        cls = type(self)
        size_str = 'x'.join(str(c) for c in self._size)
        return (
            f'<{cls.__module__}.{cls.__qualname__} '
            f'{size_str} {self.components}>'
        )

    def close(self) -> None:
        if self._gl is not None:
            get_gl_context().delete_texture(self._gl)
            self._gl = None
        self._gl_context = release_gl_context(self._gl_context)

    @property
    def components(self) -> TextureComponents:
        return self._components

    @property
    def size(self) -> ivec1 | ivec2 | ivec3:
        return type(self._size)(self._size) # type: ignore

    @property
    def is_open(self) -> bool:
        return self._gl is not None


def bind_texture(texture: Texture, index: int) -> None:
    assert index >= 0
    glActiveTexture(GL_TEXTURE0 + index)
    glBindTexture(texture._gl_target, texture._gl)


class MipmapSelection(Enum):
    NONE = 0
    NEAREST = 1
    LINEAR = 2


class TextureFilter(Enum):
    NEAREST = 0
    LINEAR = 1


class TextureComponents(Enum):
    R = OpenGL.GL.GL_RED
    RG = OpenGL.GL.GL_RG
    RGB = OpenGL.GL.GL_RGB
    RGBA = OpenGL.GL.GL_RGBA
    D = OpenGL.GL.GL_DEPTH_COMPONENT
    DS = OpenGL.GL.GL_DEPTH_STENCIL


class TextureWrap(Enum):
    CLAMP_TO_EDGE = OpenGL.GL.GL_CLAMP_TO_EDGE
    CLAMP_TO_COLOR = OpenGL.GL.GL_CLAMP_TO_BORDER
    REPEAT = OpenGL.GL.GL_REPEAT
    REPEAT_MIRRORED = OpenGL.GL.GL_MIRRORED_REPEAT
    REPEAT_MIRRORED_THEN_CLAMP_TO_EDGE = OpenGL.GL.GL_MIRROR_CLAMP_TO_EDGE


class TextureType(Enum):
    NORMAL_2D = 0
    ARRAY_2D = 1


GL_TEXTURE_WRAP_NAMES: Final = (
    GL_TEXTURE_WRAP_S,
    GL_TEXTURE_WRAP_T,
    GL_TEXTURE_WRAP_R
)


TEXTURE_COMPONENTS_COUNT: Final = {
    TextureComponents.R: 1,
    TextureComponents.RG: 2,
    TextureComponents.RGB: 3,
    TextureComponents.RGBA: 4,
    TextureComponents.D: 1,
    TextureComponents.DS: 1
}


TEXTURE_DATA_TYPE_TO_GL_DATA_TYPE: Final[dict[type[TextureDataType], Any]] = {
    glm.uint8: OpenGL.GL.GL_UNSIGNED_BYTE,
    glm.int8: OpenGL.GL.GL_BYTE,
    glm.uint16: OpenGL.GL.GL_UNSIGNED_SHORT,
    glm.int16: OpenGL.GL.GL_SHORT,
    glm.uint32: OpenGL.GL.GL_UNSIGNED_INT,
    glm.int32: OpenGL.GL.GL_INT,
    glm.float32: OpenGL.GL.GL_FLOAT,
}


TEXTURE_FILTER_TO_GL_MIN_FILTER: Final = {
    (MipmapSelection.NONE, TextureFilter.NEAREST): OpenGL.GL.GL_NEAREST,
    (MipmapSelection.NONE, TextureFilter.LINEAR): OpenGL.GL.GL_LINEAR,
    (MipmapSelection.NEAREST, TextureFilter.NEAREST):
        OpenGL.GL.GL_NEAREST_MIPMAP_NEAREST,
    (MipmapSelection.NEAREST, TextureFilter.LINEAR):
        OpenGL.GL.GL_NEAREST_MIPMAP_LINEAR,
    (MipmapSelection.LINEAR, TextureFilter.NEAREST):
        OpenGL.GL.GL_LINEAR_MIPMAP_NEAREST,
    (MipmapSelection.LINEAR, TextureFilter.LINEAR):
        OpenGL.GL.GL_LINEAR_MIPMAP_LINEAR,
}


TEXTURE_FILTER_TO_GL_MAG_FILTER: Final = {
    TextureFilter.NEAREST: OpenGL.GL.GL_NEAREST,
    TextureFilter.LINEAR: OpenGL.GL.GL_LINEAR,
}


TextureDataType = Union[
    glm.uint8, glm.int8,
    glm.uint16, glm.int16,
    glm.uint32, glm.int32,
    glm.float32
]


TEXTURE_DATA_TYPES_SORTED: Final = list(
    TEXTURE_DATA_TYPE_TO_GL_DATA_TYPE.keys()
)
TEXTURE_DATA_TYPES: Final = set(TEXTURE_DATA_TYPES_SORTED)
