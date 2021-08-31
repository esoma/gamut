
# pytest
import pytest
# python
import gc


@pytest.fixture(autouse=True)
def run_gc_after_test():
    """This fixture helps avoid any weird interaction with failing tests and
    __del__ execution impacting other tests that would otherwise not fail.
    """
    yield
    gc.collect()
