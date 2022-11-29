
from __future__ import annotations

__all__ = ['Triangle3d']

# gamut
from ._boundingbox3d import BoundingBox3d
from ._linesegment3d import LineSegment3d
from ._plane import Plane
from ._triangle2d import Triangle2d
# gamut
from gamut.math import DMatrix4, DVector3, FMatrix4, FVector3
# python
from math import copysign, inf, isnan
from typing import Generic, overload, TypeVar

T = TypeVar('T', FVector3, DVector3)


class Triangle3d(Generic[T]):

    class DegenerateError(RuntimeError):
        pass

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
    def degenerate_form(self) -> T | LineSegment3d[T] | None:
        if not self.is_degenerate:
            return None
        unique_points = set(self._positions)
        if len(unique_points) == 1:
            return next(iter(unique_points))
        elif len(unique_points) == 2:
            return LineSegment3d(*unique_points)
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
    def is_degenerate(self) -> bool:
        return isnan(self.normal.x)

    @property
    def normal(self) -> T:
        d_edge_0 = self._positions[1] - self._positions[0]
        d_edge_1 = self._positions[0] - self._positions[2]
        return -d_edge_0.cross(d_edge_1).normalize()

    @property
    def plane(self) -> Plane:
        normal = self.normal
        return Plane(-normal @ self._positions[0], normal)

    @property
    def positions(self) -> tuple[T, T, T]:
        return self._positions

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

    def get_edge_normal(self, edge: LineSegments3d[T]) -> T:
        for i, match_edge in enumerate(self.edges):
            if edge == match_edge:
                return self.edge_normals[i]
        raise ValueError('edge is not part of triangle')

    def project_orthographic(self) -> Triangle2d:
        if self.is_degenerate:
            raise self.DegenerateError(
                'unable to orthographically project a degenerate triangle'
            )
        Vector3 = type(self._positions[0])
        Matrix4 = FMatrix4 if Vector3 is FVector3 else DMatrix4
        up = Vector3(0, 1, 0)
        eye = -self.normal
        if abs(up @ eye) == 1.0:
            up = Vector3(0, 0, -1)
            eye = -eye
            assert abs(up @ eye) != 1.0
        view = Matrix4.look_at(Vector3(0), eye, up)
        projection = Matrix4.orthographic(-1, 1, -1, 1, -1, 1)
        vp = projection @ view.inverse()
        return Triangle2d(*(
            (vp @ p.xyzl).xy
            for p in self._positions
        ))

    def intersects_point(
        self,
        point: T,
        *,
        tolerance: float = 0.0
    ) -> bool:
        # handle degenerate triangles
        if self.is_degenerate:
            degen_form = self.degenerate_form
            if isinstance(degen_form, LineSegment3d):
                return degen_form.intersects_point(
                    point,
                    tolerance=tolerance
                )
            assert isinstance(degen_form, type(self._positions[0]))
            if tolerance == 0:
                return degen_form == point
            return degen_form.distance(point) <= tolerance
        # make sure the point lies in the triangle's plane
        if abs(self.plane.signed_distance_to_point(point)) > tolerance:
            return False
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
            edge.intersects_point(point, tolerance=tolerance)
            for edge in self.edges
        )

    def intersects_line_segment(
        self,
        line_segment: LineSegment3d[T],
        *,
        tolerance: float = 0.0
    ) -> bool:
        # handle degenerate triangle
        if self.is_degenerate:
            degen_form = self.degenerate_form
            if isinstance(degen_form, LineSegment3d):
                return degen_form.intersects_line_segment(
                    line_segment,
                    tolerance=tolerance
                )
            assert isinstance(degen_form, type(self._positions[0]))
            return line_segment.intersects_point(
                degen_form,
                tolerance=tolerance
            )
        # handle degenerate line segment
        if line_segment.is_degenerate:
            degen_form = line_segment.degenerate_form
            assert isinstance(degen_form, type(self._positions[0]))
            return self.intersects_point(degen_form, tolerance=tolerance)
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
        # handle degenerate triangles
        for t1, t2 in ((self, other), (other, self)):
            if t1.is_degenerate:
                degen_form = t1.degenerate_form
                if isinstance(degen_form, LineSegment3d):
                    return t2.intersects_line_segment(
                        degen_form,
                        tolerance=tolerance
                    )
                assert isinstance(degen_form, type(t1._positions[0]))
                return t2.intersects_point(degen_form, tolerance=tolerance)
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
