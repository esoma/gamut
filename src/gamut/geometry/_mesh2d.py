
from __future__ import annotations

__all__ = ['Mesh2d']

# gamut
from gamut.math import UVector3Array, Vector2Array


class Mesh2d:

    def __init__(
        self,
        positions: Vector2Array,
        triangle_indices: UVector3Array,
    ):
        if not isinstance(positions, Vector2Array):
            raise TypeError('positions must be Vector2Array')
        if not positions:
            raise ValueError('must have at least 1 vertex position')
        self._positions = positions

        if not isinstance(triangle_indices, UVector3Array):
            raise TypeError('indices must be UVector3Array')
        if not triangle_indices:
            raise ValueError('must have at least 1 triangle')
        self._triangle_indices = triangle_indices

        length = len(positions)
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

    def __eq__(self, other: Mesh2d) -> bool:
        if not isinstance(other, Mesh2d):
            return False
        return (
            self._positions == other._positions and
            self._triangle_indices == other._triangle_indices
        )

    def __repr__(self) -> str:
        return f'<gamut.geometry.Mesh2d>'

    @property
    def positions(self) -> Vector2Array:
        return self._positions

    @property
    def triangle_indices(self) -> UVector3Array:
        return self._triangle_indices
