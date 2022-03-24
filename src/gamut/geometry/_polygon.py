
from __future__ import annotations

__all__ = ['Polygon']

# gamut
from ._mesh2d import Mesh2d
from ._triangulate import triangulate
# gamut
from gamut.math import Vector2Array


class Polygon:

    def __init__(
        self,
        exterior: Vector2Array,
        *,
        holes: Iterable[Vector2Array] | None = None
    ):
        if not isinstance(exterior, Vector2Array):
            raise TypeError('exterior must be Vector2Array')
        self._exterior = exterior

        self._holes: tuple[Vector2Array, ...] = ()
        if holes is not None:
            self._holes = tuple(holes)
            for hole in self._holes:
                if not isinstance(hole, Vector2Array):
                    raise TypeError('each hole must be Vector2Array')

    def __hash__(self) -> int:
        return id(self)

    def __eq__(self, other: Polygon) -> bool:
        if not isinstance(other, Polygon):
            return False
        return (
            self._exterior == other._exterior and
            self._holes == other._holes
        )

    def __repr__(self) -> str:
        return '<gamut.geometry.Polygon>'

    @property
    def exterior(self) -> Vector2Array:
        return self._exterior

    @property
    def holes(self) -> tuple[Vector2Array, ...]:
        return self._holes

    def triangulate(self) -> Mesh2d:
        return Mesh2d(*triangulate(self._exterior, *self._holes))
