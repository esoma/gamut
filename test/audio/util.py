
__all__ = ['assert_tone', 'generate_sin_sample']

# gamut
from gamut.audio import Sample
from gamut.audio._alcontext import AlContext, LOOP_BACK_FREQUENCY
# python
from typing import Any
# numpy
import numpy as np
# pytest
import pytest


def generate_sin_sample(frequency: int) -> Sample:
    sin_data = np.sin(
        frequency * 2 * np.pi * np.linspace(0, 1, 44100, endpoint=False)
    )
    return Sample(
        1,
        8,
        44100,
        bytes((((sin_data + 1) / 2.0) * 255).astype(np.uint8))
    )


def assert_tone(
    al_context: AlContext,
    samples: int,
    frequency: Any,
    magnitude: Any
) -> None:
    if isinstance(frequency, tuple):
        left_frequency, right_frequency = frequency
    else:
        left_frequency = right_frequency = frequency
    if isinstance(magnitude, tuple):
        left_magnitude, right_magnitude = magnitude
    else:
        left_magnitude = right_magnitude = magnitude
    left, right = al_context.render(samples)
    assert_frequency_channel(left, left_frequency, left_magnitude)
    assert_frequency_channel(right, right_frequency, right_magnitude)


def assert_frequency_channel(
    raw: bytes,
    expected_frequency: Any,
    expected_magnitude: Any
) -> None:
    float_data = (
        np.frombuffer(raw, dtype=np.uint8) # type: ignore
        .astype(np.float32) - 127.5
    ) / 255.0
    magnitudes = np.abs(np.fft.fft(float_data)) # type: ignore
    freqs = (
        np.fft.fftfreq(len(float_data)) * # type: ignore
        LOOP_BACK_FREQUENCY
    )
    i = np.argmax(magnitudes)
    magnitude = magnitudes[i] / len(float_data)
    frequency = abs(freqs[i])
    assert frequency == pytest.approx(expected_frequency, abs=0.1), (
        f'{frequency} != {expected_frequency}'
    )
    if expected_magnitude is not None:
        assert magnitude == pytest.approx(expected_magnitude, abs=0.05), (
            f'{magnitude} != {expected_magnitude}'
        )
