
# gamut
from gamut.event._event import reset_events
# python
import gc
import os
from pathlib import Path
import signal
import time
from typing import Any, Generator
import warnings
# pysdl2
from sdl2 import (SDL_INIT_AUDIO, SDL_INIT_EVENTS, SDL_INIT_GAMECONTROLLER,
                  SDL_INIT_HAPTIC, SDL_INIT_JOYSTICK, SDL_INIT_TIMER,
                  SDL_INIT_VIDEO, SDL_Quit, SDL_WasInit)
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
    # exit if SDL isn't completley de-initialized
    sdl_timer_init = SDL_WasInit(SDL_INIT_TIMER) != 0
    sdl_audio_init = SDL_WasInit(SDL_INIT_AUDIO) != 0
    sdl_video_init = SDL_WasInit(SDL_INIT_VIDEO) != 0
    sdl_joystick_init = SDL_WasInit(SDL_INIT_JOYSTICK) != 0
    sdl_haptic_init = SDL_WasInit(SDL_INIT_HAPTIC) != 0
    sdl_gamecontroller_init = SDL_WasInit(SDL_INIT_GAMECONTROLLER) != 0
    sdl_events_init = SDL_WasInit(SDL_INIT_EVENTS) != 0
    if (
        sdl_timer_init or
        sdl_audio_init or
        sdl_video_init or
        sdl_joystick_init or
        sdl_haptic_init or
        sdl_gamecontroller_init or
        sdl_events_init
    ) != 0:
        if sdl_timer_init:
            warnings.warn(f'SDL Timer Subsystem Initialized')
        if sdl_audio_init:
            warnings.warn(f'SDL Audio Subsystem Initialized')
        if sdl_video_init:
            warnings.warn(f'SDL Video Subsystem Initialized')
        if sdl_joystick_init:
            warnings.warn(f'SDL Joystick Subsystem Initialized')
        if sdl_haptic_init:
            warnings.warn(f'SDL Haptic Subsystem Initialized')
        if sdl_gamecontroller_init:
            warnings.warn(f'SDL Game Controller Subsystem Initialized')
        if sdl_events_init:
            warnings.warn(f'SDL Events Subsystem Initialized')
        warnings.warn('SDL in unexpected state, cannot continue testing')
        # the sleep is necessary to avoid killing this process before
        # pytest-xdist has had a chance to send some additional data (or
        # something like that)
        time.sleep(.5)
        os.kill(os.getpid(), signal.SIGSEGV)
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
    # totally shutdown SDL
    SDL_Quit()
