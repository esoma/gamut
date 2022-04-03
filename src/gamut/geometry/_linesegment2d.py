
from __future__ import annotations

__all__ = ['LineSegment2d']

# gamut
from gamut.math import Vector2


class LineSegment2d:

    def __init__(self, a: Vector2, b: Vector2):
        if not isinstance(a, Vector2):
            raise TypeError('a must be Vector2')
        self._a = a

        if not isinstance(b, Vector2):
            raise TypeError('b must be Vector2')
        self._b = b

        self._diff = b - a


    def __hash__(self) -> int:
        return id(self)

    def __repr__(self) -> str:
        return (
            f'<gamut.geometry.LineSegment2d {tuple(self._a)} to '
            f'{tuple(self._b)}>'
        )

    def __eq__(self, other: LineSegment2d) -> bool:
        if not isinstance(other, LineSegment2d):
            return False
        return (
            (self._a == other._a and self._b == other._b) or
            (self._a == other._b and self._b == other._a)
        )

    @property
    def a(self) -> Vector2:
        return self._a

    @property
    def b(self) -> Vector2:
        return self._b

    def get_line_segment_intersection(
        self,
        other: LineSegment2d
    ) -> tuple[float, float] | None:
        if not isinstance(other, LineSegment2d):
            raise TypeError('other must be LineSegment2d')

        self._diff = self._b - self._a
        other._diff = other._b - other._a

        div = -other._diff.x * self._diff.y + self._diff.x * other._diff.y
        if div == 0:
            return None
        s = (
            (-self._diff.y * (self._a.x - other._a.x) +
            self._diff.x * (self._a.y - other._a.y)) /
            div
        )
        t = (
            (other._diff.x * (self._a.y - other._a.y) -
            other._diff.y * (self._a.x - other._a.x)) /
            div
        )

        if s >= 0 and s <= 1 and t >= 0 and t <= 1:
            return t, s
        return None

    def get_point_along_line(self, t: float) -> Vector2:
        return self._a + (t * self._diff)
