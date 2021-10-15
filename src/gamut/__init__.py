
__all__ = [
    'Application',
    'ApplicationEnd',
    'ApplicationEvent',
    'ApplicationStart',
    'Window',
    'WindowBufferSynchronization',
    'WindowClose',
    'WindowHidden',
    'WindowMoved',
    'WindowResized',
    'WindowShown',
]

# python
import warnings

warnings.filterwarnings('ignore', 'Using SDL2 binaries from ')

# gamut
from ._application import (Application, ApplicationEnd, ApplicationEvent,
                           ApplicationStart)
from ._window import (Window, WindowBufferSynchronization, WindowClose,
                      WindowHidden, WindowMoved, WindowResized, WindowShown)
