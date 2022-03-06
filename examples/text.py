
# gamut
from gamut import Application, Timer, TimerExpired, TransformNode, Window
from gamut.event import Bind
from gamut.graphics import (BlendFactor, BufferViewMap, clear_render_target,
                            Color, execute_shader, PrimitiveMode, Shader,
                            WindowRenderTarget)
from gamut.peripheral import (KeyboardConnected, KeyboardKeyPressed,
                              MouseConnected, MouseMoved)
from gamut.text import AtlasFont, Face, RenderedGlyphFormat
# python
from datetime import timedelta
from pathlib import Path
from typing import Any, Final
# pyglm
from glm import (cos, cross, lookAt, mat4, normalize, ortho, perspective, pi,
                 radians, scale, sin, translate, vec3, vec4)

RESOURCES: Final = Path(__file__).parent / 'resources'


class Draw(TimerExpired):
    pass


class App(Application):

    async def main(self) -> None:
        self.window = Window()
        self.window.title = 'Gamut Text Example'
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

        self.ortho_projection = ortho(0, 800, 0, 800, -1000, 1000)

        self.player_position = vec3(0, 0, 5)
        self.player_yaw = -pi() / 2
        self.player_pitch = 0.0
        self.player_node: TransformNode[Any] = TransformNode()
        self.projection = perspective(radians(45), 1, .1, 100)

        self.shader = Shader(vertex=vertex_shader, fragment=fragment_shader)
        face = Face(RESOURCES / 'OpenSans-Regular.ttf')
        font = AtlasFont(
            face.request_pixel_size(height=64),
            RenderedGlyphFormat.ALPHA
        )
        self.text_buffers = font.buffer_text('hello world')

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

        clear_render_target(
            self.window_render_target,
            color=Color(0, 0, 0),
        )
        # '3D' "hello world"
        for texture, (pos, uv) in self.text_buffers.items():
            execute_shader(
                self.window_render_target,
                self.shader,
                PrimitiveMode.TRIANGLE,
                BufferViewMap({
                    "pos": pos,
                    "uv": uv,
                }),
                {
                    "transform": (
                        self.projection * self.player_node.transform *
                        scale(
                            translate(
                                mat4(1),
                                vec3(-1.5, 1, -5),
                            ),
                            vec3(.01, .01, 1)
                        )
                    ),
                    "tex": texture,
                    "color": vec4(.5, 1, 1, 1),
                },
                index_range=(0, len(pos)),
                blend_source=BlendFactor.SOURCE_ALPHA,
                blend_destination=BlendFactor.ONE_MINUS_SOURCE_ALPHA,
            )
        # orthographic "hello world"
        for texture, (pos, uv) in self.text_buffers.items():
            execute_shader(
                self.window_render_target,
                self.shader,
                PrimitiveMode.TRIANGLE,
                BufferViewMap({
                    "pos": pos,
                    "uv": uv,
                }),
                {
                    "transform": (
                        self.ortho_projection *
                        translate(
                            mat4(1),
                            vec3(0, 800, 0)
                        )
                    ),
                    "tex": texture,
                    "color": vec4(1, 1, 1, 1),
                },
                index_range=(0, len(pos)),
                blend_source=BlendFactor.SOURCE_ALPHA,
                blend_destination=BlendFactor.ONE_MINUS_SOURCE_ALPHA,
            )

        self.window.flip_buffer()


vertex_shader = b"""
#version 140
in vec4 pos;
in vec2 uv;
uniform mat4 transform;
out vec2 vertex_uv;
void main()
{
    vertex_uv = uv;
    gl_Position = transform * vec4(pos);
}
"""


fragment_shader = b"""
#version 140
in vec2 vertex_uv;
uniform vec4 color;
uniform sampler2D tex;
out vec4 output_color;
void main()
{
    output_color = vec4(color.rgb, texture(tex, vertex_uv).r * color.a);
}
"""


if __name__ == '__main__':
    app = App()
    app.run()
