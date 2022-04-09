
# gamut
from gamut.geometry import ConvexHull
from gamut.math import (DMatrix4, DVector2, DVector3, DVector3Array, DVector4,
                        FMatrix4, FVector3, FVector3Array)
# python
from math import radians
from typing import Any
# pytest
import pytest


def test_hash() -> None:
    c1 = ConvexHull(DVector3Array(DVector3(1, 2, 3)))
    c2 = ConvexHull(DVector3Array(DVector3(1, 2, 3)))
    assert hash(c1) == hash(c2)
    c3 = ConvexHull(DVector3Array(DVector3(3, 2, 1)))
    assert hash(c1) != hash(c3)


def test_repr() -> None:
    c = ConvexHull(DVector3Array(DVector3(1, 2, 3)))
    assert repr(c) == '<gamut.geometry.ConvexHull>'


def test_no_points() -> None:
    with pytest.raises(ValueError) as excinfo:
        ConvexHull(DVector3Array())
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
        ConvexHull(points)
    assert str(excinfo.value) == (
        'points must be FVector3Array or DVector3Array'
    )


@pytest.mark.parametrize("points", [
    FVector3Array(FVector3(0), FVector3(1), FVector3(2)),
    FVector3Array(FVector3(0)),
    FVector3Array(FVector3(1, 2, 3), FVector3(4, 5, 6)),
    DVector3Array(DVector3(0), DVector3(1), DVector3(2)),
    DVector3Array(DVector3(0)),
    DVector3Array(DVector3(1, 2, 3), DVector3(4, 5, 6)),
])
def test_points(points: Any) -> None:
    c = ConvexHull(points)
    assert c.points == points


@pytest.mark.parametrize("convex_hull", [
    ConvexHull(DVector3Array(DVector3(0, 0, 0), DVector3(0, 0, 0))),
    ConvexHull(DVector3Array(DVector3(-1, -2, -3), DVector3(1, 2, 3))),
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
def test_d_transform(convex_hull: ConvexHull, transform: DMatrix4) -> None:
    new_ch = transform @ convex_hull
    assert new_ch is not convex_hull
    assert new_ch.points == DVector3Array(
        *(transform @ p for p in convex_hull.points)
    )


@pytest.mark.parametrize("convex_hull", [
    ConvexHull(FVector3Array(FVector3(0, 0, 0), FVector3(0, 0, 0))),
    ConvexHull(FVector3Array(FVector3(-1, -2, -3), FVector3(1, 2, 3))),
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
def test_d_transform(convex_hull: ConvexHull, transform: FMatrix4) -> None:
    new_ch = transform @ convex_hull
    assert new_ch is not convex_hull
    assert new_ch.points == FVector3Array(
        *(transform @ p for p in convex_hull.points)
    )


def test_transform_wrong_type():
    with pytest.raises(TypeError) as excinfo:
        DMatrix4(1) @ ConvexHull(
            FVector3Array(FVector3(0, 0, 0), FVector3(0, 0, 0))
        )
    assert str(excinfo.value).startswith('unsupported operand type(s) for @:')

    with pytest.raises(TypeError) as excinfo:
        FMatrix4(1) @ ConvexHull(
            DVector3Array(DVector3(0, 0, 0), DVector3(0, 0, 0))
        )
    assert str(excinfo.value).startswith('unsupported operand type(s) for @:')


@pytest.mark.parametrize("left_side", [None, 1, '123'])
def test_invalid_multiply(left_side: Any) -> None:
    with pytest.raises(TypeError):
        left_side @ ConvexHull(
            DVector3Array(DVector3(0, 0, 0), DVector3(0, 0, 0))
        )

def test_equal() -> None:
    assert (
        ConvexHull(FVector3Array(FVector3(0, 0, 0), FVector3(0, 0, 0))) ==
        ConvexHull(FVector3Array(FVector3(0, 0, 0), FVector3(0, 0, 0)))
    )
    assert (
        ConvexHull(DVector3Array(DVector3(0, 0, 0), DVector3(0, 0, 0))) !=
        ConvexHull(FVector3Array(FVector3(0, 0, 0), FVector3(0, 0, 0)))
    )
    c = ConvexHull(DVector3Array(DVector3(0, 0, 0), DVector3(0, 0, 0)))
    assert c == ConvexHull(DVector3Array(DVector3(0, 0, 0), DVector3(0, 0, 0)))
    assert c != ConvexHull(DVector3Array(DVector3(1, 0, 0), DVector3(0, 0, 0)))
    assert c != ConvexHull(DVector3Array(DVector3(0, 1, 0), DVector3(0, 0, 0)))
    assert c != ConvexHull(DVector3Array(DVector3(0, 0, 1), DVector3(0, 0, 0)))
    assert c != ConvexHull(DVector3Array(DVector3(0, 0, 0), DVector3(1, 0, 0)))
    assert c != ConvexHull(DVector3Array(DVector3(0, 0, 0), DVector3(0, 1, 0)))
    assert c != ConvexHull(DVector3Array(DVector3(0, 0, 0), DVector3(0, 0, 1)))
    assert c != object()
