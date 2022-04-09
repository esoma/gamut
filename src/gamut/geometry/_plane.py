
from __future__ import annotations

__all__ = ['Plane']

# gamut
from gamut.math import (DMatrix4, DVector3, DVector4, FMatrix4, FVector3,
                        FVector4)
# python
# DVector4
from typing import Generic, overload, TypeVar

VT = TypeVar('VT', FVector3, DVector3)
MT = TypeVar('MT', FMatrix4, DMatrix4)


class Plane(Generic[VT, MT]):

    @overload
    def __init__(
        self: Plane[FVector3, FMatrix4],
        distance: float,
        normal: FVector3
    ):
        ...

    @overload
    def __init__(
        self: Plane[DVector3, DMatrix4],
        distance: float,
        normal: DVector3
    ):
        ...

    def __init__(self, distance: float, normal: VT):
        try:
            self._distance = float(distance)
        except (TypeError, ValueError):
            raise TypeError('distance must be float')

        if not isinstance(normal, (FVector3, DVector3)):
            raise TypeError('normal must be FVector3 or DVector3')
        self._normal = normal

        magnitude = normal.magnitude
        try:
            self._distance /= magnitude
            self._normal /= magnitude
        except ZeroDivisionError:
            raise ValueError('invalid normal')

    def __hash__(self) -> int:
        return id(self)

    def __repr__(self) -> str:
        return (
            f'<gamut.geometry.Plane distance={self._distance} '
            f'normal=({self._normal.x}, {self._normal.y}, {self._normal.z})>'
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Plane):
            return False
        return (
            self._normal == other._normal and
            self._distance == other._distance
        )

    def __rmatmul__(self, transform: MT) -> Plane:
        if not isinstance(transform, (FMatrix4, DMatrix4)):
            return NotImplemented

        if isinstance(self._normal, FVector3):
            vec4_type = FVector4
        else:
            assert isinstance(self._normal, DVector3)
            vec4_type = DVector4

        p = transform.inverse().transpose() @ vec4_type(
            *self._normal,
            self._distance
        )
        return Plane(p.w, p.xyz)

    @property
    def distance(self) -> float:
        return self._distance

    @property
    def normal(self) -> VT:
        return self._normal

    def distance_to_point(self, point: VT) -> float:
        if not isinstance(point, type(self._normal)):
            raise TypeError(f'point must be {type(self._normal).__name__}')
        return self._normal @ point + self._distance
