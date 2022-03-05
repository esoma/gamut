
# gamut
from gamut.geometry import RectangularCuboid
# python
from typing import Any
# pyglm
from glm import quat, vec2, vec3, vec4
# pytest
import pytest


def test_hash() -> None:
    c1 = RectangularCuboid(
        vec3(1, 2, 3),
        vec3(4, 5, 6),
        rotation=quat(7, 8, 9, 10)
    )
    c2 = RectangularCuboid(
        vec3(1, 2, 3),
        vec3(4, 5, 6),
        rotation=quat(7, 8, 9, 10)
    )
    assert hash(c1) != hash(c2)


def test_repr() -> None:
    capsule = RectangularCuboid(
        vec3(1, 2, 3),
        vec3(4, 5, 6),
        rotation=quat(7, 8, 9, 10)
    )
    assert (
        repr(capsule) ==
        f'<gamut.geometry.RectangularCuboid center=(1.0, 2.0, 3.0) '
        f'dimensions=(4.0, 5.0, 6.0) rotation=(7.0, 8.0, 9.0, 10.0)>'
    )


@pytest.mark.parametrize("center", [None, '123', 123, vec4(1), vec2(1)])
def test_invalid_center(center: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        RectangularCuboid(center, vec3(1))
    assert str(excinfo.value) == 'center must be vec3'


@pytest.mark.parametrize("dimensions", [None, '123', 123, vec4(1), vec2(1)])
def test_invalid_dimensions(dimensions: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        RectangularCuboid(vec3(0), dimensions)
    assert str(excinfo.value) == 'dimensions must be vec3'


@pytest.mark.parametrize("rotation", ['123', 123, vec3(1), vec2(1)])
def test_invalid_rotation(rotation: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        RectangularCuboid(vec3(0), vec3(1), rotation=rotation)
    assert str(excinfo.value) == 'rotation must be quat'


@pytest.mark.parametrize("center", [vec3(1), (1, 2, 3)])
def test_center(center: Any) -> None:
    capsule = RectangularCuboid(center, vec3(1))
    assert capsule.center == center
    assert capsule.center is not center


@pytest.mark.parametrize("dimensions", [vec3(1), (1, 2, 3)])
def test_dimensions(dimensions: Any) -> None:
    capsule = RectangularCuboid(vec3(0), dimensions)
    assert capsule.dimensions == dimensions
    assert capsule.dimensions is not dimensions


def test_equal() -> None:
    rc = RectangularCuboid(vec3(0), vec3(1))
    assert rc == RectangularCuboid(vec3(0), vec3(1))
    assert rc != RectangularCuboid(vec3(1, 0, 0), vec3(1))
    assert rc != RectangularCuboid(vec3(0, 1, 0), vec3(1))
    assert rc != RectangularCuboid(vec3(0, 0, 1), vec3(1))
    assert rc != RectangularCuboid(vec3(0), vec3(1, 0, 0))
    assert rc != RectangularCuboid(vec3(0), vec3(0, 1, 0))
    assert rc != RectangularCuboid(vec3(0), vec3(0, 0, 1))
    assert rc != object()
