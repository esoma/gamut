
# gamut
from gamut.geometry import DegenerateGeometryError, LineSegment3d, Triangle3d
from gamut.math import DVector3, DVector4, FVector3
# python
from math import isclose
from typing import Any
# pytest
import pytest


def vector3_is_close(a: Any, b: Any) -> bool:
    return (
        isclose(a.x, b.x, rel_tol=.00001) and
        isclose(a.y, b.y, rel_tol=.00001) and
        isclose(a.z, b.z, rel_tol=.00001)
    )


@pytest.mark.parametrize("vtype", [FVector3, DVector3])
def test_hash(vtype: Any) -> None:
    t = Triangle3d(vtype(0, 1, 2), vtype(1), vtype(2))
    assert hash(t) == hash(Triangle3d(vtype(0, 1, 2), vtype(1), vtype(2)))
    assert hash(t) == hash(Triangle3d(vtype(1), vtype(2), vtype(0, 1, 2)))
    assert hash(t) != hash(Triangle3d(vtype(1), vtype(0, 1, 2), vtype(2)))


@pytest.mark.parametrize("vtype", [FVector3, DVector3])
def test_repr(vtype: Any) -> None:
    line = Triangle3d(vtype(0, 1, 2), vtype(3, 4, 5), vtype(8, 6, 7))
    assert (
        repr(line) ==
        f'<gamut.geometry.Triangle3d '
        f'((0.0, 1.0, 2.0), (3.0, 4.0, 5.0), (8.0, 6.0, 7.0))>'
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
        assert tri.vector_type is vtype
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
        assert tri.vector_type is vtype
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
def test_equal(vtype: Any) -> None:
    assert (
        Triangle3d(vtype(0), vtype(1), vtype(0, 1, 2)) ==
        Triangle3d(vtype(0), vtype(1), vtype(0, 1, 2))
    )
    assert (
        Triangle3d(vtype(0), vtype(1), vtype(0, 1, 2)) !=
        Triangle3d(vtype(0, 1, 0), vtype(1), vtype(0))
    )
    assert (
        Triangle3d(vtype(0), vtype(1), vtype(0, 1, 2)) !=
        Triangle3d(vtype(1), vtype(1, 0, 0), vtype(0))
    )
    assert (
        Triangle3d(vtype(0), vtype(1), vtype(0, 1, 2)) !=
        Triangle3d(vtype(0), vtype(1), vtype(1, 0, 0))
    )
    assert (
        Triangle3d(vtype(0), vtype(1), vtype(0, 1, 2)) ==
        Triangle3d(vtype(0, 1, 2), vtype(0), vtype(1))
    )
    assert (
        Triangle3d(vtype(0, 1, 2), vtype(0), vtype(1)) ==
        Triangle3d(vtype(1), vtype(0, 1, 2), vtype(0))
    )
    assert (
        Triangle3d(vtype(0), vtype(0, 1, 2), vtype(1)) !=
        Triangle3d(vtype(1), vtype(0, 1, 2), vtype(0))
    )
    assert Triangle3d(vtype(0), vtype(0, 1, 2), vtype(1)) != object()

@pytest.mark.parametrize("vtype", [FVector3, DVector3])
def test_degenerate(vtype: Any) -> None:
    with pytest.raises(Triangle3d.DegenerateError) as excinfo:
        Triangle3d(vtype(0), vtype(0), vtype(0))
    assert str(excinfo.value).startswith('degenerate triangle')
    assert excinfo.value.degenerate_form == vtype(0)

    with pytest.raises(Triangle3d.DegenerateError) as excinfo:
        Triangle3d(vtype(0), vtype(1), vtype(0))
    assert str(excinfo.value).startswith('degenerate triangle')
    assert excinfo.value.degenerate_form == LineSegment3d(vtype(0), vtype(1))

    with pytest.raises(Triangle3d.DegenerateError) as excinfo:
        Triangle3d(vtype(0), vtype(1), vtype(2))
    assert str(excinfo.value).startswith('degenerate triangle')
    assert excinfo.value.degenerate_form == LineSegment3d(vtype(2), vtype(0))

def test_degenerate_error():
    assert issubclass(Triangle3d.DegenerateError, DegenerateGeometryError)

@pytest.mark.parametrize("vtype", [FVector3, DVector3])
def test_barycentric(vtype: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Triangle3d(vtype(0), vtype(1, 0, 0), vtype(0, 1, 0)
            ).get_projected_barycentric_point_from_cartesian(None)
    assert str(excinfo.value).startswith(
        f'cartesian_point must be {vtype}'
    )
    with pytest.raises(TypeError) as excinfo:
        Triangle3d(vtype(0), vtype(1, 0, 0), vtype(0, 1, 0)
            ).get_cartesian_point_from_barycentric(None)
    assert str(excinfo.value).startswith(
        f'barycentric_point must be {vtype}'
    )

    t = Triangle3d(vtype(0, 1, 0), vtype(1, 0, 0), vtype(0))

    bp = t.get_projected_barycentric_point_from_cartesian(vtype(0))
    assert bp == vtype(1, 0, 0)
    assert t.get_cartesian_point_from_barycentric(bp) == vtype(0)

    bp = t.get_projected_barycentric_point_from_cartesian(vtype(0, 1, 0))
    assert bp == vtype(0, 1, 0)
    assert t.get_cartesian_point_from_barycentric(bp) == vtype(0, 1, 0)

    bp = t.get_projected_barycentric_point_from_cartesian(vtype(1, 0, 0))
    assert bp == vtype(0, 0, 1)
    assert t.get_cartesian_point_from_barycentric(bp) == vtype(1, 0, 0)

    bp = t.get_projected_barycentric_point_from_cartesian(vtype(0, 0, 1))
    assert bp == vtype(1, 0, 0)
    assert t.get_cartesian_point_from_barycentric(bp) == vtype(0)

    bp = t.get_projected_barycentric_point_from_cartesian(t.center)
    assert vector3_is_close(bp, vtype(1 / 3, 1 / 3, 1 / 3))
    assert t.get_cartesian_point_from_barycentric(bp) == t.center

    bp = t.get_projected_barycentric_point_from_cartesian(vtype(-1, 2, 4))
    assert bp == vtype(0, 2, -1)
    assert t.get_cartesian_point_from_barycentric(bp) == vtype(-1, 2, 0)

@pytest.mark.parametrize("vtype", [FVector3, DVector3])
def test_where_intersected_by_point(vtype: Any) -> None:
    plane = Plane(-1, vtype(0, 1, 0))

    with pytest.raises(TypeError) as excinfo:
        plane.where_intersected_by_point(None)
    assert str(excinfo.value).startswith(f'point must be {vtype.__name__}')

    assert plane.where_intersected_by_point(vtype(0)) is None
    assert plane.where_intersected_by_point(
        vtype(0), tolerance=1) == vtype(0, 1, 0)
    assert plane.where_intersected_by_point(
        vtype(0, 1, 0)) == vtype(0, 1, 0)
