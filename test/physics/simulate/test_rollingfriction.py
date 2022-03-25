
# gamut
from gamut.geometry import Composite3d, Mesh3d, Plane, Sphere
from gamut.math import Matrix4, UVector3, UVector3Array, Vector3, Vector3Array
from gamut.physics import Body, BodyType, World
# python
from datetime import timedelta
from math import isclose
# pytest
import pytest


def is_close(a, b):
    return isclose(a, b, abs_tol=1e-06)


@pytest.mark.parametrize("ball_rolling_friction, floor_friction", [
    [0, 0],
    [1, 0],
    [0, 1],
])
def test_no_rolling_friction(
    ball_rolling_friction: float,
    floor_friction: float
) -> None:
    w = World(timedelta(seconds=1 / 60.0))
    w.gravity = Vector3(0, -1, 0)

    ball = Body(1, Sphere(Vector3(0), 1), world=w, type=BodyType.DYNAMIC)
    ball.transform = Matrix4(1).translate(Vector3(0, 1, 0))
    ball.rolling_friction = ball_rolling_friction
    ball.angular_velocity = Vector3(1, 0, 0)

    floor = Body(1, Plane(0, Vector3(0, 1, 0)), world=w, type=BodyType.STATIC)
    floor.friction = floor_friction

    w.simulate(timedelta(seconds=5))
    assert isclose(ball.angular_velocity.x, 1)
    assert ball.angular_velocity.y == 0
    assert ball.angular_velocity.z == 0


def test_rolling_friction() -> None:
    w = None
    ball_1 = None
    ball_2 = None

    def reset_world():
        nonlocal ball_1
        nonlocal ball_2
        nonlocal w
        w = World(timedelta(seconds=1 / 60.0))
        w.gravity = Vector3(0, -1, 0)

        ball_1 = Body(1, Sphere(Vector3(0), 1), world=w, type=BodyType.DYNAMIC)
        ball_1.rolling_friction = .5
        ball_1.transform = Matrix4(1).translate(Vector3(5, 1.1, -5))
        ball_1.angular_velocity = Vector3(1, 0, 0)

        ball_2 = Body(1, Sphere(Vector3(0), 1), world=w, type=BodyType.DYNAMIC)
        ball_2.rolling_friction = .5
        ball_2.transform = Matrix4(1).translate(Vector3(-5, 1.1, 5))
        ball_2.angular_velocity = Vector3(1, 0, 0)

    floor_shape = Composite3d(
        Mesh3d(
            Vector3Array(
                Vector3(10, 0, 10),
                Vector3(10, 0, -10),
                Vector3(-10, 0, -10)
            ),
            UVector3Array(UVector3(0, 1, 2)),
        ),
        Mesh3d(
            Vector3Array(
                Vector3(10, 0, 10),
                Vector3(-10, 0, 10),
                Vector3(-10, 0, -10)
            ),
            UVector3Array(UVector3(0, 1, 2)),
        ),
    )
    floor = Body(1, floor_shape, type=BodyType.STATIC)
    floor.friction = .5

    reset_world()
    floor.world = w
    w.simulate(timedelta(seconds=1))
    assert is_close(ball_1.angular_velocity.x, 0.3853672063457937)
    assert is_close(ball_1.angular_velocity.y, 0)
    assert is_close(ball_1.angular_velocity.z, 0)

    assert is_close(ball_2.angular_velocity.x, 0.3853672063457937)
    assert is_close(ball_2.angular_velocity.y, 0)
    assert is_close(ball_2.angular_velocity.z, 0)

    reset_world()
    floor.world = w
    floor.friction = 0
    w.simulate(timedelta(seconds=1))

    assert is_close(ball_1.angular_velocity.x, 1)
    assert is_close(ball_1.angular_velocity.y, 0)
    assert is_close(ball_1.angular_velocity.z, 0)

    assert is_close(ball_2.angular_velocity.x, 1)
    assert is_close(ball_2.angular_velocity.y, 0)
    assert is_close(ball_2.angular_velocity.z, 0)

    reset_world()
    floor.world = w
    floor.friction = .5
    floor.shape = floor_shape
    w.simulate(timedelta(seconds=1))

    assert is_close(ball_1.angular_velocity.x, 0.3853672063457937)
    assert is_close(ball_1.angular_velocity.y, 0)
    assert is_close(ball_1.angular_velocity.z, 0)

    assert is_close(ball_2.angular_velocity.x, 0.3853672063457937)
    assert is_close(ball_2.angular_velocity.y, 0)
    assert is_close(ball_2.angular_velocity.z, 0)
