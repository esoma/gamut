
from __future__ import annotations

__all__ = ['LineSegment3d']

# gamut
from gamut.math import DVector3, FVector3
# python
from math import hypot, inf
from typing import Generic, TYPE_CHECKING, TypeVar

if TYPE_CHECKING:
    # gamut
    from ._plane import Plane

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

    def distance_to_line_segment(self, other: LineSegment[T]) -> float:
        # handle degenerate line segments
        for l1, l2 in ((self, other), (other, self)):
            if l1.is_degenerate:
                degen_form = l1.degenerate_form
                assert isinstance(degen_form, type(l1._a))
                return l2.distance_to_point(degen_form)
        # math :^)
        d1 = self._b - self._a
        d2 = other._b - other._a
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

    def distance_to_point(self, point: T) -> float:
        # handle degenerate line segment
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

    def intersects_line_segment(
        self,
        other: LineSegment[T],
        *,
        tolerance: float = 0.0
    ):
        return self.distance_to_line_segment(other) <= tolerance

    def is_parallel_with_line_segment(self, other: LineSegment3d[T]) -> bool:
        if self.is_degenerate or other.is_degenerate:
            return False
        ab = self._b - self._a
        cd = other._b - other._a
        return ab.cross(cd) ** 2 <= (ab * ab).cross(cd * cd)

    def where_intersected_by_plane(
        self,
        plane: Plane[T],
        *,
        tolerance: float = 0.0
    ) -> LineSegment3d[T] | T | None:
        # gamut
        from ._plane import Plane
        if (
            not isinstance(plane, Plane) or
            not isinstance(plane.normal, type(self._a))
        ):
            raise TypeError(f'plane must be Plane[{type(self._a).__name__}]')
        # handle degenerate segment
        if self.is_degenerate:
            degen_form = self.degenerate_form
            assert isinstance(degen_form, type(self._a))
            if abs(plane.signed_distance_to_point(degen_form)) <= tolerance:
                return degen_form
        # find the intersection using math :^)
        ab = self._b - self._a
        den = plane.normal @ ab
        if den == 0:
            # line segment is parallel to the plane, so any point of the
            # segment will do as an intersection check
            if abs(plane.signed_distance_to_point(self.a)) > tolerance:
                return None
            return self
        d = plane.normal @ plane.origin
        t = (d - plane.normal @ self._a) / den
        if tolerance == 0:
            if t < 0 or t > 1:
                return None
        else:
            t = max(min(t, 1), 0)
        p = self._a + t * ab
        if tolerance != 0:
            if abs(self.distance_to_point(p)) > tolerance:
                return None
        return p
