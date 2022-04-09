
from __future__ import annotations

__all__ = ['Shape3dCullable', 'Shape3dPointContainer']

# gamut
from ._viewfrustum3d import ViewFrustum3d
# gamut
from gamut.math import DVector3, FVector3
# python
from typing import Protocol, runtime_checkable


@runtime_checkable
class Shape3dCullable(Protocol):

    def seen_by(self, view_frustum: ViewFrustum3d) -> bool:
        ...


@runtime_checkable
class Shape3dPointContainer(Protocol):

    def contains_point(self, point: FVector3 | DVector3) -> bool:
        ...
