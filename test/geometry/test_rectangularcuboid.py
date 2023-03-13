
# gamut
from gamut.geometry import (DegenerateGeometryError, LineSegment3d,
                            Rectangle3d, RectangularCuboid)
from gamut.math import (DQuaternion, DVector2, DVector2Array, DVector3,
                        DVector3Array, DVector4, FQuaternion, FVector2,
                        FVector2Array, FVector3, FVector3Array, U8Array)
# python
from math import radians
from typing import Any
# pytest
import pytest


@pytest.mark.parametrize("center, dimensions, rotation, degenerate_form", [
    (
        FVector3(1),
        FVector3(0),
        None,
        FVector3(1),
    ),
    (
        FVector3(1),
        FVector3(1, 0, 0),
        None,
        LineSegment3d(FVector3(.5, 1, 1), FVector3(1.5, 1, 1)),
    ),
    (
        FVector3(1),
        FVector3(0, 1, 0),
        None,
        LineSegment3d(FVector3(1, .5, 1), FVector3(1, 1.5, 1)),
    ),
    (
        FVector3(1),
        FVector3(0, 0, 1),
        None,
        LineSegment3d(FVector3(1, 1, .5), FVector3(1, 1, 1.5)),
    ),
    (
        FVector3(1),
        FVector3(0, 0, 1),
        FQuaternion(1).rotate(radians(90), FVector3(1, 0, 0)),
        LineSegment3d(
            FVector3(1, 1.5, 1),
            FVector3(1, .5, 1)
        ),
    ),
    (
        FVector3(1),
        FVector3(1, 1, 0),
        None,
        Rectangle3d(FVector3(1), FVector2(1, 1)),
    ),
    (
        FVector3(1),
        FVector3(0, 1, 1),
        None,
        Rectangle3d(
            FVector3(1),
            FVector2(1, 1),
            rotation=FQuaternion(1).rotate(radians(90), FVector3(0, 1, 0))
        ),
    ),
    (
        FVector3(1),
        FVector3(1, 0, 1),
        None,
        Rectangle3d(
            FVector3(1),
            FVector2(1, 1),
            rotation=FQuaternion(1).rotate(radians(90), FVector3(1, 0, 0))
        ),
    ),
    (
        FVector3(1),
        FVector3(1, 1, 0),
        FQuaternion(1).rotate(radians(90), FVector3(0, 0, 1)),
        Rectangle3d(
            FVector3(1),
            FVector2(1, 1),
            rotation=FQuaternion(1).rotate(radians(90), FVector3(0, 0, 1)),
        ),
    ),
    (
        FVector3(1),
        FVector3(1, 0, 1),
        FQuaternion(1).rotate(radians(90), FVector3(0, 0, 1)),
        Rectangle3d(
            FVector3(1),
            FVector2(1, 1),
            rotation=(
                FQuaternion(1).rotate(radians(90), FVector3(0, 0, 1)) *
                FQuaternion(1).rotate(radians(90), FVector3(1, 0, 0))
            )
        ),
    ),
])
def test_degenerate(
    center: Any,
    dimensions: float,
    rotation: Any,
    degenerate_form: Any
) -> None:
    with pytest.raises(RectangularCuboid.DegenerateError) as excinfo:
        RectangularCuboid(center, dimensions, rotation=rotation)
    assert str(excinfo.value) == 'degenerate rectangular cuboid'
    assert excinfo.value.degenerate_form == degenerate_form


def test_degenerate_error():
    assert issubclass(
        RectangularCuboid.DegenerateError,
        DegenerateGeometryError
    )


def test_hash() -> None:
    c1 = RectangularCuboid(
        DVector3(1, 2, 3),
        DVector3(4, 5, 6),
        rotation=DQuaternion(7, 8, 9, 10)
    )
    c2 = RectangularCuboid(
        DVector3(1, 2, 3),
        DVector3(4, 5, 6),
        rotation=DQuaternion(7, 8, 9, 10)
    )
    assert hash(c1) == hash(c2)
    c3 = RectangularCuboid(
        FVector3(1, 2, 3),
        FVector3(4, 5, 6),
        rotation=FQuaternion(7, 8, 9, 10)
    )
    assert hash(c1) != hash(c3)


def test_repr() -> None:
    capsule = RectangularCuboid(
        DVector3(1, 2, 3),
        DVector3(4, 5, 6),
        rotation=DQuaternion(7, 8, 9, 10)
    )
    assert (
        repr(capsule) ==
        f'<gamut.geometry.RectangularCuboid center=(1.0, 2.0, 3.0) '
        f'dimensions=(4.0, 5.0, 6.0) rotation=(7.0, 8.0, 9.0, 10.0)>'
    )


@pytest.mark.parametrize("center", [
    None,
    '123',
    123,
    DVector4(1),
    DVector2(1)
])
def test_invalid_center(center: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        RectangularCuboid(center, DVector3(1))
    assert str(excinfo.value) == 'center must be FVector3 or DVector3'


@pytest.mark.parametrize("dimensions", [
    None,
    '123',
    123,
    DVector4(1),
    DVector2(1)
])
def test_invalid_dimensions(dimensions: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        RectangularCuboid(DVector3(0), dimensions)
    assert str(excinfo.value) == 'dimensions must be DVector3'


@pytest.mark.parametrize("rotation", ['123', 123, DVector3(1), DVector2(1)])
def test_invalid_rotation(rotation: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        RectangularCuboid(DVector3(0), DVector3(1), rotation=rotation)
    assert str(excinfo.value) == 'rotation must be DQuaternion'


def test_different_rotation() -> None:
    with pytest.raises(TypeError) as excinfo:
        RectangularCuboid(FVector3(0), FVector3(0), rotation=DQuaternion(1))
    assert str(excinfo.value) == 'rotation must be FQuaternion'

    with pytest.raises(TypeError) as excinfo:
        RectangularCuboid(DVector3(0), DVector3(0), rotation=FQuaternion(1))
    assert str(excinfo.value) == 'rotation must be DQuaternion'


@pytest.mark.parametrize("center", [DVector3(1), DVector3(1, 2, 3)])
def test_center(center: Any) -> None:
    rect = RectangularCuboid(center, DVector3(1))
    assert rect.center == center


@pytest.mark.parametrize("dimensions", [DVector3(1), DVector3(1, 2, 3)])
def test_dimensions(dimensions: Any) -> None:
    rect = RectangularCuboid(DVector3(0), dimensions)
    assert rect.dimensions == dimensions


@pytest.mark.parametrize("center, rotation", [
    (FVector3(1), FQuaternion(2)),
    (FVector3(1), FQuaternion(-2)),
    (DVector3(1), DQuaternion(2)),
    (DVector3(1), DQuaternion(-2)),
])
def test_rotation(center: Any, rotation: Any) -> None:
    r = RectangularCuboid(center, center, rotation=rotation)
    assert r.rotation == rotation

def test_default_rotation() -> None:
    r = RectangularCuboid(FVector3(0), FVector3(1))
    assert r.rotation == FQuaternion(1)

    r = RectangularCuboid(DVector3(0), DVector3(1))
    assert r.rotation == DQuaternion(1)


def test_equal() -> None:
    assert (
        RectangularCuboid(FVector3(0), FVector3(1)) ==
        RectangularCuboid(FVector3(0), FVector3(1))
    )
    assert (
        RectangularCuboid(FVector3(0), FVector3(1)) !=
        RectangularCuboid(DVector3(0), DVector3(1))
    )

    rc = RectangularCuboid(DVector3(0), DVector3(1))
    assert rc == RectangularCuboid(DVector3(0), DVector3(1))
    assert rc != RectangularCuboid(DVector3(1, 0, 0), DVector3(1))
    assert rc != RectangularCuboid(DVector3(0, 1, 0), DVector3(1))
    assert rc != RectangularCuboid(DVector3(0, 0, 1), DVector3(1))
    assert rc != RectangularCuboid(DVector3(0), DVector3(1, 2, 2))
    assert rc != RectangularCuboid(DVector3(0), DVector3(2, 1, 2))
    assert rc != RectangularCuboid(DVector3(0), DVector3(2, 2, 1))
    assert rc != object()


def test_d_render() -> None:
    rc = RectangularCuboid(DVector3(0), DVector3(1))
    positions, normals, uvs, indices = rc.render()
    assert isinstance(positions, DVector3Array)
    assert isinstance(normals, DVector3Array)
    assert isinstance(uvs, DVector2Array)
    assert isinstance(indices, U8Array)


def test_f_render() -> None:
    rc = RectangularCuboid(FVector3(0), FVector3(1))
    positions, normals, uvs, indices = rc.render()
    assert isinstance(positions, FVector3Array)
    assert isinstance(normals, FVector3Array)
    assert isinstance(uvs, FVector2Array)
    assert isinstance(indices, U8Array)
