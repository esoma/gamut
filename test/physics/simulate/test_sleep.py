
# gamut
from gamut.geometry import Sphere
from gamut.math import Vector3
from gamut.physics import Body, BodyType, World
# python
from datetime import timedelta


def test_sleep() -> None:
    w = World(timedelta(seconds=1))
    b = Body(1, Sphere(Vector3(0), 1), world=w)
    assert not b.is_sleeping

    w.simulate(timedelta(seconds=10))
    assert b.is_sleeping


def test_wake() -> None:
    w = World(timedelta(seconds=1))
    b = Body(1, Sphere(Vector3(0), 1), world=w)
    assert not b.is_sleeping

    w.simulate(timedelta(seconds=10))
    assert b.is_sleeping

    b.wake()
    assert not b.is_sleeping


def test_wake_static() -> None:
    w = World(timedelta(seconds=1))
    b = Body(1, Sphere(Vector3(0), 1), world=w, type=BodyType.STATIC)
    assert b.is_sleeping
    b.wake()
    assert b.is_sleeping


def test_cannot_sleep() -> None:
    w = World(timedelta(seconds=1))
    b = Body(1, Sphere(Vector3(0), 1), world=w)
    b.can_sleep = False

    w.simulate(timedelta(seconds=10))
    assert not b.is_sleeping


def test_angular_sleep_threshold_cannot_sleep() -> None:
    w = World(timedelta(seconds=1))
    b = Body(1, Sphere(Vector3(0), 1), world=w)
    b.angular_sleep_threshold = 0

    w.simulate(timedelta(seconds=10))
    assert not b.is_sleeping


def test_linear_sleep_threshold_cannot_sleep() -> None:
    w = World(timedelta(seconds=1))
    b = Body(1, Sphere(Vector3(0), 1), world=w)
    b.linear_sleep_threshold = 0

    w.simulate(timedelta(seconds=10))
    assert not b.is_sleeping


def test_kinematic() -> None:
    w = World(timedelta(seconds=1))
    b = Body(1, Sphere(Vector3(0), 1), world=w, type=BodyType.KINEMATIC)

    w.simulate(timedelta(seconds=10))
    assert not b.is_sleeping


def test_static() -> None:
    w = World(timedelta(seconds=1))
    b = Body(1, Sphere(Vector3(0), 1), world=w, type=BodyType.STATIC)
    assert b.is_sleeping

    w.simulate(timedelta(seconds=10))
    assert b.is_sleeping
