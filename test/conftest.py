
# gamut
# gamut
# gamut
from gamut.event._event import reset_events
# python
import gc
from typing import Any, Generator
# pytest
import pytest


@pytest.fixture(autouse=True)
def cleanup() -> Generator[Any, Any, None]:
    """This fixture helps to clean up any state that would persist between
    tests.
    """
    yield
    # make sure all events are reset so that the event futures don't persist
    # any tasks that are still waiting
    reset_events()
    # force a garbage collection to get rid of anything that is still dangling
    # and hasn't had its __del__ resolved
    gc.collect()
