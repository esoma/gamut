
from __future__ import annotations

__all__ = ['Body', 'BodyType']

# gamut
from ._physics import Body as BaseBody
from ._physics import Shape
from ._world import add_body_to_world, remove_body_from_world, World
# gamut
from gamut.geometry import (Capsule, Composite3d, Cone, ConvexHull, Cylinder,
                            Mesh, Plane, RectangularCuboid, Sphere)
from gamut.glmhelp import dmat4_exact, dvec3_exact, F64Matrix4x4, F64Vector3
# python
from enum import auto, Enum
import struct
from typing import Any, Final, Union
from weakref import ref, WeakKeyDictionary
# pyglm
from glm import dmat4, dvec3

BodyShape = Union[
    Capsule,
    Composite3d,
    Cone,
    ConvexHull,
    Cylinder,
    Plane,
    RectangularCuboid,
    Sphere
]


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
        try:
            self._type = BodyType(type)
        except ValueError:
            raise TypeError(f'type must be {BodyType}')
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

        self._kinematic_angular_velocity = dvec3(0)
        self._kinematic_linear_velocity = dvec3(0)
        self._gravity: dvec3 | None = None
        self._groups = _verify_groups(groups)
        self._mask = _verify_mask(mask)
        self._world = None
        self.world = world

    def __repr__(self) -> str:
        return f'<gamut.physics.Body mass={self.mass} shape={self.shape!r}>'

    def _set_state(self) -> None:
        if self._is_enabled:
            if self._can_sleep and self._type != BodyType.KINEMATIC:
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
        try:
            value = float(value)
        except (TypeError, ValueError):
            raise TypeError('angular damping must be float')
        if value < 0 or value > 1:
            raise ValueError('angular damping must be between 0 and 1')
        self._imp.angular_damping = value

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
    def angular_velocity(self) -> dvec3:
        if self._type == BodyType.DYNAMIC:
            return dvec3(self._imp.angular_velocity)
        elif self._type == BodyType.KINEMATIC:
            return dvec3(self._kinematic_angular_velocity)
        else:
            assert self._type == BodyType.STATIC
            return dvec3(0)

    @angular_velocity.setter
    def angular_velocity(self, value: F64Vector3) -> None:
        try:
            value = dvec3_exact(value)
        except TypeError:
            raise TypeError('angular velocity must be dvec3')
        self._kinematic_angular_velocity = value
        self._imp.angular_velocity = tuple(value)

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
        try:
            value = float(value)
        except (TypeError, ValueError):
            raise TypeError('linear damping must be float')
        if value < 0 or value > 1:
            raise ValueError('linear damping must be between 0 and 1')
        self._imp.linear_damping = value

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
    def linear_velocity(self) -> dvec3:
        if self._type == BodyType.DYNAMIC:
            return dvec3(self._imp.linear_velocity)
        elif self._type == BodyType.KINEMATIC:
            return dvec3(self._kinematic_linear_velocity)
        else:
            assert self._type == BodyType.STATIC
            return dvec3(0)

    @linear_velocity.setter
    def linear_velocity(self, value: F64Vector3) -> None:
        try:
            value = dvec3_exact(value)
        except TypeError:
            raise TypeError('linear velocity must be dvec3')
        self._kinematic_linear_velocity = value
        self._imp.linear_velocity = tuple(value)

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
    def gravity(self) -> dvec3 | None:
        return self._gravity

    @gravity.setter
    def gravity(self, value: F64Vector3 | None) -> None:
        is_explicit = value is not None
        if value is None:
            world = self.world
            if world:
                value = tuple(world.gravity)
            else:
                value = (0, 0, 0)
            self._gravity = None
        else:
            try:
                self._gravity = dvec3_exact(value)
            except (ValueError, TypeError):
                raise TypeError('gravity must be None or dvec3')
            value = tuple(self._gravity)
        self._imp.set_gravity((is_explicit, value))

    @property
    def groups(self) -> int:
        return self._groups

    @groups.setter
    def groups(self, value: int) -> None:
        self._groups = _verify_groups(value)
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
        self._mask = _verify_mask(value)
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
        self._imp.set_shape(self._shape_imp)
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
    def transform(self) -> dmat4:
        return dmat4(self._imp.transform)

    @transform.setter
    def transform(self, value: F64Matrix4x4) -> None:
        try:
            value = dmat4_exact(value)
        except TypeError:
            raise TypeError('transform must be dmat4')
        self._imp.transform = tuple(value)

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


def _verify_groups(value: int) -> int:
    try:
        value = int(value)
    except (ValueError, TypeError):
        raise TypeError('groups must be int')
    try:
        struct.pack('=i', value)
    except struct.error:
        raise ValueError('groups must be 32 bit signed int')
    return value


def _verify_mask(value: int) -> int:
    try:
        value = int(value)
    except (ValueError, TypeError):
        raise TypeError('mask must be int')
    try:
        struct.pack('=i', value)
    except struct.error:
        raise ValueError('mask must be 32 bit signed int')
    return value


def _verify_mass(value: float) -> float:
    try:
        value = float(value)
    except (ValueError, TypeError):
        raise TypeError('mass must be float')
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
    except TypeError:
        raise TypeError(f'invalid shape: {shape}')
    except KeyError:
        pass

    if isinstance(shape, Composite3d):
        shapes = shape.shapes_flattened
    else:
        shapes = [shape]

    shape_imp = Shape()
    shape_data: list[Any] = []

    for sub_shape in shapes:
        if isinstance(sub_shape, Sphere):
            shape_data.append(
                shape_imp.add_sphere((sub_shape.radius, *sub_shape.center))
            )
        elif isinstance(sub_shape, Plane):
            shape_data.append(
                shape_imp.add_plane((sub_shape.distance, *sub_shape.normal))
            )
        elif isinstance(sub_shape, Cylinder):
            shape_data.append(
                shape_imp.add_cylinder((
                    sub_shape.radius,
                    sub_shape.height,
                    *sub_shape.center,
                    *sub_shape.rotation
                ))
            )
        elif isinstance(sub_shape, RectangularCuboid):
            shape_data.append(
                shape_imp.add_rectangular_cuboid((
                    *sub_shape.center,
                    *sub_shape.dimensions,
                    *sub_shape.rotation
                ))
            )
        elif isinstance(sub_shape, Capsule):
            shape_data.append(
                shape_imp.add_capsule((
                    sub_shape.radius,
                    sub_shape.height,
                    *sub_shape.center,
                    *sub_shape.rotation
                ))
            )
        elif isinstance(sub_shape, Cone):
            shape_data.append(
                shape_imp.add_cone((
                    sub_shape.radius,
                    sub_shape.height,
                    *sub_shape.center,
                    *sub_shape.rotation
                ))
            )
        elif isinstance(sub_shape, ConvexHull):
            shape_data.append(shape_imp.add_convex_hull(
                tuple(tuple(p) for p in sub_shape.points)
            ))
        elif isinstance(sub_shape, Mesh):
            vertices = sub_shape.vertices
            triangle_indices = sub_shape.triangle_indices
            shape_data.append(vertices)
            shape_data.append(triangle_indices)
            shape_data.append(
                shape_imp.add_mesh((
                    len(vertices),
                    vertices.address,
                    len(triangle_indices),
                    triangle_indices.address
                ))
            )
        else:
            raise TypeError(f'invalid shape: {sub_shape}')

    _shape_imps[shape] = (shape_imp, tuple(shape_data))
    return shape_imp
