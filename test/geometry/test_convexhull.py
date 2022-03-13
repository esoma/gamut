
# gamut
from gamut.geometry import ConvexHull
from gamut.math import Matrix4, Vector2, Vector3, Vector3Array, Vector4
# python
from math import radians
from typing import Any
# pytest
import pytest


def test_hash() -> None:
    array = Vector3Array(Vector3(1, 2, 3))
    c1 = ConvexHull(array)
    c2 = ConvexHull(array)
    assert hash(c1) != hash(c2)


def test_repr() -> None:
    c = ConvexHull(Vector3Array(Vector3(1, 2, 3)))
    assert repr(c) == '<gamut.geometry.ConvexHull>'


def test_no_points() -> None:
    with pytest.raises(ValueError) as excinfo:
        ConvexHull(Vector3Array())
    assert str(excinfo.value) == 'must have at least 1 point'


@pytest.mark.parametrize("points", [
    [Vector3(1)],
    [1],
    ['123'],
    [Vector2(1)],
    [Vector4(1)],
])
def test_points_invalid_type(points: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        ConvexHull(points)
    assert str(excinfo.value) == 'points must be Vector3Array'


@pytest.mark.parametrize("points", [
    Vector3Array(Vector3(0), Vector3(1), Vector3(2)),
    Vector3Array(Vector3(0)),
    Vector3Array(Vector3(1, 2, 3), Vector3(4, 5, 6)),
])
def test_points(points: Vector3Array) -> None:
    c = ConvexHull(points)
    assert isinstance(c.points, Vector3Array)
    assert c.points == points


@pytest.mark.parametrize("convex_hull", [
    ConvexHull(Vector3Array(Vector3(0, 0, 0), Vector3(0, 0, 0))),
    ConvexHull(Vector3Array(Vector3(-1, -2, -3), Vector3(1, 2, 3))),
])
@pytest.mark.parametrize("transform", [
    Matrix4(1).translate(Vector3(1, 0, 0)),
    Matrix4(1).translate(Vector3(0, 1, 0)),
    Matrix4(1).translate(Vector3(0, 0, 1)),
    Matrix4(1).rotate(radians(90), Vector3(1, 0, 0)),
    Matrix4(1).rotate(radians(90), Vector3(0, 1, 0)),
    Matrix4(1).rotate(radians(90), Vector3(0, 0, 1)),
    Matrix4(1).scale(Vector3(2, 3, 4)),
])
def test_transform(convex_hull: ConvexHull, transform: Matrix4) -> None:
    new_ch = transform @ convex_hull
    assert new_ch is not convex_hull
    assert new_ch.points == Vector3Array(
        *(transform @ p for p in convex_hull.points)
    )


@pytest.mark.parametrize("left_side", [None, 1, '123'])
def test_invalid_multiply(left_side: Any) -> None:
    with pytest.raises(TypeError):
        left_side @ ConvexHull(Vector3(0, 0, 0), Vector3(0, 0, 0))


def test_equal() -> None:
    c = ConvexHull(Vector3Array(Vector3(0, 0, 0), Vector3(0, 0, 0)))
    assert c == ConvexHull(Vector3Array(Vector3(0, 0, 0), Vector3(0, 0, 0)))
    assert c != ConvexHull(Vector3Array(Vector3(1, 0, 0), Vector3(0, 0, 0)))
    assert c != ConvexHull(Vector3Array(Vector3(0, 1, 0), Vector3(0, 0, 0)))
    assert c != ConvexHull(Vector3Array(Vector3(0, 0, 1), Vector3(0, 0, 0)))
    assert c != ConvexHull(Vector3Array(Vector3(0, 0, 0), Vector3(1, 0, 0)))
    assert c != ConvexHull(Vector3Array(Vector3(0, 0, 0), Vector3(0, 1, 0)))
    assert c != ConvexHull(Vector3Array(Vector3(0, 0, 0), Vector3(0, 0, 1)))
    assert c != object()
