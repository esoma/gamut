
# gamut
from gamut.graphics import (Buffer, BufferView, BufferViewMap,
                            clear_render_target, DepthTest, execute_shader,
                            PrimitiveMode, read_color_from_render_target,
                            read_depth_from_render_target, Shader, Texture2d,
                            TextureComponents, TextureRenderTarget,
                            TextureRenderTargetDepthStencil,
                            WindowRenderTarget)
from gamut.math import FVector2, FVector2Array, FVector3, FVector4, UVector2
# python
import ctypes
from typing import Final, Union
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
    color: FVector4,
    depth: float,
    depth_test: DepthTest,
    depth_write: bool,
) -> None:
    execute_shader(
        render_target,
        shader,
        PrimitiveMode.TRIANGLE_FAN,
        BufferViewMap({
            "xy": BufferView(Buffer(FVector2Array(
                FVector2(-1, -1),
                FVector2(-1, 1),
                FVector2(1, 1),
                FVector2(1, -1),
            )), FVector2)
        }), {
            "color": color,
            "depth": ctypes.c_float(depth),
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
    (DepthTest.NEVER, False),
    (DepthTest.NEVER, True),
])
def test_no_depth_buffer_fail(
    depth_test: DepthTest,
    depth_write: bool
) -> None:
    texture = Texture2d(
        UVector2(10, 10),
        TextureComponents.RGBA, ctypes.c_uint8,
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
            FVector4(1),
            1.0,
            depth_test,
            depth_write,
        )
    assert str(excinfo.value) == (
        f'cannot execute shader with {depth_test=} and {depth_write=} on '
        f'TextureRenderTarget without a depth buffer'
    )


@pytest.mark.parametrize("depth_test, depth_write, expected_color", [
    (DepthTest.ALWAYS, False, FVector4(1)),
])
def test_no_depth_buffer_okay(
    depth_test: DepthTest,
    depth_write: bool,
    expected_color: FVector4
) -> None:
    texture = Texture2d(
        UVector2(10, 10),
        TextureComponents.RGBA, ctypes.c_uint8,
        b'\x00' * 10 * 10 * 4
    )
    render_target = TextureRenderTarget(
        [texture],
        TextureRenderTargetDepthStencil.NONE
    )
    clear_render_target(render_target, color=FVector3(0, 0, 0))

    shader = Shader(vertex=VERTEX_SHADER, fragment=FRAGMENT_SHADER)
    draw_fullscreen_quad(
        render_target,
        shader,
        FVector4(1, 1, 1, 1),
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
    (DepthTest.ALWAYS, False, FVector4(0, 0, 1, 1), 0.0),
    (DepthTest.ALWAYS, True, FVector4(0, 0, 1, 1), -.5),
    (DepthTest.NEVER, False, FVector4(0, 0, 0, 1), 0.0),
    (DepthTest.NEVER, True, FVector4(0, 0, 0, 1), 0.0),
    (DepthTest.LESS, False, FVector4(0, 0, 1, 1), 0.0),
    (DepthTest.LESS, True, FVector4(1, 1, 0, 1), -.75),
    (DepthTest.LESS_EQUAL, False, FVector4(0, 0, 1, 1), 0.0),
    (DepthTest.LESS_EQUAL, True, FVector4(0, 1, 1, 1), -.75),
    (DepthTest.GREATER, False, FVector4(0, 1, 0, 1), 0.0),
    (DepthTest.GREATER, True, FVector4(1, 1, 1, 1), 1.0),
    (DepthTest.GREATER_EQUAL, False, FVector4(.5, .5, .5, 1), 0.0),
    (DepthTest.GREATER_EQUAL, True, FVector4(1, 0, 0, 1), 1.0),
    (DepthTest.EQUAL, False, FVector4(.5, .5, .5, 1), 0.0),
    (DepthTest.EQUAL, True, FVector4(.5, .5, .5, 1), 0.0),
    (DepthTest.NOT_EQUAL, False, FVector4(0, 0, 1, 1), 0.0),
    (DepthTest.NOT_EQUAL, True, FVector4(.1, .1, .1, 1), -.5),
])
def test_basic(
    depth_test: DepthTest,
    depth_write: bool,
    expected_color: FVector4,
    expected_depth: float
) -> None:
    texture = Texture2d(
        UVector2(10, 10),
        TextureComponents.RGBA, ctypes.c_uint8,
        b'\x00' * 10 * 10 * 4
    )
    render_target = TextureRenderTarget(
        [texture],
        TextureRenderTargetDepthStencil.DEPTH_STENCIL
    )
    clear_render_target(render_target, color=FVector3(0, 0, 0), depth=0)

    shader = Shader(vertex=VERTEX_SHADER, fragment=FRAGMENT_SHADER)

    def test_draw_fullscreen_quad(color: FVector4, depth: float) -> None:
        draw_fullscreen_quad(
            render_target,
            shader,
            color,
            depth,
            depth_test,
            depth_write
        )
    test_draw_fullscreen_quad(FVector4(1, 1, 1, 1), 1)
    test_draw_fullscreen_quad(FVector4(1, 0, 0, 1), 1)
    test_draw_fullscreen_quad(FVector4(0, 1, 0, 1), .25)
    test_draw_fullscreen_quad(FVector4(.5, .5, .5, 1), 0)
    test_draw_fullscreen_quad(FVector4(1, 1, 0, 1), -.75)
    test_draw_fullscreen_quad(FVector4(0, 1, 1, 1), -.75)
    test_draw_fullscreen_quad(FVector4(.1, .1, .1, 1), -.5)
    test_draw_fullscreen_quad(FVector4(0, 0, 1, 1), -.5)

    colors = read_color_from_render_target(
        render_target,
        0, 0,
        *render_target.size
    )
    assert all(
        c.r == pytest.approx(expected_color.r, abs=.01) and
        c.g == pytest.approx(expected_color.g, abs=.01) and
        c.b == pytest.approx(expected_color.b, abs=.01) and
        c.a == pytest.approx(expected_color.a, abs=.01)
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
