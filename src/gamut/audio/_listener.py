
from __future__ import annotations

__all__ = ['Listener']

# gamut
from ._alcontext import release_al_context, require_al_context
# gamut
from gamut.math import FVector3, Vector3
# python
from ctypes import c_float
from typing import Optional
from weakref import ref
# pyopenal
from openal.al import (AL_GAIN, AL_ORIENTATION, AL_POSITION, AL_VELOCITY,
                       alListenerf, alListenerfv)

active_listener: Optional[ref[Listener]] = None


class Listener:

    def __init__(
        self,
        *,
        position: Vector3 = Vector3(0),
        velocity: Vector3 = Vector3(0),
        gain: float = 1.0,
        direction: Vector3 = Vector3(0, 0, -1),
        up: Vector3 = Vector3(0, 1, 0),
    ):
        self._al_context = require_al_context()

        gain = float(gain)
        if gain < 0.0 or gain > 1.0:
            raise ValueError('gain must be between 0.0 and 1.0')

        self.position = position
        self.velocity = velocity
        self.direction = direction
        self.up = up
        self._gain = gain

    def __del__(self) -> None:
        self.deactivate()
        self._al_context = release_al_context(self._al_context)

    def _update_position(self) -> None:
        assert active_listener is not None and active_listener() is self
        alListenerfv(AL_POSITION, FVector3(*self._position).pointer)

    def _update_velocity(self) -> None:
        assert active_listener is not None and active_listener() is self
        alListenerfv(AL_VELOCITY, FVector3(*self._velocity).pointer)

    def _update_orientation(self) -> None:
        assert active_listener is not None and active_listener() is self
        alListenerfv(AL_ORIENTATION, (c_float * 6)(
            *self._direction,
            *self._up
        ))

    def _update_gain(self) -> None:
        assert active_listener is not None and active_listener() is self
        alListenerf(AL_GAIN, self._gain)

    def activate(self) -> None:
        global active_listener
        if active_listener is not None:
            current_listener = active_listener()
            if current_listener is not None:
                current_listener.deactivate()
        assert active_listener is None
        active_listener = ref(self)
        self._update_position()
        self._update_velocity()
        self._update_orientation()
        self._update_gain()

    def deactivate(self) -> None:
        global active_listener
        if active_listener is None:
            return
        current_listener = active_listener()
        if current_listener is not self:
            return None
        active_listener = None
        zero_vec3 = FVector3(0)
        alListenerfv(AL_POSITION, zero_vec3.pointer)
        alListenerfv(AL_VELOCITY, zero_vec3.pointer)
        alListenerfv(AL_ORIENTATION, (c_float * 6)(0, 0, -1, 0, 1, 0))
        alListenerf(AL_GAIN, 1.0)

    @classmethod
    def get_active(cls) -> Optional[Listener]:
        if active_listener is None:
            return None
        return active_listener()

    @property
    def position(self) -> Vector3:
        return self._position

    @position.setter
    def position(self, value: Vector3) -> None:
        if not isinstance(value, Vector3):
            raise TypeError(f'expected Vector3, got {value!r}')
        self._position = value
        if self.get_active() is self:
            self._update_position()

    @property
    def velocity(self) -> Vector3:
        return self._velocity

    @velocity.setter
    def velocity(self, value: Vector3) -> None:
        if not isinstance(value, Vector3):
            raise TypeError(f'expected Vector3, got {value!r}')
        self._velocity = value
        if self.get_active() is self:
            self._update_velocity()

    @property
    def direction(self) -> Vector3:
        return self._direction

    @direction.setter
    def direction(self, value: Vector3) -> None:
        if not isinstance(value, Vector3):
            raise TypeError(f'expected Vector3, got {value!r}')
        self._direction = value
        if self.get_active() is self:
            self._update_orientation()

    @property
    def up(self) -> Vector3:
        return self._up

    @up.setter
    def up(self, value: Vector3) -> None:
        if not isinstance(value, Vector3):
            raise TypeError(f'expected Vector3, got {value!r}')
        self._up = value
        if self.get_active() is self:
            self._update_orientation()

    @property
    def gain(self) -> float:
        return self._gain

    @gain.setter
    def gain(self, value: float) -> None:
        if value < 0.0 or value > 1.0:
            raise ValueError('gain must be between 0.0 and 1.0')
        self._gain = value
        if self.get_active() is self:
            self._update_gain()
