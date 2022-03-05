
# gamut
from gamut.geometry import Plane, Sphere
from gamut.physics import Body, BodyType, World
# python
from datetime import timedelta
# pyglm
from glm import dmat4, dvec3, translate
# pytest
import pytest


@pytest.mark.parametrize("ball_type", [BodyType.DYNAMIC, BodyType.KINEMATIC])
@pytest.mark.parametrize("floor_type", list(BodyType))
def test_single_collision(ball_type: BodyType, floor_type: BodyType) -> None:
    w = World(timedelta(seconds=1))

    ball = Body(1, Sphere(dvec3(0), 1), world=w, type=ball_type)
    ball.transform = translate(dmat4(1), dvec3(0, 1, 0))

    floor = Body(1, Plane(0, dvec3(0, 1, 0)), world=w, type=floor_type)

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
        assert contact.local_position_a == dvec3(0, -1, 0)
        assert contact.world_position_a == dvec3(0, 0, 0)
        assert contact.normal_a == dvec3(0, -1, 0)
        assert contact.local_position_b == dvec3(0, 0, 0)
        assert contact.world_position_b == dvec3(0, 0, 0)
        assert contact.normal_b == dvec3(0, 1, 0)
    else:
        assert contact.local_position_b == dvec3(0, -1, 0)
        assert contact.world_position_b == dvec3(0, 0, 0)
        assert contact.normal_b == dvec3(0, -1, 0)
        assert contact.local_position_a == dvec3(0, 0, 0)
        assert contact.world_position_a == dvec3(0, 0, 0)
        assert contact.normal_a == dvec3(0, 1, 0)

    with pytest.raises(StopIteration):
        next(world_simulation)


def test_lots_of_collisions() -> None:
    w = World(timedelta(seconds=1))

    for x in range(100):
        for z in range(100):
            ball = Body(
                1,
                Sphere(dvec3(0), .25),
                world=w,
                type=BodyType.KINEMATIC
            )
            ball.transform = translate(dmat4(1), dvec3(x, .25, z))

    floor = Body(1, Plane(0, dvec3(0, 1, 0)), world=w, type=BodyType.STATIC)
    world_simulation = w.simulate(timedelta(seconds=1))
    collisions = next(world_simulation)
    assert len(collisions) == 10000


def test_no_collision_distance() -> None:
    w = World(timedelta(seconds=1))

    ball = Body(1, Sphere(dvec3(0), 1), world=w)
    ball.transform = translate(dmat4(1), dvec3(0, 1.1, 0))

    floor = Body(1, Plane(0, dvec3(0, 1, 0)), world=w, type=BodyType.STATIC)

    world_simulation = w.simulate(timedelta(seconds=1))
    collisions = next(world_simulation)
    assert len(collisions) == 0

    with pytest.raises(StopIteration):
        next(world_simulation)


def test_no_collision_both_static() -> None:
    w = World(timedelta(seconds=1))

    ball = Body(1, Sphere(dvec3(0), 1), world=w, type=BodyType.STATIC)
    ball.transform = translate(dmat4(1), dvec3(0, 1, 0))

    floor = Body(1, Plane(0, dvec3(0, 1, 0)), world=w, type=BodyType.STATIC)

    world_simulation = w.simulate(timedelta(seconds=1))
    collisions = next(world_simulation)
    assert len(collisions) == 0

    with pytest.raises(StopIteration):
        next(world_simulation)


@pytest.mark.parametrize("ball_group_shift", list(range(31)))
def test_no_collision_mask(ball_group_shift: int) -> None:
    ball_group = 1 << ball_group_shift

    w = World(timedelta(seconds=1))

    ball = Body(1, Sphere(dvec3(0), 1), world=w, groups=ball_group)
    ball.transform = translate(dmat4(1), dvec3(0, 1, 0))

    floor = Body(1, Plane(0, dvec3(0, 1, 0)), world=w, mask=~ball_group)

    world_simulation = w.simulate(timedelta(seconds=1))
    collisions = next(world_simulation)
    assert len(collisions) == 0

    with pytest.raises(StopIteration):
        next(world_simulation)
