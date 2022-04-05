
# gamut
from gamut import (Application, Camera, Timer, TimerExpired, TransformNode,
                   Window)
from gamut.ai import NavigationMesh3d
from gamut.event import Bind
from gamut.geometry import LineSegment3d, Mesh3d, RectangularCuboid
from gamut.gltf import Gltf
from gamut.graphics import (Buffer, BufferView, BufferViewMap,
                            clear_render_target, Color, DepthTest,
                            execute_shader, FaceCull, PrimitiveMode, Shader,
                            WindowRenderTarget)
from gamut.math import (DVector3, FMatrix3, FMatrix4, FVector2, FVector3,
                        UVector1, UVector1Array, UVector2, UVector3Array,
                        Vector3, Vector3Array)
from gamut.peripheral import (KeyboardConnected, KeyboardKeyPressed,
                              MouseButtonPressed, MouseConnected, MouseMoved)
# python
import ctypes
from datetime import timedelta
from math import cos, radians, sin
from pathlib import Path
from typing import Any, Final

RESOURCES: Final = Path(__file__).parent / 'resources'


class Draw(TimerExpired):
    pass


class App(Application):

    async def main(self) -> None:
        self.window = Window()
        self.window.title = 'Gamut Navigation Example'
        self.window.resize(UVector2(800, 800))
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

        self.player_position = FVector3(-20, 10, 20)
        self.player_yaw = -.8
        self.player_pitch = -0.25
        self.player_node: TransformNode[Any] = TransformNode()
        self.camera = Camera(
            FMatrix4.perspective(radians(45), 1, .1, 100)
        )

        self.shader = Shader(vertex=vertex_shader, fragment=fragment_shader)

        cube = RectangularCuboid(Vector3(0), Vector3(1))
        cube_positions, cube_normals, cube_indices = cube.render()
        self.cube_attributes = BufferViewMap({
            "pos": BufferView(Buffer(cube_positions), DVector3),
            "norm": BufferView(Buffer(cube_normals), DVector3),
        })
        self.cube_index_buffer_view = BufferView(
            Buffer(cube_indices),
            ctypes.c_uint8
        )

        with open(RESOURCES / 'navmesh.glb', 'rb') as f:
            navmesh_gltf = Gltf(f)
        navmesh_attrs = navmesh_gltf.meshes[0].primitives[0].attributes
        navmesh_indices = navmesh_gltf.meshes[0].primitives[0].indices.data
        navmesh_positions = navmesh_attrs["POSITION"].data
        self.navmesh_attributes = BufferViewMap({
            "pos": BufferView(Buffer(navmesh_positions), FVector3),
            "norm": BufferView(Buffer(navmesh_attrs["NORMAL"].data), FVector3)
        })
        self.navmesh_index_buffer_view = BufferView(
            Buffer(navmesh_indices),
            ctypes.c_uint16
        )
        self.navmesh_shape = Mesh3d(
            Vector3Array(*(Vector3(*v) for v in navmesh_positions)),
            UVector3Array.from_buffer(
                UVector1Array(*(UVector1(i) for i in navmesh_indices))
            )
        )
        self.navmesh = NavigationMesh3d()
        for i in range(len(navmesh_indices) // 3):
            self.navmesh.add_triangle(
                navmesh_positions[navmesh_indices[(i * 3)]],
                navmesh_positions[navmesh_indices[(i * 3) + 1]],
                navmesh_positions[navmesh_indices[(i * 3) + 2]],
            )
        self.path = list(self.navmesh.find_path(
            (FVector3(6, 0, -10), FVector3(6, 0, -8), FVector3(4, 0, -10)),
            (FVector3(4, 0, 10), FVector3(6, 0, 10), FVector3(4, 0, 8)),
        ))
        self.cube_position = self.path[0]

        with (
            Bind.on(self.keyboard.Key.escape.Pressed, self.escape),
            Bind.on(Draw, self.draw),
            Bind.on(mouse.Button.left.Pressed, self.mouse_click)
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

    async def mouse_click(self, button_pressed: MouseButtonPressed) -> None:
        clip_position = ((
            FVector2(*button_pressed.mouse.position) /
            FVector2(800, 800)
        ) * 2 - 1) * FVector2(1, -1)
        ray = self.camera.generate_ray(clip_position)
        result = self.navmesh_shape.raycast(DVector3(*ray.a), DVector3(*ray.b))
        if result:
            triangle_indices = self.navmesh_shape.triangle_indices[
                result.triangle_index
            ]
            triangle = {
                FVector3(*self.navmesh_shape.positions[i])
                for i in triangle_indices
            }
            start = tuple(triangle)
            triangle -= {FVector3(*result.position)}
            end = (FVector3(*result.position), *list(triangle)[:2])

            d_cube_position = DVector3(*self.cube_position)
            result = self.navmesh_shape.raycast(
                d_cube_position + DVector3(0, .1, 0),
                d_cube_position + DVector3(0, -1, 0)
            )
            if result:
                triangle_indices = self.navmesh_shape.triangle_indices[
                    result.triangle_index
                ]
                triangle = {
                    FVector3(*self.navmesh_shape.positions[i])
                    for i in triangle_indices
                }
                triangle -= {FVector3(*result.position)}
                start = (FVector3(*result.position), *list(triangle)[:2])
                path = self.navmesh.find_path(start, end)
                if path is not None:
                    self.path = list(path)

    async def draw(self, draw: Draw) -> None:
        player_direction = FVector3(
            cos(self.player_yaw) * cos(self.player_pitch),
            sin(self.player_pitch),
            sin(self.player_yaw) * cos(self.player_pitch)
        ).normalize()
        player_cross_direction = player_direction.cross(
            FVector3(0, 1, 0)
        ).normalize()

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

        self.camera.local_transform = FMatrix4.look_at(
            self.player_position,
            self.player_position + player_direction,
            FVector3(0, 1, 0),
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
            self.navmesh_attributes,
            {
                "camera_transform": self.camera.view_projection_transform,
                "model_transform": FMatrix4(1),
                "normal_model_transform": FMatrix3(1),
                "color": FVector3(1, 1, 1),
            },
            index_buffer_view=self.navmesh_index_buffer_view,
            depth_write=True,
            depth_test=DepthTest.LESS,
        )

        cube_movement = (draw.when - draw.previous).total_seconds() * 4
        while cube_movement and self.path:
            distance = self.cube_position.distance(self.path[0])
            if distance == 0:
                self.path.pop(0)
                continue
            travel_distance = min(distance, cube_movement)
            cube_movement -= travel_distance
            t = travel_distance / distance
            line = LineSegment3d(self.cube_position, self.path[0])
            self.cube_position = line.get_point_from_a_to_b(t)
            if cube_movement:
                self.path.pop(0)

        cube_transform = FMatrix4(1).translate(
            self.cube_position + FVector3(0, .5, 0)
        )
        execute_shader(
            self.window_render_target,
            self.shader,
            PrimitiveMode.TRIANGLE,
            self.cube_attributes,
            {
                "camera_transform": self.camera.view_projection_transform,
                "model_transform": cube_transform,
                "normal_model_transform": (
                    cube_transform.inverse().transpose().to_matrix3()
                ),
                "color": FVector3(1, 0, 0),
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
