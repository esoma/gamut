
# gamut
from gamut.geometry import RectangularCuboid
from gamut.math import (Quaternion, U8Array, Vector2, Vector3, Vector3Array,
                        Vector4)
# python
from typing import Any
# pytest
import pytest


def test_hash() -> None:
    c1 = RectangularCuboid(
        Vector3(1, 2, 3),
        Vector3(4, 5, 6),
        rotation=Quaternion(7, 8, 9, 10)
    )
    c2 = RectangularCuboid(
        Vector3(1, 2, 3),
        Vector3(4, 5, 6),
        rotation=Quaternion(7, 8, 9, 10)
    )
    assert hash(c1) != hash(c2)


def test_repr() -> None:
    capsule = RectangularCuboid(
        Vector3(1, 2, 3),
        Vector3(4, 5, 6),
        rotation=Quaternion(7, 8, 9, 10)
    )
    assert (
        repr(capsule) ==
        f'<gamut.geometry.RectangularCuboid center=(1.0, 2.0, 3.0) '
        f'dimensions=(4.0, 5.0, 6.0) rotation=(7.0, 8.0, 9.0, 10.0)>'
    )


@pytest.mark.parametrize("center", [None, '123', 123, Vector4(1), Vector2(1)])
def test_invalid_center(center: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        RectangularCuboid(center, Vector3(1))
    assert str(excinfo.value) == 'center must be Vector3'


@pytest.mark.parametrize("dimensions", [
    None,
    '123',
    123,
    Vector4(1),
    Vector2(1)
])
def test_invalid_dimensions(dimensions: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        RectangularCuboid(Vector3(0), dimensions)
    assert str(excinfo.value) == 'dimensions must be Vector3'


@pytest.mark.parametrize("rotation", ['123', 123, Vector3(1), Vector2(1)])
def test_invalid_rotation(rotation: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        RectangularCuboid(Vector3(0), Vector3(1), rotation=rotation)
    assert str(excinfo.value) == 'rotation must be Quaternion'


@pytest.mark.parametrize("center", [Vector3(1), Vector3(1, 2, 3)])
def test_center(center: Any) -> None:
    rect = RectangularCuboid(center, Vector3(1))
    assert rect.center == center


@pytest.mark.parametrize("dimensions", [Vector3(1), Vector3(1, 2, 3)])
def test_dimensions(dimensions: Any) -> None:
    rect = RectangularCuboid(Vector3(0), dimensions)
    assert rect.dimensions == dimensions


def test_equal() -> None:
    rc = RectangularCuboid(Vector3(0), Vector3(1))
    assert rc == RectangularCuboid(Vector3(0), Vector3(1))
    assert rc != RectangularCuboid(Vector3(1, 0, 0), Vector3(1))
    assert rc != RectangularCuboid(Vector3(0, 1, 0), Vector3(1))
    assert rc != RectangularCuboid(Vector3(0, 0, 1), Vector3(1))
    assert rc != RectangularCuboid(Vector3(0), Vector3(1, 0, 0))
    assert rc != RectangularCuboid(Vector3(0), Vector3(0, 1, 0))
    assert rc != RectangularCuboid(Vector3(0), Vector3(0, 0, 1))
    assert rc != object()


def test_render() -> None:
    rc = RectangularCuboid(Vector3(0), Vector3(1))
    positions, normals, indices = rc.render()
    assert isinstance(positions, Vector3Array)
    assert isinstance(normals, Vector3Array)
    assert isinstance(indices, U8Array)
