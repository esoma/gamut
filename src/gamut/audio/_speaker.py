
from __future__ import annotations

__all__ = ['Speaker', 'SpeakerState']


# gamut
from ._alcontext import release_al_context, require_al_context
from ._source import (consume_stream_buffer, get_sample_al_buffer,
                      release_sample_al_buffer, return_stream_buffer, Sample,
                      Stream)
# gamut
from gamut.math import DVector3, FVector3
# python
from ctypes import c_int, c_uint
from ctypes import pointer as c_pointer
from enum import Enum
from math import degrees, pi
from queue import Empty as QueueEmpty
from threading import Lock, Thread
from threading import get_ident as get_thread_ident
import time
from typing import Any, Final, Optional, Union
from warnings import warn
from weakref import ref
# pyopenal
from openal.al import (AL_BUFFER, AL_BUFFERS_PROCESSED, AL_BUFFERS_QUEUED,
                       AL_CONE_INNER_ANGLE, AL_CONE_OUTER_ANGLE,
                       AL_CONE_OUTER_GAIN, AL_DIRECTION, AL_FALSE, AL_GAIN,
                       AL_INITIAL, AL_LOOPING, AL_MAX_GAIN, AL_MIN_GAIN,
                       AL_PAUSED, AL_PITCH, AL_PLAYING, AL_POSITION,
                       AL_SOURCE_RELATIVE, AL_SOURCE_STATE, AL_STOPPED,
                       AL_TRUE, AL_VELOCITY, alDeleteSources, alGenSources,
                       alGetSourcei, alSourcef, alSourcefv, alSourcei,
                       alSourcePause, alSourcePlay, alSourceQueueBuffers,
                       alSourceStop, alSourceUnqueueBuffers)


class SpeakerState(Enum):
    STOPPED = 0
    PLAYING = 1
    PAUSED = 2


AL_STATE_TO_SPEAKER_STATE: Final = {
    AL_INITIAL: SpeakerState.STOPPED,
    AL_STOPPED: SpeakerState.STOPPED,
    AL_PLAYING: SpeakerState.PLAYING,
    AL_PAUSED: SpeakerState.PAUSED,
}


class Speaker:

    def __init__(
        self,
        source: Union[Sample, Stream],
        *,
        position: DVector3 = DVector3(0),
        velocity: DVector3 = DVector3(0),
        min_gain: float = 0.0,
        gain: float = 1.0,
        max_gain: float = 1.0,
        is_relative: bool = False,
        loop: bool = False,
        pitch: float = 1.0,
        direction: DVector3 = DVector3(0),
        inner_cone_angle: float = 2 * pi,
        outer_cone_angle: float = 2 * pi,
        outer_cone_gain: float = 0.0,
    ):
        self._al_context = require_al_context()

        if not isinstance(source, (Sample, Stream)):
            raise TypeError('source must be either a Sample or Stream')

        al_id = c_uint()
        alGenSources(1, c_pointer(al_id))
        self._al: Optional[c_uint] = al_id

        self._is_open = True
        self._play = False
        self._loop = loop
        self._stream_thread: Optional[Thread] = None
        self._stream_lock: Optional[Lock] = None
        self._source: Optional[Union[Sample, Stream]] = source
        if isinstance(source, Sample):
            try:
                al_buffer = get_sample_al_buffer(source)
            except Exception:
                self._source = None
                raise
            alSourcei(self._al, AL_BUFFER, al_buffer)
        else:
            self._stream_lock = Lock()
            self._stream_thread = Thread(
                target=_stream_main,
                args=(ref(self),),
                daemon=True,
            )
            self._stream_thread.start()

        try:
            self.position = position
            self.velocity = velocity
            self.min_gain = min_gain
            self.gain = gain
            self.max_gain = max_gain
            self.is_relative = is_relative
            self.loop = loop
            self.pitch = pitch
            self.direction = direction
            self.inner_cone_angle = inner_cone_angle
            self.outer_cone_angle = outer_cone_angle
            self.outer_cone_gain = outer_cone_gain
        except BaseException:
            self.close()
            raise

    def __del__(self) -> None:
        self.close()

    def __enter__(self) -> Speaker:
        return self

    def __exit__(self, *_: Any) -> None:
        self.close()

    def _stream(self) -> bool:
        assert isinstance(self._source, Stream)
        assert self._stream_lock is not None
        with self._stream_lock:
            buffers_processed = c_int()
            alGetSourcei(self._al, AL_BUFFERS_PROCESSED, buffers_processed)
            for _ in range(buffers_processed.value):
                c_al_buffer = c_uint()
                alSourceUnqueueBuffers(self._al, 1, c_al_buffer)
                return_stream_buffer(self._source, c_al_buffer.value)

            while True:
                try:
                    al_buffer = consume_stream_buffer(self._source)
                except QueueEmpty:
                    break
                if al_buffer is None:
                    if self._loop:
                        self._source.reset()
                        continue
                    else:
                        self._play = False
                    break
                alSourceQueueBuffers(self._al, 1, c_uint(al_buffer))
        return True

    def _ensure_open(self) -> None:
        if self._al is None:
            raise RuntimeError('speaker is closed')

    def close(self) -> None:
        self._is_open = False
        if hasattr(self, "_stream_thread") and self._stream_thread:
            if self._stream_thread.ident != get_thread_ident():
                self._stream_thread.join()
            self._stream_thread = None
        if hasattr(self, "_al") and self._al is not None:
            alDeleteSources(1, c_pointer(self._al))
            self._al = None
        if hasattr(self, "_source") and self._source is not None:
            if isinstance(self._source, Sample):
                release_sample_al_buffer(self._source)
            self._source = None
        self._al_context = release_al_context(self._al_context)

    def play(self) -> None:
        self._ensure_open()
        if isinstance(self._source, Stream):
            self._stream()
        self._play = True
        alSourcePlay(self._al)

    def resume(self) -> None:
        if self.state is SpeakerState.PAUSED:
            self.play()

    def pause(self) -> None:
        self._ensure_open()
        self._play = False
        alSourcePause(self._al)

    def stop(self) -> None:
        self._ensure_open()
        self._play = False
        if isinstance(self._source, Stream):
            self._source.reset()
        alSourceStop(self._al)

    @property
    def source(self) -> Union[Sample, Stream]:
        self._ensure_open()
        assert self._source is not None
        return self._source

    @source.setter
    def source(self, value: Union[Sample, Stream]) -> None:
        self._ensure_open()
        if not isinstance(self._source, Sample):
            raise TypeError('may only change the source if it is a sample')
        if not isinstance(value, Sample):
            raise TypeError('may only change the source to a sample')
        self.stop()
        al_buffer = get_sample_al_buffer(value)
        release_sample_al_buffer(self._source)
        alSourcei(self._al, AL_BUFFER, al_buffer)
        self._source = value

    @property
    def state(self) -> SpeakerState:
        self._ensure_open()
        al_state = c_int()
        alGetSourcei(self._al, AL_SOURCE_STATE, al_state)
        return AL_STATE_TO_SPEAKER_STATE[al_state.value]

    @property
    def position(self) -> DVector3:
        self._ensure_open()
        return self._position

    @position.setter
    def position(self, value: DVector3) -> None:
        self._ensure_open()
        if not isinstance(value, DVector3):
            raise TypeError(f'expected DVector3, got {value!r}')
        self._position = value
        assert self._source is not None
        if self._source.channels != 1 and self._position != DVector3(0):
            warn(
                f'{self._source} has more than 1 channel, it will be '
                f'unaffected by changes in position'
            )
        f_position = FVector3(*self._position)
        alSourcefv(self._al, AL_POSITION, f_position.pointer)

    @property
    def velocity(self) -> DVector3:
        self._ensure_open()
        return self._velocity

    @velocity.setter
    def velocity(self, value: DVector3) -> None:
        self._ensure_open()
        if not isinstance(value, DVector3):
            raise TypeError(f'expected DVector3, got {value!r}')
        self._velocity = value
        assert self._source is not None
        if self._source.channels != 1 and self._velocity != DVector3(0):
            warn(
                f'{self._source} has more than 1 channel, it will be '
                f'unaffected by changes in velocity'
            )
        f_velocity = FVector3(*self._velocity)
        alSourcefv(self._al, AL_VELOCITY, f_velocity.pointer)

    @property
    def min_gain(self) -> float:
        self._ensure_open()
        return self._min_gain

    @min_gain.setter
    def min_gain(self, value: float) -> None:
        self._ensure_open()
        value = float(value)
        if value < 0.0 or value > 1.0:
            raise ValueError('min gain must be between 0.0 and 1.0')
        self._min_gain = value
        alSourcef(self._al, AL_MIN_GAIN, self._min_gain)

    @property
    def gain(self) -> float:
        self._ensure_open()
        return self._gain

    @gain.setter
    def gain(self, value: float) -> None:
        self._ensure_open()
        value = float(value)
        if value < 0.0 or value > 1.0:
            raise ValueError('gain must be between 0.0 and 1.0')
        self._gain = value
        alSourcef(self._al, AL_GAIN, self._gain)

    @property
    def max_gain(self) -> float:
        self._ensure_open()
        return self._max_gain

    @max_gain.setter
    def max_gain(self, value: float) -> None:
        self._ensure_open()
        value = float(value)
        if value < 0.0 or value > 1.0:
            raise ValueError('max gain must be between 0.0 and 1.0')
        self._max_gain = value
        alSourcef(self._al, AL_MAX_GAIN, self._max_gain)

    @property
    def is_relative(self) -> bool:
        self._ensure_open()
        return self._is_relative

    @is_relative.setter
    def is_relative(self, value: bool) -> None:
        self._ensure_open()
        self._is_relative = bool(value)
        alSourcei(
            self._al,
            AL_SOURCE_RELATIVE,
            AL_TRUE if self._is_relative else AL_FALSE
        )

    @property
    def loop(self) -> bool:
        self._ensure_open()
        return self._loop

    @loop.setter
    def loop(self, value: bool) -> None:
        self._ensure_open()
        self._loop = bool(value)
        assert self._source is not None
        if isinstance(self._source, Sample):
            alSourcei(self._al, AL_LOOPING, AL_TRUE if value else AL_FALSE)

    @property
    def pitch(self) -> float:
        self._ensure_open()
        return self._pitch

    @pitch.setter
    def pitch(self, value: float) -> None:
        self._ensure_open()
        value = float(value)
        if value < 0.0:
            raise ValueError('pitch must be 0.0 or greater')
        self._pitch = value
        alSourcef(self._al, AL_PITCH, self._pitch)

    @property
    def direction(self) -> DVector3:
        self._ensure_open()
        return self._direction

    @direction.setter
    def direction(self, value: DVector3) -> None:
        self._ensure_open()
        if not isinstance(value, DVector3):
            raise TypeError(f'expected DVector3, got {value!r}')
        self._direction = value
        assert self._source is not None
        if self._source.channels != 1 and self._direction != DVector3(0):
            warn(
                f'{self._source} has more than 1 channel, it will be '
                f'unaffected by changes in direction'
            )
        f_direction = FVector3(*self._direction)
        alSourcefv(self._al, AL_DIRECTION, f_direction.pointer)

    @property
    def inner_cone_angle(self) -> float:
        self._ensure_open()
        return self._inner_cone_angle

    @inner_cone_angle.setter
    def inner_cone_angle(self, value: float) -> None:
        self._ensure_open()
        value = float(value)
        if value < 0.0 or value > (2 * pi):
            raise ValueError('inner cone angle must be between 0.0 and 2pi')
        self._inner_cone_angle = value
        assert self._source is not None
        if self._source.channels != 1 and self._inner_cone_angle != 2 * pi:
            warn(
                f'{self._source} has more than 1 channel, it will be '
                f'unaffected by changes in inner cone angle'
            )
        if self._direction == DVector3(0) and self._inner_cone_angle != 2 * pi:
            warn(
                f'{self._source} has no direction, it will be unaffected by '
                f'changes in inner cone angle'
            )
        alSourcef(
            self._al,
            AL_CONE_INNER_ANGLE,
            degrees(self._inner_cone_angle)
        )

    @property
    def outer_cone_angle(self) -> float:
        self._ensure_open()
        return self._outer_cone_angle

    @outer_cone_angle.setter
    def outer_cone_angle(self, value: float) -> None:
        self._ensure_open()
        value = float(value)
        if value < 0.0 or value > (2 * pi):
            raise ValueError('outer cone angle must be between 0.0 and 2pi')
        self._outer_cone_angle = value
        assert self._source is not None
        if self._source.channels != 1 and self._outer_cone_angle != 2 * pi:
            warn(
                f'{self._source} has more than 1 channel, it will be '
                f'unaffected by changes in outer cone angle'
            )
        if self._direction == DVector3(0) and self._outer_cone_angle != 2 * pi:
            warn(
                f'{self._source} has no direction, it will be unaffected by '
                f'changes in outer cone angle'
            )
        alSourcef(
            self._al,
            AL_CONE_OUTER_ANGLE,
            degrees(self._outer_cone_angle)
        )

    @property
    def outer_cone_gain(self) -> float:
        self._ensure_open()
        return self._outer_cone_gain

    @outer_cone_gain.setter
    def outer_cone_gain(self, value: float) -> None:
        self._ensure_open()
        value = float(value)
        if value < 0.0 or value > 1.0:
            raise ValueError('outer cone gain must be between 0.0 and 1.0')
        self._outer_cone_gain = value
        alSourcef(self._al, AL_CONE_OUTER_GAIN, self._outer_cone_gain)

    @property
    def is_open(self) -> bool:
        return self._is_open


def _stream_main(speaker_ref: ref[Speaker]) -> None:
    while True:
        speaker = speaker_ref()
        if speaker is None or not speaker._is_open:
            break
        if speaker.state != SpeakerState.STOPPED:
            speaker._stream()
        elif speaker._play:
            buffers_queued = c_int()
            alGetSourcei(speaker._al, AL_BUFFERS_QUEUED, buffers_queued)
            buffers_processed = c_int()
            alGetSourcei(speaker._al, AL_BUFFERS_PROCESSED, buffers_processed)
            if buffers_queued.value == buffers_processed.value:
                assert speaker._source is not None
                warn(
                    f'buffer underrun for {speaker._source}, '
                    f'audio may be choppy or incorrectly rendered: '
                    f'increase buffer count or buffer duration'
                )
                alSourcePlay(speaker._al)
                speaker._stream()
        del speaker
        time.sleep(.01)
