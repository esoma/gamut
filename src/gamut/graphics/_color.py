
__all__ = ['Color']


# python
from typing import Any, Generator


class Color:

    def __init__(
        self,
        red: float,
        green: float,
        blue: float,
        alpha: float = 1.0
    ):
        self.red = max(min(float(red), 1.0), 0.0)
        self.green = max(min(float(green), 1.0), 0.0)
        self.blue = max(min(float(blue), 1.0), 0.0)
        self.alpha = max(min(float(alpha), 1.0), 0.0)

    def __iter__(self) -> Generator[float, None, None]:
        yield self.red
        yield self.green
        yield self.blue
        yield self.alpha

    def __len__(self) -> int:
        return 4

    def __getitem__(self, index: int) -> float:
        return (self.red, self.green, self.blue, self.alpha)[index]

    def __eq__(self, other: Any) -> bool:
        try:
            return (
                len(other) == 4 and
                self.red == other[0] and
                self.green == other[1] and
                self.blue == other[2] and
                self.alpha == other[3]
            )
        except TypeError:
            return False

    def __repr__(self) -> str:
        return (
            f'<gamut.Color '
                f'{self.red}, {self.green}, {self.blue}, {self.alpha}'
            f'>'
        )
