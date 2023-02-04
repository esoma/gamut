from __future__ import annotations
# gamut
from gamut.geometry import Circle3d, DegenerateGeometryError
from gamut.math import DVector2, DVector3, DVector4, FVector3
# python
from typing import Any
# pytest
import pytest


def test_hash() -> None:
    c1 = Circle3d(DVector3(1, 2, 3), 4, DVector3(1, 0, 0))
    c2 = Circle3d(DVector3(1, 2, 3), 4, DVector3(1, 0, 0))
    assert hash(c1) == hash(c2)
    c3 = Circle3d(FVector3(1, 2, 3), 4, FVector3(1, 0, 0))
    assert hash(c1) != hash(c3)


@pytest.mark.parametrize("circle", [
    Circle3d(FVector3(1, 2, 3), 4, FVector3(1, 0, 0)),
    Circle3d(DVector3(1, 2, 3), 4, DVector3(1, 0, 0))
])
def test_repr(circle: Circle3d) -> None:
    assert (
        repr(circle) ==
        f'<gamut.geometry.Circle3d center=(1.0, 2.0, 3.0) radius=4.0 '
        f'normal=(1.0, 0.0, 0.0)>'
    )


@pytest.mark.parametrize("radius", [None, 'x', object()])
def test_invalid_radius(radius: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Circle3d(DVector3(0), radius, DVector3(1, 0, 0))
    assert str(excinfo.value) == 'radius must be float'


@pytest.mark.parametrize("center", [
    None,
    '123',
    123,
    DVector4(1),
    DVector2(1)
])
def test_invalid_center(center: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Circle3d(center, 1, DVector3(1, 0, 0))
    assert str(excinfo.value) == 'center must be FVector3 or DVector3'


@pytest.mark.parametrize("center, normal", [
    [FVector3(0), DVector3(1, 0, 0)],
    [DVector3(0), FVector3(1, 0, 0)],
    [FVector3(0), object()],
    [DVector3(0), object()],
])
def test_invalid_normal_type(center: Any, normal: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Circle3d(center, 1, normal)
    assert str(excinfo.value) == f'normal must be {type(center).__name__}'


@pytest.mark.parametrize("center, normal", [
    [FVector3(0), FVector3(0)],
    [DVector3(0), DVector3(0)],
])
def test_invalid_normal_value(center: Any, normal: Any) -> None:
    with pytest.raises(ValueError) as excinfo:
        Circle3d(center, 1, normal)
    assert str(excinfo.value) == 'invalid normal'


@pytest.mark.parametrize("vtype", [FVector3, DVector3])
def test_degenerate(vtype: type[FVector3] | type[DVector3]) -> None:
    with pytest.raises(Circle3d.DegenerateError) as excinfo:
        Circle3d(vtype(1, 2, 3), 0, vtype(1))
    assert str(excinfo.value) == 'degenerate 3d circle'
    assert excinfo.value.degenerate_form == vtype(1, 2, 3)


def test_degenerate_error():
    assert issubclass(Circle3d.DegenerateError, DegenerateGeometryError)


@pytest.mark.parametrize("radius", [-1, 1, -1.5, 1.5, '-2.0', '2.0'])
def test_radius(radius: Any) -> None:
    circle = Circle3d(DVector3(0), radius, DVector3(1))
    assert circle.radius == abs(float(radius))


@pytest.mark.parametrize("center", [
    FVector3(1),
    FVector3(1, 2, 3),
    DVector3(1),
    DVector3(1, 2, 3)
])
def test_center(center: Any) -> None:
    circle = Circle3d(center, 1, type(center)(1))
    assert circle.center == center

@pytest.mark.parametrize("normal", [
    FVector3(1),
    FVector3(1, 2, 3),
    DVector3(1),
    DVector3(1, 2, 3)
])
def test_normal(normal: Any) -> None:
    circle = Circle3d(type(normal)(0), 1, normal)
    assert circle.normal == normal.normalize()


def test_equal() -> None:
    assert (
        Circle3d(DVector3(0), 1, DVector3(1)) ==
        Circle3d(DVector3(0), 1, DVector3(1))
    )
    assert (
        Circle3d(FVector3(0), 1, FVector3(1)) ==
        Circle3d(FVector3(0), 1, FVector3(1))
    )
    assert (
        Circle3d(DVector3(0), 1, DVector3(1)) !=
        Circle3d(FVector3(0), 1, FVector3(1))
    )
    assert (
        Circle3d(DVector3(0), 1, DVector3(1)) !=
        Circle3d(DVector3(1, 0, 0), 1, DVector3(1))
    )
    assert (
        Circle3d(DVector3(0), 1, DVector3(1)) !=
        Circle3d(DVector3(0, 1, 0), 1, DVector3(1))
    )
    assert (
        Circle3d(DVector3(0), 1, DVector3(1)) !=
        Circle3d(DVector3(0, 0, 1), 1, DVector3(1))
    )
    assert (
        Circle3d(DVector3(0), 1, DVector3(1)) !=
        Circle3d(DVector3(0), 2, DVector3(1))
    )
    assert (
        Circle3d(DVector3(0), 1, DVector3(1)) !=
        Circle3d(DVector3(0), 1, DVector3(1, 0, 0))
    )
    assert (
        Circle3d(DVector3(0), 1, DVector3(1)) !=
        Circle3d(DVector3(0), 1, DVector3(0, 1, 0))
    )
    assert (
        Circle3d(DVector3(0), 1, DVector3(1)) !=
        Circle3d(DVector3(0), 1, DVector3(0, 0, 1))
    )
    assert Circle3d(DVector3(0), 1, DVector3(1)) != object()
