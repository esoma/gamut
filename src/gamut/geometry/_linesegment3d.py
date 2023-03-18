
from __future__ import annotations

__all__ = ['LineSegment3d']

# gamut
from ._error import DegenerateGeometryError
# gamut
from gamut.math import DVector3, FVector3
# python
from math import hypot
from typing import Generic, TypeVar

T = TypeVar('T', FVector3, DVector3)


class LineSegment3d(Generic[T]):

    class DegenerateError(DegenerateGeometryError):
        degenerate_form: T

    def __init__(self, a: T, b: T):
        if not isinstance(a, (FVector3, DVector3)):
            raise TypeError('a must be FVector3 or DVector3')
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
            f'<gamut.geometry.LineSegment3d {tuple(self._a)} to '
            f'{tuple(self._b)}>'
        )

    def __eq__(self, other: LineSegment3d) -> bool:
        if not isinstance(other, LineSegment3d):
            return False
        return self._a == other._a and self._b == other._b

    @property
    def a(self) -> T:
        return self._a

    @property
    def b(self) -> T:
        return self._b

    def get_distance_to_point(self, point: T) -> float:
        d = self._slope.normalize()
        s = (self._a - point) @ d
        t = (point - self._b) @ d
        h = max(s, t, 0)
        c = (point - self._a).cross(d)
        return hypot(*c, h)

    def get_point_from_a_to_b(self, t: float) -> T:
        return self._a + (t * self._slope)

    def get_point_from_b_to_a(self, t: float) -> T:
        t = -(t - 1)
        return self.get_point_from_a_to_b(t)
