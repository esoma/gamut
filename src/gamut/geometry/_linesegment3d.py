
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

    @property
    def vector_type(self) -> Type[T]:
        return type(self._a)

    def get_distance_to_point(self, point: T) -> float:
        d = self._slope.normalize()
        s = (self._a - point) @ d
        t = (point - self._b) @ d
        h = max(s, t, 0)
        c = (point - self._a).cross(d)
        return hypot(*c, h)

    def get_distance_to_line_segment(self, other: LineSegment[T]) -> float:
        # math :^)
        d1 = self._slope
        d2 = other._slope
        r = self._a - other._a
        a = d1 @ d1
        e = d2 @ d2
        f = d2 @ r
        c = d1 @ r
        b = d1 @ d2
        denom = a * e - b * b
        if denom != 0.0:
            s = max(min((b * f - c * e) / denom, 1.0), 0.0)
        else:
            s = 0.0
        t = (b * s + f) / e
        if t < 0:
            t = 0
            s = max(min(-c / a, 1.0), 0.0)
        elif t > 1:
            t = 1
            s = max(min((b - c) / a, 1.0), 0.0)
        c1 = self._a + d1 * s
        c2 = other._a + d2 * t
        return c1.distance(c2)

    def get_point_from_a_to_b(self, t: float) -> T:
        return self._a + (t * self._slope)

    def get_point_from_b_to_a(self, t: float) -> T:
        t = -(t - 1)
        return self.get_point_from_a_to_b(t)

    def project_point_time(self, point: T) -> float:
        if not isinstance(point, self.vector_type):
            raise TypeError(f'point must be {self.vector_type.__name__}]')
        ap = point - self._a
        return (ap @ self._slope) / (self._slope @ self._slope)

    def project_point(
        self,
        point: T,
        *,
        clamped: bool = False
    ) -> T:
        t = self.project_point_time(point)
        if clamped:
            t = max(min(t, 1), 0)
        return self._a + t * self._slope
