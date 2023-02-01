
__all__ = ['DegenerateGeometryError']

# python
from typing import Any


class DegenerateGeometryError(ValueError):

    degenerate_form: Any

    def __init__(self, degenerate_form: Any, message: str) -> None:
        super().__init__(message)
        self.degenerate_form = degenerate_form
