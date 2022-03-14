
# gamut
from gamut.graphics import Pack2d, Packed2dItem
from gamut.math import IVector2
# python
from itertools import permutations
# pytest
import pytest


def test_init() -> None:
    pack = Pack2d(IVector2(1, 1))
    assert pack.map == {}


def test_pack_nothing() -> None:
    pack = Pack2d(IVector2(1, 1))
    pack.pack()
    assert pack.map == {}


@pytest.mark.parametrize("bin_width", [0, 1, 10, 100])
def test_pack_too_wide(bin_width: int) -> None:
    pack = Pack2d(IVector2(bin_width, 100))
    pack.add(IVector2(bin_width + 1, 1))
    with pytest.raises(RuntimeError) as excinfo:
        pack.pack()
    assert str(excinfo.value) == 'item is too large to pack'


@pytest.mark.parametrize("bin_height", [0, 1, 10, 100])
def test_pack_too_tall(bin_height: int) -> None:
    pack = Pack2d(IVector2(100, bin_height))
    pack.add(IVector2(1, bin_height + 1))
    with pytest.raises(RuntimeError) as excinfo:
        pack.pack()
    assert str(excinfo.value) == 'item is too large to pack'


@pytest.mark.parametrize("bins", [0, 1, 10])
def test_out_of_bins(bins: int) -> None:
    pack = Pack2d(IVector2(100, 100), max_bins=bins)
    for i in range(bins + 1):
        pack.add(IVector2(100, 100))
    with pytest.raises(RuntimeError) as excinfo:
        pack.pack()
    assert str(excinfo.value) == 'no space for item'


@pytest.mark.parametrize("width", [1, 10, 100])
@pytest.mark.parametrize("height", [1, 10, 100])
def test_pack_exact_size(width: int, height: int) -> None:
    pack = Pack2d(IVector2(width, height))
    pack.add(IVector2(width, height))
    pack.pack()
    assert pack.map == {
        0: Packed2dItem(0, IVector2(0, 0))
    }


def test_map_is_copy() -> None:
    pack = Pack2d(IVector2(1, 1))
    pack.add(IVector2(1, 1))
    pack.pack()
    map = pack.map
    assert pack.map is not pack.map
    map[100] = 1 # type: ignore
    assert 100 not in pack.map


def test_packed() -> None:
    pack = Pack2d(IVector2(1, 1))
    pack.add(IVector2(1, 1))
    pack.pack()
    packed = pack.map[0]
    assert packed.bin == 0
    assert packed.position == IVector2(0, 0)
    assert repr(packed) == '<gamut.graphics.Pack2dItem bin=0 position=(0, 0)>'


@pytest.mark.parametrize("width", [1, 10, 100])
@pytest.mark.parametrize("height", [1, 10, 100])
def test_pack_tight(width: int, height: int) -> None:
    pack = Pack2d(IVector2(width, height))
    for i in range(width * height):
        pack.add(IVector2(1, 1))
    pack.pack()
    assert pack.map == {
        i: Packed2dItem(0, IVector2(w, h))
        for i, (w, h) in enumerate((
            (w, h)
            for h in range(height)
            for w in range(width)
        ))
    }


@pytest.mark.parametrize("items", permutations([
    IVector2(51, 51),
    IVector2(50, 51),
    IVector2(49, 51),
]))
def test_backfill(items: list[IVector2]) -> None:
    pack = Pack2d(IVector2(100, 100))
    for item in items:
        pack.add(item)
    pack.pack()
    assert pack.map == {
        items.index(IVector2(51, 51)): Packed2dItem(0, IVector2(0, 0)),
        items.index(IVector2(50, 51)): Packed2dItem(1, IVector2(0, 0)),
        items.index(IVector2(49, 51)): Packed2dItem(0, IVector2(51, 0)),
    }


@pytest.mark.parametrize("items", permutations([
    IVector2(51, 50),
    IVector2(50, 50),
    IVector2(49, 50),
]))
def test_newline(items: list[IVector2]) -> None:
    pack = Pack2d(IVector2(100, 100))
    for item in items:
        pack.add(item)
    pack.pack()
    assert pack.map == {
        items.index(IVector2(51, 50)): Packed2dItem(0, IVector2(0, 0)),
        items.index(IVector2(50, 50)): Packed2dItem(0, IVector2(0, 50)),
        items.index(IVector2(49, 50)): Packed2dItem(0, IVector2(51, 0)),
    }


@pytest.mark.parametrize("items", permutations([
    IVector2(52, 30),
    IVector2(51, 20),
    IVector2(50, 10),
]))
def test_last_line_expansion(items: list[IVector2]) -> None:
    pack = Pack2d(IVector2(100, 100))
    for item in items:
        pack.add(item)
    pack.pack()
    pack.add(IVector2(10, 40))
    pack.add(IVector2(50, 1))
    pack.pack()
    assert pack.map == {
        items.index(IVector2(52, 30)): Packed2dItem(0, IVector2(0, 0)),
        items.index(IVector2(51, 20)): Packed2dItem(0, IVector2(0, 30)),
        items.index(IVector2(50, 10)): Packed2dItem(0, IVector2(0, 50)),
        3: Packed2dItem(0, IVector2(50, 50)),
        4: Packed2dItem(0, IVector2(0, 90)),
    }

@pytest.mark.parametrize("items", permutations([
    IVector2(10, 40),
    IVector2(52, 30),
    IVector2(51, 20),
    IVector2(50, 10),
    IVector2(50, 1),
]))
def test_repack(items: list[IVector2]) -> None:
    pack = Pack2d(IVector2(100, 100))
    for item in items:
        pack.add(item)
        pack.pack()
    pack.repack()
    assert pack.map == {
        items.index(IVector2(10, 40)): Packed2dItem(0, IVector2(0, 0)),
        items.index(IVector2(52, 30)): Packed2dItem(0, IVector2(10, 0)),
        items.index(IVector2(51, 20)): Packed2dItem(0, IVector2(0, 40)),
        items.index(IVector2(50, 10)): Packed2dItem(0, IVector2(0, 60)),
        items.index(IVector2(50, 1)): Packed2dItem(0, IVector2(50, 60)),
    }
