
__all__ = [
    'BoundGamutApplicationEnd',
    'BoundGamutApplicationEvent',
    'BoundGamutApplicationStart',
    'GamutApplication',
    'GamutApplicationEnd',
    'GamutApplicationEvent',
    'GamutApplicationStart',
    'Window',
]

# python
import warnings

warnings.filterwarnings('ignore', 'Using SDL2 binaries from ')

# gamut
from ._application import (BoundGamutApplicationEnd,
                           BoundGamutApplicationEvent,
                           BoundGamutApplicationStart, GamutApplication,
                           GamutApplicationEnd, GamutApplicationEvent,
                           GamutApplicationStart)
from ._window import Window
