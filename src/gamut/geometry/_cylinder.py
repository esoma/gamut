
from __future__ import annotations

__all__ = ['Cylinder']

# gamut
from gamut.glmhelp import F32Vector3, vec3_exact, quat_exact, F32Quaternion
# pyglm
from glm import vec3, quat


class Cylinder:

    def __init__(
        self,
        center: F32Vector3,
        radius: float,
        height: float,
        *,
        rotation: F32Quaternion | None = None
    ):
        try:
            self._center = vec3_exact(center)
        except TypeError:
            raise TypeError('center must be vec3')

        try:
            self._radius = abs(float(radius))
        except (TypeError, ValueError):
            raise TypeError('radius must be float')

        try:
            self._height = abs(float(height))
        except (TypeError, ValueError):
            raise TypeError('height must be float')
            
        if rotation is None:
            self._rotation = quat()
        else:
            try:
                self._rotation = quat_exact(rotation)
            except TypeError:
                raise TypeError('rotation must be quat')

    def __hash__(self) -> int:
        return id(self)

    def __eq__(self, other: Cylinder) -> bool:
        if not isinstance(other, Cylinder):
            return False
        return (
            self._center == other._center and
            self._radius == other._radius and
            self._height == other._height
        )

    def __repr__(self) -> str:
        return (
            f'<gamut.geometry.Cylinder '
            f'center=({self._center.x}, {self._center.y}, {self._center.z}) '
            f'radius={self._radius} height={self._height} '
            f'rotation=({self._rotation.w}, {self._rotation.x}, '
            f'{self._rotation.y}, {self._rotation.z})>'
        )

    @property
    def center(self) -> vec3:
        return vec3(self._center)

    @property
    def height(self) -> float:
        return self._height

    @property
    def radius(self) -> float:
        return self._radius
    
    @property
    def rotation(self) -> quat:
        return quat(self._rotation)
