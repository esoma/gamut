
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
        self._local_transform = mat4(local_transform)
        self._parent_transform: Optional[mat4] = None
        self._transform: Optional[mat4] = None

    def _check_for_cycle(self, parent: TransformNode) -> None:
        if parent == self:
            raise ValueError('transform parent/child relationship cycle')
        chain = {self}
        node: Optional[TransformNode] = parent
        while node is not None:
            chain.add(node)
            node = node.parent
            if node in chain:
                raise ValueError('transform parent/child relationship cycle')


    @property
    def local_transform(self) -> mat4:
        return mat4(self._local_transform)

    @local_transform.setter
    def local_transform(self, value: mat4) -> None:
        if value != self._local_transform:
            self._transform = None
            self._local_transform = mat4(value)

    @property
    def transform(self) -> mat4:
        if (self._parent is not None and
            self._parent_transform != self._parent.transform):
            self._parent_transform = None

        if (
            self._transform is None or
            (
                self._parent is not None and
                self._parent_transform is None
            )
        ):
            self._transform = mat4(self._local_transform)
            if self._parent is not None:
                if self._parent_transform is None:
                    self._parent_transform = self._parent.transform
                self._transform @= self._parent_transform

        return mat4(self._transform)

    @property
    def parent(self) -> Optional[TransformNode]:
        return self._parent

    @parent.setter
    def parent(self, value: TransformNode) -> None:
        if value is not self._parent:
            self._check_for_cycle(value)
            self._transform = None
            self._parent_transform = None
            self._parent = value
