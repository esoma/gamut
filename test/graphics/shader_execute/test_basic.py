
# gamut
from gamut import Window
from gamut.graphics import (Buffer, BufferView, BufferViewMap,
                            clear_render_target, Color, execute_shader,
                            PrimitiveMode, read_color_from_render_target,
                            Shader, Texture2d, TextureComponents,
                            TextureRenderTarget,
                            TextureRenderTargetDepthStencil,
                            WindowRenderTarget)
# python
from pathlib import Path
from typing import Optional, Union
# pyglm
import glm
# pytest
import pytest

DIR = Path(__file__).parent


def create_render_target(
    cls: Union[type[TextureRenderTarget], type[WindowRenderTarget]]
) -> Union[TextureRenderTarget, WindowRenderTarget]:
    if cls is TextureRenderTarget:
        texture = Texture2d(
            10, 10,
            TextureComponents.RGBA, glm.uint8,
            b'\x00' * 10 * 10 * 4
        )
        return TextureRenderTarget(
            [texture],
            TextureRenderTargetDepthStencil.DEPTH_STENCIL
        )
    elif cls is WindowRenderTarget:
        window = Window()
        window.is_bordered = False
        window.resize(10, 10)
        return WindowRenderTarget(window)
    raise NotImplementedError()


@pytest.mark.parametrize("cls", [TextureRenderTarget, WindowRenderTarget])
def test_not_a_uniform(
    cls: Union[type[TextureRenderTarget], type[WindowRenderTarget]],
) -> None:
    render_target = create_render_target(cls)
    shader = Shader(
        vertex=b"""
        #version 140
        in vec2 xy;
        void main()
        {
            gl_Position = vec4(xy, 0, 1.0);
        }
        """,
    )
    with pytest.raises(ValueError) as excinfo:
        execute_shader(
            render_target,
            shader,
            PrimitiveMode.POINT,
            BufferViewMap({
                "xy": BufferView(Buffer(glm.array(
                    glm.vec2(-.9, -.9),
                    glm.vec2(-.9, .9),
                    glm.vec2(.9, .9),
                    glm.vec2(.9, -.9),
                ).to_bytes()), glm.vec2)
            }), {
                "color": glm.vec4()
            },
            index_range=(0, 4),
        )
    assert str(excinfo.value) == (
        'shader does not accept a uniform called "color"'
    )


@pytest.mark.parametrize("cls", [TextureRenderTarget, WindowRenderTarget])
def test_missing_uniform(
    cls: Union[type[TextureRenderTarget], type[WindowRenderTarget]],
) -> None:
    render_target = create_render_target(cls)
    shader = Shader(
        vertex=b"""
        #version 140
        in vec2 xy;
        uniform float z;
        void main()
        {
            gl_Position = vec4(xy, z, 1.0);
        }
        """,
    )
    with pytest.raises(ValueError) as excinfo:
        execute_shader(
            render_target,
            shader,
            PrimitiveMode.POINT,
            BufferViewMap({
                "xy": BufferView(Buffer(glm.array(
                    glm.vec2(-.9, -.9),
                    glm.vec2(-.9, .9),
                    glm.vec2(.9, .9),
                    glm.vec2(.9, -.9),
                ).to_bytes()), glm.vec2)
            }), {
            },
            index_range=(0, 4),
        )
    assert str(excinfo.value) == 'missing uniform: z'


@pytest.mark.parametrize("cls", [TextureRenderTarget, WindowRenderTarget])
def test_missing_attribute(
    cls: Union[type[TextureRenderTarget], type[WindowRenderTarget]],
) -> None:
    render_target = create_render_target(cls)
    shader = Shader(
        vertex=b"""
        #version 140
        in vec2 xy;
        in float z;
        void main()
        {
            gl_Position = vec4(xy, z, 1.0);
        }
        """,
    )
    with pytest.raises(ValueError) as excinfo:
        execute_shader(
            render_target,
            shader,
            PrimitiveMode.POINT,
            BufferViewMap({
                "xy": BufferView(Buffer(glm.array(
                    glm.vec2(-.9, -.9),
                    glm.vec2(-.9, .9),
                    glm.vec2(.9, .9),
                    glm.vec2(.9, -.9),
                ).to_bytes()), glm.vec2)
            }), {
            },
            index_range=(0, 4),
        )
    assert str(excinfo.value) == 'missing attribute: z'


@pytest.mark.parametrize("cls", [TextureRenderTarget, WindowRenderTarget])
@pytest.mark.parametrize("primitive_mode", list(PrimitiveMode))
@pytest.mark.parametrize("color", [
    Color(1, 1, 1),
    Color(1, 0, 0),
    Color(0, 1, 0),
    Color(0, 0, 1),
])
@pytest.mark.parametrize("index_key", ["index_range", "index_buffer_view"])
def test_basic(
    cls: Union[type[TextureRenderTarget], type[WindowRenderTarget]],
    primitive_mode: PrimitiveMode,
    color: Color,
    index_key: str,
) -> None:
    render_target = create_render_target(cls)
    clear_render_target(render_target, color=Color(0, 0, 0, 0))

    index_range: Optional[tuple[int, int]] = None
    index_buffer_view: Optional[BufferView[glm.uint32]] = None
    if index_key == "index_range":
        index_range = (0, 4)
    else:
        index_buffer_view = BufferView(Buffer(glm.array.from_numbers(
            glm.uint32,
            0, 1, 2, 3,
        ).to_bytes()), glm.uint32)

    shader = Shader(
        vertex=b"""
        #version 140
        in vec2 xy;
        void main()
        {
            gl_Position = vec4(xy, 0, 1.0);
        }
        """,
        fragment=b"""
        #version 140
        uniform vec4 color;
        out vec4 FragColor;
        void main()
        {
            FragColor = color;
        }
        """
    )
    execute_shader( # type: ignore
        render_target,
        shader,
        primitive_mode,
        BufferViewMap({
            "xy": BufferView(Buffer(glm.array(
                glm.vec2(-.9, -.9),
                glm.vec2(-.9, .9),
                glm.vec2(.9, .9),
                glm.vec2(.9, -.9),
            ).to_bytes()), glm.vec2)
        }), {
            "color": glm.vec4(*color)
        },
        index_range=index_range,
        index_buffer_view=index_buffer_view
    )

    colors = read_color_from_render_target(
        render_target,
        0, 0,
        *render_target.size
    )
    assert color in [c for row in colors for c in row]


@pytest.mark.parametrize("cls", [TextureRenderTarget, WindowRenderTarget])
def test_index_buffer_view_invalid_type(
    cls: Union[type[TextureRenderTarget], type[WindowRenderTarget]]
) -> None:
    render_target = create_render_target(cls)
    shader = Shader(
        vertex=b"""
        #version 140
        void main()
        {
            gl_Position = vec4(0, 0, 0, 1);
        }
        """
    )
    index_buffer_view = BufferView(Buffer(), glm.int32)
    with pytest.raises(ValueError) as excinfo:
        execute_shader(
            render_target,
            shader,
            PrimitiveMode.POINT,
            BufferViewMap({
            }), {
            },
            index_buffer_view=index_buffer_view # type: ignore
        )
    assert str(excinfo.value) == (
        f'view buffer with type {glm.int32} cannot be used for indexing'
    )


@pytest.mark.parametrize("cls", [TextureRenderTarget, WindowRenderTarget])
def test_index_buffer_view_different_stride(
    cls: Union[type[TextureRenderTarget], type[WindowRenderTarget]]
) -> None:
    render_target = create_render_target(cls)
    shader = Shader(
        vertex=b"""
        #version 140
        void main()
        {
            gl_Position = vec4(0, 0, 0, 1);
        }
        """
    )
    index_buffer_view = BufferView(Buffer(), glm.uint32, stride=1)
    with pytest.raises(ValueError) as excinfo:
        execute_shader(
            render_target,
            shader,
            PrimitiveMode.POINT,
            BufferViewMap({
            }), {
            },
            index_buffer_view=index_buffer_view
        )
    assert str(excinfo.value) == (
        f'view buffer with a stride different from its type cannot be used '
        f'for indexing'
    )

@pytest.mark.parametrize("cls", [TextureRenderTarget, WindowRenderTarget])
def test_index_buffer_view_different_offset(
    cls: Union[type[TextureRenderTarget], type[WindowRenderTarget]]
) -> None:
    render_target = create_render_target(cls)
    shader = Shader(
        vertex=b"""
        #version 140
        void main()
        {
            gl_Position = vec4(0, 0, 0, 1);
        }
        """
    )
    index_buffer_view = BufferView(Buffer(), glm.uint32, offset=1)
    with pytest.raises(ValueError) as excinfo:
        execute_shader(
            render_target,
            shader,
            PrimitiveMode.POINT,
            BufferViewMap({
            }), {
            },
            index_buffer_view=index_buffer_view
        )
    assert str(excinfo.value) == (
        f'view buffer with an offset other than 0 cannot be used for indexing'
    )


@pytest.mark.parametrize("cls", [TextureRenderTarget, WindowRenderTarget])
def test_index_buffer_view_with_instancing_divisor(
    cls: Union[type[TextureRenderTarget], type[WindowRenderTarget]]
) -> None:
    render_target = create_render_target(cls)
    shader = Shader(
        vertex=b"""
        #version 140
        void main()
        {
            gl_Position = vec4(0, 0, 0, 1);
        }
        """
    )
    index_buffer_view = BufferView(Buffer(), glm.uint32, instancing_divisor=1)
    with pytest.raises(ValueError) as excinfo:
        execute_shader(
            render_target,
            shader,
            PrimitiveMode.POINT,
            BufferViewMap({
            }), {
            },
            index_buffer_view=index_buffer_view
        )
    assert str(excinfo.value) == (
        f'view buffer with instancing_divisor cannot be used for indexing'
    )


@pytest.mark.parametrize("cls", [TextureRenderTarget, WindowRenderTarget])
def test_no_index(
    cls: Union[type[TextureRenderTarget], type[WindowRenderTarget]]
) -> None:
    render_target = create_render_target(cls)
    shader = Shader(
        vertex=b"""
        #version 140
        void main()
        {
            gl_Position = vec4(0, 0, 0, 1);
        }
        """
    )
    with pytest.raises(TypeError) as excinfo:
        execute_shader(
            render_target,
            shader,
            PrimitiveMode.POINT,
            BufferViewMap({
            }), {
            },
        )
    assert str(excinfo.value) == (
        f'index_buffer_view or index_range must be supplied'
    )


@pytest.mark.parametrize("cls", [TextureRenderTarget, WindowRenderTarget])
def test_both_index(
    cls: Union[type[TextureRenderTarget], type[WindowRenderTarget]]
) -> None:
    render_target = create_render_target(cls)
    shader = Shader(
        vertex=b"""
        #version 140
        void main()
        {
            gl_Position = vec4(0, 0, 0, 1);
        }
        """
    )
    with pytest.raises(TypeError) as excinfo:
        execute_shader( # type: ignore
            render_target,
            shader,
            PrimitiveMode.POINT,
            BufferViewMap({
            }), {
            },
            index_range=(0, 4),
            index_buffer_view=BufferView(Buffer(), glm.uint32),
        )
    assert str(excinfo.value) == (
        f'both index_buffer_view and index_range cannot be supplied'
    )
