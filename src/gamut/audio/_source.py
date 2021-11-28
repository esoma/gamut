
from __future__ import annotations

__all__ = [
    'consume_stream_buffer',
    'get_sample_al_buffer',
    'release_sample_al_buffer',
    'return_stream_buffer',
    'Sample',
    'Stream',
    'Streamable',
]

# gamut
from ._alcontext import release_al_context, require_al_context
# python
from ctypes import POINTER as C_POINTER
from ctypes import c_uint
from ctypes import cast as c_cast
from ctypes import pointer as c_pointer
from datetime import timedelta
from queue import Queue
from typing import Any, Final, Optional, Protocol
# pyopenal
from openal.al import (AL_FORMAT_MONO8, AL_FORMAT_MONO16, AL_FORMAT_STEREO8,
                       AL_FORMAT_STEREO16, alBufferData, alDeleteBuffers,
                       alGenBuffers)

CHANNELS_DATA_TYPE_TO_AL_FORMAT: Final = {
    (1, 8): AL_FORMAT_MONO8,
    (2, 8): AL_FORMAT_STEREO8,
    (1, 16): AL_FORMAT_MONO16,
    (2, 16): AL_FORMAT_STEREO16,
}


class Sample:

    def __init__(
        self,
        channels: int,
        sample_width: int,
        sample_rate: int,
        data: bytes,
    ):
        self._al_context = require_al_context()

        self._channels = channels
        self._sample_width = sample_width
        self._sample_rate = sample_rate

        try:
            al_data_type = CHANNELS_DATA_TYPE_TO_AL_FORMAT[
                (channels, sample_width)
            ]
        except KeyError:
            raise ValueError('invalid channels/sample_width combination')
        if not isinstance(sample_rate, int):
            raise TypeError('sample rate must be an integer')
        if sample_rate < 1:
            raise ValueError('sample rate must be greater than 0')
        if not isinstance(data, bytes):
            raise TypeError('data must be bytes')
        assert sample_width % 8 == 0
        if len(data) % (channels * (sample_width / 8)) != 0:
            raise ValueError('data contains partial frames')

        al_id = c_uint()
        alGenBuffers(1, c_pointer(al_id))
        self._al: Optional[c_uint] = al_id
        self._al_refs: int = 1

        alBufferData(self._al, al_data_type, data, len(data), sample_rate)

    def __del__(self) -> None:
        if self._al is not None:
            release_sample_al_buffer(self)
        self._al_context = release_al_context(self._al_context)

    @property
    def channels(self) -> int:
        return self._channels

    @property
    def sample_width(self) -> int:
        return self._sample_width

    @property
    def sample_rate(self) -> int:
        return self._sample_rate


class Stream:

    def __init__(
        self,
        channels: int,
        sample_width: int,
        sample_rate: int,
        streamable: Streamable,
        *,
        buffer_count: int = 3,
        buffer_duration: timedelta = timedelta(seconds=.1),
    ):
        self._al_context = require_al_context()

        self._channels = channels
        self._sample_width = sample_width
        self._sample_rate = sample_rate

        try:
            self._al_data_type = CHANNELS_DATA_TYPE_TO_AL_FORMAT[
                (channels, sample_width)
            ]
        except KeyError:
            raise ValueError('invalid channels/sample_width combination')
        if not isinstance(sample_rate, int):
            raise TypeError('sample rate must be an integer')
        if sample_rate < 1:
            raise ValueError('sample rate must be greater than 0')
        if not isinstance(buffer_count, int):
            raise TypeError('buffer count must be an integer')
        if buffer_count < 2:
            raise ValueError('buffer count must be at least 2')
        if not isinstance(buffer_duration, timedelta):
            raise TypeError('buffer duration must be a timedelta')

        self._buffer_count = buffer_count
        self._buffer_duration = buffer_duration.total_seconds()

        if self._buffer_duration <= 0:
            raise ValueError('buffer duration must be more than 0 seconds')

        al_ids = (c_uint * buffer_count)()
        alGenBuffers(
            buffer_count,
            c_cast(al_ids, C_POINTER(c_uint))
        )
        self._als: Any = al_ids

        self._free_buffers: Queue[int] = Queue()
        for al in self._als:
            self._free_buffers.put(al)

        self._streamable = streamable
        self._streamable.seek(0)

    def _consume_buffer(self) -> Optional[int]:
        al_buffer = self._free_buffers.get_nowait()
        data = self._streamable.read(
            max(1, int(self._buffer_duration * self._sample_rate))
        )
        if not data:
            self._free_buffers.put(al_buffer)
            return None
        alBufferData(
            al_buffer,
            self._al_data_type,
            data,
            len(data),
            self._sample_rate
        )
        return al_buffer

    def _return_buffer(self, al_buffer: int) -> None:
        assert al_buffer in self._als
        self._free_buffers.put(al_buffer)

    def __del__(self) -> None:
        if hasattr(self, "_als") and self._als is not None:
            alDeleteBuffers(
                self._buffer_count,
                c_cast(self._als, C_POINTER(c_uint))
            )
            self._als = None
        self._al_context = release_al_context(self._al_context)

    def reset(self) -> None:
        self._streamable.seek(0)

    @property
    def channels(self) -> int:
        return self._channels

    @property
    def sample_width(self) -> int:
        return self._sample_width

    @property
    def sample_rate(self) -> int:
        return self._sample_rate


class Streamable(Protocol):

    def read(self, frames: int) -> bytes:
        ...

    def seek(self, frame: int) -> None:
        ...


def get_sample_al_buffer(sample: Sample) -> int:
    assert sample._al is not None
    sample._al_refs += 1
    return sample._al.value


def release_sample_al_buffer(sample: Sample) -> None:
    assert sample._al_refs > 0
    sample._al_refs -= 1
    if sample._al_refs == 0:
        assert sample._al is not None
        alDeleteBuffers(1, c_pointer(sample._al))
        sample._al = None


def consume_stream_buffer(stream: Stream) -> Optional[int]:
    return stream._consume_buffer()


def return_stream_buffer(stream: Stream, al_buffer: int) -> None:
    return stream._return_buffer(al_buffer)
