
# gamut
from gamut._glcontext import (get_gl_context, GlContext, release_gl_context,
                              require_gl_context)
# python
import weakref
# pytest
import pytest


def test_get_gl_context_no_context() -> None:
    with pytest.raises(RuntimeError) as excinfo:
        get_gl_context()
    assert str(excinfo.value) == 'no gl context'


def test_get_gl_context_repeated_calls() -> None:
    context = require_gl_context()
    try:
        gl_context = get_gl_context()
        assert isinstance(gl_context, GlContext)
        for _ in range(100):
            assert gl_context is get_gl_context()
    finally:
        release_gl_context(context)


def test_get_gl_context_expires() -> None:
    context = require_gl_context()
    try:
        gl_context = get_gl_context()
        weak_gl_context = weakref.ref(gl_context)
    finally:
        release_gl_context(context)

    assert not gl_context.is_open
    del gl_context
    assert weak_gl_context() is None


def test_multiple_contexts() -> None:
    gl_context_1 = GlContext()
    gl_context_2 = GlContext()
    try:
        assert gl_context_1.sdl_gl_context != gl_context_2.sdl_gl_context
    finally:
        gl_context_1.close()
        gl_context_2.close()
