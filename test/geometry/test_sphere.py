
# gamut
from gamut.geometry import (DegenerateGeometryError, Plane, Shape3dCullable,
                            Shape3dPointContainer, Sphere, ViewFrustum3d)
from gamut.math import (DMatrix4, DVector2, DVector3, DVector4, FMatrix4,
                        FVector3)
# python
from math import pi, radians
from typing import Any
# pytest
import pytest


def test_cullable() -> None:
    assert isinstance(Sphere(DVector3(0), 1), Shape3dCullable)


def test_point_container() -> None:
    assert isinstance(Sphere(DVector3(0), 1), Shape3dPointContainer)


def test_sphere() -> None:
    s1 = Sphere(DVector3(1, 2, 3), 4)
    s2 = Sphere(DVector3(1, 2, 3), 4)
    assert hash(s1) == hash(s2)
    s3 = Sphere(FVector3(1, 2, 3), 4)
    assert hash(s1) != hash(s3)


def test_repr() -> None:
    sphere = Sphere(DVector3(1, 2, 3), 4)
    assert (
        repr(sphere) ==
        f'<gamut.geometry.Sphere center=(1.0, 2.0, 3.0) radius=4.0>'
    )


@pytest.mark.parametrize("radius", [None, 'x', object()])
def test_invalid_radius(radius: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Sphere(DVector3(0), radius)
    assert str(excinfo.value) == 'radius must be float'


@pytest.mark.parametrize("center", [
    None,
    '123',
    123,
    DVector4(1),
    DVector2(1)
])
def test_invalid_center(center: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Sphere(center, 1)
    assert str(excinfo.value) == 'center must be FVector3 or DVector3'


@pytest.mark.parametrize("radius", [-1, 1, -1.5, 1.5, '-2.0', '2.0'])
def test_radius(radius: Any) -> None:
    sphere = Sphere(DVector3(0), radius)
    assert sphere.radius == abs(float(radius))


@pytest.mark.parametrize("center", [
    FVector3(1),
    FVector3(1, 2, 3),
    DVector3(1),
    DVector3(1, 2, 3),
])
def test_center(center: Any) -> None:
    sphere = Sphere(center, 1)
    assert sphere.center == center


@pytest.mark.parametrize("vtype", [FVector3, DVector3])
def test_degenerate(vtype: type[FVector3] | type[DVector3]) -> None:
    with pytest.raises(Sphere.DegenerateError) as excinfo:
        Sphere(vtype(1, 2, 3), 0)
    assert str(excinfo.value) == 'degenerate sphere'
    assert excinfo.value.degenerate_form == vtype(1, 2, 3)


def test_degenerate_error():
    assert issubclass(Sphere.DegenerateError, DegenerateGeometryError)


@pytest.mark.parametrize("sphere", [
    Sphere(DVector3(0, 0, 0), 1),
    Sphere(DVector3(1, 1, 1), 2),
    Sphere(DVector3(0, .5, 1), 99),
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
def test_d_transform(sphere: Sphere, transform: DMatrix4) -> None:
    new_sphere = transform @ sphere
    assert new_sphere is not sphere

    expected_center = transform @ sphere.center
    expected_radius = (
        sphere.radius *
        max(DVector3(*(c.xyz.magnitude for c in (
            transform[0],
            transform[1],
            transform[2],
        ))))
    )

    assert new_sphere.center == expected_center
    assert new_sphere.radius == expected_radius


@pytest.mark.parametrize("sphere", [
    Sphere(FVector3(0, 0, 0), 1),
    Sphere(FVector3(1, 1, 1), 2),
    Sphere(FVector3(0, .5, 1), 99),
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
def test_f_transform(sphere: Sphere, transform: FMatrix4) -> None:
    new_sphere = transform @ sphere
    assert new_sphere is not sphere

    expected_center = transform @ sphere.center
    expected_radius = (
        sphere.radius *
        max(FVector3(*(c.xyz.magnitude for c in (
            transform[0],
            transform[1],
            transform[2],
        ))))
    )

    assert new_sphere.center == expected_center
    assert new_sphere.radius == expected_radius


@pytest.mark.parametrize("transform", [None, 123, DVector4(1), DVector2(1)])
def test_transform_invalid(transform: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        transform @ Sphere(DVector3(0, 1, 0), 1)
    assert str(excinfo.value).startswith('unsupported operand type(s) for @:')


def test_transform_wrong_type():
    with pytest.raises(TypeError) as excinfo:
        DMatrix4(1) @ Sphere(FVector3(0), 1)
    assert str(excinfo.value).startswith('unsupported operand type(s) for @:')

    with pytest.raises(TypeError) as excinfo:
        FMatrix4(1) @ Sphere(DVector3(0), 1)
    assert str(excinfo.value).startswith('unsupported operand type(s) for @:')


def test_equal() -> None:
    assert Sphere(DVector3(0), 1) == Sphere(DVector3(0), 1)
    assert Sphere(FVector3(0), 1) == Sphere(FVector3(0), 1)
    assert Sphere(FVector3(0), 1) != Sphere(DVector3(0), 1)
    assert Sphere(DVector3(0), 1) != Sphere(DVector3(1, 0, 0), 1)
    assert Sphere(DVector3(0), 1) != Sphere(DVector3(0, 1, 0), 1)
    assert Sphere(DVector3(0), 1) != Sphere(DVector3(0, 0, 1), 1)
    assert Sphere(DVector3(0), 1) != Sphere(DVector3(0), 2)
    assert Sphere(DVector3(0), 1) != object()


@pytest.mark.parametrize("sphere", [
    Sphere(DVector3(0), 1),
    Sphere(DVector3(0), 10),
    Sphere(DVector3(1, 2, 3), 5),
])
def test_d_contains_point(sphere: Sphere) -> None:
    assert sphere.contains_point(sphere.center)

    for rc in (0.1, 0.5, 0.9, 1.0):
        r = sphere.radius * rc
        base_point = DVector3(r, 0, 0)
        for angle in (0.0, pi * .5, pi, pi * .75):
            for axis in (
                DVector3(1, 0, 0),
                DVector3(0, 1, 0),
                DVector3(0, 0, 1)
            ):
                check_point = sphere.center + (
                    DMatrix4(1).rotate(angle, axis) @ base_point
                )
                assert sphere.contains_point(check_point)

    for r_plus in (.1, 2.0, 100.0):
        r = sphere.radius + r_plus
        base_point = DVector3(r, 0, 0)
        for angle in (0.0, pi * .5, pi, pi * .75):
            for axis in (
                DVector3(1, 0, 0),
                DVector3(0, 1, 0),
                DVector3(0, 0, 1)
            ):
                check_point = sphere.center + (
                    DMatrix4(1).rotate(angle, axis) @ base_point
                )
                assert not sphere.contains_point(check_point)


@pytest.mark.parametrize("sphere", [
    Sphere(FVector3(0), 1),
    Sphere(FVector3(0), 10),
    Sphere(FVector3(1, 2, 3), 5),
])
def test_f_contains_point(sphere: Sphere) -> None:
    assert sphere.contains_point(sphere.center)

    for rc in (0.1, 0.5, 0.9, 1.0):
        r = sphere.radius * rc
        base_point = FVector3(r, 0, 0)
        for angle in (0.0, pi * .5, pi, pi * .75):
            for axis in (
                FVector3(1, 0, 0),
                FVector3(0, 1, 0),
                FVector3(0, 0, 1)
            ):
                check_point = sphere.center + (
                    FMatrix4(1).rotate(angle, axis) @ base_point
                )
                assert sphere.contains_point(check_point)

    for r_plus in (.1, 2.0, 100.0):
        r = sphere.radius + r_plus
        base_point = FVector3(r, 0, 0)
        for angle in (0.0, pi * .5, pi, pi * .75):
            for axis in (
                FVector3(1, 0, 0),
                FVector3(0, 1, 0),
                FVector3(0, 0, 1)
            ):
                check_point = sphere.center + (
                    FMatrix4(1).rotate(angle, axis) @ base_point
                )
                assert not sphere.contains_point(check_point)


def test_contains_point_wrong_type() -> None:
    with pytest.raises(TypeError) as ex:
        Sphere(FVector3(0), 1).contains_point(DVector3(0))
    assert str(ex.value) == 'point must be FVector3'

    with pytest.raises(TypeError) as ex:
        Sphere(DVector3(0), 1).contains_point(FVector3(0))
    assert str(ex.value) == 'point must be DVector3'


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
    assert not Sphere(vec_type(0), .01).seen_by(frustum)
    assert Sphere(vec_type(0), 1).seen_by(frustum)
    assert Sphere(vec_type(0, 0, 1), .01).seen_by(frustum)
    # far
    assert not Sphere(vec_type(0, 0, 11), .01).seen_by(frustum)
    assert Sphere(vec_type(0, 0, 11), 1).seen_by(frustum)
    assert Sphere(vec_type(0, 0, 10), .01).seen_by(frustum)
    # left
    assert not Sphere(vec_type(-6, 0, 5), .01).seen_by(frustum)
    assert Sphere(vec_type(-6, 0, 5), 1).seen_by(frustum)
    assert Sphere(vec_type(-5, 0, 5), .01).seen_by(frustum)
    # right
    assert not Sphere(vec_type(6, 0, 5), .01).seen_by(frustum)
    assert Sphere(vec_type(6, 0, 5), 1).seen_by(frustum)
    assert Sphere(vec_type(5, 0, 5), .01).seen_by(frustum)
    # bottom
    assert not Sphere(vec_type(0, -6, 5), .01).seen_by(frustum)
    assert Sphere(vec_type(0, -6, 5), 1).seen_by(frustum)
    assert Sphere(vec_type(0, -5, 5), .01).seen_by(frustum)
    # top
    assert not Sphere(vec_type(0, 6, 5), .01).seen_by(frustum)
    assert Sphere(vec_type(0, 6, 5), 1).seen_by(frustum)
    assert Sphere(vec_type(0, 5, 5), .01).seen_by(frustum)
