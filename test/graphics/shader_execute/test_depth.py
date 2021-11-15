
# gamut
from gamut.graphics import (Buffer, BufferView, BufferViewMap,
                            clear_render_target, Color, DepthTest,
                            execute_shader, PrimitiveMode,
                            read_color_from_render_target,
                            read_depth_from_render_target, Shader, Texture2d,
                            TextureComponents, TextureRenderTarget,
                            TextureRenderTargetDepthStencil,
                            WindowRenderTarget)
# python
from typing import Final, Union
# pyglm
import glm
# pytest
import pytest

VERTEX_SHADER: Final = b"""
#version 140
in vec2 xy;
uniform float depth;
void main()
{
    gl_Position = vec4(xy, depth, 1.0);
}
"""

FRAGMENT_SHADER: Final = b"""
#version 140
uniform vec4 color;
out vec4 FragColor;
void main()
{
    FragColor = color;
}
"""


def draw_fullscreen_quad(
    render_target: Union[TextureRenderTarget, WindowRenderTarget],
    shader: Shader,
    color: Color,
    depth: float,
    depth_test: DepthTest,
    depth_write: bool,
) -> None:
    execute_shader(
        render_target,
        shader,
        PrimitiveMode.TRIANGLE_FAN,
        BufferViewMap({
            "xy": BufferView(Buffer(glm.array(
                glm.vec2(-1, -1),
                glm.vec2(-1, 1),
                glm.vec2(1, 1),
                glm.vec2(1, -1),
            ).to_bytes()), glm.vec2)
        }), {
            "color": glm.vec4(*color),
            "depth": glm.float32(depth),
        },
        index_range=(0, 4),
        depth_test=depth_test,
        depth_write=depth_write,
    )


@pytest.mark.parametrize("depth_test, depth_write", [
    (DepthTest.ALWAYS, True),
    (DepthTest.LESS, False),
    (DepthTest.LESS, True),
    (DepthTest.LESS_EQUAL, False),
    (DepthTest.LESS_EQUAL, True),
    (DepthTest.GREATER, False),
    (DepthTest.GREATER, True),
    (DepthTest.GREATER_EQUAL, False),
    (DepthTest.GREATER_EQUAL, True),
    (DepthTest.EQUAL, False),
    (DepthTest.EQUAL, True),
    (DepthTest.NOT_EQUAL, False),
    (DepthTest.NOT_EQUAL, True),
])
def test_no_depth_buffer_fail(
    depth_test: DepthTest,
    depth_write: bool
) -> None:
    texture = Texture2d(
        10, 10,
        TextureComponents.RGBA, glm.uint8,
        b'\x00' * 10 * 10 * 4
    )
    render_target = TextureRenderTarget(
        [texture],
        TextureRenderTargetDepthStencil.NONE
    )
    shader = Shader(vertex=VERTEX_SHADER, fragment=FRAGMENT_SHADER)
    with pytest.raises(ValueError) as excinfo:
        draw_fullscreen_quad(
            render_target,
            shader,
            Color(1, 1, 1),
            1.0,
            depth_test,
            depth_write,
        )
    assert str(excinfo.value) == (
        f'cannot execute shader with {depth_test=} and {depth_write=} on '
        f'TextureRenderTarget without a depth buffer'
    )


@pytest.mark.parametrize("depth_test, depth_write, expected_color", [
    (DepthTest.ALWAYS, False, Color(1, 1, 1)),
    (DepthTest.NEVER, True, Color(0, 0, 0)),
    (DepthTest.NEVER, True, Color(0, 0, 0)),
])
def test_no_depth_buffer_okay(
    depth_test: DepthTest,
    depth_write: bool,
    expected_color: Color
) -> None:
    texture = Texture2d(
        10, 10,
        TextureComponents.RGBA, glm.uint8,
        b'\x00' * 10 * 10 * 4
    )
    render_target = TextureRenderTarget(
        [texture],
        TextureRenderTargetDepthStencil.NONE
    )
    clear_render_target(render_target, color=Color(0, 0, 0))

    shader = Shader(vertex=VERTEX_SHADER, fragment=FRAGMENT_SHADER)
    draw_fullscreen_quad(
        render_target,
        shader,
        Color(1, 1, 1),
        1.0,
        depth_test,
        depth_write,
    )

    colors = read_color_from_render_target(
        render_target,
        0, 0,
        *render_target.size
    )
    assert all(c == expected_color for row in colors for c in row)


@pytest.mark.parametrize(
    "depth_test, depth_write, expected_color, expected_depth", [
    (DepthTest.ALWAYS, False, Color(0, 0, 1), 0.0),
    (DepthTest.ALWAYS, True, Color(0, 0, 1), -.5),
    (DepthTest.NEVER, False, Color(0, 0, 0), 0.0),
    (DepthTest.NEVER, True, Color(0, 0, 0), 0.0),
    (DepthTest.LESS, False, Color(0, 0, 1), 0.0),
    (DepthTest.LESS, True, Color(1, 1, 0), -.75),
    (DepthTest.LESS_EQUAL, False, Color(0, 0, 1), 0.0),
    (DepthTest.LESS_EQUAL, True, Color(0, 1, 1), -.75),
    (DepthTest.GREATER, False, Color(0, 1, 0), 0.0),
    (DepthTest.GREATER, True, Color(1, 1, 1), 1.0),
    (DepthTest.GREATER_EQUAL, False, Color(.5, .5, .5), 0.0),
    (DepthTest.GREATER_EQUAL, True, Color(1, 0, 0), 1.0),
    (DepthTest.EQUAL, False, Color(.5, .5, .5), 0.0),
    (DepthTest.EQUAL, True, Color(.5, .5, .5), 0.0),
    (DepthTest.NOT_EQUAL, False, Color(0, 0, 1), 0.0),
    (DepthTest.NOT_EQUAL, True, Color(.1, .1, .1), -.5),
])
def test_basic(
    depth_test: DepthTest,
    depth_write: bool,
    expected_color: Color,
    expected_depth: float
) -> None:
    texture = Texture2d(
        10, 10,
        TextureComponents.RGBA, glm.uint8,
        b'\x00' * 10 * 10 * 4
    )
    render_target = TextureRenderTarget(
        [texture],
        TextureRenderTargetDepthStencil.DEPTH_STENCIL
    )
    clear_render_target(render_target, color=Color(0, 0, 0), depth=0)

    shader = Shader(vertex=VERTEX_SHADER, fragment=FRAGMENT_SHADER)

    def test_draw_fullscreen_quad(color: Color, depth: float) -> None:
        draw_fullscreen_quad(
            render_target,
            shader,
            color,
            depth,
            depth_test,
            depth_write
        )
    test_draw_fullscreen_quad(Color(1, 1, 1), 1)
    test_draw_fullscreen_quad(Color(1, 0, 0), 1)
    test_draw_fullscreen_quad(Color(0, 1, 0), .25)
    test_draw_fullscreen_quad(Color(.5, .5, .5), 0)
    test_draw_fullscreen_quad(Color(1, 1, 0), -.75)
    test_draw_fullscreen_quad(Color(0, 1, 1), -.75)
    test_draw_fullscreen_quad(Color(.1, .1, .1), -.5)
    test_draw_fullscreen_quad(Color(0, 0, 1), -.5)

    colors = read_color_from_render_target(
        render_target,
        0, 0,
        *render_target.size
    )
    assert all(
        c.red == pytest.approx(expected_color.red, abs=.01) and
        c.green == pytest.approx(expected_color.green, abs=.01) and
        c.blue == pytest.approx(expected_color.blue, abs=.01) and
        c.alpha == pytest.approx(expected_color.alpha, abs=.01)
        for row in colors
        for c in row
    )

    depths = read_depth_from_render_target(
        render_target,
        0, 0,
        *render_target.size
    )
    assert all(
        d == pytest.approx(expected_depth, abs=1e-6)
        for row in depths
        for d in row
    )
