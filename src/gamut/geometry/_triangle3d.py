
from __future__ import annotations

__all__ = ['Triangle3d']

# gamut
from gamut.math import DVector3, FVector3
# python
from typing import Generic, TypeVar

T = TypeVar('T', FVector3, DVector3)


class Triangle3d(Generic[T]):

    def __init__(self, point_0: T, point_1: T, point_2: T, /):
        if not isinstance(point_0, (FVector3, DVector3)):
            raise TypeError('point 0 must be FVector3 or DVector3')
        if not isinstance(point_1, type(point_0)):
            raise TypeError('point 1 must be the same type as point 0')
        if not isinstance(point_2, type(point_0)):
            raise TypeError('point 2 must be the same type as point 0')

        self._positions = (point_0, point_1, point_2)

    def __hash__(self) -> int:
        return id(self)

    def __repr__(self) -> str:
        return (
            f'<gamut.geometry.Triangle3d '
            f'{(tuple(self._a), tuple(self._b), tuple(self._c))}>'
        )

    def __eq__(self, other: Triangle3d) -> bool:
        if not isinstance(other, Triangle3d):
            return False

        other_iter = enumerate(other.positions)
        i, other_point = next(other_iter)
        for point in (*self.positions, *self.positions):
            if point == other_point:
                try:
                    i, other_point = next(other_iter)
                except StopIteration:
                    return True
            elif i != 0:
                return False
        return False

    @property
    def center(self) -> T:
        return (self._a + self._b + self._c) / 3

    @property
    def positions(self) -> tuple[T, T, T]:
        return self._positions
