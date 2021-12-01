
from __future__ import annotations

__all__ = ['MultiSpeaker']


# gamut
from ._source import Sample
from ._speaker import Speaker, SpeakerState
from gamut._glmhelp import vec3_exact
from math import pi
from glm_typing import F32Vector3
from glm import vec3


class MultiSpeaker:
    
    def __init__(
        self,
        *,
        position: vec3 = vec3(0),
        velocity: vec3 = vec3(0),
        min_gain: float = 0.0,
        gain: float = 1.0,
        max_gain: float = 1.0,
        is_relative: bool = False,
        pitch: float = 1.0,
        direction: vec3 = vec3(0),
        inner_cone_angle: float = 2 * pi,
        outer_cone_angle: float = 2 * pi,
        outer_cone_gain: float = 0.0,
    ):
        self._speakers: list[Speaker] = []
        self.position = position
        self.velocity = velocity
        self.min_gain = min_gain
        self.gain = gain
        self.max_gain = max_gain
        self.is_relative = is_relative
        self.pitch = pitch
        self.direction = direction
        self.inner_cone_angle = inner_cone_angle
        self.outer_cone_angle = outer_cone_angle
        self.outer_cone_gain = outer_cone_gain
        
    def play(self, sample: Sample) -> None:
        for speaker in self._speakers:
            if speaker.state is SpeakerState.STOPPED:
                break
            speaker.source = sample
        else:
            speaker = Speaker(
                sample,
                position=self._position,
                velocity=self._velocity,
                min_gain=self._min_gain,
                gain=self._gain,
                max_gain=self._max_gain,
                is_relative=self._is_relative,
                pitch=self._pitch,
                direction=self._direction,
                inner_cone_angle=self._inner_cone_angle,
                outer_cone_angle=self._outer_cone_angle,
                outer_cone_gain=self._outer_cone_gain,
            )
            self._speakers.append(speaker)
        speaker.play()
        
    def resume(self) -> None:
        for speaker in self._speakers:
            speaker.resume()
        
    def pause(self) -> None:
        for speaker in self._speakers:
            speaker.pause()
        
    def stop(self) -> None:
        for speaker in self._speakers:
            speaker.stop()
        
    @property
    def position(self) -> vec3:
        return vec3(self._position)
        
    @position.setter
    def position(self, value: F32Vector3) -> None:
        self._position = vec3_exact(value)
        for speaker in self._speakers:
            speaker.position = self._position

    @property
    def velocity(self) -> vec3:
        return vec3(self._velocity)
        
    @velocity.setter
    def velocity(self, value: F32Vector3) -> None:
        self._velocity = vec3_exact(value)
        for speaker in self._speakers:
            speaker.velocity = self._velocity
        
    @property
    def min_gain(self) -> float:
        return self._min_gain
        
    @min_gain.setter
    def min_gain(self, value: float) -> None:
        self._min_gain = float(value)
        for speaker in self._speakers:
            speaker.min_gain = self._min_gain
        
    @property
    def gain(self) -> float:
        return self._gain
        
    @gain.setter
    def gain(self, value: float) -> None:
        self._gain = float(value)
        for speaker in self._speakers:
            speaker.gain = self._gain
        
    @property
    def max_gain(self) -> float:
        return self._min_gain
        
    @max_gain.setter
    def max_gain(self, value: float) -> None:
        self._max_gain = float(value)
        for speaker in self._speakers:
            speaker.max_gain = self._max_gain

    @property
    def is_relative(self) -> bool:
        return self._is_relative
        
    @is_relative.setter
    def is_relative(self, value: bool) -> None:
        self._is_relative = bool(value)
        for speaker in self._speakers:
            speaker.is_relative = self._is_relative
        
    @property
    def pitch(self) -> float:
        return self._pitch
        
    @pitch.setter
    def pitch(self, value: float) -> None:
        self._pitch = float(value)
        for speaker in self._speakers:
            speaker.pitch = self._pitch
        
    @property
    def direction(self) -> vec3:
        return vec3(self._direction)
        
    @direction.setter
    def direction(self, value: F32Vector3) -> None:
        self._direction = vec3_exact(value)
        for speaker in self._speakers:
            speaker.direction = self._direction
        
    @property
    def inner_cone_angle(self) -> float:
        return self._inner_cone_angle
        
    @inner_cone_angle.setter
    def inner_cone_angle(self, value: float) -> None:
        self._inner_cone_angle = float(value)
        for speaker in self._speakers:
            speaker.inner_cone_angle = self._inner_cone_angle
        
    @property
    def outer_cone_angle(self) -> float:
        return self._outer_cone_angle
        
    @outer_cone_angle.setter
    def outer_cone_angle(self, value: float) -> None:
        self._outer_cone_angle = float(value)
        for speaker in self._speakers:
            speaker.outer_cone_angle = self._outer_cone_angle
        
    @property
    def outer_cone_gain(self) -> float:
        return self._outer_cone_gain
        
    @outer_cone_gain.setter
    def outer_cone_gain(self, value: float) -> None:
        self._outer_cone_gain = float(value)
        for speaker in self._speakers:
            speaker.outer_cone_gain = self._outer_cone_gain