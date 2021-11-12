
from __future__ import annotations

__all__ = ['TransformNode']

# python
from typing import Optional
# pyglm
from glm import mat4


class TransformNode:

    def __init__(
        self,
        *,
        local_transform: Optional[mat4] = None,
        parent: Optional[TransformNode] = None
    ) -> None:
        self._parent = parent
        if local_transform is None:
            local_transform = mat4(1)
        self._local_transform = local_transform
        self._transform: Optional[mat4] = None

    @property
    def local_transform(self) -> mat4:
        return self._local_transform

    @local_transform.setter
    def local_transform(self, value: mat4) -> None:
        self._transform = None
        self._local_transform = value

    @property
    def transform(self) -> mat4:
        if self._transform is None:
            self._transform = self._local_transform
            if self._parent is not None:
                self._transform @= self._parent.transform
        return self._transform

    @property
    def parent(self) -> Optional[TransformNode]:
        return self._parent

    @parent.setter
    def parent(self, value: TransformNode) -> None:
        self._transform = None
        self._parent = value
