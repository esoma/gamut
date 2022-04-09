
from __future__ import annotations

__all__ = ['ConvexHull']

# gamut
from gamut.math import DMatrix4, DVector3Array, FMatrix4, FVector3Array
# python
# DVector4
from typing import Generic, overload, TypeVar

AT = TypeVar('AT', FVector3Array, DVector3Array)
MT = TypeVar('MT', FMatrix4, DMatrix4)


class ConvexHull(Generic[AT, MT]):

    @overload
    def __init__(
        self: ConvexHull[FVector3Array, FMatrix4],
        points: FVector3Array
    ):
        ...

    @overload
    def __init__(
        self: ConvexHull[DVector3Array, DMatrix4],
        points: DVector3Array
    ):
        ...

    def __init__(self, points: AT):
        if not isinstance(points, (FVector3Array, DVector3Array)):
            raise TypeError('points must be FVector3Array or DVector3Array')
        if not points:
            raise ValueError('must have at least 1 point')
        self._points = points

    def __hash__(self) -> int:
        return id(self)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ConvexHull):
            return False
        return self._points == other._points

    def __repr__(self) -> str:
        return f'<gamut.geometry.ConvexHull>'

    def __rmatmul__(self, transform: MT) -> ConvexHull:
        if not isinstance(transform, (FMatrix4, DMatrix4)):
            return NotImplemented

        return ConvexHull(type(self.points)(*(
            transform @ c for c in self._points
        )))

    @property
    def points(self) -> AT:
        return self._points
