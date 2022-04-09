
# gamut
from gamut.geometry import Composite3d, Mesh3d, Plane, Sphere
from gamut.math import (DMatrix4, DVector3, DVector3Array, UVector3,
                        UVector3Array)
from gamut.physics import Body, BodyType, World
# python
from datetime import timedelta
from math import isclose
# pytest
import pytest


def is_close(a, b):
    return isclose(a, b, abs_tol=1e-05)


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
    w.gravity = DVector3(0, -1, 0)

    ball = Body(1, Sphere(DVector3(0), 1), world=w, type=BodyType.DYNAMIC)
    ball.transform = DMatrix4(1).translate(DVector3(0, 10, 0))
    ball.restitution = ball_restitution

    floor = Body(1, Plane(0, DVector3(0, 1, 0)), world=w, type=BodyType.STATIC)
    floor.restitution = floor_restitution

    w.simulate(timedelta(seconds=5))
    assert ball.linear_velocity == DVector3(0)


def test_bounce() -> None:
    w = None
    ball_1 = None
    ball_2 = None

    def reset_world():
        nonlocal ball_1
        nonlocal ball_2
        nonlocal w
        w = World(timedelta(seconds=1 / 60.0))
        w.gravity = DVector3(0, -1, 0)

        ball_1 = Body(
            1,
            Sphere(DVector3(0), 1), world=w, type=BodyType.DYNAMIC
        )
        ball_1.restitution = 1
        ball_1.transform = DMatrix4(1).translate(DVector3(5, 10, -5))

        ball_2 = Body(
            1,
            Sphere(DVector3(0), 1), world=w, type=BodyType.DYNAMIC
        )
        ball_2.restitution = 1
        ball_2.transform = DMatrix4(1).translate(DVector3(-5, 10, 5))

    floor_shape = Composite3d(
        Mesh3d(
            DVector3Array(
                DVector3(10, 0, 10),
                DVector3(10, 0, -10),
                DVector3(-10, 0, -10)
            ),
            UVector3Array(UVector3(0, 1, 2)),
        ),
        Mesh3d(
            DVector3Array(
                DVector3(10, 0, 10),
                DVector3(-10, 0, 10),
                DVector3(-10, 0, -10)
            ),
            UVector3Array(UVector3(0, 1, 2)),
        ),
    )
    floor = Body(1, floor_shape, type=BodyType.STATIC)
    floor.restitution = 1

    reset_world()
    floor.world = w
    w.simulate(timedelta(seconds=5))
    assert is_close(ball_1.linear_velocity.x, 0)
    assert is_close(ball_1.linear_velocity.y, 3.533403999999998)
    assert is_close(ball_1.linear_velocity.z, 0)

    assert is_close(ball_2.linear_velocity.x, 0)
    assert is_close(ball_2.linear_velocity.y, 3.533403999999998)
    assert is_close(ball_2.linear_velocity.z, 0)

    reset_world()
    floor.world = w
    floor.restitution = 0
    w.simulate(timedelta(seconds=8))

    assert is_close(ball_1.linear_velocity.x, 0)
    assert is_close(ball_1.linear_velocity.y, 0)
    assert is_close(ball_1.linear_velocity.z, 0)

    assert is_close(ball_2.linear_velocity.x, 0)
    assert is_close(ball_2.linear_velocity.y, 0)
    assert is_close(ball_2.linear_velocity.z, 0)

    reset_world()
    floor.world = w
    floor.restitution = 1
    floor.shape = floor_shape
    w.simulate(timedelta(seconds=5))

    assert is_close(ball_1.linear_velocity.x, 0)
    assert is_close(ball_1.linear_velocity.y, 3.533403999999998)
    assert is_close(ball_1.linear_velocity.z, 0)

    assert is_close(ball_2.linear_velocity.x, 0)
    assert is_close(ball_2.linear_velocity.y, 3.533403999999998)
    assert is_close(ball_2.linear_velocity.z, 0)
