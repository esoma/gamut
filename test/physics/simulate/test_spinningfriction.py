
# gamut
from gamut.geometry import Plane, Sphere
from gamut.math import Matrix4, Vector3
from gamut.physics import Body, BodyType, World
# python
from datetime import timedelta
from math import isclose
# pytest
import pytest


@pytest.mark.parametrize("ball_spinning_friction, floor_friction", [
    [0, 0],
    [1, 0],
    [0, 1],
])
def test_no_spinning_friction(
    ball_spinning_friction: float,
    floor_friction: float
) -> None:
    w = World(timedelta(seconds=1 / 60.0))
    w.gravity = Vector3(0, -1, 0)

    ball = Body(1, Sphere(Vector3(0), 1), world=w, type=BodyType.DYNAMIC)
    ball.transform = Matrix4(1).translate(Vector3(0, 1, 0))
    ball.spinning_friction = ball_spinning_friction
    ball.angular_velocity = Vector3(0, 1, 0)

    floor = Body(1, Plane(0, Vector3(0, 1, 0)), world=w, type=BodyType.STATIC)
    floor.friction = floor_friction

    w.simulate(timedelta(seconds=5))
    assert ball.angular_velocity.x == 0
    assert isclose(ball.angular_velocity.y, 1)
    assert ball.angular_velocity.z == 0


def test_spinning_friction() -> None:
    w = World(timedelta(seconds=1 / 60.0))
    w.gravity = Vector3(0, -1, 0)

    ball = Body(1, Sphere(Vector3(0), 1), world=w, type=BodyType.DYNAMIC)
    ball.transform = Matrix4(1).translate(Vector3(0, 1.1, 0))
    ball.spinning_friction = .5
    ball.angular_velocity = Vector3(0, 1, 0)

    floor = Body(1, Plane(0, Vector3(0, 1, 0)), world=w, type=BodyType.STATIC)
    floor.friction = .5

    w.simulate(timedelta(seconds=1))
    assert ball.angular_velocity.x == 0
    assert ball.angular_velocity.y < 1
    assert ball.angular_velocity.z == 0
