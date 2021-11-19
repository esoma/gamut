
from __future__ import annotations

__all__ = [
    'consume_stream_buffer',
    'get_sample_al_buffer',
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

        try:
            al_data_type = CHANNELS_DATA_TYPE_TO_AL_FORMAT[
                (channels, sample_width)
            ]
        except KeyError:
            raise ValueError('invalid channels/sample_width combination')

        al_id = c_uint()
        alGenBuffers(1, c_pointer(al_id))
        self._al: Optional[c_uint] = al_id

        alBufferData(self._al, al_data_type, data, len(data), sample_rate)

    def __del__(self) -> None:
        if hasattr(self, "_al") and self._al is not None:
            alDeleteBuffers(1, c_pointer(self._al))
            self._al = None
        self._al_context = release_al_context(self._al_context)

    @property
    def channels(self) -> int:
        return self._channels


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

        try:
            self._al_data_type = CHANNELS_DATA_TYPE_TO_AL_FORMAT[
                (channels, sample_width)
            ]
        except KeyError:
            raise ValueError('invalid channels/sample_width combination')
        self._sample_rate = sample_rate
        self._buffer_count = buffer_count
        self._buffer_duration = buffer_duration.total_seconds()

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


class Streamable(Protocol):

    def read(self, frames: int) -> bytes:
        ...

    def seek(self, frame: int) -> None:
        ...


def get_sample_al_buffer(sample: Sample) -> int:
    assert sample._al is not None
    return sample._al.value

def consume_stream_buffer(stream: Stream) -> Optional[int]:
    return stream._consume_buffer()

def return_stream_buffer(stream: Stream, al_buffer: int) -> None:
    return stream._return_buffer(al_buffer)
