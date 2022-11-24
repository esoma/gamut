
# gamut
from gamut.ai import NavigationMesh3d
from gamut.ai._navigationmesh3d import Debug as NavigationMesh3dDebug
from gamut.event import Bind
from gamut.geometry import LineSegment3d, Mesh3d, RectangularCuboid, Triangle3d
from gamut.gltf import Gltf
from gamut.graphics import (BufferView, BufferViewMap, clear_render_target,
                            DepthTest, execute_shader, FaceCull, PrimitiveMode,
                            Shader)
from gamut.math import (DVector3, DVector3Array, FMatrix3, FMatrix4,
                        FMatrix4Array, FVector2, FVector3, FVector3Array,
                        UVector1, UVector1Array, UVector3Array)
from gamut.navigation._navigation import (CompactHeightField, ContourSet,
                                          HeightField)
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

        with open('examples/resources/navmesh.glb', 'rb') as f:
            navmesh_gltf = Gltf(f)
        navmesh_attrs = navmesh_gltf.meshes[0].primitives[0].attributes
        navmesh_indices = navmesh_gltf.meshes[0].primitives[0].indices.data
        navmesh_positions = navmesh_attrs["POSITION"].data
        self.navmesh_attributes = BufferViewMap({
            "pos": BufferView.from_array(navmesh_positions),
            "norm": BufferView.from_array(navmesh_attrs["NORMAL"].data)
        })
        self.navmesh_index_buffer_view = BufferView.from_array(navmesh_indices)

        # HEIGHT FIELD
        cell_size = .25
        cell_height = .25
        hf = HeightField(
            200,
            200,
            FVector3(-15, -1, -15),
            FVector3(15, 5, 15),
            cell_size, cell_height,
            1, 2
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
        #chf.partition_watershed(0, 1, 1)
        #chf.partition_monotone(0, 1, 0)
        chf.partition_layers(5, 10)

        chf_cube = RectangularCuboid(FVector3(0), FVector3(1))
        chf_cube_positions, chf_cube_normals, _, chf_cube_indices = chf_cube.render()
        self.chf_cube_transforms = [
            FMatrix4(1).translate(s[0] + ((s[1] - s[0]) * .5)).scale(s[1] - s[0])
            for s in chf.spans if s[2]
        ]
        # TODO: add isort heading
        import distinctipy
        region_color = {s[3]: None for s in chf.spans}
        colors = [FVector3(*c) for c in distinctipy.get_colors(len(region_color), [(0, 0, 0), (1, 1, 1)])]
        for i, k in enumerate(region_color.keys()):
            region_color[k] = colors[i]
        self.chf_cube_colors = [
            region_color[s[3]]
            for s in chf.spans if s[2]
        ]
        print("?")
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


        cs = ContourSet(chf, 5.0, 1)
        print(cs)

        print("___")

    async def mouse_moved(self, mouse_moved: MouseMoved) -> None:
        pass

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
        execute_shader(
            self.window_render_target,
            self.instance_shader,
            PrimitiveMode.TRIANGLE,
            self.hf_attributes,
            {
                "camera_transform": self.camera.view_projection_transform,
                "model_transform": FMatrix4(1),
                "normal_model_transform": FMatrix3(1),
                "color": FVector3(1, 0, 0),
            },
            index_buffer_view=self.hf_index_buffer_view,
            depth_write=True,
            depth_test=DepthTest.LESS,
            face_cull=FaceCull.BACK,
            instances=len(self.hf_cube_positions)
        )
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
