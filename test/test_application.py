
# gamut
from .event.test_event_loop import TestEventLoop
# gamut
from gamut import GamutApplication, GamutApplicationEnd, GamutApplicationStart
from gamut.event import Bind, Event
from gamut.peripheral import (KeyboardConnected, KeyboardDisconnected,
                              MouseConnected, MouseDisconnected)
# python
from typing import Any, ContextManager, Optional
# pytest
import pytest


class NonBlockingGamutApplication(GamutApplication):

    async def poll(self, block: bool = False) -> Optional[Event]:
        return await super().poll(block=block)


class TestGamutApplication(TestEventLoop):

    @pytest.fixture
    def cls(self) -> type[NonBlockingGamutApplication]:
        return NonBlockingGamutApplication

    @pytest.fixture
    def start_event_cls(self) -> type[GamutApplicationStart]:
        return GamutApplicationStart

    @pytest.fixture
    def end_event_cls(self) -> type[GamutApplicationEnd]:
        return GamutApplicationEnd


def test_mouse() -> None:
    connected_event: Optional[MouseConnected] = None
    disconnected_event: Optional[MouseDisconnected] = None

    class App(GamutApplication):

        async def main(self) -> None:
            assert self.mouse.is_connected

        async def connected(self, event: MouseConnected) -> None:
            nonlocal connected_event
            assert connected_event is None
            connected_event = event
            assert self.mouse.is_connected

        async def disconnected(self, event: MouseDisconnected) -> None:
            nonlocal disconnected_event
            assert disconnected_event is None
            disconnected_event = event
            assert not self.mouse.is_connected

        def run_context(self) -> ContextManager:
            super_cm = super().run_context()
            class TestContextManager:
                def __init__(cm_self) -> None:
                    cm_self.binds: list[Bind] = [
                        Bind.on(self.mouse.Connected, self.connected),
                        Bind.on(self.mouse.Disconnected, self.disconnected)
                    ]
                def __enter__(cm_self) -> None:
                    super_cm.__enter__()
                    for bind in cm_self.binds:
                        bind.__enter__()
                def __exit__(cm_self, *args: Any) -> None:
                    super_cm.__exit__(*args)
                    for bind in cm_self.binds:
                        bind.__exit__(*args)
            return TestContextManager()

    app = App()
    assert not app.mouse.is_connected
    assert connected_event is None
    assert disconnected_event is None
    app.run()
    assert not app.mouse.is_connected
    assert isinstance(connected_event, app.mouse.Connected)
    assert connected_event.mouse is app.mouse # type: ignore
    assert isinstance(disconnected_event, app.mouse.Disconnected)
    assert disconnected_event.mouse is app.mouse


def test_keyboard() -> None:
    connected_event: Optional[KeyboardConnected] = None
    disconnected_event: Optional[KeyboardDisconnected] = None

    class App(GamutApplication):

        async def main(self) -> None:
            assert self.keyboard.is_connected

        async def connected(self, event: KeyboardConnected) -> None:
            nonlocal connected_event
            assert connected_event is None
            connected_event = event
            assert self.keyboard.is_connected

        async def disconnected(self, event: KeyboardDisconnected) -> None:
            nonlocal disconnected_event
            assert disconnected_event is None
            disconnected_event = event
            assert not self.keyboard.is_connected

        def run_context(self) -> ContextManager:
            super_cm = super().run_context()
            class TestContextManager:
                def __init__(cm_self) -> None:
                    cm_self.binds: list[Bind] = [
                        Bind.on(self.keyboard.Connected, self.connected),
                        Bind.on(self.keyboard.Disconnected, self.disconnected)
                    ]
                def __enter__(cm_self) -> None:
                    super_cm.__enter__()
                    for bind in cm_self.binds:
                        bind.__enter__()
                def __exit__(cm_self, *args: Any) -> None:
                    super_cm.__exit__(*args)
                    for bind in cm_self.binds:
                        bind.__exit__(*args)
            return TestContextManager()

    app = App()
    assert not app.keyboard.is_connected
    assert connected_event is None
    assert disconnected_event is None
    app.run()
    assert not app.keyboard.is_connected
    assert isinstance(connected_event, app.keyboard.Connected)
    assert connected_event.keyboard is app.keyboard # type: ignore
    assert isinstance(disconnected_event, app.keyboard.Disconnected)
    assert disconnected_event.keyboard is app.keyboard
