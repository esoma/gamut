
from __future__ import annotations

__all__ = ['ConvexHull']

# gamut
from gamut.glmhelp import F32Vector3, vec3_exact
# pyglm
from glm import mat4, vec3


class ConvexHull:

    def __init__(self, *points: F32Vector3):
        if not points:
            raise ValueError('must have at least 1 point')
        try:
            self._points = tuple(vec3_exact(p) for p in points)
        except TypeError:
            raise TypeError('each point must be vec3')

    def __hash__(self) -> int:
        return id(self)

    def __eq__(self, other: ConvexHull) -> bool:
        if not isinstance(other, ConvexHull):
            return False
        return self._points == other._points

    def __repr__(self) -> str:
        return f'<gamut.geometry.ConvexHull>'

    def __rmul__(self, transform: mat4) -> ConvexHull:
        if not isinstance(transform, mat4):
            return NotImplemented

        return ConvexHull(*(transform * c for c in self._points))

    @property
    def points(self) -> tuple[vec3, ...]:
        return tuple(vec3(p) for p in self._points)
