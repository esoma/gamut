
from __future__ import annotations

__all__ = [
    'ivec2_exact',
    'uvec2_exact',
    'F32Vector3',
    'vec3_exact',
    'vec4_exact',
]

# python
from typing import Union
# pyglm
from glm import ivec2, uvec2, vec3, vec4
# pyglm-typing
from glm_typing import F32Vector4, I32Vector2, Number, U32Vector2


def ivec2_exact(input: I32Vector2) -> ivec2:
    if len(input) != 2:
        raise TypeError('input length must be 2')
    return ivec2(input)


def uvec2_exact(input: U32Vector2) -> uvec2:
    if len(input) != 2:
        raise TypeError('input length must be 2')
    return uvec2(input)


F32Vector3 = Union[vec3, tuple[Number, Number, Number]]

def vec3_exact(input: F32Vector3) -> vec3:
    if len(input) != 3:
        raise TypeError('input length must be 3')
    return vec3(input)


def vec4_exact(input: F32Vector4) -> vec4:
    if len(input) != 4:
        raise TypeError('input length must be 4')
    return vec4(input)
