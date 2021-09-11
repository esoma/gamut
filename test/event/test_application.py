
__all__ = ['TestApplication']

# gamut
from gamut.event import (Application, Bind, BoundApplicationEnd,
                         BoundApplicationStart, Event)
# python
from typing import Optional
# pytest
import pytest


class TestApplication:

    @pytest.fixture
    def cls(self) -> type[Application]:
        return Application

    @pytest.fixture
    def bound_start_event_cls(self) -> type[BoundApplicationStart]:
        return BoundApplicationStart

    @pytest.fixture
    def bound_end_event_cls(self) -> type[BoundApplicationEnd]:
        return BoundApplicationEnd

    def test_instantiate_base_application(
        self,
        cls: type[Application]
    ) -> None:
        with pytest.raises(TypeError) as excinfo:
            cls()
        assert str(excinfo.value) == (
            f'Can\'t instantiate abstract class {cls.__name__} with abstract '
            f'method main'
        )

    def test_base_main_call(self, cls: type[Application]) -> None:
        class TestApplication(cls): # type: ignore
            async def main(self) -> None:
                await super().main()

        app = TestApplication()
        with pytest.raises(NotImplementedError) as excinfo:
            app.run()


    @pytest.mark.parametrize("return_value", [0, 1, 100])
    def test_return_value(
        self,
        cls: type[Application],
        return_value: int
    ) -> None:
        class TestApplication(cls): # type: ignore
            async def main(self) -> int:
                return return_value

        app = TestApplication()
        assert app.run() == return_value
        assert app.run() == return_value


    @pytest.mark.parametrize("exception", [
        Exception("test"),
        KeyboardInterrupt(),
        RuntimeError("test"),
    ])
    def test_error_in_main(
        self,
        cls: type[Application],
        exception: BaseException
    ) -> None:
        class TestApplication(cls): # type: ignore
            async def main(self) -> None:
                raise exception

        app = TestApplication()
        with pytest.raises(BaseException) as excinfo:
            app.run()
        assert excinfo.value is exception


    def test_await_event(self, cls: type[Application]) -> None:
        class TestEvent(Event):
            text: str

        class TestApplication(cls): # type: ignore
            async def main(self) -> str:
                event = await TestEvent
                return event.text

            async def poll(self) -> Optional[Event]:
                return TestEvent("test")

        app = TestApplication()
        assert app.run() == "test"


    def test_start_end(
        self,
        cls: type[Application],
        bound_start_event_cls: type[BoundApplicationStart],
        bound_end_event_cls: type[BoundApplicationEnd],
    ) -> None:
        order: list[int] = []

        async def start(event: BoundApplicationStart) -> None:
            assert isinstance(event, bound_start_event_cls)
            order.append(1)

        class TestApplication(cls): # type: ignore
            async def main(self) -> None:
                order.append(2)

        async def end(event: BoundApplicationEnd) -> None:
            assert isinstance(event, bound_end_event_cls)
            order.append(3)

        with (
            Bind.on(bound_start_event_cls, start),
            Bind.on(bound_end_event_cls, end)
        ):
            TestApplication().run()

        assert order == [1, 2, 3]
