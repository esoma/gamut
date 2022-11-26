
__all__ = ['CsgBrush']

# gamut
from ._triangle3d import Triangle3d
# gamut
from gamut.math import (DMatrix4, DVector3, DVector3Array, FMatrix4, FVector3,
                        FVector3Array, IVector3, IVector3Array, U8Vector3Array,
                        U16Vector3Array, U32Vector3Array, UVector3Array)
# python
from typing import Generic, overload, TypeVar

PT = TypeVar('PT', FVector3, DVector3)


class CsgBrush(Generic[PT]):

    def __init__(self):
        self._tris = []

    def add_triangle(self, tri: Triangle3d[PT]):
        self._tris.append(tri)


def _are_points_snappable(a: PT, b: PT, distance_sq: float) -> bool:
    d = a - b
    return d @ d < distance_sq


def _is_tri_degenerate(tri: Triangle3d[PT], distance_sq: float) -> bool:
    # checks if a tri will degenerate to a line/point when snapped
    p = tri.positions
    return (
        _are_points_snappable(p[0], p[1], distance_sq) or
        _are_points_snappable(p[0], p[2], distance_sq) or
        _are_points_snappable(p[1], p[2], distance_sq)
    )


def _face_collision_check(
    a: CsgBrush[PT],
    b: CsgBrush[PT],
    snap_distance_sq: float,
    tolerance: float
) -> None:
    for a_tri in a._tris:
        if _is_tri_degenerate(a_tri, snap_distance_sq):
            continue
        for b_tri in b._tris:
            if _is_tri_degenerate(b_tri, snap_distance_sq):
                continue
            if a_tri.intersects_triangle_3d(b_tri, tolerance=tolerance):
                pass


def _update_faces(
    a: Triangle3d[PT],
    b: Triangle3d[PT],
    distance_sq: float,
    tolerance: float
) -> None:
    a_plane = a.plane
    b_plane = b.plane
    for point in a.positions:
        distance = a_plane.distance_to_point(point)
        if abs(distance) <= tolerance:
            pass
        elif distance > 0:
            pass
