
# gamut
from gamut.geometry import (BoundingBox3d, Plane, Shape3dCullable,
                            Shape3dPointContainer, Sphere, ViewFrustum3d)
from gamut.math import (DMatrix4, DVector2, DVector3, DVector3Array, DVector4,
                        FMatrix4, FVector3, FVector3Array, FVector4)
# python
from math import radians
from typing import Any
# pytest
import pytest


def test_cullable() -> None:
    assert isinstance(
        BoundingBox3d(DVector3Array(DVector3(0))),
        Shape3dCullable
    )


def test_point_container() -> None:
    assert isinstance(
        BoundingBox3d(DVector3Array(DVector3(0))),
        Shape3dPointContainer
    )


def test_hash() -> None:
    bb1 = BoundingBox3d(FVector3Array(FVector3(1, 2, 3), FVector3(4, 5, 6)))
    bb2 = BoundingBox3d(FVector3Array(FVector3(1, 2, 3), FVector3(4, 5, 6)))
    assert hash(bb1) == hash(bb2)
    bb3 = BoundingBox3d(DVector3Array(DVector3(1, 2, 3), DVector3(4, 5, 6)))
    assert hash(bb1) != hash(bb3)


@pytest.mark.parametrize("bounding_box", [
    BoundingBox3d(FVector3Array(FVector3(1, 2, 3), FVector3(4, 5, 6))),
    BoundingBox3d(DVector3Array(DVector3(1, 2, 3), DVector3(4, 5, 6)))
])
def test_repr(bounding_box: BoundingBox3d) -> None:
    assert (
        repr(bounding_box) ==
        f'<gamut.geometry.BoundingBox3d '
        f'min=(1.0, 2.0, 3.0) '
        f'max=(4.0, 5.0, 6.0)>'
    )


@pytest.mark.parametrize("points", [FVector3Array(), DVector3Array()])
def test_no_points(points: Any) -> None:
    with pytest.raises(ValueError) as excinfo:
        BoundingBox3d(points)
    assert str(excinfo.value) == 'must have at least 1 point'


@pytest.mark.parametrize("points", [
    [DVector3(1)],
    [1],
    ['123'],
    [DVector2(1)],
    [DVector4(1)],
])
def test_points_invalid_type(points: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        BoundingBox3d(points)
    assert str(excinfo.value) == (
        'points must be FVector3Array or DVector3Array'
    )


@pytest.mark.parametrize("points", [
    FVector3Array(FVector3(0)),
    FVector3Array(FVector3(0), FVector3(1)),
    FVector3Array(FVector3(0), FVector3(1, 2, 3)),
    FVector3Array(FVector3(0), FVector3(1, 2, 3), FVector3(-1, -2, -3)),
    FVector3Array(
        FVector3(-1, 2, -3),
        FVector3(-4, 0, 0),
        FVector3(2, -3, -2),
        FVector3(0, 1, 4)
    ),
    DVector3Array(DVector3(0)),
    DVector3Array(DVector3(0), DVector3(1)),
    DVector3Array(DVector3(0), DVector3(1, 2, 3)),
    DVector3Array(DVector3(0), DVector3(1, 2, 3), DVector3(-1, -2, -3)),
    DVector3Array(
        DVector3(-1, 2, -3),
        DVector3(-4, 0, 0),
        DVector3(2, -3, -2),
        DVector3(0, 1, 4)
    ),
])
def test_min_max_center(points: Any) -> None:
    bb = BoundingBox3d(points)

    if len(points) > 1:
        expected_min = points.get_component_type()(
            min(*(p.x for p in points)),
            min(*(p.y for p in points)),
            min(*(p.z for p in points)),
        )
        expected_max = points.get_component_type()(
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
    FVector3Array(FVector3(0)),
    FVector3Array(FVector3(-1, -2, -3), FVector3(1, 2, 3)),
    DVector3Array(DVector3(0)),
    DVector3Array(DVector3(-1, -2, -3), DVector3(1, 2, 3)),
])
def test_corners(points: Any) -> None:
    bb = BoundingBox3d(points)
    expected_points = tuple(
        points.get_component_type()(x, y, z)
        for x in (bb.min.x, bb.max.x)
        for y in (bb.min.y, bb.max.y)
        for z in (bb.min.z, bb.max.z)
    )
    assert bb.corners == expected_points


@pytest.mark.parametrize("bounding_box", [
    BoundingBox3d(FVector3Array(FVector3(0, 0, 0), FVector3(0, 0, 0))),
    BoundingBox3d(FVector3Array(FVector3(-1, -2, -3), FVector3(1, 2, 3))),
])
@pytest.mark.parametrize("transform", [
    FMatrix4(1).translate(FVector3(1, 0, 0)),
    FMatrix4(1).translate(FVector3(0, 1, 0)),
    FMatrix4(1).translate(FVector3(0, 0, 1)),
    FMatrix4(1).rotate(radians(90), FVector3(1, 0, 0)),
    FMatrix4(1).rotate(radians(90), FVector3(0, 1, 0)),
    FMatrix4(1).rotate(radians(90), FVector3(0, 0, 1)),
    FMatrix4(1).scale(FVector3(2, 3, 4)),
])
def test_f_transform(bounding_box: BoundingBox3d, transform: FMatrix4) -> None:
    new_bb = transform @ bounding_box
    assert new_bb is not bounding_box

    transformed_corners = tuple(
        (transform @ FVector4(*c, 1)).xyz
        for c in bounding_box.corners
    )
    expected_min = FVector3(
        min(*(c.x for c in transformed_corners)),
        min(*(c.y for c in transformed_corners)),
        min(*(c.z for c in transformed_corners)),
    )
    expected_max = FVector3(
        max(*(c.x for c in transformed_corners)),
        max(*(c.y for c in transformed_corners)),
        max(*(c.z for c in transformed_corners)),
    )

    assert new_bb.min == expected_min
    assert new_bb.max == expected_max


@pytest.mark.parametrize("bounding_box", [
    BoundingBox3d(DVector3Array(DVector3(0, 0, 0), DVector3(0, 0, 0))),
    BoundingBox3d(DVector3Array(DVector3(-1, -2, -3), DVector3(1, 2, 3))),
])
@pytest.mark.parametrize("transform", [
    DMatrix4(1).translate(DVector3(1, 0, 0)),
    DMatrix4(1).translate(DVector3(0, 1, 0)),
    DMatrix4(1).translate(DVector3(0, 0, 1)),
    DMatrix4(1).rotate(radians(90), DVector3(1, 0, 0)),
    DMatrix4(1).rotate(radians(90), DVector3(0, 1, 0)),
    DMatrix4(1).rotate(radians(90), DVector3(0, 0, 1)),
    DMatrix4(1).scale(DVector3(2, 3, 4)),
])
def test_d_transform(bounding_box: BoundingBox3d, transform: DMatrix4) -> None:
    new_bb = transform @ bounding_box
    assert new_bb is not bounding_box

    transformed_corners = tuple(
        (transform @ DVector4(*c, 1)).xyz
        for c in bounding_box.corners
    )
    expected_min = DVector3(
        min(*(c.x for c in transformed_corners)),
        min(*(c.y for c in transformed_corners)),
        min(*(c.z for c in transformed_corners)),
    )
    expected_max = DVector3(
        max(*(c.x for c in transformed_corners)),
        max(*(c.y for c in transformed_corners)),
        max(*(c.z for c in transformed_corners)),
    )

    assert new_bb.min == expected_min
    assert new_bb.max == expected_max


@pytest.mark.parametrize("bounding_box", [
    BoundingBox3d(FVector3Array(FVector3(0))),
    BoundingBox3d(DVector3Array(DVector3(0))),
])
@pytest.mark.parametrize("transform", [None, 123, DVector4(1), DVector2(1)])
def test_transform_invalid(
    bounding_box: BoundingBox3d,
    transform: Any
) -> None:
    with pytest.raises(TypeError) as excinfo:
        transform @ bounding_box
    assert str(excinfo.value).startswith('unsupported operand type(s) for @:')


def test_transform_wrong_type():
    with pytest.raises(TypeError) as excinfo:
        DMatrix4(1) @ BoundingBox3d(FVector3Array(FVector3(0)))
    assert str(excinfo.value).startswith('unsupported operand type(s) for @:')

    with pytest.raises(TypeError) as excinfo:
        FMatrix4(1) @ BoundingBox3d(DVector3Array(DVector3(0)))
    assert str(excinfo.value).startswith('unsupported operand type(s) for @:')


@pytest.mark.parametrize("array_type", [FVector3Array, DVector3Array])
def test_equal(array_type: Any) -> None:
    v_type = array_type.get_component_type()
    assert BoundingBox3d(array_type((v_type(0)))) == (
        BoundingBox3d(array_type((v_type(0))))
    )
    assert (
        BoundingBox3d(array_type(v_type(1, 2, 3), v_type(-1, -2, -3))) ==
        BoundingBox3d(array_type(v_type(1, 2, 3), v_type(-1, -2, -3)))
    )
    assert (
        BoundingBox3d(array_type(v_type(1, 2, 3), v_type(-1, -2, -3))) !=
        BoundingBox3d(array_type(v_type(0, 2, 3), v_type(-1, -2, -3)))
    )
    assert (
        BoundingBox3d(array_type(v_type(1, 2, 3), v_type(-1, -2, -3))) !=
        BoundingBox3d(array_type(v_type(1, 0, 3), v_type(-1, -2, -3)))
    )
    assert (
        BoundingBox3d(array_type(v_type(1, 2, 3), v_type(-1, -2, -3))) !=
        BoundingBox3d(array_type(v_type(1, 2, 0), v_type(-1, -2, -3)))
    )
    assert (
        BoundingBox3d(array_type(v_type(1, 2, 3), v_type(-1, -2, -3))) !=
        BoundingBox3d(array_type(v_type(1, 2, 3), v_type(0, -2, -3)))
    )
    assert (
        BoundingBox3d(array_type(v_type(1, 2, 3), v_type(-1, -2, -3))) !=
        BoundingBox3d(array_type(v_type(1, 2, 3), v_type(-1, 0, -3)))
    )
    assert (
        BoundingBox3d(array_type(v_type(1, 2, 3), v_type(-1, -2, -3))) !=
        BoundingBox3d(array_type(v_type(1, 2, 3), v_type(-1, -2, 0)))
    )
    assert BoundingBox3d(array_type(v_type(0))) != object()


@pytest.mark.parametrize("bounding_box", [
    BoundingBox3d(FVector3Array(FVector3(0))),
    BoundingBox3d(FVector3Array(FVector3(-1, -1, -1), FVector3(1, 1, 1))),
    BoundingBox3d(FVector3Array(
        FVector3(-1000, 0, 67),
        FVector3(20, -56, 87))
    ),
])
def test_f_contains_point(bounding_box: BoundingBox3d) -> None:
    assert bounding_box.contains_point(bounding_box.center)
    for corner in bounding_box.corners:
        assert bounding_box.contains_point(corner)

    for offset in (
        FVector3(1, -1, -1),
        FVector3(-1, 1, -1),
        FVector3(-1, -1, 1),
        FVector3(1, 1, -1),
        FVector3(1, -1, 1),
        FVector3(-1, 1, 1),
        FVector3(1, 1, 1),
    ):
        assert not bounding_box.contains_point(bounding_box.min - offset)
        assert not bounding_box.contains_point(bounding_box.max + offset)


@pytest.mark.parametrize("bounding_box", [
    BoundingBox3d(DVector3Array(DVector3(0))),
    BoundingBox3d(DVector3Array(DVector3(-1, -1, -1), DVector3(1, 1, 1))),
    BoundingBox3d(DVector3Array(
        DVector3(-1000, 0, 67),
        DVector3(20, -56, 87))
    ),
])
def test_d_contains_point(bounding_box: BoundingBox3d) -> None:
    assert bounding_box.contains_point(bounding_box.center)
    for corner in bounding_box.corners:
        assert bounding_box.contains_point(corner)

    for offset in (
        DVector3(1, -1, -1),
        DVector3(-1, 1, -1),
        DVector3(-1, -1, 1),
        DVector3(1, 1, -1),
        DVector3(1, -1, 1),
        DVector3(-1, 1, 1),
        DVector3(1, 1, 1),
    ):
        assert not bounding_box.contains_point(bounding_box.min - offset)
        assert not bounding_box.contains_point(bounding_box.max + offset)


def test_contains_point_wrong_type():
    with pytest.raises(TypeError) as excinfo:
        BoundingBox3d(FVector3Array(FVector3(0))).contains_point(DVector3(0))
    assert str(excinfo.value).startswith('point must be FVector3')

    with pytest.raises(TypeError) as excinfo:
        BoundingBox3d(DVector3Array(DVector3(0))).contains_point(FVector3(0))
    assert str(excinfo.value).startswith('point must be DVector3')


def test_seen_by() -> None:
    frustum = ViewFrustum3d(
        Plane(-1, DVector3(0, 0, 1)),
        Plane(10, DVector3(0, 0, -1)),
        Plane(5, DVector3(1, 0, 0)),
        Plane(5, DVector3(-1, 0, 0)),
        Plane(5, DVector3(0, 1, 0)),
        Plane(5, DVector3(0, -1, 0)),
    )

    # near
    assert not BoundingBox3d(DVector3Array(DVector3(0))).seen_by(frustum)
    assert BoundingBox3d(
        DVector3Array(DVector3(-1), DVector3(1))
    ).seen_by(frustum)
    assert BoundingBox3d(DVector3Array(DVector3(0, 0, 1))).seen_by(frustum)
    # far
    assert not BoundingBox3d(
        DVector3Array(DVector3(0, 0, 11))
    ).seen_by(frustum)
    assert BoundingBox3d(
        DVector3Array(DVector3(0, 0, 10), DVector3(0, 0, 11))
    ).seen_by(frustum)
    assert BoundingBox3d(DVector3Array(DVector3(0, 0, 10))).seen_by(frustum)
    # left
    assert not BoundingBox3d(
        DVector3Array(DVector3(-6, 0, 5))
    ).seen_by(frustum)
    assert BoundingBox3d(
        DVector3Array(DVector3(-6, 0, 5), DVector3(-5, 0, 5))
    ).seen_by(frustum)
    assert BoundingBox3d(DVector3Array(DVector3(-5, 0, 5))).seen_by(frustum)
    # right
    assert not BoundingBox3d(DVector3Array(DVector3(6, 0, 5))).seen_by(frustum)
    assert BoundingBox3d(
        DVector3Array(DVector3(6, 0, 5), DVector3(5, 0, 5))
    ).seen_by(frustum)
    assert BoundingBox3d(DVector3Array(DVector3(5, 0, 5))).seen_by(frustum)
    # bottom
    assert not BoundingBox3d(
        DVector3Array(DVector3(0, -6, 5))
    ).seen_by(frustum)
    assert BoundingBox3d(
        DVector3Array(DVector3(0, -6, 5), DVector3(0, -5, 5))
    ).seen_by(frustum)
    assert BoundingBox3d(DVector3Array(DVector3(0, -5, 5))).seen_by(frustum)
    # top
    assert not BoundingBox3d(DVector3Array(DVector3(0, 6, 5))).seen_by(frustum)
    assert BoundingBox3d(
        DVector3Array(DVector3(0, 6, 5), DVector3(0, 5, 5))
    ).seen_by(frustum)
    assert BoundingBox3d(DVector3Array(DVector3(0, 5, 5))).seen_by(frustum)


def test_intersects_sphere() -> None:
    sphere = Sphere(DVector3(0, 0, 0), 1)

    assert BoundingBox3d(DVector3Array(
        DVector3(0)
    )).intersects_sphere(sphere)
    assert BoundingBox3d(DVector3Array(
        DVector3(-1, 0, 0)
    )).intersects_sphere(sphere)
    assert BoundingBox3d(DVector3Array(
        DVector3(1, 0, 0)
    )).intersects_sphere(sphere)
    assert BoundingBox3d(DVector3Array(
        DVector3(0, -1, 0))
    ).intersects_sphere(sphere)
    assert BoundingBox3d(DVector3Array(
        DVector3(0, 1, 0))
    ).intersects_sphere(sphere)
    assert BoundingBox3d(DVector3Array(
        DVector3(0, 0, -1))
    ).intersects_sphere(sphere)
    assert BoundingBox3d(DVector3Array(
        DVector3(0, 0, 1))
    ).intersects_sphere(sphere)

    assert not BoundingBox3d(DVector3Array(
        DVector3(-1.1, 0, 0))
    ).intersects_sphere(sphere)
    assert not BoundingBox3d(DVector3Array(
        DVector3(1.1, 0, 0))
    ).intersects_sphere(sphere)
    assert not BoundingBox3d(DVector3Array(
        DVector3(0, -1.1, 0))
    ).intersects_sphere(sphere)
    assert not BoundingBox3d(DVector3Array(
        DVector3(0, 1.1, 0))
    ).intersects_sphere(sphere)
    assert not BoundingBox3d(DVector3Array(
        DVector3(0, 0, -1.1))
    ).intersects_sphere(sphere)
    assert not BoundingBox3d(DVector3Array(
        DVector3(0, 0, 1.1))
    ).intersects_sphere(sphere)


def test_intersects_bounding_box_3d() -> None:
    bb = BoundingBox3d(DVector3Array(DVector3(0, 0, 0), DVector3(1, 1, 1)))

    assert bb.intersects_bounding_box_3d_exclusive(bb)
    assert bb.intersects_bounding_box_3d_inclusive(bb)

    assert not BoundingBox3d(DVector3Array(
        DVector3(-1, 0, 0), DVector3(0, 1, 1)
    )).intersects_bounding_box_3d_exclusive(bb)
    assert BoundingBox3d(DVector3Array(
        DVector3(-1, 0, 0), DVector3(0, 1, 1)
    )).intersects_bounding_box_3d_inclusive(bb)

    assert not BoundingBox3d(DVector3Array(
        DVector3(0, -1, 0), DVector3(1, 0, 1)
    )).intersects_bounding_box_3d_exclusive(bb)
    assert BoundingBox3d(DVector3Array(
        DVector3(0, -1, 0), DVector3(1, 0, 1)
    )).intersects_bounding_box_3d_inclusive(bb)

    assert not BoundingBox3d(DVector3Array(
        DVector3(0, 0, -1), DVector3(1, 1, 0)
    )).intersects_bounding_box_3d_exclusive(bb)
    assert BoundingBox3d(DVector3Array(
        DVector3(0, 0, -1), DVector3(1, 1, 0)
    )).intersects_bounding_box_3d_inclusive(bb)

    assert not BoundingBox3d(DVector3Array(
        DVector3(2, 2, 2), DVector3(3, 3, 3)
    )).intersects_bounding_box_3d_exclusive(bb)
    assert not BoundingBox3d(DVector3Array(
        DVector3(2, 2, 2), DVector3(3, 3, 3)
    )).intersects_bounding_box_3d_inclusive(bb)
