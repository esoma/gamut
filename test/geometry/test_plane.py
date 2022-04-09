
# gamut
from gamut.geometry import Plane
from gamut.math import (DMatrix4, DVector2, DVector3, DVector4, FMatrix4,
                        FVector3, FVector4)
# python
from math import radians
from typing import Any
# pytest
import pytest


def test_hash() -> None:
    p1 = Plane(10, DVector3(.3, .7, 0))
    p2 = Plane(10, DVector3(.3, .7, 0))
    assert hash(p1) != hash(p2)


def test_repr() -> None:
    plane = Plane(10, DVector3(.3, .7, 0))
    assert (
        repr(plane) ==
        f'<gamut.geometry.Plane distance={plane.distance} '
        f'normal=({plane.normal.x}, {plane.normal.y}, {plane.normal.z})>'
    )


@pytest.mark.parametrize("distance", [None, 'x', object()])
def test_invalid_distance(distance: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Plane(distance, DVector3(0, 1, 0))
    assert str(excinfo.value) == 'distance must be float'


@pytest.mark.parametrize("normal", [
    None,
    '123',
    123,
    DVector4(1),
    DVector2(1)
])
def test_invalid_normal_type(normal: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Plane(1, normal)
    assert str(excinfo.value) == 'normal must be FVector3 or DVector3'


def test_invalid_normal_value() -> None:
    with pytest.raises(ValueError) as excinfo:
        Plane(1, DVector3(0))
    assert str(excinfo.value) == 'invalid normal'


@pytest.mark.parametrize("distance", [1, 1.5, '2.0'])
def test_distance(distance: Any) -> None:
    plane = Plane(distance, FVector3(0, 2, 0))
    assert plane.distance == float(distance) / 2.0
    plane = Plane(distance, DVector3(0, 2, 0))
    assert plane.distance == float(distance) / 2.0


@pytest.mark.parametrize("normal", [
    FVector3(1),
    FVector3(1, 2, 3),
    DVector3(1),
    DVector3(1, 2, 3)
])
def test_normal(normal: Any) -> None:
    plane = Plane(1, normal)
    assert plane.normal == normal.normalize()
    assert plane.normal is not normal


@pytest.mark.parametrize("plane", [
    Plane(0, DVector3(1, 0, 0)),
    Plane(1, DVector3(0, 1, 0)),
    Plane(-1, DVector3(0, 0, 1)),
])
@pytest.mark.parametrize("transform", [
    DMatrix4(1).translate(DVector3(1, 0, 0)),
    DMatrix4(1).translate(DVector3(0, 1, 0)),
    DMatrix4(1).translate(DVector3(0, 0, 1)),
    DMatrix4(1).rotate(radians(90), DVector3(1, 0, 0)),
    DMatrix4(1).rotate(radians(90), DVector3(0, 1, 0)),
    DMatrix4(1).rotate(radians(90), DVector3(0, 0, 1)),
    DMatrix4(1).scale(DVector3(2, 3, 4)),
])
def test_d_transform(plane: Plane, transform: DMatrix4) -> None:
    new_plane = transform @ plane
    assert new_plane is not plane

    p = transform.inverse().transpose() @ DVector4(
        *plane.normal,
        plane.distance
    )
    magnitude = p.xyz.magnitude
    assert new_plane.distance == p.w / magnitude
    assert new_plane.normal.x == pytest.approx(p.x / magnitude)
    assert new_plane.normal.y == pytest.approx(p.y / magnitude)
    assert new_plane.normal.z == pytest.approx(p.z / magnitude)


@pytest.mark.parametrize("plane", [
    Plane(0, FVector3(1, 0, 0)),
    Plane(1, FVector3(0, 1, 0)),
    Plane(-1, FVector3(0, 0, 1)),
])
@pytest.mark.parametrize("transform", [
    FMatrix4(1).translate(FVector3(1, 0, 0)),
    FMatrix4(1).translate(FVector3(0, 1, 0)),
    FMatrix4(1).translate(FVector3(0, 0, 1)),
    FMatrix4(1).rotate(radians(90), FVector3(1, 0, 0)),
    FMatrix4(1).rotate(radians(90), FVector3(0, 1, 0)),
    FMatrix4(1).rotate(radians(90), FVector3(0, 0, 1)),
    FMatrix4(1).scale(FVector3(2, 3, 4)),
])
def test_f_transform(plane: Plane, transform: Any) -> None:
    new_plane = transform @ plane
    assert new_plane is not plane

    p = transform.inverse().transpose() @ FVector4(
        *plane.normal,
        plane.distance
    )
    magnitude = p.xyz.magnitude
    assert new_plane.distance == p.w / magnitude
    assert new_plane.normal.x == pytest.approx(p.x / magnitude)
    assert new_plane.normal.y == pytest.approx(p.y / magnitude)
    assert new_plane.normal.z == pytest.approx(p.z / magnitude)


@pytest.mark.parametrize("transform", [None, 123, DVector4(1), DVector2(1)])
def test_transform_invalid(transform: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        transform @ Plane(1, DVector3(0, 1, 0))
    assert str(excinfo.value).startswith('unsupported operand type(s) for @:')


def test_transform_wrong_type():
    with pytest.raises(TypeError) as excinfo:
        DMatrix4(1) @ Plane(0, FVector3(1, 0, 0))
    assert str(excinfo.value).startswith('unsupported operand type(s) for @:')

    with pytest.raises(TypeError) as excinfo:
        FMatrix4(1) @ Plane(0, DVector3(1, 0, 0))
    assert str(excinfo.value).startswith('unsupported operand type(s) for @:')


@pytest.mark.parametrize("plane", [
    Plane(0, DVector3(1, 0, 0)),
    Plane(1, DVector3(0, 1, 0)),
    Plane(-1, DVector3(0, 0, 1)),
])
@pytest.mark.parametrize("point", [
    DVector3(0),
    DVector3(1),
    DVector3(-1),
])
def test_d_distance_to_point(plane: Plane, point: DVector3) -> None:
    expected = plane.normal @ point + plane.distance
    assert (
        plane.distance_to_point(point) == pytest.approx(expected)
    )


@pytest.mark.parametrize("plane", [
    Plane(0, FVector3(1, 0, 0)),
    Plane(1, FVector3(0, 1, 0)),
    Plane(-1, FVector3(0, 0, 1)),
])
@pytest.mark.parametrize("point", [
    FVector3(0),
    FVector3(1),
    FVector3(-1),
])
def test_f_distance_to_point(plane: Plane, point: FVector3) -> None:
    expected = plane.normal @ point + plane.distance
    assert (
        plane.distance_to_point(point) == pytest.approx(expected)
    )


@pytest.mark.parametrize("point", [None, '123', 123, DVector4(1), DVector2(1)])
def test_distance_to_point_invalid(point: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Plane(1, DVector3(0, 1, 0)).distance_to_point(point)
    assert str(excinfo.value) == 'point must be DVector3'


def test_distance_to_point_wrong_type():
    with pytest.raises(TypeError) as excinfo:
        Plane(0, FVector3(1, 0, 0)).distance_to_point(DVector3(0))
    assert str(excinfo.value).startswith('point must be FVector3')

    with pytest.raises(TypeError) as excinfo:
        Plane(0, DVector3(1, 0, 0)).distance_to_point(FVector3(0))
    assert str(excinfo.value).startswith('point must be DVector3')


def test_equal() -> None:
    assert Plane(0, DVector3(0, 1, 0)) == Plane(0, DVector3(0, 1, 0))
    assert Plane(0, FVector3(0, 1, 0)) == Plane(0, FVector3(0, 1, 0))
    assert Plane(0, DVector3(0, 1, 0)) != Plane(0, FVector3(0, 1, 0))
    assert Plane(0, DVector3(0, 1, 0)) != Plane(1, DVector3(0, 1, 0))
    assert Plane(0, DVector3(0, 1, 0)) != Plane(0, DVector3(1, 0, 0))
    assert Plane(0, DVector3(0, 1, 0)) != Plane(0, DVector3(0, 0, 1))
    assert Plane(0, DVector3(0, 1, 0)) != object()
