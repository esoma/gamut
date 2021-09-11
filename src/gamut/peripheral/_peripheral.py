
from __future__ import annotations

__all__ = [
    'BoundPeripheralEvent',
    'BoundPeripheralConnected',
    'BoundPeripheralDisconnected',
    'Peripheral',
    'PeripheralEvent',
    'PeripheralConnected',
    'PeripheralDisconnected',
]

# gamut
from gamut.event import Bind
from gamut.event import Event as BaseEvent


class PeripheralEvent(BaseEvent):
    peripheral: Peripheral


class PeripheralConnected(PeripheralEvent):
    pass


class PeripheralDisconnected(PeripheralEvent):
    pass


class BoundPeripheralEvent(PeripheralEvent, peripheral=...):
    pass


class BoundPeripheralConnected(BoundPeripheralEvent, PeripheralConnected,
    peripheral=...
):
    pass


class BoundPeripheralDisconnected(BoundPeripheralEvent, PeripheralDisconnected,
    peripheral=...
):
    pass


class Peripheral:

    Event: type[BoundPeripheralEvent]
    Connected: type[BoundPeripheralConnected]
    Disconnected: type[BoundPeripheralDisconnected]

    def __init__(self, is_connected: bool, name: str):
        self._is_connected = is_connected
        self._name = name
        class Event(BoundPeripheralEvent, peripheral=self):
            pass
        self.Event = Event
        class Connected(Event, BoundPeripheralConnected):
            pass
        self.Connected = Connected
        class Disconnected(Event, BoundPeripheralDisconnected):
            pass
        self.Disconnected = Disconnected

    @property
    def is_connected(self) -> bool:
        return self._is_connected

    @property
    def name(self) -> str:
        return self._name


async def connect_peripheral(event: PeripheralConnected) -> None:
    event.peripheral._is_connected = True

connect_peripheral_bind = Bind.on(PeripheralConnected, connect_peripheral)


async def disconnect_peripheral(event: PeripheralDisconnected) -> None:
    event.peripheral._is_connected = False

disconnect_peripheral_bind = Bind.on(
    PeripheralDisconnected,
    disconnect_peripheral
)
