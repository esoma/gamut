
# gamut
# gamut
from gamut import Window
from gamut.graphics import (clear_render_target, Color,
                            read_color_from_render_target,
                            read_depth_from_render_target,
                            read_stencil_from_render_target, Texture2d,
                            TextureComponents, TextureDataType,
                            TextureRenderTarget,
                            TextureRenderTargetDepthStencil,
                            WindowRenderTarget)
# python
from typing import Union
# pytest
import pytest


def test_window_render_target() -> None:
    window = Window()
    render_target = WindowRenderTarget(window)
    assert render_target.window is window
    assert render_target.size == window.size
    assert render_target.is_open

    render_target.close()
    assert render_target.window is window
    assert render_target.size == window.size
    assert not render_target.is_open

    window.close()
    assert render_target.window is window
    with pytest.raises(RuntimeError) as excinfo:
        render_target.size
    assert str(excinfo.value) == 'window is closed'
    assert not render_target.is_open


@pytest.mark.parametrize(
    "depth_stencil",
    list(TextureRenderTargetDepthStencil)
)
def test_texture_render_target(
    depth_stencil: TextureRenderTargetDepthStencil
) -> None:
    texture = Texture2d(
        100, 100,
        TextureComponents.RGBA, TextureDataType.UNSIGNED_BYTE,
        b'\x00' * 100 * 100 * 4
    )
    render_target = TextureRenderTarget([texture], depth_stencil)

    assert len(render_target.colors) == 1
    assert render_target.colors[0] == texture
    assert render_target.depth_stencil == depth_stencil
    assert render_target.size == (100, 100)
    assert render_target.is_open

    render_target.close()
    assert len(render_target.colors) == 1
    assert render_target.colors[0] == texture
    assert render_target.depth_stencil == depth_stencil
    assert render_target.size == (100, 100)
    assert not render_target.is_open


def test_texture_render_target_no_colors() -> None:
    with pytest.raises(ValueError) as excinfo:
        TextureRenderTarget([])
    assert str(excinfo.value) == 'at least 1 color texture must be supplied'


@pytest.mark.parametrize("width, height", [
    [101, 100],
    [100, 101],
])
def test_texture_render_target_different_color_sizes(
    width: int,
    height: int
) -> None:
    texture1 = Texture2d(
        100, 100,
        TextureComponents.RGBA, TextureDataType.UNSIGNED_BYTE,
        b'\x00' * 100 * 100 * 4
    )
    texture2 = Texture2d(
        width, height,
        TextureComponents.RGBA, TextureDataType.UNSIGNED_BYTE,
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
            100, 100,
            TextureComponents.RGBA, TextureDataType.UNSIGNED_BYTE,
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
@pytest.mark.parametrize("stencil", [-1, 0, 1])
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
        pytest.approx(c.red, color[0]) and
        pytest.approx(c.blue, color[1]) and
        pytest.approx(c.green, color[2]) and
        c.alpha == 1.0
        for row in colors for c in row
    )

    depths = read_depth_from_render_target(
        render_target,
        0, 0,
        *render_target.size
    )
    assert all(pytest.approx(d, depth) for row in depths for d in row)

    stencils = read_stencil_from_render_target(
        render_target,
        0, 0,
        *render_target.size
    )
    assert all(pytest.approx(s, stencil) for row in stencils for s in row)
