
# gamut
from gamut.geometry import (BoundingBox3d, LineSegment3d, Plane, Triangle2d,
                            Triangle3d)
from gamut.math import (DMatrix4, DVector2, DVector3, DVector4, FMatrix4,
                        FVector2, FVector3)
# python
from math import isclose, isnan
from typing import Any
# pytest
import pytest


def vector3_is_close(a: Any, b: Any) -> bool:
    return (
        isclose(a.x, b.x) and
        isclose(a.y, b.y) and
        isclose(a.z, b.z)
    )


def test_hash() -> None:
    t = Triangle3d(DVector3(0), DVector3(1), DVector3(2))
    assert hash(t) == hash(Triangle3d(DVector3(0), DVector3(1), DVector3(2)))
    assert hash(t) == hash(Triangle3d(DVector3(1), DVector3(2), DVector3(0)))
    assert hash(t) != hash(Triangle3d(DVector3(1), DVector3(0), DVector3(2)))


@pytest.mark.parametrize("vtype", [FVector3, DVector3])
def test_repr(vtype: Any) -> None:
    line = Triangle3d(vtype(0, 1, 2), vtype(3, 4, 5), vtype(6, 7, 8))
    assert (
        repr(line) ==
        f'<gamut.geometry.Triangle3d '
        f'((0.0, 1.0, 2.0), (3.0, 4.0, 5.0), (6.0, 7.0, 8.0))>'
    )


@pytest.mark.parametrize("a", [None, 'x', object(), DVector4(1)])
def test_invalid_a(a: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Triangle3d(a, DVector3(0), DVector3(0))
    assert str(excinfo.value) == 'point 0 must be FVector3 or DVector3'


@pytest.mark.parametrize("a, b, c", [
    (DVector3(0), None, DVector3(0)),
    (DVector3(0), 'x', DVector3(0)),
    (DVector3(0), object(), DVector3(0)),
    (DVector3(0), DVector4(1), DVector3(0)),
    (FVector3(0), DVector3(0), FVector3(0)),
    (DVector3(0), FVector3(0), DVector3(0)),
])
def test_invalid_b(a: Any, b: Any, c: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Triangle3d(a, b, c)
    assert str(excinfo.value) == 'point 1 must be the same type as point 0'


@pytest.mark.parametrize("a, c, b", [
    (DVector3(0), None, DVector3(0)),
    (DVector3(0), 'x', DVector3(0)),
    (DVector3(0), object(), DVector3(0)),
    (DVector3(0), DVector4(1), DVector3(0)),
    (FVector3(0), DVector3(0), FVector3(0)),
    (DVector3(0), FVector3(0), DVector3(0)),
])
def test_invalid_c(a: Any, b: Any, c: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Triangle3d(a, b, c)
    assert str(excinfo.value) == 'point 2 must be the same type as point 0'


@pytest.mark.parametrize("vtype", [FVector3, DVector3])
def test_attributes(vtype: Any) -> None:
    for tri in [
        Triangle3d(vtype(0, 0, 0), vtype(1, 1, 0), vtype(1, 1, 2)),
        Triangle3d(vtype(1, 1, 0), vtype(1, 1, 2), vtype(0, 0, 0)),
        Triangle3d(vtype(1, 1, 2), vtype(0, 0, 0), vtype(1, 1, 0)),
    ]:
        assert tri.positions == (
            vtype(0, 0, 0),
            vtype(1, 1, 0),
            vtype(1, 1, 2)
        )
        assert tri.center == sum((
            vtype(0, 0, 0),
            vtype(1, 1, 0),
            vtype(1, 1, 2)
        )) / 3
        assert LineSegment3d(vtype(0, 0, 0), vtype(1, 1, 0)) in tri.edges
        assert LineSegment3d(vtype(1, 1, 0), vtype(1, 1, 2)) in tri.edges
        assert LineSegment3d(vtype(1, 1, 2), vtype(0, 0, 0)) in tri.edges

        assert tri.bounding_box.min == vtype(0, 0, 0)
        assert tri.bounding_box.max == vtype(1, 1, 2)

        d_edge_0 = tri.positions[1] - tri.positions[0]
        d_edge_1 = tri.positions[0] - tri.positions[2]
        assert tri.normal == -d_edge_0.cross(d_edge_1).normalize()

        assert tri.plane.normal == tri.normal / tri.normal.magnitude
        for i in range(3):
            assert tri.plane.distance == (
                (tri.normal @ tri.positions[i]) / tri.normal.magnitude
            )

    for tri in [
        Triangle3d(vtype(1, 1, 0), vtype(0, 0, 0), vtype(1, 1, 2)),
        Triangle3d(vtype(1, 1, 2), vtype(1, 1, 0), vtype(0, 0, 0)),
        Triangle3d(vtype(0, 0, 0), vtype(1, 1, 2), vtype(1, 1, 0)),
    ]:
        assert tri.positions == (
            vtype(0, 0, 0),
            vtype(1, 1, 2),
            vtype(1, 1, 0),
        )
        assert tri.center == sum((
            vtype(0, 0, 0),
            vtype(1, 1, 0),
            vtype(1, 1, 2)
        )) / 3
        assert LineSegment3d(vtype(1, 1, 0), vtype(0, 0, 0)) in tri.edges
        assert LineSegment3d(vtype(0, 0, 0), vtype(1, 1, 2)) in tri.edges
        assert LineSegment3d(vtype(1, 1, 2), vtype(1, 1, 0)) in tri.edges

        assert tri.bounding_box.min == vtype(0, 0, 0)
        assert tri.bounding_box.max == vtype(1, 1, 2)

        d_edge_0 = tri.positions[1] - tri.positions[0]
        d_edge_1 = tri.positions[0] - tri.positions[2]
        assert tri.normal == -d_edge_0.cross(d_edge_1).normalize()

        assert tri.plane.normal == tri.normal / tri.normal.magnitude
        for i in range(3):
            assert tri.plane.distance == (
                (tri.normal @ tri.positions[i]) / tri.normal.magnitude
            )


@pytest.mark.parametrize("vtype", [FVector3, DVector3])
def test_normals(vtype: Any) -> None:
    tri = Triangle3d(vtype(0, 0, 0), vtype(1, 1, 0), vtype(1, -1, 0))
    assert tri.normal == vtype(0, 0, -1)
    assert vector3_is_close(
        tri.edge_normals[0],
        vtype(-0.7071067811865475, 0.7071067811865475, 0)
    )
    assert vector3_is_close(tri.edge_normals[1], vtype(1, 0, 0))
    assert vector3_is_close(
        tri.edge_normals[2],
        vtype(-0.7071067811865475, -0.7071067811865475, 0)
    )

    tri = Triangle3d(vtype(0, 0, 0), vtype(1, -1, 0), vtype(1, 1, 0))
    assert tri.normal == vtype(0, 0, 1)
    assert vector3_is_close(
        tri.edge_normals[0],
        vtype(-0.7071067811865475, -0.7071067811865475, 0)
    )
    assert vector3_is_close(tri.edge_normals[1], vtype(1, 0, 0))
    assert vector3_is_close(
        tri.edge_normals[2],
        vtype(-0.7071067811865475, 0.7071067811865475, 0)
    )

    tri = Triangle3d(vtype(0, 0, 0), vtype(1, 0, 1), vtype(1, 0, -1))
    assert tri.normal == vtype(0, 1, 0)
    assert vector3_is_close(
        tri.edge_normals[0],
        vtype(-0.7071067811865475, 0, 0.7071067811865475)
    )
    assert vector3_is_close(tri.edge_normals[1], vtype(1, 0, 0))
    assert vector3_is_close(
        tri.edge_normals[2],
        vtype(-0.7071067811865475, 0, -0.7071067811865475)
    )


@pytest.mark.parametrize("vtype", [FVector3, DVector3])
def test_equal(vtype: Any) -> None:
    assert (
        Triangle3d(vtype(0), vtype(0), vtype(0)) ==
        Triangle3d(vtype(0), vtype(0), vtype(0))
    )
    assert (
        Triangle3d(vtype(0), vtype(0), vtype(0)) !=
        Triangle3d(vtype(0, 1, 0), vtype(0), vtype(0))
    )
    assert (
        Triangle3d(vtype(0), vtype(0), vtype(0)) !=
        Triangle3d(vtype(0), vtype(1, 0, 0), vtype(0))
    )
    assert (
        Triangle3d(vtype(0), vtype(0), vtype(0)) !=
        Triangle3d(vtype(0), vtype(0), vtype(1, 0, 0))
    )
    assert (
        Triangle3d(vtype(0), vtype(1), vtype(2)) ==
        Triangle3d(vtype(2), vtype(0), vtype(1))
    )
    assert (
        Triangle3d(vtype(2), vtype(0), vtype(1)) ==
        Triangle3d(vtype(1), vtype(2), vtype(0))
    )
    assert (
        Triangle3d(vtype(0), vtype(2), vtype(1)) !=
        Triangle3d(vtype(1), vtype(2), vtype(0))
    )
    assert Triangle3d(vtype(0), vtype(0), vtype(0)) != object()


@pytest.mark.parametrize("vtype", [FVector3, DVector3])
def test_degenerate(vtype: Any) -> None:
    t = Triangle3d(vtype(0), vtype(0), vtype(0))
    assert t.is_degenerate
    assert t.degenerate_form == vtype(0)

    t = Triangle3d(vtype(0), vtype(1), vtype(0))
    assert t.is_degenerate
    assert t.degenerate_form == LineSegment3d(vtype(0), vtype(1))

    t = Triangle3d(vtype(0), vtype(1), vtype(2))
    assert t.is_degenerate
    assert t.degenerate_form == LineSegment3d(vtype(2), vtype(0))

    t = Triangle3d(vtype(0), vtype(0, 1, 0), vtype(1, 0, 0))
    assert not t.is_degenerate
    assert t.degenerate_form is None


@pytest.mark.parametrize("vtype, vtype2", [
    [FVector3, FVector2],
    [DVector3, DVector2],
])
def test_project_orthographic(vtype: Any, vtype2: Any) -> None:
    with pytest.raises(Triangle3d.DegenerateError):
        Triangle3d(vtype(0), vtype(0), vtype(0)).project_orthographic()
    with pytest.raises(Triangle3d.DegenerateError):
        Triangle3d(vtype(0), vtype(1), vtype(0)).project_orthographic()
    with pytest.raises(Triangle3d.DegenerateError):
        Triangle3d(vtype(0), vtype(1), vtype(2)).project_orthographic()

    t2 = Triangle3d(
        vtype(0, 1, 10),
        vtype(0, 0, 15),
        vtype(0, 0, 3)
    ).project_orthographic()
    assert t2.positions == (
        vtype2(3, 0),
        vtype2(10, 1),
        vtype2(15, 0),
    )

    t2 = Triangle3d(
        vtype(1, 10, 0),
        vtype(0, 15, 0),
        vtype(0, 3, 0)
    ).project_orthographic()
    assert t2.positions == (
        vtype2(0, 3),
        vtype2(1, 10),
        vtype2(0, 15),
    )

    t2 = Triangle3d(
        vtype(1, 0, 10),
        vtype(0, 0, 15),
        vtype(0, 0, 3)
    ).project_orthographic()
    assert t2.positions == (
        vtype2(0, 3),
        vtype2(1, 10),
        vtype2(0, 15),
    )


@pytest.mark.parametrize("vtype", [FVector3, DVector3])
def test_intersects_point(vtype: Any) -> None:
    tri = Triangle3d(vtype(0), vtype(0), vtype(0))
    assert tri.intersects_point(vtype(0))
    assert not tri.intersects_point(vtype(1, 0, 0))
    assert not tri.intersects_point(vtype(0, 1, 0))
    assert not tri.intersects_point(vtype(0, 0, 1))
    assert not tri.intersects_point(vtype(1, 0, 0), tolerance=.99)
    assert not tri.intersects_point(vtype(0, 1, 0), tolerance=.99)
    assert not tri.intersects_point(vtype(0, 0, 1), tolerance=.99)
    assert tri.intersects_point(vtype(1, 0, 0), tolerance=1)
    assert tri.intersects_point(vtype(0, 1, 0), tolerance=1)
    assert tri.intersects_point(vtype(0, 0, 1), tolerance=1)

    tri = Triangle3d(vtype(0), vtype(1), vtype(2))
    assert tri.intersects_point(vtype(0))
    assert tri.intersects_point(vtype(1))
    assert tri.intersects_point(vtype(2))
    assert not tri.intersects_point(vtype(3))
    assert not tri.intersects_point(vtype(-1))
    assert tri.intersects_point(vtype(3), tolerance=1.733)
    assert tri.intersects_point(vtype(-1), tolerance=1.733)

    tri = Triangle3d(
        vtype(0),
        vtype(.5),
        vtype(1, .5, 0)
    )
    assert tri.intersects_point(vtype(0))
    assert tri.intersects_point(vtype(.5))
    assert tri.intersects_point(vtype(1, .5, 0))
    assert tri.intersects_point(vtype(.5, .25, 0), tolerance=.0001)
    assert tri.intersects_point(vtype(.25), tolerance=.0001)
    assert tri.intersects_point(vtype(.75, .5, .25), tolerance=.0001)
    assert tri.intersects_point(tri.center, tolerance=.0001)
    assert not tri.intersects_point(vtype(.504, .242, .004), tolerance=.0001)
    assert not tri.intersects_point(vtype(.254, .242, .254), tolerance=.0001)
    assert not tri.intersects_point(vtype(.754, .492, .254), tolerance=.0001)
    assert tri.intersects_point(vtype(.504, .242, .004), tolerance=.01)
    assert tri.intersects_point(vtype(.254, .242, .254), tolerance=.01)
    assert tri.intersects_point(vtype(.754, .492, .254), tolerance=.01)


@pytest.mark.parametrize("vtype", [FVector3, DVector3])
def test_intersects_line_segment(vtype: Any) -> None:
    tri = Triangle3d(vtype(0), vtype(0), vtype(0))
    assert tri.intersects_line_segment(LineSegment3d(vtype(0), vtype(1)))
    assert tri.intersects_line_segment(LineSegment3d(vtype(1), vtype(0)))
    assert not tri.intersects_line_segment(
        LineSegment3d(vtype(1, 0, 0), vtype(1))
    )
    assert not tri.intersects_line_segment(
        LineSegment3d(vtype(0, 1, 0), vtype(1))
    )
    assert not tri.intersects_line_segment(
        LineSegment3d(vtype(0, 0, 1), vtype(1))
    )
    assert not tri.intersects_line_segment(
        LineSegment3d(vtype(1, 0, 0), vtype(1)),
        tolerance=.999
    )
    assert not tri.intersects_line_segment(
        LineSegment3d(vtype(0, 1, 0), vtype(1)),
        tolerance=.999
    )
    assert not tri.intersects_line_segment(
        LineSegment3d(vtype(0, 0, 1), vtype(1)),
        tolerance=.999
    )
    assert tri.intersects_line_segment(
        LineSegment3d(vtype(1, 0, 0), vtype(1)),
        tolerance=1
    )
    assert tri.intersects_line_segment(
        LineSegment3d(vtype(0, 1, 0), vtype(1)),
        tolerance=1
    )
    assert tri.intersects_line_segment(
        LineSegment3d(vtype(0, 0, 1), vtype(1)),
        tolerance=1
    )

    tri = Triangle3d(
        vtype(1, 0, 0),
        vtype(1, 1, 0),
        vtype(0, 0, 0),
    )
    assert tri.intersects_line_segment(LineSegment3d(vtype(0), vtype(0)))
    assert not tri.intersects_line_segment(LineSegment3d(vtype(1), vtype(1)))
    assert not tri.intersects_line_segment(
        LineSegment3d(vtype(1), vtype(1)),
        tolerance=.999
    )
    assert tri.intersects_line_segment(
        LineSegment3d(vtype(1), vtype(1)),
        tolerance=1
    )
    assert tri.intersects_line_segment(
        LineSegment3d(vtype(1, 0, 0), vtype(1, 1, 0))
    )
    assert tri.intersects_line_segment(
        LineSegment3d(vtype(1, 1, 0), vtype(0))
    )
    assert tri.intersects_line_segment(
        LineSegment3d(vtype(1, 0, 0), vtype(0))
    )
    assert tri.intersects_line_segment(
        LineSegment3d(vtype(1.5, .5, 0), vtype(.5, -.5, 0))
    )
    assert tri.intersects_line_segment(
        LineSegment3d(vtype(.5, 1.5, 0), vtype(.5, -.5, 0))
    )
    assert tri.intersects_line_segment(
        LineSegment3d(vtype(1.5, .5, 0), vtype(-.5, .5, 0))
    )
    assert tri.intersects_line_segment(
        LineSegment3d(vtype(.5, -.5, 0), vtype(-.5, .5, 0))
    )
    assert not tri.intersects_line_segment(
        LineSegment3d(vtype(1.5, .5, 1), vtype(.5, -.5, 1))
    )
    assert not tri.intersects_line_segment(
        LineSegment3d(vtype(.5, 1.5, 1), vtype(.5, -.5, 1))
    )
    assert not tri.intersects_line_segment(
        LineSegment3d(vtype(1.5, .5, 1), vtype(-.5, .5, 1))
    )
    assert not tri.intersects_line_segment(
        LineSegment3d(vtype(1.5, .5, 1), vtype(.5, -.5, 1)),
        tolerance=.999
    )
    assert not tri.intersects_line_segment(
        LineSegment3d(vtype(.5, 1.5, 1), vtype(.5, -.5, 1)),
        tolerance=.999
    )
    assert not tri.intersects_line_segment(
        LineSegment3d(vtype(1.5, .5, 1), vtype(-.5, .5, 1)),
        tolerance=.999
    )
    assert tri.intersects_line_segment(
        LineSegment3d(vtype(1.5, .5, 1), vtype(.5, -.5, 1)),
        tolerance=1
    )
    assert tri.intersects_line_segment(
        LineSegment3d(vtype(.5, 1.5, 1), vtype(.5, -.5, 1)),
        tolerance=1
    )
    assert tri.intersects_line_segment(
        LineSegment3d(vtype(1.5, .5, 1), vtype(-.5, .5, 1)),
        tolerance=1
    )

    assert tri.intersects_line_segment(
        LineSegment3d(vtype(.5, .25, 0), vtype(.75, .5, 0)),
    )


@pytest.mark.parametrize("vtype", [FVector3, DVector3])
def test_intersects_triangle_3d(vtype: Any) -> None:
    assert(
        Triangle3d(
            vtype(0),
            vtype(0),
            vtype(0),
        ).intersects_triangle_3d(Triangle3d(
            vtype(0),
            vtype(0),
            vtype(0),
        ))
    )
    assert(
        Triangle3d(
            vtype(0),
            vtype(0),
            vtype(0),
        ).intersects_triangle_3d(Triangle3d(
            vtype(0),
            vtype(0),
            vtype(1),
        ))
    )
    assert(
        Triangle3d(
            vtype(0),
            vtype(0),
            vtype(1),
        ).intersects_triangle_3d(Triangle3d(
            vtype(0),
            vtype(0),
            vtype(0),
        ))
    )
    assert not (
        Triangle3d(
            vtype(0),
            vtype(0),
            vtype(0),
        ).intersects_triangle_3d(Triangle3d(
            vtype(1),
            vtype(1),
            vtype(1),
        ))
    )
    assert not (
        Triangle3d(
            vtype(1),
            vtype(1),
            vtype(1),
        ).intersects_triangle_3d(Triangle3d(
            vtype(0),
            vtype(0),
            vtype(0),
        ))
    )
    assert not (
        Triangle3d(
            vtype(0),
            vtype(0),
            vtype(0),
        ).intersects_triangle_3d(Triangle3d(
            vtype(1),
            vtype(1),
            vtype(1),
        ), tolerance=.999)
    )
    assert not (
        Triangle3d(
            vtype(1),
            vtype(1),
            vtype(1),
        ).intersects_triangle_3d(Triangle3d(
            vtype(0),
            vtype(0),
            vtype(0),
        ), tolerance=.999)
    )
    assert(
        Triangle3d(
            vtype(0),
            vtype(0),
            vtype(0),
        ).intersects_triangle_3d(Triangle3d(
            vtype(1),
            vtype(0),
            vtype(0),
        ), tolerance=1)
    )
    assert(
        Triangle3d(
            vtype(1),
            vtype(0),
            vtype(0),
        ).intersects_triangle_3d(Triangle3d(
            vtype(0),
            vtype(0),
            vtype(0),
        ), tolerance=1)
    )
    assert not (
        Triangle3d(
            vtype(0),
            vtype(0),
            vtype(0),
        ).intersects_triangle_3d(Triangle3d(
            vtype(1, 0, 0),
            vtype(1, 0, 0),
            vtype(1, 0, 0),
        ), tolerance=.999)
    )
    assert not (
        Triangle3d(
            vtype(1, 0, 0),
            vtype(1, 0, 0),
            vtype(1, 0, 0),
        ).intersects_triangle_3d(Triangle3d(
            vtype(0),
            vtype(0),
            vtype(0),
        ), tolerance=.999)
    )
    assert(
        Triangle3d(
            vtype(0),
            vtype(0),
            vtype(0),
        ).intersects_triangle_3d(Triangle3d(
            vtype(1, 0, 0),
            vtype(1, 0, 0),
            vtype(1, 0, 0),
        ), tolerance=1)
    )
    assert(
        Triangle3d(
            vtype(1, 0, 0),
            vtype(1, 0, 0),
            vtype(1, 0, 0),
        ).intersects_triangle_3d(Triangle3d(
            vtype(0),
            vtype(0),
            vtype(0),
        ), tolerance=1)
    )

    assert not (
        Triangle3d(
            vtype(1, 0, 0),
            vtype(1, 1, 0),
            vtype(0, 0, 0),
        ).intersects_triangle_3d(Triangle3d(
            vtype(.4, .6, 0),
            vtype(.5, 1, 0),
            vtype(0, .5, 0),
        ))
    )
    assert(
        Triangle3d(
            vtype(1, 0, 0),
            vtype(1, 1, 0),
            vtype(0, 0, 0),
        ).intersects_triangle_3d(Triangle3d(
            vtype(.4, .6, 0),
            vtype(.5, 1, 0),
            vtype(0, .5, 0),
        ), tolerance=.15)
    )

    assert not (
        Triangle3d(
            vtype(1, 0, 0),
            vtype(1, 1, 0),
            vtype(0, 0, 0),
        ).intersects_triangle_3d(Triangle3d(
            vtype(0, 1, 0),
            vtype(.4, .6, 0),
            vtype(0, 1, 0),
        ))
    )
    assert(
        Triangle3d(
            vtype(1, 0, 0),
            vtype(1, 1, 0),
            vtype(0, 0, 0),
        ).intersects_triangle_3d(Triangle3d(
            vtype(0, 1, 0),
            vtype(.4, .6, 0),
            vtype(0, 1, 0),
        ), tolerance=.15)
    )

    assert not (
        Triangle3d(
            vtype(1, 0, 0),
            vtype(1, 1, 0),
            vtype(0, 0, 0),
        ).intersects_triangle_3d(Triangle3d(
            vtype(.4, .6, 0),
            vtype(.4, .6, 0),
            vtype(.4, .6, 0),
        ))
    )
    assert(
        Triangle3d(
            vtype(1, 0, 0),
            vtype(1, 1, 0),
            vtype(0, 0, 0),
        ).intersects_triangle_3d(Triangle3d(
            vtype(.4, .6, 0),
            vtype(.4, .6, 0),
            vtype(.4, .6, 0),
        ), tolerance=.15)
    )

    assert (
        Triangle3d(
            vtype(1, 0, 0),
            vtype(1, 1, 0),
            vtype(0, 0, 0),
        ).intersects_triangle_3d(Triangle3d(
            vtype(0, 1, 0),
            vtype(.5, .5, 0),
            vtype(.5, .5, 1),
        ))
    )
    assert (
        Triangle3d(
            vtype(0, 1, 0),
            vtype(.5, .5, 0),
            vtype(.5, .5, 1),
        ).intersects_triangle_3d(Triangle3d(
            vtype(1, 0, 0),
            vtype(1, 1, 0),
            vtype(0, 0, 0),
        ))
    )

    assert (
        Triangle3d(
            vtype(1, 0, 0),
            vtype(1, 1, 0),
            vtype(0, 0, 0),
        ).intersects_triangle_3d(Triangle3d(
            vtype(.9, .1, 0),
            vtype(.6, .4, .5),
            vtype(.6, .4, 1),
        ))
    )
    assert (
        Triangle3d(
            vtype(.9, .1, 0),
            vtype(.6, .4, .5),
            vtype(.6, .4, 1),
        ).intersects_triangle_3d(Triangle3d(
            vtype(1, 0, 0),
            vtype(1, 1, 0),
            vtype(0, 0, 0),
        ))
    )

    assert not (
        Triangle3d(
            vtype(1, 0, 0),
            vtype(1, 1, 0),
            vtype(0, 0, 0),
        ).intersects_triangle_3d(Triangle3d(
            vtype(.9, .1, .1),
            vtype(.6, .4, .5),
            vtype(.6, .4, 1),
        ))
    )
    assert not (
        Triangle3d(
            vtype(.9, .1, .1),
            vtype(.6, .4, .5),
            vtype(.6, .4, 1),
        ).intersects_triangle_3d(Triangle3d(
            vtype(1, 0, 0),
            vtype(1, 1, 0),
            vtype(0, 0, 0),
        ))
    )

    assert (
        Triangle3d(
            vtype(1, 0, 0),
            vtype(1, 1, 0),
            vtype(0, 0, 0),
        ).intersects_triangle_3d(Triangle3d(
            vtype(.9, .1, .1),
            vtype(.6, .4, .5),
            vtype(.6, .4, 1),
        ), tolerance=.1001)
    )
    assert (
        Triangle3d(
            vtype(.9, .1, .1),
            vtype(.6, .4, .5),
            vtype(.6, .4, 1),
        ).intersects_triangle_3d(Triangle3d(
            vtype(1, 0, 0),
            vtype(1, 1, 0),
            vtype(0, 0, 0),
        ), tolerance=.1001)
    )

@pytest.mark.parametrize("vtype", [FVector3, DVector3])
def test_get_edge_for_points(vtype: Any) -> None:
    t = Triangle3d(vtype(0, 1, 0), vtype(1, 0, 0), vtype(1, 1, 0))
    for edge in t.edges:
        assert t.get_edge_for_points(edge.a, edge.b) == edge
        assert t.get_edge_for_points(edge.b, edge.a) == edge

    with pytest.raises(ValueError) as excinfo:
        assert t.get_edge_for_points(vtype(0, 1, 0), vtype(1, 1, 1))
    assert str(excinfo.value).startswith(
        'one or more points are not a position of the triangle'
    )

@pytest.mark.parametrize("vtype", [FVector3, DVector3])
def test_get_edge_opposite_of_point(vtype: Any) -> None:
    t = Triangle3d(vtype(0, 1, 0), vtype(1, 0, 0), vtype(1, 1, 0))

    for edge in t.edges:
        p = t.get_point_opposite_of_edge(edge)
        assert t.get_edge_opposite_of_point(p) == edge

    with pytest.raises(ValueError) as excinfo:
        assert t.get_edge_opposite_of_point(vtype(1, 1, 1))
    assert str(excinfo.value).startswith(
        'point is not a position of the triangle'
    )


@pytest.mark.parametrize("vtype", [FVector3, DVector3])
def test_get_edge_point_opposite_of_edge(vtype: Any) -> None:
    t = Triangle3d(vtype(0, 1, 0), vtype(1, 0, 0), vtype(1, 1, 0))

    assert t.get_point_opposite_of_edge(t.edges[0]) == t._positions[2]
    assert t.get_point_opposite_of_edge(t.edges[1]) == t._positions[0]
    assert t.get_point_opposite_of_edge(t.edges[2]) == t._positions[1]

    with pytest.raises(ValueError) as excinfo:
        assert t.get_point_opposite_of_edge(LineSegment3d(vtype(0), vtype(0)))
    assert str(excinfo.value).startswith(
        'edge is not an edge of the triangle'
    )


@pytest.mark.parametrize("vtype", [FVector3, DVector3])
def test_where_intersected_by_plane(vtype: Any) -> None:
    t = Triangle3d(vtype(1), vtype(1), vtype(1))

    with pytest.raises(TypeError) as excinfo:
        assert t.where_intersected_by_plane(None)
    assert str(excinfo.value).startswith(
        f'plane must be Plane[{vtype.__name__}]'
    )

    assert t.where_intersected_by_plane(
        Plane(-1, vtype(0, 1, 0))
    ) == vtype(1)
    assert t.where_intersected_by_plane(
        Plane(0, vtype(0, 1, 0))
    ) is None
    assert t.where_intersected_by_plane(
        Plane(0, vtype(0, 1, 0)),
        tolerance=1
    ) == vtype(1)

    t = Triangle3d(vtype(1), vtype(1), vtype(0, 1, 1))
    assert t.where_intersected_by_plane(
        Plane(-1, vtype(0, 1, 0))
    ) == LineSegment3d(vtype(0, 1, 1), vtype(1))
    assert t.where_intersected_by_plane(
        Plane(-2, vtype(0, 1, 0))
    ) is None
    assert t.where_intersected_by_plane(
        Plane(-2, vtype(0, 1, 0)),
        tolerance=1
    ) == LineSegment3d(vtype(0, 1, 1), vtype(1))

    t = Triangle3d(vtype(0, 2, 0), vtype(0, 2, 0), vtype(0, -2, 0))
    assert t.where_intersected_by_plane(
        Plane(-1, vtype(0, 1, 0))
    ) == vtype(0, 1, 0)