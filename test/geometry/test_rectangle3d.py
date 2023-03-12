from __future__ import annotations
# gamut
from gamut.geometry import DegenerateGeometryError, LineSegment3d, Rectangle3d
from gamut.math import (DQuaternion, DVector2, DVector3, DVector4, FQuaternion,
                        FVector2, FVector3)
# python
from typing import Any
# pytest
import pytest


def test_hash() -> None:
    c1 = Rectangle3d(
        DVector3(1, 2, 3),
        DVector2(4, 5),
        rotation=DQuaternion(6, 7, 8, 9)
    )
    c2 = Rectangle3d(
        DVector3(1, 2, 3),
        DVector2(4, 5),
        rotation=DQuaternion(6, 7, 8, 9)
    )
    assert hash(c1) == hash(c2)
    c3 = Rectangle3d(
        FVector3(1, 2, 3),
        FVector2(4, 5),
        rotation=FQuaternion(6, 7, 8, 9)
    )
    assert hash(c1) != hash(c3)


@pytest.mark.parametrize("rectangle", [
    Rectangle3d(
        FVector3(1, 2, 3),
        FVector2(4, 5),
        rotation=FQuaternion(6, 7, 8, 9)
    ),
    Rectangle3d(
        DVector3(1, 2, 3),
        DVector2(4, 5),
        rotation=DQuaternion(6, 7, 8, 9)
    )
])
def test_repr(rectangle: Rectangle3d) -> None:
    assert (
        repr(rectangle) ==
        f'<gamut.geometry.Rectangle3d center=(1.0, 2.0, 3.0) '
        f'dimensions=(4.0, 5.0) rotation=(6.0, 7.0, 8.0, 9.0)>'
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
        Rectangle3d(center, DVector2(1))
    assert str(excinfo.value) == 'center must be FVector3 or DVector3'


@pytest.mark.parametrize("center, dimensions, expected_type", [
    [FVector3(0), DVector2(1), FVector2],
    [DVector3(0), FVector2(1), DVector2],
    [FVector3(0), object(), FVector2],
    [DVector3(0), object(), DVector2],
])
def test_invalid_dimensions_type(
    center: Any,
    dimensions: Any,
    expected_type: Any
) -> None:
    with pytest.raises(TypeError) as excinfo:
        Rectangle3d(center, dimensions)
    assert str(excinfo.value) == f'dimensions must be {expected_type.__name__}'


@pytest.mark.parametrize("center, dimensions, rotation, expected_type", [
    [FVector3(0), FVector2(1), DQuaternion(1), FQuaternion],
    [DVector3(0), DVector2(1), FQuaternion(1), DQuaternion],
    [FVector3(0), FVector2(1), object(), FQuaternion],
    [DVector3(0), DVector2(1), object(), DQuaternion],
])
def test_invalid_rotation_type(
    center: Any,
    dimensions: Any,
    rotation: Any,
    expected_type: Any
) -> None:
    with pytest.raises(TypeError) as excinfo:
        Rectangle3d(center, dimensions, rotation=rotation)
    assert str(excinfo.value) == f'rotation must be {expected_type.__name__}'


@pytest.mark.parametrize("vtype3, vtype2", [
    [FVector3, FVector2],
    [DVector3, DVector2],
])
def test_degenerate_point(
    vtype3: type[FVector3] | type[DVector3],
    vtype2: type[FVector2] | type[DVector2],
) -> None:
    with pytest.raises(Rectangle3d.DegenerateError) as excinfo:
        Rectangle3d(vtype3(1, 2, 3), vtype2(0))
    assert str(excinfo.value) == 'degenerate 3d rectangle'
    assert excinfo.value.degenerate_form == vtype3(1, 2, 3)


@pytest.mark.parametrize("vtype3, vtype2, quattype", [
    [FVector3, FVector2, FQuaternion],
    [DVector3, DVector2, DQuaternion],
])
@pytest.mark.parametrize("width, height", [
    [0, 1],
    [1, 0],
])
@pytest.mark.parametrize("rotation", [
    (1, 0, 0, 0),
    (0.7071067690849304, 0.0, 0.7071067690849304, 0.0),
])
def test_degenerate_line(
    vtype3: type[FVector3] | type[DVector3],
    vtype2: type[FVector2] | type[DVector2],
    quattype: type[FQuaternion] | type[DQuaternion],
    width: int,
    height: int,
    rotation: tuple[float, float, float, float]
) -> None:
    quat = quattype(*rotation)
    with pytest.raises(Rectangle3d.DegenerateError) as excinfo:
        Rectangle3d(vtype3(1, 2, 3), vtype2(width, height), rotation=quat)
    assert str(excinfo.value) == 'degenerate 3d rectangle'

    half_dimensions_3d = quat @ vtype3(width * .5, height * .5, 0)
    assert excinfo.value.degenerate_form == LineSegment3d(
        vtype3(1, 2, 3) - half_dimensions_3d,
        vtype3(1, 2, 3) + half_dimensions_3d,
    )


def test_degenerate_error():
    assert issubclass(Rectangle3d.DegenerateError, DegenerateGeometryError)


@pytest.mark.parametrize("dimensions", [
    DVector2(2, -1),
    DVector2(-1, 2),
    DVector2(-4, -3),
])
def test_dimensions(dimensions: Any) -> None:
    rectangle = Rectangle3d(DVector3(0), dimensions)
    assert rectangle.dimensions == abs(dimensions)


@pytest.mark.parametrize("center", [
    FVector3(1),
    FVector3(1, 2, 3),
    DVector3(1),
    DVector3(1, 2, 3)
])
def test_center(center: Any) -> None:
    rectangle = Rectangle3d(center, type(center)(1).xy)
    assert rectangle.center == center


@pytest.mark.parametrize("vtype3, vtype2, quattype", [
    [FVector3, FVector2, FQuaternion],
    [DVector3, DVector2, DQuaternion],
])
@pytest.mark.parametrize("rotation", [
    (1, 0, 0, 0),
    (0.7071067690849304, 0.0, 0.7071067690849304, 0.0),
])
def test_rotation(
    vtype3: type[FVector3] | type[DVector3],
    vtype2: type[FVector2] | type[DVector2],
    quattype: type[FQuaternion] | type[DQuaternion],
    rotation: tuple[float, float, float, float]
) -> None:
    quat = quattype(*rotation)
    rectangle = Rectangle3d(vtype3(0), vtype2(1), rotation=quat)
    assert rectangle.rotation == quat

def test_equal() -> None:
    assert (
        Rectangle3d(DVector3(0), DVector2(1)) ==
        Rectangle3d(DVector3(0), DVector2(1))
    )
    assert (
        Rectangle3d(FVector3(0), FVector2(1)) ==
        Rectangle3d(FVector3(0), FVector2(1))
    )
    assert (
        Rectangle3d(DVector3(0), DVector2(1)) !=
        Rectangle3d(FVector3(0), FVector2(1))
    )
    assert (
        Rectangle3d(DVector3(0), DVector2(1)) !=
        Rectangle3d(DVector3(0), DVector2(1), rotation=DQuaternion(0))
    )
    assert (
        Rectangle3d(DVector3(0), DVector2(1)) !=
        Rectangle3d(DVector3(1, 0, 0), DVector2(1))
    )
    assert (
        Rectangle3d(DVector3(0), DVector2(1)) !=
        Rectangle3d(DVector3(0, 1, 0), DVector2(1))
    )
    assert (
        Rectangle3d(DVector3(0), DVector2(1)) !=
        Rectangle3d(DVector3(0, 0, 1), DVector2(1))
    )
    assert (
        Rectangle3d(DVector3(0), DVector2(1)) !=
        Rectangle3d(DVector3(0), DVector2(1, 2))
    )
    assert (
        Rectangle3d(DVector3(0), DVector2(1)) !=
        Rectangle3d(DVector3(0), DVector2(2, 1))
    )
    assert Rectangle3d(DVector3(0), DVector2(1)) != object()
