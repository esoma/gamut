
__all__ = ['plugin']

# python
from typing import Type

# gamut
from .event.mypy import Plugin as EventPlugin


class Plugin(EventPlugin):
    pass


def plugin(version: str) -> Type[Plugin]:
    return Plugin
