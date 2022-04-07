
# gamut
from gamut.graphics import (Buffer, BufferView, BufferViewMap,
                            clear_render_target, Color, DepthTest,
                            execute_shader, FaceCull, Image, PrimitiveMode,
                            Shader)
from gamut.math import (FMatrix4, FVector2, FVector2Array, FVector3,
                        FVector3Array, U8Array)
# python
import ctypes
from typing import Final
# examples
from examplescommon import ExampleApplication, RESOURCES, run_application


class Draw(TimerExpired):
    pass


class App(ExampleApplication):

    async def example_main(self) -> None:
        self.window.title = 'Gamut Cube Example'

        self.shader = Shader(vertex=VERTEX_SHADER, fragment=FRAGMENT_SHADER)
        self.cube_transform = FMatrix4(1)
        self.cube_attributes = BufferViewMap({
            "pos": BufferView(
                Buffer(FVector3Array(
                    FVector3(-1, -1, -1),
                    FVector3(1, -1, -1),
                    FVector3(1, 1, -1),
                    FVector3(-1, 1, -1),
                    FVector3(-1, -1, 1),
                    FVector3(1, -1, 1),
                    FVector3(1, 1, 1),
                    FVector3(-1, 1, 1),
                )),
                FVector3,
            ),
            "uv": BufferView(
                Buffer(FVector2Array(
                    FVector2(0, 0),
                    FVector2(1, 0),
                    FVector2(1, 1),
                    FVector2(0, 1),
                    FVector2(1, 1),
                    FVector2(0, 1),
                    FVector2(0, 0),
                    FVector2(1, 0),
                )),
                FVector2
            )
        })
        self.cube_index_buffer_view = BufferView(
            Buffer(U8Array(
                0, 2, 1, 2, 0, 3,
                4, 5, 6, 6, 7, 4,
                1, 6, 5, 6, 1, 2,
                0, 7, 3, 7, 0, 4,
                0, 5, 4, 5, 0, 1,
                3, 7, 6, 6, 2, 3,
            )),
            ctypes.c_uint8
        )
        self.cube_texture = Image(RESOURCES / 'yee.jpg').to_texture()

    async def draw(self, draw: Draw) -> None:
        self.cube_transform = self.cube_transform.rotate(
            .02,
            FVector3(1, 1, 1)
        )

        clear_render_target(
            self.window_render_target,
            color=Color(0, 0, 0),
            depth=1
        )
        execute_shader(
            self.window_render_target,
            self.shader,
            PrimitiveMode.TRIANGLE,
            self.cube_attributes,
            {
                "camera_transform": self.camera.view_projection_transform,
                "model_transform": self.cube_transform,
                "tex": self.cube_texture,
            },
            index_buffer_view=self.cube_index_buffer_view,
            depth_write=True,
            depth_test=DepthTest.LESS,
            face_cull=FaceCull.BACK,
        )
        self.window.flip_buffer()


VERTEX_SHADER: Final = b"""
#version 140
in vec3 pos;
in vec2 uv;
out vec2 vertex_uv;
uniform mat4 camera_transform;
uniform mat4 model_transform;
void main()
{
    vertex_uv = uv;
    gl_Position = camera_transform * model_transform * vec4(pos, 1.0);
}
"""


FRAGMENT_SHADER: Final = b"""
#version 140
in vec2 vertex_uv;
out vec4 output_color;
uniform sampler2D tex;
void main()
{
    output_color = texture(tex, vertex_uv);
}
"""


if __name__ == '__main__':
    run_application(App)
