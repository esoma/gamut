
from __future__ import annotations

__all__ = ['Quad3d']

# gamut
from ._viewfrustum3d import ViewFrustum3d
# gamut
from gamut.glmhelp import F32Vector3, vec3_exact
# pyglm
from glm import mat4, vec3


class Quad3d:

    def __init__(
        self,
        point_0: F32Vector3,
        point_1: F32Vector3,
        point_2: F32Vector3,
        point_3: F32Vector3
    ):
        try:
            self._points = tuple(
                vec3_exact(p)
                for p in (point_0, point_1, point_2, point_3)
            )
        except TypeError:
            raise TypeError('each point must be vec3')

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

    def __rmul__(self, transform: mat4) -> Quad3d:
        if not isinstance(transform, mat4):
            return NotImplemented

        return Quad3d(*(transform * p for p in self._points))

    @property
    def points(self) -> tuple[vec3, vec3, vec3, vec3]:
        return tuple(vec3(p) for p in self._points)

    def seen_by(self, view_frustum: ViewFrustum3d) -> bool:
        for plane in view_frustum.planes:
            if all(plane.distance_to_point(p) < 0 for p in self._points):
                return False
        return True
