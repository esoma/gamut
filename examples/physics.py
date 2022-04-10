
# gamut
from gamut.geometry import Plane, RectangularCuboid
from gamut.graphics import (BufferView, BufferViewMap, clear_render_target,
                            DepthTest, execute_shader, FaceCull, PrimitiveMode,
                            Shader)
from gamut.math import (DMatrix4, DVector3, FMatrix3, FMatrix4, FVector3,
                        FVector3Array, U8Array)
from gamut.physics import Body, BodyType, World
# python
from datetime import timedelta
import random
from typing import Final
# examples
from examplescommon import ExampleApplication, run_application


class App(ExampleApplication):

    async def example_main(self) -> None:
        self.window.title = 'Gamut Physics Example'
        self.camera_position = FVector3(0, 10, 30)
        self.camera_pitch = .2

        self.shader = Shader(vertex=VERTEX_SHADER, fragment=FRAGMENT_SHADER)

        self.plane_transform = FMatrix4(1).scale(FVector3(100, 0, 100))
        self.plane_attributes = BufferViewMap({
            "pos": BufferView.from_array(FVector3Array(
                    FVector3(-1, 0, -1),
                    FVector3(1, 0, -1),
                    FVector3(1, 0, 1),
                    FVector3(-1, 0, 1),
            )),
            "norm": BufferView.from_array(FVector3Array(
                FVector3(0, 1, 0),
                FVector3(0, 1, 0),
                FVector3(0, 1, 0),
                FVector3(0, 1, 0),
            )),
        })
        self.plane_index_buffer_view = BufferView.from_array(U8Array(
            0, 2, 1,
            0, 3, 2
        ))

        cube = RectangularCuboid(DVector3(0), DVector3(1))
        cube_positions, cube_normals, _, cube_indices = cube.render()
        self.cube_attributes = BufferViewMap({
            "pos": BufferView.from_array(cube_positions),
            "norm": BufferView.from_array(cube_normals),
        })
        self.cube_index_buffer_view = BufferView.from_array(cube_indices)

        self.world = World(timedelta(seconds=1 / 60.0))
        self.world.gravity = DVector3(0, -9.8, 0)
        plane = Body(
            1,
            Plane(0, DVector3(0, 1, 0)),
            world=self.world,
            type=BodyType.STATIC
        )
        plane.friction = .5

        self.bodies = []
        for _ in range(50):
            body = Body(1, cube, world=self.world)
            body.transform = DMatrix4(1).translate(
                DVector3(
                    random.uniform(-2, 2),
                    random.uniform(1, 3),
                    random.uniform(-2, 2)
                )
            )
            body.friction = .5
            self.bodies.append(body)

    async def draw(self, step: ExampleApplication.Step) -> None:
        self.world.simulate(step.when - step.previous)

        clear_render_target(
            self.window_render_target,
            color=FVector3(0, 0, 0),
            depth=1
        )
        execute_shader(
            self.window_render_target,
            self.shader,
            PrimitiveMode.TRIANGLE,
            self.plane_attributes,
            {
                "camera_transform": self.camera.view_projection_transform,
                "model_transform": self.plane_transform,
                "normal_model_transform": FMatrix3(1),
                "color": FVector3(1, 1, 1),
            },
            index_buffer_view=self.plane_index_buffer_view,
            depth_write=True,
            depth_test=DepthTest.LESS,
            face_cull=FaceCull.BACK,
        )

        for body in self.bodies:
            execute_shader(
                self.window_render_target,
                self.shader,
                PrimitiveMode.TRIANGLE,
                self.cube_attributes,
                {
                    "camera_transform": self.camera.view_projection_transform,
                    "model_transform": body.transform.to_fmatrix(),
                    "normal_model_transform": (
                        body.transform.inverse().transpose()
                            .to_matrix3().to_fmatrix()
                    ),
                    "color": (
                        FVector3(1, 0, 0)
                        if body.is_sleeping else
                        FVector3(0, 1, 0)
                    ),
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
in vec3 norm;
out vec3 normal;
out vec3 position;
uniform mat4 camera_transform;
uniform mat4 model_transform;
uniform mat3 normal_model_transform;
void main()
{
    normal = normalize(normal_model_transform * norm);
    vec4 world_position = model_transform * vec4(pos, 1.0);
    position = world_position.xyz;
    gl_Position = camera_transform * world_position;
}
"""


FRAGMENT_SHADER: Final = b"""
#version 140
uniform vec3 color;
in vec3 normal;
in vec3 position;
out vec4 output_color;

#define LIGHT_POSITION vec3(10, 10, 10)
#define LIGHT_RANGE 100

void main()
{
    vec3 light_direction = normalize(LIGHT_POSITION - position);
    float light_distance = length(LIGHT_POSITION - position);
    float light_attenuation = 1 - max(light_distance / LIGHT_RANGE, 0);

    float light = min((
        max(dot(normal, light_direction), 0) *
        light_attenuation
    ) + .2, 1);
    output_color = vec4(color * light, 1);
}
"""


if __name__ == '__main__':
    run_application(App)
