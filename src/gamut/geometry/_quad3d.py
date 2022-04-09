
from __future__ import annotations

__all__ = ['Quad3d']

# gamut
from ._viewfrustum3d import ViewFrustum3d
# gamut
from gamut.math import (DMatrix4, DVector3, DVector3Array, FMatrix4, FVector3,
                        FVector3Array)
# python
from typing import Any, Generic, overload, TypeVar

VT = TypeVar('VT', FVector3, DVector3)
AT = TypeVar('AT', FVector3Array, DVector3Array)
MT = TypeVar('MT', FMatrix4, DMatrix4)


class Quad3d(Generic[VT, AT, MT]):

    @overload
    def __init__(
        self: Quad3d[FVector3, FVector3Array, FMatrix4],
        point_0: FVector3,
        point_1: FVector3,
        point_2: FVector3,
        point_3: FVector3
    ):
        ...

    @overload
    def __init__(
        self: Quad3d[DVector3, DVector3Array, DMatrix4],
        point_0: DVector3,
        point_1: DVector3,
        point_2: DVector3,
        point_3: DVector3
    ):
        ...

    def __init__(
        self,
        point_0: VT,
        point_1: VT,
        point_2: VT,
        point_3: VT
    ):
        if isinstance(point_0, FVector3):
            self._points = FVector3Array(point_0, point_1, point_2, point_3)
        else:
            self._points = DVector3Array(point_0, point_1, point_2, point_3)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Quad3d):
            return False
        return self._points == other._points

    def __repr__(self) -> str:
        return (
            f'<gamut.geometry.Quad3d ('
            f'({self._points[0].x}, {self._points[0].y}, {self._points[0].z})'
            ', '
            f'({self._points[1].x}, {self._points[1].y}, {self._points[1].z})'
            ', '
            f'({self._points[2].x}, {self._points[2].y}, {self._points[2].z})'
            ', '
            f'({self._points[3].x}, {self._points[3].y}, {self._points[3].z})'
            ')>'
        )

    def __rmatmul__(self, transform: MT) -> Quad3d[VT, AT, MT]:
        if not isinstance(transform, (FMatrix4, DMatrix4)):
            return NotImplemented

        return Quad3d(*(transform @ p for p in self._points))

    @property
    def points(self) -> AT:
        return self._points

    def seen_by(self, view_frustum: ViewFrustum3d[VT, Any]) -> bool:
        for plane in view_frustum.planes:
            if all(plane.distance_to_point(p) < 0 for p in self._points):
                return False
        return True
