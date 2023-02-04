from __future__ import annotations
# gamut
from gamut.geometry import (Capsule, Circle3d, DegenerateGeometryError,
                            LineSegment3d)
from gamut.math import (DQuaternion, DVector2, DVector3, DVector4, FQuaternion,
                        FVector3)
# python
from math import radians
from typing import Any
# pytest
import pytest


def test_hash() -> None:
    c1 = Capsule(DVector3(1, 2, 3), 4, 5, rotation=DQuaternion(6, 7, 8, 9))
    c2 = Capsule(DVector3(1, 2, 3), 4, 5, rotation=DQuaternion(6, 7, 8, 9))
    assert hash(c1) == hash(c2)
    c3 = Capsule(FVector3(1, 2, 3), 4, 5)
    assert hash(c1) != hash(c3)


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


@pytest.mark.parametrize("center", [
    None,
    '123',
    123,
    DVector4(1),
    DVector2(1)
])
def test_invalid_center(center: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Capsule(center, 1, 1)
    assert str(excinfo.value) == 'center must be FVector3 or DVector3'


@pytest.mark.parametrize("rotation", ['123', 123, DVector3(1), DVector2(1)])
def test_invalid_rotation(rotation: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Capsule(DVector3(0), 1, 1, rotation=rotation)
    assert str(excinfo.value) == 'rotation must be DQuaternion'


@pytest.mark.parametrize("center, radius, height, rotation, degenerate_form", [
    (
        FVector3(0),
        0,
        1,
        None,
        LineSegment3d(FVector3(0, -1, 0), FVector3(0, 1, 0))
    ),
    (
        FVector3(0),
        0,
        1,
        FQuaternion(1).rotate(radians(90), FVector3(1, 0, 0)),
        LineSegment3d(
            FQuaternion(1).rotate(radians(90), FVector3(1, 0, 0)) @
            FVector3(0, -1, 0),
            FQuaternion(1).rotate(radians(90), FVector3(1, 0, 0)) @
            FVector3(0, 1, 0)
        )
    ),
    (
        FVector3(0),
        1,
        0,
        None,
        Circle3d(FVector3(0), 1, FVector3(0, 1, 0))
    ),
    (
        FVector3(0),
        1,
        0,
        FQuaternion(1).rotate(radians(90), FVector3(1, 0, 0)),
        Circle3d(
            FVector3(0),
            1,
            FQuaternion(1).rotate(radians(90), FVector3(1, 0, 0)) @
            FVector3(0, 1, 0)
        )
    ),
    (
        FVector3(0),
        0,
        0,
        None,
        FVector3(0)
    ),
    (
        DVector3(0),
        0,
        1,
        None,
        LineSegment3d(DVector3(0, -1, 0), DVector3(0, 1, 0))
    ),
    (
        DVector3(0),
        0,
        1,
        DQuaternion(1).rotate(radians(90), DVector3(1, 0, 0)),
        LineSegment3d(
            DQuaternion(1).rotate(radians(90), DVector3(1, 0, 0)) @
            DVector3(0, -1, 0),
            DQuaternion(1).rotate(radians(90), DVector3(1, 0, 0)) @
            DVector3(0, 1, 0)
        )
    ),
    (
        DVector3(0),
        1,
        0,
        None,
        Circle3d(DVector3(0), 1, DVector3(0, 1, 0))
    ),
    (
        DVector3(0),
        1,
        0,
        DQuaternion(1).rotate(radians(90), DVector3(1, 0, 0)),
        Circle3d(
            DVector3(0),
            1,
            DQuaternion(1).rotate(radians(90), DVector3(1, 0, 0)) @
            DVector3(0, 1, 0)
        )
    ),
    (
        DVector3(0),
        0,
        0,
        None,
        DVector3(0)
    )
])
def test_degenerate(
    center: Any,
    radius: float,
    height: float,
    rotation: Any,
    degenerate_form: Any
) -> None:
    with pytest.raises(Capsule.DegenerateError) as excinfo:
        Capsule(center, radius, height, rotation=rotation)
    assert str(excinfo.value) == 'degenerate capsule'
    assert excinfo.value.degenerate_form == degenerate_form


def test_degenerate_error():
    assert issubclass(Capsule.DegenerateError, DegenerateGeometryError)


def test_different_rotation() -> None:
    with pytest.raises(TypeError) as excinfo:
        Capsule(FVector3(0), 1, 1, rotation=DQuaternion(1))
    assert str(excinfo.value) == 'rotation must be FQuaternion'

    with pytest.raises(TypeError) as excinfo:
        Capsule(DVector3(0), 1, 1, rotation=FQuaternion(1))
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
    assert Capsule(DVector3(0), 1, 1) == Capsule(DVector3(0), 1, 1)
    assert Capsule(FVector3(0), 1, 1) == Capsule(FVector3(0), 1, 1)
    assert Capsule(DVector3(0), 1, 1) != Capsule(FVector3(0), 1, 1)
    assert Capsule(DVector3(0), 1, 1) != Capsule(
        DVector3(0), 1, 1, rotation=DQuaternion(0)
    )
    assert Capsule(DVector3(0), 1, 1) != Capsule(DVector3(1, 0, 0), 1, 1)
    assert Capsule(DVector3(0), 1, 1) != Capsule(DVector3(0, 1, 0), 1, 1)
    assert Capsule(DVector3(0), 1, 1) != Capsule(DVector3(0, 0, 1), 1, 1)
    assert Capsule(DVector3(0), 1, 1) != Capsule(DVector3(0), 2, 1)
    assert Capsule(DVector3(0), 1, 1) != Capsule(DVector3(0), 1, 2)
    assert Capsule(DVector3(0), 1, 1) != object()
