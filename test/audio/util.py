
__all__ = ['assert_frequency', 'generate_sin_sample']

# gamut
from gamut.audio import Sample
from gamut.audio._alcontext import AlContext
# numpy
import numpy as np


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


def assert_frequency(al_context: AlContext, frequency: int) -> None:
    raw = al_context.render(1024)
    float_data = (
        np.frombuffer(raw, dtype=np.uint8) # type: ignore
        .astype(np.float32) - 127.5
    ) / 255.0
    magnitudes = np.abs(np.fft.fft(float_data)) # type: ignore
    freqs = np.fft.fftfreq(len(float_data)) * 22050 # type: ignore
    i = np.argmax(magnitudes)
    try:
        low_bound = freqs[i - 1]
    except IndexError:
        low_bound = 0.0
    try:
        high_bound = freqs[i + 1]
    except IndexError:
        high_bound = 22050.0
    assert frequency >= low_bound, f'{frequency} >= {low_bound}'
    assert frequency <= high_bound, f'{frequency} <= {high_bound}'
