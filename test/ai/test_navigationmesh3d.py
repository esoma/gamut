
# gamut
from gamut.ai import NavigationMesh3d
from gamut.geometry import Triangle3d
from gamut.math import Vector3
# python
from math import isclose
# pytest
import pytest


def vector_is_close(a: Vector3, b: Vector3) -> bool:
    return (
        isclose(a.x, b.x),
        isclose(a.y, b.y),
        isclose(a.z, b.z),
    )


def test_find_basic_path() -> None:
    nm = NavigationMesh3d()

    nm.add_triangle(Triangle3d(
        Vector3(0, 0, 0),
        Vector3(0, 0, 1),
        Vector3(1, 0, 0)
    ))
    nm.add_triangle(Triangle3d(
        Vector3(0, 0, 0),
        Vector3(0, 0, 1),
        Vector3(-1, 0, 0)
    ))
    nm.add_triangle(Triangle3d(
        Vector3(1, 0, 1),
        Vector3(0, 0, 1),
        Vector3(1, 0, 0)
    ))
    nm.add_triangle(Triangle3d(
        Vector3(0, 0, 0),
        Vector3(-1, 0, 0),
        Vector3(1, 0, 0)
    ))

    assert nm.contains_triangle(Triangle3d(
        Vector3(0, 0, 0),
        Vector3(0, 0, 1),
        Vector3(1, 0, 0)
    ))
    assert nm.contains_triangle(Triangle3d(
        Vector3(0, 0, 0),
        Vector3(0, 0, 1),
        Vector3(-1, 0, 0)
    ))
    assert nm.contains_triangle(Triangle3d(
        Vector3(1, 0, 1),
        Vector3(0, 0, 1),
        Vector3(1, 0, 0)
    ))
    assert nm.contains_triangle(Triangle3d(
        Vector3(0, 0, 0),
        Vector3(-1, 0, 0),
        Vector3(1, 0, 0)
    ))

    triangles = list(set(t.positions) for t in nm.triangles)
    assert {Vector3(0, 0, 0), Vector3(0, 0, 1), Vector3(1, 0, 0)} in triangles
    assert {Vector3(0, 0, 0), Vector3(0, 0, 1), Vector3(-1, 0, 0)} in triangles
    assert {Vector3(1, 0, 1), Vector3(0, 0, 1), Vector3(1, 0, 0)} in triangles
    assert {Vector3(0, 0, 0), Vector3(-1, 0, 0), Vector3(1, 0, 0)} in triangles

    path = nm.find_path(
        Vector3(0, 0, 0),
        Triangle3d(Vector3(0, 0, 0), Vector3(0, 0, 1), Vector3(1, 0, 0)),
        Vector3(1, 0, 1),
        Triangle3d(Vector3(1, 0, 1), Vector3(0, 0, 1), Vector3(1, 0, 0))
    )
    assert path == (Vector3(0, 0, 0), Vector3(1, 0, 1))


@pytest.mark.parametrize("c", [
    Vector3(1),
    Vector3(-1, 1, 1),
    Vector3(1, 1, -1),
    Vector3(-1, 1, -1),
]
)
def test_find_path_string_pull(c: Vector3) -> None:
    nm = NavigationMesh3d()

    nm.add_triangle(Triangle3d(
        Vector3(0, 0, 0) * c,
        Vector3(1, 0, 0) * c,
        Vector3(0, 0, 1) * c
    ))
    nm.add_triangle(Triangle3d(
        Vector3(0, 0, 0) * c,
        Vector3(0, 0, 1) * c,
        Vector3(-1, 0, 1) * c
    ))
    nm.add_triangle(Triangle3d(
        Vector3(-1, 0, 1) * c,
        Vector3(0, 0, 1) * c,
        Vector3(-1, 0, 2) * c
    ))
    nm.add_triangle(Triangle3d(
        Vector3(-1, 0, 1) * c,
        Vector3(-2, 0, 1) * c,
        Vector3(-1, 0, 2) * c
    ))
    nm.add_triangle(Triangle3d(
        Vector3(-1, 0, 0) * c,
        Vector3(-1, 0, 1) * c,
        Vector3(-2, 0, 1) * c
    ))
    nm.add_triangle(Triangle3d(
        Vector3(-1, 0, 0) * c,
        Vector3(-2, 0, 1) * c,
        Vector3(-2, 0, 0) * c
    ))
    nm.add_triangle(Triangle3d(
        Vector3(-1, 0, 0) * c,
        Vector3(0, 0, 0) * c,
        Vector3(0, 0, -1) * c
    ))
    nm.add_triangle(Triangle3d(
        Vector3(-1, 0, 0) * c,
        Vector3(-1, 0, -1) * c,
        Vector3(0, 0, -1) * c
    ))
    nm.add_triangle(Triangle3d(
        Vector3(-1, 0, 0) * c,
        Vector3(-1, 0, -1) * c,
        Vector3(-2, 0, 0) * c
    ))
    nm.add_triangle(Triangle3d(
        Vector3(0, 0, 0) * c,
        Vector3(0, 0, -1) * c,
        Vector3(1, 0, -1) * c
    ))
    nm.add_triangle(Triangle3d(
        Vector3(0, 0, -2) * c,
        Vector3(0, 0, -1) * c,
        Vector3(1, 0, -1) * c
    ))
    nm.add_triangle(Triangle3d(
        Vector3(0, 0, -2) * c,
        Vector3(-1, 0, -2) * c,
        Vector3(-1, 0, -3) * c
    ))
    nm.add_triangle(Triangle3d(
        Vector3(0, 0, -2) * c,
        Vector3(0, 0, -3) * c,
        Vector3(-1, 0, -3) * c
    ))
    nm.add_triangle(Triangle3d(
        Vector3(0, 0, -2) * c,
        Vector3(1, 0, -2) * c,
        Vector3(1, 0, -1) * c
    ))
    nm.add_triangle(Triangle3d(
        Vector3(0, 0, -2) * c,
        Vector3(1, 0, -2) * c,
        Vector3(0, 0, -3) * c
    ))

    path = nm.find_path(
        Vector3(1, 0, 0) * c,
        Triangle3d(
            Vector3(1, 0, 0) * c,
            Vector3(0, 0, 1) * c,
            Vector3(0, 0, 0) * c,
        ),
        Vector3(-1, 0, -2) * c,
        Triangle3d(
            Vector3(-1, 0, -2) * c,
            Vector3(-1, 0, -3) * c,
            Vector3(0, 0, -2) * c,
        )
    )
    assert path == (
        Vector3(1, 0, 0) * c,
        Vector3(-1, 0, 1) * c,
        Vector3(-1, 0, 0) * c,
        Vector3(0, 0, -1) * c,
        Vector3(0, 0, -2) * c,
        Vector3(-1, 0, -2) * c,
    )


def test_find_path_string_pull_y() -> None:
    nm = NavigationMesh3d()
    # _
    nm.add_triangle(Triangle3d(
        Vector3(0, 0, 0),
        Vector3(0, 0, 1),
        Vector3(1, 0, 1),
    ))
    nm.add_triangle(Triangle3d(
        Vector3(0, 0, 0),
        Vector3(1, 0, 0),
        Vector3(1, 0, 1),
    ))
    # __
    nm.add_triangle(Triangle3d(
        Vector3(1, 0, 0),
        Vector3(1, 0, 1),
        Vector3(2, 0, 1),
    ))
    nm.add_triangle(Triangle3d(
        Vector3(1, 0, 0),
        Vector3(2, 0, 0),
        Vector3(2, 0, 1),
    ))
    # __/
    nm.add_triangle(Triangle3d(
        Vector3(2, 0, 0),
        Vector3(2, 0, 1),
        Vector3(3, 1, 1),
    ))
    nm.add_triangle(Triangle3d(
        Vector3(2, 0, 0),
        Vector3(3, 1, 0),
        Vector3(3, 1, 1),
    ))
    #    _
    # __/
    nm.add_triangle(Triangle3d(
        Vector3(3, 1, 0),
        Vector3(3, 1, 1),
        Vector3(4, 1, 1),
    ))
    nm.add_triangle(Triangle3d(
        Vector3(3, 1, 0),
        Vector3(4, 1, 0),
        Vector3(4, 1, 1),
    ))
    #    __
    # __/
    nm.add_triangle(Triangle3d(
        Vector3(4, 1, 0),
        Vector3(4, 1, 1),
        Vector3(5, 1, 1),
    ))
    nm.add_triangle(Triangle3d(
        Vector3(4, 1, 0),
        Vector3(5, 1, 0),
        Vector3(5, 1, 1),
    ))
    #    __
    # __/  \
    nm.add_triangle(Triangle3d(
        Vector3(5, 1, 0),
        Vector3(5, 1, 1),
        Vector3(6, 0, 1),
    ))
    nm.add_triangle(Triangle3d(
        Vector3(5, 1, 0),
        Vector3(6, 0, 0),
        Vector3(6, 0, 1),
    ))
    #    __
    # __/  \_
    nm.add_triangle(Triangle3d(
        Vector3(6, 0, 0),
        Vector3(6, 0, 1),
        Vector3(7, 0, 1),
    ))
    nm.add_triangle(Triangle3d(
        Vector3(6, 0, 0),
        Vector3(7, 0, 0),
        Vector3(7, 0, 1),
    ))
    #    __
    # __/  \__
    nm.add_triangle(Triangle3d(
        Vector3(7, 0, 0),
        Vector3(7, 0, 1),
        Vector3(8, 0, 1),
    ))
    nm.add_triangle(Triangle3d(
        Vector3(7, 0, 0),
        Vector3(8, 0, 0),
        Vector3(8, 0, 1),
    ))
    #    __
    # s_/  \_e
    path = nm.find_path(
        Vector3(0, 0, 0),
        Triangle3d(
            Vector3(1, 0, 1),
            Vector3(0, 0, 0),
            Vector3(0, 0, 1),
        ),
        Vector3(8, 0, 1),
        Triangle3d(
            Vector3(8, 0, 1),
            Vector3(7, 0, 0),
            Vector3(8, 0, 0),
        )
    )
    assert vector_is_close(path[0], Vector3(0.0, 0.0, 0.0))
    assert vector_is_close(path[1], Vector3(2.0, 0.0, 0.25))
    assert vector_is_close(
        path[2],
        Vector3(2.2857142857142856, 0.2857142857142857, 0.2857142857142857)
    )
    assert vector_is_close(path[3], Vector3(3.0, 1.0, 0.3750000000000001))
    assert vector_is_close(path[4], Vector3(5.0, 1.0, 0.625))
    assert vector_is_close(
        path[5],
        Vector3(5.714285714285714, 0.2857142857142857, 0.7142857142857143)
    )
    assert vector_is_close(path[6], Vector3(6.0, 0.0, 0.75))
    assert vector_is_close(path[7], Vector3(8.0, 0.0, 1.0))
