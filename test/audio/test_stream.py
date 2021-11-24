
# gamut
from gamut.audio import Stream
from gamut.audio._alcontext import AlContext
from gamut.audio._source import consume_stream_buffer, return_stream_buffer
# python
from datetime import timedelta
from queue import Empty as QueueEmpty
from typing import Any
# pyopenal
from openal.al import alIsBuffer
# pytest
import pytest


@pytest.mark.parametrize("channels", [None, 1.1, 2.1, -1, 0, 3, 5, 7])
def test_invalid_channels(
    loopback_al_context: AlContext,
    channels: Any
) -> None:
    with pytest.raises(ValueError) as excinfo:
        Stream(channels, 8, 44100, DummyStreamable())
    assert str(excinfo.value) == 'invalid channels/sample_width combination'


@pytest.mark.parametrize("sample_width", [None, -8, 0, 1, 24, 32])
def test_invalid_sample_width(
    loopback_al_context: AlContext,
    sample_width: Any
) -> None:
    with pytest.raises(ValueError) as excinfo:
        Stream(1, sample_width, 44100, DummyStreamable())
    assert str(excinfo.value) == 'invalid channels/sample_width combination'


@pytest.mark.parametrize("sample_rate", [None, 100.5])
def test_invalid_sample_rate_type(
    loopback_al_context: AlContext,
    sample_rate: Any
) -> None:
    with pytest.raises(TypeError) as excinfo:
        Stream(1, 8, sample_rate, DummyStreamable())
    assert str(excinfo.value) == 'sample rate must be an integer'


@pytest.mark.parametrize("sample_rate", [-100, 0])
def test_invalid_sample_rate_value(
    loopback_al_context: AlContext,
    sample_rate: Any
) -> None:
    with pytest.raises(ValueError) as excinfo:
        Stream(1, 8, sample_rate, DummyStreamable())
    assert str(excinfo.value) == 'sample rate must be greater than 0'


@pytest.mark.parametrize("buffer_count", [None, object(), 2.0])
def test_invalid_buffer_count_type(
    loopback_al_context: AlContext,
    buffer_count: Any
) -> None:
    with pytest.raises(TypeError) as excinfo:
        Stream(1, 8, 44100, DummyStreamable(), buffer_count=buffer_count)
    assert str(excinfo.value) == 'buffer count must be an integer'


@pytest.mark.parametrize("buffer_count", [-100, -1, 0, 1])
def test_invalid_buffer_count_value(
    loopback_al_context: AlContext,
    buffer_count: int
) -> None:
    with pytest.raises(ValueError) as excinfo:
        Stream(1, 8, 44100, DummyStreamable(), buffer_count=buffer_count)
    assert str(excinfo.value) == 'buffer count must be at least 2'


@pytest.mark.parametrize("buffer_duration", [None, 1, 2.0, object()])
def test_invalid_buffer_duration_type(
    loopback_al_context: AlContext,
    buffer_duration: Any
) -> None:
    with pytest.raises(TypeError) as excinfo:
        Stream(1, 8, 44100, DummyStreamable(), buffer_duration=buffer_duration)
    assert str(excinfo.value) == 'buffer duration must be a timedelta'


@pytest.mark.parametrize("buffer_duration", [
    timedelta(seconds=-1),
    timedelta(seconds=0)
])
def test_invalid_buffer_duration_value(
    loopback_al_context: AlContext,
    buffer_duration: Any
) -> None:
    with pytest.raises(ValueError) as excinfo:
        Stream(1, 8, 44100, DummyStreamable(), buffer_duration=buffer_duration)
    assert str(excinfo.value) == 'buffer duration must be more than 0 seconds'


@pytest.mark.parametrize("channels", [1, 2])
@pytest.mark.parametrize("sample_width", [8, 16])
@pytest.mark.parametrize("sample_rate", [1, 8000, 44100, 96000])
def test_initialize(
    loopback_al_context: AlContext,
    channels: int,
    sample_width: int,
    sample_rate: int,
) -> None:
    streamable = DummyStreamable()
    streamable.seek(100)
    assert streamable.frame == 100

    stream = Stream(channels, sample_width, sample_rate, streamable)
    assert stream.channels == channels
    assert stream.sample_width == sample_width
    assert stream.sample_rate == sample_rate
    assert streamable.frame == 0


def test_reset(loopback_al_context: AlContext) -> None:
    streamable = DummyStreamable()
    stream = Stream(1, 8, 44100, streamable)
    assert streamable.frame == 0
    streamable.seek(99)
    assert streamable.frame == 99
    stream.reset()
    assert streamable.frame == 0


def test_consume_stream_buffer_no_data(loopback_al_context: AlContext) -> None:
    streamable = DummyStreamable()
    stream = Stream(1, 8, 44100, streamable)
    assert consume_stream_buffer(stream) is None


def test_consume_stream_buffer_partial_data(
    loopback_al_context: AlContext
) -> None:
    streamable = DummyStreamable()
    streamable.read_data = [b'\x01']
    stream = Stream(1, 8, 44100, streamable)
    assert alIsBuffer(consume_stream_buffer(stream))


def test_consume_stream_buffer_out_of_buffers(
    loopback_al_context: AlContext
) -> None:
    al_buffers: list[int] = []
    streamable = DummyStreamable()
    stream = Stream(1, 8, 44100, streamable, buffer_count=2)

    streamable.read_data = [b'\x00']
    al_buffer = consume_stream_buffer(stream)
    assert isinstance(al_buffer, int)
    al_buffers.append(al_buffer)
    assert alIsBuffer(al_buffer)

    streamable.read_data = [b'\x00']
    al_buffer = consume_stream_buffer(stream)
    assert isinstance(al_buffer, int)
    assert al_buffer not in al_buffers
    al_buffers.append(al_buffer)
    assert alIsBuffer(al_buffer)

    streamable.read_data = [b'\x00']
    with pytest.raises(QueueEmpty) as excinfo:
        consume_stream_buffer(stream)


def test_consume_stream_buffer_fill(
    loopback_al_context: AlContext
) -> None:
    streamable = DummyStreamable()
    buffer_duration = timedelta(seconds=.1)
    sample_rate = 44100
    stream = Stream(
        1, 8, sample_rate, streamable,
        buffer_duration=buffer_duration
    )
    frames_per_buffer = int(buffer_duration.total_seconds() * sample_rate)

    streamable.read_data = [b'\x00'] * (frames_per_buffer + 1)
    assert alIsBuffer(consume_stream_buffer(stream))
    assert streamable.read_data == [b'\x00']


def test_return_stream_buffer(
    loopback_al_context: AlContext
) -> None:
    al_buffers: list[int] = []
    streamable = DummyStreamable()
    stream = Stream(1, 8, 44100, streamable, buffer_count=2)

    streamable.read_data = [b'\x00']
    al_buffer = consume_stream_buffer(stream)
    assert isinstance(al_buffer, int)
    al_buffers.append(al_buffer)
    assert alIsBuffer(al_buffer)

    streamable.read_data = [b'\x00']
    al_buffer = consume_stream_buffer(stream)
    assert isinstance(al_buffer, int)
    al_buffers.append(al_buffer)
    assert alIsBuffer(al_buffer)

    return_stream_buffer(stream, al_buffers[0])

    streamable.read_data = [b'\x00']
    al_buffer = consume_stream_buffer(stream)
    assert al_buffer == al_buffers[0]
    assert alIsBuffer(al_buffer)


class DummyStreamable:

    def __init__(self) -> None:
        self.frame = 0
        self.read_data: list[bytes] = []

    def read(self, frames: int) -> bytes:
        read_value = b''.join(self.read_data[:frames])
        self.read_data = self.read_data[frames:]
        return read_value

    def seek(self, frame: int) -> None:
        self.frame = frame
