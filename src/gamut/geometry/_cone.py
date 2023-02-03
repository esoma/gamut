
from __future__ import annotations

__all__ = ['Cone']

# gamut
from ._error import DegenerateGeometryError
# gamut
from gamut._bullet import Shape
from gamut.math import DQuaternion, DVector3, FQuaternion, FVector3
# python
from typing import Generic, overload, TypeVar

VT = TypeVar('VT', FVector3, DVector3)
QT = TypeVar('QT', FQuaternion, DQuaternion)


class Cone(Generic[VT, QT]):

    class DegenerateError(DegenerateGeometryError):
        degenerate_form: VT

    @overload
    def __init__(
        self: Cone[FVector3, FQuaternion],
        center: FVector3,
        radius: float,
        height: float,
        *,
        rotation: FQuaternion | None = None
    ):
        ...

    @overload
    def __init__(
        self: Cone[DVector3, DQuaternion],
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

        if radius == 0 or height == 0:
            raise self.DegenerateError(center, 'degenerate cone')

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
        return hash((self._center, self._radius, self._height, self._rotation))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Cone):
            return False
        return (
            self._center == other._center and
            self._radius == other._radius and
            self._height == other._height and
            self._rotation == other._rotation
        )

    def __repr__(self) -> str:
        return (
            f'<gamut.geometry.Cone '
            f'center=({self._center.x}, {self._center.y}, {self._center.z}) '
            f'radius={self._radius} height={self._height} '
            f'rotation=({self._rotation.w}, {self._rotation.x}, '
            f'{self._rotation.y}, {self._rotation.z})>'
        )

    def _get_bullet_shape(self) -> Shape:
        if self._bt is None:
            try:
                self._bt = Shape(False)
                self._bt_capsule = self._bt.add_cone(
                    self._radius,
                    self._height,
                    *self._center,
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
    def height(self) -> float:
        return self._height

    @property
    def radius(self) -> float:
        return self._radius

    @property
    def rotation(self) -> QT:
        return self._rotation
