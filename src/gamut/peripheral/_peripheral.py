
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

    def __init__(self, name: str):
        self._is_connected = False
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

    def connect(self) -> BoundPeripheralConnected:
        if self._is_connected:
            raise RuntimeError('peripheral is already connected')
        self._is_connected = True
        return self.Connected()

    def disconnect(self) -> BoundPeripheralDisconnected:
        if not self._is_connected:
            raise RuntimeError('peripheral is already disconnected')
        self._is_connected = False
        return self.Disconnected()

    @property
    def name(self) -> str:
        return self._name
