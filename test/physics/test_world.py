
# gamut
from gamut.geometry import Sphere
from gamut.math import Vector3
from gamut.physics import Body, World
# python
from datetime import timedelta
from typing import Any
# pyglm
from glm import vec3
# pytest
import pytest


@pytest.mark.parametrize("fixed_time_step", [None, 'abc', 123, 1.0])
def test_invalid_fixed_time_step_type(fixed_time_step: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        World(fixed_time_step)
    assert str(excinfo.value) == 'fixed time step must be timedelta'


@pytest.mark.parametrize("fixed_time_step", [
    timedelta(seconds=-1),
    timedelta(seconds=0),
])
def test_invalid_fixed_time_step_value(fixed_time_step: timedelta) -> None:
    with pytest.raises(ValueError) as excinfo:
        World(fixed_time_step)
    assert (
        str(excinfo.value) == 'fixed time step must be greater than 0 seconds'
    )


def test_repr() -> None:
    w = World(timedelta(seconds=1))
    assert repr(w) == '<gamut.physics.World>'


def test_default_gravity() -> None:
    w = World(timedelta(seconds=1))
    assert isinstance(w.gravity, Vector3)
    assert w.gravity == Vector3(0)


@pytest.mark.parametrize("gravity", [
    Vector3(1, 2, 3),
    Vector3(4, 5, 6),
    Vector3(7, 8, 9),
])
def test_gravity_change(gravity: Vector3) -> None:
    w = World(timedelta(seconds=1))
    w.gravity = gravity
    assert w.gravity == gravity
    assert w.gravity is not gravity
    assert isinstance(w.gravity, Vector3)


@pytest.mark.parametrize("gravity", [
    None,
    1,
    (1, 2),
    (1, 2, 3, 4),
    'abc',
])
def test_invalid_gravity(gravity: Any) -> None:
    w = World(timedelta(seconds=1))
    with pytest.raises(TypeError) as excinfo:
        w.gravity = gravity
    assert str(excinfo.value) == f'expected DVector3, got {gravity!r}'


def test_bodies() -> None:
    w = World(timedelta(seconds=1))
    assert not w.bodies

    b1 = Body(1, Sphere(vec3(0), 1), world=w)
    assert len(w.bodies) == 1
    assert b1 in w.bodies

    b1.world = None
    assert not w.bodies


def test_bodies_mutable() -> None:
    w = World(timedelta(seconds=1))

    bodies = w.bodies
    assert bodies is not w.bodies
    assert isinstance(bodies, list)


@pytest.mark.parametrize("duration", [None, 'abc', 123, 1.0])
def test_simulate_duration_invalid_type(duration: timedelta) -> None:
    w = World(timedelta(seconds=1))
    with pytest.raises(TypeError) as excinfo:
        w.simulate(duration)
    assert str(excinfo.value) == 'duration must be timedelta'


@pytest.mark.parametrize("duration", [
    timedelta(seconds=-10),
    timedelta(seconds=-1),
])
def test_invalid_fixed_time_step_value(duration: timedelta) -> None:
    w = World(timedelta(seconds=1))
    with pytest.raises(ValueError) as excinfo:
        w.simulate(duration)
    assert (
        str(excinfo.value) ==
        'duration must be greater than or equal to 0 seconds'
    )
