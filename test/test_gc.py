
# gamut
import gamut.gc
from gamut.graphics import Buffer


def test_no_context() -> None:
    gamut.gc.collect()


def test_with_context() -> None:
    dummy_buffer = Buffer()
    gamut.gc.collect()
