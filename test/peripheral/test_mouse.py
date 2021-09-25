
# gamut
from .test_peripheral import TestPeripheral
# gamut
from gamut import Application, Window
from gamut.peripheral import (Mouse, MouseButton, MouseButtonPressed,
                              MouseButtonReleased, MouseConnected,
                              MouseDisconnected, MouseMoved,
                              MouseScrolledHorizontally,
                              MouseScrolledVertically, PressableMouseButton)
# python
import ctypes
from typing import Optional, Union
# pysdl2
from sdl2 import (SDL_BUTTON_LEFT, SDL_BUTTON_MIDDLE, SDL_BUTTON_RIGHT,
                  SDL_BUTTON_X1, SDL_BUTTON_X2, SDL_Event, SDL_GetWindowID,
                  SDL_MOUSEBUTTONDOWN, SDL_MOUSEBUTTONUP, SDL_MOUSEMOTION,
                  SDL_MOUSEWHEEL, SDL_MOUSEWHEEL_FLIPPED, SDL_PushEvent,
                  SDL_WINDOWEVENT, SDL_WINDOWEVENT_LEAVE)
# pytest
import pytest


def send_sdl_mouse_motion_event(window: Window, x: int, y: int) -> None:
    sdl_event = SDL_Event()
    sdl_event.type = SDL_MOUSEMOTION
    sdl_event.motion.which = 0
    sdl_event.motion.windowID = SDL_GetWindowID(window._sdl)
    sdl_event.motion.x = x
    sdl_event.motion.y = y
    SDL_PushEvent(ctypes.byref(sdl_event))


def send_sdl_mouse_wheel_event(
    window: Window,
    x: int = 0, y: int = 0,
    flipped: bool = False
) -> None:
    sdl_event = SDL_Event()
    sdl_event.type = SDL_MOUSEWHEEL
    sdl_event.wheel.which = 0
    sdl_event.wheel.direction = SDL_MOUSEWHEEL_FLIPPED if flipped else 0
    sdl_event.wheel.windowID = SDL_GetWindowID(window._sdl)
    sdl_event.wheel.x = -x if flipped else x
    sdl_event.wheel.y = -y if flipped else y
    SDL_PushEvent(ctypes.byref(sdl_event))


def send_sdl_mouse_button_event(sdl_button: int, pressed: bool) -> None:
    sdl_event = SDL_Event()
    sdl_event.type = SDL_MOUSEBUTTONDOWN if pressed else SDL_MOUSEBUTTONUP
    sdl_event.button.button = sdl_button
    sdl_event.button.which = 0
    SDL_PushEvent(ctypes.byref(sdl_event))


def send_sdl_window_leave_event() -> None:
    sdl_event = SDL_Event()
    sdl_event.type = SDL_WINDOWEVENT
    sdl_event.window.event = SDL_WINDOWEVENT_LEAVE
    SDL_PushEvent(ctypes.byref(sdl_event))


class TestMouse(TestPeripheral):

    @pytest.fixture
    def cls(self) -> type[Mouse]:
        return Mouse

    @pytest.fixture
    def connected_event(self) -> type[MouseConnected]:
        return MouseConnected

    @pytest.fixture
    def disconnected_event(self) -> type[MouseDisconnected]:
        return MouseDisconnected


def test_defaults() -> None:
    mouse = Mouse('test')
    assert mouse.position is None
    assert mouse.window is None
    assert mouse.Button.left.is_pressed is False
    assert mouse.Button.middle.is_pressed is False
    assert mouse.Button.right.is_pressed is False
    assert mouse.Button.front.is_pressed is False
    assert mouse.Button.back.is_pressed is False


@pytest.mark.parametrize("name", ['', 'test', 'Primary'])
def test_repr(name: str) -> None:
    mouse = Mouse(name)
    assert repr(mouse) == f'<gamut.peripheral.Mouse {name!r}>'


@pytest.mark.parametrize("name", ['left', 'middle', 'right', 'front', 'back'])
def test_non_instance_button_repr(name: str) -> None:
    button: MouseButton = getattr(MouseButton, name)
    assert isinstance(button, MouseButton)
    assert repr(button) == f'<gamut.peripheral.MouseButton {name!r}>'


@pytest.mark.parametrize("name", ['left', 'middle', 'right', 'front', 'back'])
def test_instance_button_repr(name: str) -> None:
    mouse = Mouse('test')
    button: PressableMouseButton = getattr(mouse.Button, name)
    assert isinstance(button, PressableMouseButton)
    assert repr(button) == (
        f'<gamut.peripheral.MouseButton {name!r} for {mouse!r}>'
    )


@pytest.mark.parametrize("name", ['left', 'middle', 'right', 'front', 'back'])
def test_button_name(name: str) -> None:
    mouse = Mouse('test')
    button: PressableMouseButton = getattr(mouse.Button, name)
    assert isinstance(button, PressableMouseButton)
    assert button.name == name


@pytest.mark.parametrize("x", [0, 20, 80, 100])
@pytest.mark.parametrize("y", [0, 20, 80, 100])
def test_poll_motion_event(x: int, y: int) -> None:
    window = Window()
    moved_event: Optional[MouseMoved] = None

    class TestApplication(Application):
        async def main(self) -> None:
            nonlocal moved_event
            send_sdl_mouse_motion_event(window, x, y)
            moved_event = await self.mouse.Moved
            assert self.mouse.position == (x, y)
            assert self.mouse.window is window

    app = TestApplication()
    app.run()
    assert isinstance(moved_event, MouseMoved)
    assert moved_event.position == (x, y)
    assert moved_event.window is window


def test_poll_window_leave_event() -> None:
    window = Window()
    moved_event: Optional[MouseMoved] = None

    class TestApplication(Application):
        async def main(self) -> None:
            nonlocal moved_event
            send_sdl_mouse_motion_event(window, 1, 1)
            await self.mouse.Moved
            send_sdl_window_leave_event()
            moved_event = await self.mouse.Moved
            assert self.mouse.position is None
            assert self.mouse.window is None

    app = TestApplication()
    app.run()
    assert isinstance(moved_event, MouseMoved)
    assert moved_event.position is None
    assert moved_event.window is None


@pytest.mark.parametrize("x, y", [
    (-1, 0), (1, 0),
    (0, -1), (0, 1),
])
@pytest.mark.parametrize("multiplier", [1, 2, 5])
@pytest.mark.parametrize("flipped", [True, False])
def test_poll_scroll_event(
    x: int, y: int,
    multiplier: int,
    flipped: bool
) -> None:
    x *= multiplier
    y *= multiplier
    assert x == 0 or y == 0

    window = Window()
    scrolled_event: Optional[Union[
        MouseScrolledHorizontally,
        MouseScrolledVertically
    ]] = None

    class TestApplication(Application):
        async def main(self) -> None:
            nonlocal scrolled_event
            send_sdl_mouse_wheel_event(window, x=x, y=y, flipped=flipped)
            scrolled_event = await (
                self.mouse.ScrolledHorizontally |
                self.mouse.ScrolledVertically
            )

    app = TestApplication()
    app.run()
    if x:
        assert isinstance(scrolled_event, MouseScrolledHorizontally)
        assert scrolled_event.delta == x
    else:
        assert isinstance(scrolled_event, MouseScrolledVertically)
        assert scrolled_event.delta == y


@pytest.mark.parametrize("sdl_button, button_name", [
    (SDL_BUTTON_LEFT, 'left'),
    (SDL_BUTTON_MIDDLE, 'middle'),
    (SDL_BUTTON_RIGHT, 'right'),
    (SDL_BUTTON_X1, 'back'),
    (SDL_BUTTON_X2, 'front'),
])
def test_poll_button_down_event(sdl_button: int, button_name: str) -> None:
    window = Window()
    pressed_event: Optional[MouseButtonPressed] = None
    button: Optional[PressableMouseButton] = None

    class TestApplication(Application):
        async def main(self) -> None:
            nonlocal button
            nonlocal pressed_event
            button = getattr(self.mouse.Button, button_name)
            assert isinstance(button, PressableMouseButton)
            send_sdl_mouse_button_event(sdl_button, True)
            pressed_event = await button.Pressed
            assert pressed_event.button is button
            assert button.is_pressed

    app = TestApplication()
    app.run()
    assert isinstance(pressed_event, MouseButtonPressed)
    assert isinstance(button, PressableMouseButton)
    assert pressed_event.button is button
    assert pressed_event.is_pressed is True


@pytest.mark.parametrize("sdl_button, button_name", [
    (SDL_BUTTON_LEFT, 'left'),
    (SDL_BUTTON_MIDDLE, 'middle'),
    (SDL_BUTTON_RIGHT, 'right'),
    (SDL_BUTTON_X1, 'back'),
    (SDL_BUTTON_X2, 'front'),
])
def test_poll_button_up_event(sdl_button: int, button_name: str) -> None:
    window = Window()
    released_event: Optional[MouseButtonReleased] = None
    button: Optional[PressableMouseButton] = None

    class TestApplication(Application):
        async def main(self) -> None:
            nonlocal button
            nonlocal released_event
            button = getattr(self.mouse.Button, button_name)
            assert isinstance(button, PressableMouseButton)
            send_sdl_mouse_button_event(sdl_button, True)
            await button.Pressed
            send_sdl_mouse_button_event(sdl_button, False)
            released_event = await button.Released
            assert released_event.button is button
            assert not button.is_pressed

    app = TestApplication()
    app.run()
    assert isinstance(released_event, MouseButtonReleased)
    assert isinstance(button, PressableMouseButton)
    assert released_event.button is button
    assert released_event.is_pressed is False
