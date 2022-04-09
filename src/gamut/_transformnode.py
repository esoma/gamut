
from __future__ import annotations

__all__ = ['TransformNode']

# gamut
from gamut.math import FMatrix4
# python
from collections import deque
from typing import Any, Callable, Generic, Optional, TypeVar
from weakref import ref

T = TypeVar('T', bound='TransformNode')
C = TypeVar('C', bound='TransformNode')


class TransformNode(Generic[C]):

    def __init__(
        self: T,
        *,
        local_transform: FMatrix4 | None = None,
        parent: TransformNode[T] | None = None,
    ) -> None:
        if parent is not None:
            parent._children.add(self)
        self._parent: ref[TransformNode[T]] | None = (
            ref(parent)
            if parent is not None else
            None
        )
        self._children: set[C] = set()
        if local_transform is None:
            local_transform = FMatrix4(1)
        elif not isinstance(local_transform, FMatrix4):
            raise TypeError('local transform must be FMatrix4x4')
        self._local_transform = local_transform
        self._parent_transform: Optional[FMatrix4] = None
        self._transform: Optional[FMatrix4] = None

    def __del__(self) -> None:
        for child in tuple(self._children):
            child.parent = None

    def _check_for_cycle(self, parent: TransformNode[T]) -> None:
        if parent == self:
            raise ValueError('transform parent/child relationship cycle')
        chain: set[TransformNode[Any]] = {self}
        node: TransformNode[Any] | None = parent
        while node is not None:
            chain.add(node)
            node = node.parent
            if node in chain:
                raise ValueError('transform parent/child relationship cycle')

    @property
    def local_transform(self) -> FMatrix4:
        return self._local_transform

    @local_transform.setter
    def local_transform(self, value: FMatrix4) -> None:
        if not isinstance(value, FMatrix4):
            raise TypeError('local transform must be FMatrix4x4')
        if value != self._local_transform:
            self._transform = None
            self._local_transform = value

    @property
    def transform(self) -> FMatrix4:
        parent = self.parent
        if (parent is not None and
            self._parent_transform != parent.transform):
            self._parent_transform = None

        if (
            self._transform is None or
            (
                parent is not None and
                self._parent_transform is None
            )
        ):
            self._transform = self._local_transform
            if parent is not None:
                if self._parent_transform is None:
                    self._parent_transform = parent.transform
                self._transform = self._parent_transform @ self._transform

        return self._transform

    @property
    def parent(self: T) -> TransformNode[T] | None:
        if self._parent is not None:
            return self._parent()
        return None

    @parent.setter
    def parent(self: T, value: TransformNode[T] | None) -> None:
        parent = self.parent
        if value is not parent:
            if value is not None:
                self._check_for_cycle(value)
            if parent is not None:
                parent._children.remove(self)
            self._transform = None
            self._parent_transform = None
            if value is None:
                self._parent = None
            else:
                self._parent = ref(value)
                value._children.add(self)

    @property
    def children(self) -> set[C]:
        return set(self._children)

    def descend(self, f: Callable[[TransformNode], None]) -> None:
        queue: deque[TransformNode] = deque([self])
        while queue:
            node = queue.popleft()
            f(node)
            queue.extend(node.children)
