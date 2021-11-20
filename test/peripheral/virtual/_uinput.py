
from __future__ import annotations

__all__ = ['VirtualController']

# python
import os
from typing import Any, Final
# evdev
from evdev import UInput  # type: ignore
from evdev.ecodes import (ABS_RX, ABS_RY, ABS_RZ, ABS_X, ABS_Y,  # type: ignore
                          ABS_Z, BTN_A, BTN_B, BTN_X, BTN_Y, EV_ABS, EV_KEY)
from evdev.eventio_async import EventIO  # type: ignore

BUTTONS: Final = (BTN_A, BTN_B, BTN_X, BTN_Y)
AXES: Final = (ABS_X, ABS_Y, ABS_Z, ABS_RX, ABS_RY, ABS_RZ)


class VirtualController:

    def __init__(self, name: str, button_count: int, axis_count: int):
        if button_count <= 0:
            raise ValueError(f'must have at least 1 button')
        if button_count > len(BUTTONS):
            raise ValueError(f'max buttons is {len(BUTTONS)}')
        if axis_count <= 0:
            raise ValueError(f'must have at least 1 axis')
        if axis_count > len(AXES):
            raise ValueError(f'max axes is {len(AXES)}')

        self._uinput = UInput({
            EV_KEY: BUTTONS[:button_count],
            EV_ABS: AXES[:axis_count],
        }, name=name)
        device = self._uinput.device
        def device_close() -> None:
            if device.fd > -1:
                try:
                    EventIO.close(device)
                    os.close(device.fd)
                finally:
                    device.fd = -1
        device.close = device_close

    def __enter__(self) -> VirtualController:
        return self

    def __exit__(self, *args: Any) -> None:
        self.close()

    def close(self) -> None:
        if self._uinput is not None:
            self._uinput.close()
            self._uinput = None
