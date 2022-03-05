
# gamut
from gamut.geometry import Sphere
from gamut.physics import Body, BodyType, World
# python
from datetime import timedelta
from math import isclose, pi
# pyglm
from glm import dmat4, dvec3, rotate
# pytest
import pytest


def test_no_angular_velocity() -> None:
    w = World(timedelta(seconds=1))
    b = Body(1, Sphere(dvec3(0), 1), world=w)

    w.simulate(timedelta(seconds=10))
    assert b.transform == dmat4(1)


@pytest.mark.parametrize("angular_magnitude", [
    dvec3(1, 0, 0),
    dvec3(0, 1, 0),
    dvec3(0, 0, 1)
])
def test_angular_velocity(angular_magnitude: dvec3) -> None:
    w = World(timedelta(seconds=.1))
    b = Body(1, Sphere(dvec3(0), 1), world=w)
    b.angular_velocity = angular_magnitude * dvec3(pi)

    w.simulate(timedelta(seconds=1))
    assert all(
        all(isclose(rc, ec, abs_tol=1e-6) for rc, ec in zip(r, e))
        for r, e in zip(b.transform, rotate(dmat4(1), pi, angular_magnitude))
    )


@pytest.mark.parametrize("body_type", [
    BodyType.KINEMATIC,
    BodyType.STATIC,
])
def test_angular_velocity_non_dynamic(body_type: BodyType) -> None:
    w = World(timedelta(seconds=.1))
    b = Body(1, Sphere(dvec3(0), 1), world=w, type=body_type)
    b.angular_velocity = dvec3(pi, pi, pi)

    w.simulate(timedelta(seconds=1))
    assert b.transform == dmat4(1)


def test_disabled_angular_velocity() -> None:
    w = World(timedelta(seconds=.1))
    b = Body(1, Sphere(dvec3(0), 1), world=w)
    b.is_enabled = False
    b.angular_velocity = dvec3(pi, pi, pi)

    w.simulate(timedelta(seconds=1))
    assert b.transform == dmat4(1)


def test_no_angular_damping() -> None:
    w = World(timedelta(seconds=1))
    b = Body(1, Sphere(dvec3(0), 1), world=w)
    b.angular_velocity = dvec3(10, 0, 0)

    w.simulate(timedelta(seconds=10))
    assert b.angular_velocity == dvec3(10, 0, 0)


def test_angular_damping() -> None:
    w = World(timedelta(seconds=1))
    b = Body(1, Sphere(dvec3(0), 1), world=w)
    b.angular_velocity = dvec3(10, 10, 10)
    b.angular_damping = .5

    w.simulate(timedelta(seconds=1))
    assert b.angular_velocity == dvec3(5, 5, 5)
    w.simulate(timedelta(seconds=1))
    assert b.angular_velocity == dvec3(2.5, 2.5, 2.5)
    w.simulate(timedelta(seconds=1))
    assert b.angular_velocity == dvec3(1.25, 1.25, 1.25)


def test_angular_damping_kinematic() -> None:
    w = World(timedelta(seconds=1))
    b = Body(1, Sphere(dvec3(0), 1), world=w, type=BodyType.KINEMATIC)
    b.angular_velocity = dvec3(pi, pi, pi)
    b.angular_damping = 1

    w.simulate(timedelta(seconds=10))
    assert b.angular_velocity == dvec3(pi, pi, pi)


def test_angular_damping_static() -> None:
    w = World(timedelta(seconds=1))
    b = Body(1, Sphere(dvec3(0), 1), world=w, type=BodyType.STATIC)
    b.angular_velocity = dvec3(pi, pi, pi)
    b.angular_damping = .5

    w.simulate(timedelta(seconds=10))
    assert b.angular_velocity == dvec3(0, 0, 0)


def test_disabled_angular_damping() -> None:
    w = World(timedelta(seconds=.1))
    b = Body(1, Sphere(dvec3(0), 1), world=w)
    b.is_enabled = False
    b.angular_velocity = dvec3(1, 2, 3)
    b.angular_damping = .5

    w.simulate(timedelta(seconds=1))
    assert b.angular_velocity == dvec3(1, 2, 3)


def test_angular_velocity_switch_to_kinematic() -> None:
    w = World(timedelta(seconds=.1))
    b = Body(1, Sphere(dvec3(0), 1), world=w)
    b.angular_velocity = dvec3(pi, 0, 0)
    b.angular_damping = .5

    w.simulate(timedelta(seconds=1))
    b.type = BodyType.KINEMATIC

    w.simulate(timedelta(seconds=1))
    assert (
        isclose(b.angular_velocity.x, pi * .5, abs_tol=1e-6) and
        b.angular_velocity.y == 0 and
        b.angular_velocity.z == 0
    )


def test_angular_velocity_switch_to_static() -> None:
    w = World(timedelta(seconds=.1))
    b = Body(1, Sphere(dvec3(0), 1), world=w)
    b.angular_velocity = dvec3(pi, 0, 0)
    b.angular_damping = .5

    w.simulate(timedelta(seconds=1))
    b.type = BodyType.STATIC

    w.simulate(timedelta(seconds=1))
    assert b.angular_velocity == dvec3(0)
