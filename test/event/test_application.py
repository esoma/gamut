
# gamut
from gamut.event import Application, Bind, Event
# python
import threading
import time
# pytest
import pytest


def test_instantiate_base_application() -> None:
    with pytest.raises(TypeError) as excinfo:
        Application() # type: ignore
    assert str(excinfo.value) == (
        'Can\'t instantiate abstract class Application with abstract method '
        'main'
    )


def test_base_main_call() -> None:
    class TestApplication(Application):
        async def main(self) -> None:
            await super().main()

    app = TestApplication()
    with pytest.raises(NotImplementedError) as excinfo:
        app.run()


@pytest.mark.parametrize("return_value", [0, 1, 100])
def test_return_value(return_value: int) -> None:
    class TestApplication(Application):
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
def test_error_in_main(exception: BaseException) -> None:
    class TestApplication(Application):
        async def main(self) -> None:
            raise exception

    app = TestApplication()
    with pytest.raises(BaseException) as excinfo:
        app.run()
    assert excinfo.value is exception


def test_await_event() -> None:
    class TestEvent(Event):
        text: str

    class TestApplication(Application):
        async def main(self) -> str:
            thread = threading.Thread(target=self.thread)
            thread.start()
            event = await TestEvent
            thread.join()
            return event.text

        def thread(self) -> None:
            time.sleep(.1)
            TestEvent("test").send()

    app = TestApplication()
    assert app.run() == "test"


def test_start_end() -> None:
    order: list[int] = []

    async def start(event: Application.Start) -> None:
        order.append(1)

    class TestApplication(Application):
        async def main(self) -> None:
            order.append(2)

    async def end(event: Application.End) -> None:
        order.append(3)

    with (
        Bind.on(TestApplication.Start, start),
        Bind.on(TestApplication.End, end)
    ):
        TestApplication().run()

    assert order == [1, 2, 3]
