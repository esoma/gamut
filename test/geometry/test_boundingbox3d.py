
# gamut
from gamut.geometry import BoundingBox3d, Plane, ViewFrustum3d
# python
from typing import Any
# pyglm
from glm import mat4, radians, rotate, scale, translate, vec2, vec3, vec4
# pytest
import pytest


def test_repr() -> None:
    bb = BoundingBox3d(vec3(1, 2, 3), vec3(4, 5, 6))
    assert (
        repr(bb) ==
        f'<gamut.geometry.BoundingBox3d '
        f'min=(1.0, 2.0, 3.0) '
        f'max=(4.0, 5.0, 6.0)>'
    )


def test_no_points() -> None:
    with pytest.raises(ValueError) as excinfo:
        BoundingBox3d()
    assert str(excinfo.value) == 'must have at least 1 point'


@pytest.mark.parametrize("good_points", [
    [],
    [vec3(0)],
    [vec3(0), vec3(0)],
])
@pytest.mark.parametrize("points", [
    [None],
    [1],
    ['123'],
    [vec2(1)],
    [vec4(1)],
])
def test_points_invalid_type(good_points: Any, points: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        BoundingBox3d(*good_points, *points)
    assert str(excinfo.value) == 'each point must be vec3'


@pytest.mark.parametrize("points", [
    [vec3(0)],
    [vec3(0), vec3(1)],
    [vec3(0), vec3(1, 2, 3)],
    [vec3(0), vec3(1, 2, 3), vec3(-1, -2, -3)],
    [vec3(-1, 2, -3), vec3(-4, 0, 0), vec3(2, -3, -2), vec3(0, 1, 4)],
])
@pytest.mark.parametrize("point_type", [vec3, tuple, list])
def test_min_max(points: list[vec3], point_type: Any) -> None:
    bb = BoundingBox3d(*(point_type(p) for p in points))

    if len(points) > 1:
        expected_min = vec3(
            min(*(p.x for p in points)),
            min(*(p.y for p in points)),
            min(*(p.z for p in points)),
        )
        expected_max = vec3(
            max(*(p.x for p in points)),
            max(*(p.y for p in points)),
            max(*(p.z for p in points)),
        )
    else:
        expected_min = points[0]
        expected_max = points[0]

    assert bb.min == expected_min
    assert bb.max == expected_max


@pytest.mark.parametrize("points", [
    [vec3(0)],
    [vec3(-1, -2, -3), vec3(1, 2, 3)],
])
def test_corners(points: list[vec3]) -> None:
    bb = BoundingBox3d(*points)

    expected_points = tuple(
        vec3(x, y, z)
        for x in (bb.min.x, bb.max.x)
        for y in (bb.min.y, bb.max.y)
        for z in (bb.min.z, bb.max.z)
    )
    assert bb.corners == expected_points


@pytest.mark.parametrize("bounding_box", [
    BoundingBox3d(vec3(0, 0, 0), vec3(0, 0, 0)),
    BoundingBox3d(vec3(-1, -2, -3), vec3(1, 2, 3)),
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
def test_transform(bounding_box: BoundingBox3d, transform: mat4) -> None:
    new_bb = transform * bounding_box
    assert new_bb is not bounding_box

    transformed_corners = tuple(transform * c for c in bounding_box.corners)
    expected_min = vec3(
        min(*(c.x for c in transformed_corners)),
        min(*(c.y for c in transformed_corners)),
        min(*(c.z for c in transformed_corners)),
    )
    expected_max = vec3(
        max(*(c.x for c in transformed_corners)),
        max(*(c.y for c in transformed_corners)),
        max(*(c.z for c in transformed_corners)),
    )

    assert new_bb.min == expected_min
    assert new_bb.max == expected_max


@pytest.mark.parametrize("transform", [None, 123, vec4(1), vec2(1)])
def test_transform_invalid(transform: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        transform * BoundingBox3d(vec3(0))
    assert str(excinfo.value).startswith('unsupported operand type(s) for *:')


def test_equal() -> None:
    assert BoundingBox3d(vec3(0)) == BoundingBox3d(vec3(0))
    assert (
        BoundingBox3d(vec3(1, 2, 3), vec3(-1, -2, -3)) ==
        BoundingBox3d(vec3(1, 2, 3), vec3(-1, -2, -3))
    )
    assert (
        BoundingBox3d(vec3(1, 2, 3), vec3(-1, -2, -3)) !=
        BoundingBox3d(vec3(0, 2, 3), vec3(-1, -2, -3))
    )
    assert (
        BoundingBox3d(vec3(1, 2, 3), vec3(-1, -2, -3)) !=
        BoundingBox3d(vec3(1, 0, 3), vec3(-1, -2, -3))
    )
    assert (
        BoundingBox3d(vec3(1, 2, 3), vec3(-1, -2, -3)) !=
        BoundingBox3d(vec3(1, 2, 0), vec3(-1, -2, -3))
    )
    assert (
        BoundingBox3d(vec3(1, 2, 3), vec3(-1, -2, -3)) !=
        BoundingBox3d(vec3(1, 2, 3), vec3(0, -2, -3))
    )
    assert (
        BoundingBox3d(vec3(1, 2, 3), vec3(-1, -2, -3)) !=
        BoundingBox3d(vec3(1, 2, 3), vec3(-1, 0, -3))
    )
    assert (
        BoundingBox3d(vec3(1, 2, 3), vec3(-1, -2, -3)) !=
        BoundingBox3d(vec3(1, 2, 3), vec3(-1, -2, 0))
    )
    assert BoundingBox3d(vec3(0)) == object()


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
    assert not BoundingBox3d(vec3(0)).seen_by(frustum)
    assert BoundingBox3d(vec3(-1), vec3(1)).seen_by(frustum)
    assert BoundingBox3d(vec3(0, 0, 1)).seen_by(frustum)
    # far
    assert not BoundingBox3d(vec3(0, 0, 11)).seen_by(frustum)
    assert BoundingBox3d(vec3(0, 0, 10), vec3(0, 0, 11)).seen_by(frustum)
    assert BoundingBox3d(vec3(0, 0, 10)).seen_by(frustum)
    # left
    assert not BoundingBox3d(vec3(-6, 0, 5)).seen_by(frustum)
    assert BoundingBox3d(vec3(-6, 0, 5), vec3(-5, 0, 5)).seen_by(frustum)
    assert BoundingBox3d(vec3(-5, 0, 5)).seen_by(frustum)
    # right
    assert not BoundingBox3d(vec3(6, 0, 5)).seen_by(frustum)
    assert BoundingBox3d(vec3(6, 0, 5), vec3(5, 0, 5)).seen_by(frustum)
    assert BoundingBox3d(vec3(5, 0, 5)).seen_by(frustum)
    # bottom
    assert not BoundingBox3d(vec3(0, -6, 5)).seen_by(frustum)
    assert BoundingBox3d(vec3(0, -6, 5), vec3(0, -5, 5)).seen_by(frustum)
    assert BoundingBox3d(vec3(0, -5, 5)).seen_by(frustum)
    # top
    assert not BoundingBox3d(vec3(0, 6, 5)).seen_by(frustum)
    assert BoundingBox3d(vec3(0, 6, 5), vec3(0, 5, 5)).seen_by(frustum)
    assert BoundingBox3d(vec3(0, 5, 5)).seen_by(frustum)
