
from __future__ import annotations

__all__ = ['Triangle3d']

# gamut
from ._error import DegenerateGeometryError
from ._linesegment3d import LineSegment3d
# gamut
from gamut.math import DVector3, FVector3
# python
from math import isnan
from typing import Generic, TypeVar

T = TypeVar('T', FVector3, DVector3)


class Triangle3d(Generic[T]):

    class DegenerateError(DegenerateGeometryError):
        degenerate_form: LineSegment3d[T] | T

    def __init__(self, point_0: T, point_1: T, point_2: T, /):
        if not isinstance(point_0, (FVector3, DVector3)):
            raise TypeError('point 0 must be FVector3 or DVector3')
        if not isinstance(point_1, type(point_0)):
            raise TypeError('point 1 must be the same type as point 0')
        if not isinstance(point_2, type(point_0)):
            raise TypeError('point 2 must be the same type as point 0')

        self._positions = (point_0, point_1, point_2)
        i = sorted(enumerate(self._positions), key=lambda x: x[1])[0][0]
        self._positions = self._positions[i:] + self._positions[:i]

        d_edge_0 = self._positions[1] - self._positions[0]
        d_edge_1 = self._positions[0] - self._positions[2]
        self._normal = -d_edge_0.cross(d_edge_1).normalize()

        if isnan(self._normal.x):
            raise self.DegenerateError(
                self._get_degenerate_form(),
                'degenerate triangle'
            )

    def __hash__(self) -> int:
        return hash(self._positions)

    def __repr__(self) -> str:
        return (
            f'<gamut.geometry.Triangle3d '
            f'{tuple(tuple(p) for p in self._positions)}>'
        )

    def __eq__(self, other: Triangle3d) -> bool:
        if not isinstance(other, Triangle3d):
            return False
        return self._positions == other._positions

    def _get_degenerate_form(self) -> T | LineSegment3d[T]:
        unique_points = set(self._positions)
        if len(unique_points) == 1:
            return next(iter(unique_points))
        elif len(unique_points) == 2:
            a, b = unique_points
            for ea, eb in (
                (self._positions[0], self._positions[1]),
                (self._positions[1], self._positions[2]),
                (self._positions[2], self._positions[0]),
            ):
                if (
                    (ea == a and eb == b) or
                    (ea == b and eb == a)
                ):
                    return LineSegment3d(ea, eb)
        segment_distance = [
            (a, b, a.distance(b))
            for a, b in (
                (self._positions[0], self._positions[1]),
                (self._positions[1], self._positions[2]),
                (self._positions[2], self._positions[0])
            )
        ]
        segment_distance.sort(key=lambda s: s[2])
        seg = segment_distance[-1]
        return LineSegment3d(seg[0], seg[1])

    @property
    def center(self) -> T:
        return sum(self._positions) / 3

    @property
    def positions(self) -> tuple[T, T, T]:
        return self._positions

    @property
    def edges(self) -> tuple[
        LineSegment3d[T],
        LineSegment3d[T],
        LineSegment3d[T]
    ]:
        return (
            LineSegment3d(self._positions[0], self._positions[1]),
            LineSegment3d(self._positions[1], self._positions[2]),
            LineSegment3d(self._positions[2], self._positions[0]),
        )
