
# gamut
from gamut import Application, Timer, TimerExpired, Window
from gamut.event import Bind
from gamut.graphics import (Buffer, BufferView, BufferViewMap,
                            clear_render_target, Color, execute_shader,
                            PrimitiveMode, Shader, WindowRenderTarget)
# python
from datetime import timedelta
# pyglm
from glm import array, mat4, rotate, vec2, vec3


class Draw(TimerExpired):
    pass


class App(Application):

    async def main(self) -> None:
        self.window = Window()
        self.window.title = 'Gamut Triangle Example'
        self.window.resize(400, 400)
        self.window.recenter()
        self.window.is_visible = True
        self.window_render_target = WindowRenderTarget(self.window)

        self.shader = Shader(vertex=vertex_shader, fragment=fragment_shader)
        self.triangle_transform = mat4(1)
        self.triangle_attributes = BufferViewMap({
            "pos": BufferView(
                Buffer(array(
                    vec2(-.5, -.5),
                    vec2(0, .5),
                    vec2(.5, -.5),
                ).to_bytes()),
                vec2,
            ),
            "color": BufferView(
                Buffer(array(
                    vec3(1, 0, 0),
                    vec3(0, 1, 0),
                    vec3(0, 0, 1),
                ).to_bytes()),
                vec3,
            ),
        })

        with Bind.on(Draw, self.draw):
            step_timer = Timer(
                self,
                timedelta(seconds=1 / 60.0),
                Draw,
                repeat=True
            )
            await self.window.Close

    async def draw(self, draw: Draw) -> None:
        clear_render_target(
            self.window_render_target,
            color=Color(0, 0, 0),
            depth=0,
        )
        self.triangle_transform *= rotate(.02, vec3(0, 0, -1))
        execute_shader(
            self.window_render_target,
            self.shader,
            PrimitiveMode.TRIANGLE,
            self.triangle_attributes,
            {"transform": self.triangle_transform},
            index_range=(0, 3)
        )
        self.window.flip_buffer()


vertex_shader = b"""
#version 140
in vec2 pos;
in vec3 color;
out vec3 vertex_color;
uniform mat4 transform;
void main()
{
    vertex_color = color;
    gl_Position = transform * vec4(pos, 0, 1.0);
}
"""


fragment_shader = b"""
#version 140
in vec3 vertex_color;
out vec4 output_color;
void main()
{
    output_color = vec4(vertex_color, 1);
}
"""


if __name__ == '__main__':
    app = App()
    app.run()
