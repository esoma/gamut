
# gamut
from gamut._glcontext import get_gl_context, GlContext
# python
import weakref


def test_get_gl_context_repeated_calls() -> None:
    gl_context = get_gl_context()
    assert isinstance(gl_context, GlContext)
    for _ in range(100):
        assert gl_context is get_gl_context()


def test_get_gl_context_expires() -> None:
    gl_context = get_gl_context()
    weak_gl_context = weakref.ref(gl_context)
    del gl_context

    assert weak_gl_context() is None
    gl_context = get_gl_context()
    assert isinstance(gl_context, GlContext)


def test_multiple_contexts() -> None:
    gl_context_1 = GlContext()
    gl_context_2 = GlContext()
    assert gl_context_1.sdl_gl_context != gl_context_2.sdl_gl_context
