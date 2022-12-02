
# gamut
from gamut.geometry import LineSegment3d, Plane, Triangle3d
from gamut.math import BVector3, DVector3, DVector4, FVector3
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


@pytest.mark.parametrize("vtype", [FVector3, DVector3])
def test_degenerate(vtype: Any) -> None:
    with pytest.raises(LineSegment3d.DegenerateError) as excinfo:
        LineSegment3d(vtype(0), vtype(0))
    assert str(excinfo.value).startswith('degenerate line segment')
    assert excinfo.value.degenerate_form == vtype(0)


@pytest.mark.parametrize("vtype", [FVector3, DVector3])
def test_attributes(vtype: Any) -> None:
    line = LineSegment3d(vtype(0, 1, 2), vtype(3, 4, 5))
    assert line.a == vtype(0, 1, 2)
    assert line.b == vtype(3, 4, 5)
    assert line.points == (line.a, line.b)


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
@pytest.mark.parametrize("axis", [
    BVector3(True, False, False),
    BVector3(False, True, False),
    BVector3(False, False, True),
    BVector3(True, True, False),
    BVector3(False, True, True),
    BVector3(True, False, True),
])
def test_are_points_on_same_side(vtype: Any, axis: BVector3) -> None:
    av = vtype(*(1 if a else 0 for a in axis))
    line = LineSegment3d(vtype(0), vtype(*(0 if a else 1 for a in axis)))
    assert line.are_points_on_same_side(vtype(1) * av, vtype(2) * av)
    assert line.are_points_on_same_side(vtype(0) * av, vtype(2) * av)
    assert line.are_points_on_same_side(vtype(0) * av, vtype(-2) * av)
    assert not line.are_points_on_same_side(vtype(2) * av, vtype(-2) * av)
    assert line.are_points_on_same_side(vtype(0) * av, vtype(0) * av)


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


@pytest.mark.parametrize("vtype", [FVector3, DVector3])
def test_distance_to_point(vtype: Any) -> None:
    line = LineSegment3d(vtype(0), vtype(5, 0, 0))
    assert line.distance_to_point(vtype(0)) == 0
    assert line.distance_to_point(vtype(5, 0, 0)) == 0
    assert line.distance_to_point(vtype(6, 0, 0)) == 1
    assert line.distance_to_point(vtype(-1, 0, 0)) == 1
    assert line.distance_to_point(vtype(0, 1, 0)) == 1
    assert line.distance_to_point(vtype(0, -1, 0)) == 1
    assert line.distance_to_point(vtype(0, 0, 2)) == 2
    assert line.distance_to_point(vtype(0, 0, -2)) == 2


@pytest.mark.parametrize("vtype", [FVector3, DVector3])
def test_intersects_point(vtype: Any) -> None:
    line = LineSegment3d(vtype(-5), vtype(5))
    assert not line.intersects_point(vtype(-6))
    assert line.intersects_point(vtype(-5))
    assert line.intersects_point(vtype(0))
    assert line.intersects_point(vtype(5))
    assert not line.intersects_point(vtype(6))

    assert line.intersects_point(vtype(6), tolerance=1.733)
    assert line.intersects_point(vtype(-1), tolerance=1.733)


@pytest.mark.parametrize("vtype", [FVector3, DVector3])
def test_is_parallel_with_line_segment(vtype: Any) -> None:
    line = LineSegment3d(vtype(-5), vtype(5))
    assert line.is_parallel_with_line_segment(line)
    assert line.is_parallel_with_line_segment(
        LineSegment3d(vtype(5), vtype(-5))
    )
    assert line.is_parallel_with_line_segment(
        LineSegment3d(vtype(8), vtype(16))
    )
    assert not line.is_parallel_with_line_segment(
        LineSegment3d(vtype(0), vtype(5, 0, 0))
    )

    line = LineSegment3d(vtype(0), vtype(5, 0, 0))
    assert line.is_parallel_with_line_segment(line)
    assert line.is_parallel_with_line_segment(
        LineSegment3d(vtype(5, 0, 0), vtype(0))
    )
    assert line.is_parallel_with_line_segment(
        LineSegment3d(vtype(5, 1, 0), vtype(0, 1, 0))
    )
    assert line.is_parallel_with_line_segment(
        LineSegment3d(vtype(5, 0, 1), vtype(0, 0, 1))
    )
    assert line.is_parallel_with_line_segment(
        LineSegment3d(vtype(5, -1, 1), vtype(0, -1, 1))
    )


@pytest.mark.parametrize("vtype", [FVector3, DVector3])
def test_distance_to_line_segment(vtype: Any) -> None:
    line = LineSegment3d(vtype(-5), vtype(5))
    assert line.distance_to_line_segment(line) == 0.0
    assert line.distance_to_line_segment(
        LineSegment3d(vtype(-4), vtype(4))
    ) == 0.0
    assert line.distance_to_line_segment(
        LineSegment3d(vtype(6), vtype(8))
    ) == vtype(5).distance(vtype(6))
    assert line.distance_to_line_segment(
        LineSegment3d(vtype(-7), vtype(-8))
    ) == vtype(-5).distance(vtype(-7))

    assert line.distance_to_line_segment(
        LineSegment3d(vtype(-1, 0, 0), vtype(0, 0, 0))
    ) == 0.0
    assert pytest.approx(
        line.distance_to_line_segment(
            LineSegment3d(vtype(-1, 0, 0), vtype(-2, 0, 0))
        )
    ) == 0.8164966106414795

    line = LineSegment3d(vtype(0), vtype(1, 0, 0))
    assert line.distance_to_line_segment(
        LineSegment3d(vtype(-1, 0, 0), vtype(-2, 0, 0))
    ) == 1.0
    assert line.distance_to_line_segment(
        LineSegment3d(vtype(0, -1, 0), vtype(1, -1, 0))
    ) == 1.0


@pytest.mark.parametrize("vtype", [FVector3, DVector3])
def test_where_intersected_by_plane(vtype: Any) -> None:
    line = LineSegment3d(vtype(0, -2, 0), vtype(0, 2, 0))

    with pytest.raises(TypeError) as excinfo:
        assert line.where_intersected_by_plane(None)
    assert str(excinfo.value).startswith(
        f'plane must be Plane[{vtype.__name__}]'
    )

    assert line.where_intersected_by_plane(
        Plane(-1, vtype(0, 1, 0))
    ) == vtype(0, 1, 0)
    assert line.where_intersected_by_plane(
        Plane(-3, vtype(0, 1, 0))
    ) is None
    assert line.where_intersected_by_plane(
        Plane(-3, vtype(0, 1, 0)),
        tolerance=1
    ) == vtype(0, 2, 0)
    assert line.where_intersected_by_plane(
        Plane(3, vtype(0, 1, 0)),
        tolerance=1
    ) == vtype(0, -2, 0)

    line = LineSegment3d(vtype(0, 1, 0), vtype(1, 1, 0))
    assert line.where_intersected_by_plane(
        Plane(-1, vtype(0, 1, 0))
    ) == LineSegment3d(vtype(0, 1, 0), vtype(1, 1, 0))
    assert line.where_intersected_by_plane(
        Plane(-2, vtype(0, 1, 0))
    ) is None
    assert line.where_intersected_by_plane(
        Plane(-2, vtype(0, 1, 0)),
        tolerance=1
    ) == LineSegment3d(vtype(0, 1, 0), vtype(1, 1, 0))


@pytest.mark.parametrize("vtype", [FVector3, DVector3])
def test_project_point(vtype: Any) -> None:
    line = LineSegment3d(vtype(0, -2, 0), vtype(0, 2, 0))

    with pytest.raises(TypeError) as excinfo:
        assert line.project_point(None)
    assert str(excinfo.value).startswith(f'point must be {vtype.__name__}')

    assert line.project_point(vtype(0, -2, 0)) == vtype(0, -2, 0)
    assert line.project_point(vtype(0, 2, 0)) == vtype(0, 2, 0)
    assert line.project_point(vtype(0, 0, 0)) == vtype(0, 0, 0)
    assert line.project_point(vtype(0, -4, 0)) == vtype(0, -4, 0)

    assert line.project_point(vtype(100, -2, -100)) == vtype(0, -2, 0)
    assert line.project_point(vtype(1, -4, -1)) == vtype(0, -4, 0)

    assert line.project_point(
        vtype(100, -2, -100),
        clamped=True
    ) == vtype(0, -2, 0)
    assert line.project_point(
        vtype(1, -4, -1),
        clamped=True
    ) == vtype(0, -2, 0)
    assert line.project_point(
        vtype(1, 4, -1),
        clamped=True
    ) == vtype(0, 2, 0)


@pytest.mark.parametrize("vtype", [FVector3, DVector3])
def test_project_point(vtype: Any) -> None:
    line = LineSegment3d(vtype(0, -2, 0), vtype(0, 2, 0))

    with pytest.raises(TypeError) as excinfo:
        assert line.where_intersected_by_point(None)
    assert str(excinfo.value).startswith(f'point must be {vtype.__name__}')

    assert line.where_intersected_by_point(vtype(0, -2, 0)) == vtype(0, -2, 0)
    assert line.where_intersected_by_point(vtype(0, 2, 0)) == vtype(0, 2, 0)
    assert line.where_intersected_by_point(vtype(0, 0, 0)) == vtype(0, 0, 0)

    assert line.where_intersected_by_point(vtype(0, -3, 0)) is None
    assert line.where_intersected_by_point(
        vtype(0, -3, 0),
        tolerance=1
    ) == vtype(0, -2, 0)
    assert line.where_intersected_by_point(vtype(1, 0, 0)) is None
    assert line.where_intersected_by_point(
        vtype(1, 0, 0),
        tolerance=1
    ) == vtype(0, 0, 0)


@pytest.mark.parametrize("vtype", [FVector3, DVector3])
def test_where_intersected_by_line_segment(vtype: Any) -> None:
    line = LineSegment3d(vtype(-5), vtype(5))

    with pytest.raises(TypeError) as excinfo:
        assert line.where_intersected_by_line_segment(None)
    assert str(excinfo.value).startswith(
        f'other must be LineSegment3d[{vtype.__name__}]'
    )

    assert line.where_intersected_by_line_segment(line) == line
    assert line.where_intersected_by_line_segment(
        LineSegment3d(vtype(-4), vtype(4))
    ) == LineSegment3d(vtype(-4), vtype(4))
    assert line.where_intersected_by_line_segment(
        LineSegment3d(vtype(6), vtype(8))
    ) is None
    assert line.where_intersected_by_line_segment(
        LineSegment3d(vtype(-7), vtype(-8))
    ) is None
    assert line.where_intersected_by_line_segment(
        LineSegment3d(vtype(-1, 0, 0), vtype(0, 0, 0))
    ) == vtype(0, 0, 0)
    assert line.where_intersected_by_line_segment(
        LineSegment3d(vtype(-1, -2, -2), vtype(-1, -3, -3))
    ) is None


    line = LineSegment3d(vtype(0), vtype(1, 0, 0))
    assert line.where_intersected_by_line_segment(
        LineSegment3d(vtype(-1, 0, 0), vtype(-2, 0, 0))
    ) is None
    assert line.where_intersected_by_line_segment(
        LineSegment3d(vtype(-1, 0, 0), vtype(-2, 0, 0)),
        tolerance=1
    ) == vtype(0)

    assert LineSegment3d(
        vtype(0),
        vtype(2, 0, 0)
    ).where_intersected_by_line_segment(
        LineSegment3d(
            vtype(-1, 0, 0),
            vtype(1, 0, 0)
        ),
    ) == LineSegment3d(vtype(0), vtype(1, 0, 0))


@pytest.mark.parametrize("vtype", [FVector3, DVector3])
def test_where_intersected_by_triangle(vtype: Any) -> None:
    line = LineSegment3d(vtype(0), vtype(2, 0, 0))

    with pytest.raises(TypeError) as excinfo:
        assert line.where_intersected_by_triangle(None)
    assert str(excinfo.value).startswith(
        f'tri must be Triangle3d[{vtype.__name__}]'
    )

    assert line.where_intersected_by_triangle(Triangle3d(
        vtype(5),
        vtype(6, 5, 5),
        vtype(5, 6, 5),
    )) is None
    assert line.where_intersected_by_triangle(Triangle3d(
        vtype(-1, 0, 0),
        vtype(1, 0, 0),
        vtype(0, 1, 0)
    )) == LineSegment3d(vtype(0, 0, 0), vtype(1, 0, 0))
    assert line.where_intersected_by_triangle(Triangle3d(
        vtype(3, 0, 0),
        vtype(1, 0, 0),
        vtype(0, 1, 0)
    )) == LineSegment3d(vtype(1, 0, 0), vtype(2, 0, 0))
    assert line.where_intersected_by_triangle(Triangle3d(
        vtype(-1, 0, 0),
        vtype(3, 0, 0),
        vtype(0, 1, 0)
    )) == LineSegment3d(vtype(0, 0, 0), vtype(2, 0, 0))

    assert line.where_intersected_by_triangle(Triangle3d(
        vtype(0, 0, 0),
        vtype(0, 1, 1),
        vtype(0, 1, 0)
    )) == vtype(0, 0, 0)

    assert line.where_intersected_by_triangle(Triangle3d(
        vtype(0, 1, 1),
        vtype(1, 1, 0),
        vtype(0, 1, 0)
    )) is None
    assert line.where_intersected_by_triangle(Triangle3d(
        vtype(0, 1, 1),
        vtype(1, 1, 0),
        vtype(0, 1, 0)
    ), tolerance=1) == vtype(0)

    assert line.where_intersected_by_triangle(Triangle3d(
        vtype(0, 2, 1),
        vtype(1, 2, 0),
        vtype(0, 1, 0)
    )) is None
    assert line.where_intersected_by_triangle(Triangle3d(
        vtype(0, 2, 1),
        vtype(1, 2, 0),
        vtype(0, 1, 0)
    ), tolerance=1) == vtype(0)

    assert vector3_is_close(
        line.where_intersected_by_triangle(
            Triangle3d(
                vtype(0, 2, 1),
                vtype(1, 2, 0),
                vtype(1, -1, 0)
            )
        ),
        vtype(1, 0, 0)
    )

    assert line.where_intersected_by_triangle(
        Triangle3d(
            vtype(1, 3, 0),
            vtype(-1, -1, 0),
            vtype(3, -1, 0)
        )
    ) == line
    assert line.where_intersected_by_triangle(
        Triangle3d(
            vtype(1, 3, 1),
            vtype(-1, -1, 1),
            vtype(3, -1, 1)
        )
    ) is None
    assert line.where_intersected_by_triangle(
        Triangle3d(
            vtype(1, 3, 1),
            vtype(-1, -1, 1),
            vtype(3, -1, 1)
        ),
        tolerance=1
    ) == line

    assert line.where_intersected_by_triangle(
        Triangle3d(
            vtype(1, 3, 0),
            vtype(1, -1, 0),
            vtype(3, -1, 0)
        )
    ) == LineSegment3d(vtype(1, 0, 0), vtype(2, 0, 0))
    assert line.where_intersected_by_triangle(
        Triangle3d(
            vtype(1, 3, 1),
            vtype(1, -1, 1),
            vtype(3, -1, 1)
        )
    ) is None
    assert line.where_intersected_by_triangle(
        Triangle3d(
            vtype(1, 3, 1),
            vtype(1, -1, 1),
            vtype(3, -1, 1)
        ),
        tolerance=1
    ) == LineSegment3d(vtype(1, 0, 0), vtype(2, 0, 0))

    assert line.where_intersected_by_triangle(
        Triangle3d(
            vtype(2, 3, 0),
            vtype(2, -1, 0),
            vtype(4, -1, 0)
        )
    ) == vtype(2, 0, 0)
    assert line.where_intersected_by_triangle(
        Triangle3d(
            vtype(2, 3, 1),
            vtype(2, -1, 1),
            vtype(4, -1, 1)
        )
    ) is None
    assert line.where_intersected_by_triangle(
        Triangle3d(
            vtype(2, 3, 1),
            vtype(2, -1, 1),
            vtype(4, -1, 1)
        ),
        tolerance=1
    ) == vtype(2, 0, 0)

    assert line.where_intersected_by_triangle(
        Triangle3d(
            vtype(0, -1, 0),
            vtype(2, -1, 0),
            vtype(1, 3, 0)
        )
    ) == LineSegment3d(vtype(.25, 0, 0), vtype(1.75, 0, 0))
    assert line.where_intersected_by_triangle(
        Triangle3d(
            vtype(0, -1, 1),
            vtype(2, -1, 1),
            vtype(1, 3, 1)
        )
    ) is None
    assert line.where_intersected_by_triangle(
        Triangle3d(
            vtype(0, -1, 1),
            vtype(2, -1, 1),
            vtype(1, 3, 1)
        ),
        tolerance=1
    ) == LineSegment3d(vtype(.25, 0, 0), vtype(1.75, 0, 0))

    assert line.where_intersected_by_triangle(
        Triangle3d(
            vtype(2, -1, 0),
            vtype(4, -1, 0),
            vtype(3, 3, 0)
        )
    ) is None

    assert line.where_intersected_by_triangle(
        Triangle3d(
            vtype(-1, 0, 0),
            vtype(-2, 0, 0),
            vtype(-1, 1, 0)
        )
    ) is None
    assert line.where_intersected_by_triangle(
        Triangle3d(
            vtype(-1, 0, 0),
            vtype(-2, 0, 0),
            vtype(-1, 1, 0)
        ),
        tolerance=1
    ) == vtype(0)

    assert line.where_intersected_by_triangle(
        Triangle3d(
            vtype(1, 1, 0),
            vtype(0, 1, 0),
            vtype(2, 2, 0)
        )
    ) is None
    assert line.where_intersected_by_triangle(
        Triangle3d(
            vtype(1, 1, 0),
            vtype(0, 1, 0),
            vtype(2, 2, 0)
        ),
        tolerance=1
    ) == LineSegment3d(vtype(0), vtype(1, 0, 0))
