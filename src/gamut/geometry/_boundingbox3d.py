
from __future__ import annotations

__all__ = ['BoundingBox3d']

# gamut
from ._sphere import Sphere
from ._viewfrustum3d import ViewFrustum3d
# gamut
from gamut.math import (DMatrix4, DVector3, DVector3Array, FMatrix4, FVector3,
                        FVector3Array)
# python
from typing import Generic, overload, TypeVar

T = TypeVar('T', FVector3Array, DVector3Array)
VT = TypeVar('VT', FVector3, DVector3)
MT = TypeVar('MT', FMatrix4, DMatrix4)


class BoundingBox3d(Generic[T, VT, MT]):

    @overload
    def __init__(
        self: BoundingBox3d[FVector3Array, FVector3, FMatrix4],
        points: FVector3Array
    ):
        ...

    @overload
    def __init__(
        self: BoundingBox3d[DVector3Array, DVector3, DMatrix4],
        points: DVector3Array
    ):
        ...

    def __init__(self, points: FVector3Array | DVector3Array):
        if not isinstance(points, (FVector3Array, DVector3Array)):
            raise TypeError('points must be FVector3Array or DVector3Array')
        if not points:
            raise ValueError('must have at least 1 point')

        self._array_type = type(points)

        if len(points) > 1:
            self._min = points.get_component_type()(
                min(*(v.x for v in points)),
                min(*(v.y for v in points)),
                min(*(v.z for v in points)),
            )
            self._max = points.get_component_type()(
                max(*(v.x for v in points)),
                max(*(v.y for v in points)),
                max(*(v.z for v in points)),
            )
        else:
            self._min = self._max = points[0]

    def __hash__(self) -> int:
        return hash((self._min, self._max))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, BoundingBox3d):
            return False
        return self._min == other._min and self._max == other._max

    def __repr__(self) -> str:
        return (
            f'<gamut.geometry.BoundingBox3d '
            f'min=({self._min.x}, {self._min.y}, {self._min.z}) '
            f'max=({self._max.x}, {self._max.y}, {self._max.z})>'
        )

    def __rmatmul__(self, transform: MT) -> BoundingBox3d[T, VT, MT]:
        if not isinstance(transform, (FMatrix4, DMatrix4)):
            return NotImplemented
        return BoundingBox3d(self._array_type(*(
            transform @ c for c in self.corners
        )))

    def _squared_distance_to_point(self, point: VT) -> float:
        result = 0.0
        for i in range(3):
            c = point[i]
            if c < self._min[i]:
                result += (self._min[i] - c) ** 2
            if c > self._max[i]:
                result += (self._max[i] - c) ** 2
        return result

    @property
    def center(self) -> VT:
        return (self._min + self._max) * .5

    @property
    def min(self) -> VT:
        return self._min

    @property
    def max(self) -> VT:
        return self._max

    @property
    def corners(self) -> tuple[VT, VT, VT, VT, VT, VT, VT, VT]:
        return tuple(
            self._array_type.get_component_type()(x, y, z)
            for x in (self._min.x, self._max.x)
            for y in (self._min.y, self._max.y)
            for z in (self._min.z, self._max.z)
        )

    def contains_point(self, point: VT) -> bool:
        expected_type = self._array_type.get_component_type()
        if not isinstance(point, expected_type):
            raise TypeError(f'point must be {expected_type.__name__}')
        return (
            all(p >= m for p, m in zip(point, self._min)) and
            all(p <= m for p, m in zip(point, self._max))
        )

    def intersects_sphere(self, sphere: Sphere) -> bool:
        return (
            self._squared_distance_to_point(sphere.center) <=
            (sphere.radius ** 2)
        )

    def seen_by(self, view_frustum: ViewFrustum3d) -> bool:
        for plane in view_frustum.planes:
            if all(plane.distance_to_point(c) < 0 for c in self.corners):
                return False
        return True
