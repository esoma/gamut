
from __future__ import annotations

__all__ = ['BreakChunk', 'BreakMethod', 'break_never', 'break_line_icu']

# python
from typing import Callable, Final, Generator

try:
    # pyicu
    from icu import BreakIterator as IcuBreakIterator
    from icu import Locale as IcuLocale
except ImportError:
    IcuBreakIterator = None
    IcuLocale = None

# icu constants
UBRK_LINE_HARD: Final = 100


class BreakChunk:

    def __init__(self, text: str, *, force_newline: bool = False):
        self.text = text
        self.force_newline = force_newline


BreakMethod = Callable[[str], Generator[BreakChunk, None, None]]


def break_never(text: str) -> Generator[BreakChunk, None, None]:
    if not text:
        return
    yield BreakChunk(text)


if IcuBreakIterator:
    def break_line_icu(text: str) -> Generator[BreakChunk, None, None]:
        break_iter = IcuBreakIterator.createLineInstance(
            IcuLocale.getDefault()
        )
        break_iter.setText(text)
        previous_chunk_index = 0
        for next_chunk_index in break_iter:
            yield BreakChunk(
                text[previous_chunk_index:next_chunk_index],
                force_newline=break_iter.getRuleStatus() == UBRK_LINE_HARD
            )
            previous_chunk_index = next_chunk_index
else:
    def break_line_icu(text: str) -> Generator[BreakChunk, None, None]:
        raise RuntimeError('PyICU library not installed')
