
# gamut
from gamut.geometry import Plane
# python
from typing import Any
# pyglm
from glm import (dot, inverse, length, mat4, normalize, radians, rotate, scale,
                 translate, transpose, vec2, vec3, vec4)
# pytest
import pytest


def test_repr() -> None:
    plane = Plane(10, vec3(.3, .7, 0))
    assert (
        repr(plane) ==
        f'<gamut.geometry.Plane distance={plane.distance} '
        f'normal=({plane.normal.x}, {plane.normal.y}, {plane.normal.z})>'
    )


@pytest.mark.parametrize("distance", [None, 'x', object()])
def test_invalid_distance(distance: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Plane(distance, vec3(0, 1, 0))
    assert str(excinfo.value) == 'distance must be float'


@pytest.mark.parametrize("normal", [None, '123', 123, vec4(1), vec2(1)])
def test_invalid_normal_type(normal: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Plane(1, normal)
    assert str(excinfo.value) == 'normal must be vec3'


def test_invalid_normal_value() -> None:
    with pytest.raises(ValueError) as excinfo:
        Plane(1, vec3(0))
    assert str(excinfo.value) == 'invalid normal'


@pytest.mark.parametrize("distance", [1, 1.5, '2.0'])
def test_distance(distance: Any) -> None:
    plane = Plane(distance, vec3(0, 2, 0))
    assert plane.distance == float(distance) / 2.0


@pytest.mark.parametrize("normal", [vec3(1), (1, 2, 3)])
def test_normal(normal: Any) -> None:
    plane = Plane(1, normal)
    assert plane.normal == normalize(normal)
    assert plane.normal is not normal


@pytest.mark.parametrize("plane", [
    Plane(0, vec3(1, 0, 0)),
    Plane(1, vec3(0, 1, 0)),
    Plane(-1, vec3(0, 0, 1)),
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
def test_transform(plane: Plane, transform: mat4) -> None:
    new_plane = transform * plane
    assert new_plane is not plane

    p = transpose(inverse(transform)) * vec4(plane.normal, plane.distance)
    magnitude = length(p.xyz)
    assert new_plane.distance == p.w / magnitude
    assert new_plane.normal.x == pytest.approx(p.x / magnitude)
    assert new_plane.normal.y == pytest.approx(p.y / magnitude)
    assert new_plane.normal.z == pytest.approx(p.z / magnitude)


@pytest.mark.parametrize("transform", [None, 123, vec4(1), vec2(1)])
def test_transform_invalid(transform: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        transform * Plane(1, vec3(0, 1, 0))
    assert str(excinfo.value).startswith('unsupported operand type(s) for *:')


@pytest.mark.parametrize("plane", [
    Plane(0, vec3(1, 0, 0)),
    Plane(1, vec3(0, 1, 0)),
    Plane(-1, vec3(0, 0, 1)),
])
@pytest.mark.parametrize("point", [
    vec3(0),
    vec3(1),
    vec3(-1),
])
@pytest.mark.parametrize("point_type", [
    vec3,
    tuple,
    list
])
def test_distance_to_point(plane: Plane, point: vec3, point_type: Any) -> None:
    expected = dot(plane.normal, point) + plane.distance
    assert (
        plane.distance_to_point(point_type(point)) == pytest.approx(expected)
    )


@pytest.mark.parametrize("point", [None, '123', 123, vec4(1), vec2(1)])
def test_distance_to_point_invalid(point: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Plane(1, vec3(0, 1, 0)).distance_to_point(point)
    assert str(excinfo.value) == 'point must be vec3'


def test_equal() -> None:
    assert Plane(0, vec3(0, 1, 0)) == Plane(0, vec3(0, 1, 0))
    assert Plane(0, vec3(0, 1, 0)) != Plane(1, vec3(0, 1, 0))
    assert Plane(0, vec3(0, 1, 0)) != Plane(0, vec3(1, 0, 0))
    assert Plane(0, vec3(0, 1, 0)) != Plane(0, vec3(0, 0, 1))
    assert Plane(0, vec3(0, 1, 0)) != object()
