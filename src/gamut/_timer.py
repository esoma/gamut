
__all__ = ['Timer', 'TimerExpired']

# gamut
from gamut.event import Event, EventLoop
# python
from datetime import datetime, timedelta
from threading import Thread
from time import sleep
from weakref import ref


class TimerExpired(Event):
    previous: datetime
    when: datetime


class Timer:

    def __init__(
        self,
        event_loop: EventLoop,
        duration: timedelta,
        event: type[TimerExpired],
        *,
        repeat: bool = False,
        fixed: bool = False,
    ) -> None:
        self._event_loop = ref(event_loop)
        self._duration = duration
        self._event = event
        self._repeat = repeat
        self._fixed = fixed
        self._thread = Thread(
            target=timer_thread_main,
            args=(ref(self), datetime.now())
        )
        self._thread.start()

    @property
    def duration(self) -> timedelta:
        return self._duration

    @property
    def event(self) -> type[TimerExpired]:
        return self._event

    @property
    def repeat(self) -> bool:
        return self._repeat

    @property
    def fixed(self) -> bool:
        return self._fixed

    def _send_event(self, event: TimerExpired) -> bool:
        event_loop = self._event_loop()
        if event_loop is None:
            return False
        event_loop.queue_event(event)
        return True


def timer_thread_main(weak_timer: ref[Timer], previous: datetime) -> None:
    timer = weak_timer()
    if timer is None:
        return
    timer_duration = timer.duration
    timer_repeat = timer.repeat
    timer_fixed = timer.fixed
    timer_event = timer.event
    del timer

    while True:
        timer = weak_timer()
        if timer is None:
            return
        now = datetime.now()
        difference = now - previous
        while difference >= timer_duration:
            when = now
            if timer_fixed:
                when = previous + timer_duration
            if not timer._send_event(timer_event(previous, when)):
                return
            if not timer_repeat:
                return
            previous = when
            assert previous <= now
            difference = now - previous
        del timer

        remaining_time = (previous + timer_duration) - datetime.now()
        if remaining_time > timedelta(microseconds=1):
            sleep(remaining_time.total_seconds())
