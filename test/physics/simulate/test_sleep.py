
# gamut
from gamut.geometry import Composite3d, Mesh3d, Sphere
from gamut.math import DVector3, DVector3Array, UVector3, UVector3Array
from gamut.physics import Body, BodyType, World
# python
from datetime import timedelta


def test_sleep() -> None:
    w = World(timedelta(seconds=1))
    b = Body(1, Sphere(DVector3(0), 1), world=w)
    assert not b.is_sleeping

    w.simulate(timedelta(seconds=10))
    assert b.is_sleeping


def test_wake() -> None:
    w = World(timedelta(seconds=1))
    b = Body(1, Sphere(DVector3(0), 1), world=w)
    assert not b.is_sleeping

    w.simulate(timedelta(seconds=10))
    assert b.is_sleeping

    b.wake()
    assert not b.is_sleeping


def test_wake_static() -> None:
    w = World(timedelta(seconds=1))
    b = Body(1, Sphere(DVector3(0), 1), world=w, type=BodyType.STATIC)
    assert b.is_sleeping
    b.wake()
    assert b.is_sleeping


def test_cannot_sleep() -> None:
    w = World(timedelta(seconds=1))
    b = Body(1, Sphere(DVector3(0), 1), world=w)
    b.can_sleep = False

    w.simulate(timedelta(seconds=10))
    assert not b.is_sleeping


def test_cannot_sleep_static() -> None:
    w = World(timedelta(seconds=1))
    shape = Composite3d(
        Sphere(DVector3(0), 1),
        Mesh3d(
            DVector3Array(DVector3(0), DVector3(1), DVector3(2)),
            UVector3Array(UVector3(0), UVector3(1), UVector3(2))
        ),
    )
    b = Body(1, shape, world=w, type=BodyType.STATIC)
    b.can_sleep = False

    w.simulate(timedelta(seconds=10))
    assert not b.is_sleeping


def test_angular_sleep_threshold_cannot_sleep() -> None:
    w = World(timedelta(seconds=1))
    b = Body(1, Sphere(DVector3(0), 1), world=w)
    b.angular_sleep_threshold = 0

    w.simulate(timedelta(seconds=10))
    assert not b.is_sleeping


def test_linear_sleep_threshold_cannot_sleep() -> None:
    w = World(timedelta(seconds=1))
    b = Body(1, Sphere(DVector3(0), 1), world=w)
    b.linear_sleep_threshold = 0

    w.simulate(timedelta(seconds=10))
    assert not b.is_sleeping


def test_kinematic() -> None:
    w = World(timedelta(seconds=1))
    b = Body(1, Sphere(DVector3(0), 1), world=w, type=BodyType.KINEMATIC)

    w.simulate(timedelta(seconds=10))
    assert not b.is_sleeping


def test_static() -> None:
    w = World(timedelta(seconds=1))
    b = Body(1, Sphere(DVector3(0), 1), world=w, type=BodyType.STATIC)
    assert b.is_sleeping

    w.simulate(timedelta(seconds=10))
    assert b.is_sleeping
