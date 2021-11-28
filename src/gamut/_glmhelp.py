
from __future__ import annotations

__all__ = ['ivec2_exact', 'vec4_exact']

# pyglm
from glm import ivec2, vec4
# pyglm-typing
from glm_typing import F32Vector4, I32Vector2


def ivec2_exact(input: I32Vector2) -> ivec2:
    if len(input) != 2:
        raise TypeError('input length must be 2')
    return ivec2(input)


def vec4_exact(input: F32Vector4) -> vec4:
    if len(input) != 4:
        raise TypeError('input length must be 4')
    return vec4(input)
