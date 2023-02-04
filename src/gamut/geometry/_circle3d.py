
from __future__ import annotations

__all__ = ['Circle3d']

# gamut
from ._error import DegenerateGeometryError
# gamut
from gamut.math import DVector3, FVector3
# python
from typing import Generic, TypeVar

VT = TypeVar('VT', FVector3, DVector3)


class Circle3d(Generic[VT]):

    class DegenerateError(DegenerateGeometryError):
        degenerate_form: VT

    def __init__(self, center: VT, radius: float, normal: VT):
        if not isinstance(center, (FVector3, DVector3)):
            raise TypeError('center must be FVector3 or DVector3')
        self._center = center

        try:
            self._radius = abs(float(radius))
        except (TypeError, ValueError):
            raise TypeError('radius must be float')
        if self._radius == 0:
            raise self.DegenerateError(center, 'degenerate 3d circle')

        if not isinstance(normal, type(self._center)):
            raise TypeError(f'normal must be {type(self._center).__name__}')
        if normal.magnitude == 0:
            raise ValueError('invalid normal')
        self._normal = normal.normalize()

    def __hash__(self) -> int:
        return hash((self._center, self._radius, self._normal))

    def __repr__(self) -> str:
        return (
            f'<gamut.geometry.Circle3d '
            f'center=({self._center.x}, {self._center.y}, {self._center.z}) '
            f'radius={self._radius} '
            f'normal=({self._normal.x}, {self._normal.y}, {self._normal.z})'
            f'>'
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Circle3d):
            return False
        return (
            self._center == other._center and
            self._radius == other._radius and
            self._normal == other._normal
        )

    @property
    def center(self) -> VT:
        return self._center

    @property
    def radius(self) -> float:
        return self._radius

    @property
    def normal(self) -> VT:
        return self._normal
