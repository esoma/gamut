
from __future__ import annotations

__all__ = ['LineSegment2d']

# gamut
from gamut.math import DVector2, FVector2
# python
from typing import Generic, TypeVar

T = TypeVar('T', FVector2, DVector2)


class LineSegment2d(Generic[T]):

    def __init__(self, a: T, b: T):
        if not isinstance(a, (FVector2, DVector2)):
            raise TypeError('a must be FVector2 or DVector2')
        self._a = a

        if not isinstance(b, type(a)):
            raise TypeError('b must be the same type as a')
        self._b = b

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

    @property
    def slope(self) -> T:
        return self._slope

    def get_distance_to_point(self, point: T) -> float:
        if not isinstance(point, type(self._a)):
            raise TypeError(f'point must be {type(self._a).__name__}')
        t = self._project_point_time(point)
        t = max(min(t, 1), 0)
        p = self._a + t * self.slope
        return point.distance(p)

    def get_line_segment_intersection(
        self,
        other: LineSegment2d
    ) -> tuple[float, float] | None:
        if not isinstance(other, LineSegment2d):
            raise TypeError('other must be LineSegment2d')

        self._slope = self._b - self._a
        other._slope = other._b - other._a

        det = -other._slope.x * self._slope.y + self._slope.x * other._slope.y
        if det == 0:
            return None
        s = (
            (-self._slope.y * (self._a.x - other._a.x) +
            self._slope.x * (self._a.y - other._a.y)) /
            det
        )
        t = (
            (other._slope.x * (self._a.y - other._a.y) -
            other._slope.y * (self._a.x - other._a.x)) /
            det
        )

        if s >= 0 and s <= 1 and t >= 0 and t <= 1:
            return t, s
        return None

    def get_point_from_a_to_b(self, t: float) -> T:
        return self._a + (t * self._slope)

    def get_point_from_b_to_a(self, t: float) -> T:
        t = -(t - 1)
        return self.get_point_from_a_to_b(t)

    def intersects_point(
        self,
        point: T,
        *,
        tolerance: float = 0.0
    ) -> bool:
        return self.get_distance_to_point(point) <= tolerance

    def is_parallel_with_line_segment(self, other: LineSegment2d[T]) -> bool:
        if self.is_degenerate or other.is_degenerate:
            return False
        return (
            -other._slope.x * self._slope.y +
            self._slope.x * other._slope.y
        ) == 0

    def where_intersected_by_line_segment(
        self,
        other: LineSegment2d[T],
        *,
        tolerance=0.0
    ) -> LineSegment2d[T] | T | None:
        # handle degenerate line segments
        if self.is_degenerate:
            # self degenerates to a point
            degen_form = self.degenerate_form
            assert isinstance(degen_form, type(self._a))
            if other.get_distance_to_point(degen_form) <= tolerance:
                return degen_form
            return None
        if other.is_degenerate:
            # other degenerate to a point
            degen_form = other.degenerate_form
            assert isinstance(degen_form, type(self._a))
            # project the point on to the line clamped to the segment
            t = self._project_point_time(degen_form)
            t = max(min(t, 1), 0)
            p = self.get_point_from_a_to_b(t)
            if self.get_distance_to_point(p) <= tolerance:
                return p
            return None
        # handle parallel segments
        ts = self._get_intersection_times_line(other)
        if ts is None:
            # segments are parallel, check if they're part of the same line
            oat = self._project_point_time(other._a)
            oap = self.get_point_from_a_to_b(oat)
            same_line = oap.distance(other._a) <= tolerance
            if same_line:
                # segments are part of the same line, figure out where the
                # points of the other segment intersect this one
                obt = self._project_point_time(other._b)
                if tolerance == 0:
                    oai = oat >= 0 and oat <= 1
                    obi = obt >= 0 and obt <= 1
                    if not oai and not obi:
                        return None
                obp = self.get_point_from_a_to_b(obt)
                if tolerance != 0:
                    oai = self.get_distance_to_point(oap) <= tolerance
                    obi = self.get_distance_to_point(obp) <= tolerance
                    if not oai and not obi:
                        return None
                intersection_points = []
                if oai:
                    if tolerance == 0:
                        intersection_points.append(oap)
                    else:
                        intersection_points.append(
                            self.get_point_from_a_to_b(max(min(oat, 1), 0))
                        )
                if obi:
                    if tolerance == 0:
                        intersection_points.append(obp)
                    else:
                        intersection_points.append(
                            self.get_point_from_a_to_b(max(min(obt, 1), 0))
                        )
                assert intersection_points
                if len(intersection_points) != 2:
                    # only one of the points of other is intersecting, figure
                    # out which point of self makes up the new intersection
                    # segment
                    nit = obt if oai else oat
                    assert nit < 0 or nit > 1
                    if nit < 0:
                        intersection_points.append(self._a)
                    else:
                        intersection_points.append(self._b)
                assert len(intersection_points) == 2
                # it is possible the same line intersection devolves into a
                # single point if the segments share a single point, but the
                # other points don't intersect
                intersection = LineSegment2d(*intersection_points)
                intersection_degen = intersection.degenerate_form
                if intersection_degen is not None:
                    return intersection_degen
                return intersection
            else:
                return None
        # not parallel
        t, s = ts
        if tolerance == 0:
            if t < 0 or t > 1 or s < 0 or s > 1:
                return None
        i = self.get_point_from_a_to_b(max(min(t, 1), 0))
        if tolerance != 0:
            if self.get_distance_to_point(i) > tolerance:
                return None
        return i

    def _get_intersection_times_line(
        self,
        other: LineSegment2d
    ) -> tuple[float, float] | None:
        assert isinstance(other, LineSegment2d)
        assert not self.is_degenerate
        assert not other.is_degenerate

        det = -other._slope.x * self._slope.y + self._slope.x * other._slope.y
        if det == 0:
            return None
        s = (
            (-self._slope.y * (self._a.x - other._a.x) +
            self._slope.x * (self._a.y - other._a.y)) /
            det
        )
        t = (
            (other._slope.x * (self._a.y - other._a.y) -
            other._slope.y * (self._a.x - other._a.x)) /
            det
        )
        return t, s

    def _project_point_time(self, point: T) -> float:
        length_2 = sum(x ** 2 for x in (self._a - self._b))
        if length_2 == 0:
            return self._a.distance(point)
        return ((point - self._a) @ self.slope) / length_2
