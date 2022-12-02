
from __future__ import annotations

__all__ = ['Triangle3d']

# gamut
from ._boundingbox3d import BoundingBox3d
from ._error import DegenerateGeometryError
from ._linesegment3d import LineSegment3d
from ._plane import Plane
from ._triangle2d import Triangle2d
# gamut
from gamut.math import DMatrix4, DVector3, FMatrix4, FVector3
# python
from math import copysign, inf, isnan
from typing import Generic, NamedTuple, overload, Type, TypeVar

T = TypeVar('T', FVector3, DVector3)


class Triangle3d(Generic[T]):

    class DegenerateError(DegenerateGeometryError):
        degenerate_form: LineSegment3d[T] | T

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

        d_edge_0 = self._positions[1] - self._positions[0]
        d_edge_1 = self._positions[0] - self._positions[2]
        self._normal = -d_edge_0.cross(d_edge_1).normalize()

        if isnan(self._normal.x):
            raise self.DegenerateError(
                self._get_degenerate_form(),
                'degenerate triangle'
            )

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

    def _get_degenerate_form(self) -> T | LineSegment3d[T] | None:
        unique_points = set(self._positions)
        if len(unique_points) == 1:
            return next(iter(unique_points))
        elif len(unique_points) == 2:
            a, b = unique_points
            for edge in self.edges:
                if (
                    (edge.a == a and edge.b == b) or
                    (edge.a == b and edge.b == a)
                ):
                    return edge
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
        return LineSegment3d(seg[0], seg[1])

    @property
    def bounding_box(self) -> BoundingBox3d:
        return BoundingBox3d(self._positions[0].get_array_type()(
            *self._positions
        ))

    @property
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

    @property
    def normal(self) -> T:
        return self._normal

    @property
    def plane(self) -> Plane:
        normal = self.normal
        return Plane(-normal @ self._positions[0], normal)

    @property
    def positions(self) -> tuple[T, T, T]:
        return self._positions

    @property
    def vector_type(self) -> Type[T]:
        return type(self._positions[0])

    def get_edge_for_points(self, a: T, b: T) -> LineSegment3d[T]:
        for edge in self.edges:
            if (edge.a == a and edge.b == b) or (edge.a == b and edge.b == a):
                return edge
        raise ValueError(
            'one or more points are not a position of the triangle'
        )

    def get_edges_for_point(
        self,
        point: T
    ) -> tuple[LineSegment3d[T], LineSegment3d[T]]:
        if point == self._positions[0]:
            return (
                LineSegment3d(self._positions[2], self._positions[0]),
                LineSegment3d(self._positions[0], self._positions[1]),
            )
        if point == self._positions[1]:
            return (
                LineSegment3d(self._positions[0], self._positions[1]),
                LineSegment3d(self._positions[1], self._positions[2]),
            )
        if point == self._positions[2]:
            return (
                LineSegment3d(self._positions[1], self._positions[2]),
                LineSegment3d(self._positions[2], self._positions[0]),
            )
        raise ValueError('point is not a position of the triangle')

    def get_edge_opposite_of_point(self, point: T) -> LineSegment3d[T]:
        if point == self._positions[0]:
            return LineSegment3d(self._positions[1], self._positions[2])
        if point == self._positions[1]:
            return LineSegment3d(self._positions[2], self._positions[0])
        if point == self._positions[2]:
            return LineSegment3d(self._positions[0], self._positions[1])
        raise ValueError('point is not a position of the triangle')

    def get_point_opposite_of_edge(self, edge: LineSegment3d[T]) -> T:
        edges = self.edges
        if edge == edges[0]:
            return self._positions[2]
        if edge == edges[1]:
            return self._positions[0]
        if edge == edges[2]:
            return self._positions[1]
        raise ValueError('edge is not an edge of the triangle')

    def get_edge_normal(self, edge: LineSegments3d[T]) -> T:
        for i, match_edge in enumerate(self.edges):
            if edge == match_edge:
                return self.edge_normals[i]
        raise ValueError('edge is not part of triangle')

    @overload
    def project_orthographic(
        self: Triangle3d[FVector3]
    ) -> Triangle2d[FVector2]:
        ...

    @overload
    def project_orthographic(
        self: Triangle3d[DVector3]
    ) -> Triangle2d[DVector2]:
        ...

    def project_orthographic(self) -> Triangle2d:
        Matrix4 = FMatrix4 if self.vector_type is FVector3 else DMatrix4
        up = self.vector_type(0, 1, 0)
        eye = -self.normal
        if abs(up @ eye) == 1.0:
            up = self.vector_type(0, 0, -1)
            eye = -eye
            assert abs(up @ eye) != 1.0
        view = Matrix4.look_at(self.vector_type(0), eye, up)
        projection = Matrix4.orthographic(-1, 1, -1, 1, -1, 1)
        vp = projection @ view.inverse()
        return Triangle2d(*(
            (vp @ p.xyzl).xy
            for p in self._positions
        ))

    def intersects_line_segment(
        self,
        line_segment: LineSegment3d[T],
        *,
        tolerance: float = 0.0
    ) -> bool:
        # check points intersecting
        for point in (line_segment.a, line_segment.b):
            if self.intersects_point(point, tolerance=tolerance):
                return True
        # check edges intersecting
        for edge in self.edges:
            if edge.intersects_line_segment(line_segment, tolerance=tolerance):
                return True
        return False

    def intersects_triangle_3d(
        self,
        other: Triangle3d[T],
        *,
        tolerance: float = 0.0
    ) -> bool:
        # broad aabb check
        if not self.bounding_box.intersects_bounding_box_3d(
            other.bounding_box,
            tolerance=tolerance
        ):
            return False
        # narrow plane/point check
        # if there are points on either side of the plane or a point inside
        # the plane then we may be intersecting
        plane = self.plane
        last_side = None
        for i, point in enumerate(other.positions):
            distance = plane.signed_distance_to_point(point)
            if abs(distance) <= tolerance:
                if last_side is not None:
                    break
                continue
            if last_side is None:
                if i != 0:
                    break
                last_side = copysign(1, distance)
            elif copysign(1, distance) != last_side:
                break
            assert(copysign(1, distance) == last_side)
        else:
            if last_side is None:
                self_2d = self.project_orthographic()
                other_2d = other.project_orthographic()
                return self_2d.intersects_triangle_2d(
                    other_2d,
                    tolerance=tolerance
                )
            return False
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

                half_a_diff = (max_a - min_a) * .5
                min_b -= half_a_diff
                max_b += half_a_diff

                idk = (min_a + max_a) * .5
                dmin = min_b - idk
                dmax = max_b - idk

                if dmin > tolerance or dmax < -tolerance:
                    return False
        return True

    def get_projected_barycentric_point_from_cartesian(
        self,
        cartesian_point: T
    ) -> T:
        if not isinstance(cartesian_point, self.vector_type):
            raise TypeError(f'cartesian_point must be {self.vector_type}')
        v0 = self._positions[2] - self._positions[0]
        v1 = self._positions[1] - self._positions[0]
        v2 = cartesian_point - self._positions[0]
        dot00 = v0 @ v0
        dot01 = v0 @ v1
        dot02 = v0 @ v2
        dot11 = v1 @ v1
        dot12 = v1 @ v2
        inv_denom = 1.0 / (dot00 * dot11 - dot01 * dot01)
        w = (dot11 * dot02 - dot01 * dot12) * inv_denom
        v = (dot00 * dot12 - dot01 * dot02) * inv_denom
        u = 1.0 - w - v
        return self.vector_type(u, v, w)

    def get_cartesian_point_from_barycentric(
        self,
        barycentric_point: T
    ) -> T:
        if not isinstance(barycentric_point, self.vector_type):
            raise TypeError(f'barycentric_point must be {self.vector_type}')
        return (
            barycentric_point.x * self._positions[0] +
            barycentric_point.y * self._positions[1] +
            barycentric_point.z * self._positions[2]
        )

    def where_intersected_by_point(
        self,
        point: T,
        *,
        tolerance: float = 0.0
    ) -> T | None:
        if not isinstance(point, self.vector_type):
            raise TypeError(f'point must be {self.vector_type.__name__}')
        # quick check to make sure the point lies in the triangle's plane
        if abs(self.plane.signed_distance_to_point(point)) > tolerance:
            return None
        # solve for the point's projected barycentric coordinates which can
        # tell us whether the projected point is in the triangle
        b_point = self.get_projected_barycentric_point_from_cartesian(point)
        if any(c < 0 for c in b_point):
            # projected point is not in the triangle, so the real point must
            # not be
            if tolerance == 0:
                # tolerance of 0 means no futher checks are needed, the point
                # isn't in the tri so it can't be intersecting
                return None
            # since we know the point is outside the tri we can check if any
            # edges are intersecting it, given the tolerance
            if not intersection_points:
                for edge in self.edges:
                    intersection = edge.where_intersected_by_point(
                        point,
                        tolerance=tolerance
                    )
                    if intersection is not None:
                        return intersection
            return None
        # projected point is in the triangle, converting it to cartesian will
        # gives us the result
        return self.get_cartesian_point_from_barycentric(b_point)

    def where_intersected_by_line_segment(
        self,
        line: LineSegment3d[T],
        *,
        tolerance: float = 0.0
    ) -> LineSegment3d[T] | T | None:
        if (
            not isinstance(line, LineSegment3d) or
            not isinstance(line.a, type(self._positions[0]))
        ):
            raise TypeError(
                f'line must be LineSegment3d'
                f'[{type(self._positions[0]).__name__}]'
            )
        # get the intersection of the line with the triangle's plane
        plane_intersection = self.plane.where_intersected_by_line_segment(
            line,
            tolerance=tolerance
        )
        if plane_intersection is None:
            return None
        if isinstance(plane_intersection, LineSegment3d):
            # the line segment is coplanar with the triangle, check for
            # intersections on each edge
            edge_intersections = []
            for edge in self.edges:
                edge_intersection = edge.where_intersected_by_line_segment(
                    plane_intersection,
                    tolerance=tolerance
                )
                if edge_intersection is not None:
                    # any segment intersection will be the result, any other
                    # intersections should be points on the same segment
                    if isinstance(edge_intersection, LineSegment3d):
                        return edge_intersection
                    edge_intersections.append(edge_intersection)
            if not edge_intersections:
                return None
            assert all(
                isinstance(ei, type(self._positions[0]))
                for ei in edge_intersections
            )
            if len(edge_intersections) == 1:
                return edge_intersections[0]
            # two points make a segment
            assert len(edge_intersections) == 2
            intersection = LineSegment3d(*edge_intersections)
            if intersection.is_degenerate:
                return intersection.degenerate_form
            return intersection
        assert isinstance(plane_intersection, type(self._positions[0]))
        return self.where_intersected_by_point(
            plane_intersection,
            tolerance=tolerance
        )

    def where_intersected_by_plane(
        self,
        plane: Plane[T],
        *,
        tolerance: float = 0.0
    ) -> Triangle3d[T] | LineSegment3d[T] | T | None:
        if (
            not isinstance(plane, Plane) or
            not isinstance(plane.normal, type(self._positions[0]))
        ):
            raise TypeError(
                f'plane must be Plane[{type(self._positions[0]).__name__}]'
            )
        # check each edge of the tri
        intersections = []
        for edge in self.edges:
            intersection = edge.where_intersected_by_plane(
                plane,
                tolerance=tolerance
            )
            if intersection is not None:
                intersections.append(intersection)
        if not intersections:
            return None
        if len(intersections) == 1:
            # 1 intersection is either a single point or segment
            return intersections[0]
        if len(intersections) == 2:
            # if there are just two intersections and one of them is a line
            # segment then we can assume that is the actual intersection (the
            # extra is almost certainly a point from a shared edge)
            for intersection in intersections:
                if isinstance(intersection, LineSegment3d):
                    return intersection
            assert all(
                isinstance(i, type(self._positions[0]))
                for i in intersections
            )
            # two points make a segment
            intersection = LineSegment3d(*intersections)
            if intersection.is_degenerate:
                return intersection.degenerate_form
            return intersection
        assert len(intersections) == 3
        # there are basically two conditions here, either we have a single line
        # segment and some points "extra" points or we have 3 line segments
        if all(isinstance(i, LineSegment3d) for i in intersections):
            return self
        for intersection in intersections:
            if isinstance(intersection, LineSegment3d):
                return intersection
        assert False

    def where_intersected_by_triangle(
        self,
        other: Triangle3d[T],
        *,
        tolerance: float = 0.0
    ) -> Triangle3d[T] | LineSegment3d[T] | T | None:
        # handle degenerate triangles
        if self.is_degenerate:
            degen_form = self.degenerate_form
            if isinstance(degen_form, LineSegment3d):
                return degen_form.where_intersected_by_triangle3d(
                    other,
                    tolerance=tolerance
                )
            assert isinstance(degen_form, type(t1._positions[0]))

        # check plane intersection first, which gives us most of the results
        # most of the time (when the triangles aren't on the same plane)
        plane_intersection = self.where_intersected_by_plane(other.plane)
        if plane_intersection is None:
            return None
        if isinstance(plane_intersection, Triangle3d):
            assert plane_intersection is self
            return self._where_intersected_by_same_plane_triangle(
                other,
                tolerance=tolerance
            )
        if isinstance(plane_intersection, LineSegment3d):
            return self.where_intersected_by_line_segment(plane_intersection)
        assert isinstance(plane_intersection, type(self._positions[0]))
        if self.intersects_point(plane_intersection, tolerance=tolerance):
            return plane_intersection
        return None

    def _where_intersected_by_same_plane_triangle(
        self,
        other: Triangle3d[T],
        *,
        tolerance: float = 0.0
    ) -> Triangle3d[T] | LineSegment3d[T] | T | None:
        pass
