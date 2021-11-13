
# gamut
from gamut.event import Event, EventLoop
from gamut.peripheral import (Peripheral, PeripheralConnected,
                              PeripheralDisconnected)
# python
from typing import Optional
# pytest
import pytest


class TestPeripheral:

    @pytest.fixture
    def cls(self) -> type[Peripheral]:
        return Peripheral

    @pytest.fixture
    def connected_event(self) -> type[PeripheralConnected]:
        return PeripheralConnected

    @pytest.fixture
    def disconnected_event(self) -> type[PeripheralDisconnected]:
        return PeripheralDisconnected

    @pytest.mark.parametrize("name", ['', 'test'])
    def test_defaults(self, cls: type[Peripheral], name: str) -> None:
        peripheral = self.instantiate(cls, name)
        assert peripheral.is_connected is False
        assert peripheral.name == name

    def instantiate(self, cls: type[Peripheral], name: str) -> Peripheral:
        return cls(name)

    def test_connect(
        self,
        cls: type[Peripheral],
        connected_event: type[PeripheralConnected]
    ) -> None:
        event: Optional[PeripheralConnected] = None
        peripheral = self.instantiate(cls, 'test')

        class App(EventLoop):
            def __init__(self) -> None:
                super().__init__()
                self.peripheral_connect_sent = False

            async def main(self) -> None:
                nonlocal event
                assert not peripheral.is_connected
                event = await connected_event
                assert peripheral.is_connected

            async def poll(self, block: bool = True) -> Optional[Event]:
                if self.peripheral_connect_sent:
                    return None
                self.peripheral_connect_sent = True
                return peripheral.connect()

        App().run()
        assert event is not None
        assert isinstance(event, peripheral.Connected)
        assert event.peripheral is peripheral
        assert peripheral.is_connected

    def test_disconnect(
        self,
        cls: type[Peripheral],
        disconnected_event: type[PeripheralDisconnected]
    ) -> None:
        event: Optional[PeripheralDisconnected] = None
        peripheral = self.instantiate(cls, 'test')

        class App(EventLoop):
            def __init__(self) -> None:
                super().__init__()
                self.peripheral_disconnect_sent = False

            async def main(self) -> None:
                nonlocal event
                assert not peripheral.is_connected
                event = await disconnected_event
                assert not peripheral.is_connected

            async def poll(self, block: bool = True) -> Optional[Event]:
                if self.peripheral_disconnect_sent:
                    return None
                self.peripheral_disconnect_sent = True
                peripheral.connect()
                return peripheral.disconnect()

        App().run()
        assert event is not None
        assert isinstance(event, peripheral.Disconnected)
        assert event.peripheral is peripheral
        assert not peripheral.is_connected

    def test_connect_already_connected(self, cls: type[Peripheral]) -> None:
        peripheral = self.instantiate(cls, 'test')
        peripheral.connect()
        with pytest.raises(RuntimeError) as excinfo:
            peripheral.connect()
        assert str(excinfo.value) == 'peripheral is already connected'

    def test_connect_already_disconnected(self, cls: type[Peripheral]) -> None:
        peripheral = self.instantiate(cls, 'test')
        with pytest.raises(RuntimeError) as excinfo:
            peripheral.disconnect()
        assert str(excinfo.value) == 'peripheral is already disconnected'
