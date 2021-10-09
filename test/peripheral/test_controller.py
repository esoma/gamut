
# gamut
from .test_peripheral import TestPeripheral
from .virtual import (skip_if_any_real_controllers,
                      skip_if_virtual_controller_nyi, VirtualController)
# gamut
from gamut import Application
from gamut.peripheral import (Controller, ControllerConnected,
                              ControllerDisconnected, Peripheral)
# python
from typing import Optional
# pytest
import pytest


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

    with VirtualController('test', button_count, axis_count) as vc:
        class TestApplication(Application):
            async def main(self) -> None:
                nonlocal connected_event
                assert not self.controllers
                connected_event = await ControllerConnected
                assert len(self.controllers) == 1

            async def poll(self, block=False):
                # python
                import time
                start = time.monotonic()
                while True:
                    event = await super().poll(block=False)
                    if event:
                        return event
                    assert time.monotonic() - start < 2

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
