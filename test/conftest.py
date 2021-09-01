
# pytest
import pytest
# python
import gc
from typing import Any, Generator


@pytest.fixture(autouse=True)
def run_gc_after_test() -> Generator[Any, Any, None]:
    """This fixture helps avoid any weird interaction with failing tests and
    __del__ execution impacting other tests that would otherwise not fail.
    """
    yield
    gc.collect()
