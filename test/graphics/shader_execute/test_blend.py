
# gamut
from gamut.graphics import (BlendFactor, BlendFunction, Buffer, BufferView,
                            BufferViewMap, clear_render_target, execute_shader,
                            PrimitiveMode, read_color_from_render_target,
                            Shader, Texture2d, TextureComponents,
                            TextureRenderTarget, WindowRenderTarget)
from gamut.math import FVector2, FVector2Array, FVector3, FVector4, UVector2
# python
import ctypes
from typing import Final, Optional, Union
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
    blend_source: BlendFactor,
    blend_destination: BlendFactor,
    blend_source_alpha: Optional[BlendFactor],
    blend_destination_alpha: Optional[BlendFactor],
    blend_function: BlendFunction,
    blend_color: Optional[FVector4],
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
        blend_source=blend_source,
        blend_destination=blend_destination,
        blend_source_alpha=blend_source_alpha,
        blend_destination_alpha=blend_destination_alpha,
        blend_function=blend_function,
        blend_color=blend_color,
    )


def calculate_factor(
    factor: BlendFactor,
    source_color: FVector4,
    destination_color: FVector4,
    blend_color: FVector4
) -> FVector4:
    if factor == BlendFactor.ZERO:
        return FVector4(0)
    elif factor == BlendFactor.ONE:
        return FVector4(1)
    elif factor == BlendFactor.SOURCE_COLOR:
        return source_color
    elif factor == BlendFactor.ONE_MINUS_SOURCE_COLOR:
        return 1 - source_color
    elif factor == BlendFactor.DESTINATION_COLOR:
        return destination_color
    elif factor == BlendFactor.ONE_MINUS_DESTINATION_COLOR:
        return 1 - destination_color
    elif factor == BlendFactor.SOURCE_ALPHA:
        return FVector4(source_color.a)
    elif factor == BlendFactor.ONE_MINUS_SOURCE_ALPHA:
        return FVector4(1 - source_color.a)
    elif factor == BlendFactor.DESTINATION_ALPHA:
        return FVector4(destination_color.a)
    elif factor == BlendFactor.ONE_MINUS_DESTINATION_ALPHA:
        return FVector4(1 - destination_color.a)
    elif factor == BlendFactor.BLEND_COLOR:
        return blend_color
    elif factor == BlendFactor.ONE_MINUS_BLEND_COLOR:
        return 1 - blend_color
    elif factor == BlendFactor.BLEND_ALPHA:
        return blend_color.a
    elif factor == BlendFactor.ONE_MINUS_BLEND_ALPHA:
        return FVector4(1 - blend_color.a)
    assert False


@pytest.mark.parametrize("blend_source", list(BlendFactor))
@pytest.mark.parametrize("blend_destination", list(BlendFactor))
def test_source_destination_factors(
    blend_source: BlendFactor,
    blend_destination: BlendFactor,
) -> None:
    color = FVector4(.45, .3, .8, .333)
    clear_color = FVector4(.2, .5, .2, 1)
    blend_color = FVector4(.8, .7, .6, .5)

    texture = Texture2d(
        UVector2(10, 10),
        TextureComponents.RGBA, ctypes.c_uint8,
        b'\x00' * 10 * 10 * 4
    )
    render_target = TextureRenderTarget([texture])
    clear_render_target(render_target, color=clear_color.rgb)

    shader = Shader(vertex=VERTEX_SHADER, fragment=FRAGMENT_SHADER)

    draw_fullscreen_quad(
        render_target,
        shader,
        color,
        blend_source,
        blend_destination,
        None,
        None,
        BlendFunction.ADD,
        blend_color,
    )

    source_factor = calculate_factor(
        blend_source,
        color,
        clear_color,
        blend_color
    )
    destination_factor = calculate_factor(
        blend_destination,
        color,
        clear_color,
        blend_color
    )
    expected_color = (
        (color * source_factor) +
        (clear_color * destination_factor)
    ).clamp(0.0, 1.0)

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


@pytest.mark.parametrize("blend_source", list(BlendFactor))
@pytest.mark.parametrize("blend_destination", list(BlendFactor))
def test_source_destination_alpha_factors(
    blend_source: BlendFactor,
    blend_destination: BlendFactor,
) -> None:
    color = FVector4(.45, .3, .8, .333)
    clear_color = FVector4(.2, .5, .2, 1)
    blend_color = FVector4(.8, .7, .6, .5)

    texture = Texture2d(
        UVector2(10, 10),
        TextureComponents.RGBA, ctypes.c_uint8,
        b'\x00' * 10 * 10 * 4
    )
    render_target = TextureRenderTarget([texture])
    clear_render_target(render_target, color=clear_color.rgb)

    shader = Shader(vertex=VERTEX_SHADER, fragment=FRAGMENT_SHADER)

    draw_fullscreen_quad(
        render_target,
        shader,
        color,
        BlendFactor.ONE,
        BlendFactor.ONE,
        blend_source,
        blend_destination,
        BlendFunction.ADD,
        blend_color,
    )

    source_factor = calculate_factor(
        blend_source,
        color,
        clear_color,
        blend_color
    )
    destination_factor = calculate_factor(
        blend_destination,
        color,
        clear_color,
        blend_color
    )
    expected_color = (
        FVector4(
            color.r, color.g, color.b,
            color.a * source_factor[3]
        ) +
        FVector4(
            clear_color.r, clear_color.g, clear_color.b,
            clear_color.a * destination_factor[3]
        )
    ).clamp(0.0, 1.0)

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


@pytest.mark.parametrize("blend_function", list(BlendFunction))
def test_function(blend_function: BlendFunction,) -> None:
    color = FVector4(.45, .3, .8, .333)
    clear_color = FVector4(.2, .5, .2, 1)

    texture = Texture2d(
        UVector2(10, 10),
        TextureComponents.RGBA, ctypes.c_uint8,
        b'\x00' * 10 * 10 * 4
    )
    render_target = TextureRenderTarget([texture])
    clear_render_target(render_target, color=clear_color.rgb)

    shader = Shader(vertex=VERTEX_SHADER, fragment=FRAGMENT_SHADER)

    draw_fullscreen_quad(
        render_target,
        shader,
        color,
        BlendFactor.ONE,
        BlendFactor.ONE,
        None,
        None,
        blend_function,
        None,
    )

    source = color
    destination = clear_color
    if blend_function == BlendFunction.ADD:
        expected_color = source + destination
    elif blend_function == BlendFunction.SUBTRACT:
        expected_color = source - destination
    elif blend_function == BlendFunction.SUBTRACT_REVERSED:
        expected_color = destination - source
    elif blend_function == BlendFunction.MIN:
        expected_color = FVector4(*(
            min(s, d)
            for s, d in zip(source, destination)
        ))
    elif blend_function == BlendFunction.MAX:
        expected_color = FVector4(*(
            max(s, d)
            for s, d in zip(source, destination)
        ))
    expected_color = expected_color.clamp(0.0, 1.0)

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


def test_default_blend_color() -> None:
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
        FVector4(.5, .5, .5, 1),
        BlendFactor.BLEND_COLOR,
        BlendFactor.ZERO,
        None,
        None,
        BlendFunction.ADD,
        None,
    )
    expected_color = FVector4(.5, .5, .5, 1)
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
