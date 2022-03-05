
# gamut
from gamut.geometry import ConvexHull
# python
from typing import Any
# pyglm
from glm import mat4, radians, rotate, scale, translate, vec2, vec3, vec4
# pytest
import pytest


def test_hash() -> None:
    c1 = ConvexHull(vec3(1, 2, 3))
    c2 = ConvexHull(vec3(1, 2, 3))
    assert hash(c1) != hash(c2)


def test_repr() -> None:
    c = ConvexHull(vec3(1, 2, 3))
    assert repr(c) == '<gamut.geometry.ConvexHull>'


def test_no_points() -> None:
    with pytest.raises(ValueError) as excinfo:
        ConvexHull()
    assert str(excinfo.value) == 'must have at least 1 point'


@pytest.mark.parametrize("good_points", [
    [],
    [vec3(0)],
    [vec3(0), vec3(0)],
])
@pytest.mark.parametrize("points", [
    [None],
    [1],
    ['123'],
    [vec2(1)],
    [vec4(1)],
])
def test_points_invalid_type(good_points: Any, points: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        ConvexHull(*good_points, *points)
    assert str(excinfo.value) == 'each point must be vec3'


@pytest.mark.parametrize("points", [
    [vec3(0), vec3(1), vec3(2)],
    [vec3(0)],
    [(1, 2, 3), (4, 5, 6)]
])
def test_points(points: Any) -> None:
    c = ConvexHull(*points)
    assert c.points == tuple(vec3(p) for p in points)


@pytest.mark.parametrize("convex_hull", [
    ConvexHull(vec3(0, 0, 0), vec3(0, 0, 0)),
    ConvexHull(vec3(-1, -2, -3), vec3(1, 2, 3)),
])
@pytest.mark.parametrize("transform", [
    translate(mat4(1), vec3(1, 0, 0)),
    translate(mat4(1), vec3(0, 1, 0)),
    translate(mat4(1), vec3(0, 0, 1)),
    rotate(mat4(1), radians(90), vec3(1, 0, 0)),
    rotate(mat4(1), radians(90), vec3(0, 1, 0)),
    rotate(mat4(1), radians(90), vec3(0, 0, 1)),
    scale(mat4(1), vec3(2, 3, 4)),
])
def test_transform(convex_hull: ConvexHull, transform: mat4) -> None:
    new_ch = transform * convex_hull
    assert new_ch is not convex_hull
    assert new_ch.points == tuple(transform * p for p in convex_hull.points)


@pytest.mark.parametrize("left_side", [None, 1, '123'])
def test_invalid_multiply(left_side: Any) -> None:
    with pytest.raises(TypeError):
        left_side * ConvexHull(vec3(0, 0, 0), vec3(0, 0, 0))


def test_equal() -> None:
    c = ConvexHull(vec3(0, 0, 0), vec3(0, 0, 0))
    assert c == ConvexHull(vec3(0, 0, 0), vec3(0, 0, 0))
    assert c != ConvexHull(vec3(1, 0, 0), vec3(0, 0, 0))
    assert c != ConvexHull(vec3(0, 1, 0), vec3(0, 0, 0))
    assert c != ConvexHull(vec3(0, 0, 1), vec3(0, 0, 0))
    assert c != ConvexHull(vec3(0, 0, 0), vec3(1, 0, 0))
    assert c != ConvexHull(vec3(0, 0, 0), vec3(0, 1, 0))
    assert c != ConvexHull(vec3(0, 0, 0), vec3(0, 0, 1))
    assert c != object()
