
from __future__ import annotations

__all__ = [
    'Application',
    'ApplicationEnd',
    'ApplicationStart',
    'ApplicationEvent',
]

# gamut
from gamut._sdl import sdl_event_callback_map, SDL_KEYBOARD_KEY, SDL_MOUSE_KEY
from gamut.event import Bind
from gamut.event import Event as BaseEvent
from gamut.event import EventLoop, EventLoopEnd, EventLoopEvent, EventLoopStart
from gamut.peripheral import (Controller, Keyboard, KeyboardConnected, Mouse,
                              MouseConnected)
# python
from ctypes import byref as c_byref
from typing import Any, ContextManager, Optional, Sequence, TypeVar
# pysdl2
from sdl2 import (SDL_Event, SDL_GetError, SDL_Init, SDL_INIT_EVENTS,
                  SDL_INIT_JOYSTICK, SDL_PollEvent, SDL_QuitSubSystem,
                  SDL_WaitEvent)

R = TypeVar('R')


class ApplicationEvent(EventLoopEvent, event_loop=...):
    event_loop: Application[Any]

    @property
    def application(self) -> Application[Any]:
        return self.event_loop


class ApplicationStart(ApplicationEvent, EventLoopStart,
                            event_loop=...):
    pass


class ApplicationEnd(ApplicationEvent, EventLoopEnd,
                          event_loop=...):
    pass


class Application(EventLoop[R]):

    Event: type[ApplicationEvent]
    Start: type[ApplicationStart]
    End: type[ApplicationEnd]

    def __init__(self) -> None:
        super().__init__()
        class Event(ApplicationEvent, self.Event): # type: ignore
            pass
        self.Event = Event
        class Start( # type: ignore
            ApplicationStart,
            Event,
            self.Start, # type: ignore
        ):
            pass
        self.Start = Start
        class End( # type: ignore
            ApplicationEnd,
            Event,
            self.End # type: ignore
        ):
            pass
        self.End = End

        self._mouse_created: bool = False
        self._keyboard_created: bool = False

        self._mice: dict[Any, Mouse] = {}
        self._keyboards: dict[Any, Keyboard] = {}
        self._controllers: dict[Any, Controller] = {}

    def run_context(self) -> ContextManager:
        return ApplicationRunContext((
            Bind.on(MouseConnected, self._register_mouse),
            Bind.on(KeyboardConnected, self._register_keyboard),
            Bind.on(self.End, self._disconnect_peripherals),
        ))

    async def poll(self, block: bool = True) -> Optional[BaseEvent]:
        event = await super().poll()
        if event:
            return event
        if not self._mouse_created:
            self._mouse_created = True
            mouse = Mouse('primary')
            return mouse.connect()
        if not self._keyboard_created:
            self._keyboard_created = True
            keyboard = Keyboard('primary')
            return keyboard.connect()
        return self._poll_sdl(block=block)

    @property
    def controllers(self) -> Sequence[Controller]:
        return tuple(self._controllers.values())

    @property
    def mice(self) -> Sequence[Mouse]:
        return tuple(self._mice.values())

    @property
    def keyboards(self) -> Sequence[Keyboard]:
        return tuple(self._keyboards.values())

    def _poll_sdl(self, block: bool) -> Optional[BaseEvent]:
        event = SDL_Event()
        if block:
            if SDL_WaitEvent(c_byref(event)) != 1:
                raise RuntimeError(SDL_GetError().decode('utf8'))
        else:
            if SDL_PollEvent(c_byref(event)) != 1:
                return None
        try:
            callback = sdl_event_callback_map[event.type]
        except KeyError:
            return None
        return callback(event, self._mice, self._keyboards, self._controllers)

    async def _disconnect_peripherals(
        self,
        event: ApplicationStart
    ) -> None:
        for keyboard in self._keyboards.values():
            keyboard.disconnect().send()
        self._keyboards = {}
        self._keyboard_created = False

        for mouse in self._mice.values():
            mouse.disconnect().send()
        self._mice = {}
        self._mouse_created = False

        for controller in self._controllers.values():
            controller.disconnect().send()
        self._controllers = {}

    async def _register_mouse(self, event: MouseConnected) -> None:
        if not self._mice:
            self._mice[SDL_MOUSE_KEY] = event.mouse

    async def _register_keyboard(self, event: KeyboardConnected) -> None:
        if not self._keyboards:
            self._keyboards[SDL_KEYBOARD_KEY] = event.keyboard


class ApplicationRunContext:

    def __init__(self, binds: tuple[Bind, ...]) -> None:
        self._binds = binds

    def __enter__(self) -> None:
        if SDL_Init(SDL_INIT_EVENTS | SDL_INIT_JOYSTICK) != 0:
            raise RuntimeError(SDL_GetError().decode('utf8'))
        for bind in self._binds:
            bind.__enter__()

    def __exit__(self, *args: Any) -> None:
        for bind in self._binds:
            bind.__exit__(*args)
        SDL_QuitSubSystem(SDL_INIT_EVENTS | SDL_INIT_JOYSTICK)
