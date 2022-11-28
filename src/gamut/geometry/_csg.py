
__all__ = ['CsgBrush']

# gamut
from ._triangle3d import Triangle2d, Triangle3d
# gamut
from gamut.math import (DMatrix4, DVector3, DVector3Array, FMatrix4, FVector3,
                        FVector3Array, IVector3, IVector3Array, U8Vector3Array,
                        U16Vector3Array, U32Vector3Array, UVector3Array)
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
        self._tris_built = False

    def union(self) -> CsgBrush[PT]:
        self._build_tris()
        result = CsgBrush()

        return result

    def _are_points_snappable(self, a: PT, b: PT) -> bool:
        d = a - b
        return d @ d < self._snap_distance_2

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
        a_intersections, b_intersections = self._get_intersections()
        tri_2d_intersections = [
            Tri2dIntersection(t, intersections, self._tolerance)
            for t, intersections in (
                *a_intersections.items(),
                *b_intersections.items()
            )
        ]

        self._tris_built = True

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

class Tri2dIntersection:

    def __init__(
        self,
        tri: Triangle3d[PT],
        intersections: set[Triangle3d[PT]],
        tolerance: float
    ) -> None:
        Matrix4 = (
            FMatrix4
            if isinstance(tri.positions[0], FVector3)
            else DMatrix4
        )
        self._plane = tri.plane

        bmc = (tri.positions[1] - tri.positions[2]).normalize()
        self._to_3d = Matrix4(
            *bmc, 0,
            *bmc.cross(tri.normal).normalize(), 0,
            *tri.normal, 0,
            *tri.positions[0], 1
        )
        to_2d = self._to_3d.inverse()

        self._2d_tris = [
            Triangle2d(*(
                (to_2d @ p.xyzl).xy
                for p in tri.positions
            ))
        ]
        for intersection in intersections:
            self._add_intersection(intersection, to_2d, tolerance)

    def _add_intersection(
        self,
        tri: Triangle3d[PT],
        to_2d: FMatrix4 | DMatrix4,
        tolerance: float
    ) -> None:
        points_to_add: list[PT] = []

        pd = [self._plane.distance_to_point(p) for p in tri.positions]
        for i, (p, d, edge) in enumerate(zip(tri.positions, pd, tri.edges)):
            if abs(d) <= tolerance:
                points_to_add.append(p)
            else:
                next_d = pd[(i + 1) % 3]
                if abs(next_d) <= tolerance:
                    continue
                if copysign(d, next_d) == d:
                    continue
                edge_intersection = self._plane.where_intersects_line_segment(
                    edge,
                    tolerance=tolerance
                )
                if edge_intersection is not None:
                    points_to_add.append(edge_intersection)

        print(points_to_add)

