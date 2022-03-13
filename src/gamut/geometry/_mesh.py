
from __future__ import annotations

__all__ = ['Mesh']

# gamut
from gamut.math import IVector3Array, Matrix4, Vector3Array


class Mesh:

    def __init__(
        self,
        vertices: Vector3Array,
        triangle_indices: IVector3Array
    ):
        if not isinstance(vertices, Vector3Array):
            raise TypeError('vertices must be Vector3Array')
        if not vertices:
            raise ValueError('must have at least 1 vertex')
        self._vertices = vertices

        if not isinstance(triangle_indices, IVector3Array):
            raise TypeError('indices must be IVector3Array')
        if not triangle_indices:
            raise ValueError('must have at least 1 triangle')
        self._triangle_indices = triangle_indices
        for triangle in self._triangle_indices:
            if (triangle.x < 0 or triangle.x >= len(vertices) or
                triangle.y < 0 or triangle.y >= len(vertices) or
                triangle.z < 0 or triangle.z >= len(vertices)):
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

    def __rmatmul__(self, transform: Matrix4) -> Mesh:
        if not isinstance(transform, Matrix4):
            return NotImplemented

        return Mesh(
            Vector3Array(*(transform @ p for p in self._vertices)),
            self._triangle_indices
        )

    @property
    def vertices(self) -> Vector3Array:
        return self._vertices

    @property
    def triangle_indices(self) -> IVector3Array:
        return self._triangle_indices
