
# gamut
from gamut.geometry import (Capsule, Composite3d, Cone, ConvexHull, Cylinder,
                            Mesh, Plane, RectangularCuboid, Sphere)
from gamut.physics import Body, BodyType, World
# python
from datetime import timedelta
from typing import Any
# pyglm
from glm import dmat4, dvec3, ivec3, mat4, vec3
# pytest
import pytest


@pytest.fixture
def world() -> World:
    return World(timedelta(seconds=1))


@pytest.mark.parametrize("mass", [None, 'abc', []])
def test_invalid_init_mass_type(mass: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Body(mass, Sphere(vec3(0), 1))
    assert str(excinfo.value) == 'mass must be float'


@pytest.mark.parametrize("mass", [-1, 0])
def test_invalid_init_mass_value(mass: Any) -> None:
    with pytest.raises(ValueError) as excinfo:
        Body(mass, Sphere(vec3(0), 1))
    assert str(excinfo.value) == 'mass must be > 0'


@pytest.mark.parametrize("shape", [None, 1, 'abc', object()])
def test_invalid_init_shape(shape: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Body(1, shape)
    assert str(excinfo.value) == f'invalid shape: {shape}'


@pytest.mark.parametrize("groups", [None, 'abc', []])
def test_invalid_init_groups_type(groups: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Body(1, Sphere(vec3(0), 1), groups=groups)
    assert str(excinfo.value) == 'groups must be int'


@pytest.mark.parametrize("groups", [
    -2147483649,
    2147483648
])
def test_invalid_init_groups_value(groups: Any) -> None:
    with pytest.raises(ValueError) as excinfo:
        Body(1, Sphere(vec3(0), 1), groups=groups)
    assert str(excinfo.value) == 'groups must be 32 bit signed int'


@pytest.mark.parametrize("mask", [None, 'abc', []])
def test_invalid_init_mask_type(mask: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Body(1, Sphere(vec3(0), 1), mask=mask)
    assert str(excinfo.value) == 'mask must be int'


@pytest.mark.parametrize("mask", [
    -2147483649,
    2147483648
])
def test_invalid_init_mask_value(mask: Any) -> None:
    with pytest.raises(ValueError) as excinfo:
        Body(1, Sphere(vec3(0), 1), mask=mask)
    assert str(excinfo.value) == 'mask must be 32 bit signed int'


@pytest.mark.parametrize("type", [None, 0, 'dynamic'])
def test_invalid_init_type(type: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Body(1, Sphere(vec3(0), 1), type=type)
    assert str(excinfo.value) == f'type must be {BodyType}'


@pytest.mark.parametrize("world", [0, 'hello world', object()])
def test_invalid_init_world(world: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Body(1, Sphere(vec3(0), 1), world=world)
    assert str(excinfo.value) == f'world must be None or {World}'


@pytest.mark.parametrize("mass", [1, 9.8])
@pytest.mark.parametrize("shape", [
    Sphere(vec3(0), 1),
    Plane(1, vec3(0, 1, 0))
])
def test_repr(mass: float, shape: Any) -> None:
    b = Body(mass, shape)
    assert repr(b) == (
        f'<gamut.physics.Body mass={float(mass)} shape={shape!r}>'
    )


def test_defaults() -> None:
    b = Body(1, Sphere(vec3(0), 1))
    assert b.angular_damping == 0
    assert b.angular_sleep_threshold == 1
    assert b.angular_velocity == dvec3(0)
    assert b.can_sleep
    assert b.is_enabled
    assert not b.is_sleeping
    assert b.linear_damping == 0
    assert b.linear_sleep_threshold == .8
    assert b.linear_velocity == dvec3(0)
    assert b.friction == 0
    assert b.gravity is None
    assert b.groups == Body.ALL_GROUPS
    assert b.mask == Body.ALL_GROUPS
    assert b.restitution == 0
    assert b.rolling_friction == 0
    assert b.spinning_friction == 0
    assert b.transform == dmat4(1)
    assert b.type == BodyType.DYNAMIC
    assert b.world is None


@pytest.mark.parametrize("angular_damping", [None, 'abc', []])
def test_invalid_angular_damping_type(angular_damping: Any) -> None:
    b = Body(1, Sphere(vec3(0), 1))
    with pytest.raises(TypeError) as excinfo:
        b.angular_damping = angular_damping
    assert str(excinfo.value) == f'angular damping must be float'


@pytest.mark.parametrize("angular_damping", [-0.1, 1.1])
def test_invalid_angular_damping_value(angular_damping: Any) -> None:
    b = Body(1, Sphere(vec3(0), 1))
    with pytest.raises(ValueError) as excinfo:
        b.angular_damping = angular_damping
    assert str(excinfo.value) == f'angular damping must be between 0 and 1'


@pytest.mark.parametrize("angular_damping", [0, 1, '.5'])
def test_angular_damping(angular_damping: Any) -> None:
    b = Body(1, Sphere(vec3(0), 1))
    b.angular_damping = angular_damping
    assert b.angular_damping == float(angular_damping)


@pytest.mark.parametrize("angular_sleep_threshold", [None, 'abc', []])
def test_invalid_angular_sleep_threshold_type(
    angular_sleep_threshold: Any
) -> None:
    b = Body(1, Sphere(vec3(0), 1))
    with pytest.raises(TypeError) as excinfo:
        b.angular_sleep_threshold = angular_sleep_threshold
    assert str(excinfo.value) == f'angular sleep threshold must be float'


@pytest.mark.parametrize("angular_sleep_threshold", [-100, -.1])
def test_invalid_angular_sleep_threshold_value(
    angular_sleep_threshold: Any
) -> None:
    b = Body(1, Sphere(vec3(0), 1))
    with pytest.raises(ValueError) as excinfo:
        b.angular_sleep_threshold = angular_sleep_threshold
    assert str(excinfo.value) == f'angular sleep threshold must be 0 or more'


@pytest.mark.parametrize("angular_sleep_threshold", [0, 1, '.5', 100])
def test_angular_sleep_threshold(angular_sleep_threshold: Any) -> None:
    b = Body(1, Sphere(vec3(0), 1))
    b.angular_sleep_threshold = angular_sleep_threshold
    assert b.angular_sleep_threshold == float(angular_sleep_threshold)


@pytest.mark.parametrize("angular_velocity", [
    None,
    'abc',
    (1, 2),
    (1, 2, 3, 4)
])
def test_invalid_angular_velocity_type(angular_velocity: Any) -> None:
    b = Body(1, Sphere(vec3(0), 1))
    with pytest.raises(TypeError) as excinfo:
        b.angular_velocity = angular_velocity
    assert str(excinfo.value) == f'angular velocity must be dvec3'


@pytest.mark.parametrize("angular_velocity", [
    (1, 2, 3),
    vec3(1, 2, 3),
    dvec3(1, 2, 3),
])
def test_angular_velocity(angular_velocity: Any) -> None:
    b = Body(1, Sphere(vec3(0), 1))
    b.angular_velocity = angular_velocity
    assert b.angular_velocity == dvec3(angular_velocity)


@pytest.mark.parametrize("can_sleep", [
    False,
    True,
    None,
    0,
    1,
    '123',
    '',
])
def test_can_sleep(can_sleep: Any) -> None:
    b = Body(1, Sphere(vec3(0), 1))
    b.can_sleep = can_sleep
    assert b.can_sleep == bool(can_sleep)


@pytest.mark.parametrize("is_enabled", [
    False,
    True,
    None,
    0,
    1,
    '123',
    '',
])
def test_is_enabled(is_enabled: Any) -> None:
    b = Body(1, Sphere(vec3(0), 1))
    b.is_enabled = is_enabled
    assert b.is_enabled == bool(is_enabled)


def test_is_sleeping() -> None:
    b = Body(1, Sphere(vec3(0), 1))
    with pytest.raises(AttributeError) as excinfo:
        b.is_sleeping = False


@pytest.mark.parametrize("linear_damping", [None, 'abc', []])
def test_invalid_linear_damping_type(linear_damping: Any) -> None:
    b = Body(1, Sphere(vec3(0), 1))
    with pytest.raises(TypeError) as excinfo:
        b.linear_damping = linear_damping
    assert str(excinfo.value) == f'linear damping must be float'


@pytest.mark.parametrize("linear_damping", [-0.1, 1.1])
def test_invalid_linear_damping_value(linear_damping: Any) -> None:
    b = Body(1, Sphere(vec3(0), 1))
    with pytest.raises(ValueError) as excinfo:
        b.linear_damping = linear_damping
    assert str(excinfo.value) == f'linear damping must be between 0 and 1'


@pytest.mark.parametrize("linear_damping", [0, 1, '.5'])
def test_linear_damping(linear_damping: Any) -> None:
    b = Body(1, Sphere(vec3(0), 1))
    b.linear_damping = linear_damping
    assert b.linear_damping == float(linear_damping)


@pytest.mark.parametrize("linear_sleep_threshold", [None, 'abc', []])
def test_invalid_linear_sleep_threshold_type(
    linear_sleep_threshold: Any
) -> None:
    b = Body(1, Sphere(vec3(0), 1))
    with pytest.raises(TypeError) as excinfo:
        b.linear_sleep_threshold = linear_sleep_threshold
    assert str(excinfo.value) == f'linear sleep threshold must be float'


@pytest.mark.parametrize("linear_sleep_threshold", [-100, -.1])
def test_invalid_linear_sleep_threshold_value(
    linear_sleep_threshold: Any
) -> None:
    b = Body(1, Sphere(vec3(0), 1))
    with pytest.raises(ValueError) as excinfo:
        b.linear_sleep_threshold = linear_sleep_threshold
    assert str(excinfo.value) == f'linear sleep threshold must be 0 or more'


@pytest.mark.parametrize("linear_sleep_threshold", [0, 1, '.5', 100])
def test_linear_sleep_threshold(linear_sleep_threshold: Any) -> None:
    b = Body(1, Sphere(vec3(0), 1))
    b.linear_sleep_threshold = linear_sleep_threshold
    assert b.linear_sleep_threshold == float(linear_sleep_threshold)


@pytest.mark.parametrize("linear_velocity", [
    None,
    'abc',
    (1, 2),
    (1, 2, 3, 4)
])
def test_invalid_linear_velocity_type(linear_velocity: Any) -> None:
    b = Body(1, Sphere(vec3(0), 1))
    with pytest.raises(TypeError) as excinfo:
        b.linear_velocity = linear_velocity
    assert str(excinfo.value) == f'linear velocity must be dvec3'


@pytest.mark.parametrize("linear_velocity", [
    (1, 2, 3),
    vec3(1, 2, 3),
    dvec3(1, 2, 3),
])
def test_linear_velocity(linear_velocity: Any) -> None:
    b = Body(1, Sphere(vec3(0), 1))
    b.linear_velocity = linear_velocity
    assert b.linear_velocity == dvec3(linear_velocity)


@pytest.mark.parametrize("friction", [None, 'abc', []])
def test_invalid_friction_type(friction: Any) -> None:
    b = Body(1, Sphere(vec3(0), 1))
    with pytest.raises(TypeError) as excinfo:
        b.friction = friction
    assert str(excinfo.value) == f'friction must be float'


@pytest.mark.parametrize("friction", [-100, 0, 1, '.5', 100])
def test_friction(friction: Any) -> None:
    b = Body(1, Sphere(vec3(0), 1))
    b.friction = friction
    assert b.friction == float(friction)


@pytest.mark.parametrize("gravity", [
    'abc',
    (1, 2),
    (1, 2, 3, 4)
])
def test_invalid_linear_velocity_type(gravity: Any) -> None:
    b = Body(1, Sphere(vec3(0), 1))
    with pytest.raises(TypeError) as excinfo:
        b.gravity = gravity
    assert str(excinfo.value) == f'gravity must be None or dvec3'


@pytest.mark.parametrize("gravity", [
    (1, 2, 3),
    vec3(1, 2, 3),
    dvec3(1, 2, 3),
])
def test_gravity_explicit(gravity: Any) -> None:
    b = Body(1, Sphere(vec3(0), 1))
    b.gravity = gravity
    assert b.gravity == dvec3(gravity)
    assert isinstance(b.gravity, dvec3)


def test_gravity_inheritance(world: World) -> None:
    b = Body(1, Sphere(vec3(0), 1))

    b.gravity = dvec3(0)
    b.gravity = None
    assert b.gravity is None

    b.world = world
    assert b.gravity is None

    b.gravity = dvec3(0)
    b.gravity = None
    assert b.gravity is None


@pytest.mark.parametrize("groups", [None, 'abc', []])
def test_invalid_groups_type(groups: Any) -> None:
    b = Body(1, Sphere(vec3(0), 1))
    with pytest.raises(TypeError) as excinfo:
        b.groups = groups
    assert str(excinfo.value) == 'groups must be int'


@pytest.mark.parametrize("groups", [
    -2147483649,
    2147483648
])
def test_invalid_groups_value(groups: Any) -> None:
    b = Body(1, Sphere(vec3(0), 1))
    with pytest.raises(ValueError) as excinfo:
        b.groups = groups
    assert str(excinfo.value) == 'groups must be 32 bit signed int'


@pytest.mark.parametrize("groups", [
    -2147483648,
    '-10',
    -1,
    0,
    1,
    '10',
    2147483647
])
def test_groups(groups: Any) -> None:
    b = Body(1, Sphere(vec3(0), 1))
    b.groups = groups
    assert b.groups == int(groups)


@pytest.mark.parametrize("mask", [None, 'abc', []])
def test_invalid_mask_type(mask: Any) -> None:
    b = Body(1, Sphere(vec3(0), 1))
    with pytest.raises(TypeError) as excinfo:
        b.mask = mask
    assert str(excinfo.value) == 'mask must be int'


@pytest.mark.parametrize("mask", [
    -2147483649,
    2147483648
])
def test_invalid_mask_value(mask: Any) -> None:
    b = Body(1, Sphere(vec3(0), 1))
    with pytest.raises(ValueError) as excinfo:
        b.mask = mask
    assert str(excinfo.value) == 'mask must be 32 bit signed int'


@pytest.mark.parametrize("mask", [
    -2147483648,
    '-10',
    -1,
    0,
    1,
    '10',
    2147483647
])
def test_mask(mask: Any) -> None:
    b = Body(1, Sphere(vec3(0), 1))
    b.mask = mask
    assert b.mask == int(mask)


@pytest.mark.parametrize("mass", [None, 'abc', []])
def test_invalid_mass_type(mass: Any) -> None:
    b = Body(1, Sphere(vec3(0), 1))
    with pytest.raises(TypeError) as excinfo:
        b.mass = mass
    assert str(excinfo.value) == 'mass must be float'


@pytest.mark.parametrize("mass", [-1, 0])
def test_invalid_mass_value(mass: Any) -> None:
    b = Body(1, Sphere(vec3(0), 1))
    with pytest.raises(ValueError) as excinfo:
        b.mass = mass
    assert str(excinfo.value) == 'mass must be > 0'


@pytest.mark.parametrize("mass", [
    0.1,
    1,
    100,
    123456,
    '9999',
])
def test_mass(mass: Any) -> None:
    b = Body(1, Sphere(vec3(0), 1))
    b.mass = mass
    assert b.mass == float(mass)


@pytest.mark.parametrize("restitution", [None, 'abc', []])
def test_invalid_restitution_type(restitution: Any) -> None:
    b = Body(1, Sphere(vec3(0), 1))
    with pytest.raises(TypeError) as excinfo:
        b.restitution = restitution
    assert str(excinfo.value) == f'restitution must be float'


@pytest.mark.parametrize("restitution", [-1, 0, 1, '.5', 2])
def test_restitution(restitution: Any) -> None:
    b = Body(1, Sphere(vec3(0), 1))
    b.restitution = restitution
    assert b.restitution == float(restitution)


@pytest.mark.parametrize("rolling_friction", [None, 'abc', []])
def test_invalid_rolling_friction_type(rolling_friction: Any) -> None:
    b = Body(1, Sphere(vec3(0), 1))
    with pytest.raises(TypeError) as excinfo:
        b.rolling_friction = rolling_friction
    assert str(excinfo.value) == f'rolling friction must be float'


@pytest.mark.parametrize("rolling_friction", [-1, 0, 1, '.5', 2])
def test_rolling_friction(rolling_friction: Any) -> None:
    b = Body(1, Sphere(vec3(0), 1))
    b.rolling_friction = rolling_friction
    assert b.rolling_friction == float(rolling_friction)


@pytest.mark.parametrize("shape", [None, 1, 'abc', object()])
def test_invalid_shape(shape: Any) -> None:
    b = Body(1, Sphere(vec3(0), 1))
    with pytest.raises(TypeError) as excinfo:
        b.shape = shape
    assert str(excinfo.value) == f'invalid shape: {shape}'


@pytest.mark.parametrize("shape", [
    Sphere(vec3(0), 1),
    Plane(1, vec3(0, 1, 0)),
    Cylinder(vec3(0), 1, 1),
    Cone(vec3(0), 1, 1),
    Capsule(vec3(0), 1, 1),
    RectangularCuboid(vec3(0), vec3(1)),
    ConvexHull(vec3(0), vec3(-1), vec3(1)),
    Mesh([vec3(0), vec3(1), vec3(2)], [ivec3(0), ivec3(1), ivec3(2)]),
    Composite3d(),
    Composite3d(
        Sphere(vec3(0), 1),
        Plane(1, vec3(0, 1, 0)),
        Cylinder(vec3(0), 1, 1),
        Cone(vec3(0), 1, 1),
        Capsule(vec3(0), 1, 1),
        RectangularCuboid(vec3(0), vec3(1)),
        ConvexHull(vec3(0), vec3(-1), vec3(1)),
        Mesh([vec3(0), vec3(1), vec3(2)], [ivec3(0), ivec3(1), ivec3(2)]),
    )
])
def test_shape(shape: Any) -> None:
    b = Body(1, Sphere(vec3(0), 1))
    b.shape = shape
    assert b.shape is shape


@pytest.mark.parametrize("spinning_friction", [None, 'abc', []])
def test_invalid_spinning_friction_type(spinning_friction: Any) -> None:
    b = Body(1, Sphere(vec3(0), 1))
    with pytest.raises(TypeError) as excinfo:
        b.spinning_friction = spinning_friction
    assert str(excinfo.value) == f'spinning friction must be float'


@pytest.mark.parametrize("spinning_friction", [-1, 0, 1, '.5', 2])
def test_spinning_friction(spinning_friction: Any) -> None:
    b = Body(1, Sphere(vec3(0), 1))
    b.spinning_friction = spinning_friction
    assert b.spinning_friction == float(spinning_friction)


@pytest.mark.parametrize("transform", [
    None,
    'abc',
    [],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
])
def test_invalid_transform_type(transform: Any) -> None:
    b = Body(1, Sphere(vec3(0), 1))
    with pytest.raises(TypeError) as excinfo:
        b.transform = transform
    assert str(excinfo.value) == f'transform must be dmat4'


@pytest.mark.parametrize("transform", [
    mat4(1),
    dmat4(1),
    (
        (1, 2, 3, 0),
        (5, 6, 7, 0),
        (9, 10, 11, 0),
        (13, 14, 15, 1),
    ),
])
def test_transform(transform: Any) -> None:
    b = Body(1, Sphere(vec3(0), 1))
    b.transform = transform
    assert b.transform == dmat4(transform)
    assert isinstance(b.transform, dmat4)


@pytest.mark.parametrize("type", [None, 'abc', []])
def test_invalid_type(type: Any) -> None:
    b = Body(1, Sphere(vec3(0), 1))
    with pytest.raises(TypeError) as excinfo:
        b.type = type
    assert str(excinfo.value) == f'type must be {BodyType}'


@pytest.mark.parametrize("type", list(BodyType))
def test_type(type: Any) -> None:
    b = Body(1, Sphere(vec3(0), 1))
    b.type = type
    assert b.type == type


@pytest.mark.parametrize("world", [0, 'hello world', object()])
def test_invalid_world(world: Any) -> None:
    b = Body(1, Sphere(vec3(0), 1))
    with pytest.raises(TypeError) as excinfo:
        b.world = world
    assert str(excinfo.value) == f'world must be None or {World}'


def test_world() -> None:
    w1 = World(timedelta(seconds=1))
    w2 = World(timedelta(seconds=1))
    b = Body(1, Sphere(vec3(0), 1))

    b.world = w1
    assert b.world is w1

    b.world = w2
    assert b.world is w2

    b.world = None
    assert b.world is None


def test_world_weak() -> None:
    w1 = World(timedelta(seconds=1))
    b = Body(1, Sphere(vec3(0), 1))

    b.world = w1
    assert b.world is w1

    del w1
    assert b.world is None
