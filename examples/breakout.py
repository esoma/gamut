
# gamut
from gamut import Application, Timer, TimerExpired, Window
from gamut.audio import Listener, MultiSpeaker, Sound
from gamut.event import Bind
from gamut.graphics import (BlendFactor, Buffer, BufferFrequency, BufferView,
                            BufferViewMap, clear_render_target, Color,
                            create_quad_position_array, execute_shader,
                            PrimitiveMode, Shader, WindowRenderTarget)
from gamut.math import (FMatrix4, FVector2, FVector3, FVector4, FVector4Array,
                        UVector2)
from gamut.peripheral import MouseButtonPressed, MouseConnected, MouseMoved
from gamut.text import AtlasFont, Face, RenderedGlyphFormat
# python
from datetime import timedelta
import gc
from pathlib import Path
from random import randrange
import traceback
from typing import Final
import warnings
# pyglm
from glm import ortho

DIR: Final = Path(__file__).parent


class Draw(TimerExpired):
    pass


class Brick:

    HITS_TO_COLOR: Final = {
        0: FVector4(0, 0, 0, 0),
        1: FVector4(0.764, 0.956, 0.933, 1),
        2: FVector4(0.572, 0.890, 0.682, 1),
        3: FVector4(0.737, 0.870, 0.486, 1),
        4: FVector4(0.878, 0.764, 0.403, 1),
        5: FVector4(0.886, 0.301, 0.250, 1),
    }

    def __init__(
        self,
        index: int,
        row: int, column: int,
        hits: int,
        size: FVector2,
        y_offset: int
    ):
        size = FVector2(size.x, -size.y)
        self.index = index
        self.top_left = FVector2(size.x * column, (size.y * row) + y_offset)
        self.bottom_right = self.top_left + size
        self.hits = hits
        self.update_color()
        self.is_active = True

    def __repr__(self) -> str:
        return f'<Brick {tuple(self.top_left)} {tuple(self.bottom_right)}>'

    def update_color(self) -> None:
        self.color = self.HITS_TO_COLOR[self.hits]


class App(Application):

    SCREEN_SIZE: Final = UVector2(800, 800)
    MAX_BALLS_SPEED: Final = 750

    ball_transform: FMatrix4

    async def main(self) -> None:
        try:
            mouse = self.mice[0]
        except IndexError:
            mouse = (await MouseConnected).mouse

        self.window = Window()
        self.window.title = 'Gamut Breakout Example'
        self.window.resize(self.SCREEN_SIZE)
        self.window.recenter()
        self.window.is_visible = True
        self.window_render_target = WindowRenderTarget(self.window)
        self.projection = FMatrix4(*(FVector4(*c) for c in ortho(
            0, self.window.size[0],
            0, self.window.size[1],
            -1000, 1000
        )))

        self.listener = Listener(gain=.25)
        self.listener.activate()
        self.speaker = MultiSpeaker()
        self.boop_sample = Sound(DIR / 'resources/boop.wav').to_sample()
        self.bwop_sample = Sound(DIR / 'resources/bwop.wav').to_sample()
        self.lose_sample = Sound(DIR / 'resources/lose.wav').to_sample()

        self.face = Face(DIR / 'resources/ArcadeClassic.ttf')
        self.small_font = AtlasFont(
            self.face.request_pixel_size(28),
            RenderedGlyphFormat.ALPHA,
        )

        self.shader = Shader(vertex=b"""
            #version 140
            in vec4 pos;
            uniform mat4 transform;
            void main()
            {
                gl_Position = transform * vec4(pos);
            }
            """, fragment=b"""
            #version 140
            uniform vec4 color;
            out vec4 output_color;
            void main()
            {
                output_color = color;
            }
            """
        )
        self.bricks_shader = Shader(vertex=b"""
            #version 140
            in vec4 pos;
            in vec4 color;
            out vec4 vertex_color;
            uniform mat4 transform;
            void main()
            {
                vertex_color = color;
                gl_Position = transform * vec4(pos);
            }
            """, fragment=b"""
            #version 140
            in vec4 vertex_color;
            out vec4 output_color;
            void main()
            {
                output_color = vertex_color;
            }
            """
        )
        self.text_shader = Shader(vertex=b"""
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
            """, fragment=b"""
            #version 140
            in vec2 vertex_uv;
            uniform vec4 color;
            uniform sampler2D tex;
            out vec4 output_color;
            void main()
            {
                output_color = vec4(
                    color.rgb,
                    texture(tex, vertex_uv).r * color.a
                );
            }
            """
        )
        self.reset()
        # run the game
        with (
            Bind.on(Draw, self.draw),
            Bind.on(MouseMoved, self.mouse_moved),
            Bind.on(mouse.Button.left.Pressed, self.mouse_left_pressed)
        ):
            draw_timer = Timer(
                self,
                timedelta(seconds=1 / 60.0),
                Draw,
                repeat=True,
                fixed=True,
            )
            await self.window.Close

    def reset(self) -> None:
        self.lives = 3
        self.update_lives_text()
        # setup the bricks
        self.brick_columns = 10
        self.brick_rows = 10
        self.brick_size = FVector2(
            self.SCREEN_SIZE[0] / self.brick_columns,
            self.SCREEN_SIZE[1] / 30.0
        )
        self.bricks = [
            Brick(
                i,
                r, c,
                (r * c) % 5 + 1,
                self.brick_size,
                self.SCREEN_SIZE[1]
            )
            for i, (c, r) in
            enumerate((
                (c, r)
                for c in range(self.brick_columns)
                for r in range(self.brick_rows)
            ))
        ]
        self.bricks_primitive_mode = PrimitiveMode.TRIANGLE
        bricks_pos_data = bytearray()
        for brick in self.bricks:
            bricks_pos_data += create_quad_position_array(
                self.bricks_primitive_mode,
                left=brick.top_left.x,
                right=brick.bottom_right.x,
                top=brick.top_left.y,
                bottom=brick.bottom_right.y
            )
        self.bricks_color_buffer = Buffer(
            FVector4Array(*(
                brick.color for brick in self.bricks for _ in range(6)
            )),
            frequency=BufferFrequency.DYNAMIC,
        )
        self.bricks_buffer_view_map = BufferViewMap({
            "pos": BufferView(Buffer(bricks_pos_data), FVector4),
            "color": BufferView(self.bricks_color_buffer, FVector4)
        })
        # setup the ball
        self.ball_active = False
        self.ball_velocity = FVector2(0, 0)
        self.ball_primitive_mode = PrimitiveMode.TRIANGLE_FAN
        self.ball_color = FVector4(0.294, 0.498, 0.945, 1)
        self.ball_size = FVector2(
            self.SCREEN_SIZE[0] / 30.0,
            self.SCREEN_SIZE[1] / 30.0
        )
        self.ball_buffer_view_map = BufferViewMap({
            "pos": BufferView(Buffer(
                create_quad_position_array(
                    self.ball_primitive_mode,
                    left=self.ball_size.x / -2.0, right=self.ball_size.x / 2.0,
                    bottom=self.ball_size.y / -2.0, top=self.ball_size.y / 2.0,
                )
            ), FVector4)
        })
        # setup the paddle
        self.paddle_x_velocity = 0.0
        self.paddle_primitive_mode = PrimitiveMode.TRIANGLE_FAN
        self.paddle_color = FVector4(1, 1, 1, 1)
        self.paddle_size = FVector2(
            self.SCREEN_SIZE[0] / 6.0,
            self.SCREEN_SIZE[1] / 30.0
        )
        self.paddle_buffer_view_map = BufferViewMap({
            "pos": BufferView(Buffer(
                create_quad_position_array(
                    self.paddle_primitive_mode,
                    left=0, right=self.paddle_size.x,
                    bottom=0, top=self.paddle_size.y,
                )
            ), FVector4)
        })
        self.update_paddle_transform(self.SCREEN_SIZE[0] / 2.0)
        self.paddle_previous_x = (self.paddle_transform @ FVector3(0)).x


    def play_boop(self) -> None:
        self.speaker.play(self.boop_sample)

    def step_physics(self, duration: timedelta) -> None:
        paddle_current_x = (self.paddle_transform @ FVector3(0)).x
        self.paddle_x_velocity = (
            abs(self.paddle_previous_x) - abs(paddle_current_x)
        )
        self.paddle_previous_x = paddle_current_x
        if self.ball_active:
            ball_step_velocity = self.ball_velocity * duration.total_seconds()
            self.do_ball_physics(ball_step_velocity)

    def activate_ball(self) -> None:
        if self.ball_active:
            return
        self.ball_active = True
        self.ball_velocity = FVector2(
            randrange(-self.MAX_BALLS_SPEED // 2, self.MAX_BALLS_SPEED // 2),
            self.MAX_BALLS_SPEED
        )

    def do_ball_physics(self, ball_step_velocity: FVector2) -> None:
        ball_position = (
            (self.ball_transform @ FVector3(0)) +
            FVector3(ball_step_velocity.x, ball_step_velocity.y, 0)
        )
        current_ball_position = self.ball_transform @ FVector3(0)
        current_ball_bottom = (
            current_ball_position.y -
            (self.ball_size[1] / 2.0)
        )
        current_ball_top = (
            current_ball_position.y +
            (self.ball_size[1] / 2.0)
        )
        current_ball_left = (
            current_ball_position.x -
            (self.ball_size[0] / 2.0)
        )
        current_ball_right = (
            current_ball_position.x +
            (self.ball_size[0] / 2.0)
        )
        ball_bottom = ball_position.y - (self.ball_size[1] / 2.0)
        ball_top = ball_position.y + (self.ball_size[1] / 2.0)
        ball_left = ball_position.x - (self.ball_size[0] / 2.0)
        ball_right = ball_position.x + (self.ball_size[0] / 2.0)
        # check if the ball will go outside the collidable bounds of the screen
        if ball_top >= self.SCREEN_SIZE[0]:
            self.ball_velocity *= FVector2(1, -1)
            ball_step_velocity += FVector2(0, self.SCREEN_SIZE[0] - ball_top)
            self.play_boop()
        if ball_left <= 0:
            self.ball_velocity *= FVector2(-1, 1)
            ball_step_velocity -= FVector2(ball_left, 0)
            self.play_boop()
        if ball_right >= self.SCREEN_SIZE[1]:
            self.ball_velocity *= FVector2(-1, 1)
            ball_step_velocity += FVector2(self.SCREEN_SIZE[1] - ball_right, 0)
            self.play_boop()
        # check if the ball will collide with the paddle
        paddle_position = self.paddle_transform @ FVector3(0)
        paddle_left = paddle_position.x
        paddle_right = paddle_position.x + self.paddle_size.x
        if (ball_step_velocity.y < 0 and
            current_ball_bottom >= self.paddle_size.y and
            ball_bottom <= self.paddle_size.y and
            ball_left <= paddle_right and ball_right >= paddle_left):
            self.play_boop()
            ball_step_velocity += FVector2(0, self.paddle_size.y - ball_bottom)
            self.ball_velocity *= FVector2(1, -1)
            self.ball_velocity -= FVector2(self.paddle_x_velocity * 50, 0)
            self.ball_velocity = FVector2(
                max(
                    min(self.ball_velocity.x, self.MAX_BALLS_SPEED),
                    -self.MAX_BALLS_SPEED
                ),
                self.ball_velocity.y
            )
        # check if the ball went outside the bottom of the screen
        if ball_top <= 0:
            self.lost_ball()
            return
        # check if the ball hit any bricks
        lowest_brick_bottom = (
            self.SCREEN_SIZE[0] - (self.brick_size[1] * self.brick_rows)
        )
        if ball_top >= lowest_brick_bottom:
            for brick in self.bricks:
                if not brick.is_active:
                    continue
                # ball hits bottom of brick
                if (ball_step_velocity.y > 0 and
                    current_ball_top <= brick.bottom_right.y and
                    ball_top >= brick.bottom_right.y and
                    ball_left <= brick.bottom_right.x and
                    ball_right >= brick.top_left.x
                ):
                    self.ball_velocity *= FVector2(1, -1)
                    ball_step_velocity += FVector2(
                        0, brick.bottom_right.y - ball_top
                    )
                    self.hit_brick(brick)
                    break
                # ball hits top of brick
                if (ball_step_velocity.y < 0 and
                    current_ball_bottom >= brick.top_left.y and
                    ball_bottom <= brick.top_left.y and
                    ball_left <= brick.bottom_right.x and
                    ball_right >= brick.top_left.x
                ):
                    self.ball_velocity *= FVector2(1, -1)
                    ball_step_velocity -= FVector2(
                        0, brick.top_left.y - ball_bottom
                    )
                    self.hit_brick(brick)
                    break

                # ball hits left side of brick
                if (ball_step_velocity.x > 0 and
                    current_ball_right <= brick.top_left.x and
                    ball_right >= brick.top_left.x and
                    ball_top >= brick.bottom_right.y and
                    ball_bottom <= brick.top_left.y
                ):
                    self.ball_velocity *= FVector2(-1, 1)
                    ball_step_velocity += FVector2(
                        brick.top_left.x - ball_right,
                        0
                    )
                    self.hit_brick(brick)
                    break
                # ball hits right side of brick
                if (ball_step_velocity.x < 0 and
                    current_ball_left >= brick.bottom_right.x and
                    ball_left <= brick.bottom_right.x and
                    ball_top >= brick.bottom_right.y and
                    ball_bottom <= brick.top_left.y
                ):
                    self.ball_velocity *= FVector2(-1, 1)
                    ball_step_velocity -= FVector2(
                        brick.bottom_right.x - ball_left,
                        0
                    )
                    self.hit_brick(brick)
                    break
        self.ball_transform = self.ball_transform.translate(
            FVector3(ball_step_velocity.x, ball_step_velocity.y, 0)
        )

    def lost_ball(self) -> None:
        paddle_position = self.paddle_transform @ FVector3(0)
        self.ball_active = False
        self.ball_velocity = FVector2(0)
        self.update_paddle_transform(
            paddle_position.x + (self.paddle_size.x / 2.0)
        )
        self.lives -= 1
        self.update_lives_text()
        self.speaker.play(self.lose_sample)
        if self.lives == 0:
            self.reset()

    def hit_brick(self, brick: Brick) -> None:
        assert brick.is_active
        brick.hits -= 1
        brick.update_color()
        if brick.hits == 0:
            brick.is_active = False
        colors = FVector4Array(*(brick.color for _ in range(6)))
        self.bricks_color_buffer.replace(
            brick.index * FVector4.get_size() * 6,
            colors,
        )
        self.speaker.play(self.bwop_sample)
        if all(not brick.is_active for brick in self.bricks):
            self.reset()

    def update_lives_text(self) -> None:
        self.lives_text_buffers = self.small_font.buffer_text(
            f'{self.lives} lives'
        )

    def update_paddle_transform(self, x: float) -> None:
        # clamp so that it doesn't go outside the bounds of the screen
        x -= self.paddle_size.x / 2.0
        x = max(min(x, self.SCREEN_SIZE[0] - self.paddle_size.x), 0)
        self.paddle_transform = FMatrix4(1).translate(FVector3(x, 0, 0))
        # update the ball position to the paddle if its not active
        if not self.ball_active:
            self.ball_transform = FMatrix4(1).translate(
                FVector3(
                    x + (self.paddle_size.x / 2.0),
                    self.paddle_size.y + (self.ball_size.y / 2.0),
                    0
                )
            )

    async def mouse_left_pressed(
        self,
        mouse_button_pressed: MouseButtonPressed
    ) -> None:
        self.activate_ball()

    async def mouse_moved(self, mouse_moved: MouseMoved) -> None:
        if mouse_moved.position is None:
            return
        self.update_paddle_transform(mouse_moved.position[0])

    async def draw(self, draw: Draw) -> None:
        self.step_physics(draw.when - draw.previous)
        clear_render_target(self.window_render_target, color=Color(0, 0, 0))
        # draw the bricks
        execute_shader(
            self.window_render_target,
            self.bricks_shader,
            self.bricks_primitive_mode,
            self.bricks_buffer_view_map,
            {
                "transform": self.projection,
            },
            index_range=(0, len(self.bricks_buffer_view_map["pos"]))
        )
        # draw the paddle
        execute_shader(
            self.window_render_target,
            self.shader,
            self.paddle_primitive_mode,
            self.paddle_buffer_view_map,
            {
                "color": self.paddle_color,
                "transform": self.projection @ self.paddle_transform,
            },
            index_range=(0, len(self.paddle_buffer_view_map["pos"]))
        )
        # draw the ball
        execute_shader(
            self.window_render_target,
            self.shader,
            self.ball_primitive_mode,
            self.ball_buffer_view_map,
            {
                "color": self.ball_color,
                "transform": self.projection @ self.ball_transform,
            },
            index_range=(0, len(self.ball_buffer_view_map["pos"]))
        )
        # draw the lives text
        for texture, (pos, uv) in self.lives_text_buffers.items():
            execute_shader(
                self.window_render_target,
                self.text_shader,
                PrimitiveMode.TRIANGLE,
                BufferViewMap({
                    "pos": pos,
                    "uv": uv,
                }),
                {
                    "color": FVector4(0, 0, 0, 1),
                    "tex": texture,
                    "transform":
                        self.projection @
                        self.paddle_transform.translate(
                            FVector3(20, self.paddle_size[1], 0)
                        ),
                },
                index_range=(0, len(pos)),
                blend_source=BlendFactor.SOURCE_ALPHA,
                blend_destination=BlendFactor.ONE_MINUS_SOURCE_ALPHA,
            )
        self.window.flip_buffer()


if __name__ == '__main__':
    app = App()
    try:
        app.run()
    except Exception as ex:
        traceback.print_exception(ex)
        warnings.simplefilter('ignore')
    del app
    gc.collect()
