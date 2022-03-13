
# gamut
from gamut.geometry import Plane, Quad3d, Shape3dCullable, ViewFrustum3d
from gamut.math import Matrix4, Vector2, Vector3, Vector3Array, Vector4
# python
from math import radians
from typing import Any
# pytest
import pytest


def test_cullable() -> None:
    assert isinstance(
        Quad3d(Vector3(0), Vector3(0), Vector3(0), Vector3(0)),
        Shape3dCullable
    )


def test_repr() -> None:
    quad = Quad3d(
        Vector3(0, 1, 2),
        Vector3(3, 4, 5),
        Vector3(6, 7, 8),
        Vector3(9, 10, 11)
    )
    assert (
        repr(quad) ==
        f'<gamut.geometry.Quad3d ('
        f'(0.0, 1.0, 2.0), '
        f'(3.0, 4.0, 5.0), '
        f'(6.0, 7.0, 8.0), '
        f'(9.0, 10.0, 11.0)'
        f')>'
    )

@pytest.mark.parametrize("point", [None, '123', 123, Vector4(1), Vector2(1)])
@pytest.mark.parametrize("point_index", range(4))
def test_invalid_point(point: Any, point_index: int) -> None:
    points = [Vector3(0), Vector3(0), Vector3(0), Vector3(0)]
    points[point_index] = point
    with pytest.raises(TypeError) as excinfo:
        Quad3d(*points)
    assert str(excinfo.value) == (
        f'invalid type {point!r}, expected {Vector3!r}'
    )


def test_points() -> None:
    expected_points = Vector3Array(
        Vector3(0, 1, 2),
        Vector3(3, 4, 5),
        Vector3(6, 7, 8),
        Vector3(9, 10, 11)
    )
    quad = Quad3d(*expected_points)
    assert quad.points == expected_points


@pytest.mark.parametrize("quad", [
    Quad3d(Vector3(0), Vector3(0), Vector3(0), Vector3(0)),
    Quad3d(
        Vector3(0, 1, 2),
        Vector3(3, 4, 5),
        Vector3(6, 7, 8),
        Vector3(9, 10, 11)
    )
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
def test_transform(quad: Quad3d, transform: Matrix4) -> None:
    new_quad = transform @ quad
    assert new_quad is not quad

    expected_points = Vector3Array(*(
        transform @ p
        for p in quad.points
    ))

    assert new_quad.points == expected_points


@pytest.mark.parametrize("transform", [None, 123, Vector4(1), Vector2(1)])
def test_transform_invalid(transform: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        transform @ Quad3d(Vector3(0), Vector3(0), Vector3(0), Vector3(0))
    assert str(excinfo.value).startswith('unsupported operand type(s) for @:')



def test_equal() -> None:
    zero_quad = Quad3d(Vector3(0), Vector3(0), Vector3(0), Vector3(0))
    assert zero_quad == zero_quad
    assert zero_quad != Quad3d(Vector3(1), Vector3(0), Vector3(0), Vector3(0))
    assert zero_quad != Quad3d(Vector3(0), Vector3(1), Vector3(0), Vector3(0))
    assert zero_quad != Quad3d(Vector3(0), Vector3(0), Vector3(1), Vector3(0))
    assert zero_quad != Quad3d(Vector3(0), Vector3(0), Vector3(0), Vector3(1))
    assert zero_quad != object()


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
    assert not Quad3d(
        Vector3(0),
        Vector3(0),
        Vector3(0),
        Vector3(0)
    ).seen_by(frustum)
    assert Quad3d(
        Vector3(0, 0, 1),
        Vector3(0),
        Vector3(0),
        Vector3(0)
    ).seen_by(frustum)
    assert Quad3d(
        Vector3(0),
        Vector3(0, 0, 1),
        Vector3(0),
        Vector3(0)
    ).seen_by(frustum)
    assert Quad3d(
        Vector3(0),
        Vector3(0),
        Vector3(0, 0, 1),
        Vector3(0)
    ).seen_by(frustum)
    assert Quad3d(
        Vector3(0),
        Vector3(0),
        Vector3(0),
        Vector3(0, 0, 1)
    ).seen_by(frustum)
    # far
    assert not Quad3d(
        Vector3(0, 0, 11),
        Vector3(0, 0, 11),
        Vector3(0, 0, 11),
        Vector3(0, 0, 11)
    ).seen_by(frustum)
    assert Quad3d(
        Vector3(0, 0, 10),
        Vector3(0, 0, 11),
        Vector3(0, 0, 11),
        Vector3(0, 0, 11)
    ).seen_by(frustum)
    assert Quad3d(
        Vector3(0, 0, 11),
        Vector3(0, 0, 10),
        Vector3(0, 0, 11),
        Vector3(0, 0, 11)
    ).seen_by(frustum)
    assert Quad3d(
        Vector3(0, 0, 11),
        Vector3(0, 0, 11),
        Vector3(0, 0, 10),
        Vector3(0, 0, 11)
    ).seen_by(frustum)
    assert Quad3d(
        Vector3(0, 0, 11),
        Vector3(0, 0, 11),
        Vector3(0, 0, 11),
        Vector3(0, 0, 10)
    ).seen_by(frustum)
    # left
    assert not Quad3d(
        Vector3(-6, 0, 5),
        Vector3(-6, 0, 5),
        Vector3(-6, 0, 5),
        Vector3(-6, 0, 5)
    ).seen_by(frustum)
    assert Quad3d(
        Vector3(-5, 0, 5),
        Vector3(-6, 0, 5),
        Vector3(-6, 0, 5),
        Vector3(-6, 0, 5)
    ).seen_by(frustum)
    assert Quad3d(
        Vector3(-6, 0, 5),
        Vector3(-5, 0, 5),
        Vector3(-6, 0, 5),
        Vector3(-6, 0, 5)
    ).seen_by(frustum)
    assert Quad3d(
        Vector3(-6, 0, 5),
        Vector3(-6, 0, 5),
        Vector3(-5, 0, 5),
        Vector3(-6, 0, 5)
    ).seen_by(frustum)
    assert Quad3d(
        Vector3(-6, 0, 5),
        Vector3(-6, 0, 5),
        Vector3(-6, 0, 5),
        Vector3(-5, 0, 5)
    ).seen_by(frustum)
    # right
    assert not Quad3d(
        Vector3(6, 0, 5),
        Vector3(6, 0, 5),
        Vector3(6, 0, 5),
        Vector3(6, 0, 5)
    ).seen_by(frustum)
    assert Quad3d(
        Vector3(5, 0, 5),
        Vector3(6, 0, 5),
        Vector3(6, 0, 5),
        Vector3(6, 0, 5)
    ).seen_by(frustum)
    assert Quad3d(
        Vector3(6, 0, 5),
        Vector3(5, 0, 5),
        Vector3(6, 0, 5),
        Vector3(6, 0, 5)
    ).seen_by(frustum)
    assert Quad3d(
        Vector3(6, 0, 5),
        Vector3(6, 0, 5),
        Vector3(5, 0, 5),
        Vector3(6, 0, 5)
    ).seen_by(frustum)
    assert Quad3d(
        Vector3(6, 0, 5),
        Vector3(6, 0, 5),
        Vector3(6, 0, 5),
        Vector3(5, 0, 5)
    ).seen_by(frustum)
    # bottom
    assert not Quad3d(
        Vector3(0, -6, 5),
        Vector3(0, -6, 5),
        Vector3(0, -6, 5),
        Vector3(0, -6, 5)
    ).seen_by(frustum)
    assert Quad3d(
        Vector3(0, -5, 5),
        Vector3(0, -6, 5),
        Vector3(0, -6, 5),
        Vector3(0, -6, 5)
    ).seen_by(frustum)
    assert Quad3d(
        Vector3(0, -6, 5),
        Vector3(0, -5, 5),
        Vector3(0, -6, 5),
        Vector3(0, -6, 5)
    ).seen_by(frustum)
    assert Quad3d(
        Vector3(0, -6, 5),
        Vector3(0, -6, 5),
        Vector3(0, -5, 5),
        Vector3(0, -6, 5)
    ).seen_by(frustum)
    assert Quad3d(
        Vector3(0, -6, 5),
        Vector3(0, -6, 5),
        Vector3(0, -6, 5),
        Vector3(0, -5, 5)
    ).seen_by(frustum)
    # top
    assert not Quad3d(
        Vector3(0, 6, 5),
        Vector3(0, 6, 5),
        Vector3(0, 6, 5),
        Vector3(0, 6, 5)
    ).seen_by(frustum)
    assert Quad3d(
        Vector3(0, 5, 5),
        Vector3(0, 6, 5),
        Vector3(0, 6, 5),
        Vector3(0, 6, 5)
    ).seen_by(frustum)
    assert Quad3d(
        Vector3(0, 6, 5),
        Vector3(0, 5, 5),
        Vector3(0, 6, 5),
        Vector3(0, 6, 5)
    ).seen_by(frustum)
    assert Quad3d(
        Vector3(0, 6, 5),
        Vector3(0, 6, 5),
        Vector3(0, 5, 5),
        Vector3(0, 6, 5)
    ).seen_by(frustum)
    assert Quad3d(
        Vector3(0, 6, 5),
        Vector3(0, 6, 5),
        Vector3(0, 6, 5),
        Vector3(0, 5, 5)
    ).seen_by(frustum)
