
from __future__ import annotations

__all__ = ['Pack2d', 'Packed2dItem']

# gamut
from gamut._glmhelp import I32Vector2, ivec2_exact
# python
from typing import Optional
# pyglm
from glm import ivec2


class Pack2d:

    def __init__(
        self,
        bin_size: I32Vector2,
        *,
        max_bins: Optional[int] = None,
    ):
        self._bin_size = ivec2_exact(bin_size)
        self._max_bins = max_bins
        self._items: list[ivec2] = []
        self._unpacked_indexes: set[int] = set()
        self._bins: list[Bin] = []
        self._map: dict[int, Packed2dItem] = {}

    def add(self, size: I32Vector2) -> int:
        size = ivec2_exact(size)
        id = len(self._items)
        self._items.append(size)
        self._unpacked_indexes.add(id)
        return id

    def pack(self) -> None:
        unpacked = [(i, self._items[i]) for i in self._unpacked_indexes]
        unpacked.sort(key=lambda s: (-s[1][1], -s[1][0]))
        for i, unit in unpacked:
            for bin_index, bin in enumerate(self._bins):
                position = bin.add(unit)
                if position:
                    break
            else:
                if self._max_bins is not None:
                    if len(self._bins) == self._max_bins:
                        raise RuntimeError('no space for item')
                    assert len(self._bins) < self._max_bins
                bin_index = len(self._bins)
                bin = Bin(self._bin_size)
                self._bins.append(bin)
                position = bin.add(unit)
                if not position:
                    raise RuntimeError('item is too large to pack')
            self._map[i] = Packed2dItem(bin_index, position)
        self._unpacked_indexes = set()

    def repack(self) -> None:
        self._unpacked_indexes = set(range(len(self._items)))
        self._map = {}
        self._bins = []
        self.pack()

    @property
    def map(self) -> dict[int, Packed2dItem]:
        return dict(self._map)


class Packed2dItem:

    def __init__(self, bin: int, position: ivec2):
        self._bin = bin
        self._position = position

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Packed2dItem):
            return NotImplemented
        return (
            self._bin == other._bin and
            self._position == other._position
        )

    @property
    def bin(self) -> int:
        return self._bin

    @property
    def position(self) -> ivec2:
        return ivec2(self._position)

    def __repr__(self) -> str:
        return (
            f'<gamut.graphics.Pack2dItem bin={self._bin} '
            f'position={tuple(self._position)}>'
        )


class Bin:

    def __init__(self, max_size: ivec2):
        self.max_size = max_size
        self.lines: list[list[int]] = []

    def add(self, size: ivec2) -> Optional[ivec2]:
        # early out for things that are larger than the max bin size
        if size[0] > self.max_size[0] or size[1] > self.max_size[1]:
            return None
        bottom = 0
        for i, (line_width, line_height) in enumerate(self.lines):
            bottom += line_height
            # lines may not exceed the width of the max width of the bin
            if line_width + size[0] > self.max_size[0]:
                continue
            # only the last line can have its height expanded
            if (i + 1) < len(self.lines) and size[1] > line_height:
                continue
            position = ivec2(line_width, bottom - line_height)
            self.lines[i] = [line_width + size[0], max(line_height, size[1])]
            return position
        # thing is too vertically large to fit in a new line
        if bottom + size[1] > self.max_size[1]:
            return None
        self.lines.append(list(size))
        return ivec2(0, bottom)
