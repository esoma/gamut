
from __future__ import annotations

__all__ = ['Plane']

# gamut
from gamut.glmhelp import F32Vector3, vec3_exact, vec4
# pyglm
from glm import dot, inverse, length, mat4, transpose, vec3


class Plane:

    def __init__(self, distance: float, normal: F32Vector3):
        try:
            self._distance = float(distance)
        except (TypeError, ValueError):
            raise TypeError('distance must be float')
        try:
            self._normal = vec3_exact(normal)
        except TypeError:
            raise TypeError('normal must be vec3')

        magnitude = length(self._normal)
        try:
            self._distance /= magnitude
            self._normal /= magnitude
        except ZeroDivisionError:
            raise ValueError('invalid normal')

    def __repr__(self) -> str:
        return (
            f'<gamut.geometry.Plane distance={self._distance} '
            f'normal=({self._normal.x}, {self._normal.y}, {self._normal.z})>'
        )

    def __eq__(self, other: Plane) -> bool:
        if not isinstance(other, Plane):
            return False
        return (
            self._normal == other._normal and
            self._distance == other._distance
        )

    def __rmul__(self, transform: mat4) -> Plane:
        if not isinstance(transform, mat4):
            return NotImplemented

        p = transpose(inverse(transform)) * vec4(self._normal, self._distance)
        return Plane(p.w, p.xyz)

    @property
    def distance(self) -> float:
        return self._distance

    @property
    def normal(self) -> vec3:
        return vec3(self._normal)

    def distance_to_point(self, point: F32Vector3) -> float:
        try:
            p = vec3_exact(point)
        except TypeError:
            raise TypeError('point must be vec3')
        return dot(self._normal, p) + self._distance
