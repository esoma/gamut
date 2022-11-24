
# gamut
from gamut.ai import NavigationMesh3d
from gamut.geometry import (
    get_max_circle_radius_between_point_and_line_segment_along_direction,
    LineSegment2d, Triangle3d)
from gamut.gltf import Gltf
from gamut.math import DVector2, DVector3, FVector3
# python
from math import inf, isclose
from pathlib import Path
from typing import Any
# pytest
import pytest

check_radius = (
    get_max_circle_radius_between_point_and_line_segment_along_direction
)


def vector3_is_close(a: Any, b: Any) -> bool:
    return (
        isclose(a.x, b.x) and
        isclose(a.y, b.y) and
        isclose(a.z, b.z)
    )


@pytest.mark.parametrize("a_y, b_y, c_y", [
    [0, 0, 0],
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
    [-1, 0, 1],
])
def test_internals_single_tri(
    a_y: float,
    b_y: float,
    c_y: float
) -> None:
    nm = NavigationMesh3d()

    a = DVector3(0, a_y, 0)
    b = DVector3(0, b_y, 1)
    c = DVector3(1, c_y, 0)
    a, b, c = sorted((a, b, c))
    a2 = a.xz
    b2 = b.xz
    c2 = c.xz
    tri = Triangle3d(a, b, c)
    ab_normal, bc_normal, ca_normal = tri.edge_normals

    nm.add_triangle(tri)

    assert nm._point_triangle[a] == {tri}
    assert nm._point_triangle[b] == {tri}
    assert nm._point_triangle[c] == {tri}

    assert nm._get_point_normal(a) == ((
        -ab_normal.xoz + -ca_normal.xoz
    ) / 2).normalize()
    assert nm._get_point_normal(b) == ((
        -ab_normal.xoz + -bc_normal.xoz
    ) / 2).normalize()
    assert nm._get_point_normal(c) == ((
        -bc_normal.xoz + -ca_normal.xoz
    ) / 2).normalize()

    nm._recalculate_point_max_radius()
    nm._recalculate_edge_max_radius()
    assert nm._point_max_radius[a] == check_radius(
        a.xz,
        LineSegment2d(b.xz, c.xz),
        nm._get_point_normal(a).xz
    )
    assert nm._point_max_radius[b] == check_radius(
        b.xz,
        LineSegment2d(a.xz, c.xz),
        nm._get_point_normal(b).xz
    )
    assert nm._point_max_radius[c] == check_radius(
        c.xz,
        LineSegment2d(a.xz, b.xz),
        nm._get_point_normal(c).xz
    )

    assert nm._edge_triangle[(a, b)] == {tri}
    assert nm._edge_triangle[(b, c)] == {tri}
    assert nm._edge_triangle[(a, c)] == {tri}

    assert nm._edge_max_radius[(a, b)] == min(
        check_radius(
            a2,
            LineSegment2d(b2, c2),
            b2 - a2,
        ),
        check_radius(
            b2,
            LineSegment2d(a2, c2),
            a2 - b2,
        ),
    )
    assert nm._edge_max_radius[(b, c)] == min(
       check_radius(
            b2,
            LineSegment2d(a2, c2),
            c2 - b2,
        ),
        check_radius(
            c2,
            LineSegment2d(a2, b2),
            b2 - c2,
        ),
    )
    assert nm._edge_max_radius[(a, c)] == min(
       check_radius(
            a2,
            LineSegment2d(b2, c2),
            c2 - a2,
        ),
        check_radius(
            c2,
            LineSegment2d(a2, b2),
            a2 - c2,
        ),
    )


def test_internals_center() -> None:
    nm = NavigationMesh3d()

    # a square composed of 8 tris:
    r"""
        ---------
       | 7/ | \6 |
       | /3 | 2\ |
       ----------
       | \1 | 0/ |
       | 5\ | /4 |
       ----------
    """
    tris = (
        Triangle3d(
            DVector3(0, 0, 0),
            DVector3(1, 0, 0),
            DVector3(0, 0, 1),
        ),
        Triangle3d(
            DVector3(0, 0, 0),
            DVector3(-1, 0, 0),
            DVector3(0, 0, 1),
        ),
        Triangle3d(
            DVector3(0, 0, 0),
            DVector3(1, 0, 0),
            DVector3(0, 0, -1),
        ),
        Triangle3d(
            DVector3(0, 0, 0),
            DVector3(-1, 0, 0),
            DVector3(0, 0, -1),
        ),
        Triangle3d(
            DVector3(1, 0, 1),
            DVector3(1, 0, 0),
            DVector3(0, 0, 1),
        ),
        Triangle3d(
            DVector3(-1, 0, 1),
            DVector3(-1, 0, 0),
            DVector3(0, 0, 1),
        ),
        Triangle3d(
            DVector3(1, 0, -1),
            DVector3(1, 0, 0),
            DVector3(0, 0, -1),
        ),
        Triangle3d(
            DVector3(-1, 0, -1),
            DVector3(-1, 0, 0),
            DVector3(0, 0, -1),
        )
    )
    for tri in tris:
        nm.add_triangle(tri)

    nm._recalculate_point_max_radius()
    nm._recalculate_edge_max_radius()

    # center point has no walls
    assert nm._point_triangle[DVector3(0, 0, 0)] == {
        tris[0], tris[1], tris[2], tris[3]
    }
    assert nm._point_max_radius[DVector3(0, 0, 0)] == inf
    assert nm._get_point_normal(DVector3(0, 0, 0)) == DVector3(0, 0, 0)

    # non-corner points
    assert nm._point_triangle[DVector3(1, 0, 0)] == {
        tris[0], tris[2], tris[4], tris[6]
    }
    assert nm._point_max_radius[DVector3(1, 0, 0)] == 1.0
    assert nm._get_point_normal(DVector3(1, 0, 0)) == DVector3(-1, 0, 0)

    assert nm._point_triangle[DVector3(-1, 0, 0)] == {
        tris[1], tris[3], tris[5], tris[7]
    }
    assert nm._point_max_radius[DVector3(-1, 0, 0)] == 1.0
    assert nm._get_point_normal(DVector3(-1, 0, 0)) == DVector3(1, 0, 0)

    assert nm._point_triangle[DVector3(0, 0, 1)] == {
        tris[0], tris[1], tris[4], tris[5]
    }
    assert nm._point_max_radius[DVector3(0, 0, 1)] == 1.0
    assert nm._get_point_normal(DVector3(0, 0, 1)) == DVector3(0, 0, -1)

    assert nm._point_triangle[DVector3(0, 0, -1)] == {
        tris[2], tris[3], tris[6], tris[7]
    }
    assert nm._point_max_radius[DVector3(0, 0, -1)] == 1.0
    assert nm._get_point_normal(DVector3(0, 0, -1)) == DVector3(0, 0, 1)

    # corners
    assert nm._point_triangle[DVector3(1, 0, 1)] == { tris[4] }
    assert isclose(nm._point_max_radius[DVector3(1, 0, 1)], 1.17157287525381)
    assert nm._get_point_normal(DVector3(1, 0, 1)) == (
        DVector3(-1, 0, -1).normalize()
    )

    assert nm._point_triangle[DVector3(1, 0, -1)] == { tris[6] }
    assert isclose(nm._point_max_radius[DVector3(1, 0, -1)], 1.17157287525381)
    assert nm._get_point_normal(DVector3(1, 0, -1)) == (
        DVector3(-1, 0, 1).normalize()
    )

    assert nm._point_triangle[DVector3(-1, 0, 1)] == { tris[5] }
    assert isclose(nm._point_max_radius[DVector3(-1, 0, 1)], 1.17157287525381)
    assert nm._get_point_normal(DVector3(-1, 0, 1)) == (
        DVector3(1, 0, -1).normalize()
    )

    assert nm._point_triangle[DVector3(-1, 0, -1)] == { tris[7] }
    assert isclose(nm._point_max_radius[DVector3(-1, 0, -1)], 1.17157287525381)
    assert nm._get_point_normal(DVector3(-1, 0, -1)) == (
        DVector3(1, 0, 1).normalize()
    )

    # inner edges
    edge = tuple(sorted((DVector3(0, 0, 0), DVector3(1, 0, 0))))
    assert nm._edge_triangle[edge] == {tris[0], tris[2]}
    assert nm._edge_max_radius[edge] == .5

    edge = tuple(sorted((DVector3(0, 0, 0), DVector3(-1, 0, 0))))
    assert nm._edge_triangle[edge] == {tris[1], tris[3]}
    assert nm._edge_max_radius[edge] == .5

    edge = tuple(sorted((DVector3(0, 0, 0), DVector3(0, 0, -1))))
    assert nm._edge_triangle[edge] == {tris[2], tris[3]}
    assert nm._edge_max_radius[edge] == .5

    edge = tuple(sorted((DVector3(0, 0, 0), DVector3(0, 0, 1))))
    assert nm._edge_triangle[edge] == {tris[0], tris[1]}
    assert nm._edge_max_radius[edge] == .5

    # outer edges
    edge = tuple(sorted((DVector3(1, 0, 0), DVector3(1, 0, 1))))
    assert nm._edge_triangle[edge] == {tris[4]}
    assert nm._edge_max_radius[edge] == .5

    edge = tuple(sorted((DVector3(1, 0, 1), DVector3(0, 0, 1))))
    assert nm._edge_triangle[edge] == {tris[4]}
    assert nm._edge_max_radius[edge] == .5

    edge = tuple(sorted((DVector3(0, 0, 1), DVector3(-1, 0, 1))))
    assert nm._edge_triangle[edge] == {tris[5]}
    assert nm._edge_max_radius[edge] == .5

    edge = tuple(sorted((DVector3(-1, 0, 1), DVector3(-1, 0, 0))))
    assert nm._edge_triangle[edge] == {tris[5]}
    assert nm._edge_max_radius[edge] == .5

    edge = tuple(sorted((DVector3(-1, 0, 0), DVector3(-1, 0, -1))))
    assert nm._edge_triangle[edge] == {tris[7]}
    assert nm._edge_max_radius[edge] == .5

    edge = tuple(sorted((DVector3(-1, 0, -1), DVector3(0, 0, -1))))
    assert nm._edge_triangle[edge] == {tris[7]}
    assert nm._edge_max_radius[edge] == .5

    edge = tuple(sorted((DVector3(0, 0, -1), DVector3(1, 0, -1))))
    assert nm._edge_triangle[edge] == {tris[6]}
    assert nm._edge_max_radius[edge] == .5

    edge = tuple(sorted((DVector3(1, 0, -1), DVector3(1, 0, 0))))
    assert nm._edge_triangle[edge] == {tris[6]}
    assert nm._edge_max_radius[edge] == .5


def test_find_basic_path() -> None:
    nm = NavigationMesh3d()

    nm.add_triangle(Triangle3d(
        DVector3(0, 0, 0),
        DVector3(0, 0, 1),
        DVector3(1, 0, 0)
    ))
    nm.add_triangle(Triangle3d(
        DVector3(0, 0, 0),
        DVector3(0, 0, 1),
        DVector3(1, 0, 0)
    ))
    nm.add_triangle(Triangle3d(
        DVector3(0, 0, 0),
        DVector3(0, 0, 1),
        DVector3(-1, 0, 0)
    ))
    nm.add_triangle(Triangle3d(
        DVector3(1, 0, 1),
        DVector3(0, 0, 1),
        DVector3(1, 0, 0)
    ))
    nm.add_triangle(Triangle3d(
        DVector3(0, 0, 0),
        DVector3(-1, 0, 0),
        DVector3(1, 0, 0)
    ))

    path = nm.find_path(
        DVector3(0, 0, 0),
        Triangle3d(DVector3(0, 0, 0), DVector3(0, 0, 1), DVector3(1, 0, 0)),
        DVector3(1, 0, 1),
        Triangle3d(DVector3(1, 0, 1), DVector3(0, 0, 1), DVector3(1, 0, 0))
    )
    assert path == (DVector3(0, 0, 0), DVector3(.5, 0, .5), DVector3(1, 0, 1))

    nm.remove_triangle(Triangle3d(
        DVector3(0, 0, 0),
        DVector3(0, 0, 1),
        DVector3(1, 0, 0)
    ))
    path = nm.find_path(
        DVector3(0, 0, 0),
        Triangle3d(DVector3(0, 0, 0), DVector3(0, 0, 1), DVector3(1, 0, 0)),
        DVector3(1, 0, 1),
        Triangle3d(DVector3(1, 0, 1), DVector3(0, 0, 1), DVector3(1, 0, 0))
    )
    assert path is None


@pytest.mark.parametrize("radius", [0.0, .1])
def test_custom_weight(radius: float) -> None:
    triangle_1 = Triangle3d(
        DVector3(-.5, 0, 0),
        DVector3(.5, 0, 0),
        DVector3(0, 0, 1)
    )
    triangle_2 = Triangle3d(
        DVector3(.5, 0, 0),
        DVector3(0, 0, 1),
        DVector3(.5, 0, 2),
    )

    def custom_calculate_weight(
        a: Triangle3d[DVector3], b: Triangle3d[DVector3]
    ) -> float:
        if {a, b} == {triangle_1, triangle_2}:
            return 1
        return .1

    nm = NavigationMesh3d(custom_calculate_weight)
    nm.add_triangle(triangle_1)
    nm.add_triangle(Triangle3d(
        DVector3(-.5, 0, 0),
        DVector3(0, 0, 1),
        DVector3(-.5, 0, 2),
    ))
    nm.add_triangle(triangle_2)
    nm.add_triangle(Triangle3d(
        DVector3(0, 0, 1),
        DVector3(.5, 0, 2),
        DVector3(-.5, 0, 2)
    ))
    path = nm.find_path(
        DVector3(-.5, 0, 0),
        triangle_1,
        DVector3(.25, 0, -1),
        triangle_2,
        radius=radius
    )
    assert path == (
        DVector3(-0.5, 0.0, 0.0),
        DVector3(0.0, 0.0, 1.0),
        DVector3(0.25, 0.0, -1.0)
    )


def test_find_single_triangle() -> None:
    nm = NavigationMesh3d()

    nm.add_triangle(Triangle3d(
        DVector3(0, 0, 0),
        DVector3(0, 0, 1),
        DVector3(1, 0, 0)
    ))

    path = nm.find_path(
        DVector3(0, 0, 0),
        Triangle3d(DVector3(0, 0, 0), DVector3(0, 0, 1), DVector3(1, 0, 0)),
        DVector3(1, 0, 0),
        Triangle3d(DVector3(0, 0, 0), DVector3(0, 0, 1), DVector3(1, 0, 0)),
    )
    assert path == (DVector3(0, 0, 0), DVector3(1, 0, 0))


def test_degenerate_triangle_point() -> None:
    nm = NavigationMesh3d()

    nm.add_triangle(Triangle3d(
        DVector3(1, 0, 0),
        DVector3(1, 0, 0),
        DVector3(1, 0, 0)
    ))
    nm.add_triangle(Triangle3d(
        DVector3(0, 0, 0),
        DVector3(1, 0, 0),
        DVector3(1, 0, 0)
    ))
    nm.add_triangle(Triangle3d(
        DVector3(0, 0, 0),
        DVector3(0, 0, 1),
        DVector3(1, 0, 0)
    ))
    nm.add_triangle(Triangle3d(
        DVector3(1, 0, 1),
        DVector3(0, 0, 1),
        DVector3(1, 0, 0)
    ))

    path = nm.find_path(
        DVector3(1, 0, 0),
        Triangle3d(DVector3(1, 0, 0), DVector3(1, 0, 0), DVector3(1, 0, 0)),
        DVector3(1, 0, 1),
        Triangle3d(DVector3(1, 0, 1), DVector3(0, 0, 1), DVector3(1, 0, 0)),
    )
    assert path == (DVector3(1, 0, 0), DVector3(1, 0, 1))


@pytest.mark.parametrize("c", [
    DVector3(1),
    DVector3(-1, 1, 1),
    DVector3(1, 1, -1),
    DVector3(-1, 1, -1),
]
)
def test_find_path_string_pull(c: DVector3) -> None:
    nm = NavigationMesh3d()

    nm.add_triangle(Triangle3d(
        DVector3(0, 0, 0) * c,
        DVector3(1, 0, 0) * c,
        DVector3(0, 0, 1) * c
    ))
    nm.add_triangle(Triangle3d(
        DVector3(0, 0, 0) * c,
        DVector3(0, 0, 1) * c,
        DVector3(-1, 0, 1) * c
    ))
    nm.add_triangle(Triangle3d(
        DVector3(-1, 0, 1) * c,
        DVector3(0, 0, 1) * c,
        DVector3(-1, 0, 2) * c
    ))
    nm.add_triangle(Triangle3d(
        DVector3(-1, 0, 1) * c,
        DVector3(-2, 0, 1) * c,
        DVector3(-1, 0, 2) * c
    ))
    nm.add_triangle(Triangle3d(
        DVector3(-1, 0, 0) * c,
        DVector3(-1, 0, 1) * c,
        DVector3(-2, 0, 1) * c
    ))
    nm.add_triangle(Triangle3d(
        DVector3(-1, 0, 0) * c,
        DVector3(-2, 0, 1) * c,
        DVector3(-2, 0, 0) * c
    ))
    nm.add_triangle(Triangle3d(
        DVector3(-1, 0, 0) * c,
        DVector3(0, 0, 0) * c,
        DVector3(0, 0, -1) * c
    ))
    nm.add_triangle(Triangle3d(
        DVector3(-1, 0, 0) * c,
        DVector3(-1, 0, -1) * c,
        DVector3(0, 0, -1) * c
    ))
    nm.add_triangle(Triangle3d(
        DVector3(-1, 0, 0) * c,
        DVector3(-1, 0, -1) * c,
        DVector3(-2, 0, 0) * c
    ))
    nm.add_triangle(Triangle3d(
        DVector3(0, 0, 0) * c,
        DVector3(0, 0, -1) * c,
        DVector3(1, 0, -1) * c
    ))
    nm.add_triangle(Triangle3d(
        DVector3(0, 0, -2) * c,
        DVector3(0, 0, -1) * c,
        DVector3(1, 0, -1) * c
    ))
    nm.add_triangle(Triangle3d(
        DVector3(0, 0, -2) * c,
        DVector3(-1, 0, -2) * c,
        DVector3(-1, 0, -3) * c
    ))
    nm.add_triangle(Triangle3d(
        DVector3(0, 0, -2) * c,
        DVector3(0, 0, -3) * c,
        DVector3(-1, 0, -3) * c
    ))
    nm.add_triangle(Triangle3d(
        DVector3(0, 0, -2) * c,
        DVector3(1, 0, -2) * c,
        DVector3(1, 0, -1) * c
    ))
    nm.add_triangle(Triangle3d(
        DVector3(0, 0, -2) * c,
        DVector3(1, 0, -2) * c,
        DVector3(0, 0, -3) * c
    ))

    path = nm.find_path(
        DVector3(1, 0, 0) * c,
        Triangle3d(
            DVector3(1, 0, 0) * c,
            DVector3(0, 0, 1) * c,
            DVector3(0, 0, 0) * c,
        ),
        DVector3(-1, 0, -2) * c,
        Triangle3d(
            DVector3(-1, 0, -2) * c,
            DVector3(-1, 0, -3) * c,
            DVector3(0, 0, -2) * c,
        )
    )
    assert path == (
        DVector3(1, 0, 0) * c,
        DVector3(-1, 0, 1) * c,
        DVector3(-1, 0, 0) * c,
        DVector3(0, 0, -1) * c,
        DVector3(0, 0, -2) * c,
        DVector3(-1, 0, -2) * c,
    )


def test_find_path_string_pull_y() -> None:
    nm = NavigationMesh3d()
    # _
    nm.add_triangle(Triangle3d(
        DVector3(0, 0, 0),
        DVector3(0, 0, 1),
        DVector3(1, 0, 1),
    ))
    nm.add_triangle(Triangle3d(
        DVector3(0, 0, 0),
        DVector3(1, 0, 1),
        DVector3(1, 0, 0),
    ))
    # __
    nm.add_triangle(Triangle3d(
        DVector3(1, 0, 0),
        DVector3(1, 0, 1),
        DVector3(2, 0, 1),
    ))
    nm.add_triangle(Triangle3d(
        DVector3(1, 0, 0),
        DVector3(2, 0, 1),
        DVector3(2, 0, 0),
    ))
    # __/
    nm.add_triangle(Triangle3d(
        DVector3(2, 0, 0),
        DVector3(2, 0, 1),
        DVector3(3, 1, 1),
    ))
    nm.add_triangle(Triangle3d(
        DVector3(2, 0, 0),
        DVector3(3, 1, 1),
        DVector3(3, 1, 0),
    ))
    #    _
    # __/
    nm.add_triangle(Triangle3d(
        DVector3(3, 1, 0),
        DVector3(3, 1, 1),
        DVector3(4, 1, 1),
    ))
    nm.add_triangle(Triangle3d(
        DVector3(3, 1, 0),
        DVector3(4, 1, 1),
        DVector3(4, 1, 0),
    ))
    #    __
    # __/
    nm.add_triangle(Triangle3d(
        DVector3(4, 1, 0),
        DVector3(4, 1, 1),
        DVector3(5, 1, 1),
    ))
    nm.add_triangle(Triangle3d(
        DVector3(4, 1, 0),
        DVector3(5, 1, 1),
        DVector3(5, 1, 0),
    ))
    #    __
    # __/  \
    nm.add_triangle(Triangle3d(
        DVector3(5, 1, 0),
        DVector3(5, 1, 1),
        DVector3(6, 0, 1),
    ))
    nm.add_triangle(Triangle3d(
        DVector3(5, 1, 0),
        DVector3(6, 0, 1),
        DVector3(6, 0, 0),
    ))
    #    __
    # __/  \_
    nm.add_triangle(Triangle3d(
        DVector3(6, 0, 0),
        DVector3(6, 0, 1),
        DVector3(7, 0, 1),
    ))
    nm.add_triangle(Triangle3d(
        DVector3(6, 0, 0),
        DVector3(7, 0, 1),
        DVector3(7, 0, 0),
    ))
    #    __
    # __/  \__
    nm.add_triangle(Triangle3d(
        DVector3(7, 0, 0),
        DVector3(7, 0, 1),
        DVector3(8, 0, 1),
    ))
    nm.add_triangle(Triangle3d(
        DVector3(7, 0, 0),
        DVector3(8, 0, 1),
        DVector3(8, 0, 0),
    ))
    #    __
    # s_/  \_e
    path = nm.find_path(
        DVector3(0, 0, 0),
        Triangle3d(
            DVector3(1, 0, 1),
            DVector3(0, 0, 0),
            DVector3(0, 0, 1),
        ),
        DVector3(8, 0, 1),
        Triangle3d(
            DVector3(7, 0, 0),
            DVector3(8, 0, 1),
            DVector3(8, 0, 0),
        )
    )
    assert vector3_is_close(path[0], DVector3(0.0, 0.0, 0.0))
    assert vector3_is_close(path[1], DVector3(2.0, 0.0, 0.25))
    assert vector3_is_close(path[2], DVector3(3.0, 1.0, 0.375))
    assert vector3_is_close(path[3], DVector3(5.0, 1.0, 0.625))
    assert vector3_is_close(path[4], DVector3(6.0, 0.0, 0.75))
    assert vector3_is_close(path[5], DVector3(8.0, 0.0, 1.0))


def test_find_path_string_pull_bug(resources: Path) -> None:
    with open(resources / 'navmesh.glb', 'rb') as f:
        navmesh_gltf = Gltf(f)
    navmesh_attrs = navmesh_gltf.meshes[0].primitives[0].attributes
    navmesh_indices = navmesh_gltf.meshes[0].primitives[0].indices.data
    navmesh_positions = navmesh_attrs["POSITION"].data

    nm = NavigationMesh3d()
    for i in range(len(navmesh_indices) // 3):
        nm.add_triangle(Triangle3d(
            navmesh_positions[navmesh_indices[(i * 3)]],
            navmesh_positions[navmesh_indices[(i * 3) + 1]],
            navmesh_positions[navmesh_indices[(i * 3) + 2]],
        ))

    path = nm.find_path(
        FVector3(-5.265909194946289, 2.0, 3.866203784942627),
        Triangle3d(
            FVector3(-6.0, 2.0, 4.0),
            FVector3(-4.0, 2.0, 4.0),
            FVector3(-4.0, 2.0, 1.0)
        ),
        FVector3(4.608282566070557, 2.0, -2.154895782470703),
        Triangle3d(
            FVector3(4.0, 2.0, -4.0),
            FVector3(4.0, 2.0, -1.0),
            FVector3(6.0, 2.0, -4.0)
        )
    )
    assert vector3_is_close(
        path[0],
        FVector3(-5.265909194946289, 2.0, 3.866203784942627)
    )
    assert vector3_is_close(path[1], FVector3(-4.0, 2.0, 1.0))
    assert vector3_is_close(path[2], FVector3(4.0, 2.0, -1.0))
    assert vector3_is_close(
        path[3],
        FVector3(4.608282566070557, 2.0, -2.154895782470703)
    )


def test_find_path_basic_portal_squeeze() -> None:
    nm = NavigationMesh3d()
    nm.add_triangle(Triangle3d(
        DVector3(0, 0, 0),
        DVector3(0, 0, 1),
        DVector3(1, 0, 1),
    ))
    nm.add_triangle(Triangle3d(
        DVector3(0, 0, 0),
        DVector3(1, 0, 1),
        DVector3(1, 0, 0),
    ))

    path = nm.find_path(
        DVector3(0, 0, 1),
        Triangle3d(
            DVector3(0, 0, 0),
            DVector3(0, 0, 1),
            DVector3(1, 0, 1),
        ),
        DVector3(1, 0, .5),
        Triangle3d(
            DVector3(0, 0, 0),
            DVector3(1, 0, 1),
            DVector3(1, 0, 0),
        ),
        radius=1,
    )
    assert path is None

    path = nm.find_path(
        DVector3(0, 0, 1),
        Triangle3d(
            DVector3(0, 0, 0),
            DVector3(0, 0, 1),
            DVector3(1, 0, 1),
        ),
        DVector3(1, 0, .5),
        Triangle3d(
            DVector3(0, 0, 0),
            DVector3(1, 0, 1),
            DVector3(1, 0, 0),
        ),
        radius=1,
        squeeze=True
    )
    assert path == (
        DVector3(0.0, 0.0, 1.0),
        DVector3(0.5, 0.0, 0.5),
        DVector3(1.0, 0.0, 0.5),
    )
