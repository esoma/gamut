
# gamut
from gamut import Application, Window
from gamut.graphics import (Buffer, clear_render_target, Color,
                            read_color_from_render_target,
                            read_depth_from_render_target,
                            read_stencil_from_render_target, Texture2d,
                            TextureComponents, TextureRenderTarget,
                            TextureRenderTargetDepthStencil,
                            WindowRenderTarget)
from gamut.math import UVector2
# python
import ctypes
from ctypes import c_uint
from ctypes import sizeof as c_sizeof
import threading
from typing import Optional, Union
# pytest
import pytest


def test_window_render_target() -> None:
    window = Window()
    render_target = WindowRenderTarget(window)
    assert render_target.window is window
    assert render_target.size == UVector2(*window.size)
    assert render_target.is_open

    render_target.close()
    assert render_target.window is window
    assert render_target.size == UVector2(*window.size)
    assert not render_target.is_open

    window.close()
    assert render_target.window is window
    with pytest.raises(RuntimeError) as excinfo:
        render_target.size
    assert str(excinfo.value) == 'window is closed'
    assert not render_target.is_open


@pytest.mark.parametrize(
    "depth_stencil",
    [*TextureRenderTargetDepthStencil, None]
)
def test_texture_render_target(
    depth_stencil: Optional[TextureRenderTargetDepthStencil]
) -> None:
    texture = Texture2d(
        UVector2(100, 100),
        TextureComponents.RGBA, ctypes.c_uint8,
        b'\x00' * 100 * 100 * 4
    )
    actual_depth_stencil: Union[TextureRenderTargetDepthStencil, Texture2d] = (
        Texture2d(
            UVector2(100, 100),
            TextureComponents.DS, ctypes.c_uint32,
            b'\x00' * 100 * 100 * c_sizeof(c_uint)
        )
    )
    if depth_stencil is not None:
        actual_depth_stencil = depth_stencil

    render_target = TextureRenderTarget([texture], actual_depth_stencil)

    assert len(render_target.colors) == 1
    assert render_target.colors[0] == texture
    assert render_target.depth_stencil == actual_depth_stencil
    assert render_target.size == UVector2(100, 100)
    assert render_target.is_open

    render_target.close()
    assert len(render_target.colors) == 1
    assert render_target.colors[0] == texture
    assert render_target.depth_stencil == actual_depth_stencil
    assert render_target.size == UVector2(100, 100)
    assert not render_target.is_open


def test_texture_render_target_no_textures() -> None:
    with pytest.raises(ValueError) as excinfo:
        TextureRenderTarget([])
    assert str(excinfo.value) == 'at least 1 texture must be supplied'


@pytest.mark.parametrize("width, height", [
    [101, 100],
    [100, 101],
])
def test_texture_render_target_different_color_sizes(
    width: int,
    height: int
) -> None:
    texture1 = Texture2d(
        UVector2(100, 100),
        TextureComponents.RGBA, ctypes.c_uint8,
        b'\x00' * 100 * 100 * 4
    )
    texture2 = Texture2d(
        UVector2(width, height),
        TextureComponents.RGBA, ctypes.c_uint8,
        b'\x00' * width * height * 4
    )
    with pytest.raises(ValueError) as excinfo:
        TextureRenderTarget([texture1, texture2])
    assert str(excinfo.value) == 'all textures must have the same size'


def create_render_target(
    cls: Union[type[TextureRenderTarget], type[WindowRenderTarget]]
) -> Union[TextureRenderTarget, WindowRenderTarget]:
    if cls is TextureRenderTarget:
        texture = Texture2d(
            UVector2(100, 100),
            TextureComponents.RGBA, ctypes.c_uint8,
            b'\x00' * 100 * 100 * 4
        )
        return TextureRenderTarget(
            [texture],
            TextureRenderTargetDepthStencil.DEPTH_STENCIL
        )
    elif cls is WindowRenderTarget:
        return WindowRenderTarget(Window())
    raise NotImplementedError()


@pytest.mark.parametrize("cls", [TextureRenderTarget, WindowRenderTarget])
@pytest.mark.parametrize("color", [
    Color(0, 0, 0, 0),
    Color(.25, .4, .6, .8),
    Color(1, 1, 1, 1),
])
@pytest.mark.parametrize("depth", [-1.0, 0.0, 1.0])
@pytest.mark.parametrize("stencil", [0, 1])
def test_clear(
    cls: Union[type[TextureRenderTarget], type[WindowRenderTarget]],
    color: Color,
    depth: float,
    stencil: int,
) -> None:
    render_target = create_render_target(cls)
    clear_render_target(
        render_target,
        color=color,
        depth=depth,
        stencil=stencil
    )

    colors = read_color_from_render_target(
        render_target,
        0, 0,
        *render_target.size
    )
    assert all(
        c.red == pytest.approx(color[0], abs=.01) and
        c.green == pytest.approx(color[1], abs=.01) and
        c.blue == pytest.approx(color[2], abs=.01) and
        c.alpha == 1.0
        for row in colors for c in row
    )

    depths = read_depth_from_render_target(
        render_target,
        0, 0,
        *render_target.size
    )
    assert all(
        d == pytest.approx(depth, abs=.01)
        for row in depths for d in row
    )

    stencils = read_stencil_from_render_target(
        render_target,
        0, 0,
        *render_target.size
    )
    assert all(s == pytest.approx(stencil) for row in stencils for s in row)


@pytest.mark.parametrize("cls", [TextureRenderTarget, WindowRenderTarget])
def test_clear_closed(
    cls: Union[type[TextureRenderTarget], type[WindowRenderTarget]]
) -> None:
    render_target = create_render_target(cls)
    render_target.close()
    with pytest.raises(RuntimeError) as excinfo:
        clear_render_target(render_target)
    assert str(excinfo.value) == 'render target is closed'


def test_read_depth_from_render_target_no_depth_buffer() -> None:
    texture = Texture2d(
        UVector2(10, 10),
        TextureComponents.RGBA, ctypes.c_uint8,
        b'\x00' * 10 * 10 * 4
    )
    render_target = TextureRenderTarget(
        [texture],
        TextureRenderTargetDepthStencil.NONE
    )
    with pytest.raises(ValueError) as excinfo:
        read_depth_from_render_target(
            render_target,
            0, 0,
            *render_target.size
        )
    assert str(excinfo.value) == (
        'cannot read depth from a render target with no depth buffer'
    )

def test_clear_render_target_no_depth_buffer() -> None:
    texture = Texture2d(
        UVector2(10, 10),
        TextureComponents.RGBA, ctypes.c_uint8,
        b'\x00' * 10 * 10 * 4
    )
    render_target = TextureRenderTarget(
        [texture],
        TextureRenderTargetDepthStencil.NONE
    )
    with pytest.raises(ValueError) as excinfo:
        clear_render_target(render_target, depth=0.0)
    assert str(excinfo.value) == (
        'cannot clear depth on a render target with no depth buffer'
    )

@pytest.mark.parametrize("cls", [TextureRenderTarget, WindowRenderTarget])
def test_render_target_transfer_to_app(
    cls: Union[type[TextureRenderTarget], type[WindowRenderTarget]],
) -> None:
    render_target = create_render_target(cls)

    class App(Application):
        async def main(self) -> None:
            assert render_target.size.x >= 100
            assert render_target.size.y >= 100
            render_target.close()

    app = App()
    app.run()
    assert not render_target.is_open


@pytest.mark.parametrize("cls", [TextureRenderTarget, WindowRenderTarget])
def test_render_target_transfer_to_main(
    cls: Union[type[TextureRenderTarget], type[WindowRenderTarget]],
) -> None:
    render_target: Optional[Union[
        TextureRenderTarget,
        WindowRenderTarget
    ]] = None

    class App(Application):
        async def main(self) -> None:
            nonlocal render_target
            render_target = create_render_target(cls)

    app = App()
    app.run()

    assert render_target is not None
    assert render_target.size.x >= 100
    assert render_target.size.y >= 100
    render_target.close()
    assert not render_target.is_open


@pytest.mark.parametrize("cls", [TextureRenderTarget, WindowRenderTarget])
def test_render_target_thread_closed_outside_render_thread(
    cls: Union[type[TextureRenderTarget], type[WindowRenderTarget]],
) -> None:
    keep_alive_buffer = Buffer()
    render_target = create_render_target(cls)

    def thread_main() -> None:
        render_target.close()

    thread = threading.Thread(target=thread_main)
    thread.start()
    thread.join()

    assert not render_target.is_open
