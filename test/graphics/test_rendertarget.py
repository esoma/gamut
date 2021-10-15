
# gamut
from gamut import Window
from gamut.graphics import (clear_render_target, Color,
                            read_color_from_render_target,
                            read_depth_from_render_target,
                            read_stencil_from_render_target,
                            TextureRenderTarget, WindowRenderTarget)
# python
from typing import Union
# pytest
import pytest


def test_window_render_target() -> None:
    window = Window()
    render_target = WindowRenderTarget(window)
    assert render_target.window is window
    assert render_target.size == window.size

    colors = read_color_from_render_target(
        render_target,
        0, 0,
        *render_target.size
    )
    assert all(c == (0.0, 0.0, 0.0, 1.0) for row in colors for c in row)

    depths = read_depth_from_render_target(
        render_target,
        0, 0,
        *render_target.size
    )
    assert all(d == 0.0 for row in depths for d in row)

    stencils = read_stencil_from_render_target(
        render_target,
        0, 0,
        *render_target.size
    )
    assert all(s == 0 for row in stencils for s in row)

    window.close()
    assert render_target.window is window
    with pytest.raises(RuntimeError):
        render_target.size


def create_render_target(
    cls: Union[type[TextureRenderTarget], type[WindowRenderTarget]]
) -> Union[TextureRenderTarget, WindowRenderTarget]:
    if cls is TextureRenderTarget:
        return TextureRenderTarget()
    elif cls is WindowRenderTarget:
        return WindowRenderTarget(Window())
    raise NotImplementedError()


@pytest.mark.parametrize("cls", [WindowRenderTarget])
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