
# gamut
from .event.test_event_loop import TestEventLoop
# gamut
from gamut import Application, ApplicationEnd, ApplicationStart
from gamut.event import Bind, Event
from gamut.peripheral import (KeyboardConnected, KeyboardDisconnected,
                              MouseConnected, MouseDisconnected)
# python
from typing import Any, ContextManager, Optional
# pytest
import pytest


class NonBlockingApplication(Application):

    async def poll(self, block: bool = False) -> Optional[Event]:
        return await super().poll(block=block)


class TestApplication(TestEventLoop):

    @pytest.fixture
    def cls(self) -> type[NonBlockingApplication]:
        return NonBlockingApplication

    @pytest.fixture
    def start_event_cls(self) -> type[ApplicationStart]:
        return ApplicationStart

    @pytest.fixture
    def end_event_cls(self) -> type[ApplicationEnd]:
        return ApplicationEnd


def test_mouse() -> None:
    connected_event: Optional[MouseConnected] = None
    disconnected_event: Optional[MouseDisconnected] = None

    class App(Application):

        async def main(self) -> None:
            assert not self.mice
            await MouseConnected
            assert self.mice
            assert len(self.mice) == 1
            assert self.mice[0].is_connected

        async def connected(self, event: MouseConnected) -> None:
            nonlocal connected_event
            assert connected_event is None
            connected_event = event

        async def disconnected(self, event: MouseDisconnected) -> None:
            nonlocal disconnected_event
            assert disconnected_event is None
            disconnected_event = event

        def run_context(self) -> ContextManager:
            super_cm = super().run_context()
            class TestContextManager:
                def __init__(cm_self) -> None:
                    cm_self.binds: list[Bind] = [
                        Bind.on(MouseConnected, self.connected),
                        Bind.on(MouseDisconnected, self.disconnected)
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
    assert not app.mice
    app.run()
    assert not app.mice
    assert isinstance(connected_event, MouseConnected)
    assert isinstance(disconnected_event, MouseDisconnected)
    assert connected_event.mouse is disconnected_event.mouse


def test_keyboard() -> None:
    connected_event: Optional[KeyboardConnected] = None
    disconnected_event: Optional[KeyboardDisconnected] = None

    class App(Application):

        async def main(self) -> None:
            assert not self.keyboards
            await KeyboardConnected
            assert self.keyboards
            assert len(self.keyboards) == 1
            assert self.keyboards[0].is_connected

        async def connected(self, event: KeyboardConnected) -> None:
            nonlocal connected_event
            assert connected_event is None
            connected_event = event

        async def disconnected(self, event: KeyboardDisconnected) -> None:
            nonlocal disconnected_event
            assert disconnected_event is None
            disconnected_event = event

        def run_context(self) -> ContextManager:
            super_cm = super().run_context()
            class TestContextManager:
                def __init__(cm_self) -> None:
                    cm_self.binds: list[Bind] = [
                        Bind.on(KeyboardConnected, self.connected),
                        Bind.on(KeyboardDisconnected, self.disconnected)
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
    assert not app.keyboards
    app.run()
    assert not app.keyboards
    assert isinstance(connected_event, KeyboardConnected)
    assert isinstance(disconnected_event, KeyboardDisconnected)
    assert connected_event.keyboard is disconnected_event.keyboard
