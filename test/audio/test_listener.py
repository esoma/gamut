
# gamut
from gamut.audio import Listener
from gamut.audio._alcontext import AlContext
from gamut.math import DVector3
# python
import gc
from typing import Any
# pytest
import pytest


def test_initialize_defaults(loopback_al_context: AlContext) -> None:
    listener = Listener()
    assert isinstance(listener.position, DVector3)
    assert listener.position == DVector3(0, 0, 0)
    assert isinstance(listener.velocity, DVector3)
    assert listener.velocity == DVector3(0, 0, 0)
    assert isinstance(listener.gain, float)
    assert listener.gain == 1.0
    assert isinstance(listener.direction, DVector3)
    assert listener.direction == DVector3(0, 0, -1)
    assert isinstance(listener.up, DVector3)
    assert listener.up == DVector3(0, 1, 0)


def test_activate_deactivate(loopback_al_context: AlContext) -> None:
    assert Listener.get_active() is None
    listener = Listener()
    listener2 = Listener()
    assert Listener.get_active() is None
    listener.deactivate()
    assert Listener.get_active() is None
    listener.activate()
    assert Listener.get_active() is listener
    listener.activate()
    assert Listener.get_active() is listener
    listener2.activate()
    assert Listener.get_active() is listener2
    listener.deactivate()
    assert Listener.get_active() is listener2
    listener2.deactivate()
    assert Listener.get_active() is None
    listener.activate()
    assert Listener.get_active() is listener
    del listener
    gc.collect()
    assert Listener.get_active() is None


@pytest.mark.parametrize("position", [
    DVector3(1, 2, 3),
    DVector3(4, 5, 6),
    DVector3(-1, -2, -3),
])
def test_position(loopback_al_context: AlContext, position: Any) -> None:
    listener = Listener()

    listener.position = position
    assert isinstance(listener.position, DVector3)
    assert listener.position == position

    position += DVector3(1)
    assert listener.position != position

    listener.activate()
    listener.position = position


@pytest.mark.parametrize("position", [(1, 2, 3), None, '123'])
def test_position_invalid_type(
    loopback_al_context: AlContext,
    position: Any
) -> None:
    listener = Listener()
    with pytest.raises(TypeError):
        listener.position = position


@pytest.mark.parametrize("velocity", [
    DVector3(1, 2, 3),
    DVector3(4, 5, 6),
    DVector3(-1, -2, -3),
])
def test_velocity(loopback_al_context: AlContext, velocity: Any) -> None:
    listener = Listener()

    listener.velocity = velocity
    assert isinstance(listener.velocity, DVector3)
    assert listener.velocity == velocity

    velocity += DVector3(1)
    assert listener.velocity != velocity

    listener.activate()
    listener.velocity = velocity


@pytest.mark.parametrize("velocity", [(1, 2, 3), None, '123'])
def test_velocity_invalid_type(
    loopback_al_context: AlContext,
    velocity: Any
) -> None:
    listener = Listener()
    with pytest.raises(TypeError):
        listener.velocity = velocity


@pytest.mark.parametrize("direction", [
    DVector3(1, 2, 3),
    DVector3(4, 5, 6),
    DVector3(-1, -2, -3),
])
def test_direction(loopback_al_context: AlContext, direction: Any) -> None:
    listener = Listener()

    listener.direction = direction
    assert isinstance(listener.direction, DVector3)
    assert listener.direction == direction

    direction += DVector3(1)
    assert listener.direction != direction

    listener.activate()
    listener.direction = direction


@pytest.mark.parametrize("direction", [(1, 2, 3), None, '123'])
def test_direction_invalid_type(
    loopback_al_context: AlContext,
    direction: Any
) -> None:
    listener = Listener()
    with pytest.raises(TypeError):
        listener.direction = direction


@pytest.mark.parametrize("up", [
    DVector3(1, 2, 3),
    DVector3(4, 5, 6),
    DVector3(-1, -2, -3),
])
def test_up(loopback_al_context: AlContext, up: Any) -> None:
    listener = Listener()

    listener.up = up
    assert isinstance(listener.up, DVector3)
    assert listener.up == up

    up += DVector3(1)
    assert listener.up != up

    listener.activate()
    listener.up = up


@pytest.mark.parametrize("up", [(1, 2, 3), None, '123'])
def test_up_invalid_type(
    loopback_al_context: AlContext,
    up: Any
) -> None:
    listener = Listener()
    with pytest.raises(TypeError):
        listener.up = up


@pytest.mark.parametrize("gain", [-1.0, -0.000001, 1.000001, 2.0])
def test_initial_gain_invalid_value(
    loopback_al_context: AlContext,
    gain: Any
) -> None:
    with pytest.raises(ValueError) as excinfo:
        Listener(gain=gain)
    assert str(excinfo.value) == 'gain must be between 0.0 and 1.0'


@pytest.mark.parametrize("gain", [-1.0, -0.000001, 1.000001, 2.0])
def test_set_gain_invalid_value(
    loopback_al_context: AlContext,
    gain: Any
) -> None:
    listener = Listener()
    with pytest.raises(ValueError) as excinfo:
        listener.gain = gain
    assert str(excinfo.value) == 'gain must be between 0.0 and 1.0'


def test_gain(loopback_al_context: AlContext) -> None:
    listener = Listener()

    listener.gain = .5
    assert listener.gain == .5
    assert isinstance(listener.gain, float)

    listener.activate()
    listener.gain = .75
