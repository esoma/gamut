
from __future__ import annotations

__all__ = [
    'add_body_to_world',
    'RaycastHit',
    'remove_body_from_world',
    'World'
]

# gamut
from ._collision import Collision, Contact
from ._groups import ALL_GROUPS, verify_groups, verify_mask
from ._physics import World as BaseWorld
# gamut
from gamut.math import Vector3
# python
from datetime import timedelta
from math import floor
from typing import Any, Generator, TYPE_CHECKING

if TYPE_CHECKING:
    # gamut
    from ._body import Body


class RaycastHit:

    def __init__(self, position: Vector3, normal: Vector3, body: Body):
        self.position = position
        self.normal = normal
        self.body = body


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

    def raycast(
        self,
        start: Vector3,
        end: Vector3,
        *,
        groups: int = ALL_GROUPS,
        mask: int = ALL_GROUPS
    ) -> Generator[RaycastHit, None, None]:
        if not isinstance(start, Vector3):
            raise TypeError(f'start must be Vector3, got {start!r}')
        if not isinstance(end, Vector3):
            raise TypeError(f'end must be Vector3, got {end!r}')
        groups = verify_groups(groups)
        mask = verify_mask(mask)

        results = self._imp.raycast(start, end, groups, mask)
        results.sort(key=lambda h: h[3])
        for hit in results:
            yield RaycastHit(hit[0], hit[1], hit[2])

    def simulate(self, duration: timedelta) -> WorldSimulation:
        return WorldSimulation(self, duration)

    @property
    def bodies(self) -> list[Body]:
        return list(self._bodies)

    @property
    def gravity(self) -> Vector3:
        return self._imp.gravity

    @gravity.setter
    def gravity(self, value: Vector3) -> None:
        self._imp.gravity = value

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
                            cc[0],
                            cc[1],
                            cc[4] * Vector3(-1),
                            cc[2],
                            cc[3],
                            cc[4],
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
