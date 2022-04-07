
from __future__ import annotations

__all__ = ['run_application']

# gamut
from gamut import Application
# python
import gc
import traceback
import warnings


def run_application(app_cls: type[Application]):
    app = app_cls()
    gc.disable()
    try:
        app.run()
    except Exception as ex:
        traceback.print_exception(ex)
        warnings.simplefilter('ignore')
    del app
    gc.collect()
