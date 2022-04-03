
# gamut
from gamut.geometry import LineSegment2d
from gamut.math import Vector2, Vector3
# python
from typing import Any
# pytest
import pytest


def test_hash() -> None:
    l1 = LineSegment2d(Vector2(0), Vector2(1))
    l2 = LineSegment2d(Vector2(0), Vector2(1))
    assert hash(l1) != hash(l2)


def test_repr() -> None:
    line = LineSegment2d(Vector2(0, 1), Vector2(2, 3))
    assert (
        repr(line) ==
        f'<gamut.geometry.LineSegment2d (0.0, 1.0) to (2.0, 3.0)>'
    )

@pytest.mark.parametrize("a", [None, 'x', object(), Vector3(1)])
def test_invalid_a(a: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        LineSegment2d(a, Vector2(0))
    assert str(excinfo.value) == 'a must be Vector2'


@pytest.mark.parametrize("b", [None, 'x', object(), Vector3(1)])
def test_invalid_b(b: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        LineSegment2d(Vector2(0), b)
    assert str(excinfo.value) == 'b must be Vector2'


def test_points() -> None:
    line = LineSegment2d(Vector2(0, 1), Vector2(2, 3))
    assert line.a == Vector2(0, 1)
    assert line.b == Vector2(2, 3)


def test_equal() -> None:
    assert (
        LineSegment2d(Vector2(0), Vector2(0)) ==
        LineSegment2d(Vector2(0), Vector2(0))
    )
    assert (
        LineSegment2d(Vector2(0), Vector2(0)) !=
        LineSegment2d(Vector2(0, 1), Vector2(0))
    )
    assert (
        LineSegment2d(Vector2(0), Vector2(0)) !=
        LineSegment2d(Vector2(0), Vector2(1, 0))
    )
    assert LineSegment2d(Vector2(0), Vector2(0)) != object()


@pytest.mark.parametrize("l1, l2", [
    (
        LineSegment2d(Vector2(0, 0), Vector2(10, 10)),
        LineSegment2d(Vector2(0, 0), Vector2(10, 10))
    ),
    (
        LineSegment2d(Vector2(0, 0), Vector2(10, 10)),
        LineSegment2d(Vector2(-10, -10), Vector2(10, 10))
    ),
    (
        LineSegment2d(Vector2(0, 0), Vector2(10, 10)),
        LineSegment2d(Vector2(10, 0), Vector2(20, 10))
    ),
        (
        LineSegment2d(Vector2(0, 0), Vector2(10, 10)),
        LineSegment2d(Vector2(-1, -1), Vector2(-10, -10))
    ),
])
def test_intersection_none(l1: LineSegment2d, l2: LineSegment2d) -> None:
    assert l1.get_line_segment_intersection(l2) is None
    assert l2.get_line_segment_intersection(l1) is None


@pytest.mark.parametrize("l1, l2, intersection", [
    (
        LineSegment2d(Vector2(-5, -5), Vector2(5, 5)),
        LineSegment2d(Vector2(-5, 5), Vector2(5, -5)),
        (.5, .5)
    ),
    (
        LineSegment2d(Vector2(-5, -5), Vector2(5, 5)),
        LineSegment2d(Vector2(-5, 5), Vector2(0, 0)),
        (.5, 1.0)
    ),
    (
        LineSegment2d(Vector2(-15, -5), Vector2(-5, 5)),
        LineSegment2d(Vector2(-15, 5), Vector2(-5, -5)),
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


def test_point_along_line() -> None:
    line = LineSegment2d(Vector2(-5, -5), Vector2(5, 5))
    assert line.get_point_along_line(0) == Vector2(-5, -5)
    assert line.get_point_along_line(.25) == Vector2(-2.5, -2.5)
    assert line.get_point_along_line(.5) == Vector2(0)
    assert line.get_point_along_line(.75) == Vector2(2.5, 2.5)
    assert line.get_point_along_line(1) == Vector2(5, 5)
