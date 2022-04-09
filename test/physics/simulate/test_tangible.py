
# gamut
from gamut.geometry import Composite3d, Mesh3d, Sphere
from gamut.math import (DMatrix4, DVector3, DVector3Array, UVector3,
                        UVector3Array)
from gamut.physics import Body, BodyType, World
# python
from datetime import timedelta
from math import isclose
# pytest
import pytest


def is_close(a, b):
    return isclose(a, b, abs_tol=1e-06)


def test_tangible() -> None:
    w = World(timedelta(seconds=1 / 120.0))
    w.gravity = DVector3(0, -9.8, 0)

    ball = Body(1, Sphere(DVector3(0), 1), world=w, type=BodyType.DYNAMIC)
    ball.transform = DMatrix4(1).translate(DVector3(0, 10, 0))

    floor_shape = Composite3d(
        Mesh3d(
            DVector3Array(
                DVector3(100, 0, 100),
                DVector3(100, 0, -100),
                DVector3(-100, 0, -100)
            ),
            UVector3Array(UVector3(0, 1, 2)),
        ),
        Mesh3d(
            DVector3Array(
                DVector3(100, 0, 100),
                DVector3(-100, 0, 100),
                DVector3(-100, 0, -100)
            ),
            UVector3Array(UVector3(0, 1, 2)),
        ),
    )
    floor = Body(1, floor_shape, type=BodyType.STATIC, world=w)

    w.simulate(timedelta(seconds=10))
    assert is_close(ball.transform[3].y, 1)


@pytest.mark.parametrize("ball_tangible, floor_tangible", [
    (True, False),
    (False, True),
    (False, False),
])
def test_intangible(ball_tangible: bool, floor_tangible: bool) -> None:
    w = World(timedelta(seconds=1 / 120.0))
    w.gravity = DVector3(0, -9.8, 0)

    ball = Body(1, Sphere(DVector3(0), 1), world=w, type=BodyType.DYNAMIC)
    ball.transform = DMatrix4(1).translate(DVector3(0, 10, 0))
    ball.tangible = ball_tangible

    floor_shape = Composite3d(
        Mesh3d(
            DVector3Array(
                DVector3(100, 0, 100),
                DVector3(100, 0, -100),
                DVector3(-100, 0, -100)
            ),
            UVector3Array(UVector3(0, 1, 2)),
        ),
        Mesh3d(
            DVector3Array(
                DVector3(100, 0, 100),
                DVector3(-100, 0, 100),
                DVector3(-100, 0, -100)
            ),
            UVector3Array(UVector3(0, 1, 2)),
        ),
    )
    floor = Body(1, floor_shape, type=BodyType.STATIC, world=w)
    floor.tangible = floor_tangible

    w.simulate(timedelta(seconds=10))
    assert ball.transform[3].y < 0
