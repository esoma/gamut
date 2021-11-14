
# gamut
from gamut import Timer, TimerExpired
from gamut.event import Event, EventLoop
# python
from datetime import timedelta
import time
# pytest
import pytest


class CustomTimerExpired(TimerExpired):
    pass


@pytest.mark.parametrize("event_type", [TimerExpired, CustomTimerExpired])
def test_once(event_type: type[TimerExpired]) -> None:
    events: list[Event] = []

    class TestLoop(EventLoop):
        async def main(self) -> None:
            timer = Timer(self, timedelta(seconds=.1), event_type)
            time.sleep(1)

        def queue_event(self, event: Event) -> None:
            events.append(event)

    test_loop = TestLoop()
    test_loop.run()

    assert len(events) == 1
    timer_expired = events[0]
    assert isinstance(timer_expired, event_type)
    assert (
        (timer_expired.when - timer_expired.previous) >= timedelta(seconds=.1)
    )


@pytest.mark.parametrize("event_type", [TimerExpired, CustomTimerExpired])
def test_fixed(event_type: type[TimerExpired]) -> None:
    events: list[Event] = []

    class TestLoop(EventLoop):
        async def main(self) -> None:
            timer = Timer(self, timedelta(seconds=.1), event_type, fixed=True)
            time.sleep(1)

        def queue_event(self, event: Event) -> None:
            events.append(event)

    test_loop = TestLoop()
    test_loop.run()

    assert len(events) == 1
    timer_expired = events[0]
    assert isinstance(timer_expired, event_type)
    assert (
        (timer_expired.when - timer_expired.previous) == timedelta(seconds=.1)
    )


@pytest.mark.parametrize("event_type", [TimerExpired, CustomTimerExpired])
def test_repeat(event_type: type[TimerExpired]) -> None:
    events: list[Event] = []

    class TestLoop(EventLoop):
        async def main(self) -> None:
            timer = Timer(self, timedelta(seconds=.1), event_type, repeat=True)
            time.sleep(1)

        def queue_event(self, event: Event) -> None:
            events.append(event)

    test_loop = TestLoop()
    test_loop.run()

    assert len(events) > 1
    assert len(events) <= 10
    for timer_expired in events:
        assert isinstance(timer_expired, event_type)
        assert (
            (timer_expired.when - timer_expired.previous) >=
            timedelta(seconds=.1)
        )

@pytest.mark.parametrize("event_type", [TimerExpired, CustomTimerExpired])
def test_repeat_fixed(event_type: type[TimerExpired]) -> None:
    events: list[Event] = []

    class TestLoop(EventLoop):
        async def main(self) -> None:
            timer = Timer(
                self,
                timedelta(seconds=.1),
                event_type,
                repeat=True,
                fixed=True
            )
            time.sleep(1)

        def queue_event(self, event: Event) -> None:
            events.append(event)

    test_loop = TestLoop()
    test_loop.run()

    assert len(events) > 1
    assert len(events) <= 10
    for timer_expired in events:
        assert isinstance(timer_expired, event_type)
        assert (
            (timer_expired.when - timer_expired.previous) ==
            timedelta(seconds=.1)
        )
