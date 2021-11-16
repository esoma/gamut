
# gamut
from gamut import Application, Timer, TimerExpired, TransformNode, Window
from gamut.event import Bind
from gamut.graphics import (BlendFactor, Buffer, BufferView, BufferViewMap,
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
from glm import (array, cos, cross, float32, lookAt, mat4, normalize,
                 perspective, pi, rotate, scale, sin, uint8, vec2, vec3)

DIR: Final = Path(__file__).parent


class Draw(TimerExpired):
    pass


class App(Application):

    async def main(self) -> None:
        self.window = Window()
        self.window.title = 'Gamut Transparency Example'
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

        self.player_position = vec3(0, 0, 10)
        self.player_yaw = -pi() / 2
        self.player_pitch = 0.0
        self.player_node = TransformNode()
        self.camera_node = TransformNode(
            local_transform=perspective(45, 1, 1.0, -1.0),
            parent=self.player_node
        )

        self.shader = Shader(vertex=vertex_shader, fragment=fragment_shader)
        self.cube_transform = mat4(1)
        self.outer_cube_transform = scale(vec3(2, 2, 2))
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
            )
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

        self.cube_transform *= rotate(.02, vec3(1, 1, 1))
        self.outer_cube_transform *= rotate(-.04, vec3(1, 1, 1))

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
                "alpha": float32(1.0),
            },
            index_buffer_view=self.cube_index_buffer_view,
            depth_write=True,
            depth_test=DepthTest.LESS,
            face_cull=FaceCull.BACK,
        )

        execute_shader(
            self.window_render_target,
            self.shader,
            PrimitiveMode.TRIANGLE,
            self.cube_attributes,
            {
                "camera_transform": self.camera_node.transform,
                "model_transform": self.outer_cube_transform,
                "tex": self.cube_texture,
                "alpha": float32(.5),
            },
            index_buffer_view=self.cube_index_buffer_view,
            depth_write=True,
            depth_test=DepthTest.LESS,
            face_cull=FaceCull.BACK,
            blend_source=BlendFactor.SOURCE_ALPHA,
            blend_destination=BlendFactor.ONE_MINUS_SOURCE_ALPHA,
        )

        self.window.flip_buffer()


vertex_shader = b"""
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


fragment_shader = b"""
#version 140
in vec2 vertex_uv;
out vec4 output_color;
uniform sampler2D tex;
uniform float alpha;
void main()
{
    output_color = texture(tex, vertex_uv) * vec4(1, 1, 1, alpha);
}
"""


if __name__ == '__main__':
    app = App()
    app.run()
