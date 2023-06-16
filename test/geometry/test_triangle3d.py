
# gamut
from gamut.geometry import (DegenerateGeometryError, LineSegment3d, Triangle2d,
                            Triangle3d)
from gamut.math import DVector2, DVector3, DVector4, FVector2, FVector3
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
def test_normals(vtype: Any) -> None:
    tri = Triangle3d(vtype(0, 0, 0), vtype(1, 1, 0), vtype(1, -1, 0))
    assert tri.normal == vtype(0, 0, -1)
    assert vector3_is_close(
        tri.edge_normals[0],
        vtype(-0.7071067811865475, 0.7071067811865475, 0)
    )
    assert tri.get_edge_normal(tri.edges[0]) == (
        vtype(-0.7071067811865475, 0.7071067811865475, 0)
    )
    assert vector3_is_close(tri.edge_normals[1], vtype(1, 0, 0))
    assert tri.get_edge_normal(tri.edges[1]) == vtype(1, 0, 0)
    assert vector3_is_close(
        tri.edge_normals[2],
        vtype(-0.7071067811865475, -0.7071067811865475, 0)
    )
    assert tri.get_edge_normal(tri.edges[2]) == (
        vtype(-0.7071067811865475, -0.7071067811865475, 0)
    )

    tri = Triangle3d(vtype(0, 0, 0), vtype(1, -1, 0), vtype(1, 1, 0))
    assert tri.normal == vtype(0, 0, 1)
    assert vector3_is_close(
        tri.edge_normals[0],
        vtype(-0.7071067811865475, -0.7071067811865475, 0)
    )
    assert tri.get_edge_normal(tri.edges[0]) == (
        vtype(-0.7071067811865475, -0.7071067811865475, 0)
    )
    assert vector3_is_close(tri.edge_normals[1], vtype(1, 0, 0))
    assert tri.get_edge_normal(tri.edges[1]) == vtype(1, 0, 0)
    assert vector3_is_close(
        tri.edge_normals[2],
        vtype(-0.7071067811865475, 0.7071067811865475, 0)
    )
    assert tri.get_edge_normal(tri.edges[2]) == (
        vtype(-0.7071067811865475, 0.7071067811865475, 0)
    )

    tri = Triangle3d(vtype(0, 0, 0), vtype(1, 0, 1), vtype(1, 0, -1))
    assert tri.normal == vtype(0, 1, 0)
    assert vector3_is_close(
        tri.edge_normals[0],
        vtype(-0.7071067811865475, 0, 0.7071067811865475)
    )
    assert tri.get_edge_normal(tri.edges[0]) == (
        vtype(-0.7071067811865475, 0, 0.7071067811865475)
    )
    assert vector3_is_close(tri.edge_normals[1], vtype(1, 0, 0))
    assert tri.get_edge_normal(tri.edges[1]) == vtype(1, 0, 0)
    assert vector3_is_close(
        tri.edge_normals[2],
        vtype(-0.7071067811865475, 0, -0.7071067811865475)
    )
    assert tri.get_edge_normal(tri.edges[2]) == (
        vtype(-0.7071067811865475, 0, -0.7071067811865475)
    )

    with pytest.raises(ValueError) as excinfo:
        tri.get_edge_normal(LineSegment3d(vtype(0), vtype(1)))
    assert str(excinfo.value).startswith('edge is not part of triangle')

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

    assert t.get_point_opposite_of_edge(t.edges[0]) == t.positions[2]
    assert t.get_point_opposite_of_edge(t.edges[1]) == t.positions[0]
    assert t.get_point_opposite_of_edge(t.edges[2]) == t.positions[1]

    with pytest.raises(ValueError) as excinfo:
        assert t.get_point_opposite_of_edge(LineSegment3d(vtype(0), vtype(2)))
    assert str(excinfo.value).startswith(
        'edge is not an edge of the triangle'
    )

@pytest.mark.parametrize("vtype", [FVector3, DVector3])
def test_get_edges_for_point(vtype: Any) -> None:
    t = Triangle3d(vtype(0, 1, 0), vtype(1, 0, 0), vtype(1, 1, 0))

    assert t.get_edges_for_point(t.positions[0]) == (
        t.edges[2],
        t.edges[0]
    )
    assert t.get_edges_for_point(t.positions[1]) == (
        t.edges[0],
        t.edges[1]
    )
    assert t.get_edges_for_point(t.positions[2]) == (
        t.edges[1],
        t.edges[2]
    )

    with pytest.raises(ValueError) as excinfo:
        assert t.get_edges_for_point(vtype(1, 1, 1))
    assert str(excinfo.value).startswith(
        'point is not a position of the triangle'
    )

@pytest.mark.parametrize("vtype, vtype2", [
    [FVector3, FVector2],
    [DVector3, DVector2],
])
def test_project_orthographic(vtype: Any, vtype2: Any) -> None:
    t2 = Triangle3d(
        vtype(0, 1, 10),
        vtype(0, 0, 15),
        vtype(0, 0, 3)
    ).project_orthographic()
    assert isinstance(t2, Triangle2d)
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
    assert isinstance(t2, Triangle2d)
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
    assert isinstance(t2, Triangle2d)
    assert t2.positions == (
        vtype2(0, 3),
        vtype2(1, 10),
        vtype2(0, 15),
    )

@pytest.mark.parametrize("vtype", [FVector3, DVector3])
def test_where_intersected_by_point(vtype: Any) -> None:
    t = Triangle3d(
        vtype(0),
        vtype(.5),
        vtype(1, .5, 0)
    )

    with pytest.raises(TypeError) as excinfo:
        assert t.where_intersected_by_point(None)
    assert str(excinfo.value).startswith(f'point must be {vtype.__name__}')

    assert t.where_intersected_by_point(vtype(0)) == vtype(0)
    assert t.where_intersected_by_point(vtype(.5)) == vtype(.5)
    assert t.where_intersected_by_point(vtype(1, .5, 0)) == vtype(1, .5, 0)

    assert t.where_intersected_by_point(vtype(.5, .25, 0)) == vtype(.5, .25, 0)
    assert t.where_intersected_by_point(vtype(.25)) == vtype(.25)
    assert (
        t.where_intersected_by_point(vtype(.75, .5, .25), tolerance=.00001) ==
        vtype(.75, .5, .25)
    )

    assert vector3_is_close(
        t.where_intersected_by_point(t.center, tolerance=.000001),
        t.center
    )

    assert t.where_intersected_by_point(
        vtype(.504, .242, .004),
        tolerance=.0001
    ) is None
    assert t.where_intersected_by_point(
        vtype(.254, .242, .254),
        tolerance=.0001
    ) is None
    assert t.where_intersected_by_point(
        vtype(.754, .492, .254),
        tolerance=.0001
    ) is None

    assert (
        t.where_intersected_by_point(vtype(.504, .242, .004), tolerance=.01) ==
        vtype(.5, .25, 0)
    )
    assert (
        t.where_intersected_by_point(vtype(.254, .242, .254), tolerance=.01) ==
        vtype(.25)
    )
    assert (
        t.where_intersected_by_point(vtype(.754, .492, .254), tolerance=.01) ==
        vtype(.75, .5, .25)
    )

    t = Triangle3d(
        vtype(0, .5, 0),
        vtype(.5),
        vtype(1, .5, 0)
    )

    assert t.where_intersected_by_point(vtype(0, .5, 1)) is None
    assert t.where_intersected_by_point(vtype(2, .5, 0), tolerance=.9) is None
    assert t.where_intersected_by_point(vtype(2, .5, 0), tolerance=1.1) == (
        vtype(1, .5, 0)
    )

@pytest.mark.parametrize("vtype, bad_vtype", [
    (FVector3, DVector3),
    (DVector3, FVector3),
])
def test_where_intersected_by_line_segment(vtype: Any, bad_vtype: Any) -> None:
    t = Triangle3d(
        vtype(1, 0, 0),
        vtype(1, 1, 0),
        vtype(0, 0, 0),
    )

    with pytest.raises(TypeError) as excinfo:
        assert t.where_intersected_by_line_segment(None)
    assert str(excinfo.value).startswith(
        f'line must be LineSegment3d[{vtype.__name__}]'
    )
    with pytest.raises(TypeError) as excinfo:
        assert t.where_intersected_by_line_segment(LineSegment3d(
            bad_vtype(0),
            bad_vtype(1),
        ))
    assert str(excinfo.value).startswith(
        f'line must be LineSegment3d[{vtype.__name__}]'
    )

    assert t.where_intersected_by_line_segment(
        LineSegment3d(vtype(0), vtype(0, 0, 1))
    ) == vtype(0)
    assert t.where_intersected_by_line_segment(
        LineSegment3d(vtype(1, 0, 0), vtype(1, 0, 1))
    ) == vtype(1, 0, 0)
    assert t.where_intersected_by_line_segment(
        LineSegment3d(vtype(1, 1, 0), vtype(1, 1, 1))
    ) == vtype(1, 1, 0)
    assert t.where_intersected_by_line_segment(
        LineSegment3d(vtype(0, 0, -1), vtype(0, 0, 1))
    ) == vtype(0)
    assert t.where_intersected_by_line_segment(
        LineSegment3d(vtype(1, 0, -1), vtype(1, 0, 1))
    ) == vtype(1, 0, 0)
    assert t.where_intersected_by_line_segment(
        LineSegment3d(vtype(1, 1, -1), vtype(1, 1, 1))
    ) == vtype(1, 1, 0)
    assert t.where_intersected_by_line_segment(
        LineSegment3d(vtype(.5, .5, -1), vtype(.5, .5, 1))
    ) == vtype(.5, .5, 0)
    assert t.where_intersected_by_line_segment(
        LineSegment3d(vtype(.5, .5, 1), vtype(.5, .5, 2))
    ) is None
    assert t.where_intersected_by_line_segment(
        LineSegment3d(vtype(.5, .5, 1), vtype(.5, .5, 2)),
        tolerance=1
    ) == vtype(.5, .5, 0)
    assert t.where_intersected_by_line_segment(
        LineSegment3d(vtype(1, 0, 0), vtype(1, 1, 0))
    ) == LineSegment3d(vtype(1, 0, 0), vtype(1, 1, 0))
    assert t.where_intersected_by_line_segment(
        LineSegment3d(vtype(2, 0, 0), vtype(2, 2, 0))
    ) is None
    assert t.where_intersected_by_line_segment(
        LineSegment3d(vtype(1, 0, 0), vtype(2, 0, 0))
    ) == vtype(1, 0, 0)
    assert t.where_intersected_by_line_segment(
        LineSegment3d(vtype(.5, 0, 0), vtype(.5, -1, 0))
    ) == vtype(.5, 0, 0)
    assert t.where_intersected_by_line_segment(
        LineSegment3d(vtype(.5, 0, 0), vtype(.5, -1, 0)),
        tolerance=10
    ) == vtype(.5, 0, 0)
