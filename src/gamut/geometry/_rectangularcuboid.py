
from __future__ import annotations

__all__ = ['RectangularCuboid']

# gamut
from gamut.glmhelp import F32Quaternion, F32Vector3, quat_exact, vec3_exact
# pyglm
from glm import quat, vec3


class RectangularCuboid:

    def __init__(
        self,
        center: F32Vector3,
        dimensions: F32Vector3,
        *,
        rotation: F32Quaternion | None = None
    ):
        try:
            self._center = vec3_exact(center)
        except TypeError:
            raise TypeError('center must be vec3')

        try:
            self._dimensions = abs(vec3_exact(dimensions))
        except TypeError:
            raise TypeError('dimensions must be vec3')

        if rotation is None:
            self._rotation = quat()
        else:
            try:
                self._rotation = quat_exact(rotation)
            except TypeError:
                raise TypeError('rotation must be quat')

    def __hash__(self) -> int:
        return id(self)

    def __eq__(self, other: RectangularCuboid) -> bool:
        if not isinstance(other, RectangularCuboid):
            return False
        return (
            self._center == other._center and
            self._dimensions == other._dimensions and
            self._rotation == other._rotation
        )

    def __repr__(self) -> str:
        return (
            f'<gamut.geometry.RectangularCuboid '
            f'center=({self._center.x}, {self._center.y}, {self._center.z}) '
            f'dimensions=({self._dimensions.x}, {self._dimensions.y}, '
            f'{self._dimensions.z}) '
            f'rotation=({self._rotation.w}, {self._rotation.x}, '
            f'{self._rotation.y}, {self._rotation.z})>'
        )

    @property
    def center(self) -> vec3:
        return vec3(self._center)

    @property
    def dimensions(self) -> vec3:
        return vec3(self._dimensions)

    @property
    def rotation(self) -> quat:
        return quat(self._rotation)
