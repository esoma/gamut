
from __future__ import annotations
# python
from typing import Optional


class Pack2d:

    def __init__(
        self,
        max_size: tuple[int, int],
        max_bins: Optional[int],
    ):
        self._max_size = max_size
        self._max_bins = max_bins
        self._items: list[tuple[int, int]] = []
        self._unpacked_indexes: set[int] = set()
        self._atlases: list[Atlas] = []

    def add(self, size: tuple[int, int]) -> int:
        id = len(self._items)
        self._items.append(size)
        self._unpacked_indexes.add(id)
        return id

    def pack(self) -> None:
        unpacked = [self._items[i] for i in self._unpacked_indexes]
        unpacked.sort(key=lambda s: (-s[1], -s[0]))
        for unit in unpacked:
            for atlas in self._atlases:
                position = atlas.add(unit)
                if position:
                    break
            else:
                atlas = Atlas(self._max_size)
                self._atlases.append(atlas)
                position = atlas.add(unit)
                if not position:
                    raise RuntimeError('item is too large to pack')
            print(position)
        self._unpacked_indexes = set()

class Atlas:

    def __init__(self, max_size: tuple[int, int]):
        self.size = (0, 0)
        self.max_size = max_size
        self.lines: list[list[int]] = []

    def add(self, size: tuple[int, int]) -> Optional[tuple[int, int]]:
        # early out for things that are larger than the max atlas size
        if size[0] > self.max_size[0] or size[1] > self.max_size[1]:
            return None
        bottom = 0
        for i, (line_width, line_height) in enumerate(self.lines):
            bottom += line_height
            # lines may not exceed the width of the max width of the atlas
            if line_width + size[0] > self.max_size[0]:
                continue
            # only the last line can have its height expanded
            if (i + 1) < len(self.lines) and size[1] > line_height:
                continue
            position = (line_width, bottom - line_height)
            self.lines[i] = [line_width + size[0], max(line_height, size[1])]
            return position
        # thing is too vertically large to fit in a new line
        if bottom + size[1] > self.max_size[1]:
            return None
        self.lines.append(list(size))
        return (0, bottom)
