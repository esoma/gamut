
# gamut
from gamut.ai import NavigationMesh3d
from gamut.ai._navigationmesh3d import Debug as NavigationMesh3dDebug
from gamut.event import Bind
from gamut.geometry import LineSegment3d, Mesh3d, RectangularCuboid, Triangle3d
from gamut.gltf import Gltf
from gamut.graphics import (BufferView, BufferViewMap, clear_render_target,
                            DepthTest, execute_shader, FaceCull, PrimitiveMode,
                            Shader)
from gamut.math import (DVector3, DVector3Array, FMatrix3, FMatrix4, FVector2,
                        FVector3, UVector1, UVector1Array, UVector3Array)
from gamut.peripheral import (MouseButtonPressed, MouseMoved,
                              MouseScrolledVertically)
# python
from typing import Final
# examples
from examplescommon import ExampleApplication, RESOURCES, run_application


class App(ExampleApplication):

    async def example_main(self) -> None:
        self.window.title = 'Gamut Navigation Example'
        self.mouse.is_relative = False
        self.camera_position = FVector3(-22, 10, 22)
        self.camera_yaw = .76
        self.camera_pitch = 0.25

        self.shader = Shader(vertex=VERTEX_SHADER, fragment=FRAGMENT_SHADER)

        self.cube_radius = 2
        self.cube_scale = FVector3(self.cube_radius)
        cube = RectangularCuboid(DVector3(0), DVector3(1))
        cube_positions, cube_normals, _, cube_indices = cube.render()
        self.cube_attributes = BufferViewMap({
            "pos": BufferView.from_array(cube_positions),
            "norm": BufferView.from_array(cube_normals),
        })
        self.cube_index_buffer_view = BufferView.from_array(cube_indices)

        with open(RESOURCES / 'navmesh.glb', 'rb') as f:
            navmesh_gltf = Gltf(f)
        navmesh_attrs = navmesh_gltf.meshes[0].primitives[0].attributes
        navmesh_indices = navmesh_gltf.meshes[0].primitives[0].indices.data
        navmesh_positions = navmesh_attrs["POSITION"].data
        self.navmesh_attributes = BufferViewMap({
            "pos": BufferView.from_array(navmesh_positions),
            "norm": BufferView.from_array(navmesh_attrs["NORMAL"].data)
        })
        self.navmesh_index_buffer_view = BufferView.from_array(navmesh_indices)
        self.navmesh_shape = Mesh3d(
            DVector3Array(*(DVector3(*v) for v in navmesh_positions)),
            UVector3Array.from_buffer(
                UVector1Array(*(UVector1(i) for i in navmesh_indices))
            )
        )
        self.navmesh = NavigationMesh3d()
        for i in range(len(navmesh_indices) // 3):
            self.navmesh.add_triangle(Triangle3d(
                navmesh_positions[navmesh_indices[(i * 3)]],
                navmesh_positions[navmesh_indices[(i * 3) + 1]],
                navmesh_positions[navmesh_indices[(i * 3) + 2]],
            ))
        """
        self.navmesh.add_triangle(Triangle3d(
            FVector3(0, 0, 0),
            FVector3(1, -.1, 0),
            FVector3(1, 0, 1),
        ))
        self.navmesh.add_triangle(Triangle3d(
            FVector3(0, 0, 0),
            FVector3(0, 0, 1),
            FVector3(1, 0, 1),
        ))
        """

        self.cube_position = FVector3(6, 0, -10)
        self.path = []
        """
        path = self.navmesh.find_path(
            self.cube_position,
            Triangle3d(
                FVector3(4, 0, -10),
                FVector3(6, 0, -8),
                FVector3(6, 0, -10),
            ),
            FVector3(4, 0, 10),
            Triangle3d(
                FVector3(4, 0, 8),
                FVector3(4, 0, 10),
                FVector3(6, 0, 10),
            ),
            radius=self.cube_radius,
            squeeze=True
        )
        if path is not None:
            self.path = list(path)
        else:
            self.path = []
        """
        self.mouse_press_bind = Bind.on(
            self.mouse.Button.left.Pressed,
            self.mouse_click
        )
        self.mouse_scrolled_vertically_bind = Bind.on(
            self.mouse.ScrolledVertically,
            self.mouse_scrolled_vertically
        )

        self.debug = NavigationMesh3dDebug(self.navmesh)

    async def mouse_moved(self, mouse_moved: MouseMoved) -> None:
        pass

    async def mouse_scrolled_vertically(
        self,
        scroll: MouseScrolledVertically
    ) -> None:
        c = scroll.delta * .1
        self.cube_radius += c
        self.cube_scale += FVector3(c, 0, c)

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
            end_triangle = Triangle3d(*(
                FVector3(*self.navmesh_shape.positions[i])
                for i in triangle_indices
            ))
            end = FVector3(*result.position)

            d_cube_position = DVector3(*self.cube_position)
            result = self.navmesh_shape.raycast(
                d_cube_position + DVector3(0, .1, 0),
                d_cube_position + DVector3(0, -1, 0)
            )
            if result:
                triangle_indices = self.navmesh_shape.triangle_indices[
                    result.triangle_index
                ]
                start_triangle = Triangle3d(*(
                    FVector3(*self.navmesh_shape.positions[i])
                    for i in triangle_indices
                ))
                start = FVector3(*result.position)
                path = self.navmesh.find_path(
                    start,
                    start_triangle,
                    end,
                    end_triangle,
                    radius=self.cube_radius,
                    squeeze=True,
                    debug=self.debug
                )
                if path is not None:
                    self.path = list(path)

    async def draw(self, step: ExampleApplication.Step) -> None:
        clear_render_target(
            self.window_render_target,
            color=FVector3(0, 0, 0),
            depth=1
        )
        """
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
        """

        cube_movement = (step.when - step.previous).total_seconds() * 10
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
        ).scale(self.cube_scale)
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

        #clear_render_target(self.window_render_target, depth=1)
        self.debug.draw(
            self.window_render_target,
            self.camera.view_projection_transform,
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
