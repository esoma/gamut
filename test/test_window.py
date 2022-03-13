
# gamut
from gamut import (Application, Window, WindowBufferSynchronization,
                   WindowClose, WindowHidden, WindowMoved, WindowResized,
                   WindowShown)
from gamut.math import IVector2, UVector2
# python
import ctypes
from typing import Any, Optional
# pysdl2
from sdl2 import (SDL_Event, SDL_GetWindowID, SDL_PushEvent, SDL_WINDOWEVENT,
                  SDL_WINDOWEVENT_CLOSE, SDL_WINDOWEVENT_MOVED)
# pytest
import pytest


def send_sdl_window_event(
    window: Window,
    type: int,
    data1: int = 0,
    data2: int = 0
) -> None:
    sdl_event = SDL_Event()
    sdl_event.type = SDL_WINDOWEVENT
    sdl_event.window.event = type
    sdl_event.window.windowID = SDL_GetWindowID(window._sdl)
    sdl_event.window.data1 = data1
    sdl_event.window.data2 = data2
    SDL_PushEvent(ctypes.byref(sdl_event))


def test_defaults() -> None:
    window = Window()
    assert window.is_bordered is True
    assert window.is_fullscreen is False
    assert window.is_visible is False
    assert window.size.x >= 1
    assert window.size.y >= 1
    assert window.title == ''


@pytest.mark.parametrize("close_count", [1, 2, 5, 10])
def test_close(close_count: int) -> None:
    window = Window()
    for _ in range(close_count):
        window.close()
    with pytest.raises(RuntimeError) as excinfo:
        window.is_bordered
    assert str(excinfo.value) == 'window is closed'

    with pytest.raises(RuntimeError) as excinfo:
        window.is_bordered = False
    assert str(excinfo.value) == 'window is closed'

    with pytest.raises(RuntimeError) as excinfo:
        window.is_fullscreen
    assert str(excinfo.value) == 'window is closed'

    with pytest.raises(RuntimeError) as excinfo:
        window.is_fullscreen = True
    assert str(excinfo.value) == 'window is closed'

    with pytest.raises(RuntimeError) as excinfo:
        window.is_visible
    assert str(excinfo.value) == 'window is closed'

    with pytest.raises(RuntimeError) as excinfo:
        window.is_visible = True
    assert str(excinfo.value) == 'window is closed'

    with pytest.raises(RuntimeError) as excinfo:
        window.size
    assert str(excinfo.value) == 'window is closed'

    with pytest.raises(RuntimeError) as excinfo:
        window.resize((50, 50))
    assert str(excinfo.value) == 'window is closed'

    with pytest.raises(RuntimeError) as excinfo:
        window.title
    assert str(excinfo.value) == 'window is closed'

    with pytest.raises(RuntimeError) as excinfo:
        window.title = 'test'
    assert str(excinfo.value) == 'window is closed'

    with pytest.raises(RuntimeError) as excinfo:
        window.recenter()
    assert str(excinfo.value) == 'window is closed'


@pytest.mark.parametrize("title", ['', 'title', '試し'])
def test_repr(title: str) -> None:
    window = Window()
    window.title = title
    assert repr(window) == f'<gamut.Window \'{title}\'>'


def test_repr_closed() -> None:
    window = Window()
    window.close()
    assert repr(window) == f'<gamut.Window [closed]>'


@pytest.mark.parametrize("value", [
    True, False,
    0, 1,
    '', '123',
    object(),
    None,
])
def test_set_is_bordered(value: Any) -> None:
    window = Window()
    window.is_bordered = value
    assert window.is_bordered is bool(value)


def test_is_bordered_in_app() -> None:
    class TestApp(Application):
        async def main(self) -> None:
            window = Window()
            assert window.is_bordered
            window.is_bordered = False
    app = TestApp()
    app.run()


@pytest.mark.parametrize("value", [
    True, False,
    0, 1,
    '', '123',
    object(),
    None,
])
def test_set_is_fullscreen(value: Any) -> None:
    window = Window()
    window.is_fullscreen = value
    assert window.is_fullscreen is bool(value)


def test_is_fullscreen_in_app() -> None:
    class TestApp(Application):
        async def main(self) -> None:
            window = Window()
            assert not window.is_fullscreen
            window.is_fullscreen = True
    app = TestApp()
    app.run()


@pytest.mark.parametrize("value", [
    True, False,
    0, 1,
    '', '123',
    object(),
    None,
])
def test_set_is_visible(value: Any) -> None:
    window = Window()
    window.is_visible = value
    assert window.is_visible is bool(value)


def test_is_visible_in_app() -> None:
    class TestApp(Application):
        async def main(self) -> None:
            window = Window()
            assert not window.is_visible
            window.is_visible = True
    app = TestApp()
    app.run()


def test_recenter() -> None:
    window = Window()
    window.recenter()


def test_recenter_in_app() -> None:
    class TestApp(Application):
        async def main(self) -> None:
            window = Window()
            window.recenter()
    app = TestApp()
    app.run()


@pytest.mark.parametrize("x", [0, 1, 100, 1000])
@pytest.mark.parametrize("y", [0, 1, 100, 1000])
def test_resize(x: int, y: int) -> None:
    window = Window()
    window.resize(UVector2(x, y))
    assert window.size.x >= 1
    assert window.size.y >= 1
    assert len(window.size) == 2
    assert all(c.__class__ is int for c in window.size)


@pytest.mark.parametrize("size", [(1,), (1, 2), '123', None, '12'])
def test_resize_invalid_type(size: Any) -> None:
    window = Window()
    with pytest.raises(TypeError):
        window.resize(size)


def test_size_in_app() -> None:
    class TestApp(Application):
        async def main(self) -> None:
            window = Window()
            assert window.size != (0, 0)
    app = TestApp()
    app.run()


def test_resize_in_app() -> None:
    class TestApp(Application):
        async def main(self) -> None:
            window = Window()
            window.resize(UVector2(200, 200))
    app = TestApp()
    app.run()


@pytest.mark.parametrize("value", [
    '', 'hello world', '試し',
    b'', b'hello world', '試し'.encode('utf8'),
    100, 200,
    100.4, 200.6,
    None, object()
])
def test_set_title(value: Any) -> None:
    window = Window()
    window.title = value
    assert window.title == str(value)


def test_title_in_app() -> None:
    class TestApp(Application):
        async def main(self) -> None:
            window = Window()
            assert window.title == ''
            window.title = 'test'
    app = TestApp()
    app.run()


def test_poll_close_event() -> None:
    window = Window()
    close_event: Optional[WindowClose] = None

    class TestApp(Application):
        async def main(self) -> None:
            nonlocal close_event
            send_sdl_window_event(window, SDL_WINDOWEVENT_CLOSE)
            close_event = await window.Close
            window.close()

    app = TestApp()
    app.run()

    assert close_event is not None
    assert isinstance(close_event, WindowClose)
    assert close_event.window is window


def test_poll_hidden_event() -> None:
    window = Window()
    hidden_event: Optional[WindowHidden] = None

    class TestApp(Application):
        async def main(self) -> None:
            nonlocal hidden_event
            window.is_visible = True
            window.is_visible = False
            hidden_event = await window.Hidden
            window.close()

    app = TestApp()
    app.run()

    assert hidden_event is not None
    assert isinstance(hidden_event, WindowHidden)
    assert hidden_event.window is window


def test_poll_moved_event() -> None:
    window = Window()
    moved_event: Optional[WindowMoved] = None

    class TestApp(Application):
        async def main(self) -> None:
            nonlocal moved_event
            send_sdl_window_event(window, SDL_WINDOWEVENT_MOVED, 99, 49)
            moved_event = await window.Moved
            window.close()

    app = TestApp()
    app.run()

    assert moved_event is not None
    assert isinstance(moved_event, WindowMoved)
    assert moved_event.window is window
    assert isinstance(moved_event.position, IVector2)
    assert len(moved_event.position) == 2
    assert all(c.__class__ is int for c in moved_event.position)


def test_poll_resized_event() -> None:
    window = Window()
    resized_event: Optional[WindowResized] = None

    class TestApp(Application):
        async def main(self) -> None:
            nonlocal resized_event
            window.resize(UVector2(234, 156))
            resized_event = await window.Resized
            window.close()

    app = TestApp()
    app.run()

    assert resized_event is not None
    assert isinstance(resized_event, WindowResized)
    assert resized_event.window is window
    assert isinstance(resized_event.size, UVector2)
    assert all(c.__class__ is int for c in resized_event.size)


def test_poll_shown_event() -> None:
    window = Window()
    shown_event: Optional[WindowShown] = None

    class TestApp(Application):
        async def main(self) -> None:
            nonlocal shown_event
            window.is_visible = True
            shown_event = await window.Shown
            window.close()

    app = TestApp()
    app.run()

    assert shown_event is not None
    assert isinstance(shown_event, WindowShown)
    assert shown_event.window is window


def test_create_window_in_app_thread() -> None:
    class TestApp(Application):
        async def main(self) -> None:
            window = Window()
    app = TestApp()
    app.run()


@pytest.mark.parametrize("synchronization", list(WindowBufferSynchronization))
def test_flip_buffer(synchronization: WindowBufferSynchronization) -> None:
    window = Window()
    window.flip_buffer(synchronization)
