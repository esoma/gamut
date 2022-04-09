
from __future__ import annotations

__all__ = ['Composite3d']

# gamut
from ._viewfrustum3d import ViewFrustum3d
# gamut
from gamut.math import DMatrix4, DVector3, FMatrix4, FVector3
# python
from typing import Generator, Generic, TypeVar

S = TypeVar('S')


class Composite3d(Generic[S]):

    def __init__(self, *shapes: S):
        self._shapes = tuple(shapes)

    def __hash__(self) -> int:
        return id(self)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Composite3d):
            return False
        if len(self._shapes) != len(other._shapes):
            return False

        other_shapes = list(other._shapes)
        for shape in self._shapes:
            try:
                other_shapes.remove(shape)
            except ValueError:
                return False
        return True

    def __repr__(self) -> str:
        shape_reprs = ', '.join(repr(s) for s in self._shapes)
        return f'<gamut.geometry.Composite3d ({shape_reprs})>'

    def __rmatmul__(self, transform: FMatrix4 | DMatrix4) -> Composite3d[S]:
        if not isinstance(transform, (FMatrix4, DMatrix4)):
            return NotImplemented

        return Composite3d(*(transform @ s for s in self._shapes))

    @property
    def shapes(self) -> tuple[S, ...]:
        return self._shapes

    @property
    def shapes_flattened(self) -> Generator[S, None, None]:
        for shape in self._shapes:
            if isinstance(shape, Composite3d):
                yield from shape.shapes_flattened
            else:
                yield shape

    def contains_point(self, point: FVector3 | DVector3) -> bool:
        for shape in self._shapes:
            try:
                f = shape.contains_point
            except AttributeError:
                continue
            if f(point):
                return True
        return False

    def seen_by(self, view_frustum: ViewFrustum3d) -> bool:
        for shape in self._shapes:
            try:
                f = shape.seen_by
            except AttributeError:
                continue
            if f(view_frustum):
                return True
        return False
