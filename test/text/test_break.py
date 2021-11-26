
# gamut
from gamut.text import break_line_icu, break_never, BreakChunk
# pytest
import pytest

try:
    # pyicu
    import icu
except ImportError:
    icu = None


def test_break_never_empty() -> None:
    break_chunks = list(break_never(''))
    assert len(break_chunks) == 0


@pytest.mark.parametrize("text", [
    'hello world',
    'hello\nworld',
])
def test_break_never(text: str) -> None:
    break_chunks = list(break_never(text))
    assert len(break_chunks) == 1
    break_chunk = break_chunks[0]
    assert isinstance(break_chunk, BreakChunk)
    assert break_chunk.text == text
    assert not break_chunk.force_newline


@pytest.mark.skipif(icu is not None, reason='icu installed')
def test_break_line_icu_not_installed() -> None:
    with pytest.raises(RuntimeError) as excinfo:
        break_line_icu('')
    assert str(excinfo.value) == 'PyICU library not installed'


@pytest.mark.skipif(icu is None, reason='icu not installed')
def test_break_line_icu_empty() -> None:
    break_chunks = list(break_line_icu(''))
    assert len(break_chunks) == 0


@pytest.mark.skipif(icu is None, reason='icu not installed')
def test_break_line_icu_hello_world() -> None:
    break_chunks = list(break_line_icu('hello world'))
    assert len(break_chunks) == 2
    assert all(isinstance(c, BreakChunk) for c in break_chunks)
    hello_chunk, world_chunk = break_chunks
    assert hello_chunk.text == 'hello '
    assert not hello_chunk.force_newline
    assert world_chunk.text == 'world'
    assert not world_chunk.force_newline


@pytest.mark.skipif(icu is None, reason='icu not installed')
def test_break_line_icu_hello_n_world() -> None:
    break_chunks = list(break_line_icu('hello\nworld'))
    assert len(break_chunks) == 2
    assert all(isinstance(c, BreakChunk) for c in break_chunks)
    hello_chunk, world_chunk = break_chunks
    assert hello_chunk.text == 'hello\n'
    assert hello_chunk.force_newline
    assert world_chunk.text == 'world'
    assert not world_chunk.force_newline
