
# gamut
from gamut.graphics import (Buffer, BufferView, BufferViewMap,
                            clear_render_target, Color, execute_shader,
                            PrimitiveMode, read_color_from_render_target,
                            Shader, Texture2d, TextureComponents,
                            TextureRenderTarget, WindowRenderTarget)
# python
from itertools import permutations
from typing import Final, Sequence, Union
# pyglm
import glm
# pytest
import pytest

VERTEX_SHADER: Final = b"""
#version 140
in vec2 xy;
in vec3 instance_color;
out vec3 vertex_color;
void main()
{
    vertex_color = instance_color;
    gl_Position = vec4(xy, 0.0, 1.0);
}
"""

FRAGMENT_SHADER: Final = b"""
#version 140
in vec3 vertex_color;
out vec4 FragColor;
void main()
{
    FragColor = vec4(vertex_color, 1);
}
"""


def draw_fullscreen_quads(
    render_target: Union[TextureRenderTarget, WindowRenderTarget],
    shader: Shader,
    colors: Sequence[Color],
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
            ).to_bytes()), glm.vec2),
            "instance_color": BufferView(Buffer(glm.array(*(
                glm.vec3(c.red, c.green, c.blue)
                for c in colors
            )).to_bytes() if colors else b''), glm.vec3, instancing_divisor=1),
        }), {
        },
        index_range=(0, 4),
        instances=len(colors)
    )


def test_negative_instances() -> None:
    texture = Texture2d(
        10, 10,
        TextureComponents.RGBA, glm.uint8,
        b'\x00' * 10 * 10 * 4
    )
    render_target = TextureRenderTarget([texture])
    shader = Shader(vertex=VERTEX_SHADER, fragment=FRAGMENT_SHADER)
    with pytest.raises(ValueError) as excinfo:
        execute_shader(
            render_target,
            shader,
            PrimitiveMode.TRIANGLE_FAN,
            BufferViewMap({
                "xy": BufferView(Buffer(), glm.vec2),
                "instance_color": BufferView(Buffer(), glm.vec3),
            }), {
            },
            index_range=(0, 4),
            instances=-1
        )
    assert str(excinfo.value) == 'instances must be 0 or more'


def test_zero_instances() -> None:
    texture = Texture2d(
        10, 10,
        TextureComponents.RGBA, glm.uint8,
        b'\x00' * 10 * 10 * 4
    )
    render_target = TextureRenderTarget([texture])
    clear_render_target(render_target, color=Color(0, 0, 0))
    shader = Shader(vertex=VERTEX_SHADER, fragment=FRAGMENT_SHADER)
    draw_fullscreen_quads(render_target, shader, [])

    read_colors = read_color_from_render_target(
        render_target,
        0, 0,
        *render_target.size
    )
    assert all(
        c == Color(0, 0, 0)
        for row in read_colors
        for c in row
    )


@pytest.mark.parametrize("colors", permutations([
    Color(1, 1, 1),
    Color(1, 0, 0),
    Color(0, 1, 0),
    Color(0, 0, 1),
]))
def test_basic(colors: Sequence[Color]) -> None:
    texture = Texture2d(
        10, 10,
        TextureComponents.RGBA, glm.uint8,
        b'\x00' * 10 * 10 * 4
    )
    render_target = TextureRenderTarget([texture])
    clear_render_target(render_target, color=Color(0, 0, 0))

    shader = Shader(vertex=VERTEX_SHADER, fragment=FRAGMENT_SHADER)

    draw_fullscreen_quads(render_target, shader, colors)

    read_colors = read_color_from_render_target(
        render_target,
        0, 0,
        *render_target.size
    )
    assert all(
        c == colors[-1]
        for row in read_colors
        for c in row
    )
