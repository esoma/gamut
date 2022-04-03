
# gamut
from gamut.geometry import Mesh3d
from gamut.math import (Matrix4, UVector3, UVector3Array, Vector2, Vector3,
                        Vector3Array, Vector4)
# python
from math import radians
from typing import Any
# pytest
import pytest


def test_hash() -> None:
    positions = Vector3Array(Vector3(1, 2, 3))
    triangle_indexes = UVector3Array(UVector3(0))
    m1 = Mesh3d(positions, triangle_indexes)
    m2 = Mesh3d(positions, triangle_indexes)
    assert hash(m1) != hash(m2)


def test_repr() -> None:
    m = Mesh3d(Vector3Array(Vector3(1, 2, 3)), UVector3Array(UVector3(0)))
    assert repr(m) == '<gamut.geometry.Mesh3d>'


def test_no_positions() -> None:
    with pytest.raises(ValueError) as excinfo:
        Mesh3d(Vector3Array(), UVector3Array(UVector3(0)))
    assert str(excinfo.value) == 'must have at least 1 vertex position'


def test_no_normals() -> None:
    with pytest.raises(ValueError) as excinfo:
        Mesh3d(
            Vector3Array(Vector3(0)),
            UVector3Array(UVector3(0)),
            normals=Vector3Array()
        )
    assert str(excinfo.value) == 'must have at least 1 vertex normal'


@pytest.mark.parametrize("positions", [
    [None],
    [1],
    ['123'],
    [Vector2(1)],
    [Vector4(1)],
])
def test_positions_invalid_type(positions: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Mesh3d(positions, [UVector3(0)])
    assert str(excinfo.value) == 'positions must be Vector3Array'


@pytest.mark.parametrize("normals", [
    [None],
    [1],
    ['123'],
    [Vector2(1)],
    [Vector4(1)],
])
def test_normals_invalid_type(normals: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Mesh3d(Vector3Array(Vector3(0)), [UVector3(0)], normals=normals)
    assert str(excinfo.value) == 'normals must be Vector3Array'


def test_no_triangle_indices() -> None:
    with pytest.raises(ValueError) as excinfo:
        Mesh3d(Vector3Array(Vector3(0)), UVector3Array())
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
        Mesh3d(Vector3Array(Vector3(0)), indices)
    assert str(excinfo.value) == 'indices must be UVector3Array'


@pytest.mark.parametrize("positions, triangle_indices, normals", [
    (
        Vector3Array(Vector3(0)),
        UVector3Array(UVector3(1, 0, 0)),
        None
    ),
    (
        Vector3Array(Vector3(0)),
        UVector3Array(UVector3(1, 0, 0)),
        Vector3Array(Vector3(0)),
    ),
    (
        Vector3Array(Vector3(0), Vector3(0)),
        UVector3Array(UVector3(1, 0, 0)),
        Vector3Array(Vector3(0)),
    ),
    (
        Vector3Array(Vector3(0)),
        UVector3Array(UVector3(1, 0, 0)),
        Vector3Array(Vector3(0), Vector3(0)),
    ),
])
def test_triangle_indices_invalid_value(
    positions: Any,
    triangle_indices: Any,
    normals: Any
) -> None:
    with pytest.raises(ValueError) as excinfo:
        Mesh3d(positions, triangle_indices, normals=normals)
    assert (
        str(excinfo.value) ==
        'triangle indices must be between 0 and the number of vertices'
    )


@pytest.mark.parametrize("positions", [
    Vector3Array(Vector3(0, 1, 2), Vector3(3, 4, 5)),
    Vector3Array(Vector3(0), Vector3(1), Vector3(2)),
])
def test_positions(positions: Any) -> None:
    m = Mesh3d(positions, UVector3Array(UVector3(0)))
    assert m.positions == positions


@pytest.mark.parametrize("triangle_indices", [
    UVector3Array(UVector3(0)),
    UVector3Array(UVector3(0, 1, 2)),
    UVector3Array(UVector3(0, 1, 2), UVector3(1, 2, 3), UVector3(2, 3, 0)),
])
def test_triangle_indices(triangle_indices: Any) -> None:
    m = Mesh3d(
        Vector3Array(Vector3(0), Vector3(1), Vector3(2), Vector3(3)),
        triangle_indices
    )
    assert m.triangle_indices == triangle_indices


@pytest.mark.parametrize("normals", [
    Vector3Array(Vector3(0, 1, 2), Vector3(3, 4, 5)),
    Vector3Array(Vector3(0), Vector3(1), Vector3(2)),
])
def test_normals(normals: Any) -> None:
    m = Mesh3d(
        Vector3Array(Vector3(0)),
        UVector3Array(UVector3(0)),
        normals=normals
    )
    assert m.normals == normals


@pytest.mark.parametrize("mesh", [
    Mesh3d(Vector3Array(Vector3(0, 1, 2)), UVector3Array(UVector3(0))),
    Mesh3d(
        Vector3Array(Vector3(0, 1, 2), Vector3(3, 4, 5)),
        UVector3Array(UVector3(0))
    ),
    Mesh3d(
        Vector3Array(Vector3(0, 1, 2), Vector3(3, 4, 5)),
        UVector3Array(UVector3(0)),
        normals=Vector3Array(Vector3(0, 1, 2), Vector3(3, 4, 5)),
    ),
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
def test_transform(mesh: Mesh3d, transform: Matrix4) -> None:
    new_ch = transform @ mesh
    assert new_ch is not mesh
    assert new_ch.positions == Vector3Array(*(
        transform @ v for v in mesh.positions
    ))
    assert new_ch.triangle_indices == mesh.triangle_indices
    if mesh.normals is None:
        assert new_ch.normals is None
    else:
        normal_transform = transform.inverse().transpose().to_matrix3()
        assert new_ch.normals == Vector3Array(*(
            normal_transform @ v for v in mesh.normals
        ))


def test_equal() -> None:
    assert Mesh3d(Vector3Array(Vector3(0)), UVector3Array(UVector3(0))) == (
        Mesh3d(Vector3Array(Vector3(0)), UVector3Array(UVector3(0)))
    )
    assert Mesh3d(Vector3Array(Vector3(0)), UVector3Array(UVector3(0))) != (
        Mesh3d(
            Vector3Array(Vector3(0), Vector3(0)),
            UVector3Array(UVector3(0))
        )
    )
    assert Mesh3d(Vector3Array(Vector3(0)), UVector3Array(UVector3(0))) != (
        Mesh3d(
            Vector3Array(Vector3(0)),
            UVector3Array(UVector3(0), UVector3(0))
        )
    )
    assert Mesh3d(Vector3Array(Vector3(0)), UVector3Array(UVector3(0))) != (
        Mesh3d(Vector3Array(Vector3(1, 0, 0)), UVector3Array(UVector3(0)))
    )
    assert Mesh3d(Vector3Array(Vector3(0)), UVector3Array(UVector3(0))) != (
        Mesh3d(Vector3Array(Vector3(0, 1, 0)), UVector3Array(UVector3(0)))
    )
    assert Mesh3d(Vector3Array(Vector3(0)), UVector3Array(UVector3(0))) != (
        Mesh3d(Vector3Array(Vector3(0, 0, 1)), UVector3Array(UVector3(0)))
    )
    positions = Vector3Array(Vector3(0), Vector3(0))
    assert (
        Mesh3d(positions, UVector3Array(UVector3(0))) !=
        Mesh3d(positions, UVector3Array(UVector3(1, 0, 0)))
    )
    assert (
        Mesh3d(positions, UVector3Array(UVector3(0))) !=
        Mesh3d(positions, UVector3Array(UVector3(0, 1, 0)))
    )
    assert (
        Mesh3d(positions, UVector3Array(UVector3(0))) !=
        Mesh3d(positions, UVector3Array(UVector3(0, 0, 1)))
    )
    assert Mesh3d(Vector3Array(Vector3(0)), UVector3Array(UVector3(0))) != (
        object()
    )
    assert Mesh3d(
        Vector3Array(Vector3(0)),
        UVector3Array(UVector3(0)),
        normals=Vector3Array(Vector3(0))
    ) == Mesh3d(
        Vector3Array(Vector3(0)),
        UVector3Array(UVector3(0)),
        normals=Vector3Array(Vector3(0))
    )
    assert Mesh3d(
        Vector3Array(Vector3(0)),
        UVector3Array(UVector3(0)),
        normals=Vector3Array(Vector3(0))
    ) != Mesh3d(
        Vector3Array(Vector3(0)),
        UVector3Array(UVector3(0)),
        normals=Vector3Array(Vector3(1))
    )


def test_raycast() -> None:
    mesh = Mesh3d(
        Vector3Array(
            Vector3(-1, -1, 0),
            Vector3(1, -1, 0),
            Vector3(1, 1, 0),
            Vector3(-1, 1, 0),
        ),
        UVector3Array(
            UVector3(0, 1, 2),
            UVector3(0, 2, 3),
        )
    )
    result = mesh.raycast(Vector3(-.5, -.5, 1), Vector3(-.5, -.5, -1))
    assert result is not None
    assert result.position == Vector3(-.5, -.5, 0)
    assert result.normal == Vector3(0, 0, 1)
    assert result.triangle_index == 0
    assert result.time == .5
