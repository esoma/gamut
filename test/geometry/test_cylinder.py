
# gamut
from gamut.geometry import Cylinder
# python
from math import pi
from typing import Any
# pyglm
from glm import (length, mat4, radians, rotate, scale, translate, vec2, vec3,
                 vec4, quat)
# pytest
import pytest


def test_hash() -> None:
    c1 = Cylinder(vec3(1, 2, 3), 4, 5, rotation=quat(6, 7, 8, 9))
    c2 = Cylinder(vec3(1, 2, 3), 4, 5, rotation=quat(6, 7, 8, 9))
    assert hash(c1) != hash(c2)


def test_repr() -> None:
    cylinder = Cylinder(vec3(1, 2, 3), 4, 5, rotation=quat(6, 7, 8, 9))
    assert (
        repr(cylinder) ==
        f'<gamut.geometry.Cylinder center=(1.0, 2.0, 3.0) radius=4.0 '
        f'height=5.0 rotation=(6.0, 7.0, 8.0, 9.0)>'
    )


@pytest.mark.parametrize("radius", [None, 'x', object()])
def test_invalid_radius(radius: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Cylinder(vec3(0), radius, 1.0)
    assert str(excinfo.value) == 'radius must be float'
    
    
@pytest.mark.parametrize("height", [None, 'x', object()])
def test_invalid_height(height: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Cylinder(vec3(0), 1.0, height)
    assert str(excinfo.value) == 'height must be float'


@pytest.mark.parametrize("center", [None, '123', 123, vec4(1), vec2(1)])
def test_invalid_center(center: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Cylinder(center, 0, 0)
    assert str(excinfo.value) == 'center must be vec3'


@pytest.mark.parametrize("radius", [-1, 1, -1.5, 1.5, '-2.0', '2.0'])
def test_radius(radius: Any) -> None:
    cylinder = Cylinder(vec3(0), radius, 1.0)
    assert cylinder.radius == abs(float(radius))
    

@pytest.mark.parametrize("height", [-1, 1, -1.5, 1.5, '-2.0', '2.0'])
def test_height(height: Any) -> None:
    cylinder = Cylinder(vec3(0), 1.0, height)
    assert cylinder.height == abs(float(height))


@pytest.mark.parametrize("center", [vec3(1), (1, 2, 3)])
def test_center(center: Any) -> None:
    cylinder = Cylinder(center, 1, 1)
    assert cylinder.center == center
    assert cylinder.center is not center


def test_equal() -> None:
    assert Cylinder(vec3(0), 0, 0) == Cylinder(vec3(0), 0, 0)
    assert Cylinder(vec3(0), 0, 0) != Cylinder(vec3(1, 0, 0), 0, 0)
    assert Cylinder(vec3(0), 0, 0) != Cylinder(vec3(0, 1, 0), 0, 0)
    assert Cylinder(vec3(0), 0, 0) != Cylinder(vec3(0, 0, 1), 0, 0)
    assert Cylinder(vec3(0), 0, 0) != Cylinder(vec3(0), 1, 0)
    assert Cylinder(vec3(0), 0, 0) != Cylinder(vec3(0), 0, 1)
    assert Cylinder(vec3(0), 0, 0) != object()
