
# gamut
from gamut.geometry import Plane, Quad3d, Shape3dCullable, ViewFrustum3d
from gamut.math import (DMatrix4, DVector2, DVector3, DVector3Array, DVector4,
                        FMatrix4, FVector3, FVector3Array)
# python
from math import radians
from typing import Any
# pytest
import pytest


def test_cullable() -> None:
    assert isinstance(
        Quad3d(DVector3(0), DVector3(0), DVector3(0), DVector3(0)),
        Shape3dCullable
    )


def test_hash() -> None:
    q1 = Quad3d(
        DVector3(0, 1, 2),
        DVector3(3, 4, 5),
        DVector3(6, 7, 8),
        DVector3(9, 10, 11)
    )
    q2 = Quad3d(
        DVector3(0, 1, 2),
        DVector3(3, 4, 5),
        DVector3(6, 7, 8),
        DVector3(9, 10, 11)
    )
    assert hash(q1) == hash(q2)
    q3 = Quad3d(
        DVector3(1, 1, 2),
        DVector3(3, 4, 5),
        DVector3(6, 7, 8),
        DVector3(9, 10, 11)
    )
    assert hash(q1) != hash(q3)


def test_repr() -> None:
    quad = Quad3d(
        DVector3(0, 1, 2),
        DVector3(3, 4, 5),
        DVector3(6, 7, 8),
        DVector3(9, 10, 11)
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

@pytest.mark.parametrize("point", [None, '123', 123, DVector4(1), DVector2(1)])
@pytest.mark.parametrize("point_index", range(4))
def test_invalid_point(point: Any, point_index: int) -> None:
    points = [DVector3(0), DVector3(0), DVector3(0), DVector3(0)]
    points[point_index] = point
    with pytest.raises(TypeError) as excinfo:
        Quad3d(*points)
    assert str(excinfo.value) == (
        f'invalid type {point!r}, expected {DVector3!r}'
    )


@pytest.mark.parametrize("expected_points", [
    FVector3Array(
        FVector3(0, 1, 2),
        FVector3(3, 4, 5),
        FVector3(6, 7, 8),
        FVector3(9, 10, 11)
    ),
    DVector3Array(
        DVector3(0, 1, 2),
        DVector3(3, 4, 5),
        DVector3(6, 7, 8),
        DVector3(9, 10, 11)
    )
])
def test_points(expected_points: Any) -> None:
    quad = Quad3d(*expected_points)
    assert quad.points == expected_points


@pytest.mark.parametrize("quad", [
    Quad3d(DVector3(0), DVector3(0), DVector3(0), DVector3(0)),
    Quad3d(
        DVector3(0, 1, 2),
        DVector3(3, 4, 5),
        DVector3(6, 7, 8),
        DVector3(9, 10, 11)
    )
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
def test_d_transform(quad: Quad3d, transform: DMatrix4) -> None:
    new_quad = transform @ quad
    assert new_quad is not quad
    expected_points = DVector3Array(*(
        transform @ p
        for p in quad.points
    ))
    assert new_quad.points == expected_points


@pytest.mark.parametrize("quad", [
    Quad3d(FVector3(0), FVector3(0), FVector3(0), FVector3(0)),
    Quad3d(
        FVector3(0, 1, 2),
        FVector3(3, 4, 5),
        FVector3(6, 7, 8),
        FVector3(9, 10, 11)
    )
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
def test_f_transform(quad: Quad3d, transform: FMatrix4) -> None:
    new_quad = transform @ quad
    assert new_quad is not quad
    expected_points = FVector3Array(*(
        transform @ p
        for p in quad.points
    ))
    assert new_quad.points == expected_points


@pytest.mark.parametrize("transform", [None, 123, DVector4(1), DVector2(1)])
def test_transform_invalid(transform: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        transform @ Quad3d(DVector3(0), DVector3(0), DVector3(0), DVector3(0))
    assert str(excinfo.value).startswith('unsupported operand type(s) for @:')


def test_transform_wrong_type():
    with pytest.raises(TypeError) as excinfo:
        DMatrix4(1) @ Quad3d(
            FVector3(0), FVector3(0), FVector3(0), FVector3(0)
        )
    assert str(excinfo.value).startswith('unsupported operand type(s) for @:')

    with pytest.raises(TypeError) as excinfo:
        FMatrix4(1) @ Quad3d(
            DVector3(0), DVector3(0), DVector3(0), DVector3(0)
        )
    assert str(excinfo.value).startswith('unsupported operand type(s) for @:')


def test_equal() -> None:
    assert (
        Quad3d(FVector3(0), FVector3(0), FVector3(0), FVector3(0)) ==
        Quad3d(FVector3(0), FVector3(0), FVector3(0), FVector3(0))
    )
    assert (
        Quad3d(DVector3(0), DVector3(0), DVector3(0), DVector3(0)) !=
        Quad3d(FVector3(0), FVector3(0), FVector3(0), FVector3(0))
    )

    zero_quad = Quad3d(DVector3(0), DVector3(0), DVector3(0), DVector3(0))
    assert zero_quad == zero_quad
    assert zero_quad != Quad3d(
        DVector3(1), DVector3(0), DVector3(0), DVector3(0)
    )
    assert zero_quad != Quad3d(
        DVector3(0), DVector3(1), DVector3(0), DVector3(0)
    )
    assert zero_quad != Quad3d(
        DVector3(0), DVector3(0), DVector3(1), DVector3(0)
    )
    assert zero_quad != Quad3d(
        DVector3(0), DVector3(0), DVector3(0), DVector3(1)
    )
    assert zero_quad != object()


@pytest.mark.parametrize("vec_type", [FVector3, DVector3])
def test_seen_by(vec_type: Any) -> None:
    frustum = ViewFrustum3d(
        Plane(-1, vec_type(0, 0, 1)),
        Plane(10, vec_type(0, 0, -1)),
        Plane(5, vec_type(1, 0, 0)),
        Plane(5, vec_type(-1, 0, 0)),
        Plane(5, vec_type(0, 1, 0)),
        Plane(5, vec_type(0, -1, 0)),
    )

    # near
    assert not Quad3d(
        vec_type(0),
        vec_type(0),
        vec_type(0),
        vec_type(0)
    ).seen_by(frustum)
    assert Quad3d(
        vec_type(0, 0, 1),
        vec_type(0),
        vec_type(0),
        vec_type(0)
    ).seen_by(frustum)
    assert Quad3d(
        vec_type(0),
        vec_type(0, 0, 1),
        vec_type(0),
        vec_type(0)
    ).seen_by(frustum)
    assert Quad3d(
        vec_type(0),
        vec_type(0),
        vec_type(0, 0, 1),
        vec_type(0)
    ).seen_by(frustum)
    assert Quad3d(
        vec_type(0),
        vec_type(0),
        vec_type(0),
        vec_type(0, 0, 1)
    ).seen_by(frustum)
    # far
    assert not Quad3d(
        vec_type(0, 0, 11),
        vec_type(0, 0, 11),
        vec_type(0, 0, 11),
        vec_type(0, 0, 11)
    ).seen_by(frustum)
    assert Quad3d(
        vec_type(0, 0, 10),
        vec_type(0, 0, 11),
        vec_type(0, 0, 11),
        vec_type(0, 0, 11)
    ).seen_by(frustum)
    assert Quad3d(
        vec_type(0, 0, 11),
        vec_type(0, 0, 10),
        vec_type(0, 0, 11),
        vec_type(0, 0, 11)
    ).seen_by(frustum)
    assert Quad3d(
        vec_type(0, 0, 11),
        vec_type(0, 0, 11),
        vec_type(0, 0, 10),
        vec_type(0, 0, 11)
    ).seen_by(frustum)
    assert Quad3d(
        vec_type(0, 0, 11),
        vec_type(0, 0, 11),
        vec_type(0, 0, 11),
        vec_type(0, 0, 10)
    ).seen_by(frustum)
    # left
    assert not Quad3d(
        vec_type(-6, 0, 5),
        vec_type(-6, 0, 5),
        vec_type(-6, 0, 5),
        vec_type(-6, 0, 5)
    ).seen_by(frustum)
    assert Quad3d(
        vec_type(-5, 0, 5),
        vec_type(-6, 0, 5),
        vec_type(-6, 0, 5),
        vec_type(-6, 0, 5)
    ).seen_by(frustum)
    assert Quad3d(
        vec_type(-6, 0, 5),
        vec_type(-5, 0, 5),
        vec_type(-6, 0, 5),
        vec_type(-6, 0, 5)
    ).seen_by(frustum)
    assert Quad3d(
        vec_type(-6, 0, 5),
        vec_type(-6, 0, 5),
        vec_type(-5, 0, 5),
        vec_type(-6, 0, 5)
    ).seen_by(frustum)
    assert Quad3d(
        vec_type(-6, 0, 5),
        vec_type(-6, 0, 5),
        vec_type(-6, 0, 5),
        vec_type(-5, 0, 5)
    ).seen_by(frustum)
    # right
    assert not Quad3d(
        vec_type(6, 0, 5),
        vec_type(6, 0, 5),
        vec_type(6, 0, 5),
        vec_type(6, 0, 5)
    ).seen_by(frustum)
    assert Quad3d(
        vec_type(5, 0, 5),
        vec_type(6, 0, 5),
        vec_type(6, 0, 5),
        vec_type(6, 0, 5)
    ).seen_by(frustum)
    assert Quad3d(
        vec_type(6, 0, 5),
        vec_type(5, 0, 5),
        vec_type(6, 0, 5),
        vec_type(6, 0, 5)
    ).seen_by(frustum)
    assert Quad3d(
        vec_type(6, 0, 5),
        vec_type(6, 0, 5),
        vec_type(5, 0, 5),
        vec_type(6, 0, 5)
    ).seen_by(frustum)
    assert Quad3d(
        vec_type(6, 0, 5),
        vec_type(6, 0, 5),
        vec_type(6, 0, 5),
        vec_type(5, 0, 5)
    ).seen_by(frustum)
    # bottom
    assert not Quad3d(
        vec_type(0, -6, 5),
        vec_type(0, -6, 5),
        vec_type(0, -6, 5),
        vec_type(0, -6, 5)
    ).seen_by(frustum)
    assert Quad3d(
        vec_type(0, -5, 5),
        vec_type(0, -6, 5),
        vec_type(0, -6, 5),
        vec_type(0, -6, 5)
    ).seen_by(frustum)
    assert Quad3d(
        vec_type(0, -6, 5),
        vec_type(0, -5, 5),
        vec_type(0, -6, 5),
        vec_type(0, -6, 5)
    ).seen_by(frustum)
    assert Quad3d(
        vec_type(0, -6, 5),
        vec_type(0, -6, 5),
        vec_type(0, -5, 5),
        vec_type(0, -6, 5)
    ).seen_by(frustum)
    assert Quad3d(
        vec_type(0, -6, 5),
        vec_type(0, -6, 5),
        vec_type(0, -6, 5),
        vec_type(0, -5, 5)
    ).seen_by(frustum)
    # top
    assert not Quad3d(
        vec_type(0, 6, 5),
        vec_type(0, 6, 5),
        vec_type(0, 6, 5),
        vec_type(0, 6, 5)
    ).seen_by(frustum)
    assert Quad3d(
        vec_type(0, 5, 5),
        vec_type(0, 6, 5),
        vec_type(0, 6, 5),
        vec_type(0, 6, 5)
    ).seen_by(frustum)
    assert Quad3d(
        vec_type(0, 6, 5),
        vec_type(0, 5, 5),
        vec_type(0, 6, 5),
        vec_type(0, 6, 5)
    ).seen_by(frustum)
    assert Quad3d(
        vec_type(0, 6, 5),
        vec_type(0, 6, 5),
        vec_type(0, 5, 5),
        vec_type(0, 6, 5)
    ).seen_by(frustum)
    assert Quad3d(
        vec_type(0, 6, 5),
        vec_type(0, 6, 5),
        vec_type(0, 6, 5),
        vec_type(0, 5, 5)
    ).seen_by(frustum)
