
# gamut
from gamut.graphics import (Buffer, BufferView, BufferViewMap,
                            clear_render_target, Color, execute_shader,
                            PrimitiveMode, read_color_from_render_target,
                            Shader, Texture2d, TextureComponents,
                            TextureRenderTarget, WindowRenderTarget)
# python
from typing import Final, Union
# pyglm
import glm
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
    color: Color,
    color_write: tuple[bool, bool, bool, bool],
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
        (10, 10),
        TextureComponents.RGBA, glm.uint8,
        b'\x00' * 10 * 10 * 4
    )
    render_target = TextureRenderTarget([texture])
    clear_render_target(render_target, color=Color(0, 0, 0))

    shader = Shader(vertex=VERTEX_SHADER, fragment=FRAGMENT_SHADER)

    draw_fullscreen_quad(
        render_target,
        shader,
        Color(.2, .4, .6, .8),
        (red, green, blue, alpha)
    )

    expected_color = glm.vec4(
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
        c.red == pytest.approx(expected_color[0], abs=.01) and
        c.green == pytest.approx(expected_color[1], abs=.01) and
        c.blue == pytest.approx(expected_color[2], abs=.01) and
        c.alpha == pytest.approx(expected_color[3], abs=.01)
        for row in colors
        for c in row
    )
