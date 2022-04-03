
# gamut
from gamut.geometry import LineSegment3d
from gamut.math import Vector3, Vector4
# python
from typing import Any
# pytest
import pytest


def test_hash() -> None:
    l1 = LineSegment3d(Vector3(0), Vector3(1))
    l2 = LineSegment3d(Vector3(0), Vector3(1))
    assert hash(l1) != hash(l2)


def test_repr() -> None:
    line = LineSegment3d(Vector3(0, 1, 2), Vector3(3, 4, 5))
    assert (
        repr(line) ==
        f'<gamut.geometry.LineSegment3d (0.0, 1.0, 2.0) to (3.0, 4.0, 5.0)>'
    )

@pytest.mark.parametrize("a", [None, 'x', object(), Vector4(1)])
def test_invalid_a(a: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        LineSegment3d(a, Vector3(0))
    assert str(excinfo.value) == 'a must be Vector3'


@pytest.mark.parametrize("b", [None, 'x', object(), Vector4(1)])
def test_invalid_b(b: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        LineSegment3d(Vector3(0), b)
    assert str(excinfo.value) == 'b must be Vector3'


def test_points() -> None:
    line = LineSegment3d(Vector3(0, 1, 2), Vector3(3, 4, 5))
    assert line.a == Vector3(0, 1, 2)
    assert line.b == Vector3(3, 4, 5)


def test_equal() -> None:
    assert (
        LineSegment3d(Vector3(0), Vector3(0)) ==
        LineSegment3d(Vector3(0), Vector3(0))
    )
    assert (
        LineSegment3d(Vector3(0), Vector3(0)) !=
        LineSegment3d(Vector3(0, 1, 0), Vector3(0))
    )
    assert (
        LineSegment3d(Vector3(0), Vector3(0)) !=
        LineSegment3d(Vector3(0), Vector3(1, 0, 0))
    )
    assert LineSegment3d(Vector3(0), Vector3(0)) != object()


def test_point_along_line() -> None:
    line = LineSegment3d(Vector3(-5, -5, -5), Vector3(5, 5, 5))
    assert line.get_point_along_line(0) == Vector3(-5, -5, -5)
    assert line.get_point_along_line(.25) == Vector3(-2.5, -2.5, -2.5)
    assert line.get_point_along_line(.5) == Vector3(0)
    assert line.get_point_along_line(.75) == Vector3(2.5, 2.5, 2.5)
    assert line.get_point_along_line(1) == Vector3(5, 5, 5)
