
// generated 2022-03-26 21:40:50.219078 from codegen/math/templates/math.h

#ifndef GAMUT_MATH_API_HPP
#define GAMUT_MATH_API_HPP

// stdlib
#include <stdbool.h>
// python
#define PY_SSIZE_T_CLEAN
#include <Python.h>

#ifdef __cplusplus
extern "C" {
#endif

typedef PyTypeObject *(*GamutMathApi_GetType)();
typedef size_t (*GamutMathApi_GetArrayLength)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateBVector1)(const bool *);
    typedef PyObject *(*GamutMathApi_CreateBVector1Array)(size_t, const bool *);
    typedef bool *(*GamutMathApi_GetBVector1ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateDVector1)(const double *);
    typedef PyObject *(*GamutMathApi_CreateDVector1Array)(size_t, const double *);
    typedef double *(*GamutMathApi_GetDVector1ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateFVector1)(const float *);
    typedef PyObject *(*GamutMathApi_CreateFVector1Array)(size_t, const float *);
    typedef float *(*GamutMathApi_GetFVector1ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateI8Vector1)(const int8_t *);
    typedef PyObject *(*GamutMathApi_CreateI8Vector1Array)(size_t, const int8_t *);
    typedef int8_t *(*GamutMathApi_GetI8Vector1ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateU8Vector1)(const uint8_t *);
    typedef PyObject *(*GamutMathApi_CreateU8Vector1Array)(size_t, const uint8_t *);
    typedef uint8_t *(*GamutMathApi_GetU8Vector1ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateI16Vector1)(const int16_t *);
    typedef PyObject *(*GamutMathApi_CreateI16Vector1Array)(size_t, const int16_t *);
    typedef int16_t *(*GamutMathApi_GetI16Vector1ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateU16Vector1)(const uint16_t *);
    typedef PyObject *(*GamutMathApi_CreateU16Vector1Array)(size_t, const uint16_t *);
    typedef uint16_t *(*GamutMathApi_GetU16Vector1ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateI32Vector1)(const int32_t *);
    typedef PyObject *(*GamutMathApi_CreateI32Vector1Array)(size_t, const int32_t *);
    typedef int32_t *(*GamutMathApi_GetI32Vector1ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateU32Vector1)(const uint32_t *);
    typedef PyObject *(*GamutMathApi_CreateU32Vector1Array)(size_t, const uint32_t *);
    typedef uint32_t *(*GamutMathApi_GetU32Vector1ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateIVector1)(const int *);
    typedef PyObject *(*GamutMathApi_CreateIVector1Array)(size_t, const int *);
    typedef int *(*GamutMathApi_GetIVector1ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateUVector1)(const unsigned int *);
    typedef PyObject *(*GamutMathApi_CreateUVector1Array)(size_t, const unsigned int *);
    typedef unsigned int *(*GamutMathApi_GetUVector1ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateI64Vector1)(const int64_t *);
    typedef PyObject *(*GamutMathApi_CreateI64Vector1Array)(size_t, const int64_t *);
    typedef int64_t *(*GamutMathApi_GetI64Vector1ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateU64Vector1)(const uint64_t *);
    typedef PyObject *(*GamutMathApi_CreateU64Vector1Array)(size_t, const uint64_t *);
    typedef uint64_t *(*GamutMathApi_GetU64Vector1ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateBVector2)(const bool *);
    typedef PyObject *(*GamutMathApi_CreateBVector2Array)(size_t, const bool *);
    typedef bool *(*GamutMathApi_GetBVector2ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateDVector2)(const double *);
    typedef PyObject *(*GamutMathApi_CreateDVector2Array)(size_t, const double *);
    typedef double *(*GamutMathApi_GetDVector2ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateFVector2)(const float *);
    typedef PyObject *(*GamutMathApi_CreateFVector2Array)(size_t, const float *);
    typedef float *(*GamutMathApi_GetFVector2ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateI8Vector2)(const int8_t *);
    typedef PyObject *(*GamutMathApi_CreateI8Vector2Array)(size_t, const int8_t *);
    typedef int8_t *(*GamutMathApi_GetI8Vector2ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateU8Vector2)(const uint8_t *);
    typedef PyObject *(*GamutMathApi_CreateU8Vector2Array)(size_t, const uint8_t *);
    typedef uint8_t *(*GamutMathApi_GetU8Vector2ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateI16Vector2)(const int16_t *);
    typedef PyObject *(*GamutMathApi_CreateI16Vector2Array)(size_t, const int16_t *);
    typedef int16_t *(*GamutMathApi_GetI16Vector2ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateU16Vector2)(const uint16_t *);
    typedef PyObject *(*GamutMathApi_CreateU16Vector2Array)(size_t, const uint16_t *);
    typedef uint16_t *(*GamutMathApi_GetU16Vector2ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateI32Vector2)(const int32_t *);
    typedef PyObject *(*GamutMathApi_CreateI32Vector2Array)(size_t, const int32_t *);
    typedef int32_t *(*GamutMathApi_GetI32Vector2ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateU32Vector2)(const uint32_t *);
    typedef PyObject *(*GamutMathApi_CreateU32Vector2Array)(size_t, const uint32_t *);
    typedef uint32_t *(*GamutMathApi_GetU32Vector2ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateIVector2)(const int *);
    typedef PyObject *(*GamutMathApi_CreateIVector2Array)(size_t, const int *);
    typedef int *(*GamutMathApi_GetIVector2ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateUVector2)(const unsigned int *);
    typedef PyObject *(*GamutMathApi_CreateUVector2Array)(size_t, const unsigned int *);
    typedef unsigned int *(*GamutMathApi_GetUVector2ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateI64Vector2)(const int64_t *);
    typedef PyObject *(*GamutMathApi_CreateI64Vector2Array)(size_t, const int64_t *);
    typedef int64_t *(*GamutMathApi_GetI64Vector2ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateU64Vector2)(const uint64_t *);
    typedef PyObject *(*GamutMathApi_CreateU64Vector2Array)(size_t, const uint64_t *);
    typedef uint64_t *(*GamutMathApi_GetU64Vector2ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateBVector3)(const bool *);
    typedef PyObject *(*GamutMathApi_CreateBVector3Array)(size_t, const bool *);
    typedef bool *(*GamutMathApi_GetBVector3ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateDVector3)(const double *);
    typedef PyObject *(*GamutMathApi_CreateDVector3Array)(size_t, const double *);
    typedef double *(*GamutMathApi_GetDVector3ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateFVector3)(const float *);
    typedef PyObject *(*GamutMathApi_CreateFVector3Array)(size_t, const float *);
    typedef float *(*GamutMathApi_GetFVector3ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateI8Vector3)(const int8_t *);
    typedef PyObject *(*GamutMathApi_CreateI8Vector3Array)(size_t, const int8_t *);
    typedef int8_t *(*GamutMathApi_GetI8Vector3ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateU8Vector3)(const uint8_t *);
    typedef PyObject *(*GamutMathApi_CreateU8Vector3Array)(size_t, const uint8_t *);
    typedef uint8_t *(*GamutMathApi_GetU8Vector3ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateI16Vector3)(const int16_t *);
    typedef PyObject *(*GamutMathApi_CreateI16Vector3Array)(size_t, const int16_t *);
    typedef int16_t *(*GamutMathApi_GetI16Vector3ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateU16Vector3)(const uint16_t *);
    typedef PyObject *(*GamutMathApi_CreateU16Vector3Array)(size_t, const uint16_t *);
    typedef uint16_t *(*GamutMathApi_GetU16Vector3ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateI32Vector3)(const int32_t *);
    typedef PyObject *(*GamutMathApi_CreateI32Vector3Array)(size_t, const int32_t *);
    typedef int32_t *(*GamutMathApi_GetI32Vector3ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateU32Vector3)(const uint32_t *);
    typedef PyObject *(*GamutMathApi_CreateU32Vector3Array)(size_t, const uint32_t *);
    typedef uint32_t *(*GamutMathApi_GetU32Vector3ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateIVector3)(const int *);
    typedef PyObject *(*GamutMathApi_CreateIVector3Array)(size_t, const int *);
    typedef int *(*GamutMathApi_GetIVector3ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateUVector3)(const unsigned int *);
    typedef PyObject *(*GamutMathApi_CreateUVector3Array)(size_t, const unsigned int *);
    typedef unsigned int *(*GamutMathApi_GetUVector3ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateI64Vector3)(const int64_t *);
    typedef PyObject *(*GamutMathApi_CreateI64Vector3Array)(size_t, const int64_t *);
    typedef int64_t *(*GamutMathApi_GetI64Vector3ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateU64Vector3)(const uint64_t *);
    typedef PyObject *(*GamutMathApi_CreateU64Vector3Array)(size_t, const uint64_t *);
    typedef uint64_t *(*GamutMathApi_GetU64Vector3ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateBVector4)(const bool *);
    typedef PyObject *(*GamutMathApi_CreateBVector4Array)(size_t, const bool *);
    typedef bool *(*GamutMathApi_GetBVector4ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateDVector4)(const double *);
    typedef PyObject *(*GamutMathApi_CreateDVector4Array)(size_t, const double *);
    typedef double *(*GamutMathApi_GetDVector4ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateFVector4)(const float *);
    typedef PyObject *(*GamutMathApi_CreateFVector4Array)(size_t, const float *);
    typedef float *(*GamutMathApi_GetFVector4ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateI8Vector4)(const int8_t *);
    typedef PyObject *(*GamutMathApi_CreateI8Vector4Array)(size_t, const int8_t *);
    typedef int8_t *(*GamutMathApi_GetI8Vector4ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateU8Vector4)(const uint8_t *);
    typedef PyObject *(*GamutMathApi_CreateU8Vector4Array)(size_t, const uint8_t *);
    typedef uint8_t *(*GamutMathApi_GetU8Vector4ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateI16Vector4)(const int16_t *);
    typedef PyObject *(*GamutMathApi_CreateI16Vector4Array)(size_t, const int16_t *);
    typedef int16_t *(*GamutMathApi_GetI16Vector4ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateU16Vector4)(const uint16_t *);
    typedef PyObject *(*GamutMathApi_CreateU16Vector4Array)(size_t, const uint16_t *);
    typedef uint16_t *(*GamutMathApi_GetU16Vector4ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateI32Vector4)(const int32_t *);
    typedef PyObject *(*GamutMathApi_CreateI32Vector4Array)(size_t, const int32_t *);
    typedef int32_t *(*GamutMathApi_GetI32Vector4ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateU32Vector4)(const uint32_t *);
    typedef PyObject *(*GamutMathApi_CreateU32Vector4Array)(size_t, const uint32_t *);
    typedef uint32_t *(*GamutMathApi_GetU32Vector4ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateIVector4)(const int *);
    typedef PyObject *(*GamutMathApi_CreateIVector4Array)(size_t, const int *);
    typedef int *(*GamutMathApi_GetIVector4ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateUVector4)(const unsigned int *);
    typedef PyObject *(*GamutMathApi_CreateUVector4Array)(size_t, const unsigned int *);
    typedef unsigned int *(*GamutMathApi_GetUVector4ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateI64Vector4)(const int64_t *);
    typedef PyObject *(*GamutMathApi_CreateI64Vector4Array)(size_t, const int64_t *);
    typedef int64_t *(*GamutMathApi_GetI64Vector4ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateU64Vector4)(const uint64_t *);
    typedef PyObject *(*GamutMathApi_CreateU64Vector4Array)(size_t, const uint64_t *);
    typedef uint64_t *(*GamutMathApi_GetU64Vector4ValuePointer)(const PyObject *);





    typedef PyObject *(*GamutMathApi_CreateDMatrix2x2)(const double *);
    typedef PyObject *(*GamutMathApi_CreateDMatrix2x2Array)(size_t, const double *);
    typedef double *(*GamutMathApi_GetDMatrix2x2ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateFMatrix2x2)(const float *);
    typedef PyObject *(*GamutMathApi_CreateFMatrix2x2Array)(size_t, const float *);
    typedef float *(*GamutMathApi_GetFMatrix2x2ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateDMatrix2x3)(const double *);
    typedef PyObject *(*GamutMathApi_CreateDMatrix2x3Array)(size_t, const double *);
    typedef double *(*GamutMathApi_GetDMatrix2x3ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateFMatrix2x3)(const float *);
    typedef PyObject *(*GamutMathApi_CreateFMatrix2x3Array)(size_t, const float *);
    typedef float *(*GamutMathApi_GetFMatrix2x3ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateDMatrix2x4)(const double *);
    typedef PyObject *(*GamutMathApi_CreateDMatrix2x4Array)(size_t, const double *);
    typedef double *(*GamutMathApi_GetDMatrix2x4ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateFMatrix2x4)(const float *);
    typedef PyObject *(*GamutMathApi_CreateFMatrix2x4Array)(size_t, const float *);
    typedef float *(*GamutMathApi_GetFMatrix2x4ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateDMatrix3x2)(const double *);
    typedef PyObject *(*GamutMathApi_CreateDMatrix3x2Array)(size_t, const double *);
    typedef double *(*GamutMathApi_GetDMatrix3x2ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateFMatrix3x2)(const float *);
    typedef PyObject *(*GamutMathApi_CreateFMatrix3x2Array)(size_t, const float *);
    typedef float *(*GamutMathApi_GetFMatrix3x2ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateDMatrix3x3)(const double *);
    typedef PyObject *(*GamutMathApi_CreateDMatrix3x3Array)(size_t, const double *);
    typedef double *(*GamutMathApi_GetDMatrix3x3ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateFMatrix3x3)(const float *);
    typedef PyObject *(*GamutMathApi_CreateFMatrix3x3Array)(size_t, const float *);
    typedef float *(*GamutMathApi_GetFMatrix3x3ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateDMatrix3x4)(const double *);
    typedef PyObject *(*GamutMathApi_CreateDMatrix3x4Array)(size_t, const double *);
    typedef double *(*GamutMathApi_GetDMatrix3x4ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateFMatrix3x4)(const float *);
    typedef PyObject *(*GamutMathApi_CreateFMatrix3x4Array)(size_t, const float *);
    typedef float *(*GamutMathApi_GetFMatrix3x4ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateDMatrix4x2)(const double *);
    typedef PyObject *(*GamutMathApi_CreateDMatrix4x2Array)(size_t, const double *);
    typedef double *(*GamutMathApi_GetDMatrix4x2ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateFMatrix4x2)(const float *);
    typedef PyObject *(*GamutMathApi_CreateFMatrix4x2Array)(size_t, const float *);
    typedef float *(*GamutMathApi_GetFMatrix4x2ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateDMatrix4x3)(const double *);
    typedef PyObject *(*GamutMathApi_CreateDMatrix4x3Array)(size_t, const double *);
    typedef double *(*GamutMathApi_GetDMatrix4x3ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateFMatrix4x3)(const float *);
    typedef PyObject *(*GamutMathApi_CreateFMatrix4x3Array)(size_t, const float *);
    typedef float *(*GamutMathApi_GetFMatrix4x3ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateDMatrix4x4)(const double *);
    typedef PyObject *(*GamutMathApi_CreateDMatrix4x4Array)(size_t, const double *);
    typedef double *(*GamutMathApi_GetDMatrix4x4ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateFMatrix4x4)(const float *);
    typedef PyObject *(*GamutMathApi_CreateFMatrix4x4Array)(size_t, const float *);
    typedef float *(*GamutMathApi_GetFMatrix4x4ValuePointer)(const PyObject *);





    typedef PyObject *(*GamutMathApi_CreateDQuaternion)(const double *);
    typedef PyObject *(*GamutMathApi_CreateDQuaternionArray)(size_t, const double *);
    typedef double *(*GamutMathApi_GetDQuaternionValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateFQuaternion)(const float *);
    typedef PyObject *(*GamutMathApi_CreateFQuaternionArray)(size_t, const float *);
    typedef float *(*GamutMathApi_GetFQuaternionValuePointer)(const PyObject *);





    typedef PyObject *(*GamutMathApi_CreateBArray)(size_t, const bool *);
    typedef bool *(*GamutMathApi_GetBValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateDArray)(size_t, const double *);
    typedef double *(*GamutMathApi_GetDValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateFArray)(size_t, const float *);
    typedef float *(*GamutMathApi_GetFValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateI8Array)(size_t, const int8_t *);
    typedef int8_t *(*GamutMathApi_GetI8ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateU8Array)(size_t, const uint8_t *);
    typedef uint8_t *(*GamutMathApi_GetU8ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateI16Array)(size_t, const int16_t *);
    typedef int16_t *(*GamutMathApi_GetI16ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateU16Array)(size_t, const uint16_t *);
    typedef uint16_t *(*GamutMathApi_GetU16ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateI32Array)(size_t, const int32_t *);
    typedef int32_t *(*GamutMathApi_GetI32ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateU32Array)(size_t, const uint32_t *);
    typedef uint32_t *(*GamutMathApi_GetU32ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateIArray)(size_t, const int *);
    typedef int *(*GamutMathApi_GetIValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateUArray)(size_t, const unsigned int *);
    typedef unsigned int *(*GamutMathApi_GetUValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateI64Array)(size_t, const int64_t *);
    typedef int64_t *(*GamutMathApi_GetI64ValuePointer)(const PyObject *);



    typedef PyObject *(*GamutMathApi_CreateU64Array)(size_t, const uint64_t *);
    typedef uint64_t *(*GamutMathApi_GetU64ValuePointer)(const PyObject *);




struct GamutMathApi
{
    const size_t version;

        GamutMathApi_GetType BVector1_GetType;
        GamutMathApi_GetType BVector1Array_GetType;
        GamutMathApi_CreateBVector1 BVector1_Create;
        GamutMathApi_CreateBVector1Array BVector1Array_Create;
        GamutMathApi_GetBVector1ValuePointer BVector1_GetValuePointer;
        GamutMathApi_GetBVector1ValuePointer BVector1Array_GetValuePointer;
        GamutMathApi_GetArrayLength BVector1Array_GetLength;

        GamutMathApi_GetType DVector1_GetType;
        GamutMathApi_GetType DVector1Array_GetType;
        GamutMathApi_CreateDVector1 DVector1_Create;
        GamutMathApi_CreateDVector1Array DVector1Array_Create;
        GamutMathApi_GetDVector1ValuePointer DVector1_GetValuePointer;
        GamutMathApi_GetDVector1ValuePointer DVector1Array_GetValuePointer;
        GamutMathApi_GetArrayLength DVector1Array_GetLength;

        GamutMathApi_GetType FVector1_GetType;
        GamutMathApi_GetType FVector1Array_GetType;
        GamutMathApi_CreateFVector1 FVector1_Create;
        GamutMathApi_CreateFVector1Array FVector1Array_Create;
        GamutMathApi_GetFVector1ValuePointer FVector1_GetValuePointer;
        GamutMathApi_GetFVector1ValuePointer FVector1Array_GetValuePointer;
        GamutMathApi_GetArrayLength FVector1Array_GetLength;

        GamutMathApi_GetType I8Vector1_GetType;
        GamutMathApi_GetType I8Vector1Array_GetType;
        GamutMathApi_CreateI8Vector1 I8Vector1_Create;
        GamutMathApi_CreateI8Vector1Array I8Vector1Array_Create;
        GamutMathApi_GetI8Vector1ValuePointer I8Vector1_GetValuePointer;
        GamutMathApi_GetI8Vector1ValuePointer I8Vector1Array_GetValuePointer;
        GamutMathApi_GetArrayLength I8Vector1Array_GetLength;

        GamutMathApi_GetType U8Vector1_GetType;
        GamutMathApi_GetType U8Vector1Array_GetType;
        GamutMathApi_CreateU8Vector1 U8Vector1_Create;
        GamutMathApi_CreateU8Vector1Array U8Vector1Array_Create;
        GamutMathApi_GetU8Vector1ValuePointer U8Vector1_GetValuePointer;
        GamutMathApi_GetU8Vector1ValuePointer U8Vector1Array_GetValuePointer;
        GamutMathApi_GetArrayLength U8Vector1Array_GetLength;

        GamutMathApi_GetType I16Vector1_GetType;
        GamutMathApi_GetType I16Vector1Array_GetType;
        GamutMathApi_CreateI16Vector1 I16Vector1_Create;
        GamutMathApi_CreateI16Vector1Array I16Vector1Array_Create;
        GamutMathApi_GetI16Vector1ValuePointer I16Vector1_GetValuePointer;
        GamutMathApi_GetI16Vector1ValuePointer I16Vector1Array_GetValuePointer;
        GamutMathApi_GetArrayLength I16Vector1Array_GetLength;

        GamutMathApi_GetType U16Vector1_GetType;
        GamutMathApi_GetType U16Vector1Array_GetType;
        GamutMathApi_CreateU16Vector1 U16Vector1_Create;
        GamutMathApi_CreateU16Vector1Array U16Vector1Array_Create;
        GamutMathApi_GetU16Vector1ValuePointer U16Vector1_GetValuePointer;
        GamutMathApi_GetU16Vector1ValuePointer U16Vector1Array_GetValuePointer;
        GamutMathApi_GetArrayLength U16Vector1Array_GetLength;

        GamutMathApi_GetType I32Vector1_GetType;
        GamutMathApi_GetType I32Vector1Array_GetType;
        GamutMathApi_CreateI32Vector1 I32Vector1_Create;
        GamutMathApi_CreateI32Vector1Array I32Vector1Array_Create;
        GamutMathApi_GetI32Vector1ValuePointer I32Vector1_GetValuePointer;
        GamutMathApi_GetI32Vector1ValuePointer I32Vector1Array_GetValuePointer;
        GamutMathApi_GetArrayLength I32Vector1Array_GetLength;

        GamutMathApi_GetType U32Vector1_GetType;
        GamutMathApi_GetType U32Vector1Array_GetType;
        GamutMathApi_CreateU32Vector1 U32Vector1_Create;
        GamutMathApi_CreateU32Vector1Array U32Vector1Array_Create;
        GamutMathApi_GetU32Vector1ValuePointer U32Vector1_GetValuePointer;
        GamutMathApi_GetU32Vector1ValuePointer U32Vector1Array_GetValuePointer;
        GamutMathApi_GetArrayLength U32Vector1Array_GetLength;

        GamutMathApi_GetType IVector1_GetType;
        GamutMathApi_GetType IVector1Array_GetType;
        GamutMathApi_CreateIVector1 IVector1_Create;
        GamutMathApi_CreateIVector1Array IVector1Array_Create;
        GamutMathApi_GetIVector1ValuePointer IVector1_GetValuePointer;
        GamutMathApi_GetIVector1ValuePointer IVector1Array_GetValuePointer;
        GamutMathApi_GetArrayLength IVector1Array_GetLength;

        GamutMathApi_GetType UVector1_GetType;
        GamutMathApi_GetType UVector1Array_GetType;
        GamutMathApi_CreateUVector1 UVector1_Create;
        GamutMathApi_CreateUVector1Array UVector1Array_Create;
        GamutMathApi_GetUVector1ValuePointer UVector1_GetValuePointer;
        GamutMathApi_GetUVector1ValuePointer UVector1Array_GetValuePointer;
        GamutMathApi_GetArrayLength UVector1Array_GetLength;

        GamutMathApi_GetType I64Vector1_GetType;
        GamutMathApi_GetType I64Vector1Array_GetType;
        GamutMathApi_CreateI64Vector1 I64Vector1_Create;
        GamutMathApi_CreateI64Vector1Array I64Vector1Array_Create;
        GamutMathApi_GetI64Vector1ValuePointer I64Vector1_GetValuePointer;
        GamutMathApi_GetI64Vector1ValuePointer I64Vector1Array_GetValuePointer;
        GamutMathApi_GetArrayLength I64Vector1Array_GetLength;

        GamutMathApi_GetType U64Vector1_GetType;
        GamutMathApi_GetType U64Vector1Array_GetType;
        GamutMathApi_CreateU64Vector1 U64Vector1_Create;
        GamutMathApi_CreateU64Vector1Array U64Vector1Array_Create;
        GamutMathApi_GetU64Vector1ValuePointer U64Vector1_GetValuePointer;
        GamutMathApi_GetU64Vector1ValuePointer U64Vector1Array_GetValuePointer;
        GamutMathApi_GetArrayLength U64Vector1Array_GetLength;

        GamutMathApi_GetType BVector2_GetType;
        GamutMathApi_GetType BVector2Array_GetType;
        GamutMathApi_CreateBVector2 BVector2_Create;
        GamutMathApi_CreateBVector2Array BVector2Array_Create;
        GamutMathApi_GetBVector2ValuePointer BVector2_GetValuePointer;
        GamutMathApi_GetBVector2ValuePointer BVector2Array_GetValuePointer;
        GamutMathApi_GetArrayLength BVector2Array_GetLength;

        GamutMathApi_GetType DVector2_GetType;
        GamutMathApi_GetType DVector2Array_GetType;
        GamutMathApi_CreateDVector2 DVector2_Create;
        GamutMathApi_CreateDVector2Array DVector2Array_Create;
        GamutMathApi_GetDVector2ValuePointer DVector2_GetValuePointer;
        GamutMathApi_GetDVector2ValuePointer DVector2Array_GetValuePointer;
        GamutMathApi_GetArrayLength DVector2Array_GetLength;

        GamutMathApi_GetType FVector2_GetType;
        GamutMathApi_GetType FVector2Array_GetType;
        GamutMathApi_CreateFVector2 FVector2_Create;
        GamutMathApi_CreateFVector2Array FVector2Array_Create;
        GamutMathApi_GetFVector2ValuePointer FVector2_GetValuePointer;
        GamutMathApi_GetFVector2ValuePointer FVector2Array_GetValuePointer;
        GamutMathApi_GetArrayLength FVector2Array_GetLength;

        GamutMathApi_GetType I8Vector2_GetType;
        GamutMathApi_GetType I8Vector2Array_GetType;
        GamutMathApi_CreateI8Vector2 I8Vector2_Create;
        GamutMathApi_CreateI8Vector2Array I8Vector2Array_Create;
        GamutMathApi_GetI8Vector2ValuePointer I8Vector2_GetValuePointer;
        GamutMathApi_GetI8Vector2ValuePointer I8Vector2Array_GetValuePointer;
        GamutMathApi_GetArrayLength I8Vector2Array_GetLength;

        GamutMathApi_GetType U8Vector2_GetType;
        GamutMathApi_GetType U8Vector2Array_GetType;
        GamutMathApi_CreateU8Vector2 U8Vector2_Create;
        GamutMathApi_CreateU8Vector2Array U8Vector2Array_Create;
        GamutMathApi_GetU8Vector2ValuePointer U8Vector2_GetValuePointer;
        GamutMathApi_GetU8Vector2ValuePointer U8Vector2Array_GetValuePointer;
        GamutMathApi_GetArrayLength U8Vector2Array_GetLength;

        GamutMathApi_GetType I16Vector2_GetType;
        GamutMathApi_GetType I16Vector2Array_GetType;
        GamutMathApi_CreateI16Vector2 I16Vector2_Create;
        GamutMathApi_CreateI16Vector2Array I16Vector2Array_Create;
        GamutMathApi_GetI16Vector2ValuePointer I16Vector2_GetValuePointer;
        GamutMathApi_GetI16Vector2ValuePointer I16Vector2Array_GetValuePointer;
        GamutMathApi_GetArrayLength I16Vector2Array_GetLength;

        GamutMathApi_GetType U16Vector2_GetType;
        GamutMathApi_GetType U16Vector2Array_GetType;
        GamutMathApi_CreateU16Vector2 U16Vector2_Create;
        GamutMathApi_CreateU16Vector2Array U16Vector2Array_Create;
        GamutMathApi_GetU16Vector2ValuePointer U16Vector2_GetValuePointer;
        GamutMathApi_GetU16Vector2ValuePointer U16Vector2Array_GetValuePointer;
        GamutMathApi_GetArrayLength U16Vector2Array_GetLength;

        GamutMathApi_GetType I32Vector2_GetType;
        GamutMathApi_GetType I32Vector2Array_GetType;
        GamutMathApi_CreateI32Vector2 I32Vector2_Create;
        GamutMathApi_CreateI32Vector2Array I32Vector2Array_Create;
        GamutMathApi_GetI32Vector2ValuePointer I32Vector2_GetValuePointer;
        GamutMathApi_GetI32Vector2ValuePointer I32Vector2Array_GetValuePointer;
        GamutMathApi_GetArrayLength I32Vector2Array_GetLength;

        GamutMathApi_GetType U32Vector2_GetType;
        GamutMathApi_GetType U32Vector2Array_GetType;
        GamutMathApi_CreateU32Vector2 U32Vector2_Create;
        GamutMathApi_CreateU32Vector2Array U32Vector2Array_Create;
        GamutMathApi_GetU32Vector2ValuePointer U32Vector2_GetValuePointer;
        GamutMathApi_GetU32Vector2ValuePointer U32Vector2Array_GetValuePointer;
        GamutMathApi_GetArrayLength U32Vector2Array_GetLength;

        GamutMathApi_GetType IVector2_GetType;
        GamutMathApi_GetType IVector2Array_GetType;
        GamutMathApi_CreateIVector2 IVector2_Create;
        GamutMathApi_CreateIVector2Array IVector2Array_Create;
        GamutMathApi_GetIVector2ValuePointer IVector2_GetValuePointer;
        GamutMathApi_GetIVector2ValuePointer IVector2Array_GetValuePointer;
        GamutMathApi_GetArrayLength IVector2Array_GetLength;

        GamutMathApi_GetType UVector2_GetType;
        GamutMathApi_GetType UVector2Array_GetType;
        GamutMathApi_CreateUVector2 UVector2_Create;
        GamutMathApi_CreateUVector2Array UVector2Array_Create;
        GamutMathApi_GetUVector2ValuePointer UVector2_GetValuePointer;
        GamutMathApi_GetUVector2ValuePointer UVector2Array_GetValuePointer;
        GamutMathApi_GetArrayLength UVector2Array_GetLength;

        GamutMathApi_GetType I64Vector2_GetType;
        GamutMathApi_GetType I64Vector2Array_GetType;
        GamutMathApi_CreateI64Vector2 I64Vector2_Create;
        GamutMathApi_CreateI64Vector2Array I64Vector2Array_Create;
        GamutMathApi_GetI64Vector2ValuePointer I64Vector2_GetValuePointer;
        GamutMathApi_GetI64Vector2ValuePointer I64Vector2Array_GetValuePointer;
        GamutMathApi_GetArrayLength I64Vector2Array_GetLength;

        GamutMathApi_GetType U64Vector2_GetType;
        GamutMathApi_GetType U64Vector2Array_GetType;
        GamutMathApi_CreateU64Vector2 U64Vector2_Create;
        GamutMathApi_CreateU64Vector2Array U64Vector2Array_Create;
        GamutMathApi_GetU64Vector2ValuePointer U64Vector2_GetValuePointer;
        GamutMathApi_GetU64Vector2ValuePointer U64Vector2Array_GetValuePointer;
        GamutMathApi_GetArrayLength U64Vector2Array_GetLength;

        GamutMathApi_GetType BVector3_GetType;
        GamutMathApi_GetType BVector3Array_GetType;
        GamutMathApi_CreateBVector3 BVector3_Create;
        GamutMathApi_CreateBVector3Array BVector3Array_Create;
        GamutMathApi_GetBVector3ValuePointer BVector3_GetValuePointer;
        GamutMathApi_GetBVector3ValuePointer BVector3Array_GetValuePointer;
        GamutMathApi_GetArrayLength BVector3Array_GetLength;

        GamutMathApi_GetType DVector3_GetType;
        GamutMathApi_GetType DVector3Array_GetType;
        GamutMathApi_CreateDVector3 DVector3_Create;
        GamutMathApi_CreateDVector3Array DVector3Array_Create;
        GamutMathApi_GetDVector3ValuePointer DVector3_GetValuePointer;
        GamutMathApi_GetDVector3ValuePointer DVector3Array_GetValuePointer;
        GamutMathApi_GetArrayLength DVector3Array_GetLength;

        GamutMathApi_GetType FVector3_GetType;
        GamutMathApi_GetType FVector3Array_GetType;
        GamutMathApi_CreateFVector3 FVector3_Create;
        GamutMathApi_CreateFVector3Array FVector3Array_Create;
        GamutMathApi_GetFVector3ValuePointer FVector3_GetValuePointer;
        GamutMathApi_GetFVector3ValuePointer FVector3Array_GetValuePointer;
        GamutMathApi_GetArrayLength FVector3Array_GetLength;

        GamutMathApi_GetType I8Vector3_GetType;
        GamutMathApi_GetType I8Vector3Array_GetType;
        GamutMathApi_CreateI8Vector3 I8Vector3_Create;
        GamutMathApi_CreateI8Vector3Array I8Vector3Array_Create;
        GamutMathApi_GetI8Vector3ValuePointer I8Vector3_GetValuePointer;
        GamutMathApi_GetI8Vector3ValuePointer I8Vector3Array_GetValuePointer;
        GamutMathApi_GetArrayLength I8Vector3Array_GetLength;

        GamutMathApi_GetType U8Vector3_GetType;
        GamutMathApi_GetType U8Vector3Array_GetType;
        GamutMathApi_CreateU8Vector3 U8Vector3_Create;
        GamutMathApi_CreateU8Vector3Array U8Vector3Array_Create;
        GamutMathApi_GetU8Vector3ValuePointer U8Vector3_GetValuePointer;
        GamutMathApi_GetU8Vector3ValuePointer U8Vector3Array_GetValuePointer;
        GamutMathApi_GetArrayLength U8Vector3Array_GetLength;

        GamutMathApi_GetType I16Vector3_GetType;
        GamutMathApi_GetType I16Vector3Array_GetType;
        GamutMathApi_CreateI16Vector3 I16Vector3_Create;
        GamutMathApi_CreateI16Vector3Array I16Vector3Array_Create;
        GamutMathApi_GetI16Vector3ValuePointer I16Vector3_GetValuePointer;
        GamutMathApi_GetI16Vector3ValuePointer I16Vector3Array_GetValuePointer;
        GamutMathApi_GetArrayLength I16Vector3Array_GetLength;

        GamutMathApi_GetType U16Vector3_GetType;
        GamutMathApi_GetType U16Vector3Array_GetType;
        GamutMathApi_CreateU16Vector3 U16Vector3_Create;
        GamutMathApi_CreateU16Vector3Array U16Vector3Array_Create;
        GamutMathApi_GetU16Vector3ValuePointer U16Vector3_GetValuePointer;
        GamutMathApi_GetU16Vector3ValuePointer U16Vector3Array_GetValuePointer;
        GamutMathApi_GetArrayLength U16Vector3Array_GetLength;

        GamutMathApi_GetType I32Vector3_GetType;
        GamutMathApi_GetType I32Vector3Array_GetType;
        GamutMathApi_CreateI32Vector3 I32Vector3_Create;
        GamutMathApi_CreateI32Vector3Array I32Vector3Array_Create;
        GamutMathApi_GetI32Vector3ValuePointer I32Vector3_GetValuePointer;
        GamutMathApi_GetI32Vector3ValuePointer I32Vector3Array_GetValuePointer;
        GamutMathApi_GetArrayLength I32Vector3Array_GetLength;

        GamutMathApi_GetType U32Vector3_GetType;
        GamutMathApi_GetType U32Vector3Array_GetType;
        GamutMathApi_CreateU32Vector3 U32Vector3_Create;
        GamutMathApi_CreateU32Vector3Array U32Vector3Array_Create;
        GamutMathApi_GetU32Vector3ValuePointer U32Vector3_GetValuePointer;
        GamutMathApi_GetU32Vector3ValuePointer U32Vector3Array_GetValuePointer;
        GamutMathApi_GetArrayLength U32Vector3Array_GetLength;

        GamutMathApi_GetType IVector3_GetType;
        GamutMathApi_GetType IVector3Array_GetType;
        GamutMathApi_CreateIVector3 IVector3_Create;
        GamutMathApi_CreateIVector3Array IVector3Array_Create;
        GamutMathApi_GetIVector3ValuePointer IVector3_GetValuePointer;
        GamutMathApi_GetIVector3ValuePointer IVector3Array_GetValuePointer;
        GamutMathApi_GetArrayLength IVector3Array_GetLength;

        GamutMathApi_GetType UVector3_GetType;
        GamutMathApi_GetType UVector3Array_GetType;
        GamutMathApi_CreateUVector3 UVector3_Create;
        GamutMathApi_CreateUVector3Array UVector3Array_Create;
        GamutMathApi_GetUVector3ValuePointer UVector3_GetValuePointer;
        GamutMathApi_GetUVector3ValuePointer UVector3Array_GetValuePointer;
        GamutMathApi_GetArrayLength UVector3Array_GetLength;

        GamutMathApi_GetType I64Vector3_GetType;
        GamutMathApi_GetType I64Vector3Array_GetType;
        GamutMathApi_CreateI64Vector3 I64Vector3_Create;
        GamutMathApi_CreateI64Vector3Array I64Vector3Array_Create;
        GamutMathApi_GetI64Vector3ValuePointer I64Vector3_GetValuePointer;
        GamutMathApi_GetI64Vector3ValuePointer I64Vector3Array_GetValuePointer;
        GamutMathApi_GetArrayLength I64Vector3Array_GetLength;

        GamutMathApi_GetType U64Vector3_GetType;
        GamutMathApi_GetType U64Vector3Array_GetType;
        GamutMathApi_CreateU64Vector3 U64Vector3_Create;
        GamutMathApi_CreateU64Vector3Array U64Vector3Array_Create;
        GamutMathApi_GetU64Vector3ValuePointer U64Vector3_GetValuePointer;
        GamutMathApi_GetU64Vector3ValuePointer U64Vector3Array_GetValuePointer;
        GamutMathApi_GetArrayLength U64Vector3Array_GetLength;

        GamutMathApi_GetType BVector4_GetType;
        GamutMathApi_GetType BVector4Array_GetType;
        GamutMathApi_CreateBVector4 BVector4_Create;
        GamutMathApi_CreateBVector4Array BVector4Array_Create;
        GamutMathApi_GetBVector4ValuePointer BVector4_GetValuePointer;
        GamutMathApi_GetBVector4ValuePointer BVector4Array_GetValuePointer;
        GamutMathApi_GetArrayLength BVector4Array_GetLength;

        GamutMathApi_GetType DVector4_GetType;
        GamutMathApi_GetType DVector4Array_GetType;
        GamutMathApi_CreateDVector4 DVector4_Create;
        GamutMathApi_CreateDVector4Array DVector4Array_Create;
        GamutMathApi_GetDVector4ValuePointer DVector4_GetValuePointer;
        GamutMathApi_GetDVector4ValuePointer DVector4Array_GetValuePointer;
        GamutMathApi_GetArrayLength DVector4Array_GetLength;

        GamutMathApi_GetType FVector4_GetType;
        GamutMathApi_GetType FVector4Array_GetType;
        GamutMathApi_CreateFVector4 FVector4_Create;
        GamutMathApi_CreateFVector4Array FVector4Array_Create;
        GamutMathApi_GetFVector4ValuePointer FVector4_GetValuePointer;
        GamutMathApi_GetFVector4ValuePointer FVector4Array_GetValuePointer;
        GamutMathApi_GetArrayLength FVector4Array_GetLength;

        GamutMathApi_GetType I8Vector4_GetType;
        GamutMathApi_GetType I8Vector4Array_GetType;
        GamutMathApi_CreateI8Vector4 I8Vector4_Create;
        GamutMathApi_CreateI8Vector4Array I8Vector4Array_Create;
        GamutMathApi_GetI8Vector4ValuePointer I8Vector4_GetValuePointer;
        GamutMathApi_GetI8Vector4ValuePointer I8Vector4Array_GetValuePointer;
        GamutMathApi_GetArrayLength I8Vector4Array_GetLength;

        GamutMathApi_GetType U8Vector4_GetType;
        GamutMathApi_GetType U8Vector4Array_GetType;
        GamutMathApi_CreateU8Vector4 U8Vector4_Create;
        GamutMathApi_CreateU8Vector4Array U8Vector4Array_Create;
        GamutMathApi_GetU8Vector4ValuePointer U8Vector4_GetValuePointer;
        GamutMathApi_GetU8Vector4ValuePointer U8Vector4Array_GetValuePointer;
        GamutMathApi_GetArrayLength U8Vector4Array_GetLength;

        GamutMathApi_GetType I16Vector4_GetType;
        GamutMathApi_GetType I16Vector4Array_GetType;
        GamutMathApi_CreateI16Vector4 I16Vector4_Create;
        GamutMathApi_CreateI16Vector4Array I16Vector4Array_Create;
        GamutMathApi_GetI16Vector4ValuePointer I16Vector4_GetValuePointer;
        GamutMathApi_GetI16Vector4ValuePointer I16Vector4Array_GetValuePointer;
        GamutMathApi_GetArrayLength I16Vector4Array_GetLength;

        GamutMathApi_GetType U16Vector4_GetType;
        GamutMathApi_GetType U16Vector4Array_GetType;
        GamutMathApi_CreateU16Vector4 U16Vector4_Create;
        GamutMathApi_CreateU16Vector4Array U16Vector4Array_Create;
        GamutMathApi_GetU16Vector4ValuePointer U16Vector4_GetValuePointer;
        GamutMathApi_GetU16Vector4ValuePointer U16Vector4Array_GetValuePointer;
        GamutMathApi_GetArrayLength U16Vector4Array_GetLength;

        GamutMathApi_GetType I32Vector4_GetType;
        GamutMathApi_GetType I32Vector4Array_GetType;
        GamutMathApi_CreateI32Vector4 I32Vector4_Create;
        GamutMathApi_CreateI32Vector4Array I32Vector4Array_Create;
        GamutMathApi_GetI32Vector4ValuePointer I32Vector4_GetValuePointer;
        GamutMathApi_GetI32Vector4ValuePointer I32Vector4Array_GetValuePointer;
        GamutMathApi_GetArrayLength I32Vector4Array_GetLength;

        GamutMathApi_GetType U32Vector4_GetType;
        GamutMathApi_GetType U32Vector4Array_GetType;
        GamutMathApi_CreateU32Vector4 U32Vector4_Create;
        GamutMathApi_CreateU32Vector4Array U32Vector4Array_Create;
        GamutMathApi_GetU32Vector4ValuePointer U32Vector4_GetValuePointer;
        GamutMathApi_GetU32Vector4ValuePointer U32Vector4Array_GetValuePointer;
        GamutMathApi_GetArrayLength U32Vector4Array_GetLength;

        GamutMathApi_GetType IVector4_GetType;
        GamutMathApi_GetType IVector4Array_GetType;
        GamutMathApi_CreateIVector4 IVector4_Create;
        GamutMathApi_CreateIVector4Array IVector4Array_Create;
        GamutMathApi_GetIVector4ValuePointer IVector4_GetValuePointer;
        GamutMathApi_GetIVector4ValuePointer IVector4Array_GetValuePointer;
        GamutMathApi_GetArrayLength IVector4Array_GetLength;

        GamutMathApi_GetType UVector4_GetType;
        GamutMathApi_GetType UVector4Array_GetType;
        GamutMathApi_CreateUVector4 UVector4_Create;
        GamutMathApi_CreateUVector4Array UVector4Array_Create;
        GamutMathApi_GetUVector4ValuePointer UVector4_GetValuePointer;
        GamutMathApi_GetUVector4ValuePointer UVector4Array_GetValuePointer;
        GamutMathApi_GetArrayLength UVector4Array_GetLength;

        GamutMathApi_GetType I64Vector4_GetType;
        GamutMathApi_GetType I64Vector4Array_GetType;
        GamutMathApi_CreateI64Vector4 I64Vector4_Create;
        GamutMathApi_CreateI64Vector4Array I64Vector4Array_Create;
        GamutMathApi_GetI64Vector4ValuePointer I64Vector4_GetValuePointer;
        GamutMathApi_GetI64Vector4ValuePointer I64Vector4Array_GetValuePointer;
        GamutMathApi_GetArrayLength I64Vector4Array_GetLength;

        GamutMathApi_GetType U64Vector4_GetType;
        GamutMathApi_GetType U64Vector4Array_GetType;
        GamutMathApi_CreateU64Vector4 U64Vector4_Create;
        GamutMathApi_CreateU64Vector4Array U64Vector4Array_Create;
        GamutMathApi_GetU64Vector4ValuePointer U64Vector4_GetValuePointer;
        GamutMathApi_GetU64Vector4ValuePointer U64Vector4Array_GetValuePointer;
        GamutMathApi_GetArrayLength U64Vector4Array_GetLength;


        GamutMathApi_GetType DMatrix2x2_GetType;
        GamutMathApi_GetType DMatrix2x2Array_GetType;
        GamutMathApi_CreateDMatrix2x2 DMatrix2x2_Create;
        GamutMathApi_CreateDMatrix2x2Array DMatrix2x2Array_Create;
        GamutMathApi_GetDMatrix2x2ValuePointer DMatrix2x2_GetValuePointer;
        GamutMathApi_GetDMatrix2x2ValuePointer DMatrix2x2Array_GetValuePointer;
        GamutMathApi_GetArrayLength DMatrix2x2Array_GetLength;

        GamutMathApi_GetType FMatrix2x2_GetType;
        GamutMathApi_GetType FMatrix2x2Array_GetType;
        GamutMathApi_CreateFMatrix2x2 FMatrix2x2_Create;
        GamutMathApi_CreateFMatrix2x2Array FMatrix2x2Array_Create;
        GamutMathApi_GetFMatrix2x2ValuePointer FMatrix2x2_GetValuePointer;
        GamutMathApi_GetFMatrix2x2ValuePointer FMatrix2x2Array_GetValuePointer;
        GamutMathApi_GetArrayLength FMatrix2x2Array_GetLength;

        GamutMathApi_GetType DMatrix2x3_GetType;
        GamutMathApi_GetType DMatrix2x3Array_GetType;
        GamutMathApi_CreateDMatrix2x3 DMatrix2x3_Create;
        GamutMathApi_CreateDMatrix2x3Array DMatrix2x3Array_Create;
        GamutMathApi_GetDMatrix2x3ValuePointer DMatrix2x3_GetValuePointer;
        GamutMathApi_GetDMatrix2x3ValuePointer DMatrix2x3Array_GetValuePointer;
        GamutMathApi_GetArrayLength DMatrix2x3Array_GetLength;

        GamutMathApi_GetType FMatrix2x3_GetType;
        GamutMathApi_GetType FMatrix2x3Array_GetType;
        GamutMathApi_CreateFMatrix2x3 FMatrix2x3_Create;
        GamutMathApi_CreateFMatrix2x3Array FMatrix2x3Array_Create;
        GamutMathApi_GetFMatrix2x3ValuePointer FMatrix2x3_GetValuePointer;
        GamutMathApi_GetFMatrix2x3ValuePointer FMatrix2x3Array_GetValuePointer;
        GamutMathApi_GetArrayLength FMatrix2x3Array_GetLength;

        GamutMathApi_GetType DMatrix2x4_GetType;
        GamutMathApi_GetType DMatrix2x4Array_GetType;
        GamutMathApi_CreateDMatrix2x4 DMatrix2x4_Create;
        GamutMathApi_CreateDMatrix2x4Array DMatrix2x4Array_Create;
        GamutMathApi_GetDMatrix2x4ValuePointer DMatrix2x4_GetValuePointer;
        GamutMathApi_GetDMatrix2x4ValuePointer DMatrix2x4Array_GetValuePointer;
        GamutMathApi_GetArrayLength DMatrix2x4Array_GetLength;

        GamutMathApi_GetType FMatrix2x4_GetType;
        GamutMathApi_GetType FMatrix2x4Array_GetType;
        GamutMathApi_CreateFMatrix2x4 FMatrix2x4_Create;
        GamutMathApi_CreateFMatrix2x4Array FMatrix2x4Array_Create;
        GamutMathApi_GetFMatrix2x4ValuePointer FMatrix2x4_GetValuePointer;
        GamutMathApi_GetFMatrix2x4ValuePointer FMatrix2x4Array_GetValuePointer;
        GamutMathApi_GetArrayLength FMatrix2x4Array_GetLength;

        GamutMathApi_GetType DMatrix3x2_GetType;
        GamutMathApi_GetType DMatrix3x2Array_GetType;
        GamutMathApi_CreateDMatrix3x2 DMatrix3x2_Create;
        GamutMathApi_CreateDMatrix3x2Array DMatrix3x2Array_Create;
        GamutMathApi_GetDMatrix3x2ValuePointer DMatrix3x2_GetValuePointer;
        GamutMathApi_GetDMatrix3x2ValuePointer DMatrix3x2Array_GetValuePointer;
        GamutMathApi_GetArrayLength DMatrix3x2Array_GetLength;

        GamutMathApi_GetType FMatrix3x2_GetType;
        GamutMathApi_GetType FMatrix3x2Array_GetType;
        GamutMathApi_CreateFMatrix3x2 FMatrix3x2_Create;
        GamutMathApi_CreateFMatrix3x2Array FMatrix3x2Array_Create;
        GamutMathApi_GetFMatrix3x2ValuePointer FMatrix3x2_GetValuePointer;
        GamutMathApi_GetFMatrix3x2ValuePointer FMatrix3x2Array_GetValuePointer;
        GamutMathApi_GetArrayLength FMatrix3x2Array_GetLength;

        GamutMathApi_GetType DMatrix3x3_GetType;
        GamutMathApi_GetType DMatrix3x3Array_GetType;
        GamutMathApi_CreateDMatrix3x3 DMatrix3x3_Create;
        GamutMathApi_CreateDMatrix3x3Array DMatrix3x3Array_Create;
        GamutMathApi_GetDMatrix3x3ValuePointer DMatrix3x3_GetValuePointer;
        GamutMathApi_GetDMatrix3x3ValuePointer DMatrix3x3Array_GetValuePointer;
        GamutMathApi_GetArrayLength DMatrix3x3Array_GetLength;

        GamutMathApi_GetType FMatrix3x3_GetType;
        GamutMathApi_GetType FMatrix3x3Array_GetType;
        GamutMathApi_CreateFMatrix3x3 FMatrix3x3_Create;
        GamutMathApi_CreateFMatrix3x3Array FMatrix3x3Array_Create;
        GamutMathApi_GetFMatrix3x3ValuePointer FMatrix3x3_GetValuePointer;
        GamutMathApi_GetFMatrix3x3ValuePointer FMatrix3x3Array_GetValuePointer;
        GamutMathApi_GetArrayLength FMatrix3x3Array_GetLength;

        GamutMathApi_GetType DMatrix3x4_GetType;
        GamutMathApi_GetType DMatrix3x4Array_GetType;
        GamutMathApi_CreateDMatrix3x4 DMatrix3x4_Create;
        GamutMathApi_CreateDMatrix3x4Array DMatrix3x4Array_Create;
        GamutMathApi_GetDMatrix3x4ValuePointer DMatrix3x4_GetValuePointer;
        GamutMathApi_GetDMatrix3x4ValuePointer DMatrix3x4Array_GetValuePointer;
        GamutMathApi_GetArrayLength DMatrix3x4Array_GetLength;

        GamutMathApi_GetType FMatrix3x4_GetType;
        GamutMathApi_GetType FMatrix3x4Array_GetType;
        GamutMathApi_CreateFMatrix3x4 FMatrix3x4_Create;
        GamutMathApi_CreateFMatrix3x4Array FMatrix3x4Array_Create;
        GamutMathApi_GetFMatrix3x4ValuePointer FMatrix3x4_GetValuePointer;
        GamutMathApi_GetFMatrix3x4ValuePointer FMatrix3x4Array_GetValuePointer;
        GamutMathApi_GetArrayLength FMatrix3x4Array_GetLength;

        GamutMathApi_GetType DMatrix4x2_GetType;
        GamutMathApi_GetType DMatrix4x2Array_GetType;
        GamutMathApi_CreateDMatrix4x2 DMatrix4x2_Create;
        GamutMathApi_CreateDMatrix4x2Array DMatrix4x2Array_Create;
        GamutMathApi_GetDMatrix4x2ValuePointer DMatrix4x2_GetValuePointer;
        GamutMathApi_GetDMatrix4x2ValuePointer DMatrix4x2Array_GetValuePointer;
        GamutMathApi_GetArrayLength DMatrix4x2Array_GetLength;

        GamutMathApi_GetType FMatrix4x2_GetType;
        GamutMathApi_GetType FMatrix4x2Array_GetType;
        GamutMathApi_CreateFMatrix4x2 FMatrix4x2_Create;
        GamutMathApi_CreateFMatrix4x2Array FMatrix4x2Array_Create;
        GamutMathApi_GetFMatrix4x2ValuePointer FMatrix4x2_GetValuePointer;
        GamutMathApi_GetFMatrix4x2ValuePointer FMatrix4x2Array_GetValuePointer;
        GamutMathApi_GetArrayLength FMatrix4x2Array_GetLength;

        GamutMathApi_GetType DMatrix4x3_GetType;
        GamutMathApi_GetType DMatrix4x3Array_GetType;
        GamutMathApi_CreateDMatrix4x3 DMatrix4x3_Create;
        GamutMathApi_CreateDMatrix4x3Array DMatrix4x3Array_Create;
        GamutMathApi_GetDMatrix4x3ValuePointer DMatrix4x3_GetValuePointer;
        GamutMathApi_GetDMatrix4x3ValuePointer DMatrix4x3Array_GetValuePointer;
        GamutMathApi_GetArrayLength DMatrix4x3Array_GetLength;

        GamutMathApi_GetType FMatrix4x3_GetType;
        GamutMathApi_GetType FMatrix4x3Array_GetType;
        GamutMathApi_CreateFMatrix4x3 FMatrix4x3_Create;
        GamutMathApi_CreateFMatrix4x3Array FMatrix4x3Array_Create;
        GamutMathApi_GetFMatrix4x3ValuePointer FMatrix4x3_GetValuePointer;
        GamutMathApi_GetFMatrix4x3ValuePointer FMatrix4x3Array_GetValuePointer;
        GamutMathApi_GetArrayLength FMatrix4x3Array_GetLength;

        GamutMathApi_GetType DMatrix4x4_GetType;
        GamutMathApi_GetType DMatrix4x4Array_GetType;
        GamutMathApi_CreateDMatrix4x4 DMatrix4x4_Create;
        GamutMathApi_CreateDMatrix4x4Array DMatrix4x4Array_Create;
        GamutMathApi_GetDMatrix4x4ValuePointer DMatrix4x4_GetValuePointer;
        GamutMathApi_GetDMatrix4x4ValuePointer DMatrix4x4Array_GetValuePointer;
        GamutMathApi_GetArrayLength DMatrix4x4Array_GetLength;

        GamutMathApi_GetType FMatrix4x4_GetType;
        GamutMathApi_GetType FMatrix4x4Array_GetType;
        GamutMathApi_CreateFMatrix4x4 FMatrix4x4_Create;
        GamutMathApi_CreateFMatrix4x4Array FMatrix4x4Array_Create;
        GamutMathApi_GetFMatrix4x4ValuePointer FMatrix4x4_GetValuePointer;
        GamutMathApi_GetFMatrix4x4ValuePointer FMatrix4x4Array_GetValuePointer;
        GamutMathApi_GetArrayLength FMatrix4x4Array_GetLength;


        GamutMathApi_GetType DQuaternion_GetType;
        GamutMathApi_GetType DQuaternionArray_GetType;
        GamutMathApi_CreateDQuaternion DQuaternion_Create;
        GamutMathApi_CreateDQuaternionArray DQuaternionArray_Create;
        GamutMathApi_GetDQuaternionValuePointer DQuaternion_GetValuePointer;
        GamutMathApi_GetDQuaternionValuePointer DQuaternionArray_GetValuePointer;
        GamutMathApi_GetArrayLength DQuaternionArray_GetLength;

        GamutMathApi_GetType FQuaternion_GetType;
        GamutMathApi_GetType FQuaternionArray_GetType;
        GamutMathApi_CreateFQuaternion FQuaternion_Create;
        GamutMathApi_CreateFQuaternionArray FQuaternionArray_Create;
        GamutMathApi_GetFQuaternionValuePointer FQuaternion_GetValuePointer;
        GamutMathApi_GetFQuaternionValuePointer FQuaternionArray_GetValuePointer;
        GamutMathApi_GetArrayLength FQuaternionArray_GetLength;


        GamutMathApi_GetType BArray_GetType;
        GamutMathApi_CreateBArray BArray_Create;
        GamutMathApi_GetBValuePointer BArray_GetValuePointer;
        GamutMathApi_GetArrayLength BArray_GetLength;

        GamutMathApi_GetType DArray_GetType;
        GamutMathApi_CreateDArray DArray_Create;
        GamutMathApi_GetDValuePointer DArray_GetValuePointer;
        GamutMathApi_GetArrayLength DArray_GetLength;

        GamutMathApi_GetType FArray_GetType;
        GamutMathApi_CreateFArray FArray_Create;
        GamutMathApi_GetFValuePointer FArray_GetValuePointer;
        GamutMathApi_GetArrayLength FArray_GetLength;

        GamutMathApi_GetType I8Array_GetType;
        GamutMathApi_CreateI8Array I8Array_Create;
        GamutMathApi_GetI8ValuePointer I8Array_GetValuePointer;
        GamutMathApi_GetArrayLength I8Array_GetLength;

        GamutMathApi_GetType U8Array_GetType;
        GamutMathApi_CreateU8Array U8Array_Create;
        GamutMathApi_GetU8ValuePointer U8Array_GetValuePointer;
        GamutMathApi_GetArrayLength U8Array_GetLength;

        GamutMathApi_GetType I16Array_GetType;
        GamutMathApi_CreateI16Array I16Array_Create;
        GamutMathApi_GetI16ValuePointer I16Array_GetValuePointer;
        GamutMathApi_GetArrayLength I16Array_GetLength;

        GamutMathApi_GetType U16Array_GetType;
        GamutMathApi_CreateU16Array U16Array_Create;
        GamutMathApi_GetU16ValuePointer U16Array_GetValuePointer;
        GamutMathApi_GetArrayLength U16Array_GetLength;

        GamutMathApi_GetType I32Array_GetType;
        GamutMathApi_CreateI32Array I32Array_Create;
        GamutMathApi_GetI32ValuePointer I32Array_GetValuePointer;
        GamutMathApi_GetArrayLength I32Array_GetLength;

        GamutMathApi_GetType U32Array_GetType;
        GamutMathApi_CreateU32Array U32Array_Create;
        GamutMathApi_GetU32ValuePointer U32Array_GetValuePointer;
        GamutMathApi_GetArrayLength U32Array_GetLength;

        GamutMathApi_GetType IArray_GetType;
        GamutMathApi_CreateIArray IArray_Create;
        GamutMathApi_GetIValuePointer IArray_GetValuePointer;
        GamutMathApi_GetArrayLength IArray_GetLength;

        GamutMathApi_GetType UArray_GetType;
        GamutMathApi_CreateUArray UArray_Create;
        GamutMathApi_GetUValuePointer UArray_GetValuePointer;
        GamutMathApi_GetArrayLength UArray_GetLength;

        GamutMathApi_GetType I64Array_GetType;
        GamutMathApi_CreateI64Array I64Array_Create;
        GamutMathApi_GetI64ValuePointer I64Array_GetValuePointer;
        GamutMathApi_GetArrayLength I64Array_GetLength;

        GamutMathApi_GetType U64Array_GetType;
        GamutMathApi_CreateU64Array U64Array_Create;
        GamutMathApi_GetU64ValuePointer U64Array_GetValuePointer;
        GamutMathApi_GetArrayLength U64Array_GetLength;

};

static struct GamutMathApi *
GamutMathApi_Get()
{
    if (!PyImport_ImportModule("gamut.math._math")){ return 0; }
    return (struct GamutMathApi *)PyCapsule_Import("gamut.math._math._api", 0);
}

static void
GamutMathApi_Release()
{
    PyObject *module = PyImport_ImportModule("gamut.math._math");
    if (!module){ return; }
    Py_DECREF(module);
    Py_DECREF(module);
}

#ifdef __cplusplus
}
#endif

#endif