
# gamut
from gamut.graphics import (Buffer, BufferView, BufferViewMap,
                            clear_render_target, Color, DepthTest,
                            execute_shader, PrimitiveMode, Shader,
                            ShaderExecutionResult, Texture2d,
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
in vec3 xyz;
void main()
{
    gl_Position = vec4(xyz, 1.0);
}
"""

FRAGMENT_SHADER: Final = b"""
#version 140
out vec4 FragColor;
void main()
{
    FragColor = vec4(1, 1, 1, 1);
}
"""


def draw_fullscreen_quad(
    render_target: Union[TextureRenderTarget, WindowRenderTarget],
    shader: Shader,
    z: float,
    depth_test: DepthTest,
    query_occluded: bool
) -> ShaderExecutionResult:
    xyz = [
        glm.vec3(-1, -1, z),
        glm.vec3(-1, 1, z),
        glm.vec3(1, 1, z),
        glm.vec3(1, -1, z),
    ]
    return execute_shader(
        render_target,
        shader,
        PrimitiveMode.TRIANGLE_FAN,
        BufferViewMap({
            "xyz": BufferView(Buffer(glm.array(xyz).to_bytes()), glm.vec3)
        }), {
        },
        index_range=(0, 4),
        depth_test=depth_test,
        query_occluded=query_occluded,
    )


def test_disabled() -> None:
    texture = Texture2d(
        (10, 10),
        TextureComponents.RGBA, glm.uint8,
        b'\x00' * 10 * 10 * 4
    )
    render_target = TextureRenderTarget([texture])

    shader = Shader(vertex=VERTEX_SHADER, fragment=FRAGMENT_SHADER)

    result = draw_fullscreen_quad(
        render_target,
        shader,
        0,
        DepthTest.ALWAYS,
        False
    )
    with pytest.raises(RuntimeError) as excinfo:
        result.occluded
    assert str(excinfo.value) == 'occlusion information not queried'


def test_enabled() -> None:
    texture = Texture2d(
        (10, 10),
        TextureComponents.RGBA, glm.uint8,
        b'\x00' * 10 * 10 * 4
    )
    render_target = TextureRenderTarget(
        [texture],
        TextureRenderTargetDepthStencil.DEPTH_STENCIL
    )
    clear_render_target(render_target, color=Color(0, 0, 0), depth=0)

    shader = Shader(vertex=VERTEX_SHADER, fragment=FRAGMENT_SHADER)

    result = draw_fullscreen_quad(
        render_target,
        shader,
        0,
        DepthTest.ALWAYS,
        True
    )
    assert result.occluded is False

    result = draw_fullscreen_quad(
        render_target,
        shader,
        0,
        DepthTest.NEVER,
        True
    )
    assert result.occluded is True
