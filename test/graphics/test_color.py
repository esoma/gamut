
# gamut
from gamut.graphics import Color
# python
from typing import Any
# pytest
import pytest


def test_alpha_default() -> None:
    color = Color(0.0, 0.0, 0.0)
    assert color.alpha == 1.0


def test_min_zero() -> None:
    color = Color(-0.1, -0.1, -0.1, -0.1)
    assert color.red == 0.0
    assert color.green == 0.0
    assert color.blue == 0.0
    assert color.alpha == 0.0


def test_max_one() -> None:
    color = Color(1.1, 1.1, 1.1, 1.1)
    assert color.red == 1.0
    assert color.green == 1.0
    assert color.blue == 1.0
    assert color.alpha == 1.0


def test_float() -> None:
    color = Color(1, 1, 1, 1)
    assert color.red == 1.0
    assert color.green == 1.0
    assert color.blue == 1.0
    assert color.alpha == 1.0


@pytest.mark.parametrize("r", [0.0, .5, 1.0])
@pytest.mark.parametrize("g", [0.0, .5, 1.0])
@pytest.mark.parametrize("b", [0.0, .5, 1.0])
@pytest.mark.parametrize("a", [0.0, .5, 1.0])
def test_attributes(r: float, g: float, b: float, a: float) -> None:
    color = Color(r, g, b, a)
    assert color.red == r
    assert color.green == g
    assert color.blue == b
    assert color.alpha == a


@pytest.mark.parametrize("r", [0.0, .5, 1.0])
@pytest.mark.parametrize("g", [0.0, .5, 1.0])
@pytest.mark.parametrize("b", [0.0, .5, 1.0])
@pytest.mark.parametrize("a", [0.0, .5, 1.0])
def test_getitem(r: float, g: float, b: float, a: float) -> None:
    color = Color(r, g, b, a)
    assert color[0] == r
    assert color[1] == g
    assert color[2] == b
    assert color[3] == a
    assert color[-1] == a
    assert color[-2] == b
    assert color[-3] == g
    assert color[-4] == r


@pytest.mark.parametrize("index", [4, -5])
def test_getitem_index_out_of_range(index: int) -> None:
    color = Color(0, 0, 0, 0)
    with pytest.raises(IndexError):
        color[index]


@pytest.mark.parametrize("index", [None, 'text', 1.0, object()])
def test_getitem_index_invalid(index: Any) -> None:
    color = Color(0, 0, 0, 0)
    with pytest.raises(TypeError):
        color[index]


def test_len() -> None:
    color = Color(0, 0, 0, 0)
    assert len(color) == 4


@pytest.mark.parametrize("r", [0.0, .5, 1.0])
@pytest.mark.parametrize("g", [0.0, .5, 1.0])
@pytest.mark.parametrize("b", [0.0, .5, 1.0])
@pytest.mark.parametrize("a", [0.0, .5, 1.0])
def test_iter(r: float, g: float, b: float, a: float) -> None:
    color = Color(r, g, b, a)
    assert tuple(color) == (r, g, b, a)


@pytest.mark.parametrize("cmp", [
    Color(0.0, .25, .5, 1.0),
    (0.0, .25, .5, 1.0),
    [0.0, .25, .5, 1.0],
])
def test_eq(cmp: Any) -> None:
    color = Color(*cmp)
    assert color == cmp


@pytest.mark.parametrize("cmp", [
    Color(0.0, .25, .5, 1.0),
    (0.0, .25, .5, 1.0),
    [0.0, .25, .5, 1.0],
    None,
    object(),
    1,
    'test',
])
def test_not_eq(cmp: Any) -> None:
    color = Color(0.0, 0.0, 0.0, 0.0)
    assert color != cmp


@pytest.mark.parametrize("r", [0.0, .5, 1.0])
@pytest.mark.parametrize("g", [0.0, .5, 1.0])
@pytest.mark.parametrize("b", [0.0, .5, 1.0])
@pytest.mark.parametrize("a", [0.0, .5, 1.0])
def test_repr(r: float, g: float, b: float, a: float) -> None:
    color = Color(r, g, b, a)
    assert repr(color) == f'<gamut.Color {r}, {g}, {b}, {a}>'
