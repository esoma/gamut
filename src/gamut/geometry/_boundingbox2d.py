
from __future__ import annotations

__all__ = ['BoundingBox2d']

# gamut
from gamut.math import DVector2, DVector2Array, FVector2, FVector2Array
# python
from typing import Generic, overload, TypeVar

T = TypeVar('T', FVector2Array, DVector2Array)
VT = TypeVar('VT', FVector2, DVector2)


class BoundingBox2d(Generic[T, VT]):

    @overload
    def __init__(
        self: BoundingBox2d[FVector2Array, FVector2],
        points: FVector2Array
    ):
        ...

    @overload
    def __init__(
        self: BoundingBox2d[DVector2Array, DVector2],
        points: DVector2Array
    ):
        ...

    def __init__(self, points: FVector2Array | DVector2Array):
        if not isinstance(points, (FVector2Array, DVector2Array)):
            raise TypeError('points must be FVector2Array or DVector2Array')
        if not points:
            raise ValueError('must have at least 1 point')

        self._array_type = type(points)

        if len(points) > 1:
            self._min = points.get_component_type()(
                min(*(v.x for v in points)),
                min(*(v.y for v in points)),
            )
            self._max = points.get_component_type()(
                max(*(v.x for v in points)),
                max(*(v.y for v in points)),
            )
        else:
            self._min = self._max = points[0]

    def __hash__(self) -> int:
        return hash((self._min, self._max))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, BoundingBox2d):
            return False
        return self._min == other._min and self._max == other._max

    def __repr__(self) -> str:
        return (
            f'<gamut.geometry.BoundingBox2d '
            f'min=({self._min.x}, {self._min.y}) '
            f'max=({self._max.x}, {self._max.y})>'
        )

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
    def corners(self) -> tuple[VT, VT, VT, VT]:
        return tuple(
            self._array_type.get_component_type()(x, y)
            for x in (self._min.x, self._max.x)
            for y in (self._min.y, self._max.y)
        )

    def contains_point(self, point: VT) -> bool:
        expected_type = self._array_type.get_component_type()
        if not isinstance(point, expected_type):
            raise TypeError(f'point must be {expected_type.__name__}')
        return (
            all(p >= m for p, m in zip(point, self._min)) and
            all(p <= m for p, m in zip(point, self._max))
        )

    def intersects_bounding_box_2d_exclusive(
        self,
        other: BoundingBox2d[T, VT]
    ) -> bool:
        if self._min.x >= other._max.x:
            return False
        if self._max.x <= other._min.x:
            return False
        if self._min.y >= other._max.y:
            return False
        if self._max.y <= other._min.y:
            return False
        return True

    def intersects_bounding_box_2d_inclusive(
        self,
        other: BoundingBox2d[T, VT]
    ) -> bool:
        if self._min.x > other._max.x:
            return False
        if self._max.x < other._min.x:
            return False
        if self._min.y > other._max.y:
            return False
        if self._max.y < other._min.y:
            return False
        return True
