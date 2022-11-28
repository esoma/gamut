
from __future__ import annotations

__all__ = ['Plane']

# gamut
from ._linesegment3d import LineSegment3d
# gamut
from gamut._bullet import Shape
from gamut.math import (DMatrix4, DVector3, DVector4, FMatrix4, FVector3,
                        FVector4)
# python
from typing import Generic, overload, TypeVar

VT = TypeVar('VT', FVector3, DVector3)
MT = TypeVar('MT', FMatrix4, DMatrix4)


class Plane(Generic[VT, MT]):

    @overload
    def __init__(
        self: Plane[FVector3, FMatrix4],
        distance: float,
        normal: FVector3
    ):
        ...

    @overload
    def __init__(
        self: Plane[DVector3, DMatrix4],
        distance: float,
        normal: DVector3
    ):
        ...

    def __init__(self, distance: float, normal: VT):
        try:
            self._distance = float(distance)
        except (TypeError, ValueError):
            raise TypeError('distance must be float')

        if not isinstance(normal, (FVector3, DVector3)):
            raise TypeError('normal must be FVector3 or DVector3')
        self._normal = normal

        magnitude = normal.magnitude
        try:
            self._distance /= magnitude
            self._normal /= magnitude
        except ZeroDivisionError:
            raise ValueError('invalid normal')

        self._bt: Shape | None = None
        self._bt_capsule: Any = None

    def __hash__(self) -> int:
        return hash((self._distance, self._normal))

    def __repr__(self) -> str:
        return (
            f'<gamut.geometry.Plane distance={self._distance} '
            f'normal=({self._normal.x}, {self._normal.y}, {self._normal.z})>'
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Plane):
            return False
        return (
            self._normal == other._normal and
            self._distance == other._distance
        )

    def __rmatmul__(self, transform: MT) -> Plane:
        if not isinstance(transform, (FMatrix4, DMatrix4)):
            return NotImplemented

        if isinstance(self._normal, FVector3):
            vec4_type = FVector4
        else:
            assert isinstance(self._normal, DVector3)
            vec4_type = DVector4

        p = transform.inverse().transpose() @ vec4_type(
            *self._normal,
            self._distance
        )
        return Plane(p.w, p.xyz)

    def _get_bullet_shape(self) -> Shape:
        if self._bt is None:
            try:
                self._bt = Shape(False)
                self._bt_capsule = self._bt.add_plane(
                    self._distance,
                    *self._normal
                )
            except BaseException:
                self._bt = None
                self._bt_capsule = None
                raise
        return self._bt

    @property
    def distance(self) -> float:
        return self._distance

    @property
    def normal(self) -> VT:
        return self._normal

    def distance_to_point(self, point: VT) -> float:
        if not isinstance(point, type(self._normal)):
            raise TypeError(f'point must be {type(self._normal).__name__}')
        return self._normal @ point + self._distance

    def where_intersects_line_segment(
        self,
        line: LineSegment3d[VT],
        *,
        tolerance = 0.0
    ) -> VT:
        print("___")
        # handle degenerate line segments
        if line.is_degenerate:
            degen_form = line.degenerate_from
            assert isinstance(degen_form, type(line.a))
            if self.distance_to_point(degen_form) <= tolerance:
                return degen_form
            else:
                return None
        # math :^)
        ab = line.a - line.b
        den = self.normal @ ab
        if den == 0:
            return None
        d = (self.normal @ line.a - self._distance) / den
        if tolerance == 0 and (d < 0 or d > 1):
            return None
        p = line.a + ab * -d
        if tolerance != 0 and self.distance_to_point(p) > tolerance:
            return None
        return p