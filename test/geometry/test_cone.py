
# gamut
from gamut.geometry import Cone
# python
from typing import Any
# pyglm
from glm import quat, vec2, vec3, vec4
# pytest
import pytest


def test_hash() -> None:
    c1 = Cone(vec3(1, 2, 3), 4, 5, rotation=quat(6, 7, 8, 9))
    c2 = Cone(vec3(1, 2, 3), 4, 5, rotation=quat(6, 7, 8, 9))
    assert hash(c1) != hash(c2)


def test_repr() -> None:
    cone = Cone(vec3(1, 2, 3), 4, 5, rotation=quat(6, 7, 8, 9))
    assert (
        repr(cone) ==
        f'<gamut.geometry.Cone center=(1.0, 2.0, 3.0) radius=4.0 '
        f'height=5.0 rotation=(6.0, 7.0, 8.0, 9.0)>'
    )


@pytest.mark.parametrize("radius", [None, 'x', object()])
def test_invalid_radius(radius: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Cone(vec3(0), radius, 1.0)
    assert str(excinfo.value) == 'radius must be float'


@pytest.mark.parametrize("height", [None, 'x', object()])
def test_invalid_height(height: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Cone(vec3(0), 1.0, height)
    assert str(excinfo.value) == 'height must be float'


@pytest.mark.parametrize("center", [None, '123', 123, vec4(1), vec2(1)])
def test_invalid_center(center: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Cone(center, 0, 0)
    assert str(excinfo.value) == 'center must be vec3'


@pytest.mark.parametrize("radius", [-1, 1, -1.5, 1.5, '-2.0', '2.0'])
def test_radius(radius: Any) -> None:
    cone = Cone(vec3(0), radius, 1.0)
    assert cone.radius == abs(float(radius))


@pytest.mark.parametrize("height", [-1, 1, -1.5, 1.5, '-2.0', '2.0'])
def test_height(height: Any) -> None:
    cone = Cone(vec3(0), 1.0, height)
    assert cone.height == abs(float(height))


@pytest.mark.parametrize("center", [vec3(1), (1, 2, 3)])
def test_center(center: Any) -> None:
    cone = Cone(center, 1, 1)
    assert cone.center == center
    assert cone.center is not center


def test_equal() -> None:
    assert Cone(vec3(0), 0, 0) == Cone(vec3(0), 0, 0)
    assert Cone(vec3(0), 0, 0) != Cone(vec3(1, 0, 0), 0, 0)
    assert Cone(vec3(0), 0, 0) != Cone(vec3(0, 1, 0), 0, 0)
    assert Cone(vec3(0), 0, 0) != Cone(vec3(0, 0, 1), 0, 0)
    assert Cone(vec3(0), 0, 0) != Cone(vec3(0), 1, 0)
    assert Cone(vec3(0), 0, 0) != Cone(vec3(0), 0, 1)
    assert Cone(vec3(0), 0, 0) != object()
