
from __future__ import annotations

__all__ = ['BoundingBox3d']

# gamut
from ._viewfrustum3d import ViewFrustum3d
# gamut
from gamut.glmhelp import F32Vector3, vec3_exact
# pyglm
from glm import mat4, vec3


class BoundingBox3d:

    def __init__(self, *points: F32Vector3):
        if not points:
            raise ValueError('must have at least 1 point')
        try:
            vectors = tuple(vec3_exact(p) for p in points)
        except TypeError:
            raise TypeError('each point must be vec3')

        if len(vectors) > 1:
            self._min = vec3(
                min(*(v.x for v in vectors)),
                min(*(v.y for v in vectors)),
                min(*(v.z for v in vectors)),
            )
            self._max = vec3(
                max(*(v.x for v in vectors)),
                max(*(v.y for v in vectors)),
                max(*(v.z for v in vectors)),
            )
        else:
            self._min = self._max = vectors[0]

    def __eq__(self, other: BoundingBox3d) -> bool:
        if not isinstance(other, BoundingBox3d):
            return False
        return self._min == other._min and self._max == other._max

    def __repr__(self) -> str:
        return (
            f'<gamut.geometry.BoundingBox3d '
            f'min=({self._min.x}, {self._min.y}, {self._min.z}) '
            f'max=({self._max.x}, {self._max.y}, {self._max.z})>'
        )

    def __rmul__(self, transform: mat4) -> BoundingBox3d:
        if not isinstance(transform, mat4):
            return NotImplemented

        return BoundingBox3d(*(transform * c for c in self.corners))

    @property
    def center(self) -> vec3:
        return (self._min + self._max) * .5

    @property
    def min(self) -> vec3:
        return vec3(self._min)

    @property
    def max(self) -> vec3:
        return vec3(self._max)

    @property
    def corners(self) -> tuple[vec3, vec3, vec3, vec3, vec3, vec3, vec3, vec3]:
        return tuple(
            vec3(x, y, z)
            for x in (self._min.x, self._max.x)
            for y in (self._min.y, self._max.y)
            for z in (self._min.z, self._max.z)
        )

    def contains_point(self, point: F32Vector3) -> bool:
        try:
            p = vec3_exact(point)
        except TypeError:
            raise TypeError('point must be vec3')
        return all(p >= self._min) and all(p <= self._max)

    def seen_by(self, view_frustum: ViewFrustum3d) -> bool:
        for plane in view_frustum.planes:
            if all(plane.distance_to_point(c) < 0 for c in self.corners):
                return False
        return True
