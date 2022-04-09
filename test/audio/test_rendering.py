
# gamut
from .util import assert_tone, generate_sin_sample
# gamut
from gamut.audio import Listener, Speaker
from gamut.audio._alcontext import AlContext
from gamut.math import DVector3
# python
from typing import Final
# pytest
import pytest

TEST_SAMPLES: Final = 1024
TEST_FREQUENCIES: Final = [43.05, 86.1, 172.25, 689.06, 1033.6]
TEST_MAGNITUDE = .173


@pytest.mark.parametrize("frequency", TEST_FREQUENCIES)
def test_baseline(
    loopback_al_context: AlContext,
    frequency: int
) -> None:
    speaker = Speaker(generate_sin_sample(frequency))
    speaker.play()
    assert_tone(loopback_al_context, 1024, frequency, TEST_MAGNITUDE)


@pytest.mark.parametrize("frequency", TEST_FREQUENCIES[1:])
def test_listener_not_active(
    loopback_al_context: AlContext,
    frequency: int
) -> None:
    listener = Listener(gain=.5)
    speaker = Speaker(generate_sin_sample(frequency))
    speaker.play()
    assert_tone(loopback_al_context, 1024, frequency, TEST_MAGNITUDE)


@pytest.mark.parametrize("frequency", TEST_FREQUENCIES[1:])
def test_listener_deactivated(
    loopback_al_context: AlContext,
    frequency: int
) -> None:
    listener = Listener(gain=.5)
    listener.activate()
    listener.deactivate()
    speaker = Speaker(generate_sin_sample(frequency))
    speaker.play()
    assert_tone(loopback_al_context, 1024, frequency, TEST_MAGNITUDE)


@pytest.mark.parametrize("frequency", TEST_FREQUENCIES[1:])
def test_speaker_pitch_down(
    loopback_al_context: AlContext,
    frequency: int
) -> None:
    speaker = Speaker(generate_sin_sample(frequency))
    speaker.pitch = .5
    speaker.play()
    assert_tone(loopback_al_context, 1024, frequency * .5, TEST_MAGNITUDE)


@pytest.mark.parametrize("frequency", TEST_FREQUENCIES)
def test_speaker_pitch_up(
    loopback_al_context: AlContext,
    frequency: int
) -> None:
    speaker = Speaker(generate_sin_sample(frequency))
    speaker.pitch = 2.0
    speaker.play()
    assert_tone(loopback_al_context, 1024, frequency * 2, TEST_MAGNITUDE)


@pytest.mark.parametrize("frequency", TEST_FREQUENCIES)
def test_speaker_gain_down(
    loopback_al_context: AlContext,
    frequency: int
) -> None:
    speaker = Speaker(generate_sin_sample(frequency))
    speaker.gain = .5
    speaker.play()
    assert_tone(loopback_al_context, 1024, frequency, TEST_MAGNITUDE * .5)


@pytest.mark.parametrize("frequency", TEST_FREQUENCIES)
def test_listener_gain_down(
    loopback_al_context: AlContext,
    frequency: int
) -> None:
    listener = Listener(gain=.5)
    listener.activate()
    speaker = Speaker(generate_sin_sample(frequency))
    speaker.play()
    assert_tone(loopback_al_context, 1024, frequency, TEST_MAGNITUDE * .5)


@pytest.mark.parametrize("frequency", TEST_FREQUENCIES)
def test_speaker_position_left(
    loopback_al_context: AlContext,
    frequency: int
) -> None:
    speaker = Speaker(generate_sin_sample(frequency))
    speaker.position = DVector3(-1, 0, 0)
    speaker.play()
    assert_tone(loopback_al_context, 1024, (frequency, 0), None)


@pytest.mark.parametrize("frequency", TEST_FREQUENCIES)
def test_speaker_position_right(
    loopback_al_context: AlContext,
    frequency: int
) -> None:
    speaker = Speaker(generate_sin_sample(frequency))
    speaker.position = DVector3(1, 0, 0)
    speaker.play()
    assert_tone(loopback_al_context, 1024, (0, frequency), None)


@pytest.mark.parametrize("frequency", TEST_FREQUENCIES)
def test_listener_position_left(
    loopback_al_context: AlContext,
    frequency: int
) -> None:
    listener = Listener(position=DVector3(-1, 0, 0))
    listener.activate()
    speaker = Speaker(generate_sin_sample(frequency))
    speaker.play()
    assert_tone(loopback_al_context, 1024, (0, frequency), None)


@pytest.mark.parametrize("frequency", TEST_FREQUENCIES)
@pytest.mark.parametrize("listener_position", [
    DVector3(0, 0, 0),
    DVector3(10, -10, 10),
    DVector3(-100, 0, 0),
])
def test_speaker_relative_position_left(
    loopback_al_context: AlContext,
    frequency: int,
    listener_position: DVector3
) -> None:
    listener = Listener(position=listener_position)
    listener.activate()
    speaker = Speaker(generate_sin_sample(frequency))
    speaker.is_relative = True
    speaker.position = DVector3(-1, 0, 0)
    speaker.play()
    assert_tone(loopback_al_context, 1024, (frequency, 0), None)


@pytest.mark.parametrize("frequency", TEST_FREQUENCIES)
@pytest.mark.parametrize("listener_position", [
    DVector3(0, 0, 0),
    DVector3(10, -10, 10),
    DVector3(-100, 0, 0),
])
def test_speaker_relative_position_right(
    loopback_al_context: AlContext,
    frequency: int,
    listener_position: DVector3
) -> None:
    listener = Listener(position=listener_position)
    listener.activate()
    speaker = Speaker(generate_sin_sample(frequency))
    speaker.is_relative = True
    speaker.position = DVector3(1, 0, 0)
    speaker.play()
    assert_tone(loopback_al_context, 1024, (0, frequency), None)
