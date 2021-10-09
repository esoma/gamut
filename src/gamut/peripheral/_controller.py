
from __future__ import annotations

__all__ = [
    'Controller',
]

# gamut
from ._peripheral import (Peripheral, PeripheralConnected,
                          PeripheralDisconnected, PeripheralEvent)
# gamut
from gamut._sdl import sdl_event_callback_map
# python
from typing import Any, Optional, Sequence, TYPE_CHECKING
from weakref import ref
# pysdl2
from sdl2 import (SDL_GetError, SDL_JOYDEVICEADDED, SDL_JOYDEVICEREMOVED,
                  SDL_JoystickClose, SDL_JoystickFromInstanceID,
                  SDL_JoystickInstanceID, SDL_JoystickName,
                  SDL_JoystickNumAxes, SDL_JoystickNumButtons,
                  SDL_JoystickOpen)

if TYPE_CHECKING:
    # gamut
    from ._keyboard import Keyboard
    from ._mouse import Mouse


class ControllerEvent(PeripheralEvent, peripheral=...):
    peripheral: Controller

    @property
    def controller(self) -> Controller:
        return self.peripheral


class ControllerConnected(ControllerEvent, PeripheralConnected,
    peripheral=...
):
    pass


class ControllerDisconnected(ControllerEvent, PeripheralDisconnected,
    peripheral=...
):
    pass


class ControllerAxis:

    def __init__(self, controller: Controller, index: int):
        self._index = index
        self._position = 0.0
        self._controller: ref[Controller] = ref(controller)

    def __repr__(self) -> str:
        identifier = repr(self._index)
        if self._controller:
            controller = self._controller()
            if controller:
                identifier = f'{identifier} for {controller!r}'
        return f'<gamut.peripheral.ControllerAxis {identifier}>'

    @property
    def index(self) -> int:
        return self._index

    @property
    def position(self) -> float:
        return self._position


class ControllerButton:

    def __init__(self, controller: Controller, index: int):
        self._index = index
        self._is_pressed = False
        self._controller: ref[Controller] = ref(controller)

    def __repr__(self) -> str:
        identifier = repr(self._index)
        if self._controller:
            controller = self._controller()
            if controller:
                identifier = f'{identifier} for {controller!r}'
        return f'<gamut.peripheral.ControllerButton {identifier}>'

    @property
    def index(self) -> int:
        return self._index

    @property
    def is_pressed(self) -> bool:
        return self._is_pressed


class Controller(Peripheral):

    Event: type[ControllerEvent]
    Connected: type[ControllerConnected]
    Disconnected: type[ControllerDisconnected]

    def __init__(self, name: str, button_count: int, axis_count: int):
        super().__init__(name)
        class Event(ControllerEvent, self.Event): # type: ignore
            pass
        self.Event = Event
        class Connected( # type: ignore
            ControllerConnected,
            Event,
            self.Connected, # type: ignore
        ):
            pass
        self.Connected = Connected
        class Disconnected( # type: ignore
            ControllerDisconnected,
            Event,
            self.Disconnected, # type: ignore
        ):
            pass
        self.Disconnected = Disconnected

        self._buttons = tuple(
            ControllerButton(self, i)
            for i in range(button_count)
        )
        self._axes = tuple(
            ControllerAxis(self, i)
            for i in range(axis_count)
        )

    def __repr__(self) -> str:
        return f'<gamut.peripheral.Controller {self._name!r}>'

    @property
    def buttons(self) -> Sequence[ControllerButton]:
        return self._buttons

    @property
    def axes(self) -> Sequence[ControllerAxis]:
        return self._axes


def sdl_joy_device_added_event_callback(
    sdl_event: Any,
    mouse: Mouse,
    keyboard: Keyboard,
    controllers: dict[Any, Controller]
) -> ControllerConnected:
    sdl_device_index: int = sdl_event.jdevice.which

    sdl_joystick = SDL_JoystickOpen(sdl_device_index)
    if not sdl_joystick:
        raise RuntimeError(SDL_GetError().decode('utf8'))

    sdl_joystick_index = SDL_JoystickInstanceID(sdl_joystick)
    if sdl_joystick_index < 0:
        raise RuntimeError(SDL_GetError().decode('utf8'))

    joystick_name = SDL_JoystickName(sdl_joystick)
    if joystick_name is None:
        raise RuntimeError(SDL_GetError().decode('utf8'))

    axis_count: int = SDL_JoystickNumAxes(sdl_joystick)
    if axis_count < 0:
        raise RuntimeError(SDL_GetError().decode('utf8'))

    button_count: int = SDL_JoystickNumButtons(sdl_joystick)
    if button_count < 0:
        raise RuntimeError(SDL_GetError().decode('utf8'))

    controllers[sdl_joystick_index] = controller = Controller(
        joystick_name.decode('utf8'),
        button_count,
        axis_count
    )

    event = controller.connect()
    assert isinstance(event, ControllerConnected)
    return event

assert SDL_JOYDEVICEADDED not in sdl_event_callback_map
sdl_event_callback_map[SDL_JOYDEVICEADDED] = (
    sdl_joy_device_added_event_callback
)


def sdl_joy_device_removed_event_callback(
    sdl_event: Any,
    mouse: Mouse,
    keyboard: Keyboard,
    controllers: dict[Any, Controller]
) -> Optional[ControllerDisconnected]:
    sdl_joystick_index: int = sdl_event.jdevice.which

    sdl_joystick = SDL_JoystickFromInstanceID(sdl_joystick_index)
    if not sdl_joystick:
        raise RuntimeError(SDL_GetError().decode('utf8'))
    SDL_JoystickClose(sdl_joystick)

    controller = controllers.pop(sdl_joystick_index)

    event = controller.disconnect()
    assert isinstance(event, ControllerDisconnected)
    return event

assert SDL_JOYDEVICEREMOVED not in sdl_event_callback_map
sdl_event_callback_map[SDL_JOYDEVICEREMOVED] = (
    sdl_joy_device_removed_event_callback
)
