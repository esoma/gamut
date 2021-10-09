
from __future__ import annotations

__all__ = ['VirtualController']

# python
from typing import Any, Final
# evdev
from evdev import UInput  # type: ignore
from evdev.ecodes import (ABS_RX, ABS_RY, ABS_RZ, ABS_X, ABS_Y,  # type: ignore
                          ABS_Z, BTN_A, BTN_B, BTN_X, BTN_Y, EV_ABS, EV_KEY)

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

    def __enter__(self) -> VirtualController:
        return self

    def __exit__(self, *args: Any) -> None:
        self.close()

    def __del__(self) -> None:
        self.close()

    def close(self) -> None:
        self._uinput.close()
