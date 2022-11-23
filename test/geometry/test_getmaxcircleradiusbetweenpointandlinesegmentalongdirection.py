
# gamut
from gamut.geometry import (
    get_max_circle_radius_between_point_and_line_segment_along_direction,
    LineSegment2d)
from gamut.math import DVector2, FVector2
# python
from math import isclose, isinf
from typing import Any
# pytest
import pytest


def test_invalid_args():
    f = get_max_circle_radius_between_point_and_line_segment_along_direction
    with pytest.raises(TypeError) as ex:
        f(
            None,
            LineSegment2d(DVector2(0), DVector2(0)),
            DVector2(0)
        )
    assert str(ex.value) == 'point must be FVector2 or DVector2'

    with pytest.raises(TypeError) as ex:
        f(
            FVector2(0),
            LineSegment2d(DVector2(0), DVector2(0)),
            FVector2(0)
        )
    assert str(ex.value) == 'line segment must be composed of FVector2'

    with pytest.raises(TypeError) as ex:
        f(
            DVector2(0),
            LineSegment2d(FVector2(0), FVector2(0)),
            DVector2(0)
        )
    assert str(ex.value) == 'line segment must be composed of DVector2'

    with pytest.raises(TypeError) as ex:
        f(
            FVector2(0),
            LineSegment2d(FVector2(0), FVector2(0)),
            DVector2(0)
        )
    assert str(ex.value) == 'direction must be FVector2'

    with pytest.raises(TypeError) as ex:
        f(
            DVector2(0),
            LineSegment2d(DVector2(0), DVector2(0)),
            FVector2(0)
        )
    assert str(ex.value) == 'direction must be DVector2'


@pytest.mark.parametrize("point, line_segment, direction, distance", [
    (
        DVector2(1, 2),
        LineSegment2d(DVector2(0, 0), DVector2(2, 0)),
        DVector2(1, -1),
        1.17157287525381,
    ),
    (
        DVector2(1, 2),
        LineSegment2d(DVector2(0, 0), DVector2(2, 0)),
        DVector2(0, -1),
        1,
    ),
    (
        DVector2(1, 2),
        LineSegment2d(DVector2(0, 0), DVector2(2, 0)),
        DVector2(1, 0),
        2,
    ),
    (
        FVector2(1, 2),
        LineSegment2d(FVector2(0, 0), FVector2(0, 2)),
        FVector2(-1, -1),
        0.5857864417795234,
    ),
    (
        FVector2(1, 2),
        LineSegment2d(FVector2(0, 0), FVector2(0, 2)),
        FVector2(-.5, 1),
        0.6909830081817645,
    ),
])
def test_result(
    point: Any,
    line_segment: Any,
    direction: Any,
    distance: float
) -> None:
    f = get_max_circle_radius_between_point_and_line_segment_along_direction
    assert isclose(f(point, line_segment, direction), distance)


@pytest.mark.parametrize("point, line_segment, direction", [
    (
        DVector2(1, 2),
        LineSegment2d(DVector2(0, 0), DVector2(2, 0)),
        DVector2(0, 1),
    ),
    (
        DVector2(1, 2),
        LineSegment2d(DVector2(0, 0), DVector2(2, 0)),
        DVector2(1, 1),
    ),
    (
        DVector2(1, 2),
        LineSegment2d(DVector2(0, 0), DVector2(2, 0)),
        DVector2(-1, 1),
    ),
])
def test_inf(
    point: Any,
    line_segment: Any,
    direction: Any,
) -> None:
    f = get_max_circle_radius_between_point_and_line_segment_along_direction
    assert isinf(f(point, line_segment, direction))
