
# gamut
from gamut.geometry import Mesh
# python
from typing import Any
# pyglm
from glm import (array, dmat4, dvec3, ivec3, mat4, radians, rotate, scale,
                 translate, vec2, vec3, vec4)
# pytest
import pytest


def test_hash() -> None:
    m1 = Mesh([vec3(1, 2, 3)], [ivec3(0)])
    m2 = Mesh([vec3(1, 2, 3)], [ivec3(0)])
    assert hash(m1) != hash(m2)


def test_repr() -> None:
    m = Mesh([vec3(1, 2, 3)], [ivec3(0)])
    assert repr(m) == '<gamut.geometry.Mesh>'


def test_no_vertices() -> None:
    with pytest.raises(ValueError) as excinfo:
        Mesh([], [ivec3(0)])
    assert str(excinfo.value) == 'must have at least 1 vertex'


@pytest.mark.parametrize("good_vertices", [
    [],
    [vec3(0)],
    [vec3(0), vec3(0)],
])
@pytest.mark.parametrize("vertices", [
    [None],
    [1],
    ['123'],
    [vec2(1)],
    [vec4(1)],
])
def test_vertices_invalid_type(good_vertices: Any, vertices: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Mesh([*good_vertices, *vertices], [ivec3(0)])
    assert str(excinfo.value) == 'each vertex must be dvec3'


def test_no_triangle_indices() -> None:
    with pytest.raises(ValueError) as excinfo:
        Mesh([vec3(0)], [])
    assert str(excinfo.value) == 'must have at least 1 triangle'


@pytest.mark.parametrize("good_indices", [
    [ivec3(0)],
])
@pytest.mark.parametrize("indices", [
    [None],
    [1],
    ['123'],
    [vec2(1)],
    [vec4(1)],
])
def test_triangle_indices_invalid_type(
    good_indices: Any,
    indices: Any
) -> None:
    with pytest.raises(TypeError) as excinfo:
        Mesh([vec3(0)], [*good_indices, *indices])
    assert str(excinfo.value) == 'each triangle must be ivec3'


@pytest.mark.parametrize("triangle_indices", [
    [ivec3(-1, 0, 0)],
    [ivec3(1, 0, 0)],
])
def test_triangle_indices_invalid_value(triangle_indices: Any) -> None:
    with pytest.raises(ValueError) as excinfo:
        Mesh([vec3(0)], triangle_indices)
    assert (
        str(excinfo.value) ==
        'triangle indices must be between 0 and the number of vertices'
    )


@pytest.mark.parametrize("vertices", [
    [vec3(0, 1, 2), (3, 4, 5)],
    [vec3(0), vec3(1), vec3(2)],
])
def test_vertices(vertices: Any) -> None:
    m = Mesh(vertices, [ivec3(0)])
    assert m.vertices == array(*(vec3(v) for v in vertices))


@pytest.mark.parametrize("triangle_indices", [
    [ivec3(0)],
    [ivec3(0, 1, 2)],
    [ivec3(0, 1, 2), ivec3(1, 2, 3), ivec3(2, 3, 0)],
])
def test_vertices(triangle_indices: Any) -> None:
    m = Mesh([vec3(0), vec3(1), vec3(2), vec3(3)], triangle_indices)
    assert m.triangle_indices == array(*(ivec3(v) for v in triangle_indices))


@pytest.mark.parametrize("mesh", [
    Mesh([vec3(0, 1, 2)], [ivec3(0)]),
    Mesh([vec3(0, 1, 2), vec3(3, 4, 5)], [ivec3(0)]),
])
@pytest.mark.parametrize("transform", [
    translate(mat4(1), vec3(1, 0, 0)),
    translate(dmat4(1), dvec3(0, 1, 0)),
    translate(dmat4(1), dvec3(0, 0, 1)),
    rotate(dmat4(1), radians(90), dvec3(1, 0, 0)),
    rotate(dmat4(1), radians(90), dvec3(0, 1, 0)),
    rotate(dmat4(1), radians(90), dvec3(0, 0, 1)),
    scale(dmat4(1), dvec3(2, 3, 4)),
])
def test_transform(mesh: Mesh, transform: dmat4) -> None:
    new_ch = transform * mesh
    assert new_ch is not mesh
    assert new_ch.vertices == array(*(
        dmat4(transform) * v for v in mesh.vertices
    ))
    assert new_ch.triangle_indices == mesh.triangle_indices


def test_equal() -> None:
    assert Mesh([vec3(0)], [ivec3(0)]) == Mesh([vec3(0)], [ivec3(0)])
    assert Mesh([vec3(0)], [ivec3(0)]) != Mesh([vec3(0), vec3(0)], [ivec3(0)])
    assert Mesh([vec3(0)], [ivec3(0)]) != Mesh([vec3(0)], [ivec3(0), ivec3(0)])
    assert Mesh([vec3(0)], [ivec3(0)]) != Mesh([vec3(1, 0, 0)], [ivec3(0)])
    assert Mesh([vec3(0)], [ivec3(0)]) != Mesh([vec3(0, 1, 0)], [ivec3(0)])
    assert Mesh([vec3(0)], [ivec3(0)]) != Mesh([vec3(0, 0, 1)], [ivec3(0)])
    assert (
        Mesh([vec3(0), vec3(0)], [ivec3(0)]) !=
        Mesh([vec3(0), vec3(0)], [ivec3(1, 0, 0)])
    )
    assert (
        Mesh([vec3(0), vec3(0)], [ivec3(0)]) !=
        Mesh([vec3(0), vec3(0)], [ivec3(0, 1, 0)])
    )
    assert (
        Mesh([vec3(0), vec3(0)], [ivec3(0)]) !=
        Mesh([vec3(0), vec3(0)], [ivec3(0, 0, 1)])
    )
    assert Mesh([vec3(0)], [ivec3(0)]) != object()
