
# gamut
from gamut.geometry import Plane, Quad3d, Shape3dCullable, ViewFrustum3d
# python
from typing import Any
# pyglm
from glm import mat4, radians, rotate, scale, translate, vec2, vec3, vec4
# pytest
import pytest


def test_cullable() -> None:
    assert isinstance(
        Quad3d(vec3(0), vec3(0), vec3(0), vec3(0)),
        Shape3dCullable
    )


def test_repr() -> None:
    quad = Quad3d(
        vec3(0, 1, 2),
        vec3(3, 4, 5),
        vec3(6, 7, 8),
        vec3(9, 10, 11)
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

@pytest.mark.parametrize("point", [None, '123', 123, vec4(1), vec2(1)])
@pytest.mark.parametrize("point_index", range(4))
def test_invalid_point(point: Any, point_index: int) -> None:
    points = [vec3(0), vec3(0), vec3(0), vec3(0)]
    points[point_index] = point
    with pytest.raises(TypeError) as excinfo:
        Quad3d(*points)
    assert str(excinfo.value) == 'each point must be vec3'


@pytest.mark.parametrize("point_type", [vec3, tuple, list])
def test_points(point_type: Any) -> None:
    expected_points = (
        vec3(0, 1, 2),
        vec3(3, 4, 5),
        vec3(6, 7, 8),
        vec3(9, 10, 11)
    )
    quad = Quad3d(*(point_type(p) for p in expected_points))
    assert quad.points == expected_points


@pytest.mark.parametrize("quad", [
    Quad3d(vec3(0), vec3(0), vec3(0), vec3(0)),
    Quad3d(
        vec3(0, 1, 2),
        vec3(3, 4, 5),
        vec3(6, 7, 8),
        vec3(9, 10, 11)
    )
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
def test_transform(quad: Quad3d, transform: mat4) -> None:
    new_quad = transform * quad
    assert new_quad is not quad

    expected_points = tuple(
        transform * p
        for p in quad.points
    )

    assert new_quad.points == expected_points


@pytest.mark.parametrize("transform", [None, 123, vec4(1), vec2(1)])
def test_transform_invalid(transform: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        transform * Quad3d(vec3(0), vec3(0), vec3(0), vec3(0))
    assert str(excinfo.value).startswith('unsupported operand type(s) for *:')



def test_equal() -> None:
    zero_quad = Quad3d(vec3(0), vec3(0), vec3(0), vec3(0))
    assert zero_quad == zero_quad
    assert zero_quad != Quad3d(vec3(1), vec3(0), vec3(0), vec3(0))
    assert zero_quad != Quad3d(vec3(0), vec3(1), vec3(0), vec3(0))
    assert zero_quad != Quad3d(vec3(0), vec3(0), vec3(1), vec3(0))
    assert zero_quad != Quad3d(vec3(0), vec3(0), vec3(0), vec3(1))
    assert zero_quad != object()


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
    assert not Quad3d(vec3(0), vec3(0), vec3(0), vec3(0)).seen_by(frustum)
    assert Quad3d(vec3(0, 0, 1), vec3(0), vec3(0), vec3(0)).seen_by(frustum)
    assert Quad3d(vec3(0), vec3(0, 0, 1), vec3(0), vec3(0)).seen_by(frustum)
    assert Quad3d(vec3(0), vec3(0), vec3(0, 0, 1), vec3(0)).seen_by(frustum)
    assert Quad3d(vec3(0), vec3(0), vec3(0), vec3(0, 0, 1)).seen_by(frustum)
    # far
    assert not Quad3d(
        vec3(0, 0, 11),
        vec3(0, 0, 11),
        vec3(0, 0, 11),
        vec3(0, 0, 11)
    ).seen_by(frustum)
    assert Quad3d(
        vec3(0, 0, 10),
        vec3(0, 0, 11),
        vec3(0, 0, 11),
        vec3(0, 0, 11)
    ).seen_by(frustum)
    assert Quad3d(
        vec3(0, 0, 11),
        vec3(0, 0, 10),
        vec3(0, 0, 11),
        vec3(0, 0, 11)
    ).seen_by(frustum)
    assert Quad3d(
        vec3(0, 0, 11),
        vec3(0, 0, 11),
        vec3(0, 0, 10),
        vec3(0, 0, 11)
    ).seen_by(frustum)
    assert Quad3d(
        vec3(0, 0, 11),
        vec3(0, 0, 11),
        vec3(0, 0, 11),
        vec3(0, 0, 10)
    ).seen_by(frustum)
    # left
    assert not Quad3d(
        vec3(-6, 0, 5),
        vec3(-6, 0, 5),
        vec3(-6, 0, 5),
        vec3(-6, 0, 5)
    ).seen_by(frustum)
    assert Quad3d(
        vec3(-5, 0, 5),
        vec3(-6, 0, 5),
        vec3(-6, 0, 5),
        vec3(-6, 0, 5)
    ).seen_by(frustum)
    assert Quad3d(
        vec3(-6, 0, 5),
        vec3(-5, 0, 5),
        vec3(-6, 0, 5),
        vec3(-6, 0, 5)
    ).seen_by(frustum)
    assert Quad3d(
        vec3(-6, 0, 5),
        vec3(-6, 0, 5),
        vec3(-5, 0, 5),
        vec3(-6, 0, 5)
    ).seen_by(frustum)
    assert Quad3d(
        vec3(-6, 0, 5),
        vec3(-6, 0, 5),
        vec3(-6, 0, 5),
        vec3(-5, 0, 5)
    ).seen_by(frustum)
    # right
    assert not Quad3d(
        vec3(6, 0, 5),
        vec3(6, 0, 5),
        vec3(6, 0, 5),
        vec3(6, 0, 5)
    ).seen_by(frustum)
    assert Quad3d(
        vec3(5, 0, 5),
        vec3(6, 0, 5),
        vec3(6, 0, 5),
        vec3(6, 0, 5)
    ).seen_by(frustum)
    assert Quad3d(
        vec3(6, 0, 5),
        vec3(5, 0, 5),
        vec3(6, 0, 5),
        vec3(6, 0, 5)
    ).seen_by(frustum)
    assert Quad3d(
        vec3(6, 0, 5),
        vec3(6, 0, 5),
        vec3(5, 0, 5),
        vec3(6, 0, 5)
    ).seen_by(frustum)
    assert Quad3d(
        vec3(6, 0, 5),
        vec3(6, 0, 5),
        vec3(6, 0, 5),
        vec3(5, 0, 5)
    ).seen_by(frustum)
    # bottom
    assert not Quad3d(
        vec3(0, -6, 5),
        vec3(0, -6, 5),
        vec3(0, -6, 5),
        vec3(0, -6, 5)
    ).seen_by(frustum)
    assert Quad3d(
        vec3(0, -5, 5),
        vec3(0, -6, 5),
        vec3(0, -6, 5),
        vec3(0, -6, 5)
    ).seen_by(frustum)
    assert Quad3d(
        vec3(0, -6, 5),
        vec3(0, -5, 5),
        vec3(0, -6, 5),
        vec3(0, -6, 5)
    ).seen_by(frustum)
    assert Quad3d(
        vec3(0, -6, 5),
        vec3(0, -6, 5),
        vec3(0, -5, 5),
        vec3(0, -6, 5)
    ).seen_by(frustum)
    assert Quad3d(
        vec3(0, -6, 5),
        vec3(0, -6, 5),
        vec3(0, -6, 5),
        vec3(0, -5, 5)
    ).seen_by(frustum)
    # top
    assert not Quad3d(
        vec3(0, 6, 5),
        vec3(0, 6, 5),
        vec3(0, 6, 5),
        vec3(0, 6, 5)
    ).seen_by(frustum)
    assert Quad3d(
        vec3(0, 5, 5),
        vec3(0, 6, 5),
        vec3(0, 6, 5),
        vec3(0, 6, 5)
    ).seen_by(frustum)
    assert Quad3d(
        vec3(0, 6, 5),
        vec3(0, 5, 5),
        vec3(0, 6, 5),
        vec3(0, 6, 5)
    ).seen_by(frustum)
    assert Quad3d(
        vec3(0, 6, 5),
        vec3(0, 6, 5),
        vec3(0, 5, 5),
        vec3(0, 6, 5)
    ).seen_by(frustum)
    assert Quad3d(
        vec3(0, 6, 5),
        vec3(0, 6, 5),
        vec3(0, 6, 5),
        vec3(0, 5, 5)
    ).seen_by(frustum)
