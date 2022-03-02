
from __future__ import annotations

__all__ = ['add_body_to_world', 'World']

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
        self._fixed_time_step = fixed_time_step.total_seconds()
        self._leftover_step_duration = 0.0

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
        duration = self._leftover_step_duration + duration.total_seconds()
        for _ in range(floor(duration / self._fixed_time_step)):
            self._imp.simulate(self._fixed_time_step)
        self._leftover_step_duration = duration % self._fixed_time_step

    @property
    def bodies(self) -> set[Body]:
        return set(self._bodies)

    @property
    def gravity(self) -> dvec3:
        return dvec3(self._imp.gravity)

    @gravity.setter
    def gravity(self, value: F64Vector3) -> None:
        self._imp.gravity = tuple(dvec3_exact(value))


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
