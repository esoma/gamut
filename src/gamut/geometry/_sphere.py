
from __future__ import annotations

__all__ = ['Sphere']

# gamut
from ._viewfrustum3d import ViewFrustum3d
# gamut
from gamut.math import Matrix4, Vector3


class Sphere:

    def __init__(self, center: Vector3, radius: float):
        if not isinstance(center, Vector3):
            raise TypeError('center must be Vector3')
        self._center = center

        try:
            self._radius = abs(float(radius))
        except (TypeError, ValueError):
            raise TypeError('radius must be float')

    def __hash__(self) -> int:
        return id(self)

    def __eq__(self, other: Sphere) -> bool:
        if not isinstance(other, Sphere):
            return False
        return (
            self._center == other._center and
            self._radius == other._radius
        )

    def __repr__(self) -> str:
        return (
            f'<gamut.geometry.Sphere '
            f'center=({self._center.x}, {self._center.y}, {self._center.z}) '
            f'radius={self._radius}>'
        )

    def __rmatmul__(self, transform: Matrix4) -> Sphere:
        if not isinstance(transform, Matrix4):
            return NotImplemented

        max_scale = max(Vector3(*(c.xyz.magnitude for c in (
            transform[0],
            transform[1],
            transform[2],
        ))))
        return Sphere(
            transform @ self._center,
            self._radius * max_scale,
        )

    @property
    def center(self) -> Vector3:
        return self._center

    @property
    def radius(self) -> float:
        return self._radius

    def contains_point(self, point: Vector3) -> bool:
        if not isinstance(point, Vector3):
            raise TypeError('point must be Vector3')

        return (self._center - point).magnitude <= self._radius

    def seen_by(self, view_frustum: ViewFrustum3d) -> bool:
        for plane in view_frustum.planes:
            distance = plane.distance_to_point(self.center)
            if distance < -self.radius:
                return False
        return True
