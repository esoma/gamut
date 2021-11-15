
# gamut
from gamut import Application, Timer, TimerExpired, TransformNode, Window
from gamut.event import Bind
from gamut.graphics import (Buffer, BufferView, BufferViewMap,
                            clear_render_target, Color, DepthTest,
                            execute_shader, FaceCull, Image, PrimitiveMode,
                            Shader, WindowRenderTarget)
from gamut.peripheral import (KeyboardConnected, KeyboardKeyPressed,
                              MouseConnected, MouseMoved)
# python
from datetime import timedelta
from pathlib import Path
from typing import Final
# pyglm
from glm import (array, cos, cross, lookAt, mat4, normalize, perspective, pi,
                 rotate, sin, translate, uint8, vec2, vec3)

DIR: Final = Path(__file__).parent


CUBES_X: Final = 100
CUBES_Y: Final = 100
CUBES_Z: Final = 100


class Draw(TimerExpired):
    pass


class App(Application):

    async def main(self) -> None:
        self.window = Window()
        self.window.title = 'Gamut Instancing Example'
        self.window.resize(800, 800)
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

        self.player_position = vec3(0, 0, 200)
        self.player_yaw = -pi() / 2
        self.player_pitch = 0.0
        self.player_node = TransformNode()
        self.camera_node = TransformNode(
            local_transform=perspective(45, 1, 1.0, -1.0),
            parent=self.player_node
        )

        self.shader = Shader(vertex=vertex_shader, fragment=fragment_shader)
        self.cube_transform = mat4(1)
        self.cube_attributes = BufferViewMap({
            "pos": BufferView(
                Buffer(array(
                    vec3(-1, -1, -1),
                    vec3(1, -1, -1),
                    vec3(1, 1, -1),
                    vec3(-1, 1, -1),
                    vec3(-1, -1, 1),
                    vec3(1, -1, 1),
                    vec3(1, 1, 1),
                    vec3(-1, 1, 1),
                ).to_bytes()),
                vec3,
            ),
            "uv": BufferView(
                Buffer(array(
                    vec2(0, 0),
                    vec2(1, 0),
                    vec2(1, 1),
                    vec2(0, 1),
                    vec2(1, 1),
                    vec2(0, 1),
                    vec2(0, 0),
                    vec2(1, 0),
                ).to_bytes()),
                vec2
            ),
            "instance_transform": BufferView(
                Buffer(array(*(
                    translate(vec3(x * 4, y * 4, z * -4))
                    for x in range(CUBES_X)
                    for y in range(CUBES_Y)
                    for z in range(CUBES_Z)
                )).to_bytes()),
                mat4,
                instancing_divisor=1,
            ),
        })
        self.cube_index_buffer_view = BufferView(
            Buffer(array.from_numbers(uint8,
                0, 2, 1, 2, 0, 3,
                4, 5, 6, 6, 7, 4,
                1, 6, 5, 6, 1, 2,
                0, 7, 3, 7, 0, 4,
                0, 5, 4, 5, 0, 1,
                3, 7, 6, 6, 2, 3,
            ).to_bytes()),
            uint8
        )
        self.cube_texture = Image(DIR / 'yee.jpg').to_texture()

        with (
            Bind.on(self.keyboard.Key.escape.Pressed, self.escape),
            Bind.on(Draw, self.draw),
            Bind.on(MouseMoved, self.mouse_moved)
        ):
            step_timer = Timer(
                self,
                timedelta(seconds=1 / 60.0),
                Draw,
                repeat=True
            )
            await self.window.Close

    async def escape(self, key_pressed: KeyboardKeyPressed) -> None:
        self.window.Close().send()

    async def mouse_moved(self, mouse_moved: MouseMoved) -> None:
        if mouse_moved.delta is not None:
            self.player_yaw += mouse_moved.delta[0] * .005
            self.player_pitch -= mouse_moved.delta[1] * .005

    async def draw(self, draw: Draw) -> None:
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
            .5
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

        self.cube_transform *= rotate(.02, vec3(1, 1, 1))

        clear_render_target(
            self.window_render_target,
            color=Color(0, 0, 0),
            depth=0
        )
        execute_shader(
            self.window_render_target,
            self.shader,
            PrimitiveMode.TRIANGLE,
            self.cube_attributes,
            {
                "camera_transform": self.camera_node.transform,
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


vertex_shader = b"""
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


fragment_shader = b"""
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
    app = App()
    app.run()
