from __future__ import annotations

__all__ = ['CsgBrush']

# gamut
from ._linesegment2d import LineSegment2d
from ._triangle2d import Triangle2d
from ._triangle3d import Triangle3d
# gamut
from gamut.math import (DMatrix4, DVector2, DVector3, DVector3Array, FMatrix4,
                        FVector2, FVector3, FVector3Array, IVector3,
                        IVector3Array, U8Vector3Array, U16Vector3Array,
                        U32Vector3Array, UVector3Array)
# python
from math import copysign
from typing import Generic, overload, TypeVar

PT = TypeVar('PT', FVector3, DVector3)


class CsgBrush(Generic[PT]):

    def __init__(self):
        self._tris = []

    def add_triangle(self, tri: Triangle3d[PT]):
        self._tris.append(tri)


class CsgOperation(Generic[PT]):

    def __init__(
        self,
        a: CsgBrush[PT],
        b: CsgBrush[PT],
        snap_distance: float
    ) -> None:
        self._a = a
        self._b = b
        self._snap_distance = snap_distance
        self._snap_distance_2 = snap_distance * snap_distance
        self._tolerance = 0.0
        self._a_tris_inside: dict[Triangle3d[PT], bool] = {}
        self._b_tris_inside: dict[Triangle3d[PT], bool] = {}
        self._tris_built = False

    def union(self) -> CsgBrush[PT]:
        self._build_tris()
        result = CsgBrush()

        return result

    def _are_points_snappable(self, a: PT, b: PT) -> bool:
        d = a - b
        return d @ d <= self._snap_distance_2

    def _is_tri_degenerate(self, tri: Triangle3d[PT]) -> bool:
        # checks if a tri will degenerate to a line/point when snapped
        p = tri.positions
        return (
            self._are_points_snappable(p[0], p[1]) or
            self._are_points_snappable(p[0], p[2]) or
            self._are_points_snappable(p[1], p[2])
        )

    def _build_tris(self) -> None:
        if self._tris_built:
            return
        a_tri_2d_intersections, b_tri_2d_intersections = (
            self._get_tri_2d_intersections()
        )
        a_tris = self._build_brush_tris(self._a, a_tri_2d_intersections)
        b_tris = self._build_brush_tris(self._b, b_tri_2d_intersections)
        for tri in a_tris:
            self._a_tris_inside[tri] = self._is_tri_inside(
                a_tris,
                b_tris,
                tri,
                True
            )
        for tri in b_tris:
            self._b_tris_inside[tri] = self._is_tri_inside(
                a_tris,
                b_tris,
                tri,
                False
            )
        self._tris_built = True

    def _is_tri_inside(
        self,
        a_tris: set[Triangle3d[PT]],
        b_tris: set[Triangle3d[PT]],
        tri: Triangle3d[PT],
        is_a_tri: bool
    ) -> bool:
        for other_tri in (*a_tris, *b_tris):
            pass

    def _get_intersections(self) -> tuple[
        dict[Triangle3d[PT], set[Triangle3d[PT]]],
        dict[Triangle3d[PT], set[Triangle3d[PT]]]
    ]:
        a_intersections: dict[Triangle3d[PT], set[Triangle3d[PT]]] = {}
        b_intersections: dict[Triangle3d[PT], set[Triangle3d[PT]]] = {}
        for a_tri in self._a._tris:
            if self._is_tri_degenerate(a_tri):
                continue
            for b_tri in self._b._tris:
                if self._is_tri_degenerate(b_tri):
                    continue
                if a_tri.intersects_triangle_3d(
                    b_tri,
                    tolerance=self._tolerance
                ):
                    a_intersections.setdefault(a_tri, set()).add(b_tri)
                    b_intersections.setdefault(b_tri, set()).add(a_tri)
        return (a_intersections, b_intersections)

    def _get_tri_2d_intersections(self) -> tuple[
        dict[Triangle3d[PT], Tri2dIntersection[PT]],
        dict[Triangle3d[PT], Tri2dIntersection[PT]],
    ]:
        a_intersections, b_intersections = self._get_intersections()
        a = {
            t: Tri2dIntersection(
                t,
                intersections,
                self._tolerance,
                self._snap_distance,
                self._snap_distance_2
            )
            for t, intersections in a_intersections.items()
        }
        b = {
            t: Tri2dIntersection(
                t,
                intersections,
                self._tolerance,
                self._snap_distance,
                self._snap_distance_2
            )
            for t, intersections in b_intersections.items()
        }
        return (a, b)

    def _build_brush_tris(
        self,
        brush: CsgBrush[PT],
        tri_2d_intersections: dict[Triangle3d[PT], Tri2dIntersection[PT]],
    ) -> set[Triangle3d[PT]]:
        brush_tris = set()
        for tri in brush._tris:
            intersection = tri_2d_intersections.get(tri)
            if intersection is None:
                if not tri.is_degenerate:
                    brush_tris.add(tri)
            else:
                for sub_tri in intersection.get_tris():
                    assert not sub_tri.is_degenerate
                    brush_tris.add(sub_tri)
        return brush_tris


class Tri2dIntersection(Generic[PT]):

    def __init__(
        self,
        tri: Triangle3d[PT],
        intersections: set[Triangle3d[PT]],
        tolerance: float,
        snap_distance: float,
        snap_distance_2: float
    ) -> None:
        Matrix4 = (
            FMatrix4
            if isinstance(tri.positions[0], FVector3)
            else DMatrix4
        )
        self._plane = tri.plane
        self._tolerance = tolerance
        self._snap_distance = snap_distance
        self._snap_distance_2 = snap_distance_2

        bmc = (tri.positions[1] - tri.positions[2]).normalize()
        self._to_3d = Matrix4(
            *bmc, 0,
            *bmc.cross(tri.normal).normalize(), 0,
            *tri.normal, 0,
            *tri.positions[0], 1
        )
        self._to_2d = self._to_3d.inverse()

        self._2d_tris = {
            Triangle2d(*(
                (self._to_2d @ p.xyzl).xy
                for p in tri.positions
            ))
        }
        self._2d_points = {
            p
            for t in self._2d_tris
            for p in t.positions
        }
        for intersection in intersections:
            self._add_intersection(intersection)

    def get_tris(self) -> Generator[Triangle3d[PT], None, None]:
        for tri2 in self._2d_tris:
            yield Triangle3d(*(
                (self._to_3d @ p.xyol).xyz
                for p in tri2.positions
            ))

    @overload
    def _are_points_snappable(
        self: Tri2dIntersection[FVector3],
        a: FVector2,
        b: FVector2
    ) -> bool:
        ...

    @overload
    def _are_points_snappable(
        self: Tri2dIntersection[DVector3],
        a: DVector2,
        b: DVector2
    ) -> bool:
        ...

    def _are_points_snappable(
        self,
        a: FVector2 | DVector2,
        b: FVector2 | DVector2
    ) -> bool:
        assert isinstance(a, type(b))
        d = a - b
        return d @ d <= self._snap_distance_2

    @overload
    def _is_tri_degenerate(
        self: Tri2dIntersection[FVector3],
        tri: Triangle2d[FVector2]
    ) -> bool:
        ...

    @overload
    def _is_tri_degenerate(
        self: Tri2dIntersection[DVector3],
        tri: Triangle2d[DVector2]
    ) -> bool:
        ...

    def _is_tri_degenerate(
        self,
        tri: Triangle2d[FVector2] | Triangle2d[DVector2]
    ) -> bool:
        # checks if a tri will degenerate to a line/point when snapped
        p = tri.positions
        return (
            self._are_points_snappable(p[0], p[1]) or
            self._are_points_snappable(p[0], p[2]) or
            self._are_points_snappable(p[1], p[2])
        )

    def _add_intersection(self, tri: Triangle3d[PT]) -> None:
        points_to_add: list[PT] = []

        pd = [self._plane.signed_distance_to_point(p) for p in tri.positions]
        for i, (p, d, edge) in enumerate(zip(tri.positions, pd, tri.edges)):
            if abs(d) <= self._tolerance:
                points_to_add.append(p)
            else:
                next_d = pd[(i + 1) % 3]
                if abs(next_d) <= self._tolerance:
                    continue
                if copysign(d, next_d) == d:
                    continue
                edge_intersection = (
                    self._plane.where_intersected_by_line_segment(
                        edge,
                        tolerance=self._tolerance
                    )
                )
                if edge_intersection is not None:
                    points_to_add.append(edge_intersection)

        added_points = []
        for p in points_to_add:
            p2 = self._add_point((self._to_2d @ p.xyzl).xy)
            if p2 is None:
                return
            added_points.append(p2)

        if len(added_points) == 2:
            self._add_line_segment(LineSegment2d(*added_points))
        elif len(added_points) == 3:
            print("ADD TRIANGLE")
            assert False

    @overload
    def _add_point(
        self: Tri2dIntersection[FVector3],
        point: FVector2
    ) -> FVector2 | None:
        ...

    @overload
    def _add_point(
        self: Tri2dIntersection[DVector3],
        point: DVector2
    ) -> DVector2 | None:
        ...

    def _add_point(
        self,
        point: FVector2 | DVector2
    ) -> FVector2 | DVector2 | None:
        assert isinstance(point, type(self._plane.normal.oo))
        for tri in list(self._2d_tris):
            assert not self._is_tri_degenerate(tri)
            #if self._is_tri_degenerate(tri):
            #    continue
            # check if the point is existing face vertex
            for p in tri.positions:
                if p.distance(point) <= self._snap_distance:
                    return p
            # check if point is on an edge
            for edge in tri.edges:
                if edge.get_distance_to_point(point) <= self._snap_distance:
                    snapped_point = self._add_snapped_point(point)
                    opposite_point = tri.get_point_opposite_of_edge(edge)
                    # if new snapped point snaps to the opposite point then we
                    # can delete the face since it will degenerate
                    if snapped_point == opposite_point:
                        self._2d_tris.remove(tri)
                        return snapped_point
                    # subdivide the tri along the edge where the intersection
                    # was
                    tri_a = Triangle2d(edge.a, snapped_point, opposite_point)
                    if self._is_tri_degenerate(tri_a):
                        return snapped_point
                    tri_b = Triangle2d(edge.b, snapped_point, opposite_point)
                    if self._is_tri_degenerate(tri_b):
                        return snapped_point
                    # if there was no degeneration we can replace the tri with
                    # the subdivided versions
                    self._2d_tris.remove(tri)
                    self._2d_tris.add(tri_a)
                    self._2d_tris.add(tri_b)
                    return snapped_point
            else:
                # not on an edge, check if the point is inside the tri
                if tri.intersects_point(point, tolerance=self._tolerance):
                    # replace this tri with 3 tris, where each edge of the
                    # original tri connects to the point
                    snapped_point = self._add_snapped_point(point)
                    for edge in tri.edges:
                        new_tri = Triangle2d(edge.a, edge.b, snapped_point)
                        if self._is_tri_degenerate(new_tri):
                            continue
                        self._2d_tris.add(new_tri)
                    self._2d_tris.remove(tri)
                    return snapped_point
        return None

    @overload
    def _add_snapped_point(
        self: Tri2dIntersection[FVector3],
        point: FVector2
    ) -> FVector2:
        ...

    @overload
    def _add_snapped_point(
        self: Tri2dIntersection[DVector3],
        point: DVector2
    ) -> DVector2:
        ...

    def _add_snapped_point(
        self,
        point: FVector2 | DVector2
    ) -> FVector2 | DVector2:
        p = point
        if self._snap_distance != 0:
            for p in self._2d_points:
                if p.distance(point) <= self._snap_distance:
                    return p
            p = point
        self._2d_points.add(p)
        return p

    @overload
    def _add_line_segment(
        self: Tri2dIntersection[FVector3],
        line: LineSegment2d[FVector2]
    ) -> None:
        ...


    @overload
    def _add_line_segment(
        self: Tri2dIntersection[DVector3],
        line: LineSegment2d[DVector2]
    ) -> None:
        ...

    def _add_line_segment(
        self,
        line: LineSegment2d[FVector2] | LineSegment2d[DVector2]
    ) -> None:
        assert isinstance(line.a, type(self._plane.normal.oo))
        shape_points = {line.a, line.b}
        for tri in list(self._2d_tris):
            for edge in tri.edges:
                intersection = edge.where_intersected_by_line_segment(
                    line,
                    tolerance=self._tolerance
                )
                # skip if no intersection or if the line and edge are parallel
                # intersecting
                if (
                    intersection is None or
                    isinstance(intersection, LineSegment2d)
                ):
                    continue
                assert isinstance(intersection, (FVector2, DVector2))
                # skip if the intersection point would snap to one of the
                # edge's points
                if (
                    self._are_points_snappable(intersection, edge.a) or
                    self._are_points_snappable(intersection, edge.b)
                ):
                    continue
                point = self._add_snapped_point(intersection)
                shape_points.add(point)
                opposite_point = tri.get_point_opposite_of_edge(edge)
                # if new snapped point snaps to the opposite point then we can
                # delete the face since it will degenerate
                if point == opposite_point:
                    self._2d_tris.remove(tri)
                    break

                if (
                    line.get_distance_to_point(opposite_point) <=
                    self._snap_distance_2
                ):
                    shape_points.add(opposite_point)
                # subdivide the tri into two using the intersection on the edge
                # as the split
                tri_a = Triangle2d(point, opposite_point, edge.a)
                tri_b = Triangle2d(opposite_point, edge.b, point)
                self._2d_tris.remove(tri)
                self._2d_tris.add(tri_a)
                self._2d_tris.add(tri_b)
                break
        self._merge_tris(shape_points)

    @overload
    def _merge_tris(
        self: Tri2dIntersection[FVector3],
        points: set[FVector2]
    ) -> None:
        ...

    @overload
    def _merge_tris(
        self: Tri2dIntersection[DVector3],
        points: set[DVector2]
    ) -> None:
        ...

    def _merge_tris(self, points: set[FVector2 | DVector2]) -> None:
        if len(points) < 3:
            return
        print("______________________")
        # sort points by the axis with the overall widest range
        min_x = min(*(p.x for p in points))
        max_x = max(*(p.x for p in points))
        min_y = min(*(p.y for p in points))
        max_y = max(*(p.y for p in points))
        axis = 0 if abs(max_x - min_x) > abs(max_y - min_y) else 1
        sorted_points = sorted(points, key=lambda p: p[axis])

        print(len(sorted_points))
        # tris around an inner vertex are merged by moving the inner vertex to
        # the closest index
        half_index = (len(points) - 1) // 2
        for point, closest in (
            *zip(
                sorted_points[1:half_index + 1],
                (sorted_points[0] for i in range(half_index))
            ),
            *zip(
                sorted_points[half_index + 1:-1],
                (sorted_points[-1] for i in range(half_index))
            )
        ):
            # find the tris that share a vertex with the point so that they
            # can be merged
            merges: list[tuple[
                Triangle2d[FVector2 | DVector2],
                FVector2 | DVector2
            ]] = []
            for tri in tuple(self._2d_tris):
                for tri_p in tri.positions:
                    if tri_p == point:
                        merges.append((tri, tri_p))
                        self._2d_tris.remove(tri)
            # create new tris
            degenerate_points: list[FVector2 | DVector2] = []
            for tri, tri_p in merges:
                opposite_edge = tri.get_edge_opposite_of_point(tri_p)
                # skip flattened faces
                if opposite_edge.a == closest or opposite_edge.b == closest:
                    continue
                new_tri = Triangle2d(
                    closest,
                    opposite_edge.a,
                    opposite_edge.b
                )
                if new_tri.is_degenerate:
                    degenerate_points.append(tri_p)
                    continue
                self._2d_tris.add(new_tri)
            if not degenerate_points:
                continue
            print("DEGEN POINTS")
            assert False


