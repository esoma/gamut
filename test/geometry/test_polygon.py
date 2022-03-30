
# gamut
from gamut.geometry import Mesh2d, Polygon
from gamut.math import Vector2, Vector2Array, Vector4
# python
from typing import Any
# pytest
import pytest


def test_hash() -> None:
    exterior = Vector2Array()
    p1 = Polygon(exterior)
    p2 = Polygon(exterior)
    assert hash(p1) != hash(p2)


def test_repr() -> None:
    p = Polygon(Vector2Array())
    assert repr(p) == '<gamut.geometry.Polygon>'


@pytest.mark.parametrize("exterior", [
    [None],
    [1],
    ['123'],
    [Vector2(1)],
    [Vector4(1)],
])
def test_exterior_invalid_type(exterior: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Polygon(exterior)
    assert str(excinfo.value) == 'exterior must be Vector2Array'


@pytest.mark.parametrize("holes", [object(), 1])
def test_holes_not_iterable(holes: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Polygon(Vector2Array(), holes=holes)


@pytest.mark.parametrize("holes", [
    [None],
    [Vector2Array(), None],
])
def test_holes_invalid_type(holes: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Polygon(Vector2Array(), holes=holes)
    assert str(excinfo.value) == 'each hole must be Vector2Array'


@pytest.mark.parametrize("exterior", [
    Vector2Array(Vector2(0, 1), Vector2(3, 4)),
    Vector2Array(Vector2(0), Vector2(1), Vector2(2)),
])
def test_exterior(exterior: Any) -> None:
    p = Polygon(exterior)
    assert p.exterior == exterior


@pytest.mark.parametrize("holes", [
    [Vector2Array(Vector2(0, 1), Vector2(3, 4))],
    [Vector2Array(Vector2(0), Vector2(1), Vector2(2))],
    [
        Vector2Array(Vector2(0, 1), Vector2(3, 4)),
        Vector2Array(Vector2(0), Vector2(1), Vector2(2)),
    ],
])
def test_holes(holes: Any) -> None:
    p = Polygon(Vector2Array(), holes=holes)
    assert isinstance(p.holes, tuple)
    assert p.holes == tuple(holes)


def test_triangulate() -> None:
    p = Polygon(
        Vector2Array(
            Vector2(0, 0),
            Vector2(100, 0),
            Vector2(100, 100),
            Vector2(0, 100)
        ),
        holes=[
            Vector2Array(
                Vector2(25, 25),
                Vector2(75, 25),
                Vector2(75, 75),
                Vector2(25, 75)
            )
        ]
    )
    mesh = p.triangulate()
    assert isinstance(mesh, Mesh2d)
    assert set(mesh.positions) == {
        Vector2(0, 0),
        Vector2(100, 0),
        Vector2(100, 100),
        Vector2(0, 100),
        Vector2(25, 25),
        Vector2(75, 25),
        Vector2(75, 75),
        Vector2(25, 75)
    }
    assert set(
        tuple(sorted(
            (mesh.positions[i.x], mesh.positions[i.y], mesh.positions[i.z]),
            key=lambda p: tuple(p)
        ))
        for i in mesh.triangle_indices
    ) == {
        (Vector2(75.0, 25.0), Vector2(100.0, 0.0), Vector2(100.0, 100.0)),
        (Vector2(0.0, 100.0), Vector2(75.0, 75.0), Vector2(100.0, 100.0)),
        (Vector2(75.0, 25.0), Vector2(75.0, 75.0), Vector2(100.0, 100.0)),
        (Vector2(0.0, 0.0), Vector2(25.0, 25.0), Vector2(75.0, 25.0)),
        (Vector2(0.0, 100.0), Vector2(25.0, 75.0), Vector2(75.0, 75.0)),
        (Vector2(0.0, 0.0), Vector2(0.0, 100.0), Vector2(25.0, 75.0)),
        (Vector2(0.0, 0.0), Vector2(25.0, 25.0), Vector2(25.0, 75.0)),
        (Vector2(0.0, 0.0), Vector2(75.0, 25.0), Vector2(100.0, 0.0))
    }
