
from __future__ import annotations

__all__ = ['ConvexHull']

# gamut
from gamut.math import Matrix4, Vector3Array


class ConvexHull:

    def __init__(self, points: Vector3Array):
        if not isinstance(points, Vector3Array):
            raise TypeError('points must be Vector3Array')
        if not points:
            raise ValueError('must have at least 1 point')
        self._points = points

    def __hash__(self) -> int:
        return id(self)

    def __eq__(self, other: ConvexHull) -> bool:
        if not isinstance(other, ConvexHull):
            return False
        return self._points == other._points

    def __repr__(self) -> str:
        return f'<gamut.geometry.ConvexHull>'

    def __rmatmul__(self, transform: Matrix4) -> ConvexHull:
        if not isinstance(transform, Matrix4):
            return NotImplemented

        return ConvexHull(Vector3Array(*(transform @ c for c in self._points)))

    @property
    def points(self) -> Vector3Array:
        return self._points
