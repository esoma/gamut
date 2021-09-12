
# gamut
from .test_peripheral import TestPeripheral
# gamut
from gamut.peripheral import Mouse, MouseConnected, MouseDisconnected
# pytest
import pytest


class TestMouse(TestPeripheral):

    @pytest.fixture
    def cls(self) -> type[Mouse]:
        return Mouse

    @pytest.fixture
    def connected_event(self) -> type[MouseConnected]:
        return MouseConnected

    @pytest.fixture
    def disconnected_event(self) -> type[MouseDisconnected]:
        return MouseDisconnected
