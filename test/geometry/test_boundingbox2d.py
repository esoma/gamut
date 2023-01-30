
# gamut
from gamut.geometry import BoundingBox2d
from gamut.math import (DVector2, DVector2Array, DVector4, FVector2,
                        FVector2Array)
# python
from typing import Any
# pytest
import pytest


def test_hash() -> None:
    bb1 = BoundingBox2d(FVector2Array(FVector2(1, 2), FVector2(4, 5)))
    bb2 = BoundingBox2d(FVector2Array(FVector2(1, 2), FVector2(4, 5)))
    assert hash(bb1) == hash(bb2)
    bb3 = BoundingBox2d(DVector2Array(DVector2(1, 2), DVector2(4, 5)))
    assert hash(bb1) != hash(bb3)


@pytest.mark.parametrize("bounding_box", [
    BoundingBox2d(FVector2Array(FVector2(1, 2), FVector2(4, 5))),
    BoundingBox2d(DVector2Array(DVector2(1, 2), DVector2(4, 5)))
])
def test_repr(bounding_box: BoundingBox2d) -> None:
    assert (
        repr(bounding_box) ==
        f'<gamut.geometry.BoundingBox2d '
        f'min=(1.0, 2.0) '
        f'max=(4.0, 5.0)>'
    )


@pytest.mark.parametrize("points", [FVector2Array(), DVector2Array()])
def test_no_points(points: Any) -> None:
    with pytest.raises(ValueError) as excinfo:
        BoundingBox2d(points)
    assert str(excinfo.value) == 'must have at least 1 point'


@pytest.mark.parametrize("points", [
    [DVector2(1)],
    [1],
    ['123'],
    [DVector2(1)],
    [DVector4(1)],
])
def test_points_invalid_type(points: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        BoundingBox2d(points)
    assert str(excinfo.value) == (
        'points must be FVector2Array or DVector2Array'
    )


@pytest.mark.parametrize("points", [
    FVector2Array(FVector2(0)),
    FVector2Array(FVector2(0), FVector2(1)),
    FVector2Array(FVector2(0), FVector2(1, 3)),
    FVector2Array(FVector2(0), FVector2(1, 3), FVector2(-1, -3)),
    FVector2Array(
        FVector2(-1, -3),
        FVector2(-4, 0),
        FVector2(-3, -2),
        FVector2(1, 4)
    ),
    DVector2Array(DVector2(0)),
    DVector2Array(DVector2(0), DVector2(1)),
    DVector2Array(DVector2(0), DVector2(1, 3)),
    DVector2Array(DVector2(0), DVector2(1, 3), DVector2(-1, -3)),
    DVector2Array(
        DVector2(-1, -3),
        DVector2(-4, 0),
        DVector2(2, -3),
        DVector2(0, 4)
    ),
])
def test_min_max_center(points: Any) -> None:
    bb = BoundingBox2d(points)

    if len(points) > 1:
        expected_min = points.get_component_type()(
            min(*(p.x for p in points)),
            min(*(p.y for p in points)),
        )
        expected_max = points.get_component_type()(
            max(*(p.x for p in points)),
            max(*(p.y for p in points)),
        )
    else:
        expected_min = points[0]
        expected_max = points[0]

    assert bb.min == expected_min
    assert bb.max == expected_max
    assert bb.center == (expected_min + expected_max) * .5


@pytest.mark.parametrize("points", [
    FVector2Array(FVector2(0)),
    FVector2Array(FVector2(-1, -3), FVector2(1, 3)),
    DVector2Array(DVector2(0)),
    DVector2Array(DVector2(-1, -3), DVector2(1, 3)),
])
def test_corners(points: Any) -> None:
    bb = BoundingBox2d(points)
    expected_points = tuple(
        points.get_component_type()(x, y)
        for x in (bb.min.x, bb.max.x)
        for y in (bb.min.y, bb.max.y)
    )
    assert bb.corners == expected_points


@pytest.mark.parametrize("array_type", [FVector2Array, DVector2Array])
def test_equal(array_type: Any) -> None:
    v_type = array_type.get_component_type()
    assert BoundingBox2d(array_type((v_type(0)))) == (
        BoundingBox2d(array_type((v_type(0))))
    )
    assert (
        BoundingBox2d(array_type(v_type(1, 3), v_type(-1, -3))) ==
        BoundingBox2d(array_type(v_type(1, 3), v_type(-1, -3)))
    )
    assert (
        BoundingBox2d(array_type(v_type(1, 3), v_type(-1, -3))) !=
        BoundingBox2d(array_type(v_type(0, 3), v_type(-1, -3)))
    )
    assert (
        BoundingBox2d(array_type(v_type(1, 3), v_type(-1, -3))) !=
        BoundingBox2d(array_type(v_type(1, 0), v_type(-1, -3)))
    )
    assert (
        BoundingBox2d(array_type(v_type(1, 3), v_type(-1, -3))) !=
        BoundingBox2d(array_type(v_type(1, 3), v_type(0, -3)))
    )
    assert (
        BoundingBox2d(array_type(v_type(1, 3), v_type(-1, -3))) !=
        BoundingBox2d(array_type(v_type(1, 3), v_type(-1, 0)))
    )
    assert BoundingBox2d(array_type(v_type(0))) != object()


@pytest.mark.parametrize("bounding_box", [
    BoundingBox2d(FVector2Array(FVector2(0))),
    BoundingBox2d(FVector2Array(FVector2(-1, -1), FVector2(1, 1))),
    BoundingBox2d(FVector2Array(
        FVector2(-1000, 67),
        FVector2(-56, 87))
    ),
])
def test_f_contains_point(bounding_box: BoundingBox2d) -> None:
    assert bounding_box.contains_point(bounding_box.center)
    for corner in bounding_box.corners:
        assert bounding_box.contains_point(corner)

    for offset in (
        FVector2(1, -1),
        FVector2(-1, 1),
        FVector2(1, 1)
    ):
        assert not bounding_box.contains_point(bounding_box.min - offset)
        assert not bounding_box.contains_point(bounding_box.max + offset)


@pytest.mark.parametrize("bounding_box", [
    BoundingBox2d(DVector2Array(DVector2(0))),
    BoundingBox2d(DVector2Array(DVector2(-1, -1), DVector2(1, 1))),
    BoundingBox2d(DVector2Array(
        DVector2(-1000, 67),
        DVector2(-56, 87))
    ),
])
def test_d_contains_point(bounding_box: BoundingBox2d) -> None:
    assert bounding_box.contains_point(bounding_box.center)
    for corner in bounding_box.corners:
        assert bounding_box.contains_point(corner)

    for offset in (
        DVector2(1, -1,),
        DVector2(-1, 1),
        DVector2(1, 1),
    ):
        assert not bounding_box.contains_point(bounding_box.min - offset)
        assert not bounding_box.contains_point(bounding_box.max + offset)


def test_contains_point_wrong_type():
    with pytest.raises(TypeError) as excinfo:
        BoundingBox2d(FVector2Array(FVector2(0))).contains_point(DVector2(0))
    assert str(excinfo.value).startswith('point must be FVector2')

    with pytest.raises(TypeError) as excinfo:
        BoundingBox2d(DVector2Array(DVector2(0))).contains_point(FVector2(0))
    assert str(excinfo.value).startswith('point must be DVector2')


def test_intersects_bounding_box_2d() -> None:
    bb = BoundingBox2d(DVector2Array(DVector2(0, 0), DVector2(1, 1)))

    assert bb.intersects_bounding_box_2d(bb)
    assert bb.intersects_bounding_box_2d(
        BoundingBox2d(DVector2Array(DVector2(.5, .5)))
    )

    assert BoundingBox2d(DVector2Array(
        DVector2(-1, 0), DVector2(0, 1)
    )).intersects_bounding_box_2d(bb)

    assert BoundingBox2d(DVector2Array(
        DVector2(0, -1), DVector2(1, 0)
    )).intersects_bounding_box_2d(bb)

    assert not BoundingBox2d(DVector2Array(
        DVector2(2, 2), DVector2(3, 3)
    )).intersects_bounding_box_2d(bb)

    assert not BoundingBox2d(DVector2Array(
        DVector2(.5, -2), DVector2(.5, -1)
    )).intersects_bounding_box_2d(bb)

    assert BoundingBox2d(DVector2Array(
        DVector2(.5, -2), DVector2(.5, -1)
    )).intersects_bounding_box_2d(bb, tolerance=1)

    assert not BoundingBox2d(DVector2Array(
        DVector2(.5, 3), DVector2(.5, 2)
    )).intersects_bounding_box_2d(bb)

    assert BoundingBox2d(DVector2Array(
        DVector2(.5, 3), DVector2(.5, 2)
    )).intersects_bounding_box_2d(bb, tolerance=1)

    assert not BoundingBox2d(DVector2Array(
        DVector2(-1, .5), DVector2(-2, .5)
    )).intersects_bounding_box_2d(bb)

    assert BoundingBox2d(DVector2Array(
        DVector2(-1, .5), DVector2(-2, .5)
    )).intersects_bounding_box_2d(bb, tolerance=1)

    assert not BoundingBox2d(DVector2Array(
        DVector2(2, .5), DVector2(3, .5)
    )).intersects_bounding_box_2d(bb)

    assert BoundingBox2d(DVector2Array(
        DVector2(2, .5), DVector2(3, .5)
    )).intersects_bounding_box_2d(bb, tolerance=1)
