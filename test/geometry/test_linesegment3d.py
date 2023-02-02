from __future__ import annotations
# gamut
from gamut.geometry import DegenerateGeometryError, LineSegment3d
from gamut.math import DVector3, DVector4, FVector3
# python
from typing import Any
# pytest
import pytest


def test_hash() -> None:
    l1 = LineSegment3d(DVector3(0), DVector3(1))
    l2 = LineSegment3d(DVector3(0), DVector3(1))
    assert hash(l1) == hash(l2)
    l3 = LineSegment3d(FVector3(0), FVector3(1))
    assert hash(l1) != hash(l3)


@pytest.mark.parametrize("vtype", [FVector3, DVector3])
def test_repr(vtype: Any) -> None:
    line = LineSegment3d(vtype(0, 1, 2), vtype(3, 4, 5))
    assert (
        repr(line) ==
        f'<gamut.geometry.LineSegment3d (0.0, 1.0, 2.0) to (3.0, 4.0, 5.0)>'
    )


@pytest.mark.parametrize("a", [None, 'x', object(), DVector4(1)])
def test_invalid_a(a: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        LineSegment3d(a, DVector3(0))
    assert str(excinfo.value) == 'a must be FVector3 or DVector3'


@pytest.mark.parametrize("a, b", [
    (DVector3(0), None),
    (DVector3(0), 'x'),
    (DVector3(0), object()),
    (DVector3(0), DVector4(1)),
    (FVector3(0), DVector3(0)),
    (DVector3(0), FVector3(0)),
])
def test_invalid_b(a: Any, b: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        LineSegment3d(a, b)
    assert str(excinfo.value) == 'b must be the same type as a'


@pytest.mark.parametrize("point", [
    (0, 0, 0),
    (1.5, 2.0, -3.0),
    (2.0, 1.5, .876),
])
@pytest.mark.parametrize("vtype", [FVector3, DVector3])
def test_degenerate(
    point: tuple[float, float],
    vtype: type[FVector3] | type[DVector3]
) -> None:
    with pytest.raises(LineSegment3d.DegenerateError) as excinfo:
        LineSegment3d(vtype(*point), vtype(*point))
    assert str(excinfo.value) == 'degenerate line segment'
    assert excinfo.value.degenerate_form == vtype(*point)


def test_degenerate_error():
    assert issubclass(LineSegment3d.DegenerateError, DegenerateGeometryError)


@pytest.mark.parametrize("vtype", [FVector3, DVector3])
def test_points(vtype: Any) -> None:
    line = LineSegment3d(vtype(0, 1, 2), vtype(3, 4, 5))
    assert line.a == vtype(0, 1, 2)
    assert line.b == vtype(3, 4, 5)


@pytest.mark.parametrize("vtype", [FVector3, DVector3])
def test_equal(vtype: Any) -> None:
    assert (
        LineSegment3d(vtype(0), vtype(1)) ==
        LineSegment3d(vtype(0), vtype(1))
    )
    assert (
        LineSegment3d(vtype(0), vtype(1)) !=
        LineSegment3d(vtype(0, 1, 0), vtype(0))
    )
    assert (
        LineSegment3d(vtype(0), vtype(1)) !=
        LineSegment3d(vtype(0), vtype(1, 0, 0))
    )
    assert LineSegment3d(vtype(0), vtype(1)) != object()


@pytest.mark.parametrize("vtype", [FVector3, DVector3])
def test_point_along_line(vtype: Any) -> None:
    line = LineSegment3d(vtype(-5), vtype(5))
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
