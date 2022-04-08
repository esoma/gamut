
# gamut
from gamut.geometry import Capsule
from gamut.math import (DQuaternion, DVector3, FQuaternion, FVector3, Vector2,
                        Vector4)
# python
from typing import Any
# pytest
import pytest


def test_hash() -> None:
    c1 = Capsule(DVector3(1, 2, 3), 4, 5, rotation=DQuaternion(6, 7, 8, 9))
    c2 = Capsule(DVector3(1, 2, 3), 4, 5, rotation=DQuaternion(6, 7, 8, 9))
    assert hash(c1) != hash(c2)


@pytest.mark.parametrize("capsule", [
    Capsule(FVector3(1, 2, 3), 4, 5, rotation=FQuaternion(6, 7, 8, 9)),
    Capsule(DVector3(1, 2, 3), 4, 5, rotation=DQuaternion(6, 7, 8, 9))
])
def test_repr(capsule: Capsule) -> None:
    assert (
        repr(capsule) ==
        f'<gamut.geometry.Capsule center=(1.0, 2.0, 3.0) radius=4.0 '
        f'height=5.0 rotation=(6.0, 7.0, 8.0, 9.0)>'
    )


@pytest.mark.parametrize("radius", [None, 'x', object()])
def test_invalid_radius(radius: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Capsule(DVector3(0), radius, 1.0)
    assert str(excinfo.value) == 'radius must be float'


@pytest.mark.parametrize("height", [None, 'x', object()])
def test_invalid_height(height: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Capsule(DVector3(0), 1.0, height)
    assert str(excinfo.value) == 'height must be float'


@pytest.mark.parametrize("center", [None, '123', 123, Vector4(1), Vector2(1)])
def test_invalid_center(center: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Capsule(center, 0, 0)
    assert str(excinfo.value) == 'center must be FVector3 or DVector3'


@pytest.mark.parametrize("rotation", ['123', 123, DVector3(1), Vector2(1)])
def test_invalid_rotation(rotation: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Capsule(DVector3(0), 0, 0, rotation=rotation)
    assert str(excinfo.value) == 'rotation must be DQuaternion'


def test_different_rotation() -> None:
    with pytest.raises(TypeError) as excinfo:
        Capsule(FVector3(0), 0, 0, rotation=DQuaternion(1))
    assert str(excinfo.value) == 'rotation must be FQuaternion'

    with pytest.raises(TypeError) as excinfo:
        Capsule(DVector3(0), 0, 0, rotation=FQuaternion(1))
    assert str(excinfo.value) == 'rotation must be DQuaternion'


@pytest.mark.parametrize("radius", [-1, 1, -1.5, 1.5, '-2.0', '2.0'])
def test_radius(radius: Any) -> None:
    capsule = Capsule(DVector3(0), radius, 1.0)
    assert capsule.radius == abs(float(radius))


@pytest.mark.parametrize("height", [-1, 1, -1.5, 1.5, '-2.0', '2.0'])
def test_height(height: Any) -> None:
    capsule = Capsule(DVector3(0), 1.0, height)
    assert capsule.height == abs(float(height))


@pytest.mark.parametrize("center", [
    FVector3(1),
    FVector3(1, 2, 3),
    DVector3(1),
    DVector3(1, 2, 3)
])
def test_center(center: Any) -> None:
    capsule = Capsule(center, 1, 1)
    assert capsule.center == center


@pytest.mark.parametrize("center, rotation", [
    (FVector3(0), FQuaternion(2)),
    (FVector3(0), FQuaternion(-2)),
    (DVector3(0), DQuaternion(2)),
    (DVector3(0), DQuaternion(-2)),
])
def test_rotation(center: Any, rotation: Any) -> None:
    capsule = Capsule(center, 1, 1, rotation=rotation)
    assert capsule.rotation == rotation


def test_default_rotation() -> None:
    capsule = Capsule(FVector3(0), 1, 1)
    assert capsule.rotation == FQuaternion(1)

    capsule = Capsule(DVector3(0), 1, 1)
    assert capsule.rotation == DQuaternion(1)


def test_equal() -> None:
    assert Capsule(DVector3(0), 0, 0) == Capsule(DVector3(0), 0, 0)
    assert Capsule(DVector3(0), 0, 0) != Capsule(
        DVector3(0), 0, 0, rotation=DQuaternion(0)
    )
    assert Capsule(DVector3(0), 0, 0) != Capsule(DVector3(1, 0, 0), 0, 0)
    assert Capsule(DVector3(0), 0, 0) != Capsule(DVector3(0, 1, 0), 0, 0)
    assert Capsule(DVector3(0), 0, 0) != Capsule(DVector3(0, 0, 1), 0, 0)
    assert Capsule(DVector3(0), 0, 0) != Capsule(DVector3(0), 1, 0)
    assert Capsule(DVector3(0), 0, 0) != Capsule(DVector3(0), 0, 1)
    assert Capsule(DVector3(0), 0, 0) != object()
