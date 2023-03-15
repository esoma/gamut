
from __future__ import annotations

__all__ = ['LineSegment2d']

# gamut
from ._error import DegenerateGeometryError
# gamut
from gamut.math import DVector2, FVector2
# python
from typing import Generic, TypeVar

T = TypeVar('T', FVector2, DVector2)


class LineSegment2d(Generic[T]):

    class DegenerateError(DegenerateGeometryError):
        degenerate_form: T

    def __init__(self, a: T, b: T):
        if not isinstance(a, (FVector2, DVector2)):
            raise TypeError('a must be FVector2 or DVector2')
        self._a = a

        if not isinstance(b, type(a)):
            raise TypeError('b must be the same type as a')
        self._b = b

        if a == b:
            raise self.DegenerateError(a, 'degenerate line segment')

        self._slope = b - a

    def __hash__(self) -> int:
        return hash((self._a, self._b))

    def __repr__(self) -> str:
        return (
            f'<gamut.geometry.LineSegment2d {tuple(self._a)} to '
            f'{tuple(self._b)}>'
        )

    def __eq__(self, other: LineSegment2d) -> bool:
        if not isinstance(other, LineSegment2d):
            return False
        return self._a == other._a and self._b == other._b

    @property
    def a(self) -> T:
        return self._a

    @property
    def b(self) -> T:
        return self._b

    @property
    def points(self) -> tuple[T, T]:
        return (self._a, self._b)

    @property
    def slope(self) -> T:
        return self._slope

    def get_line_segment_intersection(
        self,
        other: LineSegment2d
    ) -> tuple[float, float] | None:
        if not isinstance(other, LineSegment2d):
            raise TypeError('other must be LineSegment2d')

        div = -other._slope.x * self._slope.y + self._slope.x * other._slope.y
        if div == 0:
            return None
        s = (
            (-self._slope.y * (self._a.x - other._a.x) +
            self._slope.x * (self._a.y - other._a.y)) /
            div
        )
        t = (
            (other._slope.x * (self._a.y - other._a.y) -
            other._slope.y * (self._a.x - other._a.x)) /
            div
        )

        if s >= 0 and s <= 1 and t >= 0 and t <= 1:
            return t, s
        return None

    def get_point_from_a_to_b(self, t: float) -> T:
        return self._a + (t * self._slope)

    def get_point_from_b_to_a(self, t: float) -> T:
        t = -(t - 1)
        return self.get_point_from_a_to_b(t)
