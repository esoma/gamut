
from __future__ import annotations

__all__ = ['RectangularCuboid']

# gamut
from gamut.glmhelp import F32Quaternion, F32Vector3, quat_exact, vec3_exact
# pyglm
from glm import array, quat, uint8, vec3


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

    def render(self) -> tuple['array[vec3]', 'array[vec3]', 'array[uint8]']:
        half_dimensions = self._dimensions * .5
        positions = array(
            # top
            self._center + half_dimensions * vec3(1, 1, 1),
            self._center + half_dimensions * vec3(1, 1, -1),
            self._center + half_dimensions * vec3(-1, 1, -1),
            self._center + half_dimensions * vec3(-1, 1, 1),
            # bottom
            self._center + half_dimensions * vec3(-1, -1, -1),
            self._center + half_dimensions * vec3(1, -1, -1),
            self._center + half_dimensions * vec3(1, -1, 1),
            self._center + half_dimensions * vec3(-1, -1, 1),
            # right
            self._center + half_dimensions * vec3(1, -1, 1),
            self._center + half_dimensions * vec3(1, -1, -1),
            self._center + half_dimensions * vec3(1, 1, -1),
            self._center + half_dimensions * vec3(1, 1, 1),
            # left
            self._center + half_dimensions * vec3(-1, 1, -1),
            self._center + half_dimensions * vec3(-1, -1, -1),
            self._center + half_dimensions * vec3(-1, -1, 1),
            self._center + half_dimensions * vec3(-1, 1, 1),
            # front
            self._center + half_dimensions * vec3(1, -1, 1),
            self._center + half_dimensions * vec3(1, 1, 1),
            self._center + half_dimensions * vec3(-1, 1, 1),
            self._center + half_dimensions * vec3(-1, -1, 1),
            # back
            self._center + half_dimensions * vec3(1, 1, -1),
            self._center + half_dimensions * vec3(1, -1, -1),
            self._center + half_dimensions * vec3(-1, -1, -1),
            self._center + half_dimensions * vec3(-1, 1, -1),
        )
        normals = array(
            # top
            vec3(0, 1, 0), vec3(0, 1, 0), vec3(0, 1, 0), vec3(0, 1, 0),
            # bottom
            vec3(0, -1, 0), vec3(0, -1, 0), vec3(0, -1, 0), vec3(0, -1, 0),
            # right
            vec3(1, 0, 0), vec3(1, 0, 0), vec3(1, 0, 0), vec3(1, 0, 0),
            # left
            vec3(-1, 0, 0), vec3(-1, 0, 0), vec3(-1, 0, 0), vec3(-1, 0, 0),
            # front
            vec3(0, 0, 1), vec3(0, 0, 1), vec3(0, 0, 1), vec3(0, 0, 1),
            # back
            vec3(0, 0, -1), vec3(0, 0, -1), vec3(0, 0, -1), vec3(0, 0, -1),
        )
        indices = array.from_numbers(uint8,
            # top
            0, 1, 2, 2, 3, 0,
            # bottom
            4, 5, 6, 6, 7, 4,
            # right
            8, 9, 10, 10, 11, 8,
            # left
            12, 13, 14, 14, 15, 12,
            # front
            16, 17, 18, 18, 19, 16,
            # back
            20, 21, 22, 22, 23, 20,
        )
        return positions, normals, indices
