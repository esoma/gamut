
__all__ = ['TestEventLoop']

# gamut
from gamut.event import Bind, Event, EventLoop, EventLoopEnd, EventLoopStart
# python
from typing import Optional
# pytest
import pytest


class TestEventLoop:

    @pytest.fixture
    def cls(self) -> type[EventLoop]:
        return EventLoop

    @pytest.fixture
    def start_event_cls(self) -> type[EventLoopStart]:
        return EventLoopStart

    @pytest.fixture
    def end_event_cls(self) -> type[EventLoopEnd]:
        return EventLoopEnd

    def test_instantiate_base_event_loop(
        self,
        cls: type[EventLoop]
    ) -> None:
        with pytest.raises(TypeError) as excinfo:
            cls()
        assert str(excinfo.value) == (
            f'Can\'t instantiate abstract class {cls.__name__} with abstract '
            f'method main'
        )

    def test_base_main_call(self, cls: type[EventLoop]) -> None:
        class TestEventLoop(cls): # type: ignore
            async def main(self) -> None:
                await super().main()

        app = TestEventLoop()
        with pytest.raises(NotImplementedError) as excinfo:
            app.run()

    @pytest.mark.parametrize("return_value", [0, 1, 100])
    def test_return_value(
        self,
        cls: type[EventLoop],
        return_value: int
    ) -> None:
        class TestEventLoop(cls): # type: ignore
            async def main(self) -> int:
                return return_value

        app = TestEventLoop()
        assert app.run() == return_value
        assert app.run() == return_value

    @pytest.mark.parametrize("exception", [
        Exception("test"),
        KeyboardInterrupt(),
        RuntimeError("test"),
    ])
    def test_error_in_main(
        self,
        cls: type[EventLoop],
        exception: BaseException
    ) -> None:
        class TestEventLoop(cls): # type: ignore
            async def main(self) -> None:
                raise exception

        app = TestEventLoop()
        with pytest.raises(BaseException) as excinfo:
            app.run()
        assert excinfo.value is exception

    def test_await_event(self, cls: type[EventLoop]) -> None:
        class TestEvent(Event):
            text: str

        class TestEventLoop(cls): # type: ignore
            async def main(self) -> str:
                event = await TestEvent
                return event.text

            async def poll(self, block: bool = True) -> Optional[Event]:
                return TestEvent("test")

        app = TestEventLoop()
        assert app.run() == "test"

    def test_queue_event(self, cls: type[EventLoop]) -> None:
        class TestEvent(Event):
            text: str

        class TestEventLoop(cls): # type: ignore
            async def main(self) -> str:
                self.queue_event(TestEvent("test"))
                event = await TestEvent
                return event.text

        app = TestEventLoop()
        assert app.run() == "test"

    def test_start_end(
        self,
        cls: type[EventLoop],
        start_event_cls: type[EventLoopStart],
        end_event_cls: type[EventLoopEnd],
    ) -> None:
        order: list[int] = []

        async def start(event: EventLoopStart) -> None:
            assert isinstance(event, start_event_cls)
            order.append(1)

        class TestEventLoop(cls): # type: ignore
            async def main(self) -> None:
                order.append(2)

        async def end(event: EventLoopEnd) -> None:
            assert isinstance(event, end_event_cls)
            order.append(3)

        with (
            Bind.on(start_event_cls, start),
            Bind.on(end_event_cls, end)
        ):
            TestEventLoop().run()

        assert order == [1, 2, 3]
