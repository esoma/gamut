
from __future__ import annotations

__all__ = ['ViewFrustum3d']

# gamut
from ._plane import Plane
# gamut
from gamut.math import Matrix4


class ViewFrustum3d:

    def __init__(
        self,
        near_plane: Plane,
        far_plane: Plane,
        left_plane: Plane,
        right_plane: Plane,
        bottom_plane: Plane,
        top_plane: Plane,
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

    @classmethod
    def from_view_projection_transform(self, transform: Matrix4) -> Plane:
        if not isinstance(transform, Matrix4):
            raise TypeError('transform must be Matrix4')
        m = transform
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

    def __eq__(self, other: ViewFrustum3d) -> bool:
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

    def __rmatmul__(self, transform: Matrix4) -> Plane:
        if not isinstance(transform, Matrix4):
            return NotImplemented

        return ViewFrustum3d(*(transform @ p for p in self._planes))

    @property
    def near_plane(self) -> Plane:
        return self._near_plane

    @property
    def far_plane(self) -> Plane:
        return self._far_plane

    @property
    def left_plane(self) -> Plane:
        return self._left_plane

    @property
    def right_plane(self) -> Plane:
        return self._right_plane

    @property
    def top_plane(self) -> Plane:
        return self._top_plane

    @property
    def bottom_plane(self) -> Plane:
        return self._bottom_plane

    @property
    def planes(self) -> tuple[Plane, Plane, Plane, Plane, Plane, Plane]:
        return self._planes
