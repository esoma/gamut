
__all__ = [
    'BoundWindowClose',
    'BoundWindowHidden',
    'BoundWindowMoved',
    'BoundWindowResized',
    'BoundWindowShown',
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
from ._application import (GamutApplication, GamutApplicationEnd,
                           GamutApplicationEvent, GamutApplicationStart)
from ._window import (BoundWindowClose, BoundWindowHidden, BoundWindowMoved,
                      BoundWindowResized, BoundWindowShown, Window)
