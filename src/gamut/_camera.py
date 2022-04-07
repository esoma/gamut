
from __future__ import annotations

__all__ = ['Camera']

# gamut
from gamut._transformnode import TransformNode
from gamut.geometry import LineSegment3d, ViewFrustum3d
from gamut.math import FMatrix4, FVector3, FVector4
# python
from typing import Any, TypeVar

CT = TypeVar('CT', bound='Camera', covariant=True)


class Camera(TransformNode[Any]):

    def __init__(
        self: CT,
        projection_transform: FMatrix4,
        *,
        local_transform: FMatrix4 | None = None,
        parent: TransformNode[CT] | None = None
    ):
        super().__init__(local_transform=local_transform, parent=parent)
        if not isinstance(projection_transform, FMatrix4):
            raise TypeError('projection transform must be FMatrix4x4')
        self._projection = projection_transform
        self._inverse_projection = projection_transform.inverse()

    @property
    def view_projection_transform(self) -> FMatrix4:
        return self._projection @ self.transform.inverse()

    @property
    def view_frustum(self) -> ViewFrustum3d:
        return ViewFrustum3d.from_view_projection_transform(
            self.view_projection_transform.to_dmatrix()
        )

    @property
    def projection_transform(self) -> FMatrix4:
        return self._projection

    @property
    def view_transform(self) -> FMatrix4:
        return self.transform.inverse()

    def generate_ray(self, clip_position: FVector2) -> LineSegment3d[FVector3]:
        view = self.transform.inverse()
        start = (
            view @
            (self._inverse_projection @
            FVector4(*clip_position, -1, 1))
        )
        end = (
            view @
            (self._inverse_projection @
            FVector4(*clip_position, 1, 1))
        )
        start = start.xyz / start.w
        end = end.xyz / end.w
        return LineSegment3d(start, end)
