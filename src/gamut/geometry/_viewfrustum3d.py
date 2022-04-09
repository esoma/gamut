
from __future__ import annotations

__all__ = ['ViewFrustum3d']

# gamut
from ._plane import Plane
# gamut
from gamut.math import DMatrix4, DVector3, FMatrix4, FVector3
# python
from typing import Generic, overload, TypeVar

VT = TypeVar('VT', FVector3, DVector3)
MT = TypeVar('MT', FMatrix4, DMatrix4)


class ViewFrustum3d(Generic[VT, MT]):

    def __init__(
        self,
        near_plane: Plane[VT, MT],
        far_plane: Plane[VT, MT],
        left_plane: Plane[VT, MT],
        right_plane: Plane[VT, MT],
        bottom_plane: Plane[VT, MT],
        top_plane: Plane[VT, MT],
    ):
        if not isinstance(near_plane, Plane):
            raise TypeError('near plane must be Plane')
        if not isinstance(far_plane, Plane):
            raise TypeError('far plane must be Plane')
        if not isinstance(left_plane, Plane):
            raise TypeError('left plane must be Plane')
        if not isinstance(right_plane, Plane):
            raise TypeError('right plane must be Plane')
        if not isinstance(bottom_plane, Plane):
            raise TypeError('bottom plane must be Plane')
        if not isinstance(top_plane, Plane):
            raise TypeError('top plane must be Plane')

        self._near_plane = near_plane
        self._far_plane = far_plane
        self._left_plane = left_plane
        self._right_plane = right_plane
        self._bottom_plane = bottom_plane
        self._top_plane = top_plane
        self._planes = (
            near_plane,
            far_plane,
            left_plane,
            right_plane,
            bottom_plane,
            top_plane,
        )

    @overload
    @classmethod
    def from_view_projection_transform(
        cls,
        transform: FMatrix4
    ) -> ViewFrustum3d[FVector3, FMatrix4]:
        ...

    @overload
    @classmethod
    def from_view_projection_transform(
        cls,
        transform: DMatrix4
    ) -> ViewFrustum3d[DVector3, DMatrix4]:
        ...

    @classmethod
    def from_view_projection_transform(cls, transform: MT) -> ViewFrustum3d:
        if not isinstance(transform, (FMatrix4, DMatrix4)):
            raise TypeError('transform must be FMatrix4 or DMatrix4')
        r = [transform.get_row(i) for i in range(4)]
        return ViewFrustum3d(
            # near
            Plane(
                r[3].w + r[2].w,
                r[3].xyz + r[2].xyz,
            ),
            # far
            Plane(
                r[3].w - r[2].w,
                r[3].xyz - r[2].xyz,
            ),
            # left
            Plane(
                r[3].w + r[0].w,
                r[3].xyz + r[0].xyz,
            ),
            # right
            Plane(
                r[3].w - r[0].w,
                r[3].xyz - r[0].xyz,
            ),
            # bottom
            Plane(
                r[3].w + r[1].w,
                r[3].xyz + r[1].xyz,
            ),
            # top
            Plane(
                r[3].w - r[1].w,
                r[3].xyz - r[1].xyz,
            ),
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ViewFrustum3d):
            return False
        return all(p1 == p2 for p1, p2 in zip(self._planes, other._planes))

    def __repr__(self) -> str:
        return (
            f'<gamut.geometry.ViewFrustum3d '
            f'near_plane={self._near_plane} '
            f'far_plane={self._far_plane} '
            f'left_plane={self._left_plane} '
            f'right_plane={self._right_plane} '
            f'bottom_plane={self._bottom_plane} '
            f'top_plane={self._top_plane}>'
        )

    def __rmatmul__(self, transform: MT) -> ViewFrustum3d[VT, MT]:
        if not isinstance(transform, (FMatrix4, DMatrix4)):
            return NotImplemented
        return ViewFrustum3d(*(transform @ p for p in self._planes))

    @property
    def near_plane(self) -> Plane[VT, MT]:
        return self._near_plane

    @property
    def far_plane(self) -> Plane[VT, MT]:
        return self._far_plane

    @property
    def left_plane(self) -> Plane[VT, MT]:
        return self._left_plane

    @property
    def right_plane(self) -> Plane[VT, MT]:
        return self._right_plane

    @property
    def top_plane(self) -> Plane[VT, MT]:
        return self._top_plane

    @property
    def bottom_plane(self) -> Plane[VT, MT]:
        return self._bottom_plane

    @property
    def planes(self) -> tuple[
        Plane[VT, MT],
        Plane[VT, MT],
        Plane[VT, MT],
        Plane[VT, MT],
        Plane[VT, MT],
        Plane[VT, MT]
    ]:
        return self._planes
