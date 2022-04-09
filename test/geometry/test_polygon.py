
# gamut
from gamut.geometry import Mesh2d, Polygon
from gamut.math import (DVector2, DVector2Array, DVector4, FVector2,
                        FVector2Array)
# python
from typing import Any
# pytest
import pytest


def test_hash() -> None:
    exterior = DVector2Array()
    p1 = Polygon(exterior)
    p2 = Polygon(exterior)
    assert hash(p1) != hash(p2)


def test_repr() -> None:
    p = Polygon(DVector2Array())
    assert repr(p) == '<gamut.geometry.Polygon>'


@pytest.mark.parametrize("exterior", [
    [None],
    [1],
    ['123'],
    [DVector2(1)],
    [DVector4(1)],
])
def test_exterior_invalid_type(exterior: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Polygon(exterior)
    assert str(excinfo.value) == (
        'exterior must be FVector2Array or DVector2Array'
    )


@pytest.mark.parametrize("holes", [object(), 1])
def test_holes_not_iterable(holes: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Polygon(DVector2Array(), holes=holes)


@pytest.mark.parametrize("holes", [
    [None],
    [DVector2Array(), None],
])
def test_holes_invalid_type(holes: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Polygon(DVector2Array(), holes=holes)
    assert str(excinfo.value) == 'each hole must be DVector2Array'


@pytest.mark.parametrize("exterior", [
    DVector2Array(DVector2(0, 1), DVector2(3, 4)),
    DVector2Array(DVector2(0), DVector2(1), DVector2(2)),
])
def test_exterior(exterior: Any) -> None:
    p = Polygon(exterior)
    assert p.exterior == exterior


@pytest.mark.parametrize("holes", [
    [DVector2Array(DVector2(0, 1), DVector2(3, 4))],
    [DVector2Array(DVector2(0), DVector2(1), DVector2(2))],
    [
        DVector2Array(DVector2(0, 1), DVector2(3, 4)),
        DVector2Array(DVector2(0), DVector2(1), DVector2(2)),
    ],
])
def test_holes(holes: Any) -> None:
    p = Polygon(DVector2Array(), holes=holes)
    assert isinstance(p.holes, tuple)
    assert p.holes == tuple(holes)


def test_d_triangulate() -> None:
    p = Polygon(
        DVector2Array(
            DVector2(0, 0),
            DVector2(100, 0),
            DVector2(100, 100),
            DVector2(0, 100)
        ),
        holes=[
            DVector2Array(
                DVector2(25, 25),
                DVector2(75, 25),
                DVector2(75, 75),
                DVector2(25, 75)
            )
        ]
    )
    mesh = p.triangulate()
    assert isinstance(mesh, Mesh2d)
    assert set(mesh.positions) == {
        DVector2(0, 0),
        DVector2(100, 0),
        DVector2(100, 100),
        DVector2(0, 100),
        DVector2(25, 25),
        DVector2(75, 25),
        DVector2(75, 75),
        DVector2(25, 75)
    }
    assert set(
        tuple(sorted(
            (mesh.positions[i.x], mesh.positions[i.y], mesh.positions[i.z]),
            key=lambda p: tuple(p)
        ))
        for i in mesh.triangle_indices
    ) == {
        (DVector2(75.0, 25.0), DVector2(100.0, 0.0), DVector2(100.0, 100.0)),
        (DVector2(0.0, 100.0), DVector2(75.0, 75.0), DVector2(100.0, 100.0)),
        (DVector2(75.0, 25.0), DVector2(75.0, 75.0), DVector2(100.0, 100.0)),
        (DVector2(0.0, 0.0), DVector2(25.0, 25.0), DVector2(75.0, 25.0)),
        (DVector2(0.0, 100.0), DVector2(25.0, 75.0), DVector2(75.0, 75.0)),
        (DVector2(0.0, 0.0), DVector2(0.0, 100.0), DVector2(25.0, 75.0)),
        (DVector2(0.0, 0.0), DVector2(25.0, 25.0), DVector2(25.0, 75.0)),
        (DVector2(0.0, 0.0), DVector2(75.0, 25.0), DVector2(100.0, 0.0))
    }


def test_f_triangulate() -> None:
    p = Polygon(
        FVector2Array(
            FVector2(0, 0),
            FVector2(100, 0),
            FVector2(100, 100),
            FVector2(0, 100)
        ),
        holes=[
            FVector2Array(
                FVector2(25, 25),
                FVector2(75, 25),
                FVector2(75, 75),
                FVector2(25, 75)
            )
        ]
    )
    mesh = p.triangulate()
    assert isinstance(mesh, Mesh2d)
    assert set(mesh.positions) == {
        FVector2(0, 0),
        FVector2(100, 0),
        FVector2(100, 100),
        FVector2(0, 100),
        FVector2(25, 25),
        FVector2(75, 25),
        FVector2(75, 75),
        FVector2(25, 75)
    }
    assert set(
        tuple(sorted(
            (mesh.positions[i.x], mesh.positions[i.y], mesh.positions[i.z]),
            key=lambda p: tuple(p)
        ))
        for i in mesh.triangle_indices
    ) == {
        (FVector2(75.0, 25.0), FVector2(100.0, 0.0), FVector2(100.0, 100.0)),
        (FVector2(0.0, 100.0), FVector2(75.0, 75.0), FVector2(100.0, 100.0)),
        (FVector2(75.0, 25.0), FVector2(75.0, 75.0), FVector2(100.0, 100.0)),
        (FVector2(0.0, 0.0), FVector2(25.0, 25.0), FVector2(75.0, 25.0)),
        (FVector2(0.0, 100.0), FVector2(25.0, 75.0), FVector2(75.0, 75.0)),
        (FVector2(0.0, 0.0), FVector2(0.0, 100.0), FVector2(25.0, 75.0)),
        (FVector2(0.0, 0.0), FVector2(25.0, 25.0), FVector2(25.0, 75.0)),
        (FVector2(0.0, 0.0), FVector2(75.0, 25.0), FVector2(100.0, 0.0))
    }

def test_equal() -> None:
    assert Polygon(DVector2Array()) == Polygon(DVector2Array())
    assert Polygon(FVector2Array()) == Polygon(FVector2Array())
    assert Polygon(DVector2Array()) != Polygon(FVector2Array())
    assert Polygon(DVector2Array(DVector2(0))) != Polygon(DVector2Array())
    assert Polygon(FVector2Array(FVector2(0))) != Polygon(FVector2Array())
    assert Polygon(
        DVector2Array(),
        holes=[DVector2Array()]
    ) != Polygon(DVector2Array())
    assert Polygon(
        FVector2Array(),
        holes=[FVector2Array()]
    ) != Polygon(FVector2Array())
