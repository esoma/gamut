
# gamut
from gamut.ai import NavigationMesh3d
from gamut.ai._navigationmesh3d import Debug as NavigationMesh3dDebug
from gamut.event import Bind
from gamut.geometry import (LineSegment3d, Mesh3d, MeshModifier,
                            RectangularCuboid, Triangle3d)
from gamut.gltf import Gltf
from gamut.graphics import (BufferView, BufferViewMap, clear_render_target,
                            DepthTest, execute_shader, FaceCull, PrimitiveMode,
                            Shader)
from gamut.math import (DVector3, DVector3Array, FMatrix3, FMatrix4,
                        FMatrix4Array, FVector2, FVector3, FVector3Array,
                        U32Array, UVector1, UVector1Array, UVector3Array)
from gamut.navigation._navigation import (CompactHeightField, ContourSet,
                                          DetailMesh, HeightField, Mesh,
                                          NavigationMesh)
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
        self.instance_shader = Shader(vertex=INSTANCE_VERTEX_SHADER, fragment=INSTANCE_FRAGMENT_SHADER)

        self.path = []

        self.cube_radius = 1
        self.cube_scale = FVector3(self.cube_radius)
        cube = RectangularCuboid(DVector3(0), DVector3(1))
        cube_positions, cube_normals, _, cube_indices = cube.render()
        self.cube_attributes = BufferViewMap({
            "pos": BufferView.from_array(cube_positions),
            "norm": BufferView.from_array(cube_normals),
        })
        self.cube_index_buffer_view = BufferView.from_array(cube_indices)
        self.cube_position = FVector3(5, 0, -9)

        with open('examples/resources/navmesh.glb', 'rb') as f:
            navmesh_gltf = Gltf(f)
        navmesh_attrs = navmesh_gltf.meshes[0].primitives[0].attributes
        navmesh_indices = navmesh_gltf.meshes[0].primitives[0].indices.data
        print(navmesh_indices)
        navmesh_positions = navmesh_attrs["POSITION"].data
        self.navmesh_attributes = BufferViewMap({
            "pos": BufferView.from_array(navmesh_positions),
            "norm": BufferView.from_array(navmesh_attrs["NORMAL"].data)
        })
        self.navmesh_index_buffer_view = BufferView.from_array(navmesh_indices)
        self.navmesh_shape = Mesh3d(
            FVector3Array(*(FVector3(*v) for v in navmesh_positions)),
            UVector3Array.from_buffer(
                UVector1Array(*(UVector1(i) for i in navmesh_indices))
            )
        )

        mm = MeshModifier(self.navmesh_shape)
        mm.displace_border(FVector3(-.5, 0, -.5))
        self.navmesh_shape = mm.build()

        self.navmesh2_attributes = BufferViewMap({
            "pos": BufferView.from_array(self.navmesh_shape.positions),
            "norm": BufferView.from_array(navmesh_attrs["NORMAL"].data)
        })
        self.navmesh2_index_buffer_view = BufferView.from_array(
            U32Array(*(
                i
                for t in self.navmesh_shape.triangle_indices
                for i in t
            ))
        )

        #self.navmesh_shape.displace_edges()

        """
        # HEIGHT FIELD
        cell_size = .1
        cell_height = .1
        hf = HeightField(
            400,
            400,
            FVector3(-20, -2, -20),
            FVector3(20, 5, 20),
            cell_size, cell_height,
            2,
            1
        )
        for i in range(len(navmesh_indices) // 3):
            hf.add_triangles([[
                navmesh_positions[navmesh_indices[(i * 3)]],
                navmesh_positions[navmesh_indices[(i * 3) + 1]],
                navmesh_positions[navmesh_indices[(i * 3) + 2]],
            ]])
        hf.filter()

        hf_cube = RectangularCuboid(FVector3(0), FVector3(cell_size, cell_height, cell_size))
        hf_cube_positions, hf_cube_normals, _, hf_cube_indices = hf_cube.render()
        self.hf_cube_positions = [s[0] + (hf_cube.dimensions * .5) for s in hf.spans if s[2]]
        self.hf_attributes = BufferViewMap({
            "pos": BufferView.from_array(hf_cube_positions),
            "norm": BufferView.from_array(hf_cube_normals),
            "instance_color": BufferView.from_array(
                FVector3Array(*(FVector3(1, 0, 0) for pos in self.hf_cube_positions)),
                instancing_divisor=1,
            ),
            "instance_transform": BufferView.from_array(
                FMatrix4Array(*(
                    FMatrix4(1).translate(pos)
                    for pos in self.hf_cube_positions
                )),
                instancing_divisor=1,
            ),
        })
        self.hf_index_buffer_view = BufferView.from_array(hf_cube_indices)


        # COMPACT HEIGHT FIELD
        chf = CompactHeightField(hf)
        chf.erode(1)
        #chf.partition_watershed(0, 5, 5)
        #chf.partition_monotone(0, 1, 0)
        chf.partition_layers(0, 1)

        chf_cube = RectangularCuboid(FVector3(0), FVector3(1))
        chf_cube_positions, chf_cube_normals, _, chf_cube_indices = chf_cube.render()
        self.chf_cube_transforms = [
            FMatrix4(1).translate(s[0] + ((s[1] - s[0]) * .5)).scale(s[1] - s[0])
            for s in chf.spans if s[2]
        ]
        import distinctipy
        self.region_color = {s[3]: None for s in chf.spans}
        colors = [FVector3(*c) for c in distinctipy.get_colors(len(self.region_color), [(0, 0, 0), (1, 1, 1)])]
        for i, k in enumerate(self.region_color.keys()):
            self.region_color[k] = colors[i]
        self.chf_cube_colors = [
            self.region_color[s[3]]
            for s in chf.spans if s[2]
        ]
        self.chf_attributes = BufferViewMap({
            "pos": BufferView.from_array(chf_cube_positions),
            "norm": BufferView.from_array(chf_cube_normals),
            "instance_color": BufferView.from_array(
                FVector3Array(*self.chf_cube_colors),
                instancing_divisor=1,
            ),
            "instance_transform": BufferView.from_array(
                FMatrix4Array(*self.chf_cube_transforms),
                instancing_divisor=1,
            ),
        })
        self.chf_index_buffer_view = BufferView.from_array(chf_cube_indices)


        cs = ContourSet(chf, 1, 2)

        mesh = Mesh(cs, 3)
        region_polygons = {}
        mesh_polygons = mesh.polygons
        for walkable, region, vertices in mesh.polygons:
            if not walkable:
                continue
            try:
                polygons = region_polygons[region]
            except KeyError:
                polygons = region_polygons[region] = []
            polygons.append(vertices)
        self.region_mesh_attributes = {}
        for region, polygons in region_polygons.items():
            self.region_mesh_attributes[region] = BufferViewMap({
                "pos": BufferView.from_array(FVector3Array(*(
                    v
                    for p in polygons
                    for v in p
                ))),
                "norm": BufferView.from_array(FVector3Array(*(
                    FVector3(0, 1, 0)
                    for p in polygons
                    for v in p
                )))
            })

        dmesh = DetailMesh(mesh, chf, 10, .1)
        region_detail_polygons = {}
        for i, vertices in enumerate(dmesh.meshes):
            walkable, region, _ = mesh_polygons[i]
            if not walkable:
                continue
            try:
                polygons = region_detail_polygons[region]
            except KeyError:
                polygons = region_detail_polygons[region] = []
            polygons.append(vertices)
        self.region_detail_mesh_attributes = {}
        for region, polygons in region_detail_polygons.items():
            self.region_detail_mesh_attributes[region] = BufferViewMap({
                "pos": BufferView.from_array(FVector3Array(*(
                    v
                    for p in polygons
                    for v in p
                ))),
                "norm": BufferView.from_array(FVector3Array(*(
                    FVector3(0, 1, 0)
                    for p in polygons
                    for v in p
                )))
            })

        self.nm = NavigationMesh(mesh, detail_mesh=dmesh)

        print("___")

        self.mouse_press_bind = Bind.on(
            self.mouse.Button.left.Pressed,
            self.mouse_click
        )
        """

    async def mouse_moved(self, mouse_moved: MouseMoved) -> None:
        pass

    async def mouse_click(self, button_pressed: MouseButtonPressed) -> None:
        clip_position = ((
            FVector2(*button_pressed.mouse.position) /
            FVector2(800, 800)
        ) * 2 - 1) * FVector2(1, -1)
        ray = self.camera.generate_ray(clip_position)
        result = self.navmesh_shape.raycast(DVector3(*ray.a), DVector3(*ray.b))
        if result:
            start_poly, start_point = self.nm.find_nearest_polygon(
                self.cube_position,
                FVector3(.5)
            )
            end_poly, end_point = self.nm.find_nearest_polygon(
                FVector3(*result.position),
                FVector3(.5)
            )
            print(result.position, end_point)
            self.path = self.nm.find_path(
                start_poly, start_point,
                end_poly, end_point,
            )
            print(self.path)
            self.path_attributes = BufferViewMap({
                "pos": BufferView.from_array(FVector3Array(*self.path)),
                "norm": BufferView.from_array(FVector3Array(*(
                    FVector3(1, 1, 1)
                    for p in self.path
                )))
            })
            """
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
            """

    async def draw(self, step: ExampleApplication.Step) -> None:
        clear_render_target(
            self.window_render_target,
            color=FVector3(0, 0, 0),
            depth=1
        )

        execute_shader(
            self.window_render_target,
            self.shader,
            PrimitiveMode.TRIANGLE,
            self.navmesh2_attributes,
            {
                "camera_transform": self.camera.view_projection_transform,
                "model_transform": FMatrix4(1),
                "normal_model_transform": FMatrix3(1),
                "color": FVector3(1, 0, 0),
            },
            index_buffer_view=self.navmesh2_index_buffer_view,
            depth_write=True,
            depth_test=DepthTest.LESS,
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

        """
        if self.path:
            execute_shader(
                self.window_render_target,
                self.shader,
                PrimitiveMode.LINE_STRIP,
                self.path_attributes,
                {
                    "camera_transform": self.camera.view_projection_transform,
                    "model_transform": FMatrix4(1),
                    "normal_model_transform": FMatrix3(1),
                    "color": FVector3(1, 1, 0),
                },
                index_range=(0, len(self.path_attributes["pos"])),
                depth_write=True,
                depth_test=DepthTest.LESS,
            )
        """

        """
        execute_shader(
            self.window_render_target,
            self.instance_shader,
            PrimitiveMode.TRIANGLE,
            self.hf_attributes,
            {
                "camera_transform": self.camera.view_projection_transform,
                "model_transform": FMatrix4(1),
                "normal_model_transform": FMatrix3(1),
            },
            index_buffer_view=self.hf_index_buffer_view,
            depth_write=True,
            depth_test=DepthTest.LESS,
            face_cull=FaceCull.BACK,
            instances=len(self.hf_cube_positions)
        )
        """

        """
        execute_shader(
            self.window_render_target,
            self.instance_shader,
            PrimitiveMode.TRIANGLE,
            self.chf_attributes,
            {
                "camera_transform": self.camera.view_projection_transform,
                "model_transform": FMatrix4(1),
                "normal_model_transform": FMatrix3(1),
            },
            index_buffer_view=self.chf_index_buffer_view,
            depth_write=True,
            depth_test=DepthTest.LESS,
            face_cull=FaceCull.BACK,
            instances=len(self.chf_cube_transforms)
        )
        """

        """
        for region, attributes in self.region_mesh_attributes.items():
            execute_shader(
                self.window_render_target,
                self.shader,
                PrimitiveMode.TRIANGLE,
                attributes,
                {
                    "camera_transform": self.camera.view_projection_transform,
                    "model_transform": FMatrix4(1),
                    "normal_model_transform": FMatrix3(1),
                    "color": self.region_color[region],
                },
                index_range=(0, len(attributes["pos"])),
                depth_write=True,
                depth_test=DepthTest.LESS,
            )
        """

        """
        for region, attributes in self.region_detail_mesh_attributes.items():
            execute_shader(
                self.window_render_target,
                self.shader,
                PrimitiveMode.TRIANGLE,
                attributes,
                {
                    "camera_transform": self.camera.view_projection_transform,
                    "model_transform": FMatrix4(1),
                    "normal_model_transform": FMatrix3(1),
                    "color": self.region_color[region],
                },
                index_range=(0, len(attributes["pos"])),
                depth_write=True,
                depth_test=DepthTest.LESS,
            )
        """

        """
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
        """

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


INSTANCE_VERTEX_SHADER: Final = b"""
#version 140
in vec3 pos;
in vec3 norm;
in mat4 instance_transform;
in vec3 instance_color;
out vec3 normal;
out vec3 position;
out vec3 color;
uniform mat4 camera_transform;
uniform mat4 model_transform;
uniform mat3 normal_model_transform;
void main()
{
    normal = normalize(normal_model_transform * norm);
    vec4 world_position = instance_transform * model_transform * vec4(pos, 1.0);
    position = world_position.xyz;
    color = instance_color;
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


INSTANCE_FRAGMENT_SHADER: Final = b"""
#version 140
in vec3 color;
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
    print("----")
