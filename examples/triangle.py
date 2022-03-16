
# gamut
from gamut import Application, Timer, TimerExpired, Window
from gamut.event import Bind
from gamut.graphics import (Buffer, BufferView, BufferViewMap,
                            clear_render_target, Color, execute_shader,
                            PrimitiveMode, Shader, WindowRenderTarget)
from gamut.math import (FMatrix4, FVector2, FVector2Array, FVector3,
                        FVector3Array, UVector2)
# python
from datetime import timedelta


class Draw(TimerExpired):
    pass


class App(Application):

    async def main(self) -> None:
        self.window = Window()
        self.window.title = 'Gamut Triangle Example'
        self.window.resize(UVector2(400, 400))
        self.window.recenter()
        self.window.is_visible = True
        self.window_render_target = WindowRenderTarget(self.window)

        self.shader = Shader(vertex=vertex_shader, fragment=fragment_shader)
        self.triangle_transform = FMatrix4(1)
        self.triangle_attributes = BufferViewMap({
            "pos": BufferView(
                Buffer(FVector2Array(
                    FVector2(-.5, -.5),
                    FVector2(0, .5),
                    FVector2(.5, -.5),
                )),
                FVector2,
            ),
            "color": BufferView(
                Buffer(FVector3Array(
                    FVector3(1, 0, 0),
                    FVector3(0, 1, 0),
                    FVector3(0, 0, 1),
                )),
                FVector3,
            ),
        })

        with Bind.on(Draw, self.draw):
            step_timer = Timer(
                self,
                timedelta(seconds=1 / 60.0),
                Draw,
                repeat=True,
                fixed=True,
            )
            await self.window.Close

    async def draw(self, draw: Draw) -> None:
        clear_render_target(
            self.window_render_target,
            color=Color(0, 0, 0),
            depth=0,
        )
        self.triangle_transform = self.triangle_transform.rotate(
            .02,
            FVector3(0, 0, -1)
        )
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
