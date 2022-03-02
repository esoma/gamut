
from __future__ import annotations

__all__ = ['Body', 'BodyType']

# gamut
from ._physics import Body as BaseBody
from ._physics import Shape
from ._world import add_body_to_world, remove_body_from_world, World
# gamut
from gamut.geometry import Cylinder, Plane, Sphere
from gamut.glmhelp import dmat4_exact, dvec3_exact, F64Matrix4x4, F64Vector3
# python
from datetime import timedelta
from enum import auto, Enum
from math import isinf
import struct
from typing import Any, Final
from weakref import ref, WeakKeyDictionary
# pyglm
from glm import dmat4, dvec3

BodyShape = Cylinder | Plane | Sphere


class BodyType(Enum):
    DYNAMIC = auto()
    STATIC = auto()
    KINEMATIC = auto()


class Body:

    ALL_GROUPS: Final = -1

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
        self._type = BodyType(type)
        self._mass = _verify_mass(mass)

        self._is_enabled = True
        self._can_sleep = True

        self._shape = shape
        self._shape_imp = _get_shape_implementation(shape)
        self._imp = BaseBody(
            _mass_to_implementation_mass(self._mass, self._type),
            self._shape_imp,
        )
        self.type = self._type

        self._gravity: dvec3 | None = None
        self._groups = groups
        self._mask = mask
        self._world = None
        self.world = world

    def __repr__(self) -> str:
        return '<gamut.physics.Body>'

    def _set_state(self) -> None:
        if self._is_enabled:
            if self._can_sleep:
                self._imp.set_enabled()
            else:
                self._imp.set_cannot_sleep()
        else:
            self._imp.set_disabled()

    @property
    def angular_damping(self) -> float:
        return self._imp.angular_damping

    @angular_damping.setter
    def angular_damping(self, value: float) -> None:
        self._imp.angular_damping = float(value)

    @property
    def angular_sleep_threshold(self) -> float:
        return self._imp.angular_sleep_threshold

    @angular_sleep_threshold.setter
    def angular_sleep_threshold(self, value: float) -> None:
        self._imp.angular_sleep_threshold = float(value)

    @property
    def angular_velocity(self) -> dvec3:
        return dvec3(self._imp.angular_velocity)

    @angular_velocity.setter
    def angular_velocity(self, value: F64Vector3) -> None:
        self._imp.angular_velocity = tuple(dvec3_exact(value))

    @property
    def can_sleep(self) -> bool:
        return self._can_sleep

    @can_sleep.setter
    def can_sleep(self, value: bool) -> None:
        self._can_sleep = bool(value)
        self._set_state()

    @property
    def is_enabled(self) -> bool:
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, value: bool) -> None:
        self._is_enabled = bool(value)
        self._set_state()

    @property
    def is_sleeping(self) -> bool:
        return self._imp.is_sleeping

    @property
    def linear_damping(self) -> float:
        return self._imp.linear_damping

    @linear_damping.setter
    def linear_damping(self, value: float) -> None:
        self._imp.linear_damping = float(value)

    @property
    def linear_sleep_threshold(self) -> float:
        return self._imp.linear_sleep_threshold

    @linear_sleep_threshold.setter
    def linear_sleep_threshold(self, value: float) -> None:
        self._imp.linear_sleep_threshold = float(value)

    @property
    def linear_velocity(self) -> dvec3:
        return dvec3(self._imp.linear_velocity)

    @linear_velocity.setter
    def linear_velocity(self, value: F64Vector3) -> None:
        self._imp.linear_velocity = tuple(dvec3_exact(value))

    @property
    def friction(self) -> float:
        return self._imp.friction

    @friction.setter
    def friction(self, value: float) -> None:
        self._imp.friction = float(value)

    @property
    def gravity(self) -> dvec3 | None:
        return self._gravity

    @gravity.setter
    def gravity(self, value: F64Vector3 | None) -> None:
        is_explicit = value is not None
        if value is None:
            value = tuple(dvec3_exact(value))
        else:
            world = self.world
            if world:
                value = tuple(world.gravity)
            else:
                values = (0, 0, 0)
        self._imp.set_gravity((is_explicit, value))

    @property
    def groups(self) -> int:
        return self._groups

    @groups.setter
    def groups(self, value: int) -> None:
        value = int(value)
        try:
            struct.pack('=i', value)
        except struct.error:
            raise ValueError('groups must be 32 bit signed int')
        self._groups = value

        world = self.world
        if world:
            self.world = None
            self.world = world

    @property
    def mask(self) -> int:
        return self._mask

    @mask.setter
    def mask(self, value: int) -> None:
        value = int(value)
        try:
            struct.pack('=i', value)
        except struct.error:
            raise ValueError('mask must be 32 bit signed int')
        self._mask = value

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

    @property
    def restitution(self) -> float:
        return self._imp.restitution

    @restitution.setter
    def restitution(self, value: float) -> None:
        self._imp.restitution = float(value)

    @property
    def rolling_friction(self) -> float:
        return self._imp.rolling_friction

    @rolling_friction.setter
    def rolling_friction(self, value: float) -> None:
        self._imp.rolling_friction = float(value)

    @property
    def shape(self) -> BodyShape:
        return self._shape

    @property
    def spinning_friction(self) -> float:
        return self._imp.spinning_friction

    @spinning_friction.setter
    def spinning_friction(self, value: float) -> None:
        self._imp.spinning_friction = float(value)

    @property
    def transform(self) -> dmat4:
        return dmat4(self._imp.transform)

    @transform.setter
    def transform(self, value: F64Matrix4x4) -> None:
        self._imp.transform = tuple(dmat4_exact(value))

    @property
    def type(self) -> BodyType:
        return self._type

    @type.setter
    def type(self, value: BodyType) -> None:
        self._type = BodyType(value)

        if value == BodyType.DYNAMIC:
            self._imp.set_to_dynamic()
        elif value == BodyType.STATIC:
            self._imp.set_to_static()
        else:
            assert value == BodyType.KINEMATIC
            self._imp.set_to_kinematic()

    def wake(self) -> None:
        self._imp.wake()

    @property
    def world(self) -> World:
        if self._world is None:
            return None
        return self._world()

    @world.setter
    def world(self, world: World | None) -> None:
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
    value = float(value)
    if value <= 0.0:
        raise ValueError('mass must be > 0')
    return value


_shape_imps: WeakKeyDictionary[
    BodyShape,
    tuple[Shape, tuple[Any, ...]]
] = WeakKeyDictionary()


def _get_shape_implementation(shape: BodyShape) -> Shape:
    try:
        return _shape_imps[shape][0]
    except KeyError:
        pass

    shape_imp = Shape()
    shape_capsules: list[Any] = []
    if isinstance(shape, Sphere):
        shape_capsules.append(
            shape_imp.add_sphere((shape.radius, *shape.center))
        )
    elif isinstance(shape, Plane):
        shape_capsules.append(
            shape_imp.add_plane((shape.distance, *shape.normal))
        )
    elif isinstance(shape, Cylinder):
        shape_capsules.append(
            shape_imp.add_cylinder((
                shape.radius,
                shape.height,
                *shape.center,
                *shape.rotation
            ))
        )
    else:
        raise TypeError('invalid shape: {shape}')

    _shape_imps[shape] = (shape_imp, tuple(shape_capsules))

    return shape_imp
