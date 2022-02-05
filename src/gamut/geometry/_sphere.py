
from __future__ import annotations

__all__ = ['Sphere']

# gamut
from ._viewfrustum3d import ViewFrustum3d
# gamut
from gamut.glmhelp import F32Vector3, vec3_exact
# pyglm
from glm import length, mat4, vec3


class Sphere:

    def __init__(self, center: F32Vector3, radius: float):
        try:
            self._center = vec3_exact(center)
        except TypeError:
            raise TypeError('center must be vec3')

        try:
            self._radius = abs(float(radius))
        except (TypeError, ValueError):
            raise TypeError('radius must be float')

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

    def __rmul__(self, transform: mat4) -> Sphere:
        if not isinstance(transform, mat4):
            return NotImplemented

        max_scale = max(vec3(*(length(c.xyz) for c in (
            transform[0],
            transform[1],
            transform[2],
        ))))
        return Sphere(
            transform * self._center,
            self._radius * max_scale,
        )

    @property
    def center(self) -> vec3:
        return vec3(self._center)

    @property
    def radius(self) -> float:
        return self._radius

    def contains_point(self, point: F32Vector3) -> bool:
        try:
            p = vec3_exact(point)
        except TypeError:
            raise TypeError('point must be vec3')

        return length(self._center - point) <= self._radius

    def seen_by(self, view_frustum: ViewFrustum3d) -> bool:
        for plane in view_frustum.planes:
            distance = plane.distance_to_point(self.center)
            if distance < -self.radius:
                return False
        return True
