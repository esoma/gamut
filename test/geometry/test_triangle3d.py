
# gamut
from gamut.geometry import DegenerateGeometryError, LineSegment3d, Triangle3d
from gamut.math import DVector3, DVector4, FVector3
# python
from typing import Any
# pytest
import pytest


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
