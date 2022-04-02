
# gamut
from gamut.graph import NavigationMesh3d
from gamut.math import Vector3
# pytest
import pytest


def test_find_basic_path() -> None:
    nm = NavigationMesh3d()

    nm.add_triangle(Vector3(0, 0, 0), Vector3(0, 0, 1), Vector3(1, 0, 0))
    nm.add_triangle(Vector3(0, 0, 0), Vector3(0, 0, 1), Vector3(-1, 0, 0))
    nm.add_triangle(Vector3(1, 0, 1), Vector3(0, 0, 1), Vector3(1, 0, 0))
    nm.add_triangle(Vector3(0, 0, 0), Vector3(-1, 0, 0), Vector3(1, 0, 0))

    assert nm.contains_triangle(
        Vector3(0, 0, 0),
        Vector3(0, 0, 1),
        Vector3(1, 0, 0)
    )
    assert nm.contains_triangle(
        Vector3(0, 0, 0),
        Vector3(0, 0, 1),
        Vector3(-1, 0, 0)
    )
    assert nm.contains_triangle(
        Vector3(1, 0, 1),
        Vector3(0, 0, 1),
        Vector3(1, 0, 0)
    )
    assert nm.contains_triangle(
        Vector3(0, 0, 0),
        Vector3(-1, 0, 0),
        Vector3(1, 0, 0)
    )

    triangles = list(set(t) for t in nm.triangles)
    assert {Vector3(0, 0, 0), Vector3(0, 0, 1), Vector3(1, 0, 0)} in triangles
    assert {Vector3(0, 0, 0), Vector3(0, 0, 1), Vector3(-1, 0, 0)} in triangles
    assert {Vector3(1, 0, 1), Vector3(0, 0, 1), Vector3(1, 0, 0)} in triangles
    assert {Vector3(0, 0, 0), Vector3(-1, 0, 0), Vector3(1, 0, 0)} in triangles

    path = nm.find_path(
        (Vector3(0, 0, 0), Vector3(0, 0, 1), Vector3(1, 0, 0)),
        (Vector3(1, 0, 1), Vector3(0, 0, 1), Vector3(1, 0, 0))
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

    nm.add_triangle(
        Vector3(0, 0, 0) * c,
        Vector3(1, 0, 0) * c,
        Vector3(0, 0, 1) * c
    )
    nm.add_triangle(
        Vector3(0, 0, 0) * c,
        Vector3(0, 0, 1) * c,
        Vector3(-1, 0, 1) * c
    )
    nm.add_triangle(
        Vector3(-1, 0, 1) * c,
        Vector3(0, 0, 1) * c,
        Vector3(-1, 0, 2) * c
    )
    nm.add_triangle(
        Vector3(-1, 0, 1) * c,
        Vector3(-2, 0, 1) * c,
        Vector3(-1, 0, 2) * c
    )
    nm.add_triangle(
        Vector3(-1, 0, 0) * c,
        Vector3(-1, 0, 1) * c,
        Vector3(-2, 0, 1) * c
    )
    nm.add_triangle(
        Vector3(-1, 0, 0) * c,
        Vector3(-2, 0, 1) * c,
        Vector3(-2, 0, 0) * c
    )
    nm.add_triangle(
        Vector3(-1, 0, 0) * c,
        Vector3(0, 0, 0) * c,
        Vector3(0, 0, -1) * c
    )
    nm.add_triangle(
        Vector3(-1, 0, 0) * c,
        Vector3(-1, 0, -1) * c,
        Vector3(0, 0, -1) * c
    )
    nm.add_triangle(
        Vector3(-1, 0, 0) * c,
        Vector3(-1, 0, -1) * c,
        Vector3(-2, 0, 0) * c
    )
    nm.add_triangle(
        Vector3(0, 0, 0) * c,
        Vector3(0, 0, -1) * c,
        Vector3(1, 0, -1) * c
    )
    nm.add_triangle(
        Vector3(0, 0, -2) * c,
        Vector3(0, 0, -1) * c,
        Vector3(1, 0, -1) * c
    )
    nm.add_triangle(
        Vector3(0, 0, -2) * c,
        Vector3(-1, 0, -2) * c,
        Vector3(-1, 0, -3) * c
    )
    nm.add_triangle(
        Vector3(0, 0, -2) * c,
        Vector3(0, 0, -3) * c,
        Vector3(-1, 0, -3) * c
    )
    nm.add_triangle(
        Vector3(0, 0, -2) * c,
        Vector3(1, 0, -2) * c,
        Vector3(1, 0, -1) * c
    )
    nm.add_triangle(
        Vector3(0, 0, -2) * c,
        Vector3(1, 0, -2) * c,
        Vector3(0, 0, -3) * c
    )

    path = nm.find_path(
        (Vector3(1, 0, 0) * c, Vector3(0, 0, 0) * c, Vector3(0, 0, 1) * c),
        (Vector3(-1, 0, -2) * c, Vector3(0, 0, -2) * c, Vector3(-1, 0, -3) * c)
    )
    assert path == (
        Vector3(1, 0, 0) * c,
        Vector3(-1, 0, 1) * c,
        Vector3(-1, 0, 0) * c,
        Vector3(0, 0, -1) * c,
        Vector3(0, 0, -2) * c,
        Vector3(-1, 0, -2) * c,
    )
