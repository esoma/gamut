
# gamut
from gamut.geometry import RectangularCuboid
from gamut.graphics import (BufferView, BufferViewMap, clear_render_target,
                            DepthTest, execute_shader, FaceCull, Image,
                            PrimitiveMode, Shader)
from gamut.math import FMatrix4, FVector3
# python
from typing import Final
# examples
from examplescommon import ExampleApplication, RESOURCES, run_application


class App(ExampleApplication):

    async def example_main(self) -> None:
        self.window.title = 'Gamut Cube Example'

        self.shader = Shader(vertex=VERTEX_SHADER, fragment=FRAGMENT_SHADER)
        self.cube_transform = FMatrix4(1)

        cube = RectangularCuboid(FVector3(0), FVector3(2))
        cube_positions, _, cube_uvs, cube_indices = cube.render()
        self.cube_attributes = BufferViewMap({
            "pos": BufferView.from_array(cube_positions),
            "uv": BufferView.from_array(cube_uvs),
        })
        self.cube_index_buffer_view = BufferView.from_array(cube_indices)
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
