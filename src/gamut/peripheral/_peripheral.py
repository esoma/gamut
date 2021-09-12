
from __future__ import annotations

__all__ = [
    'Peripheral',
    'PeripheralEvent',
    'PeripheralConnected',
    'PeripheralDisconnected',
]

# gamut
from gamut.event import Event as BaseEvent


class PeripheralEvent(BaseEvent, peripheral=...):
    peripheral: Peripheral


class PeripheralConnected(PeripheralEvent, peripheral=...):
    pass


class PeripheralDisconnected(PeripheralEvent, peripheral=...):
    pass


class Peripheral:

    Event: type[PeripheralEvent]
    Connected: type[PeripheralConnected]
    Disconnected: type[PeripheralDisconnected]

    def __init__(self, name: str):
        self._is_connected = False
        self._name = name
        class Event(PeripheralEvent, peripheral=self):
            pass
        self.Event = Event
        class Connected(Event, PeripheralConnected):
            pass
        self.Connected = Connected
        class Disconnected(Event, PeripheralDisconnected):
            pass
        self.Disconnected = Disconnected

    @property
    def is_connected(self) -> bool:
        return self._is_connected

    def connect(self) -> PeripheralConnected:
        if self._is_connected:
            raise RuntimeError('peripheral is already connected')
        self._is_connected = True
        return self.Connected()

    def disconnect(self) -> PeripheralDisconnected:
        if not self._is_connected:
            raise RuntimeError('peripheral is already disconnected')
        self._is_connected = False
        return self.Disconnected()

    @property
    def name(self) -> str:
        return self._name
