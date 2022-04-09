
from __future__ import annotations

__all__ = ['Collision', 'Contact']

# gamut
from gamut.math import DVector3
# python
from datetime import timedelta
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # gamut
    from ._body import Body


class Collision:

    def __init__(
        self,
        when: timedelta,
        body_a: Body,
        body_b: Body,
        contacts: tuple[Contact, ...]
    ):
        self._when = when
        self._body_a = body_a
        self._body_b = body_b
        self._contacts = contacts

    def __repr__(self) -> str:
        return (
            f'<gamut.physics.Collision between '
            f'{self._body_a} and {self._body_b} at {self._when}>'
        )

    @property
    def body_a(self) -> Body:
        return self._body_a

    @property
    def body_b(self) -> Body:
        return self._body_b

    @property
    def contacts(self) -> tuple[Contact, ...]:
        return self._contacts

    @property
    def when(self) -> timedelta:
        return self._when


class Contact:

    def __init__(
        self,
        local_position_a: DVector3,
        world_position_a: DVector3,
        normal_a: DVector3,
        local_position_b: DVector3,
        world_position_b: DVector3,
        normal_b: DVector3
    ):
        self._local_position_a = local_position_a
        self._world_position_a = world_position_a
        self._normal_a = normal_a
        self._local_position_b = local_position_b
        self._world_position_b = world_position_b
        self._normal_b = normal_b

    def __repr__(self) -> str:
        return (
            f'<gamut.physics.Contact '
            f'{self._world_position_a} & {self._world_position_b}>'
        )

    @property
    def local_position_a(self) -> DVector3:
        return self._local_position_a

    @property
    def world_position_a(self) -> DVector3:
        return self._world_position_a

    @property
    def normal_a(self) -> DVector3:
        return self._normal_a

    @property
    def local_position_b(self) -> DVector3:
        return self._local_position_b

    @property
    def world_position_b(self) -> DVector3:
        return self._world_position_b

    @property
    def normal_b(self) -> DVector3:
        return self._normal_b
