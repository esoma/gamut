
__all__ = ['create_quad_position_array', 'create_quad_uv_array']

# gamut
from ._shader import PrimitiveMode
# gamut
from gamut.math import FVector2, FVector2Array, FVector4, FVector4Array


def create_quad_position_array(
    primitive_mode: PrimitiveMode,
    *,
    left: float = -1.0,
    right: float = 1.0,
    bottom: float = -1.0,
    top: float = 1.0,
    z: float = 0.0,
    w: float = 1.0,
) -> FVector4Array:
    if primitive_mode in (
        PrimitiveMode.POINT,
        PrimitiveMode.LINE_LOOP,
        PrimitiveMode.TRIANGLE_FAN,
    ):
        return FVector4Array(
            FVector4(left, bottom, z, w),
            FVector4(right, bottom, z, w),
            FVector4(right, top, z, w),
            FVector4(left, top, z, w),
        )
    elif primitive_mode == PrimitiveMode.LINE:
        return FVector4Array(
            FVector4(left, bottom, z, w), FVector4(right, bottom, z, w),
            FVector4(right, bottom, z, w), FVector4(right, top, z, w),
            FVector4(right, top, z, w), FVector4(left, top, z, w),
            FVector4(left, top, z, w), FVector4(left, bottom, z, w),
        )
    elif primitive_mode == PrimitiveMode.LINE_STRIP:
        return FVector4Array(
            FVector4(left, bottom, z, w),
            FVector4(right, bottom, z, w),
            FVector4(right, top, z, w),
            FVector4(left, top, z, w), FVector4(left, bottom, z, w),
        )
    elif primitive_mode == PrimitiveMode.TRIANGLE:
        return FVector4Array(
            FVector4(left, bottom, z, w),
            FVector4(right, bottom, z, w),
            FVector4(right, top, z, w),

            FVector4(left, bottom, z, w),
            FVector4(right, top, z, w),
            FVector4(left, top, z, w),
        )
    elif primitive_mode == PrimitiveMode.TRIANGLE_STRIP:
        return FVector4Array(
            FVector4(right, bottom, z, w),
            FVector4(right, top, z, w),
            FVector4(left, bottom, z, w),
            FVector4(left, top, z, w),
        )
    assert False


def create_quad_uv_array(
    primitive_mode: PrimitiveMode,
    *,
    left: float = 0.0,
    right: float = 1.0,
    bottom: float = 0.0,
    top: float = 1.0,
) -> FVector2Array:
    if primitive_mode in (
        PrimitiveMode.POINT,
        PrimitiveMode.LINE_LOOP,
        PrimitiveMode.TRIANGLE_FAN,
    ):
        return FVector2Array(
            FVector2(left, bottom),
            FVector2(right, bottom),
            FVector2(right, top),
            FVector2(left, top),
        )
    elif primitive_mode == PrimitiveMode.LINE:
        return FVector2Array(
            FVector2(left, bottom), FVector2(right, bottom),
            FVector2(right, bottom), FVector2(right, top),
            FVector2(right, top), FVector2(left, top),
            FVector2(left, top), FVector2(left, bottom),
        )
    elif primitive_mode == PrimitiveMode.LINE_STRIP:
        return FVector2Array(
            FVector2(left, bottom),
            FVector2(right, bottom),
            FVector2(right, top),
            FVector2(left, top), FVector2(left, bottom),
        )
    elif primitive_mode == PrimitiveMode.TRIANGLE:
        return FVector2Array(
            FVector2(left, bottom),
            FVector2(right, bottom),
            FVector2(right, top),
            FVector2(left, bottom),
            FVector2(right, top),
            FVector2(left, top),
        )
    elif primitive_mode == PrimitiveMode.TRIANGLE_STRIP:
        return FVector2Array(
            FVector2(right, bottom),
            FVector2(right, top),
            FVector2(left, bottom),
            FVector2(left, top),
        )
    assert False
