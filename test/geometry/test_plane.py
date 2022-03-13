
# gamut
from gamut.geometry import Plane
from gamut.math import Matrix4, Vector2, Vector3, Vector4
# python
from math import radians
from typing import Any
# pytest
import pytest


def test_repr() -> None:
    plane = Plane(10, Vector3(.3, .7, 0))
    assert (
        repr(plane) ==
        f'<gamut.geometry.Plane distance={plane.distance} '
        f'normal=({plane.normal.x}, {plane.normal.y}, {plane.normal.z})>'
    )


@pytest.mark.parametrize("distance", [None, 'x', object()])
def test_invalid_distance(distance: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Plane(distance, Vector3(0, 1, 0))
    assert str(excinfo.value) == 'distance must be float'


@pytest.mark.parametrize("normal", [None, '123', 123, Vector4(1), Vector2(1)])
def test_invalid_normal_type(normal: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Plane(1, normal)
    assert str(excinfo.value) == 'normal must be Vector3'


def test_invalid_normal_value() -> None:
    with pytest.raises(ValueError) as excinfo:
        Plane(1, Vector3(0))
    assert str(excinfo.value) == 'invalid normal'


@pytest.mark.parametrize("distance", [1, 1.5, '2.0'])
def test_distance(distance: Any) -> None:
    plane = Plane(distance, Vector3(0, 2, 0))
    assert plane.distance == float(distance) / 2.0


@pytest.mark.parametrize("normal", [Vector3(1), Vector3(1, 2, 3)])
def test_normal(normal: Any) -> None:
    plane = Plane(1, normal)
    assert plane.normal == normal.normalize()
    assert plane.normal is not normal


@pytest.mark.parametrize("plane", [
    Plane(0, Vector3(1, 0, 0)),
    Plane(1, Vector3(0, 1, 0)),
    Plane(-1, Vector3(0, 0, 1)),
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
def test_transform(plane: Plane, transform: Matrix4) -> None:
    new_plane = transform @ plane
    assert new_plane is not plane

    p = transform.inverse().transpose() @ Vector4(
        *plane.normal,
        plane.distance
    )
    magnitude = p.xyz.magnitude
    assert new_plane.distance == p.w / magnitude
    assert new_plane.normal.x == pytest.approx(p.x / magnitude)
    assert new_plane.normal.y == pytest.approx(p.y / magnitude)
    assert new_plane.normal.z == pytest.approx(p.z / magnitude)


@pytest.mark.parametrize("transform", [None, 123, Vector4(1), Vector2(1)])
def test_transform_invalid(transform: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        transform @ Plane(1, Vector3(0, 1, 0))
    assert str(excinfo.value).startswith('unsupported operand type(s) for @:')


@pytest.mark.parametrize("plane", [
    Plane(0, Vector3(1, 0, 0)),
    Plane(1, Vector3(0, 1, 0)),
    Plane(-1, Vector3(0, 0, 1)),
])
@pytest.mark.parametrize("point", [
    Vector3(0),
    Vector3(1),
    Vector3(-1),
])
def test_distance_to_point(plane: Plane, point: Vector3) -> None:
    expected = plane.normal @ point + plane.distance
    assert (
        plane.distance_to_point(point) == pytest.approx(expected)
    )


@pytest.mark.parametrize("point", [None, '123', 123, Vector4(1), Vector2(1)])
def test_distance_to_point_invalid(point: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Plane(1, Vector3(0, 1, 0)).distance_to_point(point)
    assert str(excinfo.value) == 'point must be Vector3'


def test_equal() -> None:
    assert Plane(0, Vector3(0, 1, 0)) == Plane(0, Vector3(0, 1, 0))
    assert Plane(0, Vector3(0, 1, 0)) != Plane(1, Vector3(0, 1, 0))
    assert Plane(0, Vector3(0, 1, 0)) != Plane(0, Vector3(1, 0, 0))
    assert Plane(0, Vector3(0, 1, 0)) != Plane(0, Vector3(0, 0, 1))
    assert Plane(0, Vector3(0, 1, 0)) != object()
