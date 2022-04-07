
# gamut
from gamut.graphics import (BufferView, BufferViewMap, clear_render_target,
                            DepthTest, execute_shader, FaceCull, Image,
                            PrimitiveMode, Shader)
from gamut.math import (FMatrix4, FMatrix4Array, FVector2, FVector2Array,
                        FVector3, FVector3Array, U8Array)
# python
from typing import Final
# examples
from examplescommon import ExampleApplication, RESOURCES, run_application

CUBES_X: Final = 100
CUBES_Y: Final = 100
CUBES_Z: Final = 100


class App(ExampleApplication):

    async def example_main(self) -> None:
        self.window.title = 'Gamut Instancing Example'

        self.shader = Shader(vertex=VERTEX_SHADER, fragment=FRAGMENT_SHADER)
        self.cube_transform = FMatrix4(1)
        self.cube_attributes = BufferViewMap({
            "pos": BufferView.from_array(FVector3Array(
                FVector3(-1, -1, -1),
                FVector3(1, -1, -1),
                FVector3(1, 1, -1),
                FVector3(-1, 1, -1),
                FVector3(-1, -1, 1),
                FVector3(1, -1, 1),
                FVector3(1, 1, 1),
                FVector3(-1, 1, 1),
            )),
            "uv": BufferView.from_array(FVector2Array(
                FVector2(0, 0),
                FVector2(1, 0),
                FVector2(1, 1),
                FVector2(0, 1),
                FVector2(1, 1),
                FVector2(0, 1),
                FVector2(0, 0),
                FVector2(1, 0),
            )),
            "instance_transform": BufferView.from_array(
                FMatrix4Array(*(
                    FMatrix4(1).translate(FVector3(x * 4, y * 4, z * -4))
                    for x in range(CUBES_X)
                    for y in range(CUBES_Y)
                    for z in range(CUBES_Z)
                )),
                instancing_divisor=1,
            ),
        })
        self.cube_index_buffer_view = BufferView.from_array(U8Array(
            0, 2, 1, 2, 0, 3,
            4, 5, 6, 6, 7, 4,
            1, 6, 5, 6, 1, 2,
            0, 7, 3, 7, 0, 4,
            0, 5, 4, 5, 0, 1,
            3, 7, 6, 6, 2, 3,
        ))
        self.cube_texture = Image(RESOURCES / 'yee.jpg').to_texture()

    async def draw(self, step: ExampleApplication.Step) -> None:
        self.cube_transform = self.cube_transform.rotate(
            .02,
            FVector3(1, 1, 1)
        )

        clear_render_target(
            self.window_render_target,
            color=FVector3(0, 0, 0),
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
            instances=CUBES_X * CUBES_Y * CUBES_Z,
            face_cull=FaceCull.BACK
        )
        self.window.flip_buffer()


VERTEX_SHADER: Final = b"""
#version 140
in vec3 pos;
in vec2 uv;
in mat4 instance_transform;
out vec2 vertex_uv;
uniform mat4 camera_transform;
uniform mat4 model_transform;
void main()
{
    vertex_uv = uv;
    gl_Position = (
        camera_transform *
        instance_transform *
        model_transform *
        vec4(pos, 1.0)
    );
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
