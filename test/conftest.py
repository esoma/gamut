
# gamut
from gamut.event._event import reset_events
# python
import gc
from pathlib import Path
import sys
from typing import Any, Generator
import warnings
# pysdl2
from sdl2 import (SDL_INIT_AUDIO, SDL_INIT_EVENTS, SDL_INIT_GAMECONTROLLER,
                  SDL_INIT_HAPTIC, SDL_INIT_JOYSTICK, SDL_INIT_TIMER,
                  SDL_INIT_VIDEO, SDL_WasInit)
# pytest
import pytest


def pytest_configure(config: Any) -> None:
    config.addinivalue_line(
        "markers",
        'controller(): mark that a test modifies OS level controller data'
    )


@pytest.fixture
def resources() -> Path:
    return Path(__file__).parent / 'resources'


@pytest.fixture(autouse=True)
def cleanup(request: Any) -> Generator[Any, Any, None]:
    """This fixture helps to clean up any state that would persist between
    tests.
    """
    # make sure SDL is completley de-initialized
    sdl_timer_init = SDL_WasInit(SDL_INIT_TIMER) != 0
    sdl_audio_init = SDL_WasInit(SDL_INIT_AUDIO) != 0
    sdl_video_init = SDL_WasInit(SDL_INIT_VIDEO) != 0
    sdl_joystick_init = SDL_WasInit(SDL_INIT_JOYSTICK) != 0
    sdl_haptic_init = SDL_WasInit(SDL_INIT_HAPTIC) != 0
    sdl_gamecontroller_init = SDL_WasInit(SDL_INIT_GAMECONTROLLER) != 0
    sdl_events_init = SDL_WasInit(SDL_INIT_EVENTS) != 0
    if SDL_WasInit(
        SDL_INIT_TIMER |
        SDL_INIT_AUDIO |
        SDL_INIT_VIDEO |
        SDL_INIT_JOYSTICK |
        SDL_INIT_HAPTIC |
        SDL_INIT_GAMECONTROLLER |
        SDL_INIT_EVENTS) != 0:
        warnings.warn(f'{sdl_timer_init=}')
        warnings.warn(f'{sdl_audio_init=}')
        warnings.warn(f'{sdl_video_init=}')
        warnings.warn(f'{sdl_joystick_init=}')
        warnings.warn(f'{sdl_haptic_init=}')
        warnings.warn(f'{sdl_gamecontroller_init=}')
        warnings.warn(f'{sdl_events_init=}')
        warnings.warn('SDL in unexpected state, cannot continue testing')
        sys.exit(1)
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
