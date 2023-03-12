
from __future__ import annotations

__all__ = ['Rectangle3d']

# gamut
from ._error import DegenerateGeometryError
from ._linesegment3d import LineSegment3d
# gamut
from gamut.math import (DQuaternion, DVector2, DVector3, FQuaternion, FVector2,
                        FVector3)
# python
from typing import Generic, overload, TypeVar

VT3 = TypeVar('VT3', FVector3, DVector3)
VT2 = TypeVar('VT2', FVector2, DVector2)
QT = TypeVar('QT', FQuaternion, DQuaternion)


class Rectangle3d(Generic[VT3, VT2, QT]):

    class DegenerateError(DegenerateGeometryError):
        degenerate_form: VT3 | LineSegment3d[VT3]

    @overload
    def __init__(
        self: Rectangle3d[FVector3, FVector2],
        center: FVector3,
        dimensions: FVector2,
        *,
        rotation: FQuaternion | None = None
    ):
        ...

    @overload
    def __init__(
        self: Rectangle3d[DVector3, DVector2],
        center: DVector3,
        dimensions: DVector2,
        *,
        rotation: DQuaternion | None = None
    ):
        ...

    def __init__(
        self,
        center: VT3,
        dimensions: VT2,
        *,
        rotation: QT | None = None
    ):
        if not isinstance(center, (FVector3, DVector3)):
            raise TypeError('center must be FVector3 or DVector3')
        self._center = center

        if type(center) is DVector3:
            dimensions_type = DVector2
            rotation_type = DQuaternion
        else:
            assert type(center) is FVector3
            dimensions_type = FVector2
            rotation_type = FQuaternion

        if not isinstance(dimensions, dimensions_type):
            raise TypeError(f'dimensions must be {dimensions_type.__name__}')
        self._dimensions = abs(dimensions)

        if rotation is None:
            self._rotation = rotation_type(1)
        else:
            if not isinstance(rotation, rotation_type):
                raise TypeError(f'rotation must be {rotation_type.__name__}')
            self._rotation = rotation

        if dimensions.x == 0 and dimensions.y == 0:
            raise self.DegenerateError(center, 'degenerate 3d rectangle')
        elif dimensions.x == 0 or dimensions.y == 0:
            assert not (dimensions.x == 0 and dimensions.y == 0)
            half_dimensions_3d = self._rotation @ (dimensions.xyo * .5)
            raise self.DegenerateError(
                LineSegment3d(
                    center - half_dimensions_3d,
                    center + half_dimensions_3d,
                ),
                'degenerate 3d rectangle'
            )

    def __hash__(self) -> int:
        return hash((self._center, self._dimensions, self._rotation))

    def __repr__(self) -> str:
        return (
            f'<gamut.geometry.Rectangle3d '
            f'center=({self._center.x}, {self._center.y}, {self._center.z}) '
            f'dimensions=({self._dimensions.x}, {self._dimensions.y}) '
            f'rotation=({self._rotation.w}, {self._rotation.x}, '
            f'{self._rotation.y}, {self._rotation.z})>'
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Rectangle3d):
            return False
        return (
            self._center == other._center and
            self._dimensions == other._dimensions and
            self._rotation == other._rotation
        )

    @property
    def center(self) -> VT3:
        return self._center

    @property
    def dimensions(self) -> VT2:
        return self._dimensions

    @property
    def rotation(self) -> QT:
        return self._rotation
