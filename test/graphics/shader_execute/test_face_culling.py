
# gamut
from gamut.graphics import (Buffer, BufferView, BufferViewMap,
                            clear_render_target, execute_shader, FaceCull,
                            PrimitiveMode, read_color_from_render_target,
                            Shader, Texture2d, TextureComponents,
                            TextureRenderTarget, WindowRenderTarget)
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
    front: bool,
    face_cull: FaceCull
) -> None:
    xy = [
        FVector2(-1, -1),
        FVector2(-1, 1),
        FVector2(1, 1),
        FVector2(1, -1),
    ]
    execute_shader(
        render_target,
        shader,
        PrimitiveMode.TRIANGLE_FAN,
        BufferViewMap({
            "xy": BufferView(Buffer(FVector2Array(
                *(reversed(xy) if front else xy)
            )), FVector2)
        }), {
            "color": color,
        },
        index_range=(0, 4),
        face_cull=face_cull
    )


@pytest.mark.parametrize("face_cull, expected_color", [
    (FaceCull.NONE, FVector4(0, 0, 1, 1)),
    (FaceCull.FRONT, FVector4(0, 1, 0, 1)),
    (FaceCull.BACK, FVector4(0, 0, 1, 1)),
])
def test_basic(face_cull: FaceCull, expected_color: FVector3) -> None:
    texture = Texture2d(
        UVector2(10, 10),
        TextureComponents.RGBA, ctypes.c_uint8,
        b'\x00' * 10 * 10 * 4
    )
    render_target = TextureRenderTarget([texture])
    clear_render_target(render_target, color=FVector3(0, 0, 0))

    shader = Shader(vertex=VERTEX_SHADER, fragment=FRAGMENT_SHADER)

    def test_draw_fullscreen_quad(
        color: FVector4,
        front: bool,
        face_cull: FaceCull
    ) -> None:
        draw_fullscreen_quad(
            render_target,
            shader,
            color,
            front,
            face_cull,
        )
    test_draw_fullscreen_quad(FVector4(1, 0, 0, 1), True, face_cull)
    test_draw_fullscreen_quad(FVector4(0, 1, 0, 1), False, face_cull)
    test_draw_fullscreen_quad(FVector4(0, 0, 1, 1), True, face_cull)

    colors = read_color_from_render_target(
        render_target,
        0, 0,
        *render_target.size
    )
    assert all(c == expected_color for row in colors for c in row)
