
from __future__ import annotations

__all__ = ['Body', 'BodyType']

# gamut
from ._groups import ALL_GROUPS as G_ALL_GROUPS
from ._groups import verify_groups, verify_mask
from ._world import add_body_to_world, remove_body_from_world, World
# gamut
from gamut._bullet import Body as BaseBody
from gamut._bullet import Shape
from gamut.geometry import (Capsule, Composite3d, Cone, ConvexHull, Cylinder,
                            Mesh3d, Plane, RectangularCuboid, Sphere)
from gamut.math import BVector3, DMatrix4, DVector3
# python
from enum import auto, Enum
from typing import Final, Union
from weakref import ref

BodyShape = Union[
    Capsule,
    Composite3d,
    Cone,
    ConvexHull,
    Cylinder,
    Plane,
    Mesh3d,
    RectangularCuboid,
    Sphere
]


class BodyType(Enum):
    DYNAMIC = auto()
    STATIC = auto()
    KINEMATIC = auto()


class Body:

    ALL_GROUPS: Final = G_ALL_GROUPS

    def __init__(
        self,
        mass: float,
        shape: BodyShape,
        *,
        groups: int = ALL_GROUPS,
        mask: int = ALL_GROUPS,
        type: BodyType = BodyType.DYNAMIC,
        world: World | None = None,
    ) -> None:
        try:
            self._type = BodyType(type)
        except ValueError:
            raise TypeError(f'type must be {BodyType}')
        self._mass = _verify_mass(mass)

        self._can_sleep = True

        self._shape = shape
        self._shape_imp = _get_shape_implementation(shape)
        self._imp = BaseBody(
            self,
            _mass_to_implementation_mass(self._mass, self._type),
            self._shape_imp,
        )
        self.type = self._type

        self._kinematic_angular_velocity = DVector3(0)
        self._kinematic_linear_velocity = DVector3(0)
        self._gravity: DVector3 | None = None
        self._groups = verify_groups(groups)
        self._mask = verify_mask(mask)
        self._world = None
        self.world = world

    def __repr__(self) -> str:
        return f'<gamut.physics.Body mass={self.mass} shape={self.shape!r}>'

    def _set_state(self) -> None:
        if self._can_sleep and self._type != BodyType.KINEMATIC:
            self._imp.set_can_sleep()
        else:
            self._imp.set_cannot_sleep()

    @property
    def angular_damping(self) -> float:
        return self._imp.angular_damping

    @angular_damping.setter
    def angular_damping(self, value: float) -> None:
        try:
            value = float(value)
        except (TypeError, ValueError):
            raise TypeError('angular damping must be float')
        if value < 0 or value > 1:
            raise ValueError('angular damping must be between 0 and 1')
        self._imp.angular_damping = value

    @property
    def angular_freedom(self) -> BVector3:
        return self._imp.angular_freedom

    @angular_freedom.setter
    def angular_freedom(self, value: BVector3) -> None:
        self._imp.angular_freedom = value

    @property
    def angular_sleep_threshold(self) -> float:
        return self._imp.angular_sleep_threshold

    @angular_sleep_threshold.setter
    def angular_sleep_threshold(self, value: float) -> None:
        try:
            value = float(value)
        except (TypeError, ValueError):
            raise TypeError('angular sleep threshold must be float')
        if value < 0:
            raise ValueError('angular sleep threshold must be 0 or more')
        self._imp.angular_sleep_threshold = value

    @property
    def angular_velocity(self) -> DVector3:
        if self._type == BodyType.DYNAMIC:
            return self._imp.angular_velocity
        elif self._type == BodyType.KINEMATIC:
            return self._kinematic_angular_velocity
        else:
            assert self._type == BodyType.STATIC
            return DVector3(0)

    @angular_velocity.setter
    def angular_velocity(self, value: DVector3) -> None:
        self._imp.angular_velocity = value
        self._kinematic_angular_velocity = value

    @property
    def can_sleep(self) -> bool:
        return self._can_sleep

    @can_sleep.setter
    def can_sleep(self, value: bool) -> None:
        self._can_sleep = bool(value)
        self._set_state()

    @property
    def is_sleeping(self) -> bool:
        return self._imp.is_sleeping

    @property
    def linear_damping(self) -> float:
        return self._imp.linear_damping

    @linear_damping.setter
    def linear_damping(self, value: float) -> None:
        try:
            value = float(value)
        except (TypeError, ValueError):
            raise TypeError('linear damping must be float')
        if value < 0 or value > 1:
            raise ValueError('linear damping must be between 0 and 1')
        self._imp.linear_damping = value

    @property
    def linear_freedom(self) -> BVector3:
        return self._imp.linear_freedom

    @linear_freedom.setter
    def linear_freedom(self, value: BVector3) -> None:
        self._imp.linear_freedom = value

    @property
    def linear_sleep_threshold(self) -> float:
        return self._imp.linear_sleep_threshold

    @linear_sleep_threshold.setter
    def linear_sleep_threshold(self, value: float) -> None:
        try:
            value = float(value)
        except (TypeError, ValueError):
            raise TypeError('linear sleep threshold must be float')
        if value < 0:
            raise ValueError('linear sleep threshold must be 0 or more')
        self._imp.linear_sleep_threshold = value

    @property
    def linear_velocity(self) -> DVector3:
        if self._type == BodyType.DYNAMIC:
            return self._imp.linear_velocity
        elif self._type == BodyType.KINEMATIC:
            return self._kinematic_linear_velocity
        else:
            assert self._type == BodyType.STATIC
            return DVector3(0)

    @linear_velocity.setter
    def linear_velocity(self, value: DVector3) -> None:
        self._imp.linear_velocity = value
        self._kinematic_linear_velocity = value

    @property
    def friction(self) -> float:
        return self._imp.friction

    @friction.setter
    def friction(self, value: float) -> None:
        try:
            value = float(value)
        except (ValueError, TypeError):
            raise TypeError('friction must be float')
        self._imp.friction = value

    @property
    def gravity(self) -> DVector3 | None:
        return self._gravity

    @gravity.setter
    def gravity(self, value: DVector3 | None) -> None:
        is_explicit = value is not None
        if value is None:
            world = self.world
            if world:
                gravity = world.gravity
            else:
                gravity = DVector3(0)
        else:
            gravity = value
        self._imp.set_gravity((is_explicit, gravity))
        self._gravity = value

    @property
    def groups(self) -> int:
        return self._groups

    @groups.setter
    def groups(self, value: int) -> None:
        self._groups = verify_groups(value)
        # re-add the body to the current world to change the groups internally
        world = self.world
        if world:
            self.world = None
            self.world = world

    @property
    def mask(self) -> int:
        return self._mask

    @mask.setter
    def mask(self, value: int) -> None:
        self._mask = verify_mask(value)
        # re-add the body to the current world to change the mask internally
        world = self.world
        if world:
            self.world = None
            self.world = world

    @property
    def mass(self) -> float:
        return self._mass

    @mass.setter
    def mass(self, value: float) -> None:
        self._mass = _verify_mass(value)
        self._imp.set_mass(
            _mass_to_implementation_mass(self._mass, self._type)
        )

    def raycast(self, start: DVector3, end: DVector3) -> RaycastHit | None:
        world = self.world
        if world is None:
            raise RuntimeError('body must be in a world')
        results = list(
            raycast(world, start, end, G_ALL_GROUPS, G_ALL_GROUPS, self._imp)
        )
        if results:
            assert len(results) == 1
            return results[0]
        return None

    @property
    def restitution(self) -> float:
        return self._imp.restitution

    @restitution.setter
    def restitution(self, value: float) -> None:
        try:
            value = float(value)
        except (ValueError, TypeError):
            raise TypeError('restitution must be float')
        self._imp.restitution = value

    @property
    def rolling_friction(self) -> float:
        return self._imp.rolling_friction

    @rolling_friction.setter
    def rolling_friction(self, value: float) -> None:
        try:
            value = float(value)
        except (ValueError, TypeError):
            raise TypeError('rolling friction must be float')
        self._imp.rolling_friction = value

    @property
    def shape(self) -> BodyShape:
        return self._shape

    @shape.setter
    def shape(self, shape: BodyShape) -> None:
        # order here is important, _get_shape_implementation can fail on an
        # invalid shape so we don't want to set anything yet
        self._shape_imp = _get_shape_implementation(shape)
        # again order is important, the implementation doesn't hold a strong
        # ref to the current shape, so some weirdness could happen if the
        # current shape is deleted prior to setting the new one
        self._imp.set_shape(self._shape_imp, self._groups, self._mask)
        self._shape = shape
        # we have to recalculate the local inertia by setting the mass
        self._imp.set_mass(
            _mass_to_implementation_mass(self._mass, self._type)
        )

    @property
    def spinning_friction(self) -> float:
        return self._imp.spinning_friction

    @spinning_friction.setter
    def spinning_friction(self, value: float) -> None:
        try:
            value = float(value)
        except (ValueError, TypeError):
            raise TypeError('spinning friction must be float')
        self._imp.spinning_friction = float(value)

    @property
    def tangible(self) -> bool:
        return self._imp.tangible

    @tangible.setter
    def tangible(self, value: bool) -> None:
        self._imp.tangible = bool(value)

    @property
    def transform(self) -> DMatrix4:
        return self._imp.transform

    @transform.setter
    def transform(self, value: DMatrix4) -> None:
        self._imp.transform = value

    @property
    def type(self) -> BodyType:
        return self._type

    @type.setter
    def type(self, value: BodyType) -> None:
        try:
            self._type = BodyType(value)
        except ValueError:
            raise TypeError(f'type must be {BodyType}')

        if value == BodyType.DYNAMIC:
            self._imp.set_to_dynamic()
        elif value == BodyType.STATIC:
            self._imp.set_to_static()
        else:
            assert value == BodyType.KINEMATIC
            self._imp.set_to_kinematic()
            self._kinematic_angular_velocity = self._imp.angular_velocity
            self._kinematic_linear_velocity = self._imp.linear_velocity
        self._set_state()

    def wake(self) -> None:
        self._imp.wake()

    @property
    def world(self) -> World:
        if self._world is None:
            return None
        return self._world()

    @world.setter
    def world(self, world: World | None) -> None:
        if world is not None and not isinstance(world, World):
            raise TypeError(f'world must be None or {World}')

        current_world = self.world
        if current_world is not None:
            remove_body_from_world(current_world, self, self._imp)
        if world is None:
            self._world = None
        else:
            self._world = ref(world)
            add_body_to_world(world, self, self._imp, self._groups, self._mask)


def _mass_to_implementation_mass(mass: float, body_type: BodyType) -> float:
    if body_type != BodyType.DYNAMIC:
        return 0
    assert mass > 0.0
    return mass


def _verify_mass(value: float) -> float:
    try:
        value = float(value)
    except (ValueError, TypeError):
        raise TypeError('mass must be float')
    if value <= 0.0:
        raise ValueError('mass must be > 0')
    return value


def _get_shape_implementation(shape: BodyShape) -> Shape:
    try:
        get_bullet_shape = shape._get_bullet_shape
    except AttributeError:
        raise TypeError(f'invalid shape: {shape}') from None
    return get_bullet_shape()
