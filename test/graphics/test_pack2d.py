
# gamut
from gamut.graphics import Pack2d, Packed2dItem
# python
from itertools import permutations
# pytest
import pytest


def test_init() -> None:
    pack = Pack2d((1, 1))
    assert pack.map == {}


def test_pack_nothing() -> None:
    pack = Pack2d((1, 1))
    pack.pack()
    assert pack.map == {}


@pytest.mark.parametrize("bin_width", [0, 1, 10, 100])
def test_pack_too_wide(bin_width: int) -> None:
    pack = Pack2d((bin_width, 100))
    pack.add((bin_width + 1, 1))
    with pytest.raises(RuntimeError) as excinfo:
        pack.pack()
    assert str(excinfo.value) == 'item is too large to pack'


@pytest.mark.parametrize("bin_height", [0, 1, 10, 100])
def test_pack_too_tall(bin_height: int) -> None:
    pack = Pack2d((100, bin_height))
    pack.add((1, bin_height + 1))
    with pytest.raises(RuntimeError) as excinfo:
        pack.pack()
    assert str(excinfo.value) == 'item is too large to pack'


@pytest.mark.parametrize("bins", [0, 1, 10])
def test_out_of_bins(bins: int) -> None:
    pack = Pack2d((100, 100), max_bins=bins)
    for i in range(bins + 1):
        pack.add((100, 100))
    with pytest.raises(RuntimeError) as excinfo:
        pack.pack()
    assert str(excinfo.value) == 'no space for item'


@pytest.mark.parametrize("width", [1, 10, 100])
@pytest.mark.parametrize("height", [1, 10, 100])
def test_pack_exact_size(width: int, height: int) -> None:
    pack = Pack2d((width, height))
    pack.add((width, height))
    pack.pack()
    assert pack.map == {
        0: Packed2dItem(0, (0, 0))
    }


def test_map_is_copy() -> None:
    pack = Pack2d((1, 1))
    pack.add((1, 1))
    pack.pack()
    map = pack.map
    assert pack.map is not pack.map
    map[100] = 1 # type: ignore
    assert 100 not in pack.map


def test_packed() -> None:
    pack = Pack2d((1, 1))
    pack.add((1, 1))
    pack.pack()
    packed = pack.map[0]
    assert packed.bin == 0
    assert packed.position == (0, 0)
    assert repr(packed) == '<gamut.graphics.Pack2dItem bin=0 position=(0, 0)>'


@pytest.mark.parametrize("width", [1, 10, 100])
@pytest.mark.parametrize("height", [1, 10, 100])
def test_pack_tight(width: int, height: int) -> None:
    pack = Pack2d((width, height))
    for i in range(width * height):
        pack.add((1, 1))
    pack.pack()
    assert pack.map == {
        i: Packed2dItem(0, (w, h))
        for i, (w, h) in enumerate((
            (w, h)
            for h in range(height)
            for w in range(width)
        ))
    }


@pytest.mark.parametrize("items", permutations([
    (51, 51),
    (50, 51),
    (49, 51),
]))
def test_backfill(items: list[tuple[int, int]]) -> None:
    pack = Pack2d((100, 100))
    for item in items:
        pack.add(item)
    pack.pack()
    assert pack.map == {
        items.index((51, 51)): Packed2dItem(0, (0, 0)),
        items.index((50, 51)): Packed2dItem(1, (0, 0)),
        items.index((49, 51)): Packed2dItem(0, (51, 0)),
    }


@pytest.mark.parametrize("items", permutations([
    (51, 50),
    (50, 50),
    (49, 50),
]))
def test_newline(items: list[tuple[int, int]]) -> None:
    pack = Pack2d((100, 100))
    for item in items:
        pack.add(item)
    pack.pack()
    assert pack.map == {
        items.index((51, 50)): Packed2dItem(0, (0, 0)),
        items.index((50, 50)): Packed2dItem(0, (0, 50)),
        items.index((49, 50)): Packed2dItem(0, (51, 0)),
    }


@pytest.mark.parametrize("items", permutations([
    (52, 30),
    (51, 20),
    (50, 10),
]))
def test_last_line_expansion(items: list[tuple[int, int]]) -> None:
    pack = Pack2d((100, 100))
    for item in items:
        pack.add(item)
    pack.pack()
    pack.add((10, 40))
    pack.add((50, 1))
    pack.pack()
    assert pack.map == {
        items.index((52, 30)): Packed2dItem(0, (0, 0)),
        items.index((51, 20)): Packed2dItem(0, (0, 30)),
        items.index((50, 10)): Packed2dItem(0, (0, 50)),
        3: Packed2dItem(0, (50, 50)),
        4: Packed2dItem(0, (0, 90)),
    }

@pytest.mark.parametrize("items", permutations([
    (10, 40),
    (52, 30),
    (51, 20),
    (50, 10),
    (50, 1),
]))
def test_repack(items: list[tuple[int, int]]) -> None:
    pack = Pack2d((100, 100))
    for item in items:
        pack.add(item)
        pack.pack()
    pack.repack()
    assert pack.map == {
        items.index((10, 40)): Packed2dItem(0, (0, 0)),
        items.index((52, 30)): Packed2dItem(0, (10, 0)),
        items.index((51, 20)): Packed2dItem(0, (0, 40)),
        items.index((50, 10)): Packed2dItem(0, (0, 60)),
        items.index((50, 1)): Packed2dItem(0, (50, 60)),
    }
