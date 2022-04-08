
from __future__ import annotations

__all__ = ['Cylinder']

# gamut
from gamut.math import DQuaternion, DVector3, FQuaternion, FVector3
# python
from typing import Generic, overload, TypeVar

VT = TypeVar('VT', FVector3, DVector3)
QT = TypeVar('QT', FQuaternion, DQuaternion)


class Cylinder(Generic[VT, QT]):

    @overload
    def __init__(
        self: BoundingBox3d[FVector3, FQuaternion],
        center: FVector3,
        radius: float,
        height: float,
        *,
        rotation: FQuaternion | None = None
    ):
        ...

    @overload
    def __init__(
        self: BoundingBox3d[DVector3, DQuaternion],
        center: DVector3,
        radius: float,
        height: float,
        *,
        rotation: DQuaternion | None = None
    ):
        ...

    def __init__(
        self,
        center: FVector3 | DVector3,
        radius: float,
        height: float,
        *,
        rotation: FQuaternion | DQuaternion | None = None
    ):
        is_double = isinstance(center, DVector3)
        if not is_double and not isinstance(center, FVector3):
            raise TypeError('center must be FVector3 or DVector3')
        self._center = center

        try:
            self._radius = abs(float(radius))
        except (TypeError, ValueError):
            raise TypeError('radius must be float')

        try:
            self._height = abs(float(height))
        except (TypeError, ValueError):
            raise TypeError('height must be float')

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

    def __hash__(self) -> int:
        return id(self)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Cylinder):
            return False
        return (
            self._center == other._center and
            self._radius == other._radius and
            self._height == other._height and
            self._rotation == other._rotation
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
    def center(self) -> VT:
        return self._center

    @property
    def height(self) -> float:
        return self._height

    @property
    def radius(self) -> float:
        return self._radius

    @property
    def rotation(self) -> QT:
        return self._rotation
