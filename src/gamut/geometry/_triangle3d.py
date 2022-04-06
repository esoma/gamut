
from __future__ import annotations

__all__ = ['Triangle3d']

# gamut
from gamut.math import DVector3, FVector3
# python
from typing import Generic, TypeVar

T = TypeVar('T', FVector3, DVector3)


class Triangle3d(Generic[T]):

    def __init__(self, a: T, b: T, c: T):
        if not isinstance(a, (FVector3, DVector3)):
            raise TypeError('a must be FVector3 or DVector3')
        self._a = a

        if not isinstance(b, type(a)):
            raise TypeError('b must be the same type as a')
        self._b = b

        if not isinstance(c, type(a)):
            raise TypeError('c must be the same type as a')
        self._c = c

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
        return {self._a, self._b, self._c} == {other._a, other._b, other._c}

    @property
    def a(self) -> T:
        return self._a

    @property
    def b(self) -> T:
        return self._b

    @property
    def c(self) -> T:
        return self._c

    @property
    def center(self) -> T:
        return (self._a + self._b + self._c) / 3

    @property
    def points(self) -> tuple[T, T, T]:
        return self._a, self._b, self._c
