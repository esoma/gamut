
from __future__ import annotations

__all__ = ['Listener']

# gamut
from ._alcontext import release_al_context, require_al_context
# python
from ctypes import c_float
from typing import Optional
from weakref import ref
# pyglm
from glm import value_ptr as glm_value_ptr
from glm import vec3
# pyopenal
from openal.al import (AL_GAIN, AL_ORIENTATION, AL_POSITION, AL_VELOCITY,
                       alListenerf, alListenerfv)

active_listener: Optional[ref[Listener]] = None


class Listener:

    def __init__(
        self,
        *,
        position: vec3 = vec3(0),
        velocity: vec3 = vec3(0),
        gain: float = 1.0,
        direction: vec3 = vec3(0, 0, -1),
        up: vec3 = vec3(0, 1, 0),
    ):
        self._al_context = require_al_context()

        gain = float(gain)
        if gain < 0.0 or gain > 1.0:
            raise ValueError('gain must be between 0.0 and 1.0')

        self._position = vec3(position)
        self._velocity = vec3(velocity)
        self._direction = vec3(direction)
        self._up = vec3(up)
        self._gain = gain

    def __del__(self) -> None:
        self.deactivate()
        self._al_context = release_al_context(self._al_context)

    def _update_position(self) -> None:
        assert active_listener is not None and active_listener() is self
        alListenerfv(AL_POSITION, glm_value_ptr(self._position))

    def _update_velocity(self) -> None:
        assert active_listener is not None and active_listener() is self
        alListenerfv(AL_VELOCITY, glm_value_ptr(self._velocity))

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
        zero_vec3 = vec3(0)
        alListenerfv(AL_POSITION, glm_value_ptr(zero_vec3))
        alListenerfv(AL_VELOCITY, glm_value_ptr(zero_vec3))
        alListenerfv(AL_ORIENTATION, (c_float * 6)(0, 0, -1, 0, 1, 0))
        alListenerf(AL_GAIN, 1.0)

    @classmethod
    def get_active(cls) -> Optional[Listener]:
        if active_listener is None:
            return None
        return active_listener()

    @property
    def position(self) -> vec3:
        return vec3(self._position)

    @position.setter
    def position(self, value: vec3) -> None:
        self._position = vec3(value)
        if self.get_active() is self:
            self._update_position()

    @property
    def velocity(self) -> vec3:
        return vec3(self._velocity)

    @velocity.setter
    def velocity(self, value: vec3) -> None:
        self._velocity = vec3(value)
        if self.get_active() is self:
            self._update_velocity()

    @property
    def direction(self) -> vec3:
        return vec3(self._direction)

    @direction.setter
    def direction(self, value: vec3) -> None:
        self._direction = vec3(value)
        if self.get_active() is self:
            self._update_orientation()

    @property
    def up(self) -> vec3:
        return vec3(self._up)

    @up.setter
    def up(self, value: vec3) -> None:
        self._up = vec3(value)
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
