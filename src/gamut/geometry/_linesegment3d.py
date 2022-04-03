
from __future__ import annotations

__all__ = ['LineSegment3d']

# gamut
from gamut.math import Vector3


class LineSegment3d:

    def __init__(self, a: Vector3, b: Vector3):
        if not isinstance(a, Vector3):
            raise TypeError('a must be Vector3')
        self._a = a

        if not isinstance(b, Vector3):
            raise TypeError('b must be Vector3')
        self._b = b

        self._diff = b - a


    def __hash__(self) -> int:
        return id(self)

    def __repr__(self) -> str:
        return (
            f'<gamut.geometry.LineSegment3d {tuple(self._a)} to '
            f'{tuple(self._b)}>'
        )

    def __eq__(self, other: LineSegment3d) -> bool:
        if not isinstance(other, LineSegment3d):
            return False
        return (
            (self._a == other._a and self._b == other._b) or
            (self._a == other._b and self._b == other._a)
        )

    @property
    def a(self) -> Vector3:
        return self._a

    @property
    def b(self) -> Vector3:
        return self._b

    def get_point_along_line(self, t: float) -> Vector2:
        return self._a + (t * self._diff)
