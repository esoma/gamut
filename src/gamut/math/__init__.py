
__all__ = [
    'BVector2', 'BVector3', 'BVector4',
    'DVector2', 'DVector3', 'DVector4',
    'FVector2', 'FVector3', 'FVector4',
    'I8Vector2', 'I8Vector3', 'I8Vector4',
    'I16Vector2', 'I16Vector3', 'I16Vector4',
    'I32Vector2', 'I32Vector3', 'I32Vector4',
    'IVector2', 'IVector3', 'IVector4',
    'I64Vector2', 'I64Vector3', 'I64Vector4',
    'U8Vector2', 'U8Vector3', 'U8Vector4',
    'U16Vector2', 'U16Vector3', 'U16Vector4',
    'U32Vector2', 'U32Vector3', 'U32Vector4',
    'UVector2', 'UVector3', 'UVector4',
    'U64Vector2', 'U64Vector3', 'U64Vector4',
    'Vector2', 'Vector3', 'Vector4',
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
    'BVector2Array', 'BVector3Array', 'BVector4Array',
    'DMatrix2x2Array', 'DMatrix2x3Array', 'DMatrix2x4Array',
    'DMatrix3x2Array', 'DMatrix3x3Array', 'DMatrix3x4Array',
    'DMatrix4x2Array', 'DMatrix4x3Array', 'DMatrix4x4Array',
    'DVector2Array', 'DVector3Array', 'DVector4Array',
    'FMatrix2x2Array', 'FMatrix2x3Array', 'FMatrix2x4Array',
    'FMatrix3x2Array', 'FMatrix3x3Array', 'FMatrix3x4Array',
    'FMatrix4x2Array', 'FMatrix4x3Array', 'FMatrix4x4Array',
    'FVector2Array', 'FVector3Array', 'FVector4Array',
    'I8Vector2Array', 'I8Vector3Array', 'I8Vector4Array',
    'I16Vector2Array', 'I16Vector3Array', 'I16Vector4Array',
    'I32Vector2Array', 'I32Vector3Array', 'I32Vector4Array',
    'I64Vector2Array', 'I64Vector3Array', 'I64Vector4Array',
    'IVector2Array', 'IVector3Array', 'IVector4Array',
    'U8Vector2Array', 'U8Vector3Array', 'U8Vector4Array',
    'U16Vector2Array', 'U16Vector3Array', 'U16Vector4Array',
    'U32Vector2Array', 'U32Vector3Array', 'U32Vector4Array',
    'U64Vector2Array', 'U64Vector3Array', 'U64Vector4Array',
    'UVector2Array', 'UVector3Array', 'UVector4Array',
    'BArray',
    'DArray', 'FArray',
    'I8Array', 'U8Array',
    'I16Array', 'U16Array',
    'I32Array', 'U32Array',
    'IArray', 'UArray',
    'I64Array', 'U64Array',
]

# gamut
from ._math import (BArray, BVector2, BVector2Array, BVector3, BVector3Array,
                    BVector4, BVector4Array, DArray, DMatrix2x2,
                    DMatrix2x2Array, DMatrix2x3, DMatrix2x3Array, DMatrix2x4,
                    DMatrix2x4Array, DMatrix3x2, DMatrix3x2Array, DMatrix3x3,
                    DMatrix3x3Array, DMatrix3x4, DMatrix3x4Array, DMatrix4x2,
                    DMatrix4x2Array, DMatrix4x3, DMatrix4x3Array, DMatrix4x4,
                    DMatrix4x4Array, DVector2, DVector2Array, DVector3,
                    DVector3Array, DVector4, DVector4Array, FArray, FMatrix2x2,
                    FMatrix2x2Array, FMatrix2x3, FMatrix2x3Array, FMatrix2x4,
                    FMatrix2x4Array, FMatrix3x2, FMatrix3x2Array, FMatrix3x3,
                    FMatrix3x3Array, FMatrix3x4, FMatrix3x4Array, FMatrix4x2,
                    FMatrix4x2Array, FMatrix4x3, FMatrix4x3Array, FMatrix4x4,
                    FMatrix4x4Array, FVector2, FVector2Array, FVector3,
                    FVector3Array, FVector4, FVector4Array, I8Array, I8Vector2,
                    I8Vector2Array, I8Vector3, I8Vector3Array, I8Vector4,
                    I8Vector4Array, I16Array, I16Vector2, I16Vector2Array,
                    I16Vector3, I16Vector3Array, I16Vector4, I16Vector4Array,
                    I32Array, I32Vector2, I32Vector2Array, I32Vector3,
                    I32Vector3Array, I32Vector4, I32Vector4Array, I64Array,
                    I64Vector2, I64Vector2Array, I64Vector3, I64Vector3Array,
                    I64Vector4, I64Vector4Array, IArray, IVector2,
                    IVector2Array, IVector3, IVector3Array, IVector4,
                    IVector4Array, U8Array, U8Vector2, U8Vector2Array,
                    U8Vector3, U8Vector3Array, U8Vector4, U8Vector4Array,
                    U16Array, U16Vector2, U16Vector2Array, U16Vector3,
                    U16Vector3Array, U16Vector4, U16Vector4Array, U32Array,
                    U32Vector2, U32Vector2Array, U32Vector3, U32Vector3Array,
                    U32Vector4, U32Vector4Array, U64Array, U64Vector2,
                    U64Vector2Array, U64Vector3, U64Vector3Array, U64Vector4,
                    U64Vector4Array, UArray, UVector2, UVector2Array, UVector3,
                    UVector3Array, UVector4, UVector4Array)

Vector2 = DVector2
Vector3 = DVector3
Vector4 = DVector4

Vector2Array = DVector2Array
Vector3Array = DVector3Array
Vector4Array = DVector4Array

FMatrix2 = FMatrix2x2
FMatrix3 = FMatrix3x3
FMatrix4 = FMatrix4x4

FMatrix2Array = FMatrix2x2Array
FMatrix3Array = FMatrix3x3Array
FMatrix4Array = FMatrix4x4Array

Matrix2x2 = Matrix2 = DMatrix2 = DMatrix2x2
Matrix2x3 = DMatrix2x3
Matrix2x4 = DMatrix2x4
Matrix3x2 = DMatrix3x2
Matrix3x3 = Matrix3 = DMatrix3 = DMatrix3x3
Matrix3x4 = DMatrix3x4
Matrix4x2 = DMatrix4x2
Matrix4x3 = DMatrix4x3
Matrix4x4 = Matrix4 = DMatrix4 = DMatrix4x4

Matrix2x2Array = Matrix2Array = DMatrix2Array = DMatrix2x2Array
Matrix2x3Array = DMatrix2x3Array
Matrix2x4Array = DMatrix2x4Array
Matrix3x2Array = DMatrix3x2Array
Matrix3x3Array = Matrix3Array = DMatrix3Array = DMatrix3x3Array
Matrix3x4Array = DMatrix3x4Array
Matrix4x2Array = DMatrix4x2Array
Matrix4x3Array = DMatrix4x3Array
Matrix4x4Array = Matrix4Array = DMatrix4Array = DMatrix4x4Array
