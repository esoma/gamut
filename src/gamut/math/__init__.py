
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
]

# gamut
from ._math import (BVector2, BVector3, BVector4, DMatrix2x2, DMatrix2x3,
                    DMatrix2x4, DMatrix3x2, DMatrix3x3, DMatrix3x4, DMatrix4x2,
                    DMatrix4x3, DMatrix4x4, DVector2, DVector3, DVector4,
                    FMatrix2x2, FMatrix2x3, FMatrix2x4, FMatrix3x2, FMatrix3x3,
                    FMatrix3x4, FMatrix4x2, FMatrix4x3, FMatrix4x4, FVector2,
                    FVector3, FVector4, I8Vector2, I8Vector3, I8Vector4,
                    I16Vector2, I16Vector3, I16Vector4, I32Vector2, I32Vector3,
                    I32Vector4, I64Vector2, I64Vector3, I64Vector4, IVector2,
                    IVector3, IVector4, U8Vector2, U8Vector3, U8Vector4,
                    U16Vector2, U16Vector3, U16Vector4, U32Vector2, U32Vector3,
                    U32Vector4, U64Vector2, U64Vector3, U64Vector4, UVector2,
                    UVector3, UVector4)

Vector2 = DVector2
Vector3 = DVector3
Vector4 = DVector4

FMatrix2 = FMatrix2x2
FMatrix3 = FMatrix3x3
FMatrix4 = FMatrix4x4

Matrix2x2 = Matrix2 = DMatrix2 = DMatrix2x2
Matrix2x3 = DMatrix2x3
Matrix2x4 = DMatrix2x4
Matrix3x2 = DMatrix3x2
Matrix3x3 = Matrix3 = DMatrix3 = DMatrix3x3
Matrix3x4 = DMatrix3x4
Matrix4x2 = DMatrix4x2
Matrix4x3 = DMatrix4x3
Matrix4x4 = Matrix4 = DMatrix4 = DMatrix4x4
