
# gamut
from gamut.geometry import Mesh
from gamut.math import (IVector3, IVector3Array, Matrix4, Vector2, Vector3,
                        Vector3Array, Vector4)
# python
from math import radians
from typing import Any
# pytest
import pytest


def test_hash() -> None:
    vertices = Vector3Array(Vector3(1, 2, 3))
    triangle_indexes = IVector3Array(IVector3(0))
    m1 = Mesh(vertices, triangle_indexes)
    m2 = Mesh(vertices, triangle_indexes)
    assert hash(m1) != hash(m2)


def test_repr() -> None:
    m = Mesh(Vector3Array(Vector3(1, 2, 3)), IVector3Array(IVector3(0)))
    assert repr(m) == '<gamut.geometry.Mesh>'


def test_no_vertices() -> None:
    with pytest.raises(ValueError) as excinfo:
        Mesh(Vector3Array(), IVector3Array(IVector3(0)))
    assert str(excinfo.value) == 'must have at least 1 vertex'


@pytest.mark.parametrize("vertices", [
    [None],
    [1],
    ['123'],
    [Vector2(1)],
    [Vector4(1)],
])
def test_vertices_invalid_type(vertices: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Mesh(vertices, [IVector3(0)])
    assert str(excinfo.value) == 'vertices must be Vector3Array'


def test_no_triangle_indices() -> None:
    with pytest.raises(ValueError) as excinfo:
        Mesh(Vector3Array(Vector3(0)), IVector3Array())
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
        Mesh(Vector3Array(Vector3(0)), indices)
    assert str(excinfo.value) == 'indices must be IVector3Array'


@pytest.mark.parametrize("triangle_indices", [
    IVector3Array(IVector3(-1, 0, 0)),
    IVector3Array(IVector3(1, 0, 0)),
])
def test_triangle_indices_invalid_value(triangle_indices: Any) -> None:
    with pytest.raises(ValueError) as excinfo:
        Mesh(Vector3Array(Vector3(0)), triangle_indices)
    assert (
        str(excinfo.value) ==
        'triangle indices must be between 0 and the number of vertices'
    )


@pytest.mark.parametrize("vertices", [
    Vector3Array(Vector3(0, 1, 2), Vector3(3, 4, 5)),
    Vector3Array(Vector3(0), Vector3(1), Vector3(2)),
])
def test_vertices(vertices: Any) -> None:
    m = Mesh(vertices, IVector3Array(IVector3(0)))
    assert m.vertices == vertices


@pytest.mark.parametrize("triangle_indices", [
    IVector3Array(IVector3(0)),
    IVector3Array(IVector3(0, 1, 2)),
    IVector3Array(IVector3(0, 1, 2), IVector3(1, 2, 3), IVector3(2, 3, 0)),
])
def test_vertices(triangle_indices: Any) -> None:
    m = Mesh(
        Vector3Array(Vector3(0), Vector3(1), Vector3(2), Vector3(3)),
        triangle_indices
    )
    assert m.triangle_indices == triangle_indices


@pytest.mark.parametrize("mesh", [
    Mesh(Vector3Array(Vector3(0, 1, 2)), IVector3Array(IVector3(0))),
    Mesh(
        Vector3Array(Vector3(0, 1, 2), Vector3(3, 4, 5)),
        IVector3Array(IVector3(0))
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
def test_transform(mesh: Mesh, transform: Matrix4) -> None:
    new_ch = transform @ mesh
    assert new_ch is not mesh
    assert new_ch.vertices == Vector3Array(*(
        transform @ v for v in mesh.vertices
    ))
    assert new_ch.triangle_indices == mesh.triangle_indices


def test_equal() -> None:
    assert Mesh(Vector3Array(Vector3(0)), IVector3Array(IVector3(0))) == (
        Mesh(Vector3Array(Vector3(0)), IVector3Array(IVector3(0)))
    )
    assert Mesh(Vector3Array(Vector3(0)), IVector3Array(IVector3(0))) != (
        Mesh(Vector3Array(Vector3(0), Vector3(0)), IVector3Array(IVector3(0)))
    )
    assert Mesh(Vector3Array(Vector3(0)), IVector3Array(IVector3(0))) != (
        Mesh(Vector3Array(Vector3(0)), IVector3Array(IVector3(0), IVector3(0)))
    )
    assert Mesh(Vector3Array(Vector3(0)), IVector3Array(IVector3(0))) != (
        Mesh(Vector3Array(Vector3(1, 0, 0)), IVector3Array(IVector3(0)))
    )
    assert Mesh(Vector3Array(Vector3(0)), IVector3Array(IVector3(0))) != (
        Mesh(Vector3Array(Vector3(0, 1, 0)), IVector3Array(IVector3(0)))
    )
    assert Mesh(Vector3Array(Vector3(0)), IVector3Array(IVector3(0))) != (
        Mesh(Vector3Array(Vector3(0, 0, 1)), IVector3Array(IVector3(0)))
    )
    vertices = Vector3Array(Vector3(0), Vector3(0))
    assert (
        Mesh(vertices, IVector3Array(IVector3(0))) !=
        Mesh(vertices, IVector3Array(IVector3(1, 0, 0)))
    )
    assert (
        Mesh(vertices, IVector3Array(IVector3(0))) !=
        Mesh(vertices, IVector3Array(IVector3(0, 1, 0)))
    )
    assert (
        Mesh(vertices, IVector3Array(IVector3(0))) !=
        Mesh(vertices, IVector3Array(IVector3(0, 0, 1)))
    )
    assert Mesh(Vector3Array(Vector3(0)), IVector3Array(IVector3(0))) != (
        object()
    )
