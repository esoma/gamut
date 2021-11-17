
__all__ = ['collect']

# gamut
from ._glcontext import get_gl_context


def collect() -> None:
    try:
        gl_context = get_gl_context()
    except RuntimeError:
        return
    gl_context.gc_collect()
