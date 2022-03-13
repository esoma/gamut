
# gamut
from gamut.geometry import (Plane, Shape3dCullable, Shape3dPointContainer,
                            Sphere, ViewFrustum3d)
from gamut.math import Matrix4, Vector2, Vector3, Vector4
# python
from math import pi, radians
from typing import Any
# pytest
import pytest


def test_cullable() -> None:
    assert isinstance(Sphere(Vector3(0), 0), Shape3dCullable)


def test_point_container() -> None:
    assert isinstance(Sphere(Vector3(0), 0), Shape3dPointContainer)


def test_sphere() -> None:
    s1 = Sphere(Vector3(1, 2, 3), 4)
    s2 = Sphere(Vector3(1, 2, 3), 4)
    assert hash(s1) != hash(s2)


def test_repr() -> None:
    sphere = Sphere(Vector3(1, 2, 3), 4)
    assert (
        repr(sphere) ==
        f'<gamut.geometry.Sphere center=(1.0, 2.0, 3.0) radius=4.0>'
    )


@pytest.mark.parametrize("radius", [None, 'x', object()])
def test_invalid_radius(radius: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Sphere(Vector3(0), radius)
    assert str(excinfo.value) == 'radius must be float'


@pytest.mark.parametrize("center", [None, '123', 123, Vector4(1), Vector2(1)])
def test_invalid_center(center: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Sphere(center, 0)
    assert str(excinfo.value) == 'center must be Vector3'


@pytest.mark.parametrize("radius", [-1, 1, -1.5, 1.5, '-2.0', '2.0'])
def test_radius(radius: Any) -> None:
    sphere = Sphere(Vector3(0), radius)
    assert sphere.radius == abs(float(radius))


@pytest.mark.parametrize("center", [Vector3(1), Vector3(1, 2, 3)])
def test_center(center: Any) -> None:
    sphere = Sphere(center, 1)
    assert sphere.center == center


@pytest.mark.parametrize("sphere", [
    Sphere(Vector3(0, 0, 0), 0),
    Sphere(Vector3(1, 1, 1), 1),
    Sphere(Vector3(0, .5, 1), 99),
])
@pytest.mark.parametrize("transform", [
    Matrix4(1).translate(Vector3(1, 0, 0)),
    Matrix4(1).translate(Vector3(0, 1, 0)),
    Matrix4(1).translate(Vector3(0, 0, 1)),
    Matrix4(1).rotate(radians(90), Vector3(1, 0, 0)),
    Matrix4(1).rotate(radians(90), Vector3(0, 1, 0)),
    Matrix4(1).rotate(radians(90), Vector3(0, 0, 1)),
    Matrix4(1).scale(Vector3(2, 3, 4)),
])
def test_transform(sphere: Sphere, transform: Matrix4) -> None:
    new_sphere = transform @ sphere
    assert new_sphere is not sphere

    expected_center = transform @ sphere.center
    expected_radius = (
        sphere.radius *
        max(Vector3(*(c.xyz.magnitude for c in (
            transform[0],
            transform[1],
            transform[2],
        ))))
    )

    assert new_sphere.center == expected_center
    assert new_sphere.radius == expected_radius


@pytest.mark.parametrize("transform", [None, 123, Vector4(1), Vector2(1)])
def test_transform_invalid(transform: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        transform @ Sphere(Vector3(0, 1, 0), 1)
    assert str(excinfo.value).startswith('unsupported operand type(s) for @:')


def test_equal() -> None:
    assert Sphere(Vector3(0), 0) == Sphere(Vector3(0), 0)
    assert Sphere(Vector3(0), 0) != Sphere(Vector3(1, 0, 0), 0)
    assert Sphere(Vector3(0), 0) != Sphere(Vector3(0, 1, 0), 0)
    assert Sphere(Vector3(0), 0) != Sphere(Vector3(0, 0, 1), 0)
    assert Sphere(Vector3(0), 0) != Sphere(Vector3(0), 1)
    assert Sphere(Vector3(0), 0) != object()


@pytest.mark.parametrize("sphere", [
    Sphere(Vector3(0), 0),
    Sphere(Vector3(0), 10),
    Sphere(Vector3(1, 2, 3), 5),
])
def test_contains_point(sphere: Sphere) -> None:
    assert sphere.contains_point(sphere.center)

    for rc in (0.1, 0.5, 0.9, 1.0):
        r = sphere.radius * rc
        base_point = Vector3(r, 0, 0)
        for angle in (0.0, pi * .5, pi, pi * .75):
            for axis in (Vector3(1, 0, 0), Vector3(0, 1, 0), Vector3(0, 0, 1)):
                check_point = sphere.center + (
                    Matrix4(1).rotate(angle, axis) @ base_point
                )
                assert sphere.contains_point(check_point)

    for r_plus in (.1, 2.0, 100.0):
        r = sphere.radius + r_plus
        base_point = Vector3(r, 0, 0)
        for angle in (0.0, pi * .5, pi, pi * .75):
            for axis in (Vector3(1, 0, 0), Vector3(0, 1, 0), Vector3(0, 0, 1)):
                check_point = sphere.center + (
                    Matrix4(1).rotate(angle, axis) @ base_point
                )
                assert not sphere.contains_point(check_point)


def test_seen_by() -> None:
    frustum = ViewFrustum3d(
        Plane(-1, Vector3(0, 0, 1)),
        Plane(10, Vector3(0, 0, -1)),
        Plane(5, Vector3(1, 0, 0)),
        Plane(5, Vector3(-1, 0, 0)),
        Plane(5, Vector3(0, 1, 0)),
        Plane(5, Vector3(0, -1, 0)),
    )

    # near
    assert not Sphere(Vector3(0), 0).seen_by(frustum)
    assert Sphere(Vector3(0), 1).seen_by(frustum)
    assert Sphere(Vector3(0, 0, 1), 0).seen_by(frustum)
    # far
    assert not Sphere(Vector3(0, 0, 11), 0).seen_by(frustum)
    assert Sphere(Vector3(0, 0, 11), 1).seen_by(frustum)
    assert Sphere(Vector3(0, 0, 10), 0).seen_by(frustum)
    # left
    assert not Sphere(Vector3(-6, 0, 5), 0).seen_by(frustum)
    assert Sphere(Vector3(-6, 0, 5), 1).seen_by(frustum)
    assert Sphere(Vector3(-5, 0, 5), 0).seen_by(frustum)
    # right
    assert not Sphere(Vector3(6, 0, 5), 0).seen_by(frustum)
    assert Sphere(Vector3(6, 0, 5), 1).seen_by(frustum)
    assert Sphere(Vector3(5, 0, 5), 0).seen_by(frustum)
    # bottom
    assert not Sphere(Vector3(0, -6, 5), 0).seen_by(frustum)
    assert Sphere(Vector3(0, -6, 5), 1).seen_by(frustum)
    assert Sphere(Vector3(0, -5, 5), 0).seen_by(frustum)
    # top
    assert not Sphere(Vector3(0, 6, 5), 0).seen_by(frustum)
    assert Sphere(Vector3(0, 6, 5), 1).seen_by(frustum)
    assert Sphere(Vector3(0, 5, 5), 0).seen_by(frustum)
