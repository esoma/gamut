
# gamut
from gamut.geometry import Mesh2d
from gamut.math import UVector3, UVector3Array, Vector2, Vector2Array, Vector4
# python
from typing import Any
# pytest
import pytest


def test_hash() -> None:
    positions = Vector2Array(Vector2(1, 2))
    triangle_indexes = UVector3Array(UVector3(0))
    m1 = Mesh2d(positions, triangle_indexes)
    m2 = Mesh2d(positions, triangle_indexes)
    assert hash(m1) != hash(m2)


def test_repr() -> None:
    m = Mesh2d(Vector2Array(Vector2(1, 2)), UVector3Array(UVector3(0)))
    assert repr(m) == '<gamut.geometry.Mesh2d>'


def test_no_positions() -> None:
    with pytest.raises(ValueError) as excinfo:
        Mesh2d(Vector2Array(), UVector3Array(UVector3(0)))
    assert str(excinfo.value) == 'must have at least 1 vertex position'


@pytest.mark.parametrize("positions", [
    [None],
    [1],
    ['123'],
    [Vector2(1)],
    [Vector4(1)],
])
def test_positions_invalid_type(positions: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Mesh2d(positions, [UVector3(0)])
    assert str(excinfo.value) == 'positions must be Vector2Array'


def test_no_triangle_indices() -> None:
    with pytest.raises(ValueError) as excinfo:
        Mesh2d(Vector2Array(Vector2(0)), UVector3Array())
    assert str(excinfo.value) == 'must have at least 1 triangle'


@pytest.mark.parametrize("indices", [
    [None],
    [1],
    ['123'],
    [Vector2(1)],
    [Vector4(1)],
])
def test_triangle_indices_invalid_type(indices: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Mesh2d(Vector2Array(Vector2(0)), indices)
    assert str(excinfo.value) == 'indices must be UVector3Array'


@pytest.mark.parametrize("positions, triangle_indices", [
    (
        Vector2Array(Vector2(0)),
        UVector3Array(UVector3(1, 0, 0)),
    ),
    (
        Vector2Array(Vector2(0)),
        UVector3Array(UVector3(1, 0, 0)),
    ),
])
def test_triangle_indices_invalid_value(
    positions: Any,
    triangle_indices: Any,
) -> None:
    with pytest.raises(ValueError) as excinfo:
        Mesh2d(positions, triangle_indices)
    assert (
        str(excinfo.value) ==
        'triangle indices must be between 0 and the number of vertices'
    )


@pytest.mark.parametrize("positions", [
    Vector2Array(Vector2(0, 1), Vector2(3, 4)),
    Vector2Array(Vector2(0), Vector2(1), Vector2(2)),
])
def test_positions(positions: Any) -> None:
    m = Mesh2d(positions, UVector3Array(UVector3(0)))
    assert m.positions == positions


@pytest.mark.parametrize("triangle_indices", [
    UVector3Array(UVector3(0)),
    UVector3Array(UVector3(0, 1, 2)),
    UVector3Array(UVector3(0, 1, 2), UVector3(1, 2, 3), UVector3(2, 3, 0)),
])
def test_triangle_indices(triangle_indices: Any) -> None:
    m = Mesh2d(
        Vector2Array(Vector2(0), Vector2(1), Vector2(2), Vector2(3)),
        triangle_indices
    )
    assert m.triangle_indices == triangle_indices


def test_equal() -> None:
    assert Mesh2d(Vector2Array(Vector2(0)), UVector3Array(UVector3(0))) == (
        Mesh2d(Vector2Array(Vector2(0)), UVector3Array(UVector3(0)))
    )
    assert Mesh2d(Vector2Array(Vector2(0)), UVector3Array(UVector3(0))) != (
        Mesh2d(
            Vector2Array(Vector2(0), Vector2(0)),
            UVector3Array(UVector3(0))
        )
    )
    assert Mesh2d(Vector2Array(Vector2(0)), UVector3Array(UVector3(0))) != (
        Mesh2d(
            Vector2Array(Vector2(0)),
            UVector3Array(UVector3(0), UVector3(0))
        )
    )
    assert Mesh2d(Vector2Array(Vector2(0)), UVector3Array(UVector3(0))) != (
        Mesh2d(Vector2Array(Vector2(1, 0)), UVector3Array(UVector3(0)))
    )
    assert Mesh2d(Vector2Array(Vector2(0)), UVector3Array(UVector3(0))) != (
        Mesh2d(Vector2Array(Vector2(0, 1)), UVector3Array(UVector3(0)))
    )
    positions = Vector2Array(Vector2(0), Vector2(0))
    assert (
        Mesh2d(positions, UVector3Array(UVector3(0))) !=
        Mesh2d(positions, UVector3Array(UVector3(1, 0, 0)))
    )
    assert (
        Mesh2d(positions, UVector3Array(UVector3(0))) !=
        Mesh2d(positions, UVector3Array(UVector3(0, 1, 0)))
    )
    assert (
        Mesh2d(positions, UVector3Array(UVector3(0))) !=
        Mesh2d(positions, UVector3Array(UVector3(0, 0, 1)))
    )
    assert Mesh2d(Vector2Array(Vector2(0)), UVector3Array(UVector3(0))) != (
        object()
    )
