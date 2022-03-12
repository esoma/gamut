
# gamut
from gamut.audio import Sample, Speaker, SpeakerState, Stream
from gamut.audio._alcontext import AlContext, LOOP_BACK_FREQUENCY
from gamut.math import Vector3
# python
from math import pi
from typing import Any, Optional, Union
# pytest
import pytest


@pytest.mark.parametrize("source_type", [Sample, Stream])
def test_initialize_defaults(
    loopback_al_context: AlContext,
    source_type: Union[type[Sample], type[Stream]],
) -> None:
    source = create_source(source_type)
    with Speaker(source) as speaker:
        assert speaker.source is source
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
        assert isinstance(speaker.loop, bool)
        assert not speaker.loop
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
        assert speaker.state == SpeakerState.STOPPED
        assert speaker.is_open


def test_set_source_sample(loopback_al_context: AlContext) -> None:
    source = create_source(Sample)
    sample = create_source(Sample)
    stream = create_source(Stream)
    with Speaker(source) as speaker:
        assert speaker.source is source
        speaker.source = sample
        assert speaker.source is sample
        with pytest.raises(TypeError) as excinfo:
            speaker.source = stream
        assert str(excinfo.value) == 'may only change the source to a sample'


def test_set_source_stream(loopback_al_context: AlContext) -> None:
    source = create_source(Stream)
    sample = create_source(Sample)
    stream = create_source(Stream)
    with Speaker(source) as speaker:
        assert speaker.source is source
        with pytest.raises(TypeError) as excinfo:
            speaker.source = sample
        assert str(excinfo.value) == (
            'may only change the source if it is a sample'
        )
        with pytest.raises(TypeError) as excinfo:
            speaker.source = stream
        assert str(excinfo.value) == (
            'may only change the source if it is a sample'
        )


@pytest.mark.parametrize("source_type", [Sample, Stream])
def test_close(
    loopback_al_context: AlContext,
    source_type: Union[type[Sample], type[Stream]],
) -> None:
    speaker = Speaker(create_source(source_type))
    assert speaker.is_open
    speaker.close()
    assert not speaker.is_open
    speaker.close()
    assert not speaker.is_open

    with pytest.raises(RuntimeError) as excinfo:
        speaker.play()
    assert str(excinfo.value) == 'speaker is closed'

    with pytest.raises(RuntimeError) as excinfo:
        speaker.pause()
    assert str(excinfo.value) == 'speaker is closed'

    with pytest.raises(RuntimeError) as excinfo:
        speaker.stop()
    assert str(excinfo.value) == 'speaker is closed'

    with pytest.raises(RuntimeError) as excinfo:
        speaker.source
    assert str(excinfo.value) == 'speaker is closed'

    with pytest.raises(RuntimeError) as excinfo:
        speaker.state
    assert str(excinfo.value) == 'speaker is closed'

    with pytest.raises(RuntimeError) as excinfo:
        speaker.position
    assert str(excinfo.value) == 'speaker is closed'

    with pytest.raises(RuntimeError) as excinfo:
        speaker.position = Vector3()
    assert str(excinfo.value) == 'speaker is closed'

    with pytest.raises(RuntimeError) as excinfo:
        speaker.velocity
    assert str(excinfo.value) == 'speaker is closed'

    with pytest.raises(RuntimeError) as excinfo:
        speaker.velocity = Vector3()
    assert str(excinfo.value) == 'speaker is closed'

    with pytest.raises(RuntimeError) as excinfo:
        speaker.min_gain
    assert str(excinfo.value) == 'speaker is closed'

    with pytest.raises(RuntimeError) as excinfo:
        speaker.min_gain = .5
    assert str(excinfo.value) == 'speaker is closed'

    with pytest.raises(RuntimeError) as excinfo:
        speaker.gain
    assert str(excinfo.value) == 'speaker is closed'

    with pytest.raises(RuntimeError) as excinfo:
        speaker.gain = .5
    assert str(excinfo.value) == 'speaker is closed'

    with pytest.raises(RuntimeError) as excinfo:
        speaker.max_gain
    assert str(excinfo.value) == 'speaker is closed'

    with pytest.raises(RuntimeError) as excinfo:
        speaker.max_gain = .5
    assert str(excinfo.value) == 'speaker is closed'

    with pytest.raises(RuntimeError) as excinfo:
        speaker.is_relative
    assert str(excinfo.value) == 'speaker is closed'

    with pytest.raises(RuntimeError) as excinfo:
        speaker.is_relative = True
    assert str(excinfo.value) == 'speaker is closed'

    with pytest.raises(RuntimeError) as excinfo:
        speaker.loop
    assert str(excinfo.value) == 'speaker is closed'

    with pytest.raises(RuntimeError) as excinfo:
        speaker.loop = True
    assert str(excinfo.value) == 'speaker is closed'

    with pytest.raises(RuntimeError) as excinfo:
        speaker.pitch
    assert str(excinfo.value) == 'speaker is closed'

    with pytest.raises(RuntimeError) as excinfo:
        speaker.pitch = .5
    assert str(excinfo.value) == 'speaker is closed'

    with pytest.raises(RuntimeError) as excinfo:
        speaker.direction
    assert str(excinfo.value) == 'speaker is closed'

    with pytest.raises(RuntimeError) as excinfo:
        speaker.direction = Vector3()
    assert str(excinfo.value) == 'speaker is closed'

    with pytest.raises(RuntimeError) as excinfo:
        speaker.inner_cone_angle
    assert str(excinfo.value) == 'speaker is closed'

    with pytest.raises(RuntimeError) as excinfo:
        speaker.inner_cone_angle = .5
    assert str(excinfo.value) == 'speaker is closed'

    with pytest.raises(RuntimeError) as excinfo:
        speaker.outer_cone_angle
    assert str(excinfo.value) == 'speaker is closed'

    with pytest.raises(RuntimeError) as excinfo:
        speaker.outer_cone_angle = .5
    assert str(excinfo.value) == 'speaker is closed'

    with pytest.raises(RuntimeError) as excinfo:
        speaker.outer_cone_gain
    assert str(excinfo.value) == 'speaker is closed'

    with pytest.raises(RuntimeError) as excinfo:
        speaker.outer_cone_gain = .5
    assert str(excinfo.value) == 'speaker is closed'


@pytest.mark.parametrize("source", [None, object(), b'\x00\x00'])
def test_invalid_source_type(
    loopback_al_context: AlContext,
    source: Any
) -> None:
    with pytest.raises(TypeError) as excinfo:
        Speaker(source)
    assert str(excinfo.value) == 'source must be either a Sample or Stream'


@pytest.mark.parametrize("source_type", [Sample, Stream])
@pytest.mark.parametrize("position", [
    Vector3(1, 2, 3),
    Vector3(-1, -2, -3)
])
def test_position(
    loopback_al_context: AlContext,
    source_type: Union[type[Sample], type[Stream]],
    position: Any
) -> None:
    with Speaker(create_source(source_type)) as speaker:
        speaker.position = position
        assert isinstance(speaker.position, Vector3)
        assert speaker.position == position

        position += Vector3(1)
        assert speaker.position != position


def test_position_stereo(loopback_al_context: AlContext) -> None:
    source = Sample(2, 8, 44100, b'')
    with Speaker(source) as speaker:
        with pytest.warns(UserWarning) as warnings:
                speaker.position = Vector3(1)
        assert len(warnings) == 1
        assert warnings[0].message.args[0] == ( # type: ignore
            f'{source} has more than 1 channel, it will be '
            f'unaffected by changes in position'
        )


@pytest.mark.parametrize("source_type", [Sample, Stream])
@pytest.mark.parametrize("velocity", [
    Vector3(1, 2, 3),
    Vector3(-1, -2, -3)
])
def test_velocity(
    loopback_al_context: AlContext,
    source_type: Union[type[Sample], type[Stream]],
    velocity: Any
) -> None:
    with Speaker(create_source(source_type)) as speaker:
        speaker.velocity = velocity
        assert isinstance(speaker.velocity, Vector3)
        assert speaker.velocity == velocity

        velocity += Vector3(1)
        assert speaker.velocity != velocity


def test_velocity_stereo(loopback_al_context: AlContext) -> None:
    source = Sample(2, 8, 44100, b'')
    with Speaker(source) as speaker:
        with pytest.warns(UserWarning) as warnings:
                speaker.velocity = Vector3(1)
        assert len(warnings) == 1
        assert warnings[0].message.args[0] == ( # type: ignore
            f'{source} has more than 1 channel, it will be '
            f'unaffected by changes in velocity'
        )


@pytest.mark.parametrize("source_type", [Sample, Stream])
@pytest.mark.parametrize("direction", [
    Vector3(1, 2, 3),
    Vector3(-1, -2, -3)
])
def test_direction(
    loopback_al_context: AlContext,
    source_type: Union[type[Sample], type[Stream]],
    direction: Any
) -> None:
    with Speaker(create_source(source_type)) as speaker:
        speaker.direction = direction
        assert isinstance(speaker.direction, Vector3)
        assert speaker.direction == direction

        direction += Vector3(1)
        assert speaker.direction != direction


def test_direction_stereo(loopback_al_context: AlContext) -> None:
    source = Sample(2, 8, 44100, b'')
    with Speaker(source) as speaker:
        with pytest.warns(UserWarning) as warnings:
                speaker.direction = Vector3(1)
        assert len(warnings) == 1
        assert warnings[0].message.args[0] == ( # type: ignore
            f'{source} has more than 1 channel, it will be '
            f'unaffected by changes in direction'
        )


@pytest.mark.parametrize("source_type", [Sample, Stream])
@pytest.mark.parametrize("min_gain", [0, 0.0, .5, 1.0, 1])
def test_min_gain(
    loopback_al_context: AlContext,
    source_type: Union[type[Sample], type[Stream]],
    min_gain: Any,
) -> None:
    with Speaker(create_source(source_type)) as speaker:
        speaker.min_gain = min_gain
        assert speaker.min_gain == min_gain
        assert isinstance(speaker.min_gain, float)


@pytest.mark.parametrize("source_type", [Sample, Stream])
@pytest.mark.parametrize("min_gain", [-1.0, -0.000001, 1.000001, 2.0])
def test_min_gain_invalid(
    loopback_al_context: AlContext,
    source_type: Union[type[Sample], type[Stream]],
    min_gain: Any
) -> None:
    with pytest.raises(ValueError) as excinfo:
        Speaker(create_source(source_type), min_gain=min_gain)
    assert str(excinfo.value) == 'min gain must be between 0.0 and 1.0'

    with Speaker(create_source(source_type)) as speaker:
        with pytest.raises(ValueError) as excinfo:
            speaker.min_gain = min_gain
    assert str(excinfo.value) == 'min gain must be between 0.0 and 1.0'


@pytest.mark.parametrize("source_type", [Sample, Stream])
@pytest.mark.parametrize("gain", [0, 0.0, .5, 1.0, 1])
def test_gain(
    loopback_al_context: AlContext,
    source_type: Union[type[Sample], type[Stream]],
    gain: Any,
) -> None:
    with Speaker(create_source(source_type)) as speaker:
        speaker.gain = gain
        assert speaker.gain == float(gain)
        assert isinstance(speaker.gain, float)


@pytest.mark.parametrize("source_type", [Sample, Stream])
@pytest.mark.parametrize("gain", [-1.0, -0.000001, 1.000001, 2.0])
def test_gain_invalid(
    loopback_al_context: AlContext,
    source_type: Union[type[Sample], type[Stream]],
    gain: Any
) -> None:
    with pytest.raises(ValueError) as excinfo:
        Speaker(create_source(source_type), gain=gain)
    assert str(excinfo.value) == 'gain must be between 0.0 and 1.0'

    with Speaker(create_source(source_type)) as speaker:
        with pytest.raises(ValueError) as excinfo:
            speaker.gain = gain
    assert str(excinfo.value) == 'gain must be between 0.0 and 1.0'


@pytest.mark.parametrize("source_type", [Sample, Stream])
@pytest.mark.parametrize("max_gain", [0, 0.0, .5, 1.0, 1])
def test_max_gain(
    loopback_al_context: AlContext,
    source_type: Union[type[Sample], type[Stream]],
    max_gain: Any,
) -> None:
    with Speaker(create_source(source_type)) as speaker:
        speaker.max_gain = max_gain
        assert speaker.max_gain == float(max_gain)
        assert isinstance(speaker.max_gain, float)


@pytest.mark.parametrize("source_type", [Sample, Stream])
@pytest.mark.parametrize("max_gain", [-1.0, -0.000001, 1.000001, 2.0])
def test_max_gain_invalid(
    loopback_al_context: AlContext,
    source_type: Union[type[Sample], type[Stream]],
    max_gain: Any
) -> None:
    with pytest.raises(ValueError) as excinfo:
        Speaker(create_source(source_type), max_gain=max_gain)
    assert str(excinfo.value) == 'max gain must be between 0.0 and 1.0'

    with Speaker(create_source(source_type)) as speaker:
        with pytest.raises(ValueError) as excinfo:
            speaker.max_gain = max_gain
    assert str(excinfo.value) == 'max gain must be between 0.0 and 1.0'


@pytest.mark.parametrize("source_type", [Sample, Stream])
@pytest.mark.parametrize("is_relative", [0, 1, False, True, None, '', 'sdf'])
def test_is_relative(
    loopback_al_context: AlContext,
    source_type: Union[type[Sample], type[Stream]],
    is_relative: Any,
) -> None:
    with Speaker(create_source(source_type)) as speaker:
        speaker.is_relative = is_relative
        assert speaker.is_relative == bool(is_relative)
        assert isinstance(speaker.is_relative, bool)


@pytest.mark.parametrize("source_type", [Sample, Stream])
@pytest.mark.parametrize("loop", [0, 1, False, True, None, '', 'sdf'])
def test_is_loop(
    loopback_al_context: AlContext,
    source_type: Union[type[Sample], type[Stream]],
    loop: Any,
) -> None:
    with Speaker(create_source(source_type)) as speaker:
        speaker.loop = loop
        assert speaker.loop == bool(loop)
        assert isinstance(speaker.loop, bool)


@pytest.mark.parametrize("source_type", [Sample, Stream])
@pytest.mark.parametrize("pitch", [0, 0.0, .5, 1.0, 1, 2.0, 10.5])
def test_pitch(
    loopback_al_context: AlContext,
    source_type: Union[type[Sample], type[Stream]],
    pitch: Any,
) -> None:
    with Speaker(create_source(source_type)) as speaker:
        speaker.pitch = pitch
        assert speaker.pitch == float(pitch)
        assert isinstance(speaker.pitch, float)


@pytest.mark.parametrize("source_type", [Sample, Stream])
@pytest.mark.parametrize("pitch", [-0.000001, -1.0, -10.0])
def test_pitch_invalid(
    loopback_al_context: AlContext,
    source_type: Union[type[Sample], type[Stream]],
    pitch: Any
) -> None:
    with pytest.raises(ValueError) as excinfo:
        Speaker(create_source(source_type), pitch=pitch)
    assert str(excinfo.value) == 'pitch must be 0.0 or greater'

    with Speaker(create_source(source_type)) as speaker:
        with pytest.raises(ValueError) as excinfo:
            speaker.pitch = pitch
    assert str(excinfo.value) == 'pitch must be 0.0 or greater'


@pytest.mark.parametrize("source_type", [Sample, Stream])
@pytest.mark.parametrize("inner_cone_angle", [0.0, pi, pi * 2])
def test_inner_cone_angle(
    loopback_al_context: AlContext,
    source_type: Union[type[Sample], type[Stream]],
    inner_cone_angle: Any,
) -> None:
    source = create_source(source_type)
    with Speaker(source) as speaker:
        if inner_cone_angle == pi * 2:
            speaker.inner_cone_angle = inner_cone_angle
        else:
            with pytest.warns(UserWarning) as warnings:
                speaker.inner_cone_angle = inner_cone_angle
            assert len(warnings) == 1
            assert warnings[0].message.args[0] == ( # type: ignore
                f'{source} has no direction, it will be unaffected by '
                f'changes in inner cone angle'
            )
        assert isinstance(speaker.inner_cone_angle, float)


def test_inner_cone_angle_stereo(loopback_al_context: AlContext) -> None:
    source = Sample(2, 8, 44100, b'')
    with Speaker(source) as speaker:
        with pytest.warns(UserWarning) as warnings:
                speaker.inner_cone_angle = pi
        assert len(warnings) == 2
        assert warnings[0].message.args[0] == ( # type: ignore
            f'{source} has more than 1 channel, it will be '
            f'unaffected by changes in inner cone angle'
        )


@pytest.mark.parametrize("source_type", [Sample, Stream])
@pytest.mark.parametrize("inner_cone_angle", [-0.000001, (pi * 2) + .000001])
def test_inner_cone_angle_invalid(
    loopback_al_context: AlContext,
    source_type: Union[type[Sample], type[Stream]],
    inner_cone_angle: Any
) -> None:
    with pytest.raises(ValueError) as excinfo:
        Speaker(create_source(source_type), inner_cone_angle=inner_cone_angle)
    assert str(excinfo.value) == 'inner cone angle must be between 0.0 and 2pi'

    with Speaker(create_source(source_type)) as speaker:
        with pytest.raises(ValueError) as excinfo:
            speaker.inner_cone_angle = inner_cone_angle
    assert str(excinfo.value) == 'inner cone angle must be between 0.0 and 2pi'


@pytest.mark.parametrize("source_type", [Sample, Stream])
@pytest.mark.parametrize("outer_cone_angle", [0.0, pi, pi * 2])
def test_outer_cone_angle(
    loopback_al_context: AlContext,
    source_type: Union[type[Sample], type[Stream]],
    outer_cone_angle: Any,
) -> None:
    source = create_source(source_type)
    with Speaker(source) as speaker:
        if outer_cone_angle == pi * 2:
            speaker.outer_cone_angle = outer_cone_angle
        else:
            with pytest.warns(UserWarning) as warnings:
                speaker.outer_cone_angle = outer_cone_angle
            assert len(warnings) == 1
            assert warnings[0].message.args[0] == ( # type: ignore
                f'{source} has no direction, it will be unaffected by '
                f'changes in outer cone angle'
            )
        assert isinstance(speaker.outer_cone_angle, float)


def test_outer_cone_angle_stereo(loopback_al_context: AlContext) -> None:
    source = Sample(2, 8, 44100, b'')
    with Speaker(source) as speaker:
        with pytest.warns(UserWarning) as warnings:
                speaker.outer_cone_angle = pi
        assert len(warnings) == 2
        assert warnings[0].message.args[0] == ( # type: ignore
            f'{source} has more than 1 channel, it will be '
            f'unaffected by changes in outer cone angle'
        )


@pytest.mark.parametrize("source_type", [Sample, Stream])
@pytest.mark.parametrize("outer_cone_angle", [-0.000001, (pi * 2) + .000001])
def test_outer_cone_angle_invalid(
    loopback_al_context: AlContext,
    source_type: Union[type[Sample], type[Stream]],
    outer_cone_angle: Any
) -> None:
    with pytest.raises(ValueError) as excinfo:
        Speaker(create_source(source_type), outer_cone_angle=outer_cone_angle)
    assert str(excinfo.value) == 'outer cone angle must be between 0.0 and 2pi'

    with Speaker(create_source(source_type)) as speaker:
        with pytest.raises(ValueError) as excinfo:
            speaker.outer_cone_angle = outer_cone_angle
    assert str(excinfo.value) == 'outer cone angle must be between 0.0 and 2pi'


@pytest.mark.parametrize("source_type", [Sample, Stream])
@pytest.mark.parametrize("outer_cone_gain", [0, 0.0, .5, 1.0, 1])
def test_outer_cone_gain(
    loopback_al_context: AlContext,
    source_type: Union[type[Sample], type[Stream]],
    outer_cone_gain: Any,
) -> None:
    with Speaker(create_source(source_type)) as speaker:
        speaker.outer_cone_gain = outer_cone_gain
        assert speaker.outer_cone_gain == float(outer_cone_gain)
        assert isinstance(speaker.outer_cone_gain, float)


@pytest.mark.parametrize("source_type", [Sample, Stream])
@pytest.mark.parametrize("outer_cone_gain", [-1.0, -0.000001, 1.000001, 2.0])
def test_outer_cone_gain_invalid(
    loopback_al_context: AlContext,
    source_type: Union[type[Sample], type[Stream]],
    outer_cone_gain: Any
) -> None:
    with pytest.raises(ValueError) as excinfo:
        Speaker(create_source(source_type), outer_cone_gain=outer_cone_gain)
    assert str(excinfo.value) == 'outer cone gain must be between 0.0 and 1.0'

    with Speaker(create_source(source_type)) as speaker:
        with pytest.raises(ValueError) as excinfo:
            speaker.outer_cone_gain = outer_cone_gain
    assert str(excinfo.value) == 'outer cone gain must be between 0.0 and 1.0'


@pytest.mark.parametrize("source_type", [Sample, Stream])
def test_controls(
    loopback_al_context: AlContext,
    source_type: Union[type[Sample], type[Stream]],
) -> None:
    with Speaker(create_source(source_type)) as speaker:
        assert speaker.state == SpeakerState.STOPPED
        speaker.play()
        assert speaker.state == SpeakerState.PLAYING
        speaker.pause()
        assert speaker.state == SpeakerState.PAUSED
        speaker.resume()
        assert speaker.state == SpeakerState.PLAYING
        speaker.pause()
        assert speaker.state == SpeakerState.PAUSED
        speaker.play()
        assert speaker.state == SpeakerState.PLAYING
        speaker.stop()
        assert speaker.state == SpeakerState.STOPPED
        speaker.resume()
        assert speaker.state == SpeakerState.STOPPED


def test_sample_reached_end(loopback_al_context: AlContext) -> None:
    sample = Sample(1, 8, 44100, b'\x00' * 44100)
    with Speaker(sample) as speaker:
        speaker.play()
        assert speaker.state == SpeakerState.PLAYING
        loopback_al_context.render(LOOP_BACK_FREQUENCY - 1)
        assert speaker.state == SpeakerState.PLAYING
        loopback_al_context.render(1)
        assert speaker.state == SpeakerState.STOPPED


def test_stream_reached_end(loopback_al_context: AlContext) -> None:
    streamable = DummyStreamable()
    streamable.data = [b'\x00'] * 44100
    with Speaker(Stream(1, 8, 44100, streamable)) as speaker:
        speaker.play()
        assert speaker.state == SpeakerState.PLAYING
        loopback_al_context.render(LOOP_BACK_FREQUENCY - 1, real_time=True)
        assert speaker.state == SpeakerState.PLAYING
        loopback_al_context.render(1, real_time=True)
        assert speaker.state == SpeakerState.STOPPED


def test_stream_underrun(loopback_al_context: AlContext) -> None:
    streamable = UnderrunStreamable()
    stream = Stream(1, 8, 44100, streamable, buffer_count=2)
    with Speaker(stream) as speaker:
        speaker.play()
        with pytest.warns(UserWarning) as warnings:
            loopback_al_context.render(LOOP_BACK_FREQUENCY, real_time=True)
        warning_messages = list({
            warning.message.args[0] for warning in warnings # type: ignore
        })
        assert len(warning_messages) == 1
        assert warning_messages[0] == (
            f'buffer underrun for {stream}, '
            f'audio may be choppy or incorrectly rendered: '
            f'increase buffer count or buffer duration'
        )


@pytest.mark.parametrize("source_type", [Sample, Stream])
def test_loop(
    loopback_al_context: AlContext,
    source_type: Union[type[Sample], type[Stream]],
) -> None:
    source: Union[Sample, Stream]
    if source_type is Sample:
        source = Sample(1, 8, 44100, b'\x00' * 44100)
    else:
        assert source_type is Stream
        streamable = DummyStreamable()
        streamable.data = streamable.reset_data = [b'\x00'] * 44100
        source = Stream(1, 8, 44100, streamable)
    with Speaker(source, loop=True) as speaker:
        speaker.play()
        assert speaker.state == SpeakerState.PLAYING
        loopback_al_context.render(
            LOOP_BACK_FREQUENCY,
            real_time=source_type is Stream
        )
        assert speaker.state == SpeakerState.PLAYING
        loopback_al_context.render(
            LOOP_BACK_FREQUENCY,
            real_time=source_type is Stream
        )
        assert speaker.state == SpeakerState.PLAYING
        speaker.loop = False
        loopback_al_context.render(
            LOOP_BACK_FREQUENCY,
            real_time=source_type is Stream
        )
        assert speaker.state == SpeakerState.STOPPED


def create_source(
    source_type: Union[type[Sample], type[Stream]]
) -> Union[Sample, Stream]:
    if source_type is Sample:
        return Sample(1, 8, 44100, b'\x00' * 44100)
    else:
        assert source_type is Stream
        return Stream(1, 8, 44100, DummyStreamable())


class DummyStreamable:

    def __init__(self) -> None:
        self.data: Optional[list[bytes]] = None
        self.reset_data: Optional[list[bytes]] = None

    def read(self, frames: int) -> bytes:
        if self.data is None:
            return b'\x00' * frames
        results = self.data[:frames]
        self.data = self.data[frames:]
        return b''.join(results)

    def seek(self, frame: int) -> None:
        assert frame == 0
        if self.reset_data is not None:
            self.data = self.reset_data


class UnderrunStreamable:

    def read(self, frames: int) -> bytes:
        return b'\x00'

    def seek(self, frame: int) -> None:
        pass
