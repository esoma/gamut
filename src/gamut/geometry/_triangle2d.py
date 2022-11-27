
from __future__ import annotations

__all__ = ['Triangle2d']

# gamut
from ._boundingbox2d import BoundingBox2d
from ._linesegment2d import LineSegment2d
# gamut
from gamut.math import DVector2, FVector2
# python
from math import inf
from typing import Generic, TypeVar

T = TypeVar('T', FVector2, DVector2)


class Triangle2d(Generic[T]):

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

    @property
    def positions(self) -> tuple[T, T, T]:
        return self._positions

    def intersects_triangle_2d(
        self,
        other: Triangle2d[T],
        *,
        tolerance: float = 0.0
    ) -> bool:
        # broad aabb check
        if not self.bounding_box.intersects_bounding_box_2d_inclusive(
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
