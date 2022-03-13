
from __future__ import annotations

__all__ = ['Quad3d']

# gamut
from ._viewfrustum3d import ViewFrustum3d
# gamut
from gamut.math import Matrix4, Vector3, Vector3Array


class Quad3d:

    def __init__(
        self,
        point_0: Vector3,
        point_1: Vector3,
        point_2: Vector3,
        point_3: Vector3
    ):
        self._points = Vector3Array(point_0, point_1, point_2, point_3)

    def __eq__(self, other: Quad3d) -> bool:
        if not isinstance(other, Quad3d):
            return False
        return self._points == other._points

    def __repr__(self) -> str:
        return (
            f'<gamut.geometry.Quad3d ('
            f'({self._points[0].x}, {self._points[0].y}, {self._points[0].z})'
            ', '
            f'({self._points[1].x}, {self._points[1].y}, {self._points[1].z})'
            ', '
            f'({self._points[2].x}, {self._points[2].y}, {self._points[2].z})'
            ', '
            f'({self._points[3].x}, {self._points[3].y}, {self._points[3].z})'
            ')>'
        )

    def __rmatmul__(self, transform: Matrix4) -> Quad3d:
        if not isinstance(transform, Matrix4):
            return NotImplemented

        return Quad3d(*(transform @ p for p in self._points))

    @property
    def points(self) -> Vector3Array:
        return self._points

    def seen_by(self, view_frustum: ViewFrustum3d) -> bool:
        for plane in view_frustum.planes:
            if all(plane.distance_to_point(p) < 0 for p in self._points):
                return False
        return True
