
# gamut
from gamut import Application, Timer, TimerExpired, TransformNode, Window
from gamut.event import Bind
from gamut.geometry import Plane, RectangularCuboid
from gamut.graphics import (Buffer, BufferView, BufferViewMap,
                            clear_render_target, Color, DepthTest,
                            execute_shader, FaceCull, PrimitiveMode, Shader,
                            WindowRenderTarget)
from gamut.math import Matrix4, Vector3
from gamut.peripheral import (KeyboardConnected, KeyboardKeyPressed,
                              MouseConnected, MouseMoved)
from gamut.physics import Body, BodyType, World
# python
from datetime import timedelta
import random
from typing import Any
# pyglm
from glm import (array, cos, cross, inverse, lookAt, mat3, mat4, normalize,
                 perspective, radians, scale, sin, transpose, uint8, vec3)


class Draw(TimerExpired):
    pass


class App(Application):

    async def main(self) -> None:
        self.window = Window()
        self.window.title = 'Gamut Physics Example'
        self.window.resize((800, 800))
        self.window.recenter()
        self.window.is_visible = True
        self.window_render_target = WindowRenderTarget(self.window)

        try:
            self.keyboard = self.keyboards[0]
        except IndexError:
            self.keyboard = (await KeyboardConnected).keyboard
        try:
            mouse = self.mice[0]
        except IndexError:
            mouse = (await MouseConnected).mouse
        mouse.relative = True

        self.player_position = vec3(-30, 10, 0)
        self.player_yaw = 0
        self.player_pitch = 0.0
        self.player_node: TransformNode[Any] = TransformNode()
        self.projection = perspective(radians(45), 1, .1, 100)

        self.shader = Shader(vertex=vertex_shader, fragment=fragment_shader)

        self.plane_transform = scale(mat4(1), vec3(100, 0, 100))
        self.plane_attributes = BufferViewMap({
            "pos": BufferView(
                Buffer(array(
                    vec3(-1, 0, -1),
                    vec3(1, 0, -1),
                    vec3(1, 0, 1),
                    vec3(-1, 0, 1),
                ).to_bytes()),
                vec3,
            ),
            "norm": BufferView(
                Buffer(array(
                    vec3(0, 1, 0),
                    vec3(0, 1, 0),
                    vec3(0, 1, 0),
                    vec3(0, 1, 0),
                ).to_bytes()),
                vec3,
            ),
        })
        self.plane_index_buffer_view = BufferView(
            Buffer(array.from_numbers(uint8,
                0, 2, 1,
                0, 3, 2
            ).to_bytes()),
            uint8
        )

        cube = RectangularCuboid(vec3(0), vec3(1))
        cube_positions, cube_normals, cube_indices = cube.render()
        self.cube_attributes = BufferViewMap({
            "pos": BufferView(Buffer(cube_positions.to_bytes()), vec3),
            "norm": BufferView(Buffer(cube_normals.to_bytes()), vec3),
        })
        self.cube_index_buffer_view = BufferView(Buffer(cube_indices), uint8)

        self.world = World(timedelta(seconds=1 / 60.0))
        self.world.gravity = Vector3(0, -9.8, 0)
        plane = Body(
            1,
            Plane(0, vec3(0, 1, 0)),
            world=self.world,
            type=BodyType.STATIC
        )
        plane.friction = .5

        self.bodies = []
        for _ in range(50):
            body = Body(1, cube, world=self.world)
            body.transform = Matrix4(1).translate(
                Vector3(
                    random.uniform(-2, 2),
                    random.uniform(1, 3),
                    random.uniform(-2, 2)
                )
            )
            body.friction = .5
            self.bodies.append(body)

        with (
            Bind.on(self.keyboard.Key.escape.Pressed, self.escape),
            Bind.on(Draw, self.draw),
            Bind.on(MouseMoved, self.mouse_moved)
        ):
            step_timer = Timer(
                self,
                timedelta(seconds=1 / 60.0),
                Draw,
                repeat=True,
                fixed=True,
            )
            await self.window.Close

    async def escape(self, key_pressed: KeyboardKeyPressed) -> None:
        self.window.Close().send()

    async def mouse_moved(self, mouse_moved: MouseMoved) -> None:
        if mouse_moved.delta is not None:
            self.player_yaw += mouse_moved.delta[0] * .005
            self.player_pitch -= mouse_moved.delta[1] * .005

    async def draw(self, draw: Draw) -> None:
        self.world.simulate(draw.when - draw.previous)

        player_direction = normalize(vec3(
            cos(self.player_yaw) * cos(self.player_pitch),
            sin(self.player_pitch),
            sin(self.player_yaw) * cos(self.player_pitch)
        ))
        player_cross_direction = normalize(cross(
            player_direction,
            vec3(0, 1, 0)
        ))

        player_frame_speed = (
            (draw.when - draw.previous).total_seconds() /
            (1 / 60.0) *
            .1
        )
        keys = self.keyboard.Key
        if keys.up.is_pressed or keys.w.is_pressed:
            self.player_position += player_frame_speed * player_direction
        if keys.down.is_pressed or keys.s.is_pressed:
            self.player_position -= player_frame_speed * player_direction
        if keys.left.is_pressed or keys.a.is_pressed:
            self.player_position -= player_frame_speed * player_cross_direction
        if keys.right.is_pressed or keys.d.is_pressed:
            self.player_position += player_frame_speed * player_cross_direction

        self.player_node.local_transform = lookAt(
            self.player_position,
            self.player_position + player_direction,
            vec3(0, 1, 0),
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
            self.plane_attributes,
            {
                "camera_transform":
                    self.projection * self.player_node.transform,
                "model_transform": self.plane_transform,
                "normal_model_transform": mat3(1),
                "color": vec3(1, 1, 1),
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
                    "camera_transform":
                        self.projection * self.player_node.transform,
                    "model_transform": mat4(body.transform),
                    "normal_model_transform": mat3(transpose(inverse(
                        mat4(body.transform)
                    ))),
                    "color": (
                        vec3(1, 0, 0)
                        if body.is_sleeping else
                        vec3(0, 1, 0)
                    ),
                },
                index_buffer_view=self.cube_index_buffer_view,
                depth_write=True,
                depth_test=DepthTest.LESS,
                face_cull=FaceCull.BACK,
            )

        self.window.flip_buffer()


vertex_shader = b"""
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


fragment_shader = b"""
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
    app = App()
    app.run()
