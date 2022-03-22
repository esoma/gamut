
from __future__ import annotations

__all__ = ['Mesh']

# gamut
from gamut.math import Matrix4, UVector3Array, Vector3Array


class Mesh:

    def __init__(
        self,
        positions: Vector3Array,
        triangle_indices: UVector3Array,
        *,
        normals: Vector3Array | None = None
    ):
        if not isinstance(positions, Vector3Array):
            raise TypeError('positions must be Vector3Array')
        if not positions:
            raise ValueError('must have at least 1 vertex position')
        self._positions = positions

        self._normals = normals
        if normals is not None:
            if not isinstance(normals, Vector3Array):
                raise TypeError('normals must be Vector3Array')
            if not normals:
                raise ValueError('must have at least 1 vertex normal')

        if not isinstance(triangle_indices, UVector3Array):
            raise TypeError('indices must be UVector3Array')
        if not triangle_indices:
            raise ValueError('must have at least 1 triangle')
        self._triangle_indices = triangle_indices

        length = len(positions)
        if normals is not None:
            length = min(length, len(normals))
        for triangle in self._triangle_indices:
            if (triangle.x >= length or
                triangle.y >= length or
                triangle.z >= length):
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
            self._positions == other._positions and
            self._triangle_indices == other._triangle_indices and
            self._normals == other._normals
        )

    def __repr__(self) -> str:
        return f'<gamut.geometry.Mesh>'

    def __rmatmul__(self, transform: Matrix4) -> Mesh:
        if not isinstance(transform, Matrix4):
            return NotImplemented

        normals: Vector3Array | None = None
        if self._normals is not None:
            normal_transform = transform.inverse().transpose().to_matrix3()
            normals = Vector3Array(*(
                normal_transform @ n for n in self._normals
            ))

        return Mesh(
            Vector3Array(*(transform @ p for p in self._positions)),
            self._triangle_indices,
            normals=normals
        )

    @property
    def normals(self) -> Vector3Array | None:
        return self._normals

    @property
    def positions(self) -> Vector3Array:
        return self._positions

    @property
    def triangle_indices(self) -> UVector3Array:
        return self._triangle_indices
