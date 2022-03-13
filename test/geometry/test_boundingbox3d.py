
# gamut
from gamut.geometry import (BoundingBox3d, Plane, Shape3dCullable,
                            Shape3dPointContainer, Sphere, ViewFrustum3d)
from gamut.math import Matrix4, Vector2, Vector3, Vector3Array, Vector4
# python
from math import radians
from typing import Any
# pytest
import pytest


def test_cullable() -> None:
    assert isinstance(
        BoundingBox3d(Vector3Array(Vector3(0))),
        Shape3dCullable
    )


def test_point_container() -> None:
    assert isinstance(
        BoundingBox3d(Vector3Array(Vector3(0))),
        Shape3dPointContainer
    )


def test_repr() -> None:
    bb = BoundingBox3d(Vector3Array(Vector3(1, 2, 3), Vector3(4, 5, 6)))
    assert (
        repr(bb) ==
        f'<gamut.geometry.BoundingBox3d '
        f'min=(1.0, 2.0, 3.0) '
        f'max=(4.0, 5.0, 6.0)>'
    )


def test_no_points() -> None:
    with pytest.raises(ValueError) as excinfo:
        BoundingBox3d(Vector3Array())
    assert str(excinfo.value) == 'must have at least 1 point'


@pytest.mark.parametrize("points", [
    [Vector3(1)],
    [1],
    ['123'],
    [Vector2(1)],
    [Vector4(1)],
])
def test_points_invalid_type(points: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        BoundingBox3d(points)
    assert str(excinfo.value) == 'points must be Vector3Array'


@pytest.mark.parametrize("points", [
    Vector3Array(Vector3(0)),
    Vector3Array(Vector3(0), Vector3(1)),
    Vector3Array(Vector3(0), Vector3(1, 2, 3)),
    Vector3Array(Vector3(0), Vector3(1, 2, 3), Vector3(-1, -2, -3)),
    Vector3Array(
        Vector3(-1, 2, -3),
        Vector3(-4, 0, 0),
        Vector3(2, -3, -2),
        Vector3(0, 1, 4)
    ),
])
def test_min_max_center(points: Vector3Array) -> None:
    bb = BoundingBox3d(points)

    if len(points) > 1:
        expected_min = Vector3(
            min(*(p.x for p in points)),
            min(*(p.y for p in points)),
            min(*(p.z for p in points)),
        )
        expected_max = Vector3(
            max(*(p.x for p in points)),
            max(*(p.y for p in points)),
            max(*(p.z for p in points)),
        )
    else:
        expected_min = points[0]
        expected_max = points[0]

    assert bb.min == expected_min
    assert bb.max == expected_max
    assert bb.center == (expected_min + expected_max) * .5


@pytest.mark.parametrize("points", [
    Vector3Array(Vector3(0)),
    Vector3Array(Vector3(-1, -2, -3), Vector3(1, 2, 3)),
])
def test_corners(points: Vector3Array) -> None:
    bb = BoundingBox3d(points)

    expected_points = tuple(
        Vector3(x, y, z)
        for x in (bb.min.x, bb.max.x)
        for y in (bb.min.y, bb.max.y)
        for z in (bb.min.z, bb.max.z)
    )
    assert bb.corners == expected_points


@pytest.mark.parametrize("bounding_box", [
    BoundingBox3d(Vector3Array(Vector3(0, 0, 0), Vector3(0, 0, 0))),
    BoundingBox3d(Vector3Array(Vector3(-1, -2, -3), Vector3(1, 2, 3))),
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
def test_transform(bounding_box: BoundingBox3d, transform: Matrix4) -> None:
    new_bb = transform @ bounding_box
    assert new_bb is not bounding_box

    transformed_corners = tuple(
        (transform @ Vector4(*c, 1)).xyz
        for c in bounding_box.corners
    )
    expected_min = Vector3(
        min(*(c.x for c in transformed_corners)),
        min(*(c.y for c in transformed_corners)),
        min(*(c.z for c in transformed_corners)),
    )
    expected_max = Vector3(
        max(*(c.x for c in transformed_corners)),
        max(*(c.y for c in transformed_corners)),
        max(*(c.z for c in transformed_corners)),
    )

    assert new_bb.min == expected_min
    assert new_bb.max == expected_max


@pytest.mark.parametrize("transform", [None, 123, Vector4(1), Vector2(1)])
def test_transform_invalid(transform: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        transform @ BoundingBox3d(Vector3Array(Vector3(0)))
    assert str(excinfo.value).startswith('unsupported operand type(s) for @:')


def test_equal() -> None:
    assert BoundingBox3d(Vector3Array((Vector3(0)))) == (
        BoundingBox3d(Vector3Array((Vector3(0))))
    )
    assert (
        BoundingBox3d(Vector3Array(Vector3(1, 2, 3), Vector3(-1, -2, -3))) ==
        BoundingBox3d(Vector3Array(Vector3(1, 2, 3), Vector3(-1, -2, -3)))
    )
    assert (
        BoundingBox3d(Vector3Array(Vector3(1, 2, 3), Vector3(-1, -2, -3))) !=
        BoundingBox3d(Vector3Array(Vector3(0, 2, 3), Vector3(-1, -2, -3)))
    )
    assert (
        BoundingBox3d(Vector3Array(Vector3(1, 2, 3), Vector3(-1, -2, -3))) !=
        BoundingBox3d(Vector3Array(Vector3(1, 0, 3), Vector3(-1, -2, -3)))
    )
    assert (
        BoundingBox3d(Vector3Array(Vector3(1, 2, 3), Vector3(-1, -2, -3))) !=
        BoundingBox3d(Vector3Array(Vector3(1, 2, 0), Vector3(-1, -2, -3)))
    )
    assert (
        BoundingBox3d(Vector3Array(Vector3(1, 2, 3), Vector3(-1, -2, -3))) !=
        BoundingBox3d(Vector3Array(Vector3(1, 2, 3), Vector3(0, -2, -3)))
    )
    assert (
        BoundingBox3d(Vector3Array(Vector3(1, 2, 3), Vector3(-1, -2, -3))) !=
        BoundingBox3d(Vector3Array(Vector3(1, 2, 3), Vector3(-1, 0, -3)))
    )
    assert (
        BoundingBox3d(Vector3Array(Vector3(1, 2, 3), Vector3(-1, -2, -3))) !=
        BoundingBox3d(Vector3Array(Vector3(1, 2, 3), Vector3(-1, -2, 0)))
    )
    assert BoundingBox3d(Vector3Array(Vector3(0))) != object()


@pytest.mark.parametrize("bounding_box", [
    BoundingBox3d(Vector3Array(Vector3(0))),
    BoundingBox3d(Vector3Array(Vector3(-1, -1, -1), Vector3(1, 1, 1))),
    BoundingBox3d(Vector3Array(Vector3(-1000, 0, 67), Vector3(20, -56, 87))),
])
def test_contains_point(bounding_box: BoundingBox3d) -> None:
    assert bounding_box.contains_point(bounding_box.center)
    for corner in bounding_box.corners:
        assert bounding_box.contains_point(corner)

    for offset in (
        Vector3(1, -1, -1),
        Vector3(-1, 1, -1),
        Vector3(-1, -1, 1),
        Vector3(1, 1, -1),
        Vector3(1, -1, 1),
        Vector3(-1, 1, 1),
        Vector3(1, 1, 1),
    ):
        assert not bounding_box.contains_point(bounding_box.min - offset)
        assert not bounding_box.contains_point(bounding_box.max + offset)


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
    assert not BoundingBox3d(Vector3Array(Vector3(0))).seen_by(frustum)
    assert BoundingBox3d(
        Vector3Array(Vector3(-1), Vector3(1))
    ).seen_by(frustum)
    assert BoundingBox3d(Vector3Array(Vector3(0, 0, 1))).seen_by(frustum)
    # far
    assert not BoundingBox3d(Vector3Array(Vector3(0, 0, 11))).seen_by(frustum)
    assert BoundingBox3d(
        Vector3Array(Vector3(0, 0, 10), Vector3(0, 0, 11))
    ).seen_by(frustum)
    assert BoundingBox3d(Vector3Array(Vector3(0, 0, 10))).seen_by(frustum)
    # left
    assert not BoundingBox3d(Vector3Array(Vector3(-6, 0, 5))).seen_by(frustum)
    assert BoundingBox3d(
        Vector3Array(Vector3(-6, 0, 5), Vector3(-5, 0, 5))
    ).seen_by(frustum)
    assert BoundingBox3d(Vector3Array(Vector3(-5, 0, 5))).seen_by(frustum)
    # right
    assert not BoundingBox3d(Vector3Array(Vector3(6, 0, 5))).seen_by(frustum)
    assert BoundingBox3d(
        Vector3Array(Vector3(6, 0, 5), Vector3(5, 0, 5))
    ).seen_by(frustum)
    assert BoundingBox3d(Vector3Array(Vector3(5, 0, 5))).seen_by(frustum)
    # bottom
    assert not BoundingBox3d(Vector3Array(Vector3(0, -6, 5))).seen_by(frustum)
    assert BoundingBox3d(
        Vector3Array(Vector3(0, -6, 5), Vector3(0, -5, 5))
    ).seen_by(frustum)
    assert BoundingBox3d(Vector3Array(Vector3(0, -5, 5))).seen_by(frustum)
    # top
    assert not BoundingBox3d(Vector3Array(Vector3(0, 6, 5))).seen_by(frustum)
    assert BoundingBox3d(
        Vector3Array(Vector3(0, 6, 5), Vector3(0, 5, 5))
    ).seen_by(frustum)
    assert BoundingBox3d(Vector3Array(Vector3(0, 5, 5))).seen_by(frustum)


def test_intersects_sphere() -> None:
    sphere = Sphere(Vector3(0, 0, 0), 1)

    assert BoundingBox3d(Vector3Array(
        Vector3(0)
    )).intersects_sphere(sphere)
    assert BoundingBox3d(Vector3Array(
        Vector3(-1, 0, 0)
    )).intersects_sphere(sphere)
    assert BoundingBox3d(Vector3Array(
        Vector3(1, 0, 0)
    )).intersects_sphere(sphere)
    assert BoundingBox3d(Vector3Array(
        Vector3(0, -1, 0))
    ).intersects_sphere(sphere)
    assert BoundingBox3d(Vector3Array(
        Vector3(0, 1, 0))
    ).intersects_sphere(sphere)
    assert BoundingBox3d(Vector3Array(
        Vector3(0, 0, -1))
    ).intersects_sphere(sphere)
    assert BoundingBox3d(Vector3Array(
        Vector3(0, 0, 1))
    ).intersects_sphere(sphere)

    assert not BoundingBox3d(Vector3Array(
        Vector3(-1.1, 0, 0))
    ).intersects_sphere(sphere)
    assert not BoundingBox3d(Vector3Array(
        Vector3(1.1, 0, 0))
    ).intersects_sphere(sphere)
    assert not BoundingBox3d(Vector3Array(
        Vector3(0, -1.1, 0))
    ).intersects_sphere(sphere)
    assert not BoundingBox3d(Vector3Array(
        Vector3(0, 1.1, 0))
    ).intersects_sphere(sphere)
    assert not BoundingBox3d(Vector3Array(
        Vector3(0, 0, -1.1))
    ).intersects_sphere(sphere)
    assert not BoundingBox3d(Vector3Array(
        Vector3(0, 0, 1.1))
    ).intersects_sphere(sphere)
