
# gamut
from .test_peripheral import TestPeripheral
# gamut
from gamut.peripheral import (Controller, ControllerConnected,
                              ControllerDisconnected, Peripheral)
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
