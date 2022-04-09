
from __future__ import annotations

__all__ = [
    'bind_texture',
    'get_texture_gl_target',
    'GL_TEXTURE_CUBE_MAP_TARGETS',
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
from gamut.math import FVector4, UVector1, UVector2, UVector3
# python
import ctypes
from ctypes import c_uint32
from ctypes import sizeof as c_sizeof
from enum import Enum
from math import prod
from typing import Any, Final, Union
# pyopengl
import OpenGL.GL
from OpenGL.GL import (GL_TEXTURE0, GL_TEXTURE_2D, GL_TEXTURE_2D_ARRAY,
                       GL_TEXTURE_BORDER_COLOR, GL_TEXTURE_CUBE_MAP,
                       GL_TEXTURE_CUBE_MAP_NEGATIVE_X,
                       GL_TEXTURE_CUBE_MAP_NEGATIVE_Y,
                       GL_TEXTURE_CUBE_MAP_NEGATIVE_Z,
                       GL_TEXTURE_CUBE_MAP_POSITIVE_X,
                       GL_TEXTURE_CUBE_MAP_POSITIVE_Y,
                       GL_TEXTURE_CUBE_MAP_POSITIVE_Z, GL_TEXTURE_MAG_FILTER,
                       GL_TEXTURE_MIN_FILTER, GL_TEXTURE_WRAP_R,
                       GL_TEXTURE_WRAP_S, GL_TEXTURE_WRAP_T,
                       GL_UNSIGNED_INT_24_8, glActiveTexture, glBindTexture,
                       glGenerateMipmap, glGenTextures, glTexImage2D,
                       glTexImage3D, glTexParameterf, glTexParameterfv,
                       glTexParameteri)
from OpenGL.GL.EXT.texture_filter_anisotropic import (
    GL_TEXTURE_MAX_ANISOTROPY_EXT, glInitTextureFilterAnisotropicEXT)


class Texture:

    def __init__(
        self,
        type: TextureType,
        *,
        anisotropy: float = 1.0,
        size: UVector1 | UVector2 | UVector3,
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
        self._type = type
        if type == TextureType.NORMAL_2D:
            size_length = 2
            wrap_length = 2
            self._gl_target = GL_TEXTURE_2D
        elif type == TextureType.ARRAY_2D:
            size_length = 3
            wrap_length = 2
            self._gl_target = GL_TEXTURE_2D_ARRAY
        elif type == TextureType.NORMAL_CUBE:
            size_length = 2
            wrap_length = 3
            self._gl_target = GL_TEXTURE_CUBE_MAP
        else:
            assert False
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
            wrap_color = FVector4(0, 0, 0, 0)
        # check anisotropy
        if anisotropy is None:
            anisotropy = 1.0
        try:
            anisotropy = float(anisotropy)
        except (TypeError, ValueError):
            raise TypeError('anisotropy must be float')
        # check the size
        if size_length == 1:
            if not isinstance(size, UVector1):
                raise TypeError('size must be UVector1')
        elif size_length == 2:
            if not isinstance(size, UVector2):
                raise TypeError('size must be UVector2')
        else:
            assert size_length == 3
            if not isinstance(size, UVector3):
                raise TypeError('size must be UVector3')
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
        if not isinstance(wrap_color, FVector4):
            raise TypeError('wrap color must be FVector4')
        # check components and get the number of components for the given
        if components == TextureComponents.DS:
            if data_type != c_uint32:
                raise ValueError(
                    f'data_type must be {c_uint32} when '
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
        expected_data_length = cube_face_data_length = (
            prod(size) *
            component_count *
            c_sizeof(data_type)
        )
        if type == TextureType.NORMAL_CUBE:
            expected_data_length *= 6
        data = bytes(data)
        if len(data) != expected_data_length:
            raise ValueError('too much or not enough data')
        # generate the texture and store copy the data to it
        self._gl = glGenTextures(1)
        glBindTexture(self._gl_target, self._gl)
        if type == TextureType.NORMAL_2D:
            assert isinstance(size, UVector2)
            glTexImage2D(
                self._gl_target,
                0,
                components.value,
                size.x, size.y,
                0,
                components.value, gl_data_type, data
            )
        elif type == TextureType.ARRAY_2D:
            assert isinstance(size, UVector3)
            glTexImage3D(
                self._gl_target,
                0,
                components.value,
                size.x, size.y, size.z,
                0,
                components.value, gl_data_type, data
            )
        elif type == TextureType.NORMAL_CUBE:
            assert isinstance(size, UVector2)
            for i, gl_cube_target in enumerate(GL_TEXTURE_CUBE_MAP_TARGETS):
                glTexImage2D(
                    gl_cube_target,
                    0,
                    components.value,
                    size.x, size.y,
                    0,
                    components.value, gl_data_type,
                    data[
                        i * cube_face_data_length:
                        (i + 1) * cube_face_data_length
                    ]
                )
        else:
            assert False
        # we only need to generate mipmaps if we're using a mipmap selection
        # that would actually check the mipmaps
        self._mipmap_selection = mipmap_selection
        if mipmap_selection != MipmapSelection.NONE:
            glGenerateMipmap(self._gl_target)
        # set the min/max filter parameters
        self._minify_filter = minify_filter
        self._magnify_filter = magnify_filter
        glTexParameteri(self._gl_target, GL_TEXTURE_MIN_FILTER, gl_min_filter)
        glTexParameteri(self._gl_target, GL_TEXTURE_MAG_FILTER, gl_mag_filter)
        # set the wrapping parameters
        self._wrap = wrap
        self._wrap_color = wrap_color
        for wrap_value, wrap_name in zip(wrap, GL_TEXTURE_WRAP_NAMES):
            glTexParameteri(self._gl_target, wrap_name, wrap_value.value)
        glTexParameterfv(
            self._gl_target,
            GL_TEXTURE_BORDER_COLOR,
            wrap_color.pointer
        )
        # set anisotropy
        self._anisotropy = anisotropy
        if anisotropy > 1.0 and glInitTextureFilterAnisotropicEXT():
            glTexParameterf(
                self._gl_target,
                GL_TEXTURE_MAX_ANISOTROPY_EXT,
                anisotropy
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
    def anisotropy(self) -> float:
        return self._anisotropy

    @property
    def components(self) -> TextureComponents:
        return self._components

    @property
    def magnify_filter(self) -> TextureFilter:
        return self._magnify_filter

    @property
    def minify_filter(self) -> TextureFilter:
        return self._minify_filter

    @property
    def mipmap_selection(self) -> MipmapSelection:
        return self._mipmap_selection

    @property
    def size(self) -> UVector1 | UVector2 | UVector3:
        return self._size

    @property
    def is_open(self) -> bool:
        return self._gl is not None

    @property
    def type(self) -> TextureType:
        return self._type

    @property
    def wrap(self) -> (
        tuple[TextureWrap] |
        tuple[TextureWrap, TextureWrap] |
        tuple[TextureWrap, TextureWrap, TextureWrap]
    ):
        return self._wrap

    @property
    def wrap_color(self) -> FVector4:
        return self._wrap_color


def get_texture_gl_target(texture: Texture) -> Any:
    return texture._gl_target


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
    NORMAL_CUBE = 2


GL_TEXTURE_WRAP_NAMES: Final = (
    GL_TEXTURE_WRAP_S,
    GL_TEXTURE_WRAP_T,
    GL_TEXTURE_WRAP_R
)


GL_TEXTURE_CUBE_MAP_TARGETS: Final = (
    GL_TEXTURE_CUBE_MAP_POSITIVE_X,
    GL_TEXTURE_CUBE_MAP_NEGATIVE_X,
    GL_TEXTURE_CUBE_MAP_POSITIVE_Y,
    GL_TEXTURE_CUBE_MAP_NEGATIVE_Y,
    GL_TEXTURE_CUBE_MAP_POSITIVE_Z,
    GL_TEXTURE_CUBE_MAP_NEGATIVE_Z,
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
    ctypes.c_uint8: OpenGL.GL.GL_UNSIGNED_BYTE,
    ctypes.c_int8: OpenGL.GL.GL_BYTE,
    ctypes.c_uint16: OpenGL.GL.GL_UNSIGNED_SHORT,
    ctypes.c_int16: OpenGL.GL.GL_SHORT,
    ctypes.c_uint32: OpenGL.GL.GL_UNSIGNED_INT,
    ctypes.c_int32: OpenGL.GL.GL_INT,
    ctypes.c_float: OpenGL.GL.GL_FLOAT,
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
    ctypes.c_uint8, ctypes.c_int8,
    ctypes.c_uint16, ctypes.c_int16,
    ctypes.c_uint32, ctypes.c_int32,
    ctypes.c_float
]


TEXTURE_DATA_TYPES_SORTED: Final = list(
    TEXTURE_DATA_TYPE_TO_GL_DATA_TYPE.keys()
)
TEXTURE_DATA_TYPES: Final = set(TEXTURE_DATA_TYPES_SORTED)
