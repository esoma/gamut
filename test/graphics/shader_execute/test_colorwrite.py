
# gamut
from gamut.graphics import (Buffer, BufferView, BufferViewMap,
                            clear_render_target, execute_shader, PrimitiveMode,
                            read_color_from_render_target, Shader, Texture2d,
                            TextureComponents, TextureRenderTarget,
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
void main()
{
    gl_Position = vec4(xy, 0.0, 1.0);
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
    color_write: tuple[bool, bool, bool, bool],
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
        },
        index_range=(0, 4),
        color_write=color_write,
    )


@pytest.mark.parametrize("red", [True, False])
@pytest.mark.parametrize("green", [True, False])
@pytest.mark.parametrize("blue", [True, False])
@pytest.mark.parametrize("alpha", [True, False])
def test_mask(red: bool, green: bool, blue: bool, alpha: bool) -> None:
    texture = Texture2d(
        UVector2(10, 10),
        TextureComponents.RGBA, ctypes.c_uint8,
        b'\x00' * 10 * 10 * 4
    )
    render_target = TextureRenderTarget([texture])
    clear_render_target(render_target, color=FVector3(0, 0, 0))

    shader = Shader(vertex=VERTEX_SHADER, fragment=FRAGMENT_SHADER)

    draw_fullscreen_quad(
        render_target,
        shader,
        FVector4(.2, .4, .6, .8),
        (red, green, blue, alpha)
    )

    expected_color = FVector4(
        .2 if red else 0,
        .4 if green else 0,
        .6 if blue else 0,
        .8 if alpha else 1
    )

    colors = read_color_from_render_target(
        render_target,
        0, 0,
        *render_target.size
    )

    assert all(
        c.r == pytest.approx(expected_color[0], abs=.01) and
        c.g == pytest.approx(expected_color[1], abs=.01) and
        c.b == pytest.approx(expected_color[2], abs=.01) and
        c.a == pytest.approx(expected_color[3], abs=.01)
        for row in colors
        for c in row
    )
