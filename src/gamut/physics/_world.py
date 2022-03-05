
from __future__ import annotations

__all__ = ['add_body_to_world', 'remove_body_from_world', 'World']

# gamut
from ._collision import Collision, Contact
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

        self._time = timedelta(seconds=0)
        try:
            self._fixed_time_seconds = fixed_time_step.total_seconds()
        except AttributeError:
            raise TypeError('fixed time step must be timedelta')
        if self._fixed_time_seconds <= 0:
            raise ValueError('fixed time step must be greater than 0 seconds')
        self._fixed_time_step = timedelta(seconds=self._fixed_time_seconds)
        self._leftover_simulation_seconds = 0.0
        self._is_simulating = False

    def __repr__(self) -> str:
        return '<gamut.physics.World>'

    def _add_body(
        self,
        body: Body,
        body_implementation: Any,
        groups: int,
        mask: int
    ) -> None:
        assert body not in self._bodies
        self._imp.add_body((body_implementation, groups, mask))
        self._bodies.add(body)

    def _remove_body(self, body: Body, body_implementation: Any) -> None:
        assert body in self._bodies
        self._imp.remove_body(body_implementation)
        self._bodies.remove(body)

    def simulate(self, duration: timedelta) -> WorldSimulation:
        return WorldSimulation(self, duration)

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

    @property
    def time(self) -> timedelta:
        return self._time


class WorldSimulation:

    def __init__(self, world: World, duration: timedelta):
        self._finished = True
        if world._is_simulating:
            raise RuntimeError('this world is already simulating')

        try:
            duration_seconds = duration.total_seconds()
        except AttributeError:
            raise TypeError('duration must be timedelta')
        if duration_seconds < 0:
            raise ValueError(
                'duration must be greater than or equal to 0 seconds'
            )

        world._is_simulating = True
        self._world = world
        self._duration_seconds = duration_seconds
        self._finished = False

        seconds = (
            world._leftover_simulation_seconds +
            duration_seconds
        )
        world._leftover_simulation_seconds = (
            seconds % world._fixed_time_seconds
        )
        self._steps = iter(range(floor(seconds / world._fixed_time_seconds)))

    def __del__(self):
        self._finish()

    def __iter__(self) -> Iterable[tuple[Collision]]:
        return self

    def __next__(self) -> tuple[Collision]:
        try:
            next(self._steps)
            self._world._time += self._world._fixed_time_step
            return tuple(
                Collision(
                    self._world._time,
                    c[0],
                    c[1],
                    tuple(
                        Contact(
                            dvec3(cc[0]),
                            dvec3(cc[1]),
                            dvec3(cc[4]) * dvec3(-1),
                            dvec3(cc[2]),
                            dvec3(cc[3]),
                            dvec3(cc[4]),
                        )
                        for cc in c[2]
                    )
                )
                for c in self._world._imp.simulate((
                    self._world._fixed_time_seconds,
                    True
                ))
            )
        except StopIteration:
            self._finish()
            raise

    def _finish(self) -> None:
        if self._finished:
            return
        for _ in self._steps:
            self._world._imp.simulate((self._world._fixed_time_seconds, False))
        self._world._is_simulating = False
        self._finished = True


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
