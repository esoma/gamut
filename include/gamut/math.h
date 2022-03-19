
// generated 2022-03-19 16:50:14.803341 from codegen/math/templates/math.h

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

        GamutMathApi_GetType GamutMathBVector1_GetType;
        GamutMathApi_GetType GamutMathBVector1Array_GetType;
        GamutMathApi_CreateBVector1 GamutMathBVector1_Create;
        GamutMathApi_CreateBVector1Array GamutMathBVector1Array_Create;
        GamutMathApi_GetBVector1ValuePointer GamutMathBVector1_GetValuePointer;
        GamutMathApi_GetBVector1ValuePointer GamutMathBVector1Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathBVector1Array_GetLength;

        GamutMathApi_GetType GamutMathDVector1_GetType;
        GamutMathApi_GetType GamutMathDVector1Array_GetType;
        GamutMathApi_CreateDVector1 GamutMathDVector1_Create;
        GamutMathApi_CreateDVector1Array GamutMathDVector1Array_Create;
        GamutMathApi_GetDVector1ValuePointer GamutMathDVector1_GetValuePointer;
        GamutMathApi_GetDVector1ValuePointer GamutMathDVector1Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathDVector1Array_GetLength;

        GamutMathApi_GetType GamutMathFVector1_GetType;
        GamutMathApi_GetType GamutMathFVector1Array_GetType;
        GamutMathApi_CreateFVector1 GamutMathFVector1_Create;
        GamutMathApi_CreateFVector1Array GamutMathFVector1Array_Create;
        GamutMathApi_GetFVector1ValuePointer GamutMathFVector1_GetValuePointer;
        GamutMathApi_GetFVector1ValuePointer GamutMathFVector1Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathFVector1Array_GetLength;

        GamutMathApi_GetType GamutMathI8Vector1_GetType;
        GamutMathApi_GetType GamutMathI8Vector1Array_GetType;
        GamutMathApi_CreateI8Vector1 GamutMathI8Vector1_Create;
        GamutMathApi_CreateI8Vector1Array GamutMathI8Vector1Array_Create;
        GamutMathApi_GetI8Vector1ValuePointer GamutMathI8Vector1_GetValuePointer;
        GamutMathApi_GetI8Vector1ValuePointer GamutMathI8Vector1Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathI8Vector1Array_GetLength;

        GamutMathApi_GetType GamutMathU8Vector1_GetType;
        GamutMathApi_GetType GamutMathU8Vector1Array_GetType;
        GamutMathApi_CreateU8Vector1 GamutMathU8Vector1_Create;
        GamutMathApi_CreateU8Vector1Array GamutMathU8Vector1Array_Create;
        GamutMathApi_GetU8Vector1ValuePointer GamutMathU8Vector1_GetValuePointer;
        GamutMathApi_GetU8Vector1ValuePointer GamutMathU8Vector1Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathU8Vector1Array_GetLength;

        GamutMathApi_GetType GamutMathI16Vector1_GetType;
        GamutMathApi_GetType GamutMathI16Vector1Array_GetType;
        GamutMathApi_CreateI16Vector1 GamutMathI16Vector1_Create;
        GamutMathApi_CreateI16Vector1Array GamutMathI16Vector1Array_Create;
        GamutMathApi_GetI16Vector1ValuePointer GamutMathI16Vector1_GetValuePointer;
        GamutMathApi_GetI16Vector1ValuePointer GamutMathI16Vector1Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathI16Vector1Array_GetLength;

        GamutMathApi_GetType GamutMathU16Vector1_GetType;
        GamutMathApi_GetType GamutMathU16Vector1Array_GetType;
        GamutMathApi_CreateU16Vector1 GamutMathU16Vector1_Create;
        GamutMathApi_CreateU16Vector1Array GamutMathU16Vector1Array_Create;
        GamutMathApi_GetU16Vector1ValuePointer GamutMathU16Vector1_GetValuePointer;
        GamutMathApi_GetU16Vector1ValuePointer GamutMathU16Vector1Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathU16Vector1Array_GetLength;

        GamutMathApi_GetType GamutMathI32Vector1_GetType;
        GamutMathApi_GetType GamutMathI32Vector1Array_GetType;
        GamutMathApi_CreateI32Vector1 GamutMathI32Vector1_Create;
        GamutMathApi_CreateI32Vector1Array GamutMathI32Vector1Array_Create;
        GamutMathApi_GetI32Vector1ValuePointer GamutMathI32Vector1_GetValuePointer;
        GamutMathApi_GetI32Vector1ValuePointer GamutMathI32Vector1Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathI32Vector1Array_GetLength;

        GamutMathApi_GetType GamutMathU32Vector1_GetType;
        GamutMathApi_GetType GamutMathU32Vector1Array_GetType;
        GamutMathApi_CreateU32Vector1 GamutMathU32Vector1_Create;
        GamutMathApi_CreateU32Vector1Array GamutMathU32Vector1Array_Create;
        GamutMathApi_GetU32Vector1ValuePointer GamutMathU32Vector1_GetValuePointer;
        GamutMathApi_GetU32Vector1ValuePointer GamutMathU32Vector1Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathU32Vector1Array_GetLength;

        GamutMathApi_GetType GamutMathIVector1_GetType;
        GamutMathApi_GetType GamutMathIVector1Array_GetType;
        GamutMathApi_CreateIVector1 GamutMathIVector1_Create;
        GamutMathApi_CreateIVector1Array GamutMathIVector1Array_Create;
        GamutMathApi_GetIVector1ValuePointer GamutMathIVector1_GetValuePointer;
        GamutMathApi_GetIVector1ValuePointer GamutMathIVector1Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathIVector1Array_GetLength;

        GamutMathApi_GetType GamutMathUVector1_GetType;
        GamutMathApi_GetType GamutMathUVector1Array_GetType;
        GamutMathApi_CreateUVector1 GamutMathUVector1_Create;
        GamutMathApi_CreateUVector1Array GamutMathUVector1Array_Create;
        GamutMathApi_GetUVector1ValuePointer GamutMathUVector1_GetValuePointer;
        GamutMathApi_GetUVector1ValuePointer GamutMathUVector1Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathUVector1Array_GetLength;

        GamutMathApi_GetType GamutMathI64Vector1_GetType;
        GamutMathApi_GetType GamutMathI64Vector1Array_GetType;
        GamutMathApi_CreateI64Vector1 GamutMathI64Vector1_Create;
        GamutMathApi_CreateI64Vector1Array GamutMathI64Vector1Array_Create;
        GamutMathApi_GetI64Vector1ValuePointer GamutMathI64Vector1_GetValuePointer;
        GamutMathApi_GetI64Vector1ValuePointer GamutMathI64Vector1Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathI64Vector1Array_GetLength;

        GamutMathApi_GetType GamutMathU64Vector1_GetType;
        GamutMathApi_GetType GamutMathU64Vector1Array_GetType;
        GamutMathApi_CreateU64Vector1 GamutMathU64Vector1_Create;
        GamutMathApi_CreateU64Vector1Array GamutMathU64Vector1Array_Create;
        GamutMathApi_GetU64Vector1ValuePointer GamutMathU64Vector1_GetValuePointer;
        GamutMathApi_GetU64Vector1ValuePointer GamutMathU64Vector1Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathU64Vector1Array_GetLength;

        GamutMathApi_GetType GamutMathBVector2_GetType;
        GamutMathApi_GetType GamutMathBVector2Array_GetType;
        GamutMathApi_CreateBVector2 GamutMathBVector2_Create;
        GamutMathApi_CreateBVector2Array GamutMathBVector2Array_Create;
        GamutMathApi_GetBVector2ValuePointer GamutMathBVector2_GetValuePointer;
        GamutMathApi_GetBVector2ValuePointer GamutMathBVector2Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathBVector2Array_GetLength;

        GamutMathApi_GetType GamutMathDVector2_GetType;
        GamutMathApi_GetType GamutMathDVector2Array_GetType;
        GamutMathApi_CreateDVector2 GamutMathDVector2_Create;
        GamutMathApi_CreateDVector2Array GamutMathDVector2Array_Create;
        GamutMathApi_GetDVector2ValuePointer GamutMathDVector2_GetValuePointer;
        GamutMathApi_GetDVector2ValuePointer GamutMathDVector2Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathDVector2Array_GetLength;

        GamutMathApi_GetType GamutMathFVector2_GetType;
        GamutMathApi_GetType GamutMathFVector2Array_GetType;
        GamutMathApi_CreateFVector2 GamutMathFVector2_Create;
        GamutMathApi_CreateFVector2Array GamutMathFVector2Array_Create;
        GamutMathApi_GetFVector2ValuePointer GamutMathFVector2_GetValuePointer;
        GamutMathApi_GetFVector2ValuePointer GamutMathFVector2Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathFVector2Array_GetLength;

        GamutMathApi_GetType GamutMathI8Vector2_GetType;
        GamutMathApi_GetType GamutMathI8Vector2Array_GetType;
        GamutMathApi_CreateI8Vector2 GamutMathI8Vector2_Create;
        GamutMathApi_CreateI8Vector2Array GamutMathI8Vector2Array_Create;
        GamutMathApi_GetI8Vector2ValuePointer GamutMathI8Vector2_GetValuePointer;
        GamutMathApi_GetI8Vector2ValuePointer GamutMathI8Vector2Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathI8Vector2Array_GetLength;

        GamutMathApi_GetType GamutMathU8Vector2_GetType;
        GamutMathApi_GetType GamutMathU8Vector2Array_GetType;
        GamutMathApi_CreateU8Vector2 GamutMathU8Vector2_Create;
        GamutMathApi_CreateU8Vector2Array GamutMathU8Vector2Array_Create;
        GamutMathApi_GetU8Vector2ValuePointer GamutMathU8Vector2_GetValuePointer;
        GamutMathApi_GetU8Vector2ValuePointer GamutMathU8Vector2Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathU8Vector2Array_GetLength;

        GamutMathApi_GetType GamutMathI16Vector2_GetType;
        GamutMathApi_GetType GamutMathI16Vector2Array_GetType;
        GamutMathApi_CreateI16Vector2 GamutMathI16Vector2_Create;
        GamutMathApi_CreateI16Vector2Array GamutMathI16Vector2Array_Create;
        GamutMathApi_GetI16Vector2ValuePointer GamutMathI16Vector2_GetValuePointer;
        GamutMathApi_GetI16Vector2ValuePointer GamutMathI16Vector2Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathI16Vector2Array_GetLength;

        GamutMathApi_GetType GamutMathU16Vector2_GetType;
        GamutMathApi_GetType GamutMathU16Vector2Array_GetType;
        GamutMathApi_CreateU16Vector2 GamutMathU16Vector2_Create;
        GamutMathApi_CreateU16Vector2Array GamutMathU16Vector2Array_Create;
        GamutMathApi_GetU16Vector2ValuePointer GamutMathU16Vector2_GetValuePointer;
        GamutMathApi_GetU16Vector2ValuePointer GamutMathU16Vector2Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathU16Vector2Array_GetLength;

        GamutMathApi_GetType GamutMathI32Vector2_GetType;
        GamutMathApi_GetType GamutMathI32Vector2Array_GetType;
        GamutMathApi_CreateI32Vector2 GamutMathI32Vector2_Create;
        GamutMathApi_CreateI32Vector2Array GamutMathI32Vector2Array_Create;
        GamutMathApi_GetI32Vector2ValuePointer GamutMathI32Vector2_GetValuePointer;
        GamutMathApi_GetI32Vector2ValuePointer GamutMathI32Vector2Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathI32Vector2Array_GetLength;

        GamutMathApi_GetType GamutMathU32Vector2_GetType;
        GamutMathApi_GetType GamutMathU32Vector2Array_GetType;
        GamutMathApi_CreateU32Vector2 GamutMathU32Vector2_Create;
        GamutMathApi_CreateU32Vector2Array GamutMathU32Vector2Array_Create;
        GamutMathApi_GetU32Vector2ValuePointer GamutMathU32Vector2_GetValuePointer;
        GamutMathApi_GetU32Vector2ValuePointer GamutMathU32Vector2Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathU32Vector2Array_GetLength;

        GamutMathApi_GetType GamutMathIVector2_GetType;
        GamutMathApi_GetType GamutMathIVector2Array_GetType;
        GamutMathApi_CreateIVector2 GamutMathIVector2_Create;
        GamutMathApi_CreateIVector2Array GamutMathIVector2Array_Create;
        GamutMathApi_GetIVector2ValuePointer GamutMathIVector2_GetValuePointer;
        GamutMathApi_GetIVector2ValuePointer GamutMathIVector2Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathIVector2Array_GetLength;

        GamutMathApi_GetType GamutMathUVector2_GetType;
        GamutMathApi_GetType GamutMathUVector2Array_GetType;
        GamutMathApi_CreateUVector2 GamutMathUVector2_Create;
        GamutMathApi_CreateUVector2Array GamutMathUVector2Array_Create;
        GamutMathApi_GetUVector2ValuePointer GamutMathUVector2_GetValuePointer;
        GamutMathApi_GetUVector2ValuePointer GamutMathUVector2Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathUVector2Array_GetLength;

        GamutMathApi_GetType GamutMathI64Vector2_GetType;
        GamutMathApi_GetType GamutMathI64Vector2Array_GetType;
        GamutMathApi_CreateI64Vector2 GamutMathI64Vector2_Create;
        GamutMathApi_CreateI64Vector2Array GamutMathI64Vector2Array_Create;
        GamutMathApi_GetI64Vector2ValuePointer GamutMathI64Vector2_GetValuePointer;
        GamutMathApi_GetI64Vector2ValuePointer GamutMathI64Vector2Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathI64Vector2Array_GetLength;

        GamutMathApi_GetType GamutMathU64Vector2_GetType;
        GamutMathApi_GetType GamutMathU64Vector2Array_GetType;
        GamutMathApi_CreateU64Vector2 GamutMathU64Vector2_Create;
        GamutMathApi_CreateU64Vector2Array GamutMathU64Vector2Array_Create;
        GamutMathApi_GetU64Vector2ValuePointer GamutMathU64Vector2_GetValuePointer;
        GamutMathApi_GetU64Vector2ValuePointer GamutMathU64Vector2Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathU64Vector2Array_GetLength;

        GamutMathApi_GetType GamutMathBVector3_GetType;
        GamutMathApi_GetType GamutMathBVector3Array_GetType;
        GamutMathApi_CreateBVector3 GamutMathBVector3_Create;
        GamutMathApi_CreateBVector3Array GamutMathBVector3Array_Create;
        GamutMathApi_GetBVector3ValuePointer GamutMathBVector3_GetValuePointer;
        GamutMathApi_GetBVector3ValuePointer GamutMathBVector3Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathBVector3Array_GetLength;

        GamutMathApi_GetType GamutMathDVector3_GetType;
        GamutMathApi_GetType GamutMathDVector3Array_GetType;
        GamutMathApi_CreateDVector3 GamutMathDVector3_Create;
        GamutMathApi_CreateDVector3Array GamutMathDVector3Array_Create;
        GamutMathApi_GetDVector3ValuePointer GamutMathDVector3_GetValuePointer;
        GamutMathApi_GetDVector3ValuePointer GamutMathDVector3Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathDVector3Array_GetLength;

        GamutMathApi_GetType GamutMathFVector3_GetType;
        GamutMathApi_GetType GamutMathFVector3Array_GetType;
        GamutMathApi_CreateFVector3 GamutMathFVector3_Create;
        GamutMathApi_CreateFVector3Array GamutMathFVector3Array_Create;
        GamutMathApi_GetFVector3ValuePointer GamutMathFVector3_GetValuePointer;
        GamutMathApi_GetFVector3ValuePointer GamutMathFVector3Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathFVector3Array_GetLength;

        GamutMathApi_GetType GamutMathI8Vector3_GetType;
        GamutMathApi_GetType GamutMathI8Vector3Array_GetType;
        GamutMathApi_CreateI8Vector3 GamutMathI8Vector3_Create;
        GamutMathApi_CreateI8Vector3Array GamutMathI8Vector3Array_Create;
        GamutMathApi_GetI8Vector3ValuePointer GamutMathI8Vector3_GetValuePointer;
        GamutMathApi_GetI8Vector3ValuePointer GamutMathI8Vector3Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathI8Vector3Array_GetLength;

        GamutMathApi_GetType GamutMathU8Vector3_GetType;
        GamutMathApi_GetType GamutMathU8Vector3Array_GetType;
        GamutMathApi_CreateU8Vector3 GamutMathU8Vector3_Create;
        GamutMathApi_CreateU8Vector3Array GamutMathU8Vector3Array_Create;
        GamutMathApi_GetU8Vector3ValuePointer GamutMathU8Vector3_GetValuePointer;
        GamutMathApi_GetU8Vector3ValuePointer GamutMathU8Vector3Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathU8Vector3Array_GetLength;

        GamutMathApi_GetType GamutMathI16Vector3_GetType;
        GamutMathApi_GetType GamutMathI16Vector3Array_GetType;
        GamutMathApi_CreateI16Vector3 GamutMathI16Vector3_Create;
        GamutMathApi_CreateI16Vector3Array GamutMathI16Vector3Array_Create;
        GamutMathApi_GetI16Vector3ValuePointer GamutMathI16Vector3_GetValuePointer;
        GamutMathApi_GetI16Vector3ValuePointer GamutMathI16Vector3Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathI16Vector3Array_GetLength;

        GamutMathApi_GetType GamutMathU16Vector3_GetType;
        GamutMathApi_GetType GamutMathU16Vector3Array_GetType;
        GamutMathApi_CreateU16Vector3 GamutMathU16Vector3_Create;
        GamutMathApi_CreateU16Vector3Array GamutMathU16Vector3Array_Create;
        GamutMathApi_GetU16Vector3ValuePointer GamutMathU16Vector3_GetValuePointer;
        GamutMathApi_GetU16Vector3ValuePointer GamutMathU16Vector3Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathU16Vector3Array_GetLength;

        GamutMathApi_GetType GamutMathI32Vector3_GetType;
        GamutMathApi_GetType GamutMathI32Vector3Array_GetType;
        GamutMathApi_CreateI32Vector3 GamutMathI32Vector3_Create;
        GamutMathApi_CreateI32Vector3Array GamutMathI32Vector3Array_Create;
        GamutMathApi_GetI32Vector3ValuePointer GamutMathI32Vector3_GetValuePointer;
        GamutMathApi_GetI32Vector3ValuePointer GamutMathI32Vector3Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathI32Vector3Array_GetLength;

        GamutMathApi_GetType GamutMathU32Vector3_GetType;
        GamutMathApi_GetType GamutMathU32Vector3Array_GetType;
        GamutMathApi_CreateU32Vector3 GamutMathU32Vector3_Create;
        GamutMathApi_CreateU32Vector3Array GamutMathU32Vector3Array_Create;
        GamutMathApi_GetU32Vector3ValuePointer GamutMathU32Vector3_GetValuePointer;
        GamutMathApi_GetU32Vector3ValuePointer GamutMathU32Vector3Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathU32Vector3Array_GetLength;

        GamutMathApi_GetType GamutMathIVector3_GetType;
        GamutMathApi_GetType GamutMathIVector3Array_GetType;
        GamutMathApi_CreateIVector3 GamutMathIVector3_Create;
        GamutMathApi_CreateIVector3Array GamutMathIVector3Array_Create;
        GamutMathApi_GetIVector3ValuePointer GamutMathIVector3_GetValuePointer;
        GamutMathApi_GetIVector3ValuePointer GamutMathIVector3Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathIVector3Array_GetLength;

        GamutMathApi_GetType GamutMathUVector3_GetType;
        GamutMathApi_GetType GamutMathUVector3Array_GetType;
        GamutMathApi_CreateUVector3 GamutMathUVector3_Create;
        GamutMathApi_CreateUVector3Array GamutMathUVector3Array_Create;
        GamutMathApi_GetUVector3ValuePointer GamutMathUVector3_GetValuePointer;
        GamutMathApi_GetUVector3ValuePointer GamutMathUVector3Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathUVector3Array_GetLength;

        GamutMathApi_GetType GamutMathI64Vector3_GetType;
        GamutMathApi_GetType GamutMathI64Vector3Array_GetType;
        GamutMathApi_CreateI64Vector3 GamutMathI64Vector3_Create;
        GamutMathApi_CreateI64Vector3Array GamutMathI64Vector3Array_Create;
        GamutMathApi_GetI64Vector3ValuePointer GamutMathI64Vector3_GetValuePointer;
        GamutMathApi_GetI64Vector3ValuePointer GamutMathI64Vector3Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathI64Vector3Array_GetLength;

        GamutMathApi_GetType GamutMathU64Vector3_GetType;
        GamutMathApi_GetType GamutMathU64Vector3Array_GetType;
        GamutMathApi_CreateU64Vector3 GamutMathU64Vector3_Create;
        GamutMathApi_CreateU64Vector3Array GamutMathU64Vector3Array_Create;
        GamutMathApi_GetU64Vector3ValuePointer GamutMathU64Vector3_GetValuePointer;
        GamutMathApi_GetU64Vector3ValuePointer GamutMathU64Vector3Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathU64Vector3Array_GetLength;

        GamutMathApi_GetType GamutMathBVector4_GetType;
        GamutMathApi_GetType GamutMathBVector4Array_GetType;
        GamutMathApi_CreateBVector4 GamutMathBVector4_Create;
        GamutMathApi_CreateBVector4Array GamutMathBVector4Array_Create;
        GamutMathApi_GetBVector4ValuePointer GamutMathBVector4_GetValuePointer;
        GamutMathApi_GetBVector4ValuePointer GamutMathBVector4Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathBVector4Array_GetLength;

        GamutMathApi_GetType GamutMathDVector4_GetType;
        GamutMathApi_GetType GamutMathDVector4Array_GetType;
        GamutMathApi_CreateDVector4 GamutMathDVector4_Create;
        GamutMathApi_CreateDVector4Array GamutMathDVector4Array_Create;
        GamutMathApi_GetDVector4ValuePointer GamutMathDVector4_GetValuePointer;
        GamutMathApi_GetDVector4ValuePointer GamutMathDVector4Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathDVector4Array_GetLength;

        GamutMathApi_GetType GamutMathFVector4_GetType;
        GamutMathApi_GetType GamutMathFVector4Array_GetType;
        GamutMathApi_CreateFVector4 GamutMathFVector4_Create;
        GamutMathApi_CreateFVector4Array GamutMathFVector4Array_Create;
        GamutMathApi_GetFVector4ValuePointer GamutMathFVector4_GetValuePointer;
        GamutMathApi_GetFVector4ValuePointer GamutMathFVector4Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathFVector4Array_GetLength;

        GamutMathApi_GetType GamutMathI8Vector4_GetType;
        GamutMathApi_GetType GamutMathI8Vector4Array_GetType;
        GamutMathApi_CreateI8Vector4 GamutMathI8Vector4_Create;
        GamutMathApi_CreateI8Vector4Array GamutMathI8Vector4Array_Create;
        GamutMathApi_GetI8Vector4ValuePointer GamutMathI8Vector4_GetValuePointer;
        GamutMathApi_GetI8Vector4ValuePointer GamutMathI8Vector4Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathI8Vector4Array_GetLength;

        GamutMathApi_GetType GamutMathU8Vector4_GetType;
        GamutMathApi_GetType GamutMathU8Vector4Array_GetType;
        GamutMathApi_CreateU8Vector4 GamutMathU8Vector4_Create;
        GamutMathApi_CreateU8Vector4Array GamutMathU8Vector4Array_Create;
        GamutMathApi_GetU8Vector4ValuePointer GamutMathU8Vector4_GetValuePointer;
        GamutMathApi_GetU8Vector4ValuePointer GamutMathU8Vector4Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathU8Vector4Array_GetLength;

        GamutMathApi_GetType GamutMathI16Vector4_GetType;
        GamutMathApi_GetType GamutMathI16Vector4Array_GetType;
        GamutMathApi_CreateI16Vector4 GamutMathI16Vector4_Create;
        GamutMathApi_CreateI16Vector4Array GamutMathI16Vector4Array_Create;
        GamutMathApi_GetI16Vector4ValuePointer GamutMathI16Vector4_GetValuePointer;
        GamutMathApi_GetI16Vector4ValuePointer GamutMathI16Vector4Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathI16Vector4Array_GetLength;

        GamutMathApi_GetType GamutMathU16Vector4_GetType;
        GamutMathApi_GetType GamutMathU16Vector4Array_GetType;
        GamutMathApi_CreateU16Vector4 GamutMathU16Vector4_Create;
        GamutMathApi_CreateU16Vector4Array GamutMathU16Vector4Array_Create;
        GamutMathApi_GetU16Vector4ValuePointer GamutMathU16Vector4_GetValuePointer;
        GamutMathApi_GetU16Vector4ValuePointer GamutMathU16Vector4Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathU16Vector4Array_GetLength;

        GamutMathApi_GetType GamutMathI32Vector4_GetType;
        GamutMathApi_GetType GamutMathI32Vector4Array_GetType;
        GamutMathApi_CreateI32Vector4 GamutMathI32Vector4_Create;
        GamutMathApi_CreateI32Vector4Array GamutMathI32Vector4Array_Create;
        GamutMathApi_GetI32Vector4ValuePointer GamutMathI32Vector4_GetValuePointer;
        GamutMathApi_GetI32Vector4ValuePointer GamutMathI32Vector4Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathI32Vector4Array_GetLength;

        GamutMathApi_GetType GamutMathU32Vector4_GetType;
        GamutMathApi_GetType GamutMathU32Vector4Array_GetType;
        GamutMathApi_CreateU32Vector4 GamutMathU32Vector4_Create;
        GamutMathApi_CreateU32Vector4Array GamutMathU32Vector4Array_Create;
        GamutMathApi_GetU32Vector4ValuePointer GamutMathU32Vector4_GetValuePointer;
        GamutMathApi_GetU32Vector4ValuePointer GamutMathU32Vector4Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathU32Vector4Array_GetLength;

        GamutMathApi_GetType GamutMathIVector4_GetType;
        GamutMathApi_GetType GamutMathIVector4Array_GetType;
        GamutMathApi_CreateIVector4 GamutMathIVector4_Create;
        GamutMathApi_CreateIVector4Array GamutMathIVector4Array_Create;
        GamutMathApi_GetIVector4ValuePointer GamutMathIVector4_GetValuePointer;
        GamutMathApi_GetIVector4ValuePointer GamutMathIVector4Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathIVector4Array_GetLength;

        GamutMathApi_GetType GamutMathUVector4_GetType;
        GamutMathApi_GetType GamutMathUVector4Array_GetType;
        GamutMathApi_CreateUVector4 GamutMathUVector4_Create;
        GamutMathApi_CreateUVector4Array GamutMathUVector4Array_Create;
        GamutMathApi_GetUVector4ValuePointer GamutMathUVector4_GetValuePointer;
        GamutMathApi_GetUVector4ValuePointer GamutMathUVector4Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathUVector4Array_GetLength;

        GamutMathApi_GetType GamutMathI64Vector4_GetType;
        GamutMathApi_GetType GamutMathI64Vector4Array_GetType;
        GamutMathApi_CreateI64Vector4 GamutMathI64Vector4_Create;
        GamutMathApi_CreateI64Vector4Array GamutMathI64Vector4Array_Create;
        GamutMathApi_GetI64Vector4ValuePointer GamutMathI64Vector4_GetValuePointer;
        GamutMathApi_GetI64Vector4ValuePointer GamutMathI64Vector4Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathI64Vector4Array_GetLength;

        GamutMathApi_GetType GamutMathU64Vector4_GetType;
        GamutMathApi_GetType GamutMathU64Vector4Array_GetType;
        GamutMathApi_CreateU64Vector4 GamutMathU64Vector4_Create;
        GamutMathApi_CreateU64Vector4Array GamutMathU64Vector4Array_Create;
        GamutMathApi_GetU64Vector4ValuePointer GamutMathU64Vector4_GetValuePointer;
        GamutMathApi_GetU64Vector4ValuePointer GamutMathU64Vector4Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathU64Vector4Array_GetLength;


        GamutMathApi_GetType GamutMathDMatrix2x2_GetType;
        GamutMathApi_GetType GamutMathDMatrix2x2Array_GetType;
        GamutMathApi_CreateDMatrix2x2 GamutMathDMatrix2x2_Create;
        GamutMathApi_CreateDMatrix2x2Array GamutMathDMatrix2x2Array_Create;
        GamutMathApi_GetDMatrix2x2ValuePointer GamutMathDMatrix2x2_GetValuePointer;
        GamutMathApi_GetDMatrix2x2ValuePointer GamutMathDMatrix2x2Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathDMatrix2x2Array_GetLength;

        GamutMathApi_GetType GamutMathFMatrix2x2_GetType;
        GamutMathApi_GetType GamutMathFMatrix2x2Array_GetType;
        GamutMathApi_CreateFMatrix2x2 GamutMathFMatrix2x2_Create;
        GamutMathApi_CreateFMatrix2x2Array GamutMathFMatrix2x2Array_Create;
        GamutMathApi_GetFMatrix2x2ValuePointer GamutMathFMatrix2x2_GetValuePointer;
        GamutMathApi_GetFMatrix2x2ValuePointer GamutMathFMatrix2x2Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathFMatrix2x2Array_GetLength;

        GamutMathApi_GetType GamutMathDMatrix2x3_GetType;
        GamutMathApi_GetType GamutMathDMatrix2x3Array_GetType;
        GamutMathApi_CreateDMatrix2x3 GamutMathDMatrix2x3_Create;
        GamutMathApi_CreateDMatrix2x3Array GamutMathDMatrix2x3Array_Create;
        GamutMathApi_GetDMatrix2x3ValuePointer GamutMathDMatrix2x3_GetValuePointer;
        GamutMathApi_GetDMatrix2x3ValuePointer GamutMathDMatrix2x3Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathDMatrix2x3Array_GetLength;

        GamutMathApi_GetType GamutMathFMatrix2x3_GetType;
        GamutMathApi_GetType GamutMathFMatrix2x3Array_GetType;
        GamutMathApi_CreateFMatrix2x3 GamutMathFMatrix2x3_Create;
        GamutMathApi_CreateFMatrix2x3Array GamutMathFMatrix2x3Array_Create;
        GamutMathApi_GetFMatrix2x3ValuePointer GamutMathFMatrix2x3_GetValuePointer;
        GamutMathApi_GetFMatrix2x3ValuePointer GamutMathFMatrix2x3Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathFMatrix2x3Array_GetLength;

        GamutMathApi_GetType GamutMathDMatrix2x4_GetType;
        GamutMathApi_GetType GamutMathDMatrix2x4Array_GetType;
        GamutMathApi_CreateDMatrix2x4 GamutMathDMatrix2x4_Create;
        GamutMathApi_CreateDMatrix2x4Array GamutMathDMatrix2x4Array_Create;
        GamutMathApi_GetDMatrix2x4ValuePointer GamutMathDMatrix2x4_GetValuePointer;
        GamutMathApi_GetDMatrix2x4ValuePointer GamutMathDMatrix2x4Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathDMatrix2x4Array_GetLength;

        GamutMathApi_GetType GamutMathFMatrix2x4_GetType;
        GamutMathApi_GetType GamutMathFMatrix2x4Array_GetType;
        GamutMathApi_CreateFMatrix2x4 GamutMathFMatrix2x4_Create;
        GamutMathApi_CreateFMatrix2x4Array GamutMathFMatrix2x4Array_Create;
        GamutMathApi_GetFMatrix2x4ValuePointer GamutMathFMatrix2x4_GetValuePointer;
        GamutMathApi_GetFMatrix2x4ValuePointer GamutMathFMatrix2x4Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathFMatrix2x4Array_GetLength;

        GamutMathApi_GetType GamutMathDMatrix3x2_GetType;
        GamutMathApi_GetType GamutMathDMatrix3x2Array_GetType;
        GamutMathApi_CreateDMatrix3x2 GamutMathDMatrix3x2_Create;
        GamutMathApi_CreateDMatrix3x2Array GamutMathDMatrix3x2Array_Create;
        GamutMathApi_GetDMatrix3x2ValuePointer GamutMathDMatrix3x2_GetValuePointer;
        GamutMathApi_GetDMatrix3x2ValuePointer GamutMathDMatrix3x2Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathDMatrix3x2Array_GetLength;

        GamutMathApi_GetType GamutMathFMatrix3x2_GetType;
        GamutMathApi_GetType GamutMathFMatrix3x2Array_GetType;
        GamutMathApi_CreateFMatrix3x2 GamutMathFMatrix3x2_Create;
        GamutMathApi_CreateFMatrix3x2Array GamutMathFMatrix3x2Array_Create;
        GamutMathApi_GetFMatrix3x2ValuePointer GamutMathFMatrix3x2_GetValuePointer;
        GamutMathApi_GetFMatrix3x2ValuePointer GamutMathFMatrix3x2Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathFMatrix3x2Array_GetLength;

        GamutMathApi_GetType GamutMathDMatrix3x3_GetType;
        GamutMathApi_GetType GamutMathDMatrix3x3Array_GetType;
        GamutMathApi_CreateDMatrix3x3 GamutMathDMatrix3x3_Create;
        GamutMathApi_CreateDMatrix3x3Array GamutMathDMatrix3x3Array_Create;
        GamutMathApi_GetDMatrix3x3ValuePointer GamutMathDMatrix3x3_GetValuePointer;
        GamutMathApi_GetDMatrix3x3ValuePointer GamutMathDMatrix3x3Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathDMatrix3x3Array_GetLength;

        GamutMathApi_GetType GamutMathFMatrix3x3_GetType;
        GamutMathApi_GetType GamutMathFMatrix3x3Array_GetType;
        GamutMathApi_CreateFMatrix3x3 GamutMathFMatrix3x3_Create;
        GamutMathApi_CreateFMatrix3x3Array GamutMathFMatrix3x3Array_Create;
        GamutMathApi_GetFMatrix3x3ValuePointer GamutMathFMatrix3x3_GetValuePointer;
        GamutMathApi_GetFMatrix3x3ValuePointer GamutMathFMatrix3x3Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathFMatrix3x3Array_GetLength;

        GamutMathApi_GetType GamutMathDMatrix3x4_GetType;
        GamutMathApi_GetType GamutMathDMatrix3x4Array_GetType;
        GamutMathApi_CreateDMatrix3x4 GamutMathDMatrix3x4_Create;
        GamutMathApi_CreateDMatrix3x4Array GamutMathDMatrix3x4Array_Create;
        GamutMathApi_GetDMatrix3x4ValuePointer GamutMathDMatrix3x4_GetValuePointer;
        GamutMathApi_GetDMatrix3x4ValuePointer GamutMathDMatrix3x4Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathDMatrix3x4Array_GetLength;

        GamutMathApi_GetType GamutMathFMatrix3x4_GetType;
        GamutMathApi_GetType GamutMathFMatrix3x4Array_GetType;
        GamutMathApi_CreateFMatrix3x4 GamutMathFMatrix3x4_Create;
        GamutMathApi_CreateFMatrix3x4Array GamutMathFMatrix3x4Array_Create;
        GamutMathApi_GetFMatrix3x4ValuePointer GamutMathFMatrix3x4_GetValuePointer;
        GamutMathApi_GetFMatrix3x4ValuePointer GamutMathFMatrix3x4Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathFMatrix3x4Array_GetLength;

        GamutMathApi_GetType GamutMathDMatrix4x2_GetType;
        GamutMathApi_GetType GamutMathDMatrix4x2Array_GetType;
        GamutMathApi_CreateDMatrix4x2 GamutMathDMatrix4x2_Create;
        GamutMathApi_CreateDMatrix4x2Array GamutMathDMatrix4x2Array_Create;
        GamutMathApi_GetDMatrix4x2ValuePointer GamutMathDMatrix4x2_GetValuePointer;
        GamutMathApi_GetDMatrix4x2ValuePointer GamutMathDMatrix4x2Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathDMatrix4x2Array_GetLength;

        GamutMathApi_GetType GamutMathFMatrix4x2_GetType;
        GamutMathApi_GetType GamutMathFMatrix4x2Array_GetType;
        GamutMathApi_CreateFMatrix4x2 GamutMathFMatrix4x2_Create;
        GamutMathApi_CreateFMatrix4x2Array GamutMathFMatrix4x2Array_Create;
        GamutMathApi_GetFMatrix4x2ValuePointer GamutMathFMatrix4x2_GetValuePointer;
        GamutMathApi_GetFMatrix4x2ValuePointer GamutMathFMatrix4x2Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathFMatrix4x2Array_GetLength;

        GamutMathApi_GetType GamutMathDMatrix4x3_GetType;
        GamutMathApi_GetType GamutMathDMatrix4x3Array_GetType;
        GamutMathApi_CreateDMatrix4x3 GamutMathDMatrix4x3_Create;
        GamutMathApi_CreateDMatrix4x3Array GamutMathDMatrix4x3Array_Create;
        GamutMathApi_GetDMatrix4x3ValuePointer GamutMathDMatrix4x3_GetValuePointer;
        GamutMathApi_GetDMatrix4x3ValuePointer GamutMathDMatrix4x3Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathDMatrix4x3Array_GetLength;

        GamutMathApi_GetType GamutMathFMatrix4x3_GetType;
        GamutMathApi_GetType GamutMathFMatrix4x3Array_GetType;
        GamutMathApi_CreateFMatrix4x3 GamutMathFMatrix4x3_Create;
        GamutMathApi_CreateFMatrix4x3Array GamutMathFMatrix4x3Array_Create;
        GamutMathApi_GetFMatrix4x3ValuePointer GamutMathFMatrix4x3_GetValuePointer;
        GamutMathApi_GetFMatrix4x3ValuePointer GamutMathFMatrix4x3Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathFMatrix4x3Array_GetLength;

        GamutMathApi_GetType GamutMathDMatrix4x4_GetType;
        GamutMathApi_GetType GamutMathDMatrix4x4Array_GetType;
        GamutMathApi_CreateDMatrix4x4 GamutMathDMatrix4x4_Create;
        GamutMathApi_CreateDMatrix4x4Array GamutMathDMatrix4x4Array_Create;
        GamutMathApi_GetDMatrix4x4ValuePointer GamutMathDMatrix4x4_GetValuePointer;
        GamutMathApi_GetDMatrix4x4ValuePointer GamutMathDMatrix4x4Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathDMatrix4x4Array_GetLength;

        GamutMathApi_GetType GamutMathFMatrix4x4_GetType;
        GamutMathApi_GetType GamutMathFMatrix4x4Array_GetType;
        GamutMathApi_CreateFMatrix4x4 GamutMathFMatrix4x4_Create;
        GamutMathApi_CreateFMatrix4x4Array GamutMathFMatrix4x4Array_Create;
        GamutMathApi_GetFMatrix4x4ValuePointer GamutMathFMatrix4x4_GetValuePointer;
        GamutMathApi_GetFMatrix4x4ValuePointer GamutMathFMatrix4x4Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathFMatrix4x4Array_GetLength;


        GamutMathApi_GetType GamutMathDQuaternion_GetType;
        GamutMathApi_GetType GamutMathDQuaternionArray_GetType;
        GamutMathApi_CreateDQuaternion GamutMathDQuaternion_Create;
        GamutMathApi_CreateDQuaternionArray GamutMathDQuaternionArray_Create;
        GamutMathApi_GetDQuaternionValuePointer GamutMathDQuaternion_GetValuePointer;
        GamutMathApi_GetDQuaternionValuePointer GamutMathDQuaternionArray_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathDQuaternionArray_GetLength;

        GamutMathApi_GetType GamutMathFQuaternion_GetType;
        GamutMathApi_GetType GamutMathFQuaternionArray_GetType;
        GamutMathApi_CreateFQuaternion GamutMathFQuaternion_Create;
        GamutMathApi_CreateFQuaternionArray GamutMathFQuaternionArray_Create;
        GamutMathApi_GetFQuaternionValuePointer GamutMathFQuaternion_GetValuePointer;
        GamutMathApi_GetFQuaternionValuePointer GamutMathFQuaternionArray_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathFQuaternionArray_GetLength;


        GamutMathApi_GetType GamutMathBArray_GetType;
        GamutMathApi_CreateBArray GamutMathBArray_Create;
        GamutMathApi_GetBValuePointer GamutMathBArray_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathBArray_GetLength;

        GamutMathApi_GetType GamutMathDArray_GetType;
        GamutMathApi_CreateDArray GamutMathDArray_Create;
        GamutMathApi_GetDValuePointer GamutMathDArray_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathDArray_GetLength;

        GamutMathApi_GetType GamutMathFArray_GetType;
        GamutMathApi_CreateFArray GamutMathFArray_Create;
        GamutMathApi_GetFValuePointer GamutMathFArray_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathFArray_GetLength;

        GamutMathApi_GetType GamutMathI8Array_GetType;
        GamutMathApi_CreateI8Array GamutMathI8Array_Create;
        GamutMathApi_GetI8ValuePointer GamutMathI8Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathI8Array_GetLength;

        GamutMathApi_GetType GamutMathU8Array_GetType;
        GamutMathApi_CreateU8Array GamutMathU8Array_Create;
        GamutMathApi_GetU8ValuePointer GamutMathU8Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathU8Array_GetLength;

        GamutMathApi_GetType GamutMathI16Array_GetType;
        GamutMathApi_CreateI16Array GamutMathI16Array_Create;
        GamutMathApi_GetI16ValuePointer GamutMathI16Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathI16Array_GetLength;

        GamutMathApi_GetType GamutMathU16Array_GetType;
        GamutMathApi_CreateU16Array GamutMathU16Array_Create;
        GamutMathApi_GetU16ValuePointer GamutMathU16Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathU16Array_GetLength;

        GamutMathApi_GetType GamutMathI32Array_GetType;
        GamutMathApi_CreateI32Array GamutMathI32Array_Create;
        GamutMathApi_GetI32ValuePointer GamutMathI32Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathI32Array_GetLength;

        GamutMathApi_GetType GamutMathU32Array_GetType;
        GamutMathApi_CreateU32Array GamutMathU32Array_Create;
        GamutMathApi_GetU32ValuePointer GamutMathU32Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathU32Array_GetLength;

        GamutMathApi_GetType GamutMathIArray_GetType;
        GamutMathApi_CreateIArray GamutMathIArray_Create;
        GamutMathApi_GetIValuePointer GamutMathIArray_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathIArray_GetLength;

        GamutMathApi_GetType GamutMathUArray_GetType;
        GamutMathApi_CreateUArray GamutMathUArray_Create;
        GamutMathApi_GetUValuePointer GamutMathUArray_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathUArray_GetLength;

        GamutMathApi_GetType GamutMathI64Array_GetType;
        GamutMathApi_CreateI64Array GamutMathI64Array_Create;
        GamutMathApi_GetI64ValuePointer GamutMathI64Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathI64Array_GetLength;

        GamutMathApi_GetType GamutMathU64Array_GetType;
        GamutMathApi_CreateU64Array GamutMathU64Array_Create;
        GamutMathApi_GetU64ValuePointer GamutMathU64Array_GetValuePointer;
        GamutMathApi_GetArrayLength GamutMathU64Array_GetLength;

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