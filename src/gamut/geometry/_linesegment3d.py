
from __future__ import annotations

__all__ = ['LineSegment3d']

# gamut
from gamut.math import DVector3, FVector3
# python
from math import hypot
from typing import Generic, TypeVar

T = TypeVar('T', FVector3, DVector3)


class LineSegment3d(Generic[T]):

    def __init__(self, a: T, b: T):
        if not isinstance(a, (FVector3, DVector3)):
            raise TypeError('a must be FVector3 or DVector3')
        self._a = a

        if not isinstance(b, type(a)):
            raise TypeError('b must be the same type as a')
        self._b = b

        self._diff = b - a

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
    def is_degenerate(self) -> bool:
        return self._a == self._b

    @property
    def degenerate_form(self) -> T | None:
        if not self.is_degenerate:
            return None
        return self._a

    @property
    def points(self) -> tuple[T, T]:
        return (self._a, self._b)

    def are_points_on_same_side(self, p0: T, p1: T) -> bool:
        bma = self.b - self.a
        cp1 = bma.cross(p0 - self.a)
        cp2 = bma.cross(p1 - self.a)
        return cp1 @ cp2 >= 0

    def get_point_from_a_to_b(self, t: float) -> T:
        return self._a + (t * self._diff)

    def get_point_from_b_to_a(self, t: float) -> T:
        t = -(t - 1)
        return self.get_point_from_a_to_b(t)

    def distance_to_point(self, point: VT) -> float:
        # handle degenerate line segments
        if self.is_degenerate:
            degen_form = self.degenerate_form
            assert isinstance(degen_form, type(self._a))
            return point.distance(degen_form)
        # math :^)
        bma = self._b - self._a
        d = bma.normalize()
        s = (self._a - point) @ d
        t = (point - self._b) @ d
        h = max(s, t, 0)
        c = (point - self._a).cross(d)
        return hypot(*c, h)

    def intersects_point(
        self,
        point: T,
        *,
        tolerance: float = 0.0
    ) -> bool:
        return self.distance_to_point(point) <= tolerance
