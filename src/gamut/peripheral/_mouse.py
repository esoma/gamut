
from __future__ import annotations

__all__ = [
    'Mouse',
    'MouseConnected',
    'MouseDisconnected',
    'MouseEvent',
]

# gamut
from ._peripheral import (Peripheral, PeripheralConnected,
                          PeripheralDisconnected, PeripheralEvent)


class MouseEvent(PeripheralEvent, peripheral=...):
    peripheral: Mouse

    @property
    def mouse(self) -> Mouse:
        return self.peripheral


class MouseConnected(MouseEvent, PeripheralConnected, peripheral=...):
    pass


class MouseDisconnected(MouseEvent, PeripheralDisconnected, peripheral=...):
    pass


class Mouse(Peripheral):

    Event: type[MouseEvent]
    Connected: type[MouseConnected]
    Disconnected: type[MouseDisconnected]

    def __init__(self, name: str):
        super().__init__(name)
        class Event(MouseEvent, self.Event): # type: ignore
            pass
        self.Event = Event
        class Connected( # type: ignore
            MouseConnected,
            Event,
            self.Connected, # type: ignore
        ):
            pass
        self.Connected = Connected
        class Disconnected( # type: ignore
            MouseDisconnected,
            Event,
            self.Disconnected, # type: ignore
        ):
            pass
        self.Disconnected = Disconnected
