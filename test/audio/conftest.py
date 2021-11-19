
# gamut
from gamut.audio._alcontext import (AlContext, get_al_context,
                                    LOOP_BACK_AVAILABLE, release_al_context,
                                    require_al_context)
# python
from typing import Any, Generator
# pytest
import pytest


@pytest.fixture
def loopback_al_context(request: Any) -> Generator[AlContext, None, None]:
    if not LOOP_BACK_AVAILABLE:
        pytest.skip('audio loopback not available')
    al_context_mark = require_al_context(loopback=LOOP_BACK_AVAILABLE)
    yield get_al_context()
    release_al_context(al_context_mark)
