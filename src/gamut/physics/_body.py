
from __future__ import annotations

__all__ = ['Body']

# gamut
from ._physics import Body as BaseBody
from ._world import add_body_to_world, remove_body_from_world, World
# python
from weakref import ref


class Body:

    def __init__(self, world: World | None) -> None:
        self._imp = BaseBody()
        self._world = None
        self.world = world

    def __repr__(self) -> str:
        return '<gamut.physics.Body>'

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
            add_body_to_world(world, self, self._imp)
