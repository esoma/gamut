
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

    def is_parallel_with_line_segment(self, other: LineSegment3d[T]) -> bool:
        return (
            self._slope.cross(other._slope) ** 2 <=
            (self._slope * self._slope).cross(other._slope * other._slope)
        )

    def where_intersected_by_point(
        self,
        point: T,
        *,
        tolerance: float = 0.0
    ) -> T | None:
        if not isinstance(point, self.vector_type):
            raise TypeError(f'point must be {self.vector_type.__name__}]')
        projected_point = self.project_point(point, clamped=True)
        if point.distance(projected_point) <= tolerance:
            return projected_point
        return None

    def where_intersected_by_line_segment(
        self,
        other: LineSegment3d[T],
        *,
        tolerance: float = 0.0
    ) -> LineSegment3d[T] | T | None:
        if (
            not isinstance(other, LineSegment3d) or
            not isinstance(other.a, self.vector_type)
        ):
            raise TypeError(
                f'other must be LineSegment3d[{self.vector_type.__name__}]'
            )
        # figure out at which time on each line that the two intersect
        det = -other._slope.x * self._slope.y + self._slope.x * other._slope.y
        if det == 0:
            # lines are parallel
            # we need to check if the segments are part of the same line or not
            # so project a point from one to the other and see if the distance
            # between that point and the projected version are within tolerance
            # (if they are part of the same line the point shouldn't change)
            oat = self.project_point_time(other._a)
            oap = self.get_point_from_a_to_b(oat)
            if oap.distance(other._a) > tolerance:
                # the segments are not part of the same line, there is no
                # intersection
                return None
            # the segments part of the same line so the points that make up
            # the segments can tell us about any intersections
            obt = self.project_point_time(other._b)
            obp = self.get_point_from_a_to_b(obt)
            intersections = [
                self.project_point(op, clamped=True)
                for op in (oap, obp)
                if self.get_distance_to_point(op) <= tolerance
            ]
            if not intersections:
                return None
            if len(intersections) == 1:
                # only one of the points of other is intersecting self, figure
                # out which point of self makes up the new intersection
                # segment
                t = obt if oap == intersections[0] else oat
                if t < 0:
                    intersections.append(self._a)
                else:
                    intersections.append(self._b)
            assert len(intersections) == 2
            # it is possible the same line intersection devolves into a
            # single point if the segments share a single point, but the
            # other points don't intersect
            if intersections[0] == intersections[1]:
                return intersections[0]
            return LineSegment3d(*sorted(intersections))
        # lines are not parallel, find the nearest points on each line and
        # use their distance to find the intersection
        st = (
            (other._slope.x * (self._a.y - other._a.y) -
            other._slope.y * (self._a.x - other._a.x)) /
            det
        )
        ot = (
            (-self._slope.y * (self._a.x - other._a.x) +
            self._slope.x * (self._a.y - other._a.y)) /
            det
        )
        st = max(min(st, 1), 0)
        ot = max(min(ot, 1), 0)
        sp = self.get_point_from_a_to_b(st)
        op = other.get_point_from_a_to_b(ot)
        if sp.distance(op) > tolerance:
            return None
        return sp
