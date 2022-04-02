
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

    def intersection(self, other: LineSegment2d) -> Vector2 | None:
        if not isinstance(other, LineSegment2d):
            raise TypeError('other must be LineSegment2d')
        self_diff = self._a - self._b
        other_diff = other._a - other._b

        x_diffs = Vector2(self_diff.x, other_diff.x)
        y_diffs = Vector2(self_diff.y, other_diff.y)

        div = get_vec2_determinant(x_diffs, y_diffs)
        if div == 0:
            return None

        d = Vector2(
            get_vec2_determinant(self._a, self._b),
            get_vec2_determinant(other._a, other._b)
        )
        return Vector2(
            get_vec2_determinant(d, x_diffs) / div,
            get_vec2_determinant(d, y_diffs) / div
        )


def get_vec2_determinant(a: Vector2, b: Vector2) -> float:
    return a[0] * b[1] - a[1] * b[0]
