
# gamut
from gamut.geometry import BoundingBox2d, LineSegment2d, Triangle2d
from gamut.math import DVector2, DVector4, FVector2
# python
from math import isclose, isnan
from typing import Any
# pytest
import pytest


def vector2_is_close(a: Any, b: Any) -> bool:
    return (
        isclose(a.x, b.x) and
        isclose(a.y, b.y)
    )


def test_hash() -> None:
    t = Triangle2d(DVector2(0), DVector2(1), DVector2(2))
    assert hash(t) == hash(Triangle2d(DVector2(0), DVector2(1), DVector2(2)))
    assert hash(t) == hash(Triangle2d(DVector2(1), DVector2(2), DVector2(0)))
    assert hash(t) != hash(Triangle2d(DVector2(1), DVector2(0), DVector2(2)))


@pytest.mark.parametrize("vtype", [FVector2, DVector2])
def test_repr(vtype: Any) -> None:
    line = Triangle2d(vtype(0, 1), vtype(3, 4), vtype(6, 7))
    assert (
        repr(line) ==
        f'<gamut.geometry.Triangle2d '
        f'((0.0, 1.0), (3.0, 4.0), (6.0, 7.0))>'
    )


@pytest.mark.parametrize("a", [None, 'x', object(), DVector4(1)])
def test_invalid_a(a: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Triangle2d(a, DVector2(0), DVector2(0))
    assert str(excinfo.value) == 'point 0 must be FVector2 or DVector2'


@pytest.mark.parametrize("a, b, c", [
    (DVector2(0), None, DVector2(0)),
    (DVector2(0), 'x', DVector2(0)),
    (DVector2(0), object(), DVector2(0)),
    (DVector2(0), DVector4(1), DVector2(0)),
    (FVector2(0), DVector2(0), FVector2(0)),
    (DVector2(0), FVector2(0), DVector2(0)),
])
def test_invalid_b(a: Any, b: Any, c: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Triangle2d(a, b, c)
    assert str(excinfo.value) == 'point 1 must be the same type as point 0'


@pytest.mark.parametrize("a, c, b", [
    (DVector2(0), None, DVector2(0)),
    (DVector2(0), 'x', DVector2(0)),
    (DVector2(0), object(), DVector2(0)),
    (DVector2(0), DVector4(1), DVector2(0)),
    (FVector2(0), DVector2(0), FVector2(0)),
    (DVector2(0), FVector2(0), DVector2(0)),
])
def test_invalid_c(a: Any, b: Any, c: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Triangle2d(a, b, c)
    assert str(excinfo.value) == 'point 2 must be the same type as point 0'


@pytest.mark.parametrize("vtype", [FVector2, DVector2])
def test_attributes(vtype: Any) -> None:
    for tri in [
        Triangle2d(vtype(0, 0), vtype(1, 0), vtype(1, 2)),
        Triangle2d(vtype(1, 0), vtype(1, 2), vtype(0, 0)),
        Triangle2d(vtype(1, 2), vtype(0, 0), vtype(1, 0)),
    ]:
        assert tri.is_clockwise
        assert not tri.is_counterclockwise
        assert tri.positions == (
            vtype(0, 0),
            vtype(1, 0),
            vtype(1, 2)
        )
        assert tri.center == sum((
            vtype(0, 0),
            vtype(1, 0),
            vtype(1, 2)
        )) / 3
        assert LineSegment2d(vtype(0, 0), vtype(1, 0)) == tri.edges[0]
        assert LineSegment2d(vtype(1, 0), vtype(1, 2)) == tri.edges[1]
        assert LineSegment2d(vtype(1, 2), vtype(0, 0)) == tri.edges[2]
        assert vtype(0, -1) == tri.edge_normals[0]
        assert vtype(1, 0) == tri.edge_normals[1]
        assert vtype(-2, 1).normalize()  == tri.edge_normals[2]

        assert tri.bounding_box.min == vtype(0, 0)
        assert tri.bounding_box.max == vtype(1, 2)

    for tri in [
        Triangle2d(vtype(1, 0), vtype(0, 0), vtype(1, 2)),
        Triangle2d(vtype(1, 2), vtype(1, 0), vtype(0, 0)),
        Triangle2d(vtype(0, 0), vtype(1, 2), vtype(1, 0)),
    ]:
        assert not tri.is_clockwise
        assert tri.is_counterclockwise
        assert tri.positions == (
            vtype(0, 0),
            vtype(1, 2),
            vtype(1, 0),
        )
        assert tri.center == sum((
            vtype(0, 0),
            vtype(1, 0),
            vtype(1, 2)
        )) / 3
        assert LineSegment2d(vtype(0, 0), vtype(1, 2)) == tri.edges[0]
        assert LineSegment2d(vtype(1, 2), vtype(1, 0)) == tri.edges[1]
        assert LineSegment2d(vtype(1, 0), vtype(0, 0)) == tri.edges[2]
        assert vtype(-2, 1).normalize() == tri.edge_normals[0]
        assert vtype(1, 0) == tri.edge_normals[1]
        assert vtype(0, -1) == tri.edge_normals[2]

        assert tri.bounding_box.min == vtype(0, 0)
        assert tri.bounding_box.max == vtype(1, 2)


@pytest.mark.parametrize("vtype", [FVector2, DVector2])
def test_degenerate(vtype: Any) -> None:
    assert Triangle2d(vtype(0), vtype(0), vtype(0)).is_degenerate
    assert Triangle2d(vtype(0), vtype(0), vtype(0)).degenerate_form == vtype(0)

    assert Triangle2d(vtype(0), vtype(1), vtype(0)).is_degenerate
    assert Triangle2d(vtype(0), vtype(0, 1), vtype(0)).degenerate_form == (
        LineSegment2d(vtype(0, 1), vtype(0))
    )

    assert Triangle2d(vtype(0), vtype(1), vtype(2)).is_degenerate
    assert Triangle2d(vtype(0), vtype(0, 1), vtype(0, 2)).degenerate_form == (
        LineSegment2d(vtype(0, 2), vtype(0))
    )

    assert not Triangle2d(vtype(0), vtype(0, 1), vtype(2)).is_degenerate
    assert Triangle2d(vtype(0), vtype(0, 1), vtype(2)).degenerate_form is None


@pytest.mark.parametrize("vtype", [FVector2, DVector2])
def test_equal(vtype: Any) -> None:
    assert (
        Triangle2d(vtype(0), vtype(0), vtype(0)) ==
        Triangle2d(vtype(0), vtype(0), vtype(0))
    )
    assert (
        Triangle2d(vtype(0), vtype(0), vtype(0)) !=
        Triangle2d(vtype(0, 1), vtype(0), vtype(0))
    )
    assert (
        Triangle2d(vtype(0), vtype(0), vtype(0)) !=
        Triangle2d(vtype(0), vtype(1, 0), vtype(0))
    )
    assert (
        Triangle2d(vtype(0), vtype(0), vtype(0)) !=
        Triangle2d(vtype(0), vtype(0), vtype(1, 0))
    )
    assert (
        Triangle2d(vtype(0), vtype(1), vtype(2)) ==
        Triangle2d(vtype(2), vtype(0), vtype(1))
    )
    assert (
        Triangle2d(vtype(2), vtype(0), vtype(1)) ==
        Triangle2d(vtype(1), vtype(2), vtype(0))
    )
    assert (
        Triangle2d(vtype(0), vtype(2), vtype(1)) !=
        Triangle2d(vtype(1), vtype(2), vtype(0))
    )
    assert Triangle2d(vtype(0), vtype(0), vtype(0)) != object()


@pytest.mark.parametrize("vtype", [FVector2, DVector2])
def test_intersects_point(vtype: Any) -> None:
    tri = Triangle2d(vtype(0), vtype(0), vtype(0))
    assert tri.intersects_point(vtype(0))
    assert not tri.intersects_point(vtype(1))
    assert tri.intersects_point(vtype(1, 0), tolerance=1)

    tri = Triangle2d(vtype(0), vtype(1, 0), vtype(0))
    assert tri.intersects_point(vtype(0))
    assert tri.intersects_point(vtype(.5, 0))
    assert tri.intersects_point(vtype(1, 0))
    assert not tri.intersects_point(vtype(2, 0))
    assert tri.intersects_point(vtype(2, 0), tolerance=1)

    tri = Triangle2d(vtype(0), vtype(1, 0), vtype(0, 1))
    assert tri.intersects_point(vtype(0))
    assert tri.intersects_point(vtype(1, 0))
    assert tri.intersects_point(vtype(0, 1))
    assert tri.intersects_point(vtype(.5, 0))
    assert tri.intersects_point(vtype(0, .5))
    assert tri.intersects_point(vtype(.25, .25))
    assert not tri.intersects_point(vtype(2, 0))
    assert tri.intersects_point(vtype(2, 0), tolerance=1)


@pytest.mark.parametrize("vtype", [FVector2, DVector2])
def test_intersects_triangle_2d(vtype: Any) -> None:
    assert(
        Triangle2d(
            vtype(0),
            vtype(0),
            vtype(0),
        ).intersects_triangle_2d(Triangle2d(
            vtype(0),
            vtype(0),
            vtype(0),
        ))
    )
    assert not (
        Triangle2d(
            vtype(0),
            vtype(0),
            vtype(0),
        ).intersects_triangle_2d(Triangle2d(
            vtype(1),
            vtype(1),
            vtype(1),
        ))
    )

    assert (
        Triangle2d(
            vtype(0),
            vtype(1),
            vtype(0),
        ).intersects_triangle_2d(Triangle2d(
            vtype(0),
            vtype(1),
            vtype(0),
        ))
    )
    assert not (
        Triangle2d(
            vtype(0),
            vtype(1),
            vtype(0),
        ).intersects_triangle_2d(Triangle2d(
            vtype(1, 0),
            vtype(2, 1),
            vtype(1, 0),
        ))
    )

    assert(
        not
        Triangle2d(
            vtype(1, 0),
            vtype(1, 1),
            vtype(0, 0),
        ).intersects_triangle_2d(Triangle2d(
            vtype(.4, .6),
            vtype(.5, 1),
            vtype(0, .5),
        ))
    )
    assert(
        Triangle2d(
            vtype(1, 0),
            vtype(1, 1),
            vtype(0, 0),
        ).intersects_triangle_2d(Triangle2d(
            vtype(.4, .6),
            vtype(.5, 1),
            vtype(0, .5),
        ),
            tolerance=.145
        )
    )
    assert(
        Triangle2d(
            vtype(1, 0),
            vtype(1, 1),
            vtype(0, 0),
        ).intersects_triangle_2d(Triangle2d(
            vtype(.5, .5),
            vtype(.5, 1),
            vtype(0, .5),
        ))
    )
    assert(
        Triangle2d(
            vtype(1, 0),
            vtype(1, 1),
            vtype(0, 0),
        ).intersects_triangle_2d(Triangle2d(
            vtype(.4, .6),
            vtype(1, 1),
            vtype(0, .5),
        ))
    )
    assert(
        Triangle2d(
            vtype(1, 0),
            vtype(1, 1),
            vtype(0, 0),
        ).intersects_triangle_2d(Triangle2d(
            vtype(.6, .4),
            vtype(1, .5),
            vtype(.5, 0),
        ))
    )
    assert(
        Triangle2d(
            vtype(1, 0),
            vtype(1, 1),
            vtype(0, 0),
        ).intersects_triangle_2d(Triangle2d(
            vtype(.65, .35),
            vtype(.85, .4),
            vtype(.6, .15),
        ))
    )
