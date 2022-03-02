
from __future__ import annotations

__all__ = [
    'dmat4_exact',
    'dvec3_exact',
    'mat4_exact',
    'ivec1_exact',
    'ivec2_exact',
    'ivec3_exact',
    'I32Vector1',
    'I32Vector2',
    'I32Vector3',
    'uvec2_exact',
    'F32Matrix4x4',
    'F32Quaternion',
    'F32Vector3',
    'F32Vector4',
    'F64Vector3',
    'F64Matrix4x4',
    'vec3_exact',
    'vec4_exact',
]

# python
from typing import Any, Union
# pyglm
from glm import (dmat4, dvec3, imvec2, imvec3, ivec1, ivec2, ivec3, mat4,
                 mvec3, uvec2, vec3, vec4, quat)
# pyglm-typing
from glm_typing import F32Matrix4x4, F32Vector4, Number, F32Quaternion


I32Vector1 = Union[ivec1, tuple[Number]]
def ivec1_exact(input: Any) -> ivec1:
    if len(input) != 1:
        raise TypeError('input length must be 1')
    return ivec1(input)


I32Vector2 = Union[imvec2, ivec2, tuple[Number, Number]]
def ivec2_exact(input: Any) -> ivec2:
    if len(input) != 2:
        raise TypeError('input length must be 2')
    return ivec2(input)


def uvec2_exact(input: Any) -> uvec2:
    if len(input) != 2:
        raise TypeError('input length must be 2')
    return uvec2(input)


F32Vector3 = Union[mvec3, vec3, tuple[Number, Number, Number]]
def vec3_exact(input: Any) -> vec3:
    if len(input) != 3:
        raise TypeError('input length must be 3')
    return vec3(input)


F64Vector3 = Union[dvec3, tuple[Number, Number, Number]]
def dvec3_exact(input: Any) -> dvec3:
    if len(input) != 3:
        raise TypeError('input length must be 3')
    return dvec3(input)


I32Vector3 = Union[imvec3, ivec3, tuple[Number, Number, Number]]
def ivec3_exact(input: Any) -> ivec3:
    if len(input) != 3:
        raise TypeError('input length must be 3')
    return ivec3(input)


def vec4_exact(input: Any) -> vec4:
    if len(input) != 4:
        raise TypeError('input length must be 4')
    return vec4(input)


def mat4_exact(input: Any) -> mat4:
    return mat4(input)


F64Matrix4x4 = Union[
    dmat4,
    tuple[
        Number, Number, Number, Number,
        Number, Number, Number, Number,
        Number, Number, Number, Number,
        Number, Number, Number, Number,
    ]
]
def dmat4_exact(input: Any) -> dmat4:
    return dmat4(input)
    
    
def quat_exact(input: Any) -> quat:
    return quat(input)

