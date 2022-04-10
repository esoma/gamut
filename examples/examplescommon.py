
from __future__ import annotations

__all__ = ['ExampleApplication', 'RESOURCES', 'run_application']

# gamut
from gamut import Application, Camera, Timer, TimerExpired, Window
from gamut.event import Bind
from gamut.graphics import WindowRenderTarget
from gamut.math import FMatrix4, FVector3, UVector2
from gamut.peripheral import KeyboardConnected, MouseConnected
# python
from datetime import timedelta
import gc
from math import cos, radians, sin
from pathlib import Path
import traceback
from typing import Final
import warnings

RESOURCES: Final = Path(__file__).parent / 'resources'


class ExampleApplication(Application):

    class Step(TimerExpired):
        pass

    async def main(self) -> None:
        self.window = Window()
        self.window.resize(UVector2(800, 800))
        self.window.recenter()
        self.window.is_visible = True
        self.window_render_target = WindowRenderTarget(self.window)

        self.camera = Camera(FMatrix4.perspective(radians(45), 1, .1, 100))
        self.camera_position = FVector3(0, 0, 5)
        self.camera_pitch = 0
        self.camera_yaw = 0
        self.update_camera_transform()

        try:
            self.keyboard = self.keyboards[0]
        except IndexError:
            self.keyboard = (await KeyboardConnected).keyboard
        try:
            self.mouse = self.mice[0]
        except IndexError:
            self.mouse = (await MouseConnected).mouse
        self.mouse.is_relative = True

        await self.example_main()

        with (
            Bind.on(self.keyboard.Key.escape.Pressed, self.escape),
            Bind.on(self.Step, self.step),
            Bind.on(self.mouse.Moved, self.mouse_moved)
        ):
            self.step_timer = Timer(
                self,
                timedelta(seconds=1 / 60.0),
                self.Step,
                repeat=True,
                fixed=True,
            )
            await self.window.Close

    async def escape(self, key_pressed: KeyboardKeyPressed) -> None:
        self.window.Close().send()

    async def mouse_moved(self, mouse_moved: MouseMoved) -> None:
        if mouse_moved.delta is not None:
            self.camera_yaw += mouse_moved.delta[0] * .005
            self.camera_pitch += mouse_moved.delta[1] * .005
            self.update_camera_transform()

    def move_camera(self, step: Step) -> None:
        speed = (
            (step.when - step.previous).total_seconds() /
            (1 / 60.0) *
            .1
        )
        direction = FVector3(
            sin(-self.camera_yaw) * cos(self.camera_pitch),
            sin(self.camera_pitch),
            cos(self.camera_yaw) * cos(self.camera_pitch),
        ).normalize()
        cross_direction = direction.cross(FVector3(0, 1, 0)).normalize()

        keys = self.keyboard.Key
        if keys.up.is_pressed or keys.w.is_pressed:
            self.camera_position -= speed * direction
        if keys.down.is_pressed or keys.s.is_pressed:
            self.camera_position += speed * direction
        if keys.left.is_pressed or keys.a.is_pressed:
            self.camera_position += speed * cross_direction
        if keys.right.is_pressed or keys.d.is_pressed:
            self.camera_position -= speed * cross_direction
        self.update_camera_transform()

    def update_camera_transform(self) -> None:
        self.camera.local_transform = (
            FMatrix4(1).translate(self.camera_position) @
            FMatrix4(1).rotate(-self.camera_yaw, FVector3(0, 1, 0)) @
            FMatrix4(1).rotate(-self.camera_pitch, FVector3(1, 0, 0))
        )

    async def step(self, step: Step) -> None:
        self.move_camera(step)
        await self.draw(step)

    async def example_main(self) -> None:
        pass

    async def draw(self, step: Step) -> None:
        pass


def run_application(app_cls: type[Application]) -> None:
    app = app_cls()
    gc.disable()
    try:
        app.run()
    except Exception as ex:
        traceback.print_exception(ex)
        warnings.simplefilter('ignore')
    del app
    gc.collect()
