
# gamut
from gamut.event._event import reset_events
# python
import gc
from pathlib import Path
from typing import Any, Generator
# pysdl2
from sdl2 import (SDL_INIT_AUDIO, SDL_INIT_EVENTS, SDL_INIT_GAMECONTROLLER,
                  SDL_INIT_HAPTIC, SDL_INIT_JOYSTICK, SDL_INIT_TIMER,
                  SDL_INIT_VIDEO, SDL_WasInit)
# pytest
import pytest


def pytest_configure(config: Any) -> None:
    config.addinivalue_line(
        "controller", 'mark that a test modifies OS level controller data'
    )


@pytest.fixture
def resources() -> Path:
    return Path(__file__).parent / 'resources'


@pytest.fixture(autouse=True)
def cleanup(request: Any) -> Generator[Any, Any, None]:
    """This fixture helps to clean up any state that would persist between
    tests.
    """
    if SDL_WasInit(
        SDL_INIT_TIMER |
        SDL_INIT_AUDIO |
        SDL_INIT_VIDEO |
        SDL_INIT_JOYSTICK |
        SDL_INIT_HAPTIC |
        SDL_INIT_GAMECONTROLLER |
        SDL_INIT_EVENTS) != 0:
        pytest.exit('SDL in unexpected state, cannot continue testing')
    # do the test
    yield
    # make sure all events are reset so that the event futures don't persist
    # any tasks that are still waiting
    reset_events()
    # re-enable garbage collection in case it was disabled without re-enabling
    gc.enable()
    # force a garbage collection to get rid of anything that is still dangling
    # and hasn't had its __del__ resolved
    gc.collect()
    # make sure SDL was completley de-initialized
    assert SDL_WasInit(SDL_INIT_TIMER) == 0
    assert SDL_WasInit(SDL_INIT_AUDIO) == 0
    assert SDL_WasInit(SDL_INIT_VIDEO) == 0
    assert SDL_WasInit(SDL_INIT_JOYSTICK) == 0
    assert SDL_WasInit(SDL_INIT_HAPTIC) == 0
    assert SDL_WasInit(SDL_INIT_GAMECONTROLLER) == 0
    assert SDL_WasInit(SDL_INIT_EVENTS) == 0
