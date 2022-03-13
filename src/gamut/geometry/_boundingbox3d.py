
from __future__ import annotations

__all__ = ['BoundingBox3d']

# gamut
from ._sphere import Sphere
from ._viewfrustum3d import ViewFrustum3d
# gamut
from gamut.math import Matrix4, Vector3, Vector3Array


class BoundingBox3d:

    def __init__(self, points: Vector3Array):
        if not isinstance(points, Vector3Array):
            raise TypeError('points must be Vector3Array')
        if not points:
            raise ValueError('must have at least 1 point')

        if len(points) > 1:
            self._min = Vector3(
                min(*(v.x for v in points)),
                min(*(v.y for v in points)),
                min(*(v.z for v in points)),
            )
            self._max = Vector3(
                max(*(v.x for v in points)),
                max(*(v.y for v in points)),
                max(*(v.z for v in points)),
            )
        else:
            self._min = self._max = points[0]

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

    def __rmatmul__(self, transform: Matrix4) -> BoundingBox3d:
        if not isinstance(transform, Matrix4):
            return NotImplemented

        return BoundingBox3d(Vector3Array(*(
            transform @ c for c in self.corners
        )))

    def _squared_distance_to_point(self, point: Vector3) -> float:
        result = 0.0
        for i in range(3):
            c = point[i]
            if c < self._min[i]:
                result += (self._min[i] - c) ** 2
            if c > self._max[i]:
                result += (self._max[i] - c) ** 2
        return result

    @property
    def center(self) -> Vector3:
        return (self._min + self._max) * .5

    @property
    def min(self) -> Vector3:
        return self._min

    @property
    def max(self) -> Vector3:
        return self._max

    @property
    def corners(self) -> tuple[
        Vector3, Vector3,
        Vector3, Vector3,
        Vector3, Vector3,
        ector3, Vector3
    ]:
        return tuple(
            Vector3(x, y, z)
            for x in (self._min.x, self._max.x)
            for y in (self._min.y, self._max.y)
            for z in (self._min.z, self._max.z)
        )

    def contains_point(self, point: Vector3) -> bool:
        if not isinstance(point, Vector3):
            raise TypeError('point must be Vector3')
        return (
            all(p >= m for p, m in zip(point, self._min)) and
            all(p <= m for p, m in zip(point, self._max))
        )

    def intersects_sphere(self, sphere: Sphere) -> bool:
        return (
            self._squared_distance_to_point(sphere.center) <=
            (sphere.radius ** 2)
        )

    def seen_by(self, view_frustum: ViewFrustum3d) -> bool:
        for plane in view_frustum.planes:
            if all(plane.distance_to_point(c) < 0 for c in self.corners):
                return False
        return True
