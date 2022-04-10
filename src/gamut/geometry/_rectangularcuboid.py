
from __future__ import annotations

__all__ = ['RectangularCuboid']

# gamut
from gamut._bullet import Shape
from gamut.math import (DQuaternion, DVector3, DVector3Array, FQuaternion,
                        FVector3, FVector3Array, U8Array)
# python
from typing import Generic, overload, TypeVar

AT = TypeVar('AT', FVector3Array, DVector3Array)
VT = TypeVar('VT', FVector3, DVector3)
QT = TypeVar('QT', FQuaternion, DQuaternion)


class RectangularCuboid(Generic[VT, QT, AT]):

    @overload
    def __init__(
        self: RectangularCuboid[FVector3, FQuaternion, FVector3Array],
        center: FVector3,
        dimensions: FVector3,
        *,
        rotation: FQuaternion | None = None
    ):
        ...

    @overload
    def __init__(
        self: RectangularCuboid[DVector3, DQuaternion, DVector3Array],
        center: DVector3,
        dimensions: DVector3,
        *,
        rotation: DQuaternion | None = None
    ):
        ...

    def __init__(
        self,
        center: VT,
        dimensions: VT,
        *,
        rotation: QT | None = None
    ):
        is_double = isinstance(center, DVector3)
        if not is_double and not isinstance(center, FVector3):
            raise TypeError('center must be FVector3 or DVector3')
        self._center = center

        if not isinstance(dimensions, type(center)):
            raise TypeError(f'dimensions must be {type(center).__name__}')
        self._dimensions = dimensions

        if is_double:
            quat_type = DQuaternion
        else:
            quat_type = FQuaternion

        if rotation is None:
            self._rotation = quat_type(1)
        else:
            if not isinstance(rotation, quat_type):
                raise TypeError(f'rotation must be {quat_type.__name__}')
            self._rotation = rotation

        self._bt: Shape | None = None
        self._bt_capsule: Any = None

    def __hash__(self) -> int:
        return hash((self._center, self._dimensions, self._rotation))

    def __eq__(self, other: object) -> bool:
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

    def _get_bullet_shape(self) -> Shape:
        if self._bt is None:
            try:
                self._bt = Shape(False)
                self._bt_capsule = self._bt.add_rectangular_cuboid(
                    *self._center,
                    *self._dimensions,
                    *self._rotation
                )
            except BaseException:
                self._bt = None
                self._bt_capsule = None
                raise
        return self._bt

    @property
    def center(self) -> VT:
        return self._center

    @property
    def dimensions(self) -> VT:
        return self._dimensions

    @property
    def rotation(self) -> QT:
        return self._rotation

    def render(self) -> tuple[AT, AT, U8Array]:
        if isinstance(self._center, DVector3):
            array_type = DVector3Array
            vector_type = DVector3
        else:
            assert isinstance(self._center, FVector3)
            array_type = FVector3Array
            vector_type = FVector3

        half_dimensions = self._dimensions * .5
        positions = array_type(
            # top
            self._center + half_dimensions * vector_type(1, 1, 1),
            self._center + half_dimensions * vector_type(1, 1, -1),
            self._center + half_dimensions * vector_type(-1, 1, -1),
            self._center + half_dimensions * vector_type(-1, 1, 1),
            # bottom
            self._center + half_dimensions * vector_type(-1, -1, -1),
            self._center + half_dimensions * vector_type(1, -1, -1),
            self._center + half_dimensions * vector_type(1, -1, 1),
            self._center + half_dimensions * vector_type(-1, -1, 1),
            # right
            self._center + half_dimensions * vector_type(1, -1, 1),
            self._center + half_dimensions * vector_type(1, -1, -1),
            self._center + half_dimensions * vector_type(1, 1, -1),
            self._center + half_dimensions * vector_type(1, 1, 1),
            # left
            self._center + half_dimensions * vector_type(-1, 1, -1),
            self._center + half_dimensions * vector_type(-1, -1, -1),
            self._center + half_dimensions * vector_type(-1, -1, 1),
            self._center + half_dimensions * vector_type(-1, 1, 1),
            # front
            self._center + half_dimensions * vector_type(1, -1, 1),
            self._center + half_dimensions * vector_type(1, 1, 1),
            self._center + half_dimensions * vector_type(-1, 1, 1),
            self._center + half_dimensions * vector_type(-1, -1, 1),
            # back
            self._center + half_dimensions * vector_type(1, 1, -1),
            self._center + half_dimensions * vector_type(1, -1, -1),
            self._center + half_dimensions * vector_type(-1, -1, -1),
            self._center + half_dimensions * vector_type(-1, 1, -1),
        )
        normals = array_type(
            # top
            vector_type(0, 1, 0), vector_type(0, 1, 0),
            vector_type(0, 1, 0), vector_type(0, 1, 0),
            # bottom
            vector_type(0, -1, 0), vector_type(0, -1, 0),
            vector_type(0, -1, 0), vector_type(0, -1, 0),
            # right
            vector_type(1, 0, 0), vector_type(1, 0, 0),
            vector_type(1, 0, 0), vector_type(1, 0, 0),
            # left
            vector_type(-1, 0, 0), vector_type(-1, 0, 0),
            vector_type(-1, 0, 0), vector_type(-1, 0, 0),
            # front
            vector_type(0, 0, 1), vector_type(0, 0, 1),
            vector_type(0, 0, 1), vector_type(0, 0, 1),
            # back
            vector_type(0, 0, -1), vector_type(0, 0, -1),
            vector_type(0, 0, -1), vector_type(0, 0, -1),
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
