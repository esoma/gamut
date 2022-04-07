
# gamut
from gamut.graphics import (BlendFactor, BufferViewMap, clear_render_target,
                            Color, execute_shader, PrimitiveMode, Shader)
from gamut.math import FMatrix4, FVector3, FVector4
from gamut.text import AtlasFont, Face, RenderedGlyphFormat
# python
from typing import Final
# examples
from examplescommon import ExampleApplication, RESOURCES, run_application


class App(ExampleApplication):

    async def example_main(self) -> None:
        self.window.title = 'Gamut Text Example'

        self.ortho_projection = FMatrix4.orthographic(
            0, 800,
            0, 800,
            -1000, 1000
        )

        self.shader = Shader(vertex=VERTEX_SHADER, fragment=FRAGMENT_SHADER)
        face = Face(RESOURCES / 'OpenSans-Regular.ttf')
        font = AtlasFont(
            face.request_pixel_size(height=64),
            RenderedGlyphFormat.ALPHA
        )
        self.text_buffers = font.buffer_text('hello world')

    async def draw(self, step: ExampleApplication.Step) -> None:
        clear_render_target(
            self.window_render_target,
            color=Color(0, 0, 0),
        )
        # '3D' "hello world"
        for texture, (pos, uv) in self.text_buffers.items():
            execute_shader(
                self.window_render_target,
                self.shader,
                PrimitiveMode.TRIANGLE,
                BufferViewMap({
                    "pos": pos,
                    "uv": uv,
                }),
                {
                    "transform": (
                        self.camera.view_projection_transform @
                        FMatrix4(1).translate(
                            FVector3(-1.5, 1, -5),
                        ).scale(
                            FVector3(.01, .01, 1)
                        )
                    ),
                    "tex": texture,
                    "color": FVector4(.5, 1, 1, 1),
                },
                index_range=(0, len(pos)),
                blend_source=BlendFactor.SOURCE_ALPHA,
                blend_destination=BlendFactor.ONE_MINUS_SOURCE_ALPHA,
            )
        # orthographic "hello world"
        for texture, (pos, uv) in self.text_buffers.items():
            execute_shader(
                self.window_render_target,
                self.shader,
                PrimitiveMode.TRIANGLE,
                BufferViewMap({
                    "pos": pos,
                    "uv": uv,
                }),
                {
                    "transform": (
                        self.ortho_projection @
                        FMatrix4(1).translate(FVector3(0, 800, 0))
                    ),
                    "tex": texture,
                    "color": FVector4(1, 1, 1, 1),
                },
                index_range=(0, len(pos)),
                blend_source=BlendFactor.SOURCE_ALPHA,
                blend_destination=BlendFactor.ONE_MINUS_SOURCE_ALPHA,
            )

        self.window.flip_buffer()


VERTEX_SHADER: Final = b"""
#version 140
in vec4 pos;
in vec2 uv;
uniform mat4 transform;
out vec2 vertex_uv;
void main()
{
    vertex_uv = uv;
    gl_Position = transform * vec4(pos);
}
"""


FRAGMENT_SHADER: Final = b"""
#version 140
in vec2 vertex_uv;
uniform vec4 color;
uniform sampler2D tex;
out vec4 output_color;
void main()
{
    output_color = vec4(color.rgb, texture(tex, vertex_uv).r * color.a);
}
"""


if __name__ == '__main__':
    run_application(App)
