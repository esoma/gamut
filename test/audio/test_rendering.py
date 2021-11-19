
# gamut
from .util import assert_frequency, generate_sin_sample
# gamut
from gamut.audio import Speaker
from gamut.audio._alcontext import AlContext
# pytest
import pytest


@pytest.mark.parametrize("frequency", [50, 120, 400, 800, 1200])
def test_frequency(
    loopback_al_context: AlContext,
    frequency: int
) -> None:
    speaker = Speaker(generate_sin_sample(frequency))
    speaker.play()
    assert_frequency(loopback_al_context, frequency)
