
__all__ = ['create_quad_position_array', 'create_quad_uv_array']

# gamut
from ._shader import PrimitiveMode
# pyglm
from glm import array as glm_array
from glm import vec2, vec4


def create_quad_position_array(
    primitive_mode: PrimitiveMode,
    *,
    left: float = -1.0,
    right: float = 1.0,
    bottom: float = -1.0,
    top: float = 1.0,
    z: float = 0.0,
    w: float = 1.0,
) -> glm_array:
    if primitive_mode in (
        PrimitiveMode.POINT,
        PrimitiveMode.LINE_LOOP,
        PrimitiveMode.TRIANGLE_FAN,
    ):
        return glm_array(
            vec4(left, bottom, z, w),
            vec4(right, bottom, z, w),
            vec4(right, top, z, w),
            vec4(left, top, z, w),
        )
    elif primitive_mode == PrimitiveMode.LINE:
        return glm_array(
            vec4(left, bottom, z, w), vec4(right, bottom, z, w),
            vec4(right, bottom, z, w), vec4(right, top, z, w),
            vec4(right, top, z, w), vec4(left, top, z, w),
            vec4(left, top, z, w), vec4(left, bottom, z, w),
        )
    elif primitive_mode == PrimitiveMode.LINE_STRIP:
        return glm_array(
            vec4(left, bottom, z, w),
            vec4(right, bottom, z, w),
            vec4(right, top, z, w),
            vec4(left, top, z, w), vec4(left, bottom, z, w),
        )
    elif primitive_mode == PrimitiveMode.TRIANGLE:
        return glm_array(
            vec4(left, bottom, z, w),
            vec4(right, bottom, z, w),
            vec4(right, top, z, w),

            vec4(left, bottom, z, w),
            vec4(right, top, z, w),
            vec4(left, top, z, w),
        )
    elif primitive_mode == PrimitiveMode.TRIANGLE_STRIP:
        return glm_array(
            vec4(right, bottom, z, w),
            vec4(right, top, z, w),
            vec4(left, bottom, z, w),
            vec4(left, top, z, w),
        )
    assert False


def create_quad_uv_array(
    primitive_mode: PrimitiveMode,
    *,
    left: float = 0.0,
    right: float = 1.0,
    bottom: float = 0.0,
    top: float = 1.0,
) -> glm_array:
    if primitive_mode in (
        PrimitiveMode.POINT,
        PrimitiveMode.LINE_LOOP,
        PrimitiveMode.TRIANGLE_FAN,
    ):
        return glm_array(
            vec2(left, bottom),
            vec2(right, bottom),
            vec2(right, top),
            vec2(left, top),
        )
    elif primitive_mode == PrimitiveMode.LINE:
        return glm_array(
            vec2(left, bottom), vec2(right, bottom),
            vec2(right, bottom), vec2(right, top),
            vec2(right, top), vec2(left, top),
            vec2(left, top), vec2(left, bottom),
        )
    elif primitive_mode == PrimitiveMode.LINE_STRIP:
        return glm_array(
            vec2(left, bottom),
            vec2(right, bottom),
            vec2(right, top),
            vec2(left, top), vec2(left, bottom),
        )
    elif primitive_mode == PrimitiveMode.TRIANGLE:
        return glm_array(
            vec2(left, bottom), vec2(right, bottom), vec2(right, top),
            vec2(left, bottom), vec2(right, top), vec2(left, top),
        )
    elif primitive_mode == PrimitiveMode.TRIANGLE_STRIP:
        return glm_array(
            vec2(right, bottom),
            vec2(right, top),
            vec2(left, bottom),
            vec2(left, top),
        )
    assert False
