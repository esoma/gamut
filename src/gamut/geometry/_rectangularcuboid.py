
from __future__ import annotations

__all__ = ['RectangularCuboid']

# gamut
from gamut.math import Quaternion, U8Array, Vector3, Vector3Array


class RectangularCuboid:

    def __init__(
        self,
        center: Vector3,
        dimensions: Vector3,
        *,
        rotation: Quaternion | None = None
    ):
        if not isinstance(center, Vector3):
            raise TypeError('center must be Vector3')
        self._center = center

        if not isinstance(dimensions, Vector3):
            raise TypeError('dimensions must be Vector3')
        self._dimensions = dimensions

        if rotation is None:
            self._rotation = Quaternion(1)
        else:
            if not isinstance(rotation, Quaternion):
                raise TypeError('rotation must be Quaternion')
            self._rotation = rotation

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
    def center(self) -> Vector3:
        return self._center

    @property
    def dimensions(self) -> Vector3:
        return self._dimensions

    @property
    def rotation(self) -> Quaternion:
        return self._rotation

    def render(self) -> tuple[Vector3Array, Vector3Array, U8Array]:
        half_dimensions = self._dimensions * .5
        positions = Vector3Array(
            # top
            self._center + half_dimensions * Vector3(1, 1, 1),
            self._center + half_dimensions * Vector3(1, 1, -1),
            self._center + half_dimensions * Vector3(-1, 1, -1),
            self._center + half_dimensions * Vector3(-1, 1, 1),
            # bottom
            self._center + half_dimensions * Vector3(-1, -1, -1),
            self._center + half_dimensions * Vector3(1, -1, -1),
            self._center + half_dimensions * Vector3(1, -1, 1),
            self._center + half_dimensions * Vector3(-1, -1, 1),
            # right
            self._center + half_dimensions * Vector3(1, -1, 1),
            self._center + half_dimensions * Vector3(1, -1, -1),
            self._center + half_dimensions * Vector3(1, 1, -1),
            self._center + half_dimensions * Vector3(1, 1, 1),
            # left
            self._center + half_dimensions * Vector3(-1, 1, -1),
            self._center + half_dimensions * Vector3(-1, -1, -1),
            self._center + half_dimensions * Vector3(-1, -1, 1),
            self._center + half_dimensions * Vector3(-1, 1, 1),
            # front
            self._center + half_dimensions * Vector3(1, -1, 1),
            self._center + half_dimensions * Vector3(1, 1, 1),
            self._center + half_dimensions * Vector3(-1, 1, 1),
            self._center + half_dimensions * Vector3(-1, -1, 1),
            # back
            self._center + half_dimensions * Vector3(1, 1, -1),
            self._center + half_dimensions * Vector3(1, -1, -1),
            self._center + half_dimensions * Vector3(-1, -1, -1),
            self._center + half_dimensions * Vector3(-1, 1, -1),
        )
        normals = Vector3Array(
            # top
            Vector3(0, 1, 0), Vector3(0, 1, 0),
            Vector3(0, 1, 0), Vector3(0, 1, 0),
            # bottom
            Vector3(0, -1, 0), Vector3(0, -1, 0),
            Vector3(0, -1, 0), Vector3(0, -1, 0),
            # right
            Vector3(1, 0, 0), Vector3(1, 0, 0),
            Vector3(1, 0, 0), Vector3(1, 0, 0),
            # left
            Vector3(-1, 0, 0), Vector3(-1, 0, 0),
            Vector3(-1, 0, 0), Vector3(-1, 0, 0),
            # front
            Vector3(0, 0, 1), Vector3(0, 0, 1),
            Vector3(0, 0, 1), Vector3(0, 0, 1),
            # back
            Vector3(0, 0, -1), Vector3(0, 0, -1),
            Vector3(0, 0, -1), Vector3(0, 0, -1),
        )
        indices = U8Array(
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
