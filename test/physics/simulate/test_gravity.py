
# gamut
from gamut.geometry import Sphere
from gamut.math import DMatrix4, DVector3
from gamut.physics import Body, BodyType, World
# python
from datetime import timedelta
# pytest
import pytest


def test_no_gravity() -> None:
    w = World(timedelta(seconds=1))
    b = Body(1, Sphere(DVector3(0), 1), world=w)

    w.simulate(timedelta(seconds=10))
    assert b.transform == DMatrix4(1)
    assert b.linear_velocity == DVector3(0)


def test_world_gravity_inherit() -> None:
    w = World(timedelta(seconds=1))
    w.gravity = DVector3(0, 1, 0)
    b = Body(1, Sphere(DVector3(0), 1), world=w)

    w.simulate(timedelta(seconds=10))
    assert b.transform == DMatrix4(1).translate(DVector3(0, 55, 0))
    assert b.linear_velocity == DVector3(0, 10, 0)


def test_body_gravity() -> None:
    w = World(timedelta(seconds=1))
    b = Body(1, Sphere(DVector3(0), 1), world=w)
    b.gravity = DVector3(0, 1, 0)

    w.simulate(timedelta(seconds=10))
    assert b.transform == DMatrix4(1).translate(DVector3(0, 55, 0))
    assert b.linear_velocity == DVector3(0, 10, 0)


@pytest.mark.parametrize("body_type", [
    BodyType.KINEMATIC,
    BodyType.STATIC,
])
def test_non_dynamic_body_gravity(body_type: BodyType) -> None:
    w = World(timedelta(seconds=1))
    b = Body(1, Sphere(DVector3(0), 1), world=w, type=body_type)
    b.gravity = DVector3(0, 1, 0)

    w.simulate(timedelta(seconds=10))
    assert b.transform == DMatrix4(1)
    assert b.linear_velocity == DVector3(0)
