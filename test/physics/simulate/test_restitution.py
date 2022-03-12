
# gamut
from gamut.geometry import Plane, Sphere
from gamut.math import Matrix4, Vector3
from gamut.physics import Body, BodyType, World
# python
from datetime import timedelta
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
    w.gravity = Vector3(0, -1, 0)

    ball = Body(1, Sphere(Vector3(0), 1), world=w, type=BodyType.DYNAMIC)
    ball.transform = Matrix4(1).translate(Vector3(0, 10, 0))
    ball.restitution = ball_restitution

    floor = Body(1, Plane(0, Vector3(0, 1, 0)), world=w, type=BodyType.STATIC)
    floor.restitution = floor_restitution

    w.simulate(timedelta(seconds=5))
    assert ball.linear_velocity == Vector3(0)


def test_bounce() -> None:
    w = World(timedelta(seconds=1 / 60.0))
    w.gravity = Vector3(0, -1, 0)

    ball = Body(1, Sphere(Vector3(0), 1), world=w, type=BodyType.DYNAMIC)
    ball.transform = Matrix4(1).translate(Vector3(0, 10, 0))
    ball.restitution = 1

    floor = Body(1, Plane(0, Vector3(0, 1, 0)), world=w, type=BodyType.STATIC)
    floor.restitution = 1

    w.simulate(timedelta(seconds=5))
    assert ball.linear_velocity.x == 0
    assert ball.linear_velocity.y > 0
    assert ball.linear_velocity.z == 0
