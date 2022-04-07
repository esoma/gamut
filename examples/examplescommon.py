
from __future__ import annotations

__all__ = ['ExampleApplication', 'run_application']

# gamut
from gamut import Application, Timer, TimerExpired, Window
from gamut.event import Bind
from gamut.graphics import WindowRenderTarget
from gamut.math import UVector2
# python
from datetime import timedelta
import gc
import traceback
import warnings


class ExampleApplication(Application):

    class Draw(TimerExpired):
        pass

    async def main(self) -> None:
        self.window = Window()
        self.window.resize(UVector2(800, 800))
        self.window.recenter()
        self.window.is_visible = True
        self.window_render_target = WindowRenderTarget(self.window)

        await self.example_main()

        with Bind.on(self.Draw, self.draw):
            self.draw_timer = Timer(
                self,
                timedelta(seconds=1 / 60.0),
                self.Draw,
                repeat=True,
                fixed=True,
            )
            await self.window.Close

    async def example_main(self) -> None:
        pass

    async def draw(self, draw: Draw) -> None:
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
