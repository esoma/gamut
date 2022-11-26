
from __future__ import annotations

__all__ = ['Triangle3d']

# gamut
from ._boundingbox3d import BoundingBox3d
from ._linesegment3d import LineSegment3d
from ._plane import Plane
# gamut
from gamut.math import DVector3, FVector3
# python
from math import copysign, inf
from typing import Generic, TypeVar

T = TypeVar('T', FVector3, DVector3)


class Triangle3d(Generic[T]):

    def __init__(self, point_0: T, point_1: T, point_2: T, /):
        if not isinstance(point_0, (FVector3, DVector3)):
            raise TypeError('point 0 must be FVector3 or DVector3')
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
            f'<gamut.geometry.Triangle3d '
            f'{tuple(tuple(p) for p in self._positions)}>'
        )

    def __eq__(self, other: Triangle3d) -> bool:
        if not isinstance(other, Triangle3d):
            return False
        return self._positions == other._positions

    @property
    def bounding_box(self) -> BoundingBox3d:
        return BoundingBox3d(self._positions[0].get_array_type()(
            *self._positions
        ))

    def center(self) -> T:
        return sum(self._positions) / 3

    @property
    def edges(self) -> tuple[
        LineSegment3d[T],
        LineSegment3d[T],
        LineSegment3d[T]
    ]:
        return (
            LineSegment3d(self._positions[0], self._positions[1]),
            LineSegment3d(self._positions[1], self._positions[2]),
            LineSegment3d(self._positions[2], self._positions[0]),
        )

    @property
    def edge_normals(self) -> tuple[T, T, T]:
        p = self._positions
        normal = self.normal
        return (
            (p[1] - p[0]).cross(normal).normalize(),
            (p[2] - p[1]).cross(normal).normalize(),
            (p[0] - p[2]).cross(normal).normalize(),
        )

    def get_edge_normal(self, edge: LineSegments3d[T]) -> T:
        for i, match_edge in enumerate(self.edges):
            if edge == match_edge:
                return self.edge_normals[i]
        raise ValueError('edge is not part of triangle')

    def normal(self) -> T:
        d_edge_0 = self._positions[1] - self._positions[0]
        d_edge_1 = self._positions[0] - self._positions[2]
        return -d_edge_0.cross(d_edge_1).normalize()

    @property
    def plane(self) -> Plane:
        normal = self.normal
        return Plane(normal @ self._positions[0], normal)

    @property
    def positions(self) -> tuple[T, T, T]:
        return self._positions

    def project_ortho(self) -> None:
        p1mp0 = self._positions[1] - self._positions[0]
        p2mp0 = self._positions[2] - self._positions[0]
        ox = (p1mp0).normalize()
        oz = ox.cross(p2mp0).normalize()
        oy = oz.cross(ox)

        p0 = self._positions[0].x
        ptype = type(p0)
        p1 = ptype(p1mp0.magnitude, 0)
        p2 = ptype(p2mp0 @ ox, p2mp0 @ oy)
        return p0, p1, p2

    def intersects_triangle_3d(
        self,
        other: Triangle3d[T],
        *,
        tolerance: float = 0.0
    ) -> bool:
        # broad aabb check
        if not self.bounding_box.intersects_bounding_box_3d_inclusive(
            other.bounding_box
        ):
            return False
        print("AABB passed")
        # narrow plane/point check
        # if there are points on either side of the plane or a point inside
        # the plane then we may be intersecting
        plane = self.plane
        last_side = None
        for point in other.positions:
            distance = plane.distance_to_point(point)
            if abs(distance) <= tolerance:
                break
            elif last_side is None:
                last_side = copysign(1, distance)
            elif copysign(1, distance) != last_side:
                break
            assert(copysign(1, distance) == last_side)
        else:
            return False
        if last_side is None:
            print("2D")
        print("PLANE PASSED")
        # SAT theorem
        for a_edge in self.edges:
            a_axis = (a_edge.a - a_edge.b).normalize()
            for b_edge in other.edges:
                b_axis = (b_edge.a - b_edge.b).normalize()

                sep_axis = a_axis.cross(b_axis)
                if sep_axis == type(sep_axis)():
                    continue
                sep_axis = sep_axis.normalize()

                min_a = min_b = inf
                max_a = max_b = -inf

                for a_pos, b_pos in zip(self.positions, other.positions):
                    d = sep_axis @ a_pos
                    min_a = min(min_a, d)
                    max_a = max(max_a, d)

                    d = sep_axis @ b_pos
                    min_b = min(min_b, d)
                    max_b = max(max_b, d)

                print(min_a, max_a, min_b, max_b)
                half_a_diff = (max_a - min_a) * .5
                min_b -= half_a_diff
                max_b += half_a_diff

                idk = (min_a + max_a) * .5
                dmin = min_b - idk
                dmax = max_b - idk

                if dmin > tolerance or dmax < -tolerance:
                    return False
        return True
