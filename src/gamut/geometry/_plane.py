
from __future__ import annotations

__all__ = ['Plane']

# gamut
from ._linesegment3d import LineSegment3d
# gamut
from gamut._bullet import Shape
from gamut.math import (DMatrix4, DVector3, DVector4, FMatrix4, FVector3,
                        FVector4)
# python
from typing import Generic, overload, TYPE_CHECKING, TypeVar

if TYPE_CHECKING:
    # gamut
    from ._triangle3d import Triangle3d

VT = TypeVar('VT', FVector3, DVector3)


class Plane(Generic[VT]):

    @overload
    def __init__(
        self: Plane[FVector3],
        distance: float,
        normal: FVector3
    ):
        ...

    @overload
    def __init__(
        self: Plane[DVector3],
        distance: float,
        normal: DVector3
    ):
        ...

    def __init__(self, distance: float, normal: VT):
        try:
            self._distance = float(distance)
        except (TypeError, ValueError):
            raise TypeError('distance must be float')

        if not isinstance(normal, (FVector3, DVector3)):
            raise TypeError('normal must be FVector3 or DVector3')
        self._normal = normal

        magnitude = normal.magnitude
        try:
            self._distance /= magnitude
            self._normal /= magnitude
        except ZeroDivisionError:
            raise ValueError('invalid normal')

        self._bt: Shape | None = None
        self._bt_capsule: Any = None

    def __hash__(self) -> int:
        return hash((self._distance, self._normal))

    def __repr__(self) -> str:
        return (
            f'<gamut.geometry.Plane distance={self._distance} '
            f'normal=({self._normal.x}, {self._normal.y}, {self._normal.z})>'
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Plane):
            return False
        return (
            self._normal == other._normal and
            self._distance == other._distance
        )

    @overload
    def __rmatmul__(self: Plane[FVector3], transform: FMatrix4) -> Plane:
        ...

    @overload
    def __rmatmul__(self: Plane[DVector3], transform: DMatrix4) -> Plane:
        ...

    def __rmatmul__(self, transform: FMatrix4 | DMatrix4) -> Plane:
        if not isinstance(transform, (FMatrix4, DMatrix4)):
            return NotImplemented

        if isinstance(self._normal, FVector3):
            vec4_type = FVector4
        else:
            assert isinstance(self._normal, DVector3)
            vec4_type = DVector4

        p = transform.inverse().transpose() @ vec4_type(
            *self._normal,
            self._distance
        )
        return Plane(p.w, p.xyz)

    def _get_bullet_shape(self) -> Shape:
        if self._bt is None:
            try:
                self._bt = Shape(False)
                self._bt_capsule = self._bt.add_plane(
                    self._distance,
                    *self._normal
                )
            except BaseException:
                self._bt = None
                self._bt_capsule = None
                raise
        return self._bt

    @property
    def distance(self) -> float:
        return self._distance

    @property
    def normal(self) -> VT:
        return self._normal

    @property
    def origin(self) -> VT:
        return self._normal * -self._distance

    def project_point(self, point: VT) -> VT:
        if not isinstance(point, type(self._normal)):
            raise TypeError(f'point must be {type(self._normal).__name__}')
        v = point - self.origin
        d = v @ self._normal
        return point - d * self._normal

    def signed_distance_to_point(self, point: VT) -> float:
        if not isinstance(point, type(self._normal)):
            raise TypeError(f'point must be {type(self._normal).__name__}')
        return self._normal @ point + self._distance

    def where_intersected_by_point(
        self,
        point: VT,
        *,
        tolerance = 0.0
    ) -> VT | None:
        if not isinstance(point, type(self._normal)):
            raise TypeError(f'point must be {type(self._normal).__name__}')
        if abs(self.signed_distance_to_point(point)) <= tolerance:
            if tolerance == 0.0:
                return point
            else:
                return self.project_point(point)
        else:
            return None

    def where_intersected_by_line_segment(
        self,
        line: LineSegment3d[VT],
        *,
        tolerance = 0.0
    ) -> LineSegment3d[VT] | VT | None:
        if (
            not isinstance(line, LineSegment3d) or
            not isinstance(line.a, type(self._normal))
        ):
            raise TypeError(
                f'line must be LineSegment3d[{type(self._normal).__name__}]'
            )
        # handle degenerate line segments
        if line.is_degenerate:
            degen_form = line.degenerate_form
            assert isinstance(degen_form, type(line.a))
            return self.where_intersected_by_point(
                degen_form,
                tolerance=tolerance
            )
        # find the intersection using math :^)
        ab = line.b - line.a
        den = self.normal @ ab
        if den == 0:
            # line segment is parallel to the plane, so any point of the
            # segment will do as an intersection check
            if abs(self.signed_distance_to_point(line.a)) > tolerance:
                return None
            if tolerance == 0:
                return line
            else:
                return LineSegment3d(
                    self.project_point(line.a),
                    self.project_point(line.b)
                )
        d = self._normal @ self.origin
        t = (d - self._normal @ line.a) / den
        if tolerance == 0:
            if t < 0 or t > 1:
                return None
        else:
            t = max(min(t, 1), 0)
        p = line.a + t * ab
        if tolerance != 0:
            if abs(line.distance_to_point(p)) > tolerance:
                return None
            p = self.project_point(p)
        return p

    def where_intersected_by_triangle(
        self,
        tri: Triangle3d[VT],
        *,
        tolerance = 0.0
    ) -> Triangle3d[VT] | LineSegment3d[VT] | VT | None:
        # gamut
        from gamut.geometry import Triangle3d
        if (
            not isinstance(tri, Triangle3d) or
            not isinstance(tri.positions[0], type(self._normal))
        ):
            raise TypeError(
                f'tri must be Triangle3d[{type(self._normal).__name__}]'
            )
        # handle degenerate triangles
        if tri.is_degenerate:
            degen_form = tri.degenerate_form
            if isinstance(degen_form, LineSegment3d):
                return self.where_intersected_by_line_segment(
                    degen_form,
                    tolerance=tolerance
                )
            assert isinstance(degen_form, type(self._normal))
            return self.where_intersected_by_point(
                degen_form,
                tolerance=tolerance
            )
        # check each edge of the tri
        intersections = []
        for edge in tri.edges:
            intersection = self.where_intersected_by_line_segment(
                edge,
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
                isinstance(i, type(self._normal))
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
            if tolerance == 0:
                return tri
            else:
                return Triangle3d(*(
                    self.project_point(p)
                    for p in tri.positions
                ))
        for intersection in intersections:
            if isinstance(intersection, LineSegment3d):
                return intersection
        assert False
