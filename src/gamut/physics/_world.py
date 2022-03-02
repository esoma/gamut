
from __future__ import annotations

__all__ = ['add_body_to_world', 'remove_body_from_world', 'World']

# gamut
from ._physics import World as BaseWorld
# gamut
from gamut.glmhelp import dvec3_exact, F64Vector3
# python
from datetime import timedelta
from math import floor
from typing import Any, TYPE_CHECKING
# pyglm
from glm import dvec3

if TYPE_CHECKING:
    # gamut
    from ._body import Body


class World:

    def __init__(self, fixed_time_step: timedelta) -> None:
        self._imp = BaseWorld()
        self._bodies: set[Body] = set()

        try:
            self._fixed_time_seconds = fixed_time_step.total_seconds()
        except AttributeError:
            raise TypeError('fixed time step must be timedelta')
        if self._fixed_time_seconds <= 0:
            raise ValueError('fixed time step must be greater than 0 seconds')
        self._leftover_simulation_seconds = 0.0

    def __repr__(self) -> str:
        return '<gamut.physics.World>'

    def _add_body(
        self,
        body: Body,
        body_implementation: Any,
        groups: int,
        mask: int
    ) -> None:
        if body in self._bodies:
            return
        self._imp.add_body((body_implementation, groups, mask))
        self._bodies.add(body)

    def _remove_body(self, body: Body, body_implementation: Any) -> None:
        if body not in self._bodies:
            return
        self._imp.remove_body(body_implementation)
        self._bodies.remove(body)

    def simulate(self, duration: timedelta) -> None:
        try:
            duration_seconds = duration.total_seconds()
        except AttributeError:
            raise TypeError('duration must be timedelta')
        if duration_seconds < 0:
            raise ValueError(
                'duration must be greater than or equal to 0 seconds'
            )

        seconds = self._leftover_simulation_seconds + duration_seconds
        for _ in range(floor(seconds / self._fixed_time_seconds)):
            self._imp.simulate(self._fixed_time_seconds)
        self._leftover_simulation_seconds = seconds % self._fixed_time_seconds

    @property
    def bodies(self) -> list[Body]:
        return list(self._bodies)

    @property
    def gravity(self) -> dvec3:
        return dvec3(self._imp.gravity)

    @gravity.setter
    def gravity(self, value: F64Vector3) -> None:
        try:
            value = dvec3_exact(value)
        except TypeError:
            raise TypeError('gravity must be dvec3')
        self._imp.gravity = tuple(value)


def add_body_to_world(
    world: World,
    body: Body,
    body_implementation: Any,
    groups: int,
    mask: int
) -> None:
    world._add_body(body, body_implementation, groups, mask)


def remove_body_from_world(
    world: World,
    body: Body,
    body_implementation: Any
) -> None:
    world._remove_body(body, body_implementation)
