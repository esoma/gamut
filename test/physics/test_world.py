
# gamut
from gamut.geometry import Sphere
from gamut.math import FVector3, Matrix4, Vector3
from gamut.physics import Body, RaycastHit, World
# python
from datetime import timedelta
from math import isclose as _isclose
from typing import Any
# pytest
import pytest


def is_close(a, b):
    return _isclose(a, b, abs_tol=1e-04)


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

    b1 = Body(1, Sphere(Vector3(0), 1), world=w)
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


@pytest.mark.parametrize("start", [None, (1, 2, 3), FVector3(1)])
def test_raycast_start_invalid(start: Any) -> None:
    w = World(timedelta(seconds=1))
    with pytest.raises(TypeError):
        w.raycast(start, Vector3(0))


@pytest.mark.parametrize("end", [None, (1, 2, 3), FVector3(1)])
def test_raycast_end_invalid(end: Any) -> None:
    w = World(timedelta(seconds=1))
    with pytest.raises(TypeError):
        w.raycast(Vector3(0), end)


def test_raycast() -> None:
    w = World(timedelta(seconds=1))
    b1 = Body(1, Sphere(Vector3(0), 1), world=w)
    b1.transform = Matrix4(1).translate(Vector3(5, 0, 0))
    b2 = Body(1, Sphere(Vector3(0), 1), world=w)
    b2.transform = Matrix4(1).translate(Vector3(-5, 0, 0))
    b3 = Body(1, Sphere(Vector3(0), 1), world=w)
    b3.transform = Matrix4(1).translate(Vector3(7, 0, 0))
    b4 = Body(1, Sphere(Vector3(0), 1), world=w)
    b4.transform = Matrix4(1).translate(Vector3(12, 0, 0))

    hit = w.raycast(Vector3(0), Vector3(10, 0, 0))
    assert isinstance(hit, RaycastHit)
    assert isinstance(hit.position, Vector3)
    assert hit.position == Vector3(4, 0, 0)
    assert isinstance(hit.normal, Vector3)
    assert hit.normal == Vector3(-1, 0, 0)
    assert hit.body is b1
    assert hit.time == 0.4

    hit = w.raycast(Vector3(10, 0, 0), Vector3(0))
    assert isinstance(hit, RaycastHit)
    assert isinstance(hit.position, Vector3)
    assert hit.position == Vector3(8, 0, 0)
    assert isinstance(hit.normal, Vector3)
    assert hit.normal == Vector3(1, 0, 0)
    assert hit.body is b3
    assert hit.time == 0.2


def test_raycast_sphere() -> None:
    w = World(timedelta(seconds=1))
    b1 = Body(1, Sphere(Vector3(0), 1), world=w)
    b1.transform = Matrix4(1).translate(Vector3(5, 0, 0))
    b2 = Body(1, Sphere(Vector3(0), 1), world=w)
    b2.transform = Matrix4(1).translate(Vector3(-5, 0, 0))
    b3 = Body(1, Sphere(Vector3(0), 1), world=w)
    b3.transform = Matrix4(1).translate(Vector3(7, 0, 0))
    b4 = Body(1, Sphere(Vector3(0), 1), world=w)
    b4.transform = Matrix4(1).translate(Vector3(13, 0, 0))

    hit = w.raycast(
        Vector3(0, 0, 1.5),
        Vector3(10, 0, 1.5),
        shape=Sphere(Vector3(0), 1)
    )
    assert isinstance(hit, RaycastHit)
    assert isinstance(hit.position, Vector3)
    assert is_close(hit.position.x, 4.338153699186215)
    assert is_close(hit.position.y, 0)
    assert is_close(hit.position.z, 0.7496395627894177)
    assert isinstance(hit.normal, Vector3)
    assert is_close(hit.normal.x, -0.6618463008137848)
    assert is_close(hit.normal.y, 0)
    assert is_close(hit.normal.z, 0.7496395627894177)
    assert hit.body is b1
    assert is_close(hit.time, 0.3675670948413434)

    hit = w.raycast(
        Vector3(10, 0, 0),
        Vector3(0),
        shape=Sphere(Vector3(0), 1)
    )
    assert isinstance(hit, RaycastHit)
    assert isinstance(hit.position, Vector3)
    assert hit.position == Vector3(8, 0, 0)
    assert isinstance(hit.normal, Vector3)
    assert hit.normal == Vector3(1, 0, 0)
    assert hit.body is b3
    assert is_close(hit.time, 0.09992300362041014)
