
from __future__ import annotations

__all__ = ['Triangle2d']

# gamut
from ._boundingbox2d import BoundingBox2d
from ._error import DegenerateGeometryError
from ._linesegment2d import LineSegment2d
# gamut
from gamut.math import DVector2, FVector2
# python
from math import inf
from typing import Generic, TypeVar

T = TypeVar('T', FVector2, DVector2)


class Triangle2d(Generic[T]):

    class DegenerateError(DegenerateGeometryError):
        degenerate_form: LineSegment2d[T] | T

    def __init__(self, point_0: T, point_1: T, point_2: T, /):
        if not isinstance(point_0, (FVector2, DVector2)):
            raise TypeError('point 0 must be FVector2 or DVector2')
        if not isinstance(point_1, type(point_0)):
            raise TypeError('point 1 must be the same type as point 0')
        if not isinstance(point_2, type(point_0)):
            raise TypeError('point 2 must be the same type as point 0')

        self._positions = (point_0, point_1, point_2)
        i = sorted(enumerate(self._positions), key=lambda x: x[1])[0][0]
        self._positions = self._positions[i:] + self._positions[:i]

        degenerate_form = self._get_degenerate_form()
        if degenerate_form is not None:
            raise self.DegenerateError(degenerate_form, 'degenerate triangle')

    def __hash__(self) -> int:
        return hash(self._positions)

    def __repr__(self) -> str:
        return (
            f'<gamut.geometry.Triangle2d '
            f'{tuple(tuple(p) for p in self._positions)}>'
        )

    def __eq__(self, other: Triangle2d) -> bool:
        if not isinstance(other, Triangle2d):
            return False
        return self._positions == other._positions

    @property
    def bounding_box(self) -> BoundingBox2d:
        return BoundingBox2d(self._positions[0].get_array_type()(
            *self._positions
        ))

    @property
    def center(self) -> T:
        return sum(self._positions) / 3

    @property
    def edges(self) -> tuple[
        LineSegment2d[T],
        LineSegment2d[T],
        LineSegment2d[T]
    ]:
        return (
            LineSegment2d(self._positions[0], self._positions[1]),
            LineSegment2d(self._positions[1], self._positions[2]),
            LineSegment2d(self._positions[2], self._positions[0]),
        )

    @property
    def edge_normals(self) -> tuple[T, T, T]:
        c = 1 if self.is_clockwise else -1
        p = self._positions
        v = type(self._positions[0])
        return (
            v(p[1].y - p[0].y, p[0].x - p[1].x).normalize() * c,
            v(p[2].y - p[1].y, p[1].x - p[2].x).normalize() * c,
            v(p[0].y - p[2].y, p[2].x - p[0].x).normalize() * c,
        )

    @property
    def is_clockwise(self) -> bool:
        d_edge_0 = self._positions[1].xyo - self._positions[0].xyo
        d_edge_1 = self._positions[0].xyo - self._positions[2].xyo
        return d_edge_0.cross(d_edge_1).normalize().z < 0

    @property
    def is_counterclockwise(self) -> bool:
        return not self.is_clockwise

    def _get_degenerate_form(self) -> T | LineSegment2d[T] | None:
        unique_points = set(self._positions)
        if len(unique_points) == 1:
            return next(iter(unique_points))
        elif len(unique_points) == 2:
            a, b = unique_points
            for ea, eb in (
                (self._positions[0], self._positions[1]),
                (self._positions[1], self._positions[2]),
                (self._positions[2], self._positions[0]),
            ):
                if (
                    (ea == a and eb == b) or
                    (ea == b and eb == a)
                ):
                    return LineSegment2d(ea, eb)
        edges = self.edges
        if not edges[0].is_parallel_with_line_segment(edges[1]):
            return None
        segment_distance = [
            (a, b, a.distance(b))
            for a, b in (
                (self._positions[0], self._positions[1]),
                (self._positions[1], self._positions[2]),
                (self._positions[2], self._positions[0])
            )
        ]
        segment_distance.sort(key=lambda s: s[2])
        seg = segment_distance[-1]
        return LineSegment2d(seg[0], seg[1])

    @property
    def positions(self) -> tuple[T, T, T]:
        return self._positions

    def get_edge_opposite_of_point(self, point: T) -> LineSegment2d[T]:
        if point == self._positions[0]:
            return LineSegment2d(self._positions[1], self._positions[2])
        if point == self._positions[1]:
            return LineSegment2d(self._positions[2], self._positions[0])
        if point == self._positions[2]:
            return LineSegment2d(self._positions[0], self._positions[1])
        raise ValueError('point is not a position of the triangle')

    def get_point_opposite_of_edge(self, edge: LineSegment2d[T]) -> T:
        edges = self.edges
        if edge == edges[0]:
            return self._positions[2]
        if edge == edges[1]:
            return self._positions[0]
        if edge == edges[2]:
            return self._positions[1]
        raise ValueError('edge is not an edge of the triangle')

    def intersects_point(
        self,
        point: T,
        *,
        tolerance: float = 0.0
    ) -> bool:
        # solve for the points barycentric coordinates
        v0 = self._positions[2] - self._positions[0]
        v1 = self._positions[1] - self._positions[0]
        v2 = point - self._positions[0]
        dot00 = v0 @ v0
        dot01 = v0 @ v1
        dot02 = v0 @ v2
        dot11 = v1 @ v1
        dot12 = v1 @ v2
        inv_denom = 1.0 / (dot00 * dot11 - dot01 * dot01)
        u = (dot11 * dot02 - dot01 * dot12) * inv_denom
        if u < 0:
            return self._intersects_point_not_inside(point, tolerance)
        v = (dot00 * dot12 - dot01 * dot02) * inv_denom
        if v >= 0 and u + v <= 1:
            return True
        return self._intersects_point_not_inside(point, tolerance)

    def _intersects_point_not_inside(self, point: T, tolerance: float) -> bool:
        # checks if the point which has already been calculated to not be
        # inside the tri intersects the tri with a tolerance
        if tolerance == 0:
            # tolerance of 0 means no futher checks are needed, the point isn't
            # in the tri so it can't be intersecting
            return False
        # since we know the point is outside the tri we can check if any edges
        # are intersecting it, given the tolerance
        return any(
            edge.get_distance_to_point(point) <= tolerance
            for edge in self.edges
        )

    def intersects_triangle_2d(
        self,
        other: Triangle2d[T],
        *,
        tolerance: float = 0.0
    ) -> bool:
        # broad aabb check
        if not self.bounding_box.intersects_bounding_box_2d(
            other.bounding_box
        ):
            return False
        # SAT theorem
        for sep_axis in (*self.edge_normals, *other.edge_normals):
            min_a = min_b = inf
            max_a = max_b = -inf
            for a_pos, b_pos in zip(self.positions, other.positions):
                d = sep_axis @ a_pos
                min_a = min(min_a, d)
                max_a = max(max_a, d)

                d = sep_axis @ b_pos
                min_b = min(min_b, d)
                max_b = max(max_b, d)

            half_a_diff = (max_a - min_a) * .5
            min_b -= half_a_diff
            max_b += half_a_diff

            idk = (min_a + max_a) * .5
            dmin = min_b - idk
            dmax = max_b - idk

            if dmin > tolerance or dmax < -tolerance:
                return False
        return True
