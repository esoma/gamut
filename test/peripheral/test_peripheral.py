
# gamut
from gamut.event import Application, Event
from gamut.peripheral import (Peripheral, PeripheralConnected,
                              PeripheralDisconnected)
# python
from typing import Optional
# pytest
import pytest


@pytest.mark.parametrize("name", ['', 'test'])
def test_defaults(name: str) -> None:
    peripheral = Peripheral(name)
    assert peripheral.is_connected is False
    assert peripheral.name == name


def test_connect() -> None:
    event: Optional[PeripheralConnected] = None
    peripheral = Peripheral('test')

    class App(Application):
        def __init__(self) -> None:
            super().__init__()
            self.peripheral_connect_sent = False

        async def main(self) -> None:
            nonlocal event
            assert not peripheral.is_connected
            event = await PeripheralConnected
            assert peripheral.is_connected

        async def poll(self) -> Optional[Event]:
            if self.peripheral_connect_sent:
                return None
            self.peripheral_connect_sent = True
            return peripheral.connect()

    App().run()
    assert event is not None
    assert isinstance(event, peripheral.Connected)
    assert event.peripheral is peripheral
    assert peripheral.is_connected


def test_disconnect() -> None:
    event: Optional[PeripheralDisconnected] = None
    peripheral = Peripheral('test')

    class App(Application):
        def __init__(self) -> None:
            super().__init__()
            self.peripheral_disconnect_sent = False

        async def main(self) -> None:
            nonlocal event
            assert not peripheral.is_connected
            event = await PeripheralDisconnected
            assert not peripheral.is_connected

        async def poll(self) -> Optional[Event]:
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


def test_connect_already_connected() -> None:
    peripheral = Peripheral('test')
    peripheral.connect()
    with pytest.raises(RuntimeError) as excinfo:
        peripheral.connect()
    assert str(excinfo.value) == 'peripheral is already connected'


def test_connect_already_disconnected() -> None:
    peripheral = Peripheral('test')
    with pytest.raises(RuntimeError) as excinfo:
        peripheral.disconnect()
    assert str(excinfo.value) == 'peripheral is already disconnected'
