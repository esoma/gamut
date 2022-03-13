
from __future__ import annotations

__all__ = ['Capsule']

# gamut
from gamut.math import Quaternion, Vector3


class Capsule:

    def __init__(
        self,
        center: Vector3,
        radius: float,
        height: float,
        *,
        rotation: Quaternion | None = None
    ):
        if not isinstance(center, Vector3):
            raise TypeError('center must be Vector3')
        self._center = center

        try:
            self._radius = abs(float(radius))
        except (TypeError, ValueError):
            raise TypeError('radius must be float')

        try:
            self._height = abs(float(height))
        except (TypeError, ValueError):
            raise TypeError('height must be float')

        if rotation is None:
            self._rotation = Quaternion(1)
        else:
            if not isinstance(rotation, Quaternion):
                raise TypeError('rotation must be Quaternion')
            self._rotation = rotation

    def __hash__(self) -> int:
        return id(self)

    def __eq__(self, other: Capsule) -> bool:
        if not isinstance(other, Capsule):
            return False
        return (
            self._center == other._center and
            self._radius == other._radius and
            self._height == other._height and
            self._rotation == other._rotation
        )

    def __repr__(self) -> str:
        return (
            f'<gamut.geometry.Capsule '
            f'center=({self._center.x}, {self._center.y}, {self._center.z}) '
            f'radius={self._radius} height={self._height} '
            f'rotation=({self._rotation.w}, {self._rotation.x}, '
            f'{self._rotation.y}, {self._rotation.z})>'
        )

    @property
    def center(self) -> Vector3:
        return self._center

    @property
    def height(self) -> float:
        return self._height

    @property
    def radius(self) -> float:
        return self._radius

    @property
    def rotation(self) -> Quaternion:
        return self._rotation
