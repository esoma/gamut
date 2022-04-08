
__all__ = [
    'BVector1', 'BVector2', 'BVector3', 'BVector4',
    'DVector1', 'DVector2', 'DVector3', 'DVector4',
    'FVector1', 'FVector2', 'FVector3', 'FVector4',
    'I8Vector1', 'I8Vector2', 'I8Vector3', 'I8Vector4',
    'I16Vector1', 'I16Vector2', 'I16Vector3', 'I16Vector4',
    'I32Vector1', 'I32Vector2', 'I32Vector3', 'I32Vector4',
    'IVector1', 'IVector2', 'IVector3', 'IVector4',
    'I64Vector1', 'I64Vector2', 'I64Vector3', 'I64Vector4',
    'U8Vector1', 'U8Vector2', 'U8Vector3', 'U8Vector4',
    'U16Vector1', 'U16Vector2', 'U16Vector3', 'U16Vector4',
    'U32Vector1', 'U32Vector2', 'U32Vector3', 'U32Vector4',
    'UVector1', 'UVector2', 'UVector3', 'UVector4',
    'U64Vector1', 'U64Vector2', 'U64Vector3', 'U64Vector4',
    'Vector1', 'Vector2', 'Vector3', 'Vector4',
    'FMatrix2x2', 'FMatrix2x3', 'FMatrix2x4',
    'FMatrix3x2', 'FMatrix3x3', 'FMatrix3x4',
    'FMatrix4x2', 'FMatrix4x3', 'FMatrix4x4',
    'DMatrix2x2', 'DMatrix2x3', 'DMatrix2x4',
    'DMatrix3x2', 'DMatrix3x3', 'DMatrix3x4',
    'DMatrix4x2', 'DMatrix4x3', 'DMatrix4x4',
    'FMatrix2', 'FMatrix3', 'FMatrix4',
    'DMatrix2', 'DMatrix3', 'DMatrix4',
    'Matrix2x2', 'Matrix2x3', 'Matrix2x4',
    'Matrix3x2', 'Matrix3x3', 'Matrix3x4',
    'Matrix4x2', 'Matrix4x3', 'Matrix4x4',
    'Matrix2', 'Matrix3', 'Matrix4',
    'DMatrix2x2Array', 'DMatrix2x3Array', 'DMatrix2x4Array',
    'DMatrix3x2Array', 'DMatrix3x3Array', 'DMatrix3x4Array',
    'DMatrix4x2Array', 'DMatrix4x3Array', 'DMatrix4x4Array',
    'DVector2Array', 'DVector3Array', 'DVector4Array',
    'FMatrix2x2Array', 'FMatrix2x3Array', 'FMatrix2x4Array',
    'FMatrix3x2Array', 'FMatrix3x3Array', 'FMatrix3x4Array',
    'FMatrix4x2Array', 'FMatrix4x3Array', 'FMatrix4x4Array',
    'BVector1Array', 'BVector2Array', 'BVector3Array', 'BVector4Array',
    'FVector1Array', 'FVector2Array', 'FVector3Array', 'FVector4Array',
    'I8Vector1Array', 'I8Vector2Array', 'I8Vector3Array', 'I8Vector4Array',
    'I16Vector1Array', 'I16Vector2Array', 'I16Vector3Array', 'I16Vector4Array',
    'I32Vector1Array', 'I32Vector2Array', 'I32Vector3Array', 'I32Vector4Array',
    'I64Vector1Array', 'I64Vector2Array', 'I64Vector3Array', 'I64Vector4Array',
    'IVector1Array', 'IVector2Array', 'IVector3Array', 'IVector4Array',
    'U8Vector1Array', 'U8Vector2Array', 'U8Vector3Array', 'U8Vector4Array',
    'U16Vector1Array', 'U16Vector2Array', 'U16Vector3Array', 'U16Vector4Array',
    'U32Vector1Array', 'U32Vector2Array', 'U32Vector3Array', 'U32Vector4Array',
    'U64Vector1Array', 'U64Vector2Array', 'U64Vector3Array', 'U64Vector4Array',
    'UVector1Array', 'UVector2Array', 'UVector3Array', 'UVector4Array',
    'BArray',
    'DArray', 'FArray',
    'I8Array', 'U8Array',
    'I16Array', 'U16Array',
    'I32Array', 'U32Array',
    'IArray', 'UArray',
    'I64Array', 'U64Array',
    'FQuaternion', 'FQuaternionArray',
    'DQuaternion', 'DQuaternionArray',
    'Quaternion', 'QuaternionArray',
]

# gamut
from ._math import (BArray, BVector1, BVector1Array, BVector2, BVector2Array,
                    BVector3, BVector3Array, BVector4, BVector4Array, DArray,
                    DMatrix2x2, DMatrix2x2Array, DMatrix2x3, DMatrix2x3Array,
                    DMatrix2x4, DMatrix2x4Array, DMatrix3x2, DMatrix3x2Array,
                    DMatrix3x3, DMatrix3x3Array, DMatrix3x4, DMatrix3x4Array,
                    DMatrix4x2, DMatrix4x2Array, DMatrix4x3, DMatrix4x3Array,
                    DMatrix4x4, DMatrix4x4Array, DQuaternion, DQuaternionArray,
                    DVector1, DVector1Array, DVector2, DVector2Array, DVector3,
                    DVector3Array, DVector4, DVector4Array, FArray, FMatrix2x2,
                    FMatrix2x2Array, FMatrix2x3, FMatrix2x3Array, FMatrix2x4,
                    FMatrix2x4Array, FMatrix3x2, FMatrix3x2Array, FMatrix3x3,
                    FMatrix3x3Array, FMatrix3x4, FMatrix3x4Array, FMatrix4x2,
                    FMatrix4x2Array, FMatrix4x3, FMatrix4x3Array, FMatrix4x4,
                    FMatrix4x4Array, FQuaternion, FQuaternionArray, FVector1,
                    FVector1Array, FVector2, FVector2Array, FVector3,
                    FVector3Array, FVector4, FVector4Array, I8Array, I8Vector1,
                    I8Vector1Array, I8Vector2, I8Vector2Array, I8Vector3,
                    I8Vector3Array, I8Vector4, I8Vector4Array, I16Array,
                    I16Vector1, I16Vector1Array, I16Vector2, I16Vector2Array,
                    I16Vector3, I16Vector3Array, I16Vector4, I16Vector4Array,
                    I32Array, I32Vector1, I32Vector1Array, I32Vector2,
                    I32Vector2Array, I32Vector3, I32Vector3Array, I32Vector4,
                    I32Vector4Array, I64Array, I64Vector1, I64Vector1Array,
                    I64Vector2, I64Vector2Array, I64Vector3, I64Vector3Array,
                    I64Vector4, I64Vector4Array, IArray, IVector1,
                    IVector1Array, IVector2, IVector2Array, IVector3,
                    IVector3Array, IVector4, IVector4Array, U8Array, U8Vector1,
                    U8Vector1Array, U8Vector2, U8Vector2Array, U8Vector3,
                    U8Vector3Array, U8Vector4, U8Vector4Array, U16Array,
                    U16Vector1, U16Vector1Array, U16Vector2, U16Vector2Array,
                    U16Vector3, U16Vector3Array, U16Vector4, U16Vector4Array,
                    U32Array, U32Vector1, U32Vector1Array, U32Vector2,
                    U32Vector2Array, U32Vector3, U32Vector3Array, U32Vector4,
                    U32Vector4Array, U64Array, U64Vector1, U64Vector1Array,
                    U64Vector2, U64Vector2Array, U64Vector3, U64Vector3Array,
                    U64Vector4, U64Vector4Array, UArray, UVector1,
                    UVector1Array, UVector2, UVector2Array, UVector3,
                    UVector3Array, UVector4, UVector4Array)
# python
from typing import TypeAlias

Vector1: TypeAlias = DVector1
Vector2: TypeAlias = DVector2
Vector3: TypeAlias = DVector3
Vector4: TypeAlias = DVector4

Vector1Array: TypeAlias = DVector1Array
Vector2Array: TypeAlias = DVector2Array
Vector3Array: TypeAlias = DVector3Array
Vector4Array: TypeAlias = DVector4Array

FMatrix2: TypeAlias = FMatrix2x2
FMatrix3: TypeAlias = FMatrix3x3
FMatrix4: TypeAlias = FMatrix4x4

FMatrix2Array: TypeAlias = FMatrix2x2Array
FMatrix3Array: TypeAlias = FMatrix3x3Array
FMatrix4Array: TypeAlias = FMatrix4x4Array

Matrix2x2: TypeAlias = DMatrix2x2
Matrix2: TypeAlias = DMatrix2x2
DMatrix2: TypeAlias = DMatrix2x2
Matrix2x3: TypeAlias = DMatrix2x3
Matrix2x4: TypeAlias = DMatrix2x4
Matrix3x2: TypeAlias = DMatrix3x2
Matrix3x3: TypeAlias = DMatrix3x3
Matrix3: TypeAlias = DMatrix3x3
DMatrix3: TypeAlias = DMatrix3x3
Matrix3x4: TypeAlias = DMatrix3x4
Matrix4x2: TypeAlias = DMatrix4x2
Matrix4x3: TypeAlias = DMatrix4x3
Matrix4x4: TypeAlias = DMatrix4x4
Matrix4: TypeAlias = DMatrix4x4
DMatrix4: TypeAlias = DMatrix4x4

Matrix2x2Array: TypeAlias = DMatrix2x2Array
Matrix2Array: TypeAlias = DMatrix2x2Array
DMatrix2Array: TypeAlias = DMatrix2x2Array
Matrix2x3Array: TypeAlias = DMatrix2x3Array
Matrix2x4Array: TypeAlias = DMatrix2x4Array
Matrix3x2Array: TypeAlias = DMatrix3x2Array
Matrix3x3Array: TypeAlias = DMatrix3x3Array
Matrix3Array: TypeAlias = DMatrix3x3Array
DMatrix3Array: TypeAlias = DMatrix3x3Array
Matrix3x4Array: TypeAlias = DMatrix3x4Array
Matrix4x2Array: TypeAlias = DMatrix4x2Array
Matrix4x3Array: TypeAlias = DMatrix4x3Array
Matrix4x4Array: TypeAlias = DMatrix4x4Array
Matrix4Array: TypeAlias = DMatrix4x4Array
DMatrix4Array: TypeAlias = DMatrix4x4Array

Quaternion: TypeAlias = DQuaternion
QuaternionArray: TypeAlias = DQuaternionArray
