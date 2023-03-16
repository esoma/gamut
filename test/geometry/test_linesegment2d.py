from __future__ import annotations
# gamut
from gamut.geometry import DegenerateGeometryError, LineSegment2d
from gamut.math import DVector2, DVector3, FVector2
# python
from math import isclose
from typing import Any
# pytest
import pytest


def test_hash() -> None:
    l1 = LineSegment2d(DVector2(0), DVector2(1))
    l2 = LineSegment2d(DVector2(0), DVector2(1))
    assert hash(l1) == hash(l2)
    l3 = LineSegment2d(FVector2(0), FVector2(1))
    assert hash(l1) != hash(l3)


@pytest.mark.parametrize("vtype", [FVector2, DVector2])
def test_repr(vtype: Any) -> None:
    line = LineSegment2d(vtype(0, 1), vtype(2, 3))
    assert (
        repr(line) ==
        f'<gamut.geometry.LineSegment2d (0.0, 1.0) to (2.0, 3.0)>'
    )

@pytest.mark.parametrize("a", [None, 'x', object(), DVector3(1)])
def test_invalid_a(a: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        LineSegment2d(a, DVector2(0))
    assert str(excinfo.value) == 'a must be FVector2 or DVector2'


@pytest.mark.parametrize("a, b", [
    (DVector2(0), None),
    (DVector2(0), 'x'),
    (DVector2(0), object()),
    (DVector2(0), DVector3(1)),
    (FVector2(0), DVector2(0)),
    (DVector2(0), FVector2(0)),
])
def test_invalid_b(a: Any, b: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        LineSegment2d(a, b)
    assert str(excinfo.value) == 'b must be the same type as a'


@pytest.mark.parametrize("point", [
    (0, 0),
    (1.5, 2.0),
    (2.0, 1.5),
])
@pytest.mark.parametrize("vtype", [FVector2, DVector2])
def test_degenerate(
    point: tuple[float, float],
    vtype: type[FVector2] | type[DVector2]
) -> None:
    with pytest.raises(LineSegment2d.DegenerateError) as excinfo:
        LineSegment2d(vtype(*point), vtype(*point))
    assert str(excinfo.value) == 'degenerate line segment'
    assert excinfo.value.degenerate_form == vtype(*point)


def test_degenerate_error():
    assert issubclass(LineSegment2d.DegenerateError, DegenerateGeometryError)


@pytest.mark.parametrize("vtype", [FVector2, DVector2])
def test_attributes(vtype: Any) -> None:
    line = LineSegment2d(vtype(0, 1), vtype(2, 3))
    assert line.a == vtype(0, 1)
    assert line.b == vtype(2, 3)
    assert line.points == (line.a, line.b)
    assert line.slope == vtype(2, 3) - vtype(0, 1)


@pytest.mark.parametrize("vtype", [FVector2, DVector2])
def test_equal(vtype: Any) -> None:
    assert (
        LineSegment2d(vtype(0), vtype(1)) ==
        LineSegment2d(vtype(0), vtype(1))
    )
    assert (
        LineSegment2d(vtype(0), vtype(1)) !=
        LineSegment2d(vtype(0, 1), vtype(0))
    )
    assert (
        LineSegment2d(vtype(0), vtype(1)) !=
        LineSegment2d(vtype(0), vtype(1, 0))
    )
    assert LineSegment2d(vtype(0), vtype(1)) != object()


def test_distance_to_point_invalid() -> None:
    line = LineSegment2d(DVector2(-5, -5), DVector2(5, 5))
    with pytest.raises(TypeError) as ex:
        line.get_distance_to_point(FVector2(0))
    assert str(ex.value) == 'point must be DVector2'

    line = LineSegment2d(FVector2(-5, -5), FVector2(5, 5))
    with pytest.raises(TypeError) as ex:
        line.get_distance_to_point(DVector2(0))
    assert str(ex.value) == 'point must be FVector2'


@pytest.mark.parametrize("edge, point, distance", [
    (
        LineSegment2d(DVector2(0, 0), DVector2(10, 10)),
        DVector2(0, 0),
        0
    ),
    (
        LineSegment2d(DVector2(0, 0), DVector2(10, 10)),
        DVector2(10, 10),
        0
    ),
    (
        LineSegment2d(DVector2(0, 0), DVector2(10, 10)),
        DVector2(5, 5),
        0
    ),
    (
        LineSegment2d(DVector2(0, 0), DVector2(10, 10)),
        DVector2(0, 10),
        7.0710678118654755
    ),
])
def test_distance_to_point(
    edge: LineSegment2d,
    point: Any,
    distance: float
) -> None:
    assert isclose(edge.get_distance_to_point(point), distance)


def test_intersection_invalid() -> None:
    line = LineSegment2d(DVector2(0, 0), DVector2(10, 10))
    with pytest.raises(TypeError) as ex:
        line.get_line_segment_intersection(None)
    assert str(ex.value) == 'other must be LineSegment2d'


@pytest.mark.parametrize("l1, l2", [
    (
        LineSegment2d(DVector2(0, 0), DVector2(10, 10)),
        LineSegment2d(DVector2(0, 0), DVector2(10, 10))
    ),
    (
        LineSegment2d(DVector2(0, 0), DVector2(10, 10)),
        LineSegment2d(DVector2(-10, -10), DVector2(10, 10))
    ),
    (
        LineSegment2d(DVector2(0, 0), DVector2(10, 10)),
        LineSegment2d(DVector2(10, 0), DVector2(20, 10))
    ),
        (
        LineSegment2d(DVector2(0, 0), DVector2(10, 10)),
        LineSegment2d(DVector2(-1, -1), DVector2(-10, -10))
    ),
])
def test_intersection_none(l1: LineSegment2d, l2: LineSegment2d) -> None:
    assert l1.get_line_segment_intersection(l2) is None
    assert l2.get_line_segment_intersection(l1) is None


@pytest.mark.parametrize("l1, l2, intersection", [
    (
        LineSegment2d(DVector2(-5, -5), DVector2(5, 5)),
        LineSegment2d(DVector2(-5, 5), DVector2(5, -5)),
        (.5, .5)
    ),
    (
        LineSegment2d(DVector2(-5, -5), DVector2(5, 5)),
        LineSegment2d(DVector2(-5, 5), DVector2(0, 0)),
        (.5, 1.0)
    ),
    (
        LineSegment2d(DVector2(-15, -5), DVector2(-5, 5)),
        LineSegment2d(DVector2(-15, 5), DVector2(-5, -5)),
        (.5, .5)
    ),
    (
        LineSegment2d(FVector2(-5, -5), FVector2(5, 5)),
        LineSegment2d(FVector2(-5, 5), FVector2(5, -5)),
        (.5, .5)
    ),
    (
        LineSegment2d(FVector2(-5, -5), FVector2(5, 5)),
        LineSegment2d(FVector2(-5, 5), FVector2(0, 0)),
        (.5, 1.0)
    ),
    (
        LineSegment2d(FVector2(-15, -5), FVector2(-5, 5)),
        LineSegment2d(FVector2(-15, 5), FVector2(-5, -5)),
        (.5, .5)
    ),
])
def test_intersection(
    l1: LineSegment2d,
    l2: LineSegment2d,
    intersection: tuple[float, float]
) -> None:
    t, s = l1.get_line_segment_intersection(l2)
    assert intersection[0] == t
    assert intersection[1] == s

    t, s = l2.get_line_segment_intersection(l1)
    assert intersection[0] == s
    assert intersection[1] == t


@pytest.mark.parametrize("vtype", [FVector2, DVector2])
def test_get_point(vtype: Any) -> None:
    line = LineSegment2d(vtype(-5), vtype(5))
    assert line.get_point_from_a_to_b(0) == vtype(-5)
    assert line.get_point_from_a_to_b(.25) == vtype(-2.5)
    assert line.get_point_from_a_to_b(.5) == vtype(0)
    assert line.get_point_from_a_to_b(.75) == vtype(2.5)
    assert line.get_point_from_a_to_b(1) == vtype(5)
    assert line.get_point_from_a_to_b(2) == vtype(15)
    assert line.get_point_from_a_to_b(-1) == vtype(-15)

    assert line.get_point_from_b_to_a(0) == vtype(5)
    assert line.get_point_from_b_to_a(.25) == vtype(2.5)
    assert line.get_point_from_b_to_a(.5) == vtype(0)
    assert line.get_point_from_b_to_a(.75) == vtype(-2.5)
    assert line.get_point_from_b_to_a(1) == vtype(-5)
    assert line.get_point_from_b_to_a(2) == vtype(-15)
    assert line.get_point_from_b_to_a(-1) == vtype(15)
