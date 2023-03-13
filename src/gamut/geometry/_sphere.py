
from __future__ import annotations

__all__ = ['Sphere']

# gamut
from ._error import DegenerateGeometryError
from ._viewfrustum3d import ViewFrustum3d
# gamut
from gamut._bullet import Shape
from gamut.math import DMatrix4, DVector3, FMatrix4, FVector3
# python
from typing import Any, Generic, overload, TypeVar

VT = TypeVar('VT', FVector3, DVector3)
MT = TypeVar('MT', FMatrix4, DMatrix4)


class Sphere(Generic[VT, MT]):

    class DegenerateError(DegenerateGeometryError):
        degenerate_form: VT

    @overload
    def __init__(
        self: Sphere[FVector3, FMatrix4],
        center: FVector3,
        radius: float
    ):
        ...

    @overload
    def __init__(
        self: Sphere[DVector3, DMatrix4],
        center: DVector3,
        radius: float
    ):
        ...

    def __init__(self, center: VT, radius: float):
        if not isinstance(center, (FVector3, DVector3)):
            raise TypeError('center must be FVector3 or DVector3')
        self._center = center

        try:
            self._radius = abs(float(radius))
        except (TypeError, ValueError):
            raise TypeError('radius must be float')

        if self._radius == 0:
            raise self.DegenerateError(center, 'degenerate sphere')

        self._bt: Shape | None = None
        self._bt_capsule: Any = None

    def __hash__(self) -> int:
        return hash((self._center, self._radius))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Sphere):
            return False
        return (
            self._center == other._center and
            self._radius == other._radius
        )

    def __repr__(self) -> str:
        return (
            f'<gamut.geometry.Sphere '
            f'center=({self._center.x}, {self._center.y}, {self._center.z}) '
            f'radius={self._radius}>'
        )

    def __rmatmul__(self, transform: MT) -> Sphere:
        if not isinstance(transform, (FMatrix4, DMatrix4)):
            return NotImplemented

        max_scale = max(DVector3(*(c.xyz.magnitude for c in (
            transform[0],
            transform[1],
            transform[2],
        ))))
        return Sphere(
            transform @ self._center,
            self._radius * max_scale,
        )

    def _get_bullet_shape(self) -> Shape:
        if self._bt is None:
            try:
                self._bt = Shape(False)
                self._bt_capsule = self._bt.add_sphere(
                    self._radius,
                    *self._center,
                )
            except BaseException:
                self._bt = None
                self._bt_capsule = None
                raise
        return self._bt

    @property
    def center(self) -> VT:
        return self._center

    @property
    def radius(self) -> float:
        return self._radius

    def contains_point(self, point: VT) -> bool:
        if not isinstance(point, type(self._center)):
            raise TypeError(f'point must be {type(self._center).__name__}')

        return (self._center - point).magnitude <= self._radius

    def seen_by(self, view_frustum: ViewFrustum3d[VT, Any]) -> bool:
        for plane in view_frustum.planes:
            distance = plane.distance_to_point(self.center)
            if distance < -self.radius:
                return False
        return True
