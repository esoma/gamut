
# gamut
from gamut.audio import MultiSpeaker, Sample, SpeakerState
from gamut.audio._alcontext import AlContext
from gamut.math import Vector3
# python
from math import pi
from typing import Any, Union
# pytest
import pytest


@pytest.fixture
def sample() -> Sample:
    return Sample(1, 8, 44100, b'\x00' * 44100)


def test_initialize_defaults(loopback_al_context: AlContext) -> None:
    speaker = MultiSpeaker()
    assert isinstance(speaker.position, Vector3)
    assert speaker.position == Vector3(0, 0, 0)
    assert isinstance(speaker.velocity, Vector3)
    assert speaker.velocity == Vector3(0, 0, 0)
    assert isinstance(speaker.min_gain, float)
    assert speaker.min_gain == 0.0
    assert isinstance(speaker.gain, float)
    assert speaker.gain == 1.0
    assert isinstance(speaker.max_gain, float)
    assert speaker.max_gain == 1.0
    assert isinstance(speaker.is_relative, bool)
    assert not speaker.is_relative
    assert isinstance(speaker.pitch, float)
    assert speaker.pitch == 1.0
    assert isinstance(speaker.direction, Vector3)
    assert speaker.direction == Vector3(0, 0, 0)
    assert isinstance(speaker.inner_cone_angle, float)
    assert speaker.inner_cone_angle == 2 * pi
    assert isinstance(speaker.outer_cone_angle, float)
    assert speaker.outer_cone_angle == 2 * pi
    assert isinstance(speaker.outer_cone_gain, float)
    assert speaker.outer_cone_gain == 0.0


def test_controls(loopback_al_context: AlContext, sample: Sample) -> None:
    multi_speaker = MultiSpeaker()
    speakers = [multi_speaker.play(sample) for _ in range(10)]
    assert all(s.state == SpeakerState.PLAYING for s in speakers)
    multi_speaker.pause()
    assert all(s.state == SpeakerState.PAUSED for s in speakers)
    multi_speaker.resume()
    assert all(s.state == SpeakerState.PLAYING for s in speakers)
    multi_speaker.stop()
    assert all(s.state == SpeakerState.STOPPED for s in speakers)
    multi_speaker.resume()
    assert all(s.state == SpeakerState.STOPPED for s in speakers)


def test_play_reuse(loopback_al_context: AlContext, sample: Sample) -> None:
    multi_speaker = MultiSpeaker()
    speaker_1 = multi_speaker.play(sample)
    multi_speaker.stop()
    speaker_2 = multi_speaker.play(sample)
    assert speaker_2 is speaker_1
    speaker_3 = multi_speaker.play(sample)
    assert speaker_3 is not speaker_1


@pytest.mark.parametrize("position", [Vector3(1, 2, 3), Vector3(-1, -2, -3)])
def test_position(
    loopback_al_context: AlContext,
    sample: Sample,
    position: Union[Vector3, tuple[int, int, int]]
) -> None:
    multi_speaker = MultiSpeaker()
    speakers = [multi_speaker.play(sample) for _ in range(10)]
    assert all(s.position == multi_speaker.position for s in speakers)
    multi_speaker.position = position
    assert multi_speaker.position == position
    assert isinstance(multi_speaker.position, Vector3)
    assert all(s.position == multi_speaker.position for s in speakers)


@pytest.mark.parametrize("position", [(1, 2, 3), '123', None])
def test_position_invalid_type(
    loopback_al_context: AlContext,
    position: Any
) -> None:
    multi_speaker = MultiSpeaker()
    with pytest.raises(TypeError):
        multi_speaker.position = position


@pytest.mark.parametrize("velocity", [Vector3(1, 2, 3), Vector3(-1, -2, -3)])
def test_velocity(
    loopback_al_context: AlContext,
    sample: Sample,
    velocity: Union[Vector3, tuple[int, int, int]]
) -> None:
    multi_speaker = MultiSpeaker()
    speakers = [multi_speaker.play(sample) for _ in range(10)]
    assert all(s.velocity == multi_speaker.velocity for s in speakers)
    multi_speaker.velocity = velocity
    assert multi_speaker.velocity == velocity
    assert isinstance(multi_speaker.velocity, Vector3)
    assert all(s.velocity == multi_speaker.velocity for s in speakers)


@pytest.mark.parametrize("velocity", [(1, 2, 3), '123', None])
def test_velocity_invalid_type(
    loopback_al_context: AlContext,
    velocity: Any
) -> None:
    multi_speaker = MultiSpeaker()
    with pytest.raises(TypeError):
        multi_speaker.velocity = velocity


@pytest.mark.parametrize("direction", [Vector3(1, 2, 3), Vector3(-1, -2, -3)])
def test_direction(
    loopback_al_context: AlContext,
    sample: Sample,
    direction: Union[Vector3, tuple[int, int, int]]
) -> None:
    multi_speaker = MultiSpeaker()
    speakers = [multi_speaker.play(sample) for _ in range(10)]
    assert all(s.direction == multi_speaker.direction for s in speakers)
    multi_speaker.direction = direction
    assert multi_speaker.direction == direction
    assert isinstance(multi_speaker.direction, Vector3)
    assert all(s.direction == multi_speaker.direction for s in speakers)


@pytest.mark.parametrize("direction", [(1, 2, 3), '123', None])
def test_direction_invalid_type(
    loopback_al_context: AlContext,
    direction: Any
) -> None:
    multi_speaker = MultiSpeaker()
    with pytest.raises(TypeError):
        multi_speaker.direction = direction


@pytest.mark.parametrize("min_gain", [0, 0.0, .5, 1.0, 1])
def test_min_gain(
    loopback_al_context: AlContext,
    sample: Sample,
    min_gain: float
) -> None:
    multi_speaker = MultiSpeaker()
    speakers = [multi_speaker.play(sample) for _ in range(10)]
    assert all(s.min_gain == multi_speaker.min_gain for s in speakers)
    multi_speaker.min_gain = min_gain
    assert multi_speaker.min_gain == min_gain
    assert isinstance(multi_speaker.min_gain, float)
    assert all(s.min_gain == multi_speaker.min_gain for s in speakers)


@pytest.mark.parametrize("gain", [0, 0.0, .5, 1.0, 1])
def test_gain(
    loopback_al_context: AlContext,
    sample: Sample,
    gain: float
) -> None:
    multi_speaker = MultiSpeaker()
    speakers = [multi_speaker.play(sample) for _ in range(10)]
    assert all(s.gain == multi_speaker.gain for s in speakers)
    multi_speaker.gain = gain
    assert multi_speaker.gain == gain
    assert isinstance(multi_speaker.gain, float)
    assert all(s.gain == multi_speaker.gain for s in speakers)


@pytest.mark.parametrize("max_gain", [0, 0.0, .5, 1.0, 1])
def test_max_gain(
    loopback_al_context: AlContext,
    sample: Sample,
    max_gain: float
) -> None:
    multi_speaker = MultiSpeaker()
    speakers = [multi_speaker.play(sample) for _ in range(10)]
    assert all(s.max_gain == multi_speaker.max_gain for s in speakers)
    multi_speaker.max_gain = max_gain
    assert multi_speaker.max_gain == max_gain
    assert isinstance(multi_speaker.max_gain, float)
    assert all(s.max_gain == multi_speaker.max_gain for s in speakers)


@pytest.mark.parametrize("is_relative", [True, False, 0, 1, None, '', 'sdf'])
def test_is_relative(
    loopback_al_context: AlContext,
    sample: Sample,
    is_relative: Any
) -> None:
    multi_speaker = MultiSpeaker()
    speakers = [multi_speaker.play(sample) for _ in range(10)]
    assert all(s.is_relative == multi_speaker.is_relative for s in speakers)
    multi_speaker.is_relative = is_relative
    assert multi_speaker.is_relative == bool(is_relative)
    assert isinstance(multi_speaker.is_relative, bool)
    assert all(s.is_relative == multi_speaker.is_relative for s in speakers)


@pytest.mark.parametrize("pitch", [0, 0.0, .5, 1.0, 1, 2.0, 10.5])
def test_pitch(
    loopback_al_context: AlContext,
    sample: Sample,
    pitch: float
) -> None:
    multi_speaker = MultiSpeaker()
    speakers = [multi_speaker.play(sample) for _ in range(10)]
    assert all(s.pitch == multi_speaker.pitch for s in speakers)
    multi_speaker.pitch = pitch
    assert multi_speaker.pitch == pitch
    assert isinstance(multi_speaker.pitch, float)
    assert all(s.pitch == multi_speaker.pitch for s in speakers)


@pytest.mark.parametrize("inner_cone_angle", [0.0, pi, pi * 2])
def test_inner_cone_angle(
    loopback_al_context: AlContext,
    sample: Sample,
    inner_cone_angle: float
) -> None:
    multi_speaker = MultiSpeaker()
    speakers = [multi_speaker.play(sample) for _ in range(10)]
    assert all(
        s.inner_cone_angle == multi_speaker.inner_cone_angle
        for s in speakers
    )
    if inner_cone_angle == pi * 2:
        multi_speaker.inner_cone_angle = inner_cone_angle
    else:
        with pytest.warns(UserWarning) as warnings:
            multi_speaker.inner_cone_angle = inner_cone_angle
        assert len(warnings) == 10
        for warning in warnings:
            assert warning.message.args[0] == ( # type: ignore
                f'{sample} has no direction, it will be unaffected by '
                f'changes in inner cone angle'
            )
    assert multi_speaker.inner_cone_angle == inner_cone_angle
    assert isinstance(multi_speaker.inner_cone_angle, float)
    assert all(
        s.inner_cone_angle == multi_speaker.inner_cone_angle
        for s in speakers
    )


@pytest.mark.parametrize("outer_cone_angle", [0.0, pi, pi * 2])
def test_outer_cone_angle(
    loopback_al_context: AlContext,
    sample: Sample,
    outer_cone_angle: float
) -> None:
    multi_speaker = MultiSpeaker()
    speakers = [multi_speaker.play(sample) for _ in range(10)]
    assert all(
        s.outer_cone_angle == multi_speaker.outer_cone_angle
        for s in speakers
    )
    if outer_cone_angle == pi * 2:
        multi_speaker.outer_cone_angle = outer_cone_angle
    else:
        with pytest.warns(UserWarning) as warnings:
            multi_speaker.outer_cone_angle = outer_cone_angle
        assert len(warnings) == 10
        for warning in warnings:
            assert warning.message.args[0] == ( # type: ignore
                f'{sample} has no direction, it will be unaffected by '
                f'changes in outer cone angle'
            )
    assert multi_speaker.outer_cone_angle == outer_cone_angle
    assert isinstance(multi_speaker.outer_cone_angle, float)
    print([s.outer_cone_angle for s in speakers])
    print(multi_speaker.outer_cone_angle)
    assert all(
        s.outer_cone_angle == multi_speaker.outer_cone_angle
        for s in speakers
    )


@pytest.mark.parametrize("outer_cone_gain", [0, 0.0, .5, 1.0, 1])
def test_outer_cone_gain(
    loopback_al_context: AlContext,
    sample: Sample,
    outer_cone_gain: float
) -> None:
    multi_speaker = MultiSpeaker()
    speakers = [multi_speaker.play(sample) for _ in range(10)]
    assert all(
        s.outer_cone_gain == multi_speaker.outer_cone_gain
        for s in speakers
    )
    multi_speaker.outer_cone_gain = outer_cone_gain
    assert multi_speaker.outer_cone_gain == outer_cone_gain
    assert isinstance(multi_speaker.outer_cone_gain, float)
    assert all(
        s.outer_cone_gain == multi_speaker.outer_cone_gain
        for s in speakers
    )
