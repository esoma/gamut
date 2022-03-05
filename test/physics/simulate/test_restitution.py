
# gamut
from gamut.geometry import Plane, Sphere
from gamut.physics import Body, BodyType, World
# python
from datetime import timedelta
# pyglm
from glm import dmat4, dvec3, translate
# pytest
import pytest


@pytest.mark.parametrize("ball_restitution, floor_restitution", [
    [0, 0],
    [1, 0],
    [0, 1],
])
def test_no_restitution(
    ball_restitution: float,
    floor_restitution: float
) -> None:
    w = World(timedelta(seconds=1 / 60.0))
    w.gravity = dvec3(0, -1, 0)

    ball = Body(1, Sphere(dvec3(0), 1), world=w, type=BodyType.DYNAMIC)
    ball.transform = translate(dmat4(1), dvec3(0, 10, 0))
    ball.restitution = ball_restitution

    floor = Body(1, Plane(0, dvec3(0, 1, 0)), world=w, type=BodyType.STATIC)
    floor.restitution = floor_restitution

    w.simulate(timedelta(seconds=5))
    assert ball.linear_velocity == dvec3(0)


def test_bounce() -> None:
    w = World(timedelta(seconds=1 / 60.0))
    w.gravity = dvec3(0, -1, 0)

    ball = Body(1, Sphere(dvec3(0), 1), world=w, type=BodyType.DYNAMIC)
    ball.transform = translate(dmat4(1), dvec3(0, 10, 0))
    ball.restitution = 1

    floor = Body(1, Plane(0, dvec3(0, 1, 0)), world=w, type=BodyType.STATIC)
    floor.restitution = 1

    w.simulate(timedelta(seconds=5))
    assert ball.linear_velocity.x == 0
    assert ball.linear_velocity.y > 0
    assert ball.linear_velocity.z == 0
