
__all__ = ['plugin']

# gamut
from .event.mypy import Plugin as EventPlugin
# python
from typing import Type


class Plugin(EventPlugin):
    pass


def plugin(version: str) -> Type[Plugin]:
    return Plugin
