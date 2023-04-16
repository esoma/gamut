
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

    def are_points_on_same_side(self, p0: T, p1: T) -> bool:
        bma = self.b - self.a
        cp1 = bma.cross(p0 - self.a)
        cp2 = bma.cross(p1 - self.a)
        return cp1 @ cp2 >= 0

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
            not isinstance(plane.normal, self.vector_type)
        ):
            raise TypeError(
                f'plane must be Plane[{self.vector_type.__name__}]'
            )
        # find the intersection using math :^)
        den = plane.normal @ self._slope
        if den == 0:
            # line segment is parallel to the plane, so any point of the
            # segment will do as an intersection check
            if abs(plane.get_signed_distance_to_point(self.a)) > tolerance:
                return None
            return self
        d = plane.normal @ plane.origin
        t = (d - plane.normal @ self._a) / den
        if tolerance == 0:
            if t < 0 or t > 1:
                return None
        else:
            t = max(min(t, 1), 0)
        p = self._a + t * self._slope
        if tolerance != 0:
            if abs(self.get_distance_to_point(p)) > tolerance:
                return None
        return p

    def where_intersected_by_triangle(
        self,
        tri: Triangle3d[T],
        *,
        tolerance: float = 0.0
    ) -> LineSegment3d[T] | T | None:
        # gamut
        from ._triangle3d import Triangle3d
        if (
            not isinstance(tri, Triangle3d) or
            tri.vector_type is not self.vector_type
        ):
            raise TypeError(
                f'tri must be Triangle3d[{self.vector_type.__name__}]'
            )
        # first check where the segment intersects the plane that the triangle
        # is on
        plane_intersection = self.where_intersected_by_plane(
            tri.plane,
            tolerance=tolerance
        )
        if plane_intersection is None:
            # no plane intersection means no triangle intersection
            return None
        if isinstance(plane_intersection, self.vector_type):
            # point intersection, check if the intersection point is inside
            # the triangle
            b_point = tri.get_projected_barycentric_point_from_cartesian(
                plane_intersection
            )
            if all(c >= 0 for c in b_point):
                # point is in the triangle, this is the intersection
                return plane_intersection
            # point isn't in the triangle, check for intersections against any
            # of the triangle's edges
            for edge in tri.edges:
                if edge.where_intersected_by_point(
                    plane_intersection,
                    tolerance=tolerance
                ) is not None:
                    return plane_intersection
            return None
        # segment intersection
        assert isinstance(plane_intersection, LineSegment3d)
        # check which points of the intersection are in the triangle
        inside_points = [
            p
            for p in (plane_intersection._a, plane_intersection._b)
            if all(
                c >= 0
                for c in tri.get_projected_barycentric_point_from_cartesian(p)
            )
        ]
        if len(inside_points) == 2:
            # all points of the segment are inside the tri, it is the
            # intersection
            return plane_intersection
        if len(inside_points) == 1:
            inside_point = inside_points[0]
            # one point inside and one outside, which means it intersects one
            # of the triangle's edges
            for edge in tri.edges:
                edge_intersection = (
                    plane_intersection.where_intersected_by_line_segment(
                        edge,
                        tolerance=tolerance
                    )
                )
                if edge_intersection is not None:
                    if isinstance(edge_intersection, LineSegment3d):
                        # a segment intersection should share one of its points
                        # with the existing inside point
                        if inside_point == edge_intersection._a:
                            edge_intersection = edge_intersection._b
                        else:
                            assert inside_point == edge_intersection._b
                            edge_intersection = edge_intersection._a
                    assert isinstance(edge_intersection, self.vector_type)
                    # construct the intersection from the edge intersection
                    # point and the plane intersection point inside the
                    # triangle
                    if inside_point == edge_intersection:
                        return inside_point
                    return LineSegment3d(*sorted((
                        inside_point,
                        edge_intersection
                    )))
            # no other intersections, just this point
            return inside_point
        # all points outside
        assert len(inside_points) == 0
        # check where the edges of the triangle intersect with the plane
        # intersections
        intersections: set[T] = set()
        for edge in tri.edges:
            edge_intersection = (
                plane_intersection.where_intersected_by_line_segment(
                    edge,
                    tolerance=tolerance
                )
            )
            if edge_intersection is not None:
                if isinstance(edge_intersection, LineSegment3d):
                    return edge_intersection
                intersections.add(edge_intersection)
        assert len(intersections) < 3
        if not intersections:
            return None
        if len(intersections) == 2:
            return LineSegment3d(*sorted(intersections))
        assert len(intersections) == 1
        return next(iter(intersections))
