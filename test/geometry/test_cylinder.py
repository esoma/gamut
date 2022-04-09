
# gamut
from gamut.geometry import Cylinder
from gamut.math import (DQuaternion, DVector2, DVector3, DVector4, FQuaternion,
                        FVector3)
# python
from typing import Any
# pytest
import pytest


def test_hash() -> None:
    c1 = Cylinder(DVector3(1, 2, 3), 4, 5, rotation=DQuaternion(6, 7, 8, 9))
    c2 = Cylinder(DVector3(1, 2, 3), 4, 5, rotation=DQuaternion(6, 7, 8, 9))
    assert hash(c1) != hash(c2)

@pytest.mark.parametrize("cylinder", [
    Cylinder(
        FVector3(1, 2, 3),
        4,
        5,
        rotation=FQuaternion(6, 7, 8, 9)
    ),
    Cylinder(
        DVector3(1, 2, 3),
        4,
        5,
        rotation=DQuaternion(6, 7, 8, 9)
    )
])
def test_repr(cylinder: Cylinder) -> None:
    assert (
        repr(cylinder) ==
        f'<gamut.geometry.Cylinder center=(1.0, 2.0, 3.0) radius=4.0 '
        f'height=5.0 rotation=(6.0, 7.0, 8.0, 9.0)>'
    )


@pytest.mark.parametrize("radius", [None, 'x', object()])
def test_invalid_radius(radius: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Cylinder(DVector3(0), radius, 1.0)
    assert str(excinfo.value) == 'radius must be float'


@pytest.mark.parametrize("height", [None, 'x', object()])
def test_invalid_height(height: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Cylinder(DVector3(0), 1.0, height)
    assert str(excinfo.value) == 'height must be float'


@pytest.mark.parametrize("center", [
    None,
    '123',
    123,
    DVector4(1),
    DVector2(1)
])
def test_invalid_center(center: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Cylinder(center, 0, 0)
    assert str(excinfo.value) == 'center must be FVector3 or DVector3'


@pytest.mark.parametrize("rotation", ['123', 123, DVector3(1), DVector2(1)])
def test_invalid_rotation(rotation: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Cylinder(DVector3(0), 0, 0, rotation=rotation)
    assert str(excinfo.value) == 'rotation must be DQuaternion'


def test_different_rotation() -> None:
    with pytest.raises(TypeError) as excinfo:
        Cylinder(FVector3(0), 0, 0, rotation=DQuaternion(1))
    assert str(excinfo.value) == 'rotation must be FQuaternion'

    with pytest.raises(TypeError) as excinfo:
        Cylinder(DVector3(0), 0, 0, rotation=FQuaternion(1))
    assert str(excinfo.value) == 'rotation must be DQuaternion'


@pytest.mark.parametrize("radius", [-1, 1, -1.5, 1.5, '-2.0', '2.0'])
def test_radius(radius: Any) -> None:
    cylinder = Cylinder(DVector3(0), radius, 1.0)
    assert cylinder.radius == abs(float(radius))


@pytest.mark.parametrize("height", [-1, 1, -1.5, 1.5, '-2.0', '2.0'])
def test_height(height: Any) -> None:
    cylinder = Cylinder(DVector3(0), 1.0, height)
    assert cylinder.height == abs(float(height))


@pytest.mark.parametrize("center", [
    FVector3(1),
    FVector3(1, 2, 3),
    DVector3(1),
    DVector3(1, 2, 3)
])
def test_center(center: Any) -> None:
    cylinder = Cylinder(center, 1, 1)
    assert cylinder.center == center


@pytest.mark.parametrize("center, rotation", [
    (FVector3(0), FQuaternion(2)),
    (FVector3(0), FQuaternion(-2)),
    (DVector3(0), DQuaternion(2)),
    (DVector3(0), DQuaternion(-2)),
])
def test_rotation(center: Any, rotation: Any) -> None:
    cylinder = Cylinder(center, 1, 1, rotation=rotation)
    assert cylinder.rotation == rotation


def test_default_rotation() -> None:
    cylinder = Cylinder(FVector3(0), 1, 1)
    assert cylinder.rotation == FQuaternion(1)

    cylinder = Cylinder(DVector3(0), 1, 1)
    assert cylinder.rotation == DQuaternion(1)


def test_equal() -> None:
    assert Cylinder(DVector3(0), 0, 0) == Cylinder(DVector3(0), 0, 0)
    assert Cylinder(FVector3(0), 0, 0) == Cylinder(FVector3(0), 0, 0)
    assert Cylinder(DVector3(0), 0, 0) != Cylinder(FVector3(0), 0, 0)
    assert Cylinder(DVector3(0), 0, 0) != Cylinder(
        DVector3(0), 0, 0, rotation=DQuaternion(0)
    )
    assert Cylinder(DVector3(0), 0, 0) != Cylinder(DVector3(1, 0, 0), 0, 0)
    assert Cylinder(DVector3(0), 0, 0) != Cylinder(DVector3(0, 1, 0), 0, 0)
    assert Cylinder(DVector3(0), 0, 0) != Cylinder(DVector3(0, 0, 1), 0, 0)
    assert Cylinder(DVector3(0), 0, 0) != Cylinder(DVector3(0), 1, 0)
    assert Cylinder(DVector3(0), 0, 0) != Cylinder(DVector3(0), 0, 1)
    assert Cylinder(DVector3(0), 0, 0) != object()
