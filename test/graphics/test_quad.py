
# gamut
from gamut.graphics import (create_quad_position_array, create_quad_uv_array,
                            PrimitiveMode)
# python
from typing import Any
# pyglm
from glm import vec2, vec4
# pytest
import pytest


@pytest.mark.parametrize("primitive_mode", list(PrimitiveMode))
@pytest.mark.parametrize("left", [None, 11.5])
@pytest.mark.parametrize("right", [None, 12.6])
@pytest.mark.parametrize("bottom", [None, 13.7])
@pytest.mark.parametrize("top", [None, 14.8])
@pytest.mark.parametrize("z", [None, 15.9])
@pytest.mark.parametrize("w", [None, 16.1])
def test_position(
    primitive_mode: PrimitiveMode,
    left: Any, right: Any,
    bottom: Any, top: Any,
    z: Any, w: Any,
) -> None:
    kwargs: dict[str, float] = {}
    if left is not None:
        kwargs["left"] = left
    else:
        left = -1.0
    if right is not None:
        kwargs["right"] = right
    else:
        right = 1.0
    if bottom is not None:
        kwargs["bottom"] = bottom
    else:
        bottom = -1.0
    if top is not None:
        kwargs["top"] = top
    else:
        top = 1.0
    if z is not None:
        kwargs["z"] = z
    else:
        z = 0.0
    if w is not None:
        kwargs["w"] = w
    else:
        w = 1.0
    array = create_quad_position_array(primitive_mode, **kwargs)
    if primitive_mode in (
        PrimitiveMode.POINT,
        PrimitiveMode.LINE_LOOP,
        PrimitiveMode.TRIANGLE_FAN,
    ):
        assert len(array) == 4
        assert array[0] == vec4(left, bottom, z, w)
        assert array[1] == vec4(right, bottom, z, w)
        assert array[2] == vec4(right, top, z, w)
        assert array[3] == vec4(left, top, z, w)
    elif primitive_mode == PrimitiveMode.LINE:
        assert len(array) == 8
        assert array[0] == vec4(left, bottom, z, w)
        assert array[1] == vec4(right, bottom, z, w)
        assert array[2] == vec4(right, bottom, z, w)
        assert array[3] == vec4(right, top, z, w)
        assert array[4] == vec4(right, top, z, w)
        assert array[5] == vec4(left, top, z, w)
        assert array[6] == vec4(left, top, z, w)
        assert array[7] == vec4(left, bottom, z, w)
    elif primitive_mode == PrimitiveMode.LINE_STRIP:
        assert len(array) == 5
        assert array[0] == vec4(left, bottom, z, w)
        assert array[1] == vec4(right, bottom, z, w)
        assert array[2] == vec4(right, top, z, w)
        assert array[3] == vec4(left, top, z, w)
        assert array[4] == vec4(left, bottom, z, w)
    elif primitive_mode == PrimitiveMode.TRIANGLE:
        assert len(array) == 6
        assert array[0] == vec4(left, bottom, z, w)
        assert array[1] == vec4(right, bottom, z, w)
        assert array[2] == vec4(right, top, z, w)
        assert array[3] == vec4(left, bottom, z, w)
        assert array[4] == vec4(right, top, z, w)
        assert array[5] == vec4(left, top, z, w)
    elif primitive_mode == PrimitiveMode.TRIANGLE_STRIP:
        assert len(array) == 4
        assert array[0] == vec4(right, bottom, z, w)
        assert array[1] == vec4(right, top, z, w)
        assert array[2] == vec4(left, bottom, z, w)
        assert array[3] == vec4(left, top, z, w)


@pytest.mark.parametrize("primitive_mode", list(PrimitiveMode))
@pytest.mark.parametrize("left", [None, 11.5])
@pytest.mark.parametrize("right", [None, 12.6])
@pytest.mark.parametrize("bottom", [None, 13.7])
@pytest.mark.parametrize("top", [None, 14.8])
def test_uv(
    primitive_mode: PrimitiveMode,
    left: Any, right: Any,
    bottom: Any, top: Any,
) -> None:
    kwargs: dict[str, float] = {}
    if left is not None:
        kwargs["left"] = left
    else:
        left = 0.0
    if right is not None:
        kwargs["right"] = right
    else:
        right = 1.0
    if bottom is not None:
        kwargs["bottom"] = bottom
    else:
        bottom = 0.0
    if top is not None:
        kwargs["top"] = top
    else:
        top = 1.0
    array = create_quad_uv_array(primitive_mode, **kwargs)
    if primitive_mode in (
        PrimitiveMode.POINT,
        PrimitiveMode.LINE_LOOP,
        PrimitiveMode.TRIANGLE_FAN,
    ):
        assert len(array) == 4
        assert array[0] == vec2(left, bottom)
        assert array[1] == vec2(right, bottom)
        assert array[2] == vec2(right, top)
        assert array[3] == vec2(left, top)
    elif primitive_mode == PrimitiveMode.LINE:
        assert len(array) == 8
        assert array[0] == vec2(left, bottom)
        assert array[1] == vec2(right, bottom)
        assert array[2] == vec2(right, bottom)
        assert array[3] == vec2(right, top)
        assert array[4] == vec2(right, top)
        assert array[5] == vec2(left, top)
        assert array[6] == vec2(left, top)
        assert array[7] == vec2(left, bottom)
    elif primitive_mode == PrimitiveMode.LINE_STRIP:
        assert len(array) == 5
        assert array[0] == vec2(left, bottom)
        assert array[1] == vec2(right, bottom)
        assert array[2] == vec2(right, top)
        assert array[3] == vec2(left, top)
        assert array[4] == vec2(left, bottom)
    elif primitive_mode == PrimitiveMode.TRIANGLE:
        assert len(array) == 6
        assert array[0] == vec2(left, bottom)
        assert array[1] == vec2(right, bottom)
        assert array[2] == vec2(right, top)
        assert array[3] == vec2(left, bottom)
        assert array[4] == vec2(right, top)
        assert array[5] == vec2(left, top)
    elif primitive_mode == PrimitiveMode.TRIANGLE_STRIP:
        assert len(array) == 4
        assert array[0] == vec2(right, bottom)
        assert array[1] == vec2(right, top)
        assert array[2] == vec2(left, bottom)
        assert array[3] == vec2(left, top)
