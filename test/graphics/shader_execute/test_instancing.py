
# gamut
from gamut.graphics import (Buffer, BufferView, BufferViewMap,
                            clear_render_target, execute_shader, PrimitiveMode,
                            read_color_from_render_target, Shader, Texture2d,
                            TextureComponents, TextureRenderTarget,
                            WindowRenderTarget)
from gamut.math import (FVector2, FVector2Array, FVector3, FVector3Array,
                        FVector4, UVector2)
# python
import ctypes
from itertools import permutations
from typing import Final, Sequence, Union
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
    colors: Sequence[FVector3],
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
            )), FVector2),
            "instance_color": BufferView(Buffer(
                FVector3Array(*colors)
                if colors else b''
            ), FVector3, instancing_divisor=1),
        }), {
        },
        index_range=(0, 4),
        instances=len(colors)
    )


def test_negative_instances() -> None:
    texture = Texture2d(
        UVector2(10, 10),
        TextureComponents.RGBA, ctypes.c_uint8,
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
                "xy": BufferView(Buffer(), FVector2),
                "instance_color": BufferView(Buffer(), FVector3),
            }), {
            },
            index_range=(0, 4),
            instances=-1
        )
    assert str(excinfo.value) == 'instances must be 0 or more'


def test_zero_instances() -> None:
    texture = Texture2d(
        UVector2(10, 10),
        TextureComponents.RGBA, ctypes.c_uint8,
        b'\x00' * 10 * 10 * 4
    )
    render_target = TextureRenderTarget([texture])
    clear_render_target(render_target, color=FVector3(0, 0, 0))
    shader = Shader(vertex=VERTEX_SHADER, fragment=FRAGMENT_SHADER)
    draw_fullscreen_quads(render_target, shader, [])

    read_colors = read_color_from_render_target(
        render_target,
        0, 0,
        *render_target.size
    )
    assert all(
        c == FVector4(0, 0, 0, 1)
        for row in read_colors
        for c in row
    )


@pytest.mark.parametrize("colors", permutations([
    FVector3(1, 1, 1),
    FVector3(1, 0, 0),
    FVector3(0, 1, 0),
    FVector3(0, 0, 1),
]))
def test_basic(colors: Sequence[FVector3]) -> None:
    texture = Texture2d(
        UVector2(10, 10),
        TextureComponents.RGBA, ctypes.c_uint8,
        b'\x00' * 10 * 10 * 4
    )
    render_target = TextureRenderTarget([texture])
    clear_render_target(render_target, color=FVector3(0, 0, 0))

    shader = Shader(vertex=VERTEX_SHADER, fragment=FRAGMENT_SHADER)

    draw_fullscreen_quads(render_target, shader, colors)

    read_colors = read_color_from_render_target(
        render_target,
        0, 0,
        *render_target.size
    )
    assert all(
        c == FVector4(*colors[-1], 1)
        for row in read_colors
        for c in row
    )
