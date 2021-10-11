
__all__ = [
    'skip_if_any_real_controllers',
    'skip_if_virtual_controller_nyi',
    'VirtualController',
]

# python
from sys import platform
from typing import TypeVar
# pysdl2
from sdl2 import (SDL_GetError, SDL_Init, SDL_INIT_JOYSTICK, SDL_NumJoysticks,
                  SDL_QuitSubSystem)

if platform == 'linux':
    # gamut
    from ._uinput import VirtualController
else:
    from ._nyi import VirtualController # type: ignore

# gamut
from ._nyi import VirtualController as NyiVirtualController
# pytest
import pytest

T = TypeVar('T')

def skip_if_virtual_controller_nyi(func: T) -> T:
    if VirtualController is NyiVirtualController: # type: ignore
        return pytest.mark.skip( # type: ignore
            reason='Virtual Controller NYI'
        )(func)
    return func


if SDL_Init(SDL_INIT_JOYSTICK) == 0:
    any_real_controllers = SDL_NumJoysticks() > 0
    SDL_QuitSubSystem(SDL_INIT_JOYSTICK)
else:
    raise RuntimeError(SDL_GetError().decode('utf8'))

def skip_if_any_real_controllers(func: T) -> T:
    if any_real_controllers:
        return pytest.mark.skip( # type: ignore
            reason='Real controllers connected.'
        )(func)
    return func
