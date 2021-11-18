
__all__ = ['TestApplication']

# gamut
from gamut import Application
from gamut.event import Event
# python
import time
from typing import Optional, TypeVar

R = TypeVar('R')


class TestApplication(Application[R]):

    async def poll(
        self,
        block: bool = True,
        timeout: int = 5
    ) -> Optional[Event]:
        start = time.monotonic()
        while True:
            event = await super().poll(block=False)
            if event:
                return event
            if time.monotonic() - start > timeout:
                raise RuntimeError('polling timed out')
            time.sleep(.01)
