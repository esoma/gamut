
# gamut
from gamut.audio import Sample
from gamut.audio._alcontext import AlContext
from gamut.audio._source import get_sample_al_buffer
# python
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
        Sample(channels, 8, 44100, b'')
    assert str(excinfo.value) == 'invalid channels/sample_width combination'


@pytest.mark.parametrize("sample_width", [None, -8, 0, 1, 24, 32])
def test_invalid_sample_width(
    loopback_al_context: AlContext,
    sample_width: Any
) -> None:
    with pytest.raises(ValueError) as excinfo:
        Sample(1, sample_width, 44100, b'')
    assert str(excinfo.value) == 'invalid channels/sample_width combination'


@pytest.mark.parametrize("sample_rate", [None, 100.5])
def test_invalid_sample_rate_type(
    loopback_al_context: AlContext,
    sample_rate: Any
) -> None:
    with pytest.raises(TypeError) as excinfo:
        Sample(1, 8, sample_rate, b'')
    assert str(excinfo.value) == 'sample rate must be an integer'


@pytest.mark.parametrize("sample_rate", [-100, 0])
def test_invalid_sample_rate_value(
    loopback_al_context: AlContext,
    sample_rate: Any
) -> None:
    with pytest.raises(ValueError) as excinfo:
        Sample(1, 8, sample_rate, b'')
    assert str(excinfo.value) == 'sample rate must be greater than 0'


@pytest.mark.parametrize("data", [None, 1, object()])
def test_invalid_data_type(
    loopback_al_context: AlContext,
    data: Any
) -> None:
    with pytest.raises(TypeError) as excinfo:
        Sample(1, 8, 44100, data)
    assert str(excinfo.value) == 'data must be bytes'


@pytest.mark.parametrize("channels, sample_width, data", [
    (1, 16, b'\x00'),
    (1, 16, b'\x00\x00\x00'),
    (2, 8, b'\x00'),
    (2, 8, b'\x00\x00\x00'),
    (2, 16, b'\x00'),
    (2, 16, b'\x00\x00'),
    (2, 16, b'\x00\x00\x00'),
    (2, 16, b'\x00\x00\x00\x00\x00'),
    (2, 16, b'\x00\x00\x00\x00\x00\x00'),
    (2, 16, b'\x00\x00\x00\x00\x00\x00\x00'),
])
def test_invalid_data_value(
    loopback_al_context: AlContext,
    channels: int,
    sample_width: int,
    data: bytes
) -> None:
    with pytest.raises(ValueError) as excinfo:
        Sample(channels, sample_width, 44100, data)
    assert str(excinfo.value) == 'data contains partial frames'


@pytest.mark.parametrize("channels", [1, 2])
@pytest.mark.parametrize("sample_width", [8, 16])
@pytest.mark.parametrize("sample_rate", [1, 8000, 44100, 96000])
@pytest.mark.parametrize("data_multiplier", [0, 1, 10])
def test_initialize(
    loopback_al_context: AlContext,
    channels: int,
    sample_width: int,
    sample_rate: int,
    data_multiplier: int,
) -> None:
    data = b'\x00' * (sample_width // 8) * channels * data_multiplier
    sample = Sample(channels, sample_width, sample_rate, data)
    assert sample.channels == channels
    assert sample.sample_width == sample_width
    assert sample.sample_rate == sample_rate


def test_get_sample_al_buffer(loopback_al_context: AlContext) -> None:
    sample = Sample(1, 8, 44100, b'')
    al_buffer = get_sample_al_buffer(sample)
    assert isinstance(al_buffer, int)
    assert alIsBuffer(al_buffer)
