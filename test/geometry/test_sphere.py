
# gamut
from gamut.geometry import Plane, Sphere, ViewFrustum3d
# python
from typing import Any
# pyglm
from glm import (length, mat4, radians, rotate, scale, translate, vec2, vec3,
                 vec4)
# pytest
import pytest


def test_repr() -> None:
    sphere = Sphere(vec3(1, 2, 3), 4)
    assert (
        repr(sphere) ==
        f'<gamut.geometry.Sphere center=(1.0, 2.0, 3.0) radius=4.0>'
    )


@pytest.mark.parametrize("radius", [None, 'x', object()])
def test_invalid_radius(radius: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Sphere(vec3(0), radius)
    assert str(excinfo.value) == 'radius must be float'


@pytest.mark.parametrize("center", [None, '123', 123, vec4(1), vec2(1)])
def test_invalid_center(center: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Sphere(center, 0)
    assert str(excinfo.value) == 'center must be vec3'


@pytest.mark.parametrize("radius", [-1, 1, -1.5, 1.5, '-2.0', '2.0'])
def test_radius(radius: Any) -> None:
    sphere = Sphere(vec3(0), radius)
    assert sphere.radius == abs(float(radius))


@pytest.mark.parametrize("center", [vec3(1), (1, 2, 3)])
def test_center(center: Any) -> None:
    sphere = Sphere(center, 1)
    assert sphere.center == center
    assert sphere.center is not center


@pytest.mark.parametrize("sphere", [
    Sphere(vec3(0, 0, 0), 0),
    Sphere(vec3(1, 1, 1), 1),
    Sphere(vec3(0, .5, 1), 99),
])
@pytest.mark.parametrize("transform", [
    translate(mat4(1), vec3(1, 0, 0)),
    translate(mat4(1), vec3(0, 1, 0)),
    translate(mat4(1), vec3(0, 0, 1)),
    rotate(mat4(1), radians(90), vec3(1, 0, 0)),
    rotate(mat4(1), radians(90), vec3(0, 1, 0)),
    rotate(mat4(1), radians(90), vec3(0, 0, 1)),
    scale(mat4(1), vec3(2, 3, 4)),
])
def test_transform(sphere: Sphere, transform: mat4) -> None:
    new_sphere = transform * sphere
    assert new_sphere is not sphere

    expected_center = transform * sphere.center
    expected_radius = (
        sphere.radius *
        max(vec3(*(length(c.xyz) for c in (
            transform[0],
            transform[1],
            transform[2],
        ))))
    )

    assert new_sphere.center == expected_center
    assert new_sphere.radius == expected_radius


@pytest.mark.parametrize("transform", [None, 123, vec4(1), vec2(1)])
def test_transform_invalid(transform: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        transform * Sphere(vec3(0, 1, 0), 1)
    assert str(excinfo.value).startswith('unsupported operand type(s) for *:')


def test_equal() -> None:
    assert Sphere(vec3(0), 0) == Sphere(vec3(0), 0)
    assert Sphere(vec3(0), 0) != Sphere(vec3(1, 0, 0), 0)
    assert Sphere(vec3(0), 0) != Sphere(vec3(0, 1, 0), 0)
    assert Sphere(vec3(0), 0) != Sphere(vec3(0, 0, 1), 0)
    assert Sphere(vec3(0), 0) != Sphere(vec3(0), 1)
    assert Sphere(vec3(0), 0) != object()


def test_seen_by() -> None:
    frustum = ViewFrustum3d(
        Plane(-1, vec3(0, 0, 1)),
        Plane(10, vec3(0, 0, -1)),
        Plane(5, vec3(1, 0, 0)),
        Plane(5, vec3(-1, 0, 0)),
        Plane(5, vec3(0, 1, 0)),
        Plane(5, vec3(0, -1, 0)),
    )

    # near
    assert not Sphere(vec3(0), 0).seen_by(frustum)
    assert Sphere(vec3(0), 1).seen_by(frustum)
    assert Sphere(vec3(0, 0, 1), 0).seen_by(frustum)
    # far
    assert not Sphere(vec3(0, 0, 11), 0).seen_by(frustum)
    assert Sphere(vec3(0, 0, 11), 1).seen_by(frustum)
    assert Sphere(vec3(0, 0, 10), 0).seen_by(frustum)
    # left
    assert not Sphere(vec3(-6, 0, 5), 0).seen_by(frustum)
    assert Sphere(vec3(-6, 0, 5), 1).seen_by(frustum)
    assert Sphere(vec3(-5, 0, 5), 0).seen_by(frustum)
    # right
    assert not Sphere(vec3(6, 0, 5), 0).seen_by(frustum)
    assert Sphere(vec3(6, 0, 5), 1).seen_by(frustum)
    assert Sphere(vec3(5, 0, 5), 0).seen_by(frustum)
    # bottom
    assert not Sphere(vec3(0, -6, 5), 0).seen_by(frustum)
    assert Sphere(vec3(0, -6, 5), 1).seen_by(frustum)
    assert Sphere(vec3(0, -5, 5), 0).seen_by(frustum)
    # top
    assert not Sphere(vec3(0, 6, 5), 0).seen_by(frustum)
    assert Sphere(vec3(0, 6, 5), 1).seen_by(frustum)
    assert Sphere(vec3(0, 5, 5), 0).seen_by(frustum)
