
from __future__ import annotations

__all__ = ['Plane']

# gamut
from gamut.math import Matrix4, Vector3, Vector4


class Plane:

    def __init__(self, distance: float, normal: Vector3):
        try:
            self._distance = float(distance)
        except (TypeError, ValueError):
            raise TypeError('distance must be float')

        if not isinstance(normal, Vector3):
            raise TypeError('normal must be Vector3')
        self._normal = normal

        magnitude = normal.magnitude
        try:
            self._distance /= magnitude
            self._normal /= magnitude
        except ZeroDivisionError:
            raise ValueError('invalid normal')

    def __hash__(self) -> int:
        return id(self)

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

    def __rmatmul__(self, transform: Matrix4) -> Plane:
        if not isinstance(transform, Matrix4):
            return NotImplemented

        p = transform.inverse().transpose() @ Vector4(
            *self._normal,
            self._distance
        )
        return Plane(p.w, p.xyz)

    @property
    def distance(self) -> float:
        return self._distance

    @property
    def normal(self) -> Vector3:
        return self._normal

    def distance_to_point(self, point: Vector3) -> float:
        if not isinstance(point, Vector3):
            raise TypeError('point must be Vector3')
        return self._normal @ point + self._distance
