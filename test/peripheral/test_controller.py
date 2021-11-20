
# gamut
from ..application import TestApplication as Application
from .test_peripheral import TestPeripheral
from .virtual import (skip_if_any_real_controllers,
                      skip_if_virtual_controller_nyi, VirtualController)
# gamut
from gamut.peripheral import (Controller, ControllerAxis, ControllerAxisMoved,
                              ControllerButton, ControllerButtonPressed,
                              ControllerButtonReleased, ControllerConnected,
                              ControllerDisconnected, Peripheral)
# python
import ctypes
from typing import Optional
# pysdl2
from sdl2 import (SDL_Event, SDL_JOYAXISMOTION, SDL_JOYBUTTONDOWN,
                  SDL_JOYBUTTONUP, SDL_JoystickClose, SDL_JoystickInstanceID,
                  SDL_JoystickOpen, SDL_PushEvent)
# pytest
import pytest


def send_sdl_joystick_button_event(
    sdl_device_index: int,
    button_index: int,
    pressed: bool
) -> None:
    sdl_joystick = SDL_JoystickOpen(sdl_device_index)
    sdl_joystick_id = SDL_JoystickInstanceID(sdl_joystick)
    SDL_JoystickClose(sdl_joystick)
    sdl_event = SDL_Event()
    sdl_event.type = SDL_JOYBUTTONDOWN if pressed else SDL_JOYBUTTONUP
    sdl_event.jbutton.which = sdl_joystick_id
    sdl_event.jbutton.button = button_index
    SDL_PushEvent(ctypes.byref(sdl_event))


def send_sdl_joystick_axis_moved_event(
    sdl_device_index: int,
    axis_index: int,
    position: float
) -> None:
    sdl_joystick = SDL_JoystickOpen(sdl_device_index)
    sdl_joystick_id = SDL_JoystickInstanceID(sdl_joystick)
    SDL_JoystickClose(sdl_joystick)
    sdl_event = SDL_Event()
    sdl_event.type = SDL_JOYAXISMOTION
    sdl_event.jaxis.which = sdl_joystick_id
    sdl_event.jaxis.axis = axis_index
    sdl_event.jaxis.value = int(position * 32767)
    SDL_PushEvent(ctypes.byref(sdl_event))


class TestController(TestPeripheral):

    @pytest.fixture
    def cls(self) -> type[Controller]:
        return Controller

    @pytest.fixture
    def connected_event(self) -> type[ControllerConnected]:
        return ControllerConnected

    @pytest.fixture
    def disconnected_event(self) -> type[ControllerDisconnected]:
        return ControllerDisconnected

    def instantiate(self, cls: type[Peripheral], name: str) -> Controller:
        assert issubclass(cls, Controller)
        return cls(name, 0, 0)


@pytest.mark.parametrize('button_count', [0, 1, 2, 6])
@pytest.mark.parametrize('axis_count', [0, 1, 2, 6])
def test_defaults(button_count: int, axis_count: int) -> None:
    controller = Controller('test', button_count, axis_count)

    assert len(controller.buttons) == button_count
    for index, button in enumerate(controller.buttons):
        assert button.index == index
        assert not button.is_pressed

    assert len(controller.axes) == axis_count
    for index, axis in enumerate(controller.axes):
        assert axis.index == index
        assert axis.position == 0.0


@pytest.mark.parametrize("name", ['', 'test', 'Primary'])
def test_repr(name: str) -> None:
    controller = Controller(name, 0, 0)
    assert repr(controller) == f'<gamut.peripheral.Controller {name!r}>'


@pytest.mark.parametrize("button_index", [0, 1, 2])
def test_button_repr(button_index: int) -> None:
    controller = Controller('test', 3, 0)
    button = controller.buttons[button_index]
    assert repr(button) == (
        f'<gamut.peripheral.ControllerButton '
        f'{button_index!r} for {controller!r}>'
    )


@pytest.mark.parametrize("axis_index", [0, 1, 2])
def test_axis_repr(axis_index: int) -> None:
    controller = Controller('test', 0, 3)
    axis = controller.axes[axis_index]
    assert repr(axis) == (
        f'<gamut.peripheral.ControllerAxis {axis_index!r} for {controller!r}>'
    )


@skip_if_any_real_controllers
@skip_if_virtual_controller_nyi
@pytest.mark.parametrize("button_count", [1, 4])
@pytest.mark.parametrize("axis_count", [1, 4])
def test_poll_joy_device_added_event_prior_to_application_start(
    button_count: int,
    axis_count: int
) -> None:
    connected_event: Optional[ControllerConnected] = None

    class TestApplication(Application):
        async def main(self) -> None:
            nonlocal connected_event
            assert not self.controllers
            connected_event = await ControllerConnected
            assert len(self.controllers) == 1

    with VirtualController('test', button_count, axis_count) as vc:
        app = TestApplication()
        app.run()

    assert isinstance(connected_event, ControllerConnected)
    controller = connected_event.controller
    assert isinstance(controller, Controller)
    assert controller.name == 'test'
    assert len(controller.buttons) == button_count
    assert len(controller.axes) == axis_count
    assert not controller.is_connected
    assert not app.controllers


@skip_if_any_real_controllers
@skip_if_virtual_controller_nyi
@pytest.mark.parametrize("button_count", [1, 4])
@pytest.mark.parametrize("axis_count", [1, 4])
def test_poll_joy_device_added_event_after_application_start(
    button_count: int,
    axis_count: int
) -> None:
    connected_event: Optional[ControllerConnected] = None

    class TestApplication(Application):
        async def main(self) -> None:
            with VirtualController('test', button_count, axis_count) as vc:
                nonlocal connected_event
                assert not self.controllers
                connected_event = await ControllerConnected
                assert len(self.controllers) == 1

    app = TestApplication()
    app.run()
    assert isinstance(connected_event, ControllerConnected)
    controller = connected_event.controller
    assert isinstance(controller, Controller)
    assert controller.name == 'test'
    assert len(controller.buttons) == button_count
    assert len(controller.axes) == axis_count
    assert not controller.is_connected
    assert not app.controllers


@skip_if_any_real_controllers
@skip_if_virtual_controller_nyi
@pytest.mark.parametrize("button_count", [1, 4])
@pytest.mark.parametrize("axis_count", [1, 4])
def test_poll_joy_device_removed_event_added_prior_to_application_start(
    button_count: int,
    axis_count: int
) -> None:
    controller: Optional[Controller] = None
    disconnected_event: Optional[ControllerDisconnected] = None

    with VirtualController('test', button_count, axis_count) as vc:
        class TestApplication(Application):
            async def main(self) -> None:
                nonlocal controller
                nonlocal disconnected_event
                assert not self.controllers
                connected_event = await ControllerConnected
                controller = connected_event.controller
                vc.close()
                disconnected_event = await ControllerDisconnected

        app = TestApplication()
        app.run()

    assert isinstance(disconnected_event, ControllerDisconnected)
    assert isinstance(controller, Controller)
    assert controller.name == 'test'
    assert len(controller.buttons) == button_count
    assert len(controller.axes) == axis_count
    assert not controller.is_connected
    assert not app.controllers


@skip_if_any_real_controllers
@skip_if_virtual_controller_nyi
@pytest.mark.parametrize("button_count", [1, 4])
@pytest.mark.parametrize("axis_count", [1, 4])
def test_poll_joy_device_removed_event_added_after_to_application_start(
    button_count: int,
    axis_count: int
) -> None:
    controller: Optional[Controller] = None
    disconnected_event: Optional[ControllerDisconnected] = None

    class TestApplication(Application):
        async def main(self) -> None:
            nonlocal controller
            nonlocal disconnected_event
            assert not self.controllers
            with VirtualController('test', button_count, axis_count) as vc:
                connected_event = await ControllerConnected
                controller = connected_event.controller
            disconnected_event = await ControllerDisconnected

    app = TestApplication()
    app.run()

    assert isinstance(disconnected_event, ControllerDisconnected)
    assert isinstance(controller, Controller)
    assert controller.name == 'test'
    assert len(controller.buttons) == button_count
    assert len(controller.axes) == axis_count
    assert not controller.is_connected
    assert not app.controllers


@skip_if_any_real_controllers
@skip_if_virtual_controller_nyi
@pytest.mark.parametrize("button_index", [0, 1, 2, 3])
def test_poll_joy_button_down_event(button_index: int) -> None:
    pressed_event: Optional[ControllerButtonPressed] = None
    button: Optional[ControllerButton]

    class TestApplication(Application):
        async def main(self) -> None:
            nonlocal pressed_event
            nonlocal button
            controller = (await ControllerConnected).controller
            send_sdl_joystick_button_event(0, button_index, True)
            button = controller.buttons[button_index]
            assert not button.is_pressed
            pressed_event = await button.Pressed
            assert button.is_pressed

    with VirtualController('test', 4, 2) as vc:
        app = TestApplication()
        app.run()

    assert isinstance(pressed_event, ControllerButtonPressed)
    assert isinstance(button, ControllerButton)
    assert button.index == button_index
    assert button.is_pressed


@skip_if_any_real_controllers
@skip_if_virtual_controller_nyi
@pytest.mark.parametrize("button_index", [0, 1, 2, 3])
def test_poll_joy_button_up_event(button_index: int) -> None:
    released_event: Optional[ControllerButtonReleased] = None
    button: Optional[ControllerButton]

    class TestApplication(Application):
        async def main(self) -> None:
            nonlocal released_event
            nonlocal button
            controller = (await ControllerConnected).controller

            send_sdl_joystick_button_event(0, button_index, True)
            button = controller.buttons[button_index]
            assert not button.is_pressed
            await button.Pressed
            assert button.is_pressed

            send_sdl_joystick_button_event(0, button_index, False)
            released_event = await button.Released
            assert not button.is_pressed

    with VirtualController('test', 4, 2) as vc:
        app = TestApplication()
        app.run()

    assert isinstance(released_event, ControllerButtonReleased)
    assert isinstance(button, ControllerButton)
    assert button.index == button_index
    assert not button.is_pressed


@skip_if_any_real_controllers
@skip_if_virtual_controller_nyi
@pytest.mark.parametrize("axis_index", [0, 1, 2, 3])
@pytest.mark.parametrize("axis_position", [-1.0, -.5, 0.0, .5, 1.0])
def test_poll_joy_axis_moved_event(
    axis_index: int,
    axis_position: float
) -> None:
    moved_event: Optional[ControllerAxisMoved] = None
    axis: Optional[ControllerAxis]

    class TestApplication(Application):
        async def main(self) -> None:
            nonlocal moved_event
            nonlocal axis
            controller = (await ControllerConnected).controller

            send_sdl_joystick_axis_moved_event(0, axis_index, axis_position)
            axis = controller.axes[axis_index]
            assert axis.position == 0.0
            moved_event = await axis.Moved
            assert pytest.approx(axis.position, axis_position)

    with VirtualController('test', 4, 4) as vc:
        app = TestApplication()
        app.run()

    assert isinstance(moved_event, ControllerAxisMoved)
    assert isinstance(axis, ControllerAxis)
    assert axis.index == axis_index
    assert pytest.approx(axis.position, axis_position)
