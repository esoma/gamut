
# gamut
from gamut.geometry import Sphere
from gamut.math import BVector3, Matrix4, Vector3
from gamut.physics import Body, BodyType, World
# python
from datetime import timedelta
from math import isclose, pi
# pytest
import pytest


def test_no_linear_velocity() -> None:
    w = World(timedelta(seconds=1))
    b = Body(1, Sphere(Vector3(0), 1), world=w)

    w.simulate(timedelta(seconds=10))
    assert b.transform == Matrix4(1)


@pytest.mark.parametrize("linear_velocity", [
    Vector3(1, 0, 0),
    Vector3(0, 1, 0),
    Vector3(0, 0, 1)
])
def test_linear_velocity(linear_velocity: Vector3) -> None:
    w = World(timedelta(seconds=.1))
    b = Body(1, Sphere(Vector3(0), 1), world=w)
    b.linear_velocity = linear_velocity

    w.simulate(timedelta(seconds=1))
    assert all(
        all(isclose(rc, ec, abs_tol=1e-6) for rc, ec in zip(r, e))
        for r, e in zip(b.transform, Matrix4(1).translate(linear_velocity))
    )


@pytest.mark.parametrize("body_type", [
    BodyType.KINEMATIC,
    BodyType.STATIC,
])
def test_linear_velocity_non_dynamic(body_type: BodyType) -> None:
    w = World(timedelta(seconds=.1))
    b = Body(1, Sphere(Vector3(0), 1), world=w, type=body_type)
    b.linear_velocity = Vector3(1, 2, 3)

    w.simulate(timedelta(seconds=1))
    assert b.transform == Matrix4(1)


def test_disabled_linear_velocity() -> None:
    w = World(timedelta(seconds=.1))
    b = Body(1, Sphere(Vector3(0), 1), world=w)
    b.is_enabled = False
    b.linear_velocity = Vector3(1, 2, 3)

    w.simulate(timedelta(seconds=1))
    assert b.transform == Matrix4(1)


def test_no_linear_damping() -> None:
    w = World(timedelta(seconds=1))
    b = Body(1, Sphere(Vector3(0), 1), world=w)
    b.linear_velocity = Vector3(1, 2, 3)

    w.simulate(timedelta(seconds=10))
    assert b.linear_velocity == Vector3(1, 2, 3)


def test_linear_damping() -> None:
    w = World(timedelta(seconds=1))
    b = Body(1, Sphere(Vector3(0), 1), world=w)
    b.linear_velocity = Vector3(10, 10, 10)
    b.linear_damping = .5

    w.simulate(timedelta(seconds=1))
    assert b.linear_velocity == Vector3(5, 5, 5)
    w.simulate(timedelta(seconds=1))
    assert b.linear_velocity == Vector3(2.5, 2.5, 2.5)
    w.simulate(timedelta(seconds=1))
    assert b.linear_velocity == Vector3(1.25, 1.25, 1.25)


def test_linear_damping_kinematic() -> None:
    w = World(timedelta(seconds=1))
    b = Body(1, Sphere(Vector3(0), 1), world=w, type=BodyType.KINEMATIC)
    b.linear_velocity = Vector3(1, 2, 3)
    b.linear_damping = 1

    w.simulate(timedelta(seconds=10))
    assert b.linear_velocity == Vector3(1, 2, 3)


def test_linear_damping_static() -> None:
    w = World(timedelta(seconds=1))
    b = Body(1, Sphere(Vector3(0), 1), world=w, type=BodyType.STATIC)
    b.linear_velocity = Vector3(pi, pi, pi)
    b.linear_damping = .5

    w.simulate(timedelta(seconds=10))
    assert b.linear_velocity == Vector3(0, 0, 0)


def test_disabled_linear_damping() -> None:
    w = World(timedelta(seconds=.1))
    b = Body(1, Sphere(Vector3(0), 1), world=w)
    b.is_enabled = False
    b.linear_velocity = Vector3(1, 2, 3)
    b.linear_damping = .5

    w.simulate(timedelta(seconds=1))
    assert b.linear_velocity == Vector3(1, 2, 3)


def test_linear_freedom() -> None:
    w = World(timedelta(seconds=.1))
    b = Body(1, Sphere(Vector3(0), 1), world=w)

    b.linear_freedom = BVector3(False, False, False)
    b.linear_velocity = Vector3(1, 2, 3)
    assert b.linear_velocity == Vector3(0)

    b.linear_freedom = BVector3(True, True, True)
    b.linear_velocity = Vector3(1, 2, 3)
    b.linear_freedom = BVector3(False, False, False)
    assert b.linear_velocity == Vector3(0)

    w.gravity = Vector3(1)
    w.simulate(timedelta(seconds=1))
    assert b.linear_velocity == Vector3(0)


def test_linear_velocity_switch_to_kinematic() -> None:
    w = World(timedelta(seconds=.1))
    b = Body(1, Sphere(Vector3(0), 1), world=w)
    b.linear_velocity = Vector3(pi, 0, 0)
    b.linear_damping = .5

    w.simulate(timedelta(seconds=1))
    b.type = BodyType.KINEMATIC

    w.simulate(timedelta(seconds=1))
    assert (
        isclose(b.linear_velocity.x, pi * .5, abs_tol=1e-6) and
        b.linear_velocity.y == 0 and
        b.linear_velocity.z == 0
    )


def test_linear_velocity_switch_to_static() -> None:
    w = World(timedelta(seconds=.1))
    b = Body(1, Sphere(Vector3(0), 1), world=w)
    b.linear_velocity = Vector3(pi, 0, 0)
    b.linear_damping = .5

    w.simulate(timedelta(seconds=1))
    b.type = BodyType.STATIC

    w.simulate(timedelta(seconds=1))
    assert b.linear_velocity == Vector3(0)
