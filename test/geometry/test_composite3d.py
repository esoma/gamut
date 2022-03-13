
# gamut
from gamut.geometry import (Composite3d, Plane, Shape3dCullable,
                            Shape3dPointContainer, Sphere, ViewFrustum3d)
from gamut.math import Matrix4, Vector2, Vector3, Vector4
# python
from math import radians
from typing import Any
# pytest
import pytest


def test_hash() -> None:
    c1 = Composite3d()
    c2 = Composite3d()
    assert hash(c1) != hash(c2)


def test_cullable() -> None:
    assert isinstance(Composite3d(), Shape3dCullable)


def test_point_container() -> None:
    assert isinstance(Composite3d(), Shape3dPointContainer)


@pytest.mark.parametrize("shapes", [
    [],
    [None, 1],
])
def test_repr(shapes: Any) -> None:
    composite = Composite3d(*shapes)
    shape_reprs = ', '.join(repr(s) for s in shapes)
    assert (
        repr(composite) ==
        f'<gamut.geometry.Composite3d ({shape_reprs})>'
    )


@pytest.mark.parametrize("shapes", [
    [],
    [None, 1],
])
def test_shapes(shapes: Any) -> None:
    composite = Composite3d(*shapes)
    assert composite.shapes == tuple(shapes)
    assert all(
        actual is expected
        for actual, expected in zip(composite.shapes, shapes)
    )


def test_shapes_flattened():
    composite = Composite3d(
        1, 2, 3,
        Composite3d(4, 5, 6),
        7, 8, 9
    )
    assert tuple(composite.shapes_flattened) == (1, 2, 3, 4, 5, 6, 7, 8, 9)


@pytest.mark.parametrize("composite", [
    Composite3d(),
    Composite3d(Sphere(Vector3(0), 0), Sphere(Vector3(0), 0)),
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
def test_transform(composite: Composite3d, transform: Matrix4) -> None:
    new_composite = transform @ composite
    assert new_composite is not composite

    transformed_shapes = tuple(transform @ s for s in composite.shapes)

    assert new_composite.shapes == transformed_shapes


def test_transform_shape_not_implemented() -> None:
    composite = Composite3d(None)
    with pytest.raises(TypeError) as excinfo:
        Matrix4(1) @ composite
    assert str(excinfo.value).startswith('unsupported operand type(s) for @:')


@pytest.mark.parametrize("transform", [None, 123, Vector4(1), Vector2(1)])
def test_transform_invalid(transform: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        transform @ Composite3d()
    assert str(excinfo.value).startswith('unsupported operand type(s) for @:')


def test_equal() -> None:
    assert Composite3d() == Composite3d()
    assert Composite3d(1) == Composite3d(1)
    assert Composite3d(1, None, '123') == Composite3d(1, None, '123')
    assert Composite3d(1, None, '123') == Composite3d(None, '123', 1)
    assert Composite3d(1, None, '123') == Composite3d(None, 1, '123')
    assert Composite3d(1, None, '123') == Composite3d('123', None, 1)
    assert Composite3d(1, None, '123', 1) == Composite3d('123', None, 1, 1)
    assert Composite3d(1, None, '123', 1) != Composite3d('123', None, 1)
    assert Composite3d(1, None, '123') != Composite3d('123', None, 1, 1)
    assert Composite3d() != object()


def test_contains_point() -> None:
    class Contains123:
        def contains_point(self, point):
            return point == Vector3(1, 2, 3)

    assert not Composite3d().contains_point(Vector3(0))
    assert not Composite3d().contains_point(Vector3(1, 2, 3))
    assert not Composite3d(None).contains_point(Vector3(0))
    assert not Composite3d(None).contains_point(Vector3(1, 2, 3))
    assert not Composite3d(Contains123()).contains_point(Vector3(0))
    assert Composite3d(Contains123()).contains_point(Vector3(1, 2, 3))
    assert Composite3d(None, Contains123()).contains_point(Vector3(1, 2, 3))


def test_seen_by() -> None:
    frustum_a = ViewFrustum3d(
        Plane(-1, Vector3(0, 0, 1)),
        Plane(10, Vector3(0, 0, -1)),
        Plane(5, Vector3(1, 0, 0)),
        Plane(5, Vector3(-1, 0, 0)),
        Plane(5, Vector3(0, 1, 0)),
        Plane(5, Vector3(0, -1, 0)),
    )

    frustum_b = ViewFrustum3d(
        Plane(-1, Vector3(0, 0, 1)),
        Plane(10, Vector3(0, 0, -1)),
        Plane(5, Vector3(1, 0, 0)),
        Plane(5, Vector3(-1, 0, 0)),
        Plane(5, Vector3(0, 1, 0)),
        Plane(5, Vector3(0, -1, 0)),
    )

    class SeenByFrustumA:
        def seen_by(self, view_frustum):
            return view_frustum is frustum_a

    assert not Composite3d().seen_by(frustum_a)
    assert not Composite3d().seen_by(frustum_b)
    assert not Composite3d(None).seen_by(frustum_a)
    assert not Composite3d(None).seen_by(frustum_b)
    assert Composite3d(SeenByFrustumA()).seen_by(frustum_a)
    assert not Composite3d(SeenByFrustumA()).seen_by(frustum_b)
    assert Composite3d(None, SeenByFrustumA()).seen_by(frustum_a)
    assert not Composite3d(None, SeenByFrustumA()).seen_by(frustum_b)
