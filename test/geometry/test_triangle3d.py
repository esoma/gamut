
# gamut
from gamut.geometry import BoundingBox3d, LineSegment3d, Plane, Triangle3d
from gamut.math import DVector3, DVector4, FVector3
# python
from math import isclose
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
def test_intersects_triangle_3d(vtype: Any) -> None:
    assert(
        not
        Triangle3d(
            vtype(0),
            vtype(0),
            vtype(0),
        ).intersects_triangle_3d(Triangle3d(
            vtype(0),
            vtype(0),
            vtype(0),
        ),
            tolerance=.01
        )
    )

    t = Triangle3d(
            vtype(1, 0, 0),
            vtype(1, 1, 0),
            vtype(0, 0, 0),
        )
    print(t.project_ortho())

    assert(
        not
        Triangle3d(
            vtype(1, 0, 0),
            vtype(1, 1, 0),
            vtype(0, 0, 0),
        ).intersects_triangle_3d(Triangle3d(
            vtype(.4, .6, 0),
            vtype(.5, 1, 0),
            vtype(0, .5, 0),
        ),
            tolerance=.01
        )
    )
    assert False
