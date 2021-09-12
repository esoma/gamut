
from __future__ import annotations

__all__ = [
    'Mouse',
    'MouseConnected',
    'MouseDisconnected',
    'MouseEvent',
    'Peripheral',
    'PeripheralConnected',
    'PeripheralDisconnected',
    'PeripheralEvent',
]

# gamut
from ._mouse import Mouse, MouseConnected, MouseDisconnected, MouseEvent
from ._peripheral import (Peripheral, PeripheralConnected,
                          PeripheralDisconnected, PeripheralEvent)
