
from __future__ import annotations

__all__ = ['Polygon']

# gamut
from ._mesh2d import Mesh2d
from ._triangulate import triangulate_d, triangulate_f
# gamut
from gamut.math import DVector2Array, FVector2Array, UVector3Array
# python
from typing import Generic, overload, TypeVar

T = TypeVar('T', FVector2Array, DVector2Array)


class Polygon(Generic[T]):

    @overload
    def __init__(
        self: Polygon[FVector2Array],
        exterior: FVector2Array,
        *,
        holes: Iterable[FVector2Array] | None = None
    ):
        ...

    @overload
    def __init__(
        self: Polygon[DVector2Array],
        exterior: DVector2Array,
        *,
        holes: Iterable[DVector2Array] | None = None
    ):
        ...

    def __init__(
        self,
        exterior: FVector2Array | DVector2Array,
        *,
        holes: Iterable[FVector2Array | DVector2Array] | None = None
    ):
        if not isinstance(exterior, (FVector2Array, DVector2Array)):
            raise TypeError('exterior must be FVector2Array or DVector2Array')
        self._exterior = exterior

        self._holes: tuple[T, ...] = ()
        if holes is not None:
            self._holes = tuple(holes)
            for hole in self._holes:
                if not isinstance(hole, type(self._exterior)):
                    raise TypeError(
                        f'each hole must be {type(self._exterior).__name__}'
                    )

    def __hash__(self) -> int:
        return id(self)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Polygon):
            return False
        return (
            self._exterior == other._exterior and
            self._holes == other._holes
        )

    def __repr__(self) -> str:
        return '<gamut.geometry.Polygon>'

    @property
    def exterior(self) -> T:
        return self._exterior

    @property
    def holes(self) -> tuple[T, ...]:
        return self._holes

    def triangulate(self) -> Mesh2d[T, UVector3Array]:
        if isinstance(self._exterior, FVector2Array):
            return Mesh2d(*triangulate_f(self._exterior, *self._holes))
        else:
            return Mesh2d(*triangulate_d(self._exterior, *self._holes))
