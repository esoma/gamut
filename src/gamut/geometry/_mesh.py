
from __future__ import annotations

__all__ = ['Mesh']

# gamut
from gamut.glmhelp import dvec3_exact, F64Vector3, I32Vector3, ivec3_exact
# python
from copy import deepcopy
from typing import Iterable
# pyglm
from glm import array, dmat4, dvec3, ivec3, mat4


class Mesh:

    def __init__(
        self,
        vertices: Iterable[F64Vector3],
        triangle_indices: Iterable[I32Vector3]
    ):
        try:
            self._vertices = array(*(dvec3_exact(v) for v in vertices))
        except TypeError as ex:
            if str(ex) == 'cannot create an empty array':
                raise ValueError('must have at least 1 vertex')
            raise TypeError('each vertex must be dvec3')
        try:
            self._triangle_indices = array(*(
                ivec3_exact(t) for t in triangle_indices
            ))
        except TypeError as ex:
            if str(ex) == 'cannot create an empty array':
                raise ValueError('must have at least 1 triangle')
            raise TypeError('each triangle must be ivec3')
        for triangle in self._triangle_indices:
            if (triangle.x < 0 or triangle.x >= len(self._vertices) or
                triangle.y < 0 or triangle.y >= len(self._vertices) or
                triangle.z < 0 or triangle.z >= len(self._vertices)):
                raise ValueError(
                    'triangle indices must be between 0 and the number of '
                    'vertices'
                )

    def __hash__(self) -> int:
        return id(self)

    def __eq__(self, other: Mesh) -> bool:
        if not isinstance(other, Mesh):
            return False
        return (
            self._vertices == other._vertices and
            self._triangle_indices == other._triangle_indices
        )

    def __repr__(self) -> str:
        return f'<gamut.geometry.Mesh>'

    def __rmul__(self, transform: mat4 | dmat4) -> Mesh:
        if isinstance(transform, mat4):
            transform = dmat4(transform)
        elif not isinstance(transform, dmat4):
            return NotImplemented

        return Mesh(
            (transform * p for p in self._vertices),
            self._triangle_indices
        )

    @property
    def vertices(self) -> 'array[dvec3]':
        return deepcopy(self._vertices)

    @property
    def triangle_indices(self) -> 'array[ivec3]':
        return deepcopy(self._triangle_indices)
