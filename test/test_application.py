
# gamut
from .event.test_application import TestApplication
# gamut
from gamut import (BoundGamutApplicationEnd, BoundGamutApplicationStart,
                   GamutApplication)
from gamut.event import Event
# python
from typing import Optional
# pytest
import pytest


class NonBlockingGamutApplication(GamutApplication):

    async def poll(self, block: bool = False) -> Optional[Event]:
        return await super().poll(block=block)


class TestGamutApplication(TestApplication):

    @pytest.fixture
    def cls(self) -> type[NonBlockingGamutApplication]:
        return NonBlockingGamutApplication

    @pytest.fixture
    def bound_start_event_cls(self) -> type[BoundGamutApplicationStart]:
        return BoundGamutApplicationStart

    @pytest.fixture
    def bound_end_event_cls(self) -> type[BoundGamutApplicationEnd]:
        return BoundGamutApplicationEnd
