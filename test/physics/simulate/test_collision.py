
# gamut
from gamut.geometry import Composite3d, Mesh, Plane, Sphere
from gamut.math import Matrix4, UVector3, UVector3Array, Vector3, Vector3Array
from gamut.physics import Body, BodyType, World
# python
from datetime import timedelta
from math import isclose
# pytest
import pytest


def is_close(a, b):
    return isclose(a, b, abs_tol=1e-06)


@pytest.mark.parametrize("ball_type", [BodyType.DYNAMIC, BodyType.KINEMATIC])
@pytest.mark.parametrize("floor_type", list(BodyType))
def test_single_collision(ball_type: BodyType, floor_type: BodyType) -> None:
    w = World(timedelta(seconds=1))

    ball = Body(1, Sphere(Vector3(0), 1), world=w, type=ball_type)
    ball.transform = Matrix4(1).translate(Vector3(0, 1, 0))

    floor = Body(1, Plane(0, Vector3(0, 1, 0)), world=w, type=floor_type)

    world_simulation = w.simulate(timedelta(seconds=1))
    collisions = next(world_simulation)
    assert len(collisions) == 1
    collision = collisions[0]

    assert collision.when == timedelta(seconds=1)
    assert ball in (collision.body_a, collision.body_b)
    assert floor in (collision.body_a, collision.body_b)
    assert len(collision.contacts) == 1
    contact = collision.contacts[0]

    if collision.body_a is ball:
        assert contact.local_position_a == Vector3(0, -1, 0)
        assert contact.world_position_a == Vector3(0, 0, 0)
        assert contact.normal_a == Vector3(0, -1, 0)
        assert contact.local_position_b == Vector3(0, 0, 0)
        assert contact.world_position_b == Vector3(0, 0, 0)
        assert contact.normal_b == Vector3(0, 1, 0)
    else:
        assert contact.local_position_b == Vector3(0, -1, 0)
        assert contact.world_position_b == Vector3(0, 0, 0)
        assert contact.normal_b == Vector3(0, -1, 0)
        assert contact.local_position_a == Vector3(0, 0, 0)
        assert contact.world_position_a == Vector3(0, 0, 0)
        assert contact.normal_a == Vector3(0, 1, 0)

    with pytest.raises(StopIteration):
        next(world_simulation)


def test_lots_of_collisions() -> None:
    w = World(timedelta(seconds=1))

    for x in range(100):
        for z in range(100):
            ball = Body(
                1,
                Sphere(Vector3(0), .25),
                world=w,
                type=BodyType.KINEMATIC
            )
            ball.transform = Matrix4(1).translate(Vector3(x, .25, z))

    floor = Body(1, Plane(0, Vector3(0, 1, 0)), world=w, type=BodyType.STATIC)
    world_simulation = w.simulate(timedelta(seconds=1))
    collisions = next(world_simulation)
    assert len(collisions) == 10000


def test_no_collision_distance() -> None:
    w = World(timedelta(seconds=1))

    ball = Body(1, Sphere(Vector3(0), 1), world=w)
    ball.transform = Matrix4(1).translate(Vector3(0, 1.1, 0))

    floor = Body(1, Plane(0, Vector3(0, 1, 0)), world=w, type=BodyType.STATIC)

    world_simulation = w.simulate(timedelta(seconds=1))
    collisions = next(world_simulation)
    assert len(collisions) == 0

    with pytest.raises(StopIteration):
        next(world_simulation)


def test_no_collision_both_static() -> None:
    w = World(timedelta(seconds=1))

    ball = Body(1, Sphere(Vector3(0), 1), world=w, type=BodyType.STATIC)
    ball.transform = Matrix4(1).translate(Vector3(0, 1, 0))

    floor = Body(1, Plane(0, Vector3(0, 1, 0)), world=w, type=BodyType.STATIC)

    world_simulation = w.simulate(timedelta(seconds=1))
    collisions = next(world_simulation)
    assert len(collisions) == 0

    with pytest.raises(StopIteration):
        next(world_simulation)


@pytest.mark.parametrize("ball_group_shift", list(range(31)))
def test_no_collision_mask(ball_group_shift: int) -> None:
    ball_group = 1 << ball_group_shift

    w = World(timedelta(seconds=1))

    ball = Body(1, Sphere(Vector3(0), 1), world=w, groups=ball_group)
    ball.transform = Matrix4(1).translate(Vector3(0, 1, 0))

    floor = Body(1, Plane(0, Vector3(0, 1, 0)), world=w, mask=~ball_group)

    world_simulation = w.simulate(timedelta(seconds=1))
    collisions = next(world_simulation)
    assert len(collisions) == 0

    with pytest.raises(StopIteration):
        next(world_simulation)


def test_mesh_collision_normals() -> None:
    w = World(timedelta(seconds=1 / 120.0))
    w.gravity = Vector3(0, -9.8, 0)

    ball = Body(1, Sphere(Vector3(0), 1), world=w, type=BodyType.DYNAMIC)
    ball.transform = Matrix4(1).translate(Vector3(99, 1.2, 0))
    ball.linear_velocity = Vector3(-8, 0, 0)

    floor_shape = Composite3d(
        Mesh(
            Vector3Array(
                Vector3(100, 0, 100),
                Vector3(100, 0, -100),
                Vector3(-100, 0, -100)
            ),
            UVector3Array(UVector3(0, 1, 2)),
            normals=Vector3Array(
                Vector3(0, 1, 0),
                Vector3(0, 1, 0),
                Vector3(0, 1, 0)
            )
        ),
        Mesh(
            Vector3Array(
                Vector3(100, 0, 100),
                Vector3(-100, 0, 100),
                Vector3(-100, 0, -100)
            ),
            UVector3Array(UVector3(0, 1, 2)),
            normals=Vector3Array(
                Vector3(0, 1, 0),
                Vector3(0, 1, 0),
                Vector3(0, 1, 0)
            )
        ),
    )
    floor = Body(1, floor_shape, type=BodyType.STATIC, world=w)

    w.simulate(timedelta(seconds=1))
    for _ in range(150):
        for collisions in w.simulate(timedelta(seconds=.1)):
            assert len(collisions) >= 1
            for collision in collisions:
                for contact in collision.contacts:
                    assert is_close(contact.normal_a.x, 0)
                    assert is_close(contact.normal_a.y, -1)
                    assert is_close(contact.normal_a.z, 0)
                    assert is_close(contact.normal_b.x, 0)
                    assert is_close(contact.normal_b.y, 1)
                    assert is_close(contact.normal_b.z, 0)
            assert is_close(ball.linear_velocity.y, 0)
