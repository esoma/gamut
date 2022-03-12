
// generated 2022-03-12 02:15:25.112788 from codegen/math/templates/test_api.cpp

// python
#define PY_SSIZE_T_CLEAN
#include <Python.h>
// gamut
#include "gamut/math.h"

#define TEST(X) if (!(X)){ PyErr_Format(PyExc_AssertionError, #X " (line %i)", __LINE__); return 0; };


static PyObject *
test_GamutMathApi_Get(PyObject *self, PyObject *args)
{
    struct GamutMathApi *api = GamutMathApi_Get();
    if (!api){ return 0; }
    TEST(!PyErr_Occurred());


            TEST(api->GamutMathBVector2_GetType != 0);
            TEST(api->GamutMathBVector2_Create != 0);
            TEST(api->GamutMathBVector2_GetValuePointer != 0);

        TEST(api->GamutMathBVector2Array_Create != 0);
        TEST(api->GamutMathBVector2Array_GetType != 0);
        TEST(api->GamutMathBVector2Array_GetValuePointer != 0);
        TEST(api->GamutMathBVector2Array_GetLength != 0);


            TEST(api->GamutMathDVector2_GetType != 0);
            TEST(api->GamutMathDVector2_Create != 0);
            TEST(api->GamutMathDVector2_GetValuePointer != 0);

        TEST(api->GamutMathDVector2Array_Create != 0);
        TEST(api->GamutMathDVector2Array_GetType != 0);
        TEST(api->GamutMathDVector2Array_GetValuePointer != 0);
        TEST(api->GamutMathDVector2Array_GetLength != 0);


            TEST(api->GamutMathFVector2_GetType != 0);
            TEST(api->GamutMathFVector2_Create != 0);
            TEST(api->GamutMathFVector2_GetValuePointer != 0);

        TEST(api->GamutMathFVector2Array_Create != 0);
        TEST(api->GamutMathFVector2Array_GetType != 0);
        TEST(api->GamutMathFVector2Array_GetValuePointer != 0);
        TEST(api->GamutMathFVector2Array_GetLength != 0);


            TEST(api->GamutMathI8Vector2_GetType != 0);
            TEST(api->GamutMathI8Vector2_Create != 0);
            TEST(api->GamutMathI8Vector2_GetValuePointer != 0);

        TEST(api->GamutMathI8Vector2Array_Create != 0);
        TEST(api->GamutMathI8Vector2Array_GetType != 0);
        TEST(api->GamutMathI8Vector2Array_GetValuePointer != 0);
        TEST(api->GamutMathI8Vector2Array_GetLength != 0);


            TEST(api->GamutMathU8Vector2_GetType != 0);
            TEST(api->GamutMathU8Vector2_Create != 0);
            TEST(api->GamutMathU8Vector2_GetValuePointer != 0);

        TEST(api->GamutMathU8Vector2Array_Create != 0);
        TEST(api->GamutMathU8Vector2Array_GetType != 0);
        TEST(api->GamutMathU8Vector2Array_GetValuePointer != 0);
        TEST(api->GamutMathU8Vector2Array_GetLength != 0);


            TEST(api->GamutMathI16Vector2_GetType != 0);
            TEST(api->GamutMathI16Vector2_Create != 0);
            TEST(api->GamutMathI16Vector2_GetValuePointer != 0);

        TEST(api->GamutMathI16Vector2Array_Create != 0);
        TEST(api->GamutMathI16Vector2Array_GetType != 0);
        TEST(api->GamutMathI16Vector2Array_GetValuePointer != 0);
        TEST(api->GamutMathI16Vector2Array_GetLength != 0);


            TEST(api->GamutMathU16Vector2_GetType != 0);
            TEST(api->GamutMathU16Vector2_Create != 0);
            TEST(api->GamutMathU16Vector2_GetValuePointer != 0);

        TEST(api->GamutMathU16Vector2Array_Create != 0);
        TEST(api->GamutMathU16Vector2Array_GetType != 0);
        TEST(api->GamutMathU16Vector2Array_GetValuePointer != 0);
        TEST(api->GamutMathU16Vector2Array_GetLength != 0);


            TEST(api->GamutMathI32Vector2_GetType != 0);
            TEST(api->GamutMathI32Vector2_Create != 0);
            TEST(api->GamutMathI32Vector2_GetValuePointer != 0);

        TEST(api->GamutMathI32Vector2Array_Create != 0);
        TEST(api->GamutMathI32Vector2Array_GetType != 0);
        TEST(api->GamutMathI32Vector2Array_GetValuePointer != 0);
        TEST(api->GamutMathI32Vector2Array_GetLength != 0);


            TEST(api->GamutMathU32Vector2_GetType != 0);
            TEST(api->GamutMathU32Vector2_Create != 0);
            TEST(api->GamutMathU32Vector2_GetValuePointer != 0);

        TEST(api->GamutMathU32Vector2Array_Create != 0);
        TEST(api->GamutMathU32Vector2Array_GetType != 0);
        TEST(api->GamutMathU32Vector2Array_GetValuePointer != 0);
        TEST(api->GamutMathU32Vector2Array_GetLength != 0);


            TEST(api->GamutMathIVector2_GetType != 0);
            TEST(api->GamutMathIVector2_Create != 0);
            TEST(api->GamutMathIVector2_GetValuePointer != 0);

        TEST(api->GamutMathIVector2Array_Create != 0);
        TEST(api->GamutMathIVector2Array_GetType != 0);
        TEST(api->GamutMathIVector2Array_GetValuePointer != 0);
        TEST(api->GamutMathIVector2Array_GetLength != 0);


            TEST(api->GamutMathUVector2_GetType != 0);
            TEST(api->GamutMathUVector2_Create != 0);
            TEST(api->GamutMathUVector2_GetValuePointer != 0);

        TEST(api->GamutMathUVector2Array_Create != 0);
        TEST(api->GamutMathUVector2Array_GetType != 0);
        TEST(api->GamutMathUVector2Array_GetValuePointer != 0);
        TEST(api->GamutMathUVector2Array_GetLength != 0);


            TEST(api->GamutMathI64Vector2_GetType != 0);
            TEST(api->GamutMathI64Vector2_Create != 0);
            TEST(api->GamutMathI64Vector2_GetValuePointer != 0);

        TEST(api->GamutMathI64Vector2Array_Create != 0);
        TEST(api->GamutMathI64Vector2Array_GetType != 0);
        TEST(api->GamutMathI64Vector2Array_GetValuePointer != 0);
        TEST(api->GamutMathI64Vector2Array_GetLength != 0);


            TEST(api->GamutMathU64Vector2_GetType != 0);
            TEST(api->GamutMathU64Vector2_Create != 0);
            TEST(api->GamutMathU64Vector2_GetValuePointer != 0);

        TEST(api->GamutMathU64Vector2Array_Create != 0);
        TEST(api->GamutMathU64Vector2Array_GetType != 0);
        TEST(api->GamutMathU64Vector2Array_GetValuePointer != 0);
        TEST(api->GamutMathU64Vector2Array_GetLength != 0);


            TEST(api->GamutMathBVector3_GetType != 0);
            TEST(api->GamutMathBVector3_Create != 0);
            TEST(api->GamutMathBVector3_GetValuePointer != 0);

        TEST(api->GamutMathBVector3Array_Create != 0);
        TEST(api->GamutMathBVector3Array_GetType != 0);
        TEST(api->GamutMathBVector3Array_GetValuePointer != 0);
        TEST(api->GamutMathBVector3Array_GetLength != 0);


            TEST(api->GamutMathDVector3_GetType != 0);
            TEST(api->GamutMathDVector3_Create != 0);
            TEST(api->GamutMathDVector3_GetValuePointer != 0);

        TEST(api->GamutMathDVector3Array_Create != 0);
        TEST(api->GamutMathDVector3Array_GetType != 0);
        TEST(api->GamutMathDVector3Array_GetValuePointer != 0);
        TEST(api->GamutMathDVector3Array_GetLength != 0);


            TEST(api->GamutMathFVector3_GetType != 0);
            TEST(api->GamutMathFVector3_Create != 0);
            TEST(api->GamutMathFVector3_GetValuePointer != 0);

        TEST(api->GamutMathFVector3Array_Create != 0);
        TEST(api->GamutMathFVector3Array_GetType != 0);
        TEST(api->GamutMathFVector3Array_GetValuePointer != 0);
        TEST(api->GamutMathFVector3Array_GetLength != 0);


            TEST(api->GamutMathI8Vector3_GetType != 0);
            TEST(api->GamutMathI8Vector3_Create != 0);
            TEST(api->GamutMathI8Vector3_GetValuePointer != 0);

        TEST(api->GamutMathI8Vector3Array_Create != 0);
        TEST(api->GamutMathI8Vector3Array_GetType != 0);
        TEST(api->GamutMathI8Vector3Array_GetValuePointer != 0);
        TEST(api->GamutMathI8Vector3Array_GetLength != 0);


            TEST(api->GamutMathU8Vector3_GetType != 0);
            TEST(api->GamutMathU8Vector3_Create != 0);
            TEST(api->GamutMathU8Vector3_GetValuePointer != 0);

        TEST(api->GamutMathU8Vector3Array_Create != 0);
        TEST(api->GamutMathU8Vector3Array_GetType != 0);
        TEST(api->GamutMathU8Vector3Array_GetValuePointer != 0);
        TEST(api->GamutMathU8Vector3Array_GetLength != 0);


            TEST(api->GamutMathI16Vector3_GetType != 0);
            TEST(api->GamutMathI16Vector3_Create != 0);
            TEST(api->GamutMathI16Vector3_GetValuePointer != 0);

        TEST(api->GamutMathI16Vector3Array_Create != 0);
        TEST(api->GamutMathI16Vector3Array_GetType != 0);
        TEST(api->GamutMathI16Vector3Array_GetValuePointer != 0);
        TEST(api->GamutMathI16Vector3Array_GetLength != 0);


            TEST(api->GamutMathU16Vector3_GetType != 0);
            TEST(api->GamutMathU16Vector3_Create != 0);
            TEST(api->GamutMathU16Vector3_GetValuePointer != 0);

        TEST(api->GamutMathU16Vector3Array_Create != 0);
        TEST(api->GamutMathU16Vector3Array_GetType != 0);
        TEST(api->GamutMathU16Vector3Array_GetValuePointer != 0);
        TEST(api->GamutMathU16Vector3Array_GetLength != 0);


            TEST(api->GamutMathI32Vector3_GetType != 0);
            TEST(api->GamutMathI32Vector3_Create != 0);
            TEST(api->GamutMathI32Vector3_GetValuePointer != 0);

        TEST(api->GamutMathI32Vector3Array_Create != 0);
        TEST(api->GamutMathI32Vector3Array_GetType != 0);
        TEST(api->GamutMathI32Vector3Array_GetValuePointer != 0);
        TEST(api->GamutMathI32Vector3Array_GetLength != 0);


            TEST(api->GamutMathU32Vector3_GetType != 0);
            TEST(api->GamutMathU32Vector3_Create != 0);
            TEST(api->GamutMathU32Vector3_GetValuePointer != 0);

        TEST(api->GamutMathU32Vector3Array_Create != 0);
        TEST(api->GamutMathU32Vector3Array_GetType != 0);
        TEST(api->GamutMathU32Vector3Array_GetValuePointer != 0);
        TEST(api->GamutMathU32Vector3Array_GetLength != 0);


            TEST(api->GamutMathIVector3_GetType != 0);
            TEST(api->GamutMathIVector3_Create != 0);
            TEST(api->GamutMathIVector3_GetValuePointer != 0);

        TEST(api->GamutMathIVector3Array_Create != 0);
        TEST(api->GamutMathIVector3Array_GetType != 0);
        TEST(api->GamutMathIVector3Array_GetValuePointer != 0);
        TEST(api->GamutMathIVector3Array_GetLength != 0);


            TEST(api->GamutMathUVector3_GetType != 0);
            TEST(api->GamutMathUVector3_Create != 0);
            TEST(api->GamutMathUVector3_GetValuePointer != 0);

        TEST(api->GamutMathUVector3Array_Create != 0);
        TEST(api->GamutMathUVector3Array_GetType != 0);
        TEST(api->GamutMathUVector3Array_GetValuePointer != 0);
        TEST(api->GamutMathUVector3Array_GetLength != 0);


            TEST(api->GamutMathI64Vector3_GetType != 0);
            TEST(api->GamutMathI64Vector3_Create != 0);
            TEST(api->GamutMathI64Vector3_GetValuePointer != 0);

        TEST(api->GamutMathI64Vector3Array_Create != 0);
        TEST(api->GamutMathI64Vector3Array_GetType != 0);
        TEST(api->GamutMathI64Vector3Array_GetValuePointer != 0);
        TEST(api->GamutMathI64Vector3Array_GetLength != 0);


            TEST(api->GamutMathU64Vector3_GetType != 0);
            TEST(api->GamutMathU64Vector3_Create != 0);
            TEST(api->GamutMathU64Vector3_GetValuePointer != 0);

        TEST(api->GamutMathU64Vector3Array_Create != 0);
        TEST(api->GamutMathU64Vector3Array_GetType != 0);
        TEST(api->GamutMathU64Vector3Array_GetValuePointer != 0);
        TEST(api->GamutMathU64Vector3Array_GetLength != 0);


            TEST(api->GamutMathBVector4_GetType != 0);
            TEST(api->GamutMathBVector4_Create != 0);
            TEST(api->GamutMathBVector4_GetValuePointer != 0);

        TEST(api->GamutMathBVector4Array_Create != 0);
        TEST(api->GamutMathBVector4Array_GetType != 0);
        TEST(api->GamutMathBVector4Array_GetValuePointer != 0);
        TEST(api->GamutMathBVector4Array_GetLength != 0);


            TEST(api->GamutMathDVector4_GetType != 0);
            TEST(api->GamutMathDVector4_Create != 0);
            TEST(api->GamutMathDVector4_GetValuePointer != 0);

        TEST(api->GamutMathDVector4Array_Create != 0);
        TEST(api->GamutMathDVector4Array_GetType != 0);
        TEST(api->GamutMathDVector4Array_GetValuePointer != 0);
        TEST(api->GamutMathDVector4Array_GetLength != 0);


            TEST(api->GamutMathFVector4_GetType != 0);
            TEST(api->GamutMathFVector4_Create != 0);
            TEST(api->GamutMathFVector4_GetValuePointer != 0);

        TEST(api->GamutMathFVector4Array_Create != 0);
        TEST(api->GamutMathFVector4Array_GetType != 0);
        TEST(api->GamutMathFVector4Array_GetValuePointer != 0);
        TEST(api->GamutMathFVector4Array_GetLength != 0);


            TEST(api->GamutMathI8Vector4_GetType != 0);
            TEST(api->GamutMathI8Vector4_Create != 0);
            TEST(api->GamutMathI8Vector4_GetValuePointer != 0);

        TEST(api->GamutMathI8Vector4Array_Create != 0);
        TEST(api->GamutMathI8Vector4Array_GetType != 0);
        TEST(api->GamutMathI8Vector4Array_GetValuePointer != 0);
        TEST(api->GamutMathI8Vector4Array_GetLength != 0);


            TEST(api->GamutMathU8Vector4_GetType != 0);
            TEST(api->GamutMathU8Vector4_Create != 0);
            TEST(api->GamutMathU8Vector4_GetValuePointer != 0);

        TEST(api->GamutMathU8Vector4Array_Create != 0);
        TEST(api->GamutMathU8Vector4Array_GetType != 0);
        TEST(api->GamutMathU8Vector4Array_GetValuePointer != 0);
        TEST(api->GamutMathU8Vector4Array_GetLength != 0);


            TEST(api->GamutMathI16Vector4_GetType != 0);
            TEST(api->GamutMathI16Vector4_Create != 0);
            TEST(api->GamutMathI16Vector4_GetValuePointer != 0);

        TEST(api->GamutMathI16Vector4Array_Create != 0);
        TEST(api->GamutMathI16Vector4Array_GetType != 0);
        TEST(api->GamutMathI16Vector4Array_GetValuePointer != 0);
        TEST(api->GamutMathI16Vector4Array_GetLength != 0);


            TEST(api->GamutMathU16Vector4_GetType != 0);
            TEST(api->GamutMathU16Vector4_Create != 0);
            TEST(api->GamutMathU16Vector4_GetValuePointer != 0);

        TEST(api->GamutMathU16Vector4Array_Create != 0);
        TEST(api->GamutMathU16Vector4Array_GetType != 0);
        TEST(api->GamutMathU16Vector4Array_GetValuePointer != 0);
        TEST(api->GamutMathU16Vector4Array_GetLength != 0);


            TEST(api->GamutMathI32Vector4_GetType != 0);
            TEST(api->GamutMathI32Vector4_Create != 0);
            TEST(api->GamutMathI32Vector4_GetValuePointer != 0);

        TEST(api->GamutMathI32Vector4Array_Create != 0);
        TEST(api->GamutMathI32Vector4Array_GetType != 0);
        TEST(api->GamutMathI32Vector4Array_GetValuePointer != 0);
        TEST(api->GamutMathI32Vector4Array_GetLength != 0);


            TEST(api->GamutMathU32Vector4_GetType != 0);
            TEST(api->GamutMathU32Vector4_Create != 0);
            TEST(api->GamutMathU32Vector4_GetValuePointer != 0);

        TEST(api->GamutMathU32Vector4Array_Create != 0);
        TEST(api->GamutMathU32Vector4Array_GetType != 0);
        TEST(api->GamutMathU32Vector4Array_GetValuePointer != 0);
        TEST(api->GamutMathU32Vector4Array_GetLength != 0);


            TEST(api->GamutMathIVector4_GetType != 0);
            TEST(api->GamutMathIVector4_Create != 0);
            TEST(api->GamutMathIVector4_GetValuePointer != 0);

        TEST(api->GamutMathIVector4Array_Create != 0);
        TEST(api->GamutMathIVector4Array_GetType != 0);
        TEST(api->GamutMathIVector4Array_GetValuePointer != 0);
        TEST(api->GamutMathIVector4Array_GetLength != 0);


            TEST(api->GamutMathUVector4_GetType != 0);
            TEST(api->GamutMathUVector4_Create != 0);
            TEST(api->GamutMathUVector4_GetValuePointer != 0);

        TEST(api->GamutMathUVector4Array_Create != 0);
        TEST(api->GamutMathUVector4Array_GetType != 0);
        TEST(api->GamutMathUVector4Array_GetValuePointer != 0);
        TEST(api->GamutMathUVector4Array_GetLength != 0);


            TEST(api->GamutMathI64Vector4_GetType != 0);
            TEST(api->GamutMathI64Vector4_Create != 0);
            TEST(api->GamutMathI64Vector4_GetValuePointer != 0);

        TEST(api->GamutMathI64Vector4Array_Create != 0);
        TEST(api->GamutMathI64Vector4Array_GetType != 0);
        TEST(api->GamutMathI64Vector4Array_GetValuePointer != 0);
        TEST(api->GamutMathI64Vector4Array_GetLength != 0);


            TEST(api->GamutMathU64Vector4_GetType != 0);
            TEST(api->GamutMathU64Vector4_Create != 0);
            TEST(api->GamutMathU64Vector4_GetValuePointer != 0);

        TEST(api->GamutMathU64Vector4Array_Create != 0);
        TEST(api->GamutMathU64Vector4Array_GetType != 0);
        TEST(api->GamutMathU64Vector4Array_GetValuePointer != 0);
        TEST(api->GamutMathU64Vector4Array_GetLength != 0);


            TEST(api->GamutMathDMatrix2x2_GetType != 0);
            TEST(api->GamutMathDMatrix2x2_Create != 0);
            TEST(api->GamutMathDMatrix2x2_GetValuePointer != 0);

        TEST(api->GamutMathDMatrix2x2Array_Create != 0);
        TEST(api->GamutMathDMatrix2x2Array_GetType != 0);
        TEST(api->GamutMathDMatrix2x2Array_GetValuePointer != 0);
        TEST(api->GamutMathDMatrix2x2Array_GetLength != 0);


            TEST(api->GamutMathFMatrix2x2_GetType != 0);
            TEST(api->GamutMathFMatrix2x2_Create != 0);
            TEST(api->GamutMathFMatrix2x2_GetValuePointer != 0);

        TEST(api->GamutMathFMatrix2x2Array_Create != 0);
        TEST(api->GamutMathFMatrix2x2Array_GetType != 0);
        TEST(api->GamutMathFMatrix2x2Array_GetValuePointer != 0);
        TEST(api->GamutMathFMatrix2x2Array_GetLength != 0);


            TEST(api->GamutMathDMatrix2x3_GetType != 0);
            TEST(api->GamutMathDMatrix2x3_Create != 0);
            TEST(api->GamutMathDMatrix2x3_GetValuePointer != 0);

        TEST(api->GamutMathDMatrix2x3Array_Create != 0);
        TEST(api->GamutMathDMatrix2x3Array_GetType != 0);
        TEST(api->GamutMathDMatrix2x3Array_GetValuePointer != 0);
        TEST(api->GamutMathDMatrix2x3Array_GetLength != 0);


            TEST(api->GamutMathFMatrix2x3_GetType != 0);
            TEST(api->GamutMathFMatrix2x3_Create != 0);
            TEST(api->GamutMathFMatrix2x3_GetValuePointer != 0);

        TEST(api->GamutMathFMatrix2x3Array_Create != 0);
        TEST(api->GamutMathFMatrix2x3Array_GetType != 0);
        TEST(api->GamutMathFMatrix2x3Array_GetValuePointer != 0);
        TEST(api->GamutMathFMatrix2x3Array_GetLength != 0);


            TEST(api->GamutMathDMatrix2x4_GetType != 0);
            TEST(api->GamutMathDMatrix2x4_Create != 0);
            TEST(api->GamutMathDMatrix2x4_GetValuePointer != 0);

        TEST(api->GamutMathDMatrix2x4Array_Create != 0);
        TEST(api->GamutMathDMatrix2x4Array_GetType != 0);
        TEST(api->GamutMathDMatrix2x4Array_GetValuePointer != 0);
        TEST(api->GamutMathDMatrix2x4Array_GetLength != 0);


            TEST(api->GamutMathFMatrix2x4_GetType != 0);
            TEST(api->GamutMathFMatrix2x4_Create != 0);
            TEST(api->GamutMathFMatrix2x4_GetValuePointer != 0);

        TEST(api->GamutMathFMatrix2x4Array_Create != 0);
        TEST(api->GamutMathFMatrix2x4Array_GetType != 0);
        TEST(api->GamutMathFMatrix2x4Array_GetValuePointer != 0);
        TEST(api->GamutMathFMatrix2x4Array_GetLength != 0);


            TEST(api->GamutMathDMatrix3x2_GetType != 0);
            TEST(api->GamutMathDMatrix3x2_Create != 0);
            TEST(api->GamutMathDMatrix3x2_GetValuePointer != 0);

        TEST(api->GamutMathDMatrix3x2Array_Create != 0);
        TEST(api->GamutMathDMatrix3x2Array_GetType != 0);
        TEST(api->GamutMathDMatrix3x2Array_GetValuePointer != 0);
        TEST(api->GamutMathDMatrix3x2Array_GetLength != 0);


            TEST(api->GamutMathFMatrix3x2_GetType != 0);
            TEST(api->GamutMathFMatrix3x2_Create != 0);
            TEST(api->GamutMathFMatrix3x2_GetValuePointer != 0);

        TEST(api->GamutMathFMatrix3x2Array_Create != 0);
        TEST(api->GamutMathFMatrix3x2Array_GetType != 0);
        TEST(api->GamutMathFMatrix3x2Array_GetValuePointer != 0);
        TEST(api->GamutMathFMatrix3x2Array_GetLength != 0);


            TEST(api->GamutMathDMatrix3x3_GetType != 0);
            TEST(api->GamutMathDMatrix3x3_Create != 0);
            TEST(api->GamutMathDMatrix3x3_GetValuePointer != 0);

        TEST(api->GamutMathDMatrix3x3Array_Create != 0);
        TEST(api->GamutMathDMatrix3x3Array_GetType != 0);
        TEST(api->GamutMathDMatrix3x3Array_GetValuePointer != 0);
        TEST(api->GamutMathDMatrix3x3Array_GetLength != 0);


            TEST(api->GamutMathFMatrix3x3_GetType != 0);
            TEST(api->GamutMathFMatrix3x3_Create != 0);
            TEST(api->GamutMathFMatrix3x3_GetValuePointer != 0);

        TEST(api->GamutMathFMatrix3x3Array_Create != 0);
        TEST(api->GamutMathFMatrix3x3Array_GetType != 0);
        TEST(api->GamutMathFMatrix3x3Array_GetValuePointer != 0);
        TEST(api->GamutMathFMatrix3x3Array_GetLength != 0);


            TEST(api->GamutMathDMatrix3x4_GetType != 0);
            TEST(api->GamutMathDMatrix3x4_Create != 0);
            TEST(api->GamutMathDMatrix3x4_GetValuePointer != 0);

        TEST(api->GamutMathDMatrix3x4Array_Create != 0);
        TEST(api->GamutMathDMatrix3x4Array_GetType != 0);
        TEST(api->GamutMathDMatrix3x4Array_GetValuePointer != 0);
        TEST(api->GamutMathDMatrix3x4Array_GetLength != 0);


            TEST(api->GamutMathFMatrix3x4_GetType != 0);
            TEST(api->GamutMathFMatrix3x4_Create != 0);
            TEST(api->GamutMathFMatrix3x4_GetValuePointer != 0);

        TEST(api->GamutMathFMatrix3x4Array_Create != 0);
        TEST(api->GamutMathFMatrix3x4Array_GetType != 0);
        TEST(api->GamutMathFMatrix3x4Array_GetValuePointer != 0);
        TEST(api->GamutMathFMatrix3x4Array_GetLength != 0);


            TEST(api->GamutMathDMatrix4x2_GetType != 0);
            TEST(api->GamutMathDMatrix4x2_Create != 0);
            TEST(api->GamutMathDMatrix4x2_GetValuePointer != 0);

        TEST(api->GamutMathDMatrix4x2Array_Create != 0);
        TEST(api->GamutMathDMatrix4x2Array_GetType != 0);
        TEST(api->GamutMathDMatrix4x2Array_GetValuePointer != 0);
        TEST(api->GamutMathDMatrix4x2Array_GetLength != 0);


            TEST(api->GamutMathFMatrix4x2_GetType != 0);
            TEST(api->GamutMathFMatrix4x2_Create != 0);
            TEST(api->GamutMathFMatrix4x2_GetValuePointer != 0);

        TEST(api->GamutMathFMatrix4x2Array_Create != 0);
        TEST(api->GamutMathFMatrix4x2Array_GetType != 0);
        TEST(api->GamutMathFMatrix4x2Array_GetValuePointer != 0);
        TEST(api->GamutMathFMatrix4x2Array_GetLength != 0);


            TEST(api->GamutMathDMatrix4x3_GetType != 0);
            TEST(api->GamutMathDMatrix4x3_Create != 0);
            TEST(api->GamutMathDMatrix4x3_GetValuePointer != 0);

        TEST(api->GamutMathDMatrix4x3Array_Create != 0);
        TEST(api->GamutMathDMatrix4x3Array_GetType != 0);
        TEST(api->GamutMathDMatrix4x3Array_GetValuePointer != 0);
        TEST(api->GamutMathDMatrix4x3Array_GetLength != 0);


            TEST(api->GamutMathFMatrix4x3_GetType != 0);
            TEST(api->GamutMathFMatrix4x3_Create != 0);
            TEST(api->GamutMathFMatrix4x3_GetValuePointer != 0);

        TEST(api->GamutMathFMatrix4x3Array_Create != 0);
        TEST(api->GamutMathFMatrix4x3Array_GetType != 0);
        TEST(api->GamutMathFMatrix4x3Array_GetValuePointer != 0);
        TEST(api->GamutMathFMatrix4x3Array_GetLength != 0);


            TEST(api->GamutMathDMatrix4x4_GetType != 0);
            TEST(api->GamutMathDMatrix4x4_Create != 0);
            TEST(api->GamutMathDMatrix4x4_GetValuePointer != 0);

        TEST(api->GamutMathDMatrix4x4Array_Create != 0);
        TEST(api->GamutMathDMatrix4x4Array_GetType != 0);
        TEST(api->GamutMathDMatrix4x4Array_GetValuePointer != 0);
        TEST(api->GamutMathDMatrix4x4Array_GetLength != 0);


            TEST(api->GamutMathFMatrix4x4_GetType != 0);
            TEST(api->GamutMathFMatrix4x4_Create != 0);
            TEST(api->GamutMathFMatrix4x4_GetValuePointer != 0);

        TEST(api->GamutMathFMatrix4x4Array_Create != 0);
        TEST(api->GamutMathFMatrix4x4Array_GetType != 0);
        TEST(api->GamutMathFMatrix4x4Array_GetValuePointer != 0);
        TEST(api->GamutMathFMatrix4x4Array_GetLength != 0);


        TEST(api->GamutMathBArray_Create != 0);
        TEST(api->GamutMathBArray_GetType != 0);
        TEST(api->GamutMathBArray_GetValuePointer != 0);
        TEST(api->GamutMathBArray_GetLength != 0);


        TEST(api->GamutMathDArray_Create != 0);
        TEST(api->GamutMathDArray_GetType != 0);
        TEST(api->GamutMathDArray_GetValuePointer != 0);
        TEST(api->GamutMathDArray_GetLength != 0);


        TEST(api->GamutMathFArray_Create != 0);
        TEST(api->GamutMathFArray_GetType != 0);
        TEST(api->GamutMathFArray_GetValuePointer != 0);
        TEST(api->GamutMathFArray_GetLength != 0);


        TEST(api->GamutMathI8Array_Create != 0);
        TEST(api->GamutMathI8Array_GetType != 0);
        TEST(api->GamutMathI8Array_GetValuePointer != 0);
        TEST(api->GamutMathI8Array_GetLength != 0);


        TEST(api->GamutMathU8Array_Create != 0);
        TEST(api->GamutMathU8Array_GetType != 0);
        TEST(api->GamutMathU8Array_GetValuePointer != 0);
        TEST(api->GamutMathU8Array_GetLength != 0);


        TEST(api->GamutMathI16Array_Create != 0);
        TEST(api->GamutMathI16Array_GetType != 0);
        TEST(api->GamutMathI16Array_GetValuePointer != 0);
        TEST(api->GamutMathI16Array_GetLength != 0);


        TEST(api->GamutMathU16Array_Create != 0);
        TEST(api->GamutMathU16Array_GetType != 0);
        TEST(api->GamutMathU16Array_GetValuePointer != 0);
        TEST(api->GamutMathU16Array_GetLength != 0);


        TEST(api->GamutMathI32Array_Create != 0);
        TEST(api->GamutMathI32Array_GetType != 0);
        TEST(api->GamutMathI32Array_GetValuePointer != 0);
        TEST(api->GamutMathI32Array_GetLength != 0);


        TEST(api->GamutMathU32Array_Create != 0);
        TEST(api->GamutMathU32Array_GetType != 0);
        TEST(api->GamutMathU32Array_GetValuePointer != 0);
        TEST(api->GamutMathU32Array_GetLength != 0);


        TEST(api->GamutMathIArray_Create != 0);
        TEST(api->GamutMathIArray_GetType != 0);
        TEST(api->GamutMathIArray_GetValuePointer != 0);
        TEST(api->GamutMathIArray_GetLength != 0);


        TEST(api->GamutMathUArray_Create != 0);
        TEST(api->GamutMathUArray_GetType != 0);
        TEST(api->GamutMathUArray_GetValuePointer != 0);
        TEST(api->GamutMathUArray_GetLength != 0);


        TEST(api->GamutMathI64Array_Create != 0);
        TEST(api->GamutMathI64Array_GetType != 0);
        TEST(api->GamutMathI64Array_GetValuePointer != 0);
        TEST(api->GamutMathI64Array_GetLength != 0);


        TEST(api->GamutMathU64Array_Create != 0);
        TEST(api->GamutMathU64Array_GetType != 0);
        TEST(api->GamutMathU64Array_GetValuePointer != 0);
        TEST(api->GamutMathU64Array_GetLength != 0);

    Py_RETURN_NONE;
}





    static PyObject *
    test_BVector2(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathBVector2_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            bool components[2] = {

                    0,

                    1

            };
            PyObject *obj = api->GamutMathBVector2_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            bool *value_ptr = api->GamutMathBVector2_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (bool)0);

                TEST(value_ptr[1] == (bool)1);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        bool *value_ptr = api->GamutMathBVector2_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }

    static PyObject *
    test_BVector2Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathBVector2Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        bool components[20] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathBVector2Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathBVector2Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            bool *value_ptr = api->GamutMathBVector2Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 2; j++)
            {
                TEST(value_ptr[j] == (bool)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathBVector2Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        bool *value_ptr = api->GamutMathBVector2Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }





    static PyObject *
    test_DVector2(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathDVector2_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            double components[2] = {

                    0,

                    1

            };
            PyObject *obj = api->GamutMathDVector2_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            double *value_ptr = api->GamutMathDVector2_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (double)0);

                TEST(value_ptr[1] == (double)1);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        double *value_ptr = api->GamutMathDVector2_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }

    static PyObject *
    test_DVector2Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathDVector2Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        double components[20] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathDVector2Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathDVector2Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            double *value_ptr = api->GamutMathDVector2Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 2; j++)
            {
                TEST(value_ptr[j] == (double)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathDVector2Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        double *value_ptr = api->GamutMathDVector2Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }





    static PyObject *
    test_FVector2(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathFVector2_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            float components[2] = {

                    0,

                    1

            };
            PyObject *obj = api->GamutMathFVector2_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            float *value_ptr = api->GamutMathFVector2_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (float)0);

                TEST(value_ptr[1] == (float)1);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        float *value_ptr = api->GamutMathFVector2_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }

    static PyObject *
    test_FVector2Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathFVector2Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        float components[20] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathFVector2Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathFVector2Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            float *value_ptr = api->GamutMathFVector2Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 2; j++)
            {
                TEST(value_ptr[j] == (float)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathFVector2Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        float *value_ptr = api->GamutMathFVector2Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }





    static PyObject *
    test_I8Vector2(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathI8Vector2_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            int8_t components[2] = {

                    0,

                    1

            };
            PyObject *obj = api->GamutMathI8Vector2_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            int8_t *value_ptr = api->GamutMathI8Vector2_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (int8_t)0);

                TEST(value_ptr[1] == (int8_t)1);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        int8_t *value_ptr = api->GamutMathI8Vector2_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }

    static PyObject *
    test_I8Vector2Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathI8Vector2Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        int8_t components[20] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathI8Vector2Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathI8Vector2Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            int8_t *value_ptr = api->GamutMathI8Vector2Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 2; j++)
            {
                TEST(value_ptr[j] == (int8_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathI8Vector2Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        int8_t *value_ptr = api->GamutMathI8Vector2Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }





    static PyObject *
    test_U8Vector2(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathU8Vector2_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            uint8_t components[2] = {

                    0,

                    1

            };
            PyObject *obj = api->GamutMathU8Vector2_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            uint8_t *value_ptr = api->GamutMathU8Vector2_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (uint8_t)0);

                TEST(value_ptr[1] == (uint8_t)1);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        uint8_t *value_ptr = api->GamutMathU8Vector2_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }

    static PyObject *
    test_U8Vector2Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathU8Vector2Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        uint8_t components[20] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathU8Vector2Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathU8Vector2Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            uint8_t *value_ptr = api->GamutMathU8Vector2Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 2; j++)
            {
                TEST(value_ptr[j] == (uint8_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathU8Vector2Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        uint8_t *value_ptr = api->GamutMathU8Vector2Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }





    static PyObject *
    test_I16Vector2(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathI16Vector2_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            int16_t components[2] = {

                    0,

                    1

            };
            PyObject *obj = api->GamutMathI16Vector2_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            int16_t *value_ptr = api->GamutMathI16Vector2_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (int16_t)0);

                TEST(value_ptr[1] == (int16_t)1);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        int16_t *value_ptr = api->GamutMathI16Vector2_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }

    static PyObject *
    test_I16Vector2Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathI16Vector2Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        int16_t components[20] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathI16Vector2Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathI16Vector2Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            int16_t *value_ptr = api->GamutMathI16Vector2Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 2; j++)
            {
                TEST(value_ptr[j] == (int16_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathI16Vector2Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        int16_t *value_ptr = api->GamutMathI16Vector2Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }





    static PyObject *
    test_U16Vector2(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathU16Vector2_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            uint16_t components[2] = {

                    0,

                    1

            };
            PyObject *obj = api->GamutMathU16Vector2_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            uint16_t *value_ptr = api->GamutMathU16Vector2_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (uint16_t)0);

                TEST(value_ptr[1] == (uint16_t)1);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        uint16_t *value_ptr = api->GamutMathU16Vector2_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }

    static PyObject *
    test_U16Vector2Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathU16Vector2Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        uint16_t components[20] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathU16Vector2Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathU16Vector2Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            uint16_t *value_ptr = api->GamutMathU16Vector2Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 2; j++)
            {
                TEST(value_ptr[j] == (uint16_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathU16Vector2Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        uint16_t *value_ptr = api->GamutMathU16Vector2Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }





    static PyObject *
    test_I32Vector2(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathI32Vector2_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            int32_t components[2] = {

                    0,

                    1

            };
            PyObject *obj = api->GamutMathI32Vector2_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            int32_t *value_ptr = api->GamutMathI32Vector2_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (int32_t)0);

                TEST(value_ptr[1] == (int32_t)1);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        int32_t *value_ptr = api->GamutMathI32Vector2_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }

    static PyObject *
    test_I32Vector2Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathI32Vector2Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        int32_t components[20] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathI32Vector2Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathI32Vector2Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            int32_t *value_ptr = api->GamutMathI32Vector2Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 2; j++)
            {
                TEST(value_ptr[j] == (int32_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathI32Vector2Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        int32_t *value_ptr = api->GamutMathI32Vector2Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }





    static PyObject *
    test_U32Vector2(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathU32Vector2_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            uint32_t components[2] = {

                    0,

                    1

            };
            PyObject *obj = api->GamutMathU32Vector2_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            uint32_t *value_ptr = api->GamutMathU32Vector2_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (uint32_t)0);

                TEST(value_ptr[1] == (uint32_t)1);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        uint32_t *value_ptr = api->GamutMathU32Vector2_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }

    static PyObject *
    test_U32Vector2Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathU32Vector2Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        uint32_t components[20] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathU32Vector2Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathU32Vector2Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            uint32_t *value_ptr = api->GamutMathU32Vector2Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 2; j++)
            {
                TEST(value_ptr[j] == (uint32_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathU32Vector2Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        uint32_t *value_ptr = api->GamutMathU32Vector2Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }





    static PyObject *
    test_IVector2(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathIVector2_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            int components[2] = {

                    0,

                    1

            };
            PyObject *obj = api->GamutMathIVector2_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            int *value_ptr = api->GamutMathIVector2_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (int)0);

                TEST(value_ptr[1] == (int)1);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        int *value_ptr = api->GamutMathIVector2_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }

    static PyObject *
    test_IVector2Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathIVector2Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        int components[20] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathIVector2Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathIVector2Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            int *value_ptr = api->GamutMathIVector2Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 2; j++)
            {
                TEST(value_ptr[j] == (int)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathIVector2Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        int *value_ptr = api->GamutMathIVector2Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }





    static PyObject *
    test_UVector2(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathUVector2_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            unsigned int components[2] = {

                    0,

                    1

            };
            PyObject *obj = api->GamutMathUVector2_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            unsigned int *value_ptr = api->GamutMathUVector2_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (unsigned int)0);

                TEST(value_ptr[1] == (unsigned int)1);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        unsigned int *value_ptr = api->GamutMathUVector2_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }

    static PyObject *
    test_UVector2Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathUVector2Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        unsigned int components[20] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathUVector2Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathUVector2Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            unsigned int *value_ptr = api->GamutMathUVector2Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 2; j++)
            {
                TEST(value_ptr[j] == (unsigned int)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathUVector2Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        unsigned int *value_ptr = api->GamutMathUVector2Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }





    static PyObject *
    test_I64Vector2(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathI64Vector2_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            int64_t components[2] = {

                    0,

                    1

            };
            PyObject *obj = api->GamutMathI64Vector2_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            int64_t *value_ptr = api->GamutMathI64Vector2_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (int64_t)0);

                TEST(value_ptr[1] == (int64_t)1);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        int64_t *value_ptr = api->GamutMathI64Vector2_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }

    static PyObject *
    test_I64Vector2Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathI64Vector2Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        int64_t components[20] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathI64Vector2Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathI64Vector2Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            int64_t *value_ptr = api->GamutMathI64Vector2Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 2; j++)
            {
                TEST(value_ptr[j] == (int64_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathI64Vector2Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        int64_t *value_ptr = api->GamutMathI64Vector2Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }





    static PyObject *
    test_U64Vector2(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathU64Vector2_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            uint64_t components[2] = {

                    0,

                    1

            };
            PyObject *obj = api->GamutMathU64Vector2_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            uint64_t *value_ptr = api->GamutMathU64Vector2_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (uint64_t)0);

                TEST(value_ptr[1] == (uint64_t)1);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        uint64_t *value_ptr = api->GamutMathU64Vector2_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }

    static PyObject *
    test_U64Vector2Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathU64Vector2Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        uint64_t components[20] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathU64Vector2Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathU64Vector2Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            uint64_t *value_ptr = api->GamutMathU64Vector2Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 2; j++)
            {
                TEST(value_ptr[j] == (uint64_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathU64Vector2Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        uint64_t *value_ptr = api->GamutMathU64Vector2Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }





    static PyObject *
    test_BVector3(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathBVector3_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            bool components[3] = {

                    0,

                    1,

                    2

            };
            PyObject *obj = api->GamutMathBVector3_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            bool *value_ptr = api->GamutMathBVector3_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (bool)0);

                TEST(value_ptr[1] == (bool)1);

                TEST(value_ptr[2] == (bool)2);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        bool *value_ptr = api->GamutMathBVector3_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }

    static PyObject *
    test_BVector3Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathBVector3Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        bool components[30] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathBVector3Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathBVector3Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            bool *value_ptr = api->GamutMathBVector3Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 3; j++)
            {
                TEST(value_ptr[j] == (bool)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathBVector3Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        bool *value_ptr = api->GamutMathBVector3Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }





    static PyObject *
    test_DVector3(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathDVector3_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            double components[3] = {

                    0,

                    1,

                    2

            };
            PyObject *obj = api->GamutMathDVector3_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            double *value_ptr = api->GamutMathDVector3_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (double)0);

                TEST(value_ptr[1] == (double)1);

                TEST(value_ptr[2] == (double)2);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        double *value_ptr = api->GamutMathDVector3_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }

    static PyObject *
    test_DVector3Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathDVector3Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        double components[30] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathDVector3Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathDVector3Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            double *value_ptr = api->GamutMathDVector3Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 3; j++)
            {
                TEST(value_ptr[j] == (double)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathDVector3Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        double *value_ptr = api->GamutMathDVector3Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }





    static PyObject *
    test_FVector3(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathFVector3_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            float components[3] = {

                    0,

                    1,

                    2

            };
            PyObject *obj = api->GamutMathFVector3_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            float *value_ptr = api->GamutMathFVector3_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (float)0);

                TEST(value_ptr[1] == (float)1);

                TEST(value_ptr[2] == (float)2);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        float *value_ptr = api->GamutMathFVector3_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }

    static PyObject *
    test_FVector3Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathFVector3Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        float components[30] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathFVector3Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathFVector3Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            float *value_ptr = api->GamutMathFVector3Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 3; j++)
            {
                TEST(value_ptr[j] == (float)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathFVector3Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        float *value_ptr = api->GamutMathFVector3Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }





    static PyObject *
    test_I8Vector3(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathI8Vector3_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            int8_t components[3] = {

                    0,

                    1,

                    2

            };
            PyObject *obj = api->GamutMathI8Vector3_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            int8_t *value_ptr = api->GamutMathI8Vector3_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (int8_t)0);

                TEST(value_ptr[1] == (int8_t)1);

                TEST(value_ptr[2] == (int8_t)2);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        int8_t *value_ptr = api->GamutMathI8Vector3_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }

    static PyObject *
    test_I8Vector3Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathI8Vector3Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        int8_t components[30] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathI8Vector3Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathI8Vector3Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            int8_t *value_ptr = api->GamutMathI8Vector3Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 3; j++)
            {
                TEST(value_ptr[j] == (int8_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathI8Vector3Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        int8_t *value_ptr = api->GamutMathI8Vector3Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }





    static PyObject *
    test_U8Vector3(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathU8Vector3_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            uint8_t components[3] = {

                    0,

                    1,

                    2

            };
            PyObject *obj = api->GamutMathU8Vector3_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            uint8_t *value_ptr = api->GamutMathU8Vector3_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (uint8_t)0);

                TEST(value_ptr[1] == (uint8_t)1);

                TEST(value_ptr[2] == (uint8_t)2);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        uint8_t *value_ptr = api->GamutMathU8Vector3_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }

    static PyObject *
    test_U8Vector3Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathU8Vector3Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        uint8_t components[30] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathU8Vector3Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathU8Vector3Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            uint8_t *value_ptr = api->GamutMathU8Vector3Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 3; j++)
            {
                TEST(value_ptr[j] == (uint8_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathU8Vector3Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        uint8_t *value_ptr = api->GamutMathU8Vector3Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }





    static PyObject *
    test_I16Vector3(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathI16Vector3_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            int16_t components[3] = {

                    0,

                    1,

                    2

            };
            PyObject *obj = api->GamutMathI16Vector3_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            int16_t *value_ptr = api->GamutMathI16Vector3_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (int16_t)0);

                TEST(value_ptr[1] == (int16_t)1);

                TEST(value_ptr[2] == (int16_t)2);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        int16_t *value_ptr = api->GamutMathI16Vector3_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }

    static PyObject *
    test_I16Vector3Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathI16Vector3Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        int16_t components[30] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathI16Vector3Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathI16Vector3Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            int16_t *value_ptr = api->GamutMathI16Vector3Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 3; j++)
            {
                TEST(value_ptr[j] == (int16_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathI16Vector3Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        int16_t *value_ptr = api->GamutMathI16Vector3Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }





    static PyObject *
    test_U16Vector3(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathU16Vector3_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            uint16_t components[3] = {

                    0,

                    1,

                    2

            };
            PyObject *obj = api->GamutMathU16Vector3_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            uint16_t *value_ptr = api->GamutMathU16Vector3_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (uint16_t)0);

                TEST(value_ptr[1] == (uint16_t)1);

                TEST(value_ptr[2] == (uint16_t)2);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        uint16_t *value_ptr = api->GamutMathU16Vector3_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }

    static PyObject *
    test_U16Vector3Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathU16Vector3Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        uint16_t components[30] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathU16Vector3Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathU16Vector3Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            uint16_t *value_ptr = api->GamutMathU16Vector3Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 3; j++)
            {
                TEST(value_ptr[j] == (uint16_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathU16Vector3Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        uint16_t *value_ptr = api->GamutMathU16Vector3Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }





    static PyObject *
    test_I32Vector3(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathI32Vector3_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            int32_t components[3] = {

                    0,

                    1,

                    2

            };
            PyObject *obj = api->GamutMathI32Vector3_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            int32_t *value_ptr = api->GamutMathI32Vector3_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (int32_t)0);

                TEST(value_ptr[1] == (int32_t)1);

                TEST(value_ptr[2] == (int32_t)2);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        int32_t *value_ptr = api->GamutMathI32Vector3_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }

    static PyObject *
    test_I32Vector3Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathI32Vector3Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        int32_t components[30] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathI32Vector3Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathI32Vector3Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            int32_t *value_ptr = api->GamutMathI32Vector3Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 3; j++)
            {
                TEST(value_ptr[j] == (int32_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathI32Vector3Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        int32_t *value_ptr = api->GamutMathI32Vector3Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }





    static PyObject *
    test_U32Vector3(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathU32Vector3_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            uint32_t components[3] = {

                    0,

                    1,

                    2

            };
            PyObject *obj = api->GamutMathU32Vector3_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            uint32_t *value_ptr = api->GamutMathU32Vector3_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (uint32_t)0);

                TEST(value_ptr[1] == (uint32_t)1);

                TEST(value_ptr[2] == (uint32_t)2);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        uint32_t *value_ptr = api->GamutMathU32Vector3_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }

    static PyObject *
    test_U32Vector3Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathU32Vector3Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        uint32_t components[30] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathU32Vector3Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathU32Vector3Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            uint32_t *value_ptr = api->GamutMathU32Vector3Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 3; j++)
            {
                TEST(value_ptr[j] == (uint32_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathU32Vector3Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        uint32_t *value_ptr = api->GamutMathU32Vector3Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }





    static PyObject *
    test_IVector3(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathIVector3_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            int components[3] = {

                    0,

                    1,

                    2

            };
            PyObject *obj = api->GamutMathIVector3_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            int *value_ptr = api->GamutMathIVector3_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (int)0);

                TEST(value_ptr[1] == (int)1);

                TEST(value_ptr[2] == (int)2);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        int *value_ptr = api->GamutMathIVector3_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }

    static PyObject *
    test_IVector3Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathIVector3Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        int components[30] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathIVector3Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathIVector3Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            int *value_ptr = api->GamutMathIVector3Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 3; j++)
            {
                TEST(value_ptr[j] == (int)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathIVector3Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        int *value_ptr = api->GamutMathIVector3Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }





    static PyObject *
    test_UVector3(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathUVector3_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            unsigned int components[3] = {

                    0,

                    1,

                    2

            };
            PyObject *obj = api->GamutMathUVector3_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            unsigned int *value_ptr = api->GamutMathUVector3_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (unsigned int)0);

                TEST(value_ptr[1] == (unsigned int)1);

                TEST(value_ptr[2] == (unsigned int)2);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        unsigned int *value_ptr = api->GamutMathUVector3_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }

    static PyObject *
    test_UVector3Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathUVector3Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        unsigned int components[30] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathUVector3Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathUVector3Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            unsigned int *value_ptr = api->GamutMathUVector3Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 3; j++)
            {
                TEST(value_ptr[j] == (unsigned int)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathUVector3Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        unsigned int *value_ptr = api->GamutMathUVector3Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }





    static PyObject *
    test_I64Vector3(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathI64Vector3_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            int64_t components[3] = {

                    0,

                    1,

                    2

            };
            PyObject *obj = api->GamutMathI64Vector3_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            int64_t *value_ptr = api->GamutMathI64Vector3_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (int64_t)0);

                TEST(value_ptr[1] == (int64_t)1);

                TEST(value_ptr[2] == (int64_t)2);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        int64_t *value_ptr = api->GamutMathI64Vector3_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }

    static PyObject *
    test_I64Vector3Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathI64Vector3Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        int64_t components[30] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathI64Vector3Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathI64Vector3Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            int64_t *value_ptr = api->GamutMathI64Vector3Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 3; j++)
            {
                TEST(value_ptr[j] == (int64_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathI64Vector3Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        int64_t *value_ptr = api->GamutMathI64Vector3Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }





    static PyObject *
    test_U64Vector3(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathU64Vector3_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            uint64_t components[3] = {

                    0,

                    1,

                    2

            };
            PyObject *obj = api->GamutMathU64Vector3_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            uint64_t *value_ptr = api->GamutMathU64Vector3_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (uint64_t)0);

                TEST(value_ptr[1] == (uint64_t)1);

                TEST(value_ptr[2] == (uint64_t)2);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        uint64_t *value_ptr = api->GamutMathU64Vector3_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }

    static PyObject *
    test_U64Vector3Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathU64Vector3Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        uint64_t components[30] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathU64Vector3Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathU64Vector3Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            uint64_t *value_ptr = api->GamutMathU64Vector3Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 3; j++)
            {
                TEST(value_ptr[j] == (uint64_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathU64Vector3Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        uint64_t *value_ptr = api->GamutMathU64Vector3Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }





    static PyObject *
    test_BVector4(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathBVector4_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            bool components[4] = {

                    0,

                    1,

                    2,

                    3

            };
            PyObject *obj = api->GamutMathBVector4_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            bool *value_ptr = api->GamutMathBVector4_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (bool)0);

                TEST(value_ptr[1] == (bool)1);

                TEST(value_ptr[2] == (bool)2);

                TEST(value_ptr[3] == (bool)3);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        bool *value_ptr = api->GamutMathBVector4_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }

    static PyObject *
    test_BVector4Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathBVector4Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        bool components[40] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29,

                30,

                31,

                32,

                33,

                34,

                35,

                36,

                37,

                38,

                39

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathBVector4Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathBVector4Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            bool *value_ptr = api->GamutMathBVector4Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 4; j++)
            {
                TEST(value_ptr[j] == (bool)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathBVector4Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        bool *value_ptr = api->GamutMathBVector4Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }





    static PyObject *
    test_DVector4(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathDVector4_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            double components[4] = {

                    0,

                    1,

                    2,

                    3

            };
            PyObject *obj = api->GamutMathDVector4_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            double *value_ptr = api->GamutMathDVector4_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (double)0);

                TEST(value_ptr[1] == (double)1);

                TEST(value_ptr[2] == (double)2);

                TEST(value_ptr[3] == (double)3);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        double *value_ptr = api->GamutMathDVector4_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }

    static PyObject *
    test_DVector4Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathDVector4Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        double components[40] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29,

                30,

                31,

                32,

                33,

                34,

                35,

                36,

                37,

                38,

                39

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathDVector4Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathDVector4Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            double *value_ptr = api->GamutMathDVector4Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 4; j++)
            {
                TEST(value_ptr[j] == (double)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathDVector4Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        double *value_ptr = api->GamutMathDVector4Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }





    static PyObject *
    test_FVector4(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathFVector4_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            float components[4] = {

                    0,

                    1,

                    2,

                    3

            };
            PyObject *obj = api->GamutMathFVector4_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            float *value_ptr = api->GamutMathFVector4_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (float)0);

                TEST(value_ptr[1] == (float)1);

                TEST(value_ptr[2] == (float)2);

                TEST(value_ptr[3] == (float)3);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        float *value_ptr = api->GamutMathFVector4_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }

    static PyObject *
    test_FVector4Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathFVector4Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        float components[40] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29,

                30,

                31,

                32,

                33,

                34,

                35,

                36,

                37,

                38,

                39

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathFVector4Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathFVector4Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            float *value_ptr = api->GamutMathFVector4Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 4; j++)
            {
                TEST(value_ptr[j] == (float)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathFVector4Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        float *value_ptr = api->GamutMathFVector4Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }





    static PyObject *
    test_I8Vector4(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathI8Vector4_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            int8_t components[4] = {

                    0,

                    1,

                    2,

                    3

            };
            PyObject *obj = api->GamutMathI8Vector4_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            int8_t *value_ptr = api->GamutMathI8Vector4_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (int8_t)0);

                TEST(value_ptr[1] == (int8_t)1);

                TEST(value_ptr[2] == (int8_t)2);

                TEST(value_ptr[3] == (int8_t)3);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        int8_t *value_ptr = api->GamutMathI8Vector4_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }

    static PyObject *
    test_I8Vector4Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathI8Vector4Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        int8_t components[40] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29,

                30,

                31,

                32,

                33,

                34,

                35,

                36,

                37,

                38,

                39

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathI8Vector4Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathI8Vector4Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            int8_t *value_ptr = api->GamutMathI8Vector4Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 4; j++)
            {
                TEST(value_ptr[j] == (int8_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathI8Vector4Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        int8_t *value_ptr = api->GamutMathI8Vector4Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }





    static PyObject *
    test_U8Vector4(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathU8Vector4_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            uint8_t components[4] = {

                    0,

                    1,

                    2,

                    3

            };
            PyObject *obj = api->GamutMathU8Vector4_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            uint8_t *value_ptr = api->GamutMathU8Vector4_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (uint8_t)0);

                TEST(value_ptr[1] == (uint8_t)1);

                TEST(value_ptr[2] == (uint8_t)2);

                TEST(value_ptr[3] == (uint8_t)3);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        uint8_t *value_ptr = api->GamutMathU8Vector4_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }

    static PyObject *
    test_U8Vector4Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathU8Vector4Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        uint8_t components[40] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29,

                30,

                31,

                32,

                33,

                34,

                35,

                36,

                37,

                38,

                39

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathU8Vector4Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathU8Vector4Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            uint8_t *value_ptr = api->GamutMathU8Vector4Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 4; j++)
            {
                TEST(value_ptr[j] == (uint8_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathU8Vector4Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        uint8_t *value_ptr = api->GamutMathU8Vector4Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }





    static PyObject *
    test_I16Vector4(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathI16Vector4_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            int16_t components[4] = {

                    0,

                    1,

                    2,

                    3

            };
            PyObject *obj = api->GamutMathI16Vector4_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            int16_t *value_ptr = api->GamutMathI16Vector4_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (int16_t)0);

                TEST(value_ptr[1] == (int16_t)1);

                TEST(value_ptr[2] == (int16_t)2);

                TEST(value_ptr[3] == (int16_t)3);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        int16_t *value_ptr = api->GamutMathI16Vector4_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }

    static PyObject *
    test_I16Vector4Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathI16Vector4Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        int16_t components[40] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29,

                30,

                31,

                32,

                33,

                34,

                35,

                36,

                37,

                38,

                39

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathI16Vector4Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathI16Vector4Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            int16_t *value_ptr = api->GamutMathI16Vector4Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 4; j++)
            {
                TEST(value_ptr[j] == (int16_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathI16Vector4Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        int16_t *value_ptr = api->GamutMathI16Vector4Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }





    static PyObject *
    test_U16Vector4(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathU16Vector4_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            uint16_t components[4] = {

                    0,

                    1,

                    2,

                    3

            };
            PyObject *obj = api->GamutMathU16Vector4_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            uint16_t *value_ptr = api->GamutMathU16Vector4_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (uint16_t)0);

                TEST(value_ptr[1] == (uint16_t)1);

                TEST(value_ptr[2] == (uint16_t)2);

                TEST(value_ptr[3] == (uint16_t)3);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        uint16_t *value_ptr = api->GamutMathU16Vector4_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }

    static PyObject *
    test_U16Vector4Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathU16Vector4Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        uint16_t components[40] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29,

                30,

                31,

                32,

                33,

                34,

                35,

                36,

                37,

                38,

                39

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathU16Vector4Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathU16Vector4Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            uint16_t *value_ptr = api->GamutMathU16Vector4Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 4; j++)
            {
                TEST(value_ptr[j] == (uint16_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathU16Vector4Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        uint16_t *value_ptr = api->GamutMathU16Vector4Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }





    static PyObject *
    test_I32Vector4(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathI32Vector4_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            int32_t components[4] = {

                    0,

                    1,

                    2,

                    3

            };
            PyObject *obj = api->GamutMathI32Vector4_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            int32_t *value_ptr = api->GamutMathI32Vector4_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (int32_t)0);

                TEST(value_ptr[1] == (int32_t)1);

                TEST(value_ptr[2] == (int32_t)2);

                TEST(value_ptr[3] == (int32_t)3);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        int32_t *value_ptr = api->GamutMathI32Vector4_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }

    static PyObject *
    test_I32Vector4Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathI32Vector4Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        int32_t components[40] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29,

                30,

                31,

                32,

                33,

                34,

                35,

                36,

                37,

                38,

                39

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathI32Vector4Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathI32Vector4Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            int32_t *value_ptr = api->GamutMathI32Vector4Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 4; j++)
            {
                TEST(value_ptr[j] == (int32_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathI32Vector4Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        int32_t *value_ptr = api->GamutMathI32Vector4Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }





    static PyObject *
    test_U32Vector4(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathU32Vector4_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            uint32_t components[4] = {

                    0,

                    1,

                    2,

                    3

            };
            PyObject *obj = api->GamutMathU32Vector4_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            uint32_t *value_ptr = api->GamutMathU32Vector4_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (uint32_t)0);

                TEST(value_ptr[1] == (uint32_t)1);

                TEST(value_ptr[2] == (uint32_t)2);

                TEST(value_ptr[3] == (uint32_t)3);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        uint32_t *value_ptr = api->GamutMathU32Vector4_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }

    static PyObject *
    test_U32Vector4Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathU32Vector4Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        uint32_t components[40] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29,

                30,

                31,

                32,

                33,

                34,

                35,

                36,

                37,

                38,

                39

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathU32Vector4Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathU32Vector4Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            uint32_t *value_ptr = api->GamutMathU32Vector4Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 4; j++)
            {
                TEST(value_ptr[j] == (uint32_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathU32Vector4Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        uint32_t *value_ptr = api->GamutMathU32Vector4Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }





    static PyObject *
    test_IVector4(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathIVector4_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            int components[4] = {

                    0,

                    1,

                    2,

                    3

            };
            PyObject *obj = api->GamutMathIVector4_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            int *value_ptr = api->GamutMathIVector4_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (int)0);

                TEST(value_ptr[1] == (int)1);

                TEST(value_ptr[2] == (int)2);

                TEST(value_ptr[3] == (int)3);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        int *value_ptr = api->GamutMathIVector4_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }

    static PyObject *
    test_IVector4Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathIVector4Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        int components[40] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29,

                30,

                31,

                32,

                33,

                34,

                35,

                36,

                37,

                38,

                39

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathIVector4Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathIVector4Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            int *value_ptr = api->GamutMathIVector4Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 4; j++)
            {
                TEST(value_ptr[j] == (int)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathIVector4Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        int *value_ptr = api->GamutMathIVector4Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }





    static PyObject *
    test_UVector4(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathUVector4_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            unsigned int components[4] = {

                    0,

                    1,

                    2,

                    3

            };
            PyObject *obj = api->GamutMathUVector4_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            unsigned int *value_ptr = api->GamutMathUVector4_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (unsigned int)0);

                TEST(value_ptr[1] == (unsigned int)1);

                TEST(value_ptr[2] == (unsigned int)2);

                TEST(value_ptr[3] == (unsigned int)3);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        unsigned int *value_ptr = api->GamutMathUVector4_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }

    static PyObject *
    test_UVector4Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathUVector4Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        unsigned int components[40] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29,

                30,

                31,

                32,

                33,

                34,

                35,

                36,

                37,

                38,

                39

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathUVector4Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathUVector4Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            unsigned int *value_ptr = api->GamutMathUVector4Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 4; j++)
            {
                TEST(value_ptr[j] == (unsigned int)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathUVector4Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        unsigned int *value_ptr = api->GamutMathUVector4Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }





    static PyObject *
    test_I64Vector4(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathI64Vector4_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            int64_t components[4] = {

                    0,

                    1,

                    2,

                    3

            };
            PyObject *obj = api->GamutMathI64Vector4_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            int64_t *value_ptr = api->GamutMathI64Vector4_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (int64_t)0);

                TEST(value_ptr[1] == (int64_t)1);

                TEST(value_ptr[2] == (int64_t)2);

                TEST(value_ptr[3] == (int64_t)3);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        int64_t *value_ptr = api->GamutMathI64Vector4_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }

    static PyObject *
    test_I64Vector4Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathI64Vector4Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        int64_t components[40] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29,

                30,

                31,

                32,

                33,

                34,

                35,

                36,

                37,

                38,

                39

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathI64Vector4Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathI64Vector4Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            int64_t *value_ptr = api->GamutMathI64Vector4Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 4; j++)
            {
                TEST(value_ptr[j] == (int64_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathI64Vector4Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        int64_t *value_ptr = api->GamutMathI64Vector4Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }





    static PyObject *
    test_U64Vector4(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathU64Vector4_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            uint64_t components[4] = {

                    0,

                    1,

                    2,

                    3

            };
            PyObject *obj = api->GamutMathU64Vector4_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            uint64_t *value_ptr = api->GamutMathU64Vector4_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (uint64_t)0);

                TEST(value_ptr[1] == (uint64_t)1);

                TEST(value_ptr[2] == (uint64_t)2);

                TEST(value_ptr[3] == (uint64_t)3);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        uint64_t *value_ptr = api->GamutMathU64Vector4_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }

    static PyObject *
    test_U64Vector4Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathU64Vector4Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        uint64_t components[40] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29,

                30,

                31,

                32,

                33,

                34,

                35,

                36,

                37,

                38,

                39

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathU64Vector4Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathU64Vector4Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            uint64_t *value_ptr = api->GamutMathU64Vector4Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 4; j++)
            {
                TEST(value_ptr[j] == (uint64_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathU64Vector4Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        uint64_t *value_ptr = api->GamutMathU64Vector4Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }










    static PyObject *
    test_DMatrix2x2(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathDMatrix2x2_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            double components[4] = {

                    0,

                    1,

                    2,

                    3

            };
            PyObject *obj = api->GamutMathDMatrix2x2_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            double *value_ptr = api->GamutMathDMatrix2x2_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (double)0);

                TEST(value_ptr[1] == (double)1);

                TEST(value_ptr[2] == (double)2);

                TEST(value_ptr[3] == (double)3);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        double *value_ptr = api->GamutMathDMatrix2x2_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }

    static PyObject *
    test_DMatrix2x2Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathDMatrix2x2Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        double components[40] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29,

                30,

                31,

                32,

                33,

                34,

                35,

                36,

                37,

                38,

                39

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathDMatrix2x2Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathDMatrix2x2Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            double *value_ptr = api->GamutMathDMatrix2x2Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 4; j++)
            {
                TEST(value_ptr[j] == (double)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathDMatrix2x2Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        double *value_ptr = api->GamutMathDMatrix2x2Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }









    static PyObject *
    test_FMatrix2x2(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathFMatrix2x2_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            float components[4] = {

                    0,

                    1,

                    2,

                    3

            };
            PyObject *obj = api->GamutMathFMatrix2x2_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            float *value_ptr = api->GamutMathFMatrix2x2_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (float)0);

                TEST(value_ptr[1] == (float)1);

                TEST(value_ptr[2] == (float)2);

                TEST(value_ptr[3] == (float)3);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        float *value_ptr = api->GamutMathFMatrix2x2_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }

    static PyObject *
    test_FMatrix2x2Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathFMatrix2x2Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        float components[40] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29,

                30,

                31,

                32,

                33,

                34,

                35,

                36,

                37,

                38,

                39

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathFMatrix2x2Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathFMatrix2x2Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            float *value_ptr = api->GamutMathFMatrix2x2Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 4; j++)
            {
                TEST(value_ptr[j] == (float)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathFMatrix2x2Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        float *value_ptr = api->GamutMathFMatrix2x2Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }









    static PyObject *
    test_DMatrix2x3(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathDMatrix2x3_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            double components[6] = {

                    0,

                    1,

                    2,

                    3,

                    4,

                    5

            };
            PyObject *obj = api->GamutMathDMatrix2x3_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            double *value_ptr = api->GamutMathDMatrix2x3_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (double)0);

                TEST(value_ptr[1] == (double)1);

                TEST(value_ptr[2] == (double)2);

                TEST(value_ptr[3] == (double)3);

                TEST(value_ptr[4] == (double)4);

                TEST(value_ptr[5] == (double)5);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        double *value_ptr = api->GamutMathDMatrix2x3_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }

    static PyObject *
    test_DMatrix2x3Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathDMatrix2x3Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        double components[60] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29,

                30,

                31,

                32,

                33,

                34,

                35,

                36,

                37,

                38,

                39,

                40,

                41,

                42,

                43,

                44,

                45,

                46,

                47,

                48,

                49,

                50,

                51,

                52,

                53,

                54,

                55,

                56,

                57,

                58,

                59

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathDMatrix2x3Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathDMatrix2x3Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            double *value_ptr = api->GamutMathDMatrix2x3Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 6; j++)
            {
                TEST(value_ptr[j] == (double)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathDMatrix2x3Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        double *value_ptr = api->GamutMathDMatrix2x3Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }









    static PyObject *
    test_FMatrix2x3(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathFMatrix2x3_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            float components[6] = {

                    0,

                    1,

                    2,

                    3,

                    4,

                    5

            };
            PyObject *obj = api->GamutMathFMatrix2x3_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            float *value_ptr = api->GamutMathFMatrix2x3_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (float)0);

                TEST(value_ptr[1] == (float)1);

                TEST(value_ptr[2] == (float)2);

                TEST(value_ptr[3] == (float)3);

                TEST(value_ptr[4] == (float)4);

                TEST(value_ptr[5] == (float)5);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        float *value_ptr = api->GamutMathFMatrix2x3_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }

    static PyObject *
    test_FMatrix2x3Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathFMatrix2x3Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        float components[60] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29,

                30,

                31,

                32,

                33,

                34,

                35,

                36,

                37,

                38,

                39,

                40,

                41,

                42,

                43,

                44,

                45,

                46,

                47,

                48,

                49,

                50,

                51,

                52,

                53,

                54,

                55,

                56,

                57,

                58,

                59

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathFMatrix2x3Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathFMatrix2x3Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            float *value_ptr = api->GamutMathFMatrix2x3Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 6; j++)
            {
                TEST(value_ptr[j] == (float)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathFMatrix2x3Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        float *value_ptr = api->GamutMathFMatrix2x3Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }









    static PyObject *
    test_DMatrix2x4(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathDMatrix2x4_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            double components[8] = {

                    0,

                    1,

                    2,

                    3,

                    4,

                    5,

                    6,

                    7

            };
            PyObject *obj = api->GamutMathDMatrix2x4_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            double *value_ptr = api->GamutMathDMatrix2x4_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (double)0);

                TEST(value_ptr[1] == (double)1);

                TEST(value_ptr[2] == (double)2);

                TEST(value_ptr[3] == (double)3);

                TEST(value_ptr[4] == (double)4);

                TEST(value_ptr[5] == (double)5);

                TEST(value_ptr[6] == (double)6);

                TEST(value_ptr[7] == (double)7);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        double *value_ptr = api->GamutMathDMatrix2x4_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }

    static PyObject *
    test_DMatrix2x4Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathDMatrix2x4Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        double components[80] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29,

                30,

                31,

                32,

                33,

                34,

                35,

                36,

                37,

                38,

                39,

                40,

                41,

                42,

                43,

                44,

                45,

                46,

                47,

                48,

                49,

                50,

                51,

                52,

                53,

                54,

                55,

                56,

                57,

                58,

                59,

                60,

                61,

                62,

                63,

                64,

                65,

                66,

                67,

                68,

                69,

                70,

                71,

                72,

                73,

                74,

                75,

                76,

                77,

                78,

                79

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathDMatrix2x4Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathDMatrix2x4Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            double *value_ptr = api->GamutMathDMatrix2x4Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 8; j++)
            {
                TEST(value_ptr[j] == (double)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathDMatrix2x4Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        double *value_ptr = api->GamutMathDMatrix2x4Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }









    static PyObject *
    test_FMatrix2x4(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathFMatrix2x4_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            float components[8] = {

                    0,

                    1,

                    2,

                    3,

                    4,

                    5,

                    6,

                    7

            };
            PyObject *obj = api->GamutMathFMatrix2x4_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            float *value_ptr = api->GamutMathFMatrix2x4_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (float)0);

                TEST(value_ptr[1] == (float)1);

                TEST(value_ptr[2] == (float)2);

                TEST(value_ptr[3] == (float)3);

                TEST(value_ptr[4] == (float)4);

                TEST(value_ptr[5] == (float)5);

                TEST(value_ptr[6] == (float)6);

                TEST(value_ptr[7] == (float)7);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        float *value_ptr = api->GamutMathFMatrix2x4_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }

    static PyObject *
    test_FMatrix2x4Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathFMatrix2x4Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        float components[80] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29,

                30,

                31,

                32,

                33,

                34,

                35,

                36,

                37,

                38,

                39,

                40,

                41,

                42,

                43,

                44,

                45,

                46,

                47,

                48,

                49,

                50,

                51,

                52,

                53,

                54,

                55,

                56,

                57,

                58,

                59,

                60,

                61,

                62,

                63,

                64,

                65,

                66,

                67,

                68,

                69,

                70,

                71,

                72,

                73,

                74,

                75,

                76,

                77,

                78,

                79

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathFMatrix2x4Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathFMatrix2x4Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            float *value_ptr = api->GamutMathFMatrix2x4Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 8; j++)
            {
                TEST(value_ptr[j] == (float)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathFMatrix2x4Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        float *value_ptr = api->GamutMathFMatrix2x4Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }









    static PyObject *
    test_DMatrix3x2(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathDMatrix3x2_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            double components[6] = {

                    0,

                    1,

                    2,

                    3,

                    4,

                    5

            };
            PyObject *obj = api->GamutMathDMatrix3x2_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            double *value_ptr = api->GamutMathDMatrix3x2_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (double)0);

                TEST(value_ptr[1] == (double)1);

                TEST(value_ptr[2] == (double)2);

                TEST(value_ptr[3] == (double)3);

                TEST(value_ptr[4] == (double)4);

                TEST(value_ptr[5] == (double)5);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        double *value_ptr = api->GamutMathDMatrix3x2_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }

    static PyObject *
    test_DMatrix3x2Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathDMatrix3x2Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        double components[60] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29,

                30,

                31,

                32,

                33,

                34,

                35,

                36,

                37,

                38,

                39,

                40,

                41,

                42,

                43,

                44,

                45,

                46,

                47,

                48,

                49,

                50,

                51,

                52,

                53,

                54,

                55,

                56,

                57,

                58,

                59

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathDMatrix3x2Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathDMatrix3x2Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            double *value_ptr = api->GamutMathDMatrix3x2Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 6; j++)
            {
                TEST(value_ptr[j] == (double)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathDMatrix3x2Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        double *value_ptr = api->GamutMathDMatrix3x2Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }









    static PyObject *
    test_FMatrix3x2(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathFMatrix3x2_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            float components[6] = {

                    0,

                    1,

                    2,

                    3,

                    4,

                    5

            };
            PyObject *obj = api->GamutMathFMatrix3x2_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            float *value_ptr = api->GamutMathFMatrix3x2_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (float)0);

                TEST(value_ptr[1] == (float)1);

                TEST(value_ptr[2] == (float)2);

                TEST(value_ptr[3] == (float)3);

                TEST(value_ptr[4] == (float)4);

                TEST(value_ptr[5] == (float)5);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        float *value_ptr = api->GamutMathFMatrix3x2_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }

    static PyObject *
    test_FMatrix3x2Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathFMatrix3x2Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        float components[60] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29,

                30,

                31,

                32,

                33,

                34,

                35,

                36,

                37,

                38,

                39,

                40,

                41,

                42,

                43,

                44,

                45,

                46,

                47,

                48,

                49,

                50,

                51,

                52,

                53,

                54,

                55,

                56,

                57,

                58,

                59

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathFMatrix3x2Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathFMatrix3x2Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            float *value_ptr = api->GamutMathFMatrix3x2Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 6; j++)
            {
                TEST(value_ptr[j] == (float)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathFMatrix3x2Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        float *value_ptr = api->GamutMathFMatrix3x2Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }









    static PyObject *
    test_DMatrix3x3(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathDMatrix3x3_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            double components[9] = {

                    0,

                    1,

                    2,

                    3,

                    4,

                    5,

                    6,

                    7,

                    8

            };
            PyObject *obj = api->GamutMathDMatrix3x3_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            double *value_ptr = api->GamutMathDMatrix3x3_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (double)0);

                TEST(value_ptr[1] == (double)1);

                TEST(value_ptr[2] == (double)2);

                TEST(value_ptr[3] == (double)3);

                TEST(value_ptr[4] == (double)4);

                TEST(value_ptr[5] == (double)5);

                TEST(value_ptr[6] == (double)6);

                TEST(value_ptr[7] == (double)7);

                TEST(value_ptr[8] == (double)8);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        double *value_ptr = api->GamutMathDMatrix3x3_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }

    static PyObject *
    test_DMatrix3x3Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathDMatrix3x3Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        double components[90] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29,

                30,

                31,

                32,

                33,

                34,

                35,

                36,

                37,

                38,

                39,

                40,

                41,

                42,

                43,

                44,

                45,

                46,

                47,

                48,

                49,

                50,

                51,

                52,

                53,

                54,

                55,

                56,

                57,

                58,

                59,

                60,

                61,

                62,

                63,

                64,

                65,

                66,

                67,

                68,

                69,

                70,

                71,

                72,

                73,

                74,

                75,

                76,

                77,

                78,

                79,

                80,

                81,

                82,

                83,

                84,

                85,

                86,

                87,

                88,

                89

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathDMatrix3x3Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathDMatrix3x3Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            double *value_ptr = api->GamutMathDMatrix3x3Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 9; j++)
            {
                TEST(value_ptr[j] == (double)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathDMatrix3x3Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        double *value_ptr = api->GamutMathDMatrix3x3Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }









    static PyObject *
    test_FMatrix3x3(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathFMatrix3x3_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            float components[9] = {

                    0,

                    1,

                    2,

                    3,

                    4,

                    5,

                    6,

                    7,

                    8

            };
            PyObject *obj = api->GamutMathFMatrix3x3_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            float *value_ptr = api->GamutMathFMatrix3x3_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (float)0);

                TEST(value_ptr[1] == (float)1);

                TEST(value_ptr[2] == (float)2);

                TEST(value_ptr[3] == (float)3);

                TEST(value_ptr[4] == (float)4);

                TEST(value_ptr[5] == (float)5);

                TEST(value_ptr[6] == (float)6);

                TEST(value_ptr[7] == (float)7);

                TEST(value_ptr[8] == (float)8);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        float *value_ptr = api->GamutMathFMatrix3x3_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }

    static PyObject *
    test_FMatrix3x3Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathFMatrix3x3Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        float components[90] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29,

                30,

                31,

                32,

                33,

                34,

                35,

                36,

                37,

                38,

                39,

                40,

                41,

                42,

                43,

                44,

                45,

                46,

                47,

                48,

                49,

                50,

                51,

                52,

                53,

                54,

                55,

                56,

                57,

                58,

                59,

                60,

                61,

                62,

                63,

                64,

                65,

                66,

                67,

                68,

                69,

                70,

                71,

                72,

                73,

                74,

                75,

                76,

                77,

                78,

                79,

                80,

                81,

                82,

                83,

                84,

                85,

                86,

                87,

                88,

                89

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathFMatrix3x3Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathFMatrix3x3Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            float *value_ptr = api->GamutMathFMatrix3x3Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 9; j++)
            {
                TEST(value_ptr[j] == (float)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathFMatrix3x3Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        float *value_ptr = api->GamutMathFMatrix3x3Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }









    static PyObject *
    test_DMatrix3x4(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathDMatrix3x4_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            double components[12] = {

                    0,

                    1,

                    2,

                    3,

                    4,

                    5,

                    6,

                    7,

                    8,

                    9,

                    10,

                    11

            };
            PyObject *obj = api->GamutMathDMatrix3x4_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            double *value_ptr = api->GamutMathDMatrix3x4_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (double)0);

                TEST(value_ptr[1] == (double)1);

                TEST(value_ptr[2] == (double)2);

                TEST(value_ptr[3] == (double)3);

                TEST(value_ptr[4] == (double)4);

                TEST(value_ptr[5] == (double)5);

                TEST(value_ptr[6] == (double)6);

                TEST(value_ptr[7] == (double)7);

                TEST(value_ptr[8] == (double)8);

                TEST(value_ptr[9] == (double)9);

                TEST(value_ptr[10] == (double)10);

                TEST(value_ptr[11] == (double)11);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        double *value_ptr = api->GamutMathDMatrix3x4_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }

    static PyObject *
    test_DMatrix3x4Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathDMatrix3x4Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        double components[120] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29,

                30,

                31,

                32,

                33,

                34,

                35,

                36,

                37,

                38,

                39,

                40,

                41,

                42,

                43,

                44,

                45,

                46,

                47,

                48,

                49,

                50,

                51,

                52,

                53,

                54,

                55,

                56,

                57,

                58,

                59,

                60,

                61,

                62,

                63,

                64,

                65,

                66,

                67,

                68,

                69,

                70,

                71,

                72,

                73,

                74,

                75,

                76,

                77,

                78,

                79,

                80,

                81,

                82,

                83,

                84,

                85,

                86,

                87,

                88,

                89,

                90,

                91,

                92,

                93,

                94,

                95,

                96,

                97,

                98,

                99,

                100,

                101,

                102,

                103,

                104,

                105,

                106,

                107,

                108,

                109,

                110,

                111,

                112,

                113,

                114,

                115,

                116,

                117,

                118,

                119

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathDMatrix3x4Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathDMatrix3x4Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            double *value_ptr = api->GamutMathDMatrix3x4Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 12; j++)
            {
                TEST(value_ptr[j] == (double)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathDMatrix3x4Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        double *value_ptr = api->GamutMathDMatrix3x4Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }









    static PyObject *
    test_FMatrix3x4(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathFMatrix3x4_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            float components[12] = {

                    0,

                    1,

                    2,

                    3,

                    4,

                    5,

                    6,

                    7,

                    8,

                    9,

                    10,

                    11

            };
            PyObject *obj = api->GamutMathFMatrix3x4_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            float *value_ptr = api->GamutMathFMatrix3x4_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (float)0);

                TEST(value_ptr[1] == (float)1);

                TEST(value_ptr[2] == (float)2);

                TEST(value_ptr[3] == (float)3);

                TEST(value_ptr[4] == (float)4);

                TEST(value_ptr[5] == (float)5);

                TEST(value_ptr[6] == (float)6);

                TEST(value_ptr[7] == (float)7);

                TEST(value_ptr[8] == (float)8);

                TEST(value_ptr[9] == (float)9);

                TEST(value_ptr[10] == (float)10);

                TEST(value_ptr[11] == (float)11);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        float *value_ptr = api->GamutMathFMatrix3x4_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }

    static PyObject *
    test_FMatrix3x4Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathFMatrix3x4Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        float components[120] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29,

                30,

                31,

                32,

                33,

                34,

                35,

                36,

                37,

                38,

                39,

                40,

                41,

                42,

                43,

                44,

                45,

                46,

                47,

                48,

                49,

                50,

                51,

                52,

                53,

                54,

                55,

                56,

                57,

                58,

                59,

                60,

                61,

                62,

                63,

                64,

                65,

                66,

                67,

                68,

                69,

                70,

                71,

                72,

                73,

                74,

                75,

                76,

                77,

                78,

                79,

                80,

                81,

                82,

                83,

                84,

                85,

                86,

                87,

                88,

                89,

                90,

                91,

                92,

                93,

                94,

                95,

                96,

                97,

                98,

                99,

                100,

                101,

                102,

                103,

                104,

                105,

                106,

                107,

                108,

                109,

                110,

                111,

                112,

                113,

                114,

                115,

                116,

                117,

                118,

                119

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathFMatrix3x4Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathFMatrix3x4Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            float *value_ptr = api->GamutMathFMatrix3x4Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 12; j++)
            {
                TEST(value_ptr[j] == (float)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathFMatrix3x4Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        float *value_ptr = api->GamutMathFMatrix3x4Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }









    static PyObject *
    test_DMatrix4x2(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathDMatrix4x2_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            double components[8] = {

                    0,

                    1,

                    2,

                    3,

                    4,

                    5,

                    6,

                    7

            };
            PyObject *obj = api->GamutMathDMatrix4x2_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            double *value_ptr = api->GamutMathDMatrix4x2_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (double)0);

                TEST(value_ptr[1] == (double)1);

                TEST(value_ptr[2] == (double)2);

                TEST(value_ptr[3] == (double)3);

                TEST(value_ptr[4] == (double)4);

                TEST(value_ptr[5] == (double)5);

                TEST(value_ptr[6] == (double)6);

                TEST(value_ptr[7] == (double)7);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        double *value_ptr = api->GamutMathDMatrix4x2_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }

    static PyObject *
    test_DMatrix4x2Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathDMatrix4x2Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        double components[80] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29,

                30,

                31,

                32,

                33,

                34,

                35,

                36,

                37,

                38,

                39,

                40,

                41,

                42,

                43,

                44,

                45,

                46,

                47,

                48,

                49,

                50,

                51,

                52,

                53,

                54,

                55,

                56,

                57,

                58,

                59,

                60,

                61,

                62,

                63,

                64,

                65,

                66,

                67,

                68,

                69,

                70,

                71,

                72,

                73,

                74,

                75,

                76,

                77,

                78,

                79

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathDMatrix4x2Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathDMatrix4x2Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            double *value_ptr = api->GamutMathDMatrix4x2Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 8; j++)
            {
                TEST(value_ptr[j] == (double)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathDMatrix4x2Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        double *value_ptr = api->GamutMathDMatrix4x2Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }









    static PyObject *
    test_FMatrix4x2(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathFMatrix4x2_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            float components[8] = {

                    0,

                    1,

                    2,

                    3,

                    4,

                    5,

                    6,

                    7

            };
            PyObject *obj = api->GamutMathFMatrix4x2_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            float *value_ptr = api->GamutMathFMatrix4x2_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (float)0);

                TEST(value_ptr[1] == (float)1);

                TEST(value_ptr[2] == (float)2);

                TEST(value_ptr[3] == (float)3);

                TEST(value_ptr[4] == (float)4);

                TEST(value_ptr[5] == (float)5);

                TEST(value_ptr[6] == (float)6);

                TEST(value_ptr[7] == (float)7);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        float *value_ptr = api->GamutMathFMatrix4x2_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }

    static PyObject *
    test_FMatrix4x2Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathFMatrix4x2Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        float components[80] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29,

                30,

                31,

                32,

                33,

                34,

                35,

                36,

                37,

                38,

                39,

                40,

                41,

                42,

                43,

                44,

                45,

                46,

                47,

                48,

                49,

                50,

                51,

                52,

                53,

                54,

                55,

                56,

                57,

                58,

                59,

                60,

                61,

                62,

                63,

                64,

                65,

                66,

                67,

                68,

                69,

                70,

                71,

                72,

                73,

                74,

                75,

                76,

                77,

                78,

                79

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathFMatrix4x2Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathFMatrix4x2Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            float *value_ptr = api->GamutMathFMatrix4x2Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 8; j++)
            {
                TEST(value_ptr[j] == (float)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathFMatrix4x2Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        float *value_ptr = api->GamutMathFMatrix4x2Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }









    static PyObject *
    test_DMatrix4x3(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathDMatrix4x3_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            double components[12] = {

                    0,

                    1,

                    2,

                    3,

                    4,

                    5,

                    6,

                    7,

                    8,

                    9,

                    10,

                    11

            };
            PyObject *obj = api->GamutMathDMatrix4x3_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            double *value_ptr = api->GamutMathDMatrix4x3_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (double)0);

                TEST(value_ptr[1] == (double)1);

                TEST(value_ptr[2] == (double)2);

                TEST(value_ptr[3] == (double)3);

                TEST(value_ptr[4] == (double)4);

                TEST(value_ptr[5] == (double)5);

                TEST(value_ptr[6] == (double)6);

                TEST(value_ptr[7] == (double)7);

                TEST(value_ptr[8] == (double)8);

                TEST(value_ptr[9] == (double)9);

                TEST(value_ptr[10] == (double)10);

                TEST(value_ptr[11] == (double)11);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        double *value_ptr = api->GamutMathDMatrix4x3_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }

    static PyObject *
    test_DMatrix4x3Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathDMatrix4x3Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        double components[120] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29,

                30,

                31,

                32,

                33,

                34,

                35,

                36,

                37,

                38,

                39,

                40,

                41,

                42,

                43,

                44,

                45,

                46,

                47,

                48,

                49,

                50,

                51,

                52,

                53,

                54,

                55,

                56,

                57,

                58,

                59,

                60,

                61,

                62,

                63,

                64,

                65,

                66,

                67,

                68,

                69,

                70,

                71,

                72,

                73,

                74,

                75,

                76,

                77,

                78,

                79,

                80,

                81,

                82,

                83,

                84,

                85,

                86,

                87,

                88,

                89,

                90,

                91,

                92,

                93,

                94,

                95,

                96,

                97,

                98,

                99,

                100,

                101,

                102,

                103,

                104,

                105,

                106,

                107,

                108,

                109,

                110,

                111,

                112,

                113,

                114,

                115,

                116,

                117,

                118,

                119

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathDMatrix4x3Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathDMatrix4x3Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            double *value_ptr = api->GamutMathDMatrix4x3Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 12; j++)
            {
                TEST(value_ptr[j] == (double)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathDMatrix4x3Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        double *value_ptr = api->GamutMathDMatrix4x3Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }









    static PyObject *
    test_FMatrix4x3(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathFMatrix4x3_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            float components[12] = {

                    0,

                    1,

                    2,

                    3,

                    4,

                    5,

                    6,

                    7,

                    8,

                    9,

                    10,

                    11

            };
            PyObject *obj = api->GamutMathFMatrix4x3_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            float *value_ptr = api->GamutMathFMatrix4x3_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (float)0);

                TEST(value_ptr[1] == (float)1);

                TEST(value_ptr[2] == (float)2);

                TEST(value_ptr[3] == (float)3);

                TEST(value_ptr[4] == (float)4);

                TEST(value_ptr[5] == (float)5);

                TEST(value_ptr[6] == (float)6);

                TEST(value_ptr[7] == (float)7);

                TEST(value_ptr[8] == (float)8);

                TEST(value_ptr[9] == (float)9);

                TEST(value_ptr[10] == (float)10);

                TEST(value_ptr[11] == (float)11);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        float *value_ptr = api->GamutMathFMatrix4x3_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }

    static PyObject *
    test_FMatrix4x3Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathFMatrix4x3Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        float components[120] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29,

                30,

                31,

                32,

                33,

                34,

                35,

                36,

                37,

                38,

                39,

                40,

                41,

                42,

                43,

                44,

                45,

                46,

                47,

                48,

                49,

                50,

                51,

                52,

                53,

                54,

                55,

                56,

                57,

                58,

                59,

                60,

                61,

                62,

                63,

                64,

                65,

                66,

                67,

                68,

                69,

                70,

                71,

                72,

                73,

                74,

                75,

                76,

                77,

                78,

                79,

                80,

                81,

                82,

                83,

                84,

                85,

                86,

                87,

                88,

                89,

                90,

                91,

                92,

                93,

                94,

                95,

                96,

                97,

                98,

                99,

                100,

                101,

                102,

                103,

                104,

                105,

                106,

                107,

                108,

                109,

                110,

                111,

                112,

                113,

                114,

                115,

                116,

                117,

                118,

                119

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathFMatrix4x3Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathFMatrix4x3Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            float *value_ptr = api->GamutMathFMatrix4x3Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 12; j++)
            {
                TEST(value_ptr[j] == (float)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathFMatrix4x3Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        float *value_ptr = api->GamutMathFMatrix4x3Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }









    static PyObject *
    test_DMatrix4x4(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathDMatrix4x4_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            double components[16] = {

                    0,

                    1,

                    2,

                    3,

                    4,

                    5,

                    6,

                    7,

                    8,

                    9,

                    10,

                    11,

                    12,

                    13,

                    14,

                    15

            };
            PyObject *obj = api->GamutMathDMatrix4x4_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            double *value_ptr = api->GamutMathDMatrix4x4_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (double)0);

                TEST(value_ptr[1] == (double)1);

                TEST(value_ptr[2] == (double)2);

                TEST(value_ptr[3] == (double)3);

                TEST(value_ptr[4] == (double)4);

                TEST(value_ptr[5] == (double)5);

                TEST(value_ptr[6] == (double)6);

                TEST(value_ptr[7] == (double)7);

                TEST(value_ptr[8] == (double)8);

                TEST(value_ptr[9] == (double)9);

                TEST(value_ptr[10] == (double)10);

                TEST(value_ptr[11] == (double)11);

                TEST(value_ptr[12] == (double)12);

                TEST(value_ptr[13] == (double)13);

                TEST(value_ptr[14] == (double)14);

                TEST(value_ptr[15] == (double)15);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        double *value_ptr = api->GamutMathDMatrix4x4_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }

    static PyObject *
    test_DMatrix4x4Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathDMatrix4x4Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        double components[160] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29,

                30,

                31,

                32,

                33,

                34,

                35,

                36,

                37,

                38,

                39,

                40,

                41,

                42,

                43,

                44,

                45,

                46,

                47,

                48,

                49,

                50,

                51,

                52,

                53,

                54,

                55,

                56,

                57,

                58,

                59,

                60,

                61,

                62,

                63,

                64,

                65,

                66,

                67,

                68,

                69,

                70,

                71,

                72,

                73,

                74,

                75,

                76,

                77,

                78,

                79,

                80,

                81,

                82,

                83,

                84,

                85,

                86,

                87,

                88,

                89,

                90,

                91,

                92,

                93,

                94,

                95,

                96,

                97,

                98,

                99,

                100,

                101,

                102,

                103,

                104,

                105,

                106,

                107,

                108,

                109,

                110,

                111,

                112,

                113,

                114,

                115,

                116,

                117,

                118,

                119,

                120,

                121,

                122,

                123,

                124,

                125,

                126,

                127,

                128,

                129,

                130,

                131,

                132,

                133,

                134,

                135,

                136,

                137,

                138,

                139,

                140,

                141,

                142,

                143,

                144,

                145,

                146,

                147,

                148,

                149,

                150,

                151,

                152,

                153,

                154,

                155,

                156,

                157,

                158,

                159

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathDMatrix4x4Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathDMatrix4x4Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            double *value_ptr = api->GamutMathDMatrix4x4Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 16; j++)
            {
                TEST(value_ptr[j] == (double)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathDMatrix4x4Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        double *value_ptr = api->GamutMathDMatrix4x4Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }









    static PyObject *
    test_FMatrix4x4(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathFMatrix4x4_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            float components[16] = {

                    0,

                    1,

                    2,

                    3,

                    4,

                    5,

                    6,

                    7,

                    8,

                    9,

                    10,

                    11,

                    12,

                    13,

                    14,

                    15

            };
            PyObject *obj = api->GamutMathFMatrix4x4_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            float *value_ptr = api->GamutMathFMatrix4x4_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (float)0);

                TEST(value_ptr[1] == (float)1);

                TEST(value_ptr[2] == (float)2);

                TEST(value_ptr[3] == (float)3);

                TEST(value_ptr[4] == (float)4);

                TEST(value_ptr[5] == (float)5);

                TEST(value_ptr[6] == (float)6);

                TEST(value_ptr[7] == (float)7);

                TEST(value_ptr[8] == (float)8);

                TEST(value_ptr[9] == (float)9);

                TEST(value_ptr[10] == (float)10);

                TEST(value_ptr[11] == (float)11);

                TEST(value_ptr[12] == (float)12);

                TEST(value_ptr[13] == (float)13);

                TEST(value_ptr[14] == (float)14);

                TEST(value_ptr[15] == (float)15);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        float *value_ptr = api->GamutMathFMatrix4x4_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }

    static PyObject *
    test_FMatrix4x4Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathFMatrix4x4Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        float components[160] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29,

                30,

                31,

                32,

                33,

                34,

                35,

                36,

                37,

                38,

                39,

                40,

                41,

                42,

                43,

                44,

                45,

                46,

                47,

                48,

                49,

                50,

                51,

                52,

                53,

                54,

                55,

                56,

                57,

                58,

                59,

                60,

                61,

                62,

                63,

                64,

                65,

                66,

                67,

                68,

                69,

                70,

                71,

                72,

                73,

                74,

                75,

                76,

                77,

                78,

                79,

                80,

                81,

                82,

                83,

                84,

                85,

                86,

                87,

                88,

                89,

                90,

                91,

                92,

                93,

                94,

                95,

                96,

                97,

                98,

                99,

                100,

                101,

                102,

                103,

                104,

                105,

                106,

                107,

                108,

                109,

                110,

                111,

                112,

                113,

                114,

                115,

                116,

                117,

                118,

                119,

                120,

                121,

                122,

                123,

                124,

                125,

                126,

                127,

                128,

                129,

                130,

                131,

                132,

                133,

                134,

                135,

                136,

                137,

                138,

                139,

                140,

                141,

                142,

                143,

                144,

                145,

                146,

                147,

                148,

                149,

                150,

                151,

                152,

                153,

                154,

                155,

                156,

                157,

                158,

                159

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathFMatrix4x4Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathFMatrix4x4Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            float *value_ptr = api->GamutMathFMatrix4x4Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 16; j++)
            {
                TEST(value_ptr[j] == (float)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathFMatrix4x4Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        float *value_ptr = api->GamutMathFMatrix4x4Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }









    static PyObject *
    test_BArray(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathBArray_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        bool components[10] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathBArray_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathBArray_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            bool *value_ptr = api->GamutMathBArray_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i; j++)
            {
                TEST(value_ptr[j] == (bool)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathBArray_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        bool *value_ptr = api->GamutMathBArray_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }



    static PyObject *
    test_DArray(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathDArray_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        double components[10] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathDArray_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathDArray_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            double *value_ptr = api->GamutMathDArray_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i; j++)
            {
                TEST(value_ptr[j] == (double)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathDArray_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        double *value_ptr = api->GamutMathDArray_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }



    static PyObject *
    test_FArray(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathFArray_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        float components[10] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathFArray_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathFArray_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            float *value_ptr = api->GamutMathFArray_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i; j++)
            {
                TEST(value_ptr[j] == (float)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathFArray_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        float *value_ptr = api->GamutMathFArray_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }



    static PyObject *
    test_I8Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathI8Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        int8_t components[10] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathI8Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathI8Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            int8_t *value_ptr = api->GamutMathI8Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i; j++)
            {
                TEST(value_ptr[j] == (int8_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathI8Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        int8_t *value_ptr = api->GamutMathI8Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }



    static PyObject *
    test_U8Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathU8Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        uint8_t components[10] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathU8Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathU8Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            uint8_t *value_ptr = api->GamutMathU8Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i; j++)
            {
                TEST(value_ptr[j] == (uint8_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathU8Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        uint8_t *value_ptr = api->GamutMathU8Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }



    static PyObject *
    test_I16Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathI16Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        int16_t components[10] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathI16Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathI16Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            int16_t *value_ptr = api->GamutMathI16Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i; j++)
            {
                TEST(value_ptr[j] == (int16_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathI16Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        int16_t *value_ptr = api->GamutMathI16Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }



    static PyObject *
    test_U16Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathU16Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        uint16_t components[10] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathU16Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathU16Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            uint16_t *value_ptr = api->GamutMathU16Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i; j++)
            {
                TEST(value_ptr[j] == (uint16_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathU16Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        uint16_t *value_ptr = api->GamutMathU16Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }



    static PyObject *
    test_I32Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathI32Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        int32_t components[10] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathI32Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathI32Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            int32_t *value_ptr = api->GamutMathI32Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i; j++)
            {
                TEST(value_ptr[j] == (int32_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathI32Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        int32_t *value_ptr = api->GamutMathI32Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }



    static PyObject *
    test_U32Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathU32Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        uint32_t components[10] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathU32Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathU32Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            uint32_t *value_ptr = api->GamutMathU32Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i; j++)
            {
                TEST(value_ptr[j] == (uint32_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathU32Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        uint32_t *value_ptr = api->GamutMathU32Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }



    static PyObject *
    test_IArray(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathIArray_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        int components[10] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathIArray_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathIArray_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            int *value_ptr = api->GamutMathIArray_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i; j++)
            {
                TEST(value_ptr[j] == (int)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathIArray_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        int *value_ptr = api->GamutMathIArray_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }



    static PyObject *
    test_UArray(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathUArray_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        unsigned int components[10] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathUArray_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathUArray_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            unsigned int *value_ptr = api->GamutMathUArray_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i; j++)
            {
                TEST(value_ptr[j] == (unsigned int)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathUArray_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        unsigned int *value_ptr = api->GamutMathUArray_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }



    static PyObject *
    test_I64Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathI64Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        int64_t components[10] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathI64Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathI64Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            int64_t *value_ptr = api->GamutMathI64Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i; j++)
            {
                TEST(value_ptr[j] == (int64_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathI64Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        int64_t *value_ptr = api->GamutMathI64Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }



    static PyObject *
    test_U64Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMathU64Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        uint64_t components[10] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMathU64Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMathU64Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            uint64_t *value_ptr = api->GamutMathU64Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i; j++)
            {
                TEST(value_ptr[j] == (uint64_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMathU64Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        uint64_t *value_ptr = api->GamutMathU64Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }




static PyMethodDef module_methods[] = {
    {"test_GamutMathApi_Get", test_GamutMathApi_Get, METH_NOARGS, 0},

        {"test_BVector2", test_BVector2, METH_NOARGS, 0},
        {"test_BVector2Array", test_BVector2Array, METH_NOARGS, 0},

        {"test_DVector2", test_DVector2, METH_NOARGS, 0},
        {"test_DVector2Array", test_DVector2Array, METH_NOARGS, 0},

        {"test_FVector2", test_FVector2, METH_NOARGS, 0},
        {"test_FVector2Array", test_FVector2Array, METH_NOARGS, 0},

        {"test_I8Vector2", test_I8Vector2, METH_NOARGS, 0},
        {"test_I8Vector2Array", test_I8Vector2Array, METH_NOARGS, 0},

        {"test_U8Vector2", test_U8Vector2, METH_NOARGS, 0},
        {"test_U8Vector2Array", test_U8Vector2Array, METH_NOARGS, 0},

        {"test_I16Vector2", test_I16Vector2, METH_NOARGS, 0},
        {"test_I16Vector2Array", test_I16Vector2Array, METH_NOARGS, 0},

        {"test_U16Vector2", test_U16Vector2, METH_NOARGS, 0},
        {"test_U16Vector2Array", test_U16Vector2Array, METH_NOARGS, 0},

        {"test_I32Vector2", test_I32Vector2, METH_NOARGS, 0},
        {"test_I32Vector2Array", test_I32Vector2Array, METH_NOARGS, 0},

        {"test_U32Vector2", test_U32Vector2, METH_NOARGS, 0},
        {"test_U32Vector2Array", test_U32Vector2Array, METH_NOARGS, 0},

        {"test_IVector2", test_IVector2, METH_NOARGS, 0},
        {"test_IVector2Array", test_IVector2Array, METH_NOARGS, 0},

        {"test_UVector2", test_UVector2, METH_NOARGS, 0},
        {"test_UVector2Array", test_UVector2Array, METH_NOARGS, 0},

        {"test_I64Vector2", test_I64Vector2, METH_NOARGS, 0},
        {"test_I64Vector2Array", test_I64Vector2Array, METH_NOARGS, 0},

        {"test_U64Vector2", test_U64Vector2, METH_NOARGS, 0},
        {"test_U64Vector2Array", test_U64Vector2Array, METH_NOARGS, 0},

        {"test_BVector3", test_BVector3, METH_NOARGS, 0},
        {"test_BVector3Array", test_BVector3Array, METH_NOARGS, 0},

        {"test_DVector3", test_DVector3, METH_NOARGS, 0},
        {"test_DVector3Array", test_DVector3Array, METH_NOARGS, 0},

        {"test_FVector3", test_FVector3, METH_NOARGS, 0},
        {"test_FVector3Array", test_FVector3Array, METH_NOARGS, 0},

        {"test_I8Vector3", test_I8Vector3, METH_NOARGS, 0},
        {"test_I8Vector3Array", test_I8Vector3Array, METH_NOARGS, 0},

        {"test_U8Vector3", test_U8Vector3, METH_NOARGS, 0},
        {"test_U8Vector3Array", test_U8Vector3Array, METH_NOARGS, 0},

        {"test_I16Vector3", test_I16Vector3, METH_NOARGS, 0},
        {"test_I16Vector3Array", test_I16Vector3Array, METH_NOARGS, 0},

        {"test_U16Vector3", test_U16Vector3, METH_NOARGS, 0},
        {"test_U16Vector3Array", test_U16Vector3Array, METH_NOARGS, 0},

        {"test_I32Vector3", test_I32Vector3, METH_NOARGS, 0},
        {"test_I32Vector3Array", test_I32Vector3Array, METH_NOARGS, 0},

        {"test_U32Vector3", test_U32Vector3, METH_NOARGS, 0},
        {"test_U32Vector3Array", test_U32Vector3Array, METH_NOARGS, 0},

        {"test_IVector3", test_IVector3, METH_NOARGS, 0},
        {"test_IVector3Array", test_IVector3Array, METH_NOARGS, 0},

        {"test_UVector3", test_UVector3, METH_NOARGS, 0},
        {"test_UVector3Array", test_UVector3Array, METH_NOARGS, 0},

        {"test_I64Vector3", test_I64Vector3, METH_NOARGS, 0},
        {"test_I64Vector3Array", test_I64Vector3Array, METH_NOARGS, 0},

        {"test_U64Vector3", test_U64Vector3, METH_NOARGS, 0},
        {"test_U64Vector3Array", test_U64Vector3Array, METH_NOARGS, 0},

        {"test_BVector4", test_BVector4, METH_NOARGS, 0},
        {"test_BVector4Array", test_BVector4Array, METH_NOARGS, 0},

        {"test_DVector4", test_DVector4, METH_NOARGS, 0},
        {"test_DVector4Array", test_DVector4Array, METH_NOARGS, 0},

        {"test_FVector4", test_FVector4, METH_NOARGS, 0},
        {"test_FVector4Array", test_FVector4Array, METH_NOARGS, 0},

        {"test_I8Vector4", test_I8Vector4, METH_NOARGS, 0},
        {"test_I8Vector4Array", test_I8Vector4Array, METH_NOARGS, 0},

        {"test_U8Vector4", test_U8Vector4, METH_NOARGS, 0},
        {"test_U8Vector4Array", test_U8Vector4Array, METH_NOARGS, 0},

        {"test_I16Vector4", test_I16Vector4, METH_NOARGS, 0},
        {"test_I16Vector4Array", test_I16Vector4Array, METH_NOARGS, 0},

        {"test_U16Vector4", test_U16Vector4, METH_NOARGS, 0},
        {"test_U16Vector4Array", test_U16Vector4Array, METH_NOARGS, 0},

        {"test_I32Vector4", test_I32Vector4, METH_NOARGS, 0},
        {"test_I32Vector4Array", test_I32Vector4Array, METH_NOARGS, 0},

        {"test_U32Vector4", test_U32Vector4, METH_NOARGS, 0},
        {"test_U32Vector4Array", test_U32Vector4Array, METH_NOARGS, 0},

        {"test_IVector4", test_IVector4, METH_NOARGS, 0},
        {"test_IVector4Array", test_IVector4Array, METH_NOARGS, 0},

        {"test_UVector4", test_UVector4, METH_NOARGS, 0},
        {"test_UVector4Array", test_UVector4Array, METH_NOARGS, 0},

        {"test_I64Vector4", test_I64Vector4, METH_NOARGS, 0},
        {"test_I64Vector4Array", test_I64Vector4Array, METH_NOARGS, 0},

        {"test_U64Vector4", test_U64Vector4, METH_NOARGS, 0},
        {"test_U64Vector4Array", test_U64Vector4Array, METH_NOARGS, 0},


        {"test_DMatrix2x2", test_DMatrix2x2, METH_NOARGS, 0},
        {"test_DMatrix2x2Array", test_DMatrix2x2Array, METH_NOARGS, 0},

        {"test_FMatrix2x2", test_FMatrix2x2, METH_NOARGS, 0},
        {"test_FMatrix2x2Array", test_FMatrix2x2Array, METH_NOARGS, 0},

        {"test_DMatrix2x3", test_DMatrix2x3, METH_NOARGS, 0},
        {"test_DMatrix2x3Array", test_DMatrix2x3Array, METH_NOARGS, 0},

        {"test_FMatrix2x3", test_FMatrix2x3, METH_NOARGS, 0},
        {"test_FMatrix2x3Array", test_FMatrix2x3Array, METH_NOARGS, 0},

        {"test_DMatrix2x4", test_DMatrix2x4, METH_NOARGS, 0},
        {"test_DMatrix2x4Array", test_DMatrix2x4Array, METH_NOARGS, 0},

        {"test_FMatrix2x4", test_FMatrix2x4, METH_NOARGS, 0},
        {"test_FMatrix2x4Array", test_FMatrix2x4Array, METH_NOARGS, 0},

        {"test_DMatrix3x2", test_DMatrix3x2, METH_NOARGS, 0},
        {"test_DMatrix3x2Array", test_DMatrix3x2Array, METH_NOARGS, 0},

        {"test_FMatrix3x2", test_FMatrix3x2, METH_NOARGS, 0},
        {"test_FMatrix3x2Array", test_FMatrix3x2Array, METH_NOARGS, 0},

        {"test_DMatrix3x3", test_DMatrix3x3, METH_NOARGS, 0},
        {"test_DMatrix3x3Array", test_DMatrix3x3Array, METH_NOARGS, 0},

        {"test_FMatrix3x3", test_FMatrix3x3, METH_NOARGS, 0},
        {"test_FMatrix3x3Array", test_FMatrix3x3Array, METH_NOARGS, 0},

        {"test_DMatrix3x4", test_DMatrix3x4, METH_NOARGS, 0},
        {"test_DMatrix3x4Array", test_DMatrix3x4Array, METH_NOARGS, 0},

        {"test_FMatrix3x4", test_FMatrix3x4, METH_NOARGS, 0},
        {"test_FMatrix3x4Array", test_FMatrix3x4Array, METH_NOARGS, 0},

        {"test_DMatrix4x2", test_DMatrix4x2, METH_NOARGS, 0},
        {"test_DMatrix4x2Array", test_DMatrix4x2Array, METH_NOARGS, 0},

        {"test_FMatrix4x2", test_FMatrix4x2, METH_NOARGS, 0},
        {"test_FMatrix4x2Array", test_FMatrix4x2Array, METH_NOARGS, 0},

        {"test_DMatrix4x3", test_DMatrix4x3, METH_NOARGS, 0},
        {"test_DMatrix4x3Array", test_DMatrix4x3Array, METH_NOARGS, 0},

        {"test_FMatrix4x3", test_FMatrix4x3, METH_NOARGS, 0},
        {"test_FMatrix4x3Array", test_FMatrix4x3Array, METH_NOARGS, 0},

        {"test_DMatrix4x4", test_DMatrix4x4, METH_NOARGS, 0},
        {"test_DMatrix4x4Array", test_DMatrix4x4Array, METH_NOARGS, 0},

        {"test_FMatrix4x4", test_FMatrix4x4, METH_NOARGS, 0},
        {"test_FMatrix4x4Array", test_FMatrix4x4Array, METH_NOARGS, 0},


        {"test_BArray", test_BArray, METH_NOARGS, 0},

        {"test_DArray", test_DArray, METH_NOARGS, 0},

        {"test_FArray", test_FArray, METH_NOARGS, 0},

        {"test_I8Array", test_I8Array, METH_NOARGS, 0},

        {"test_U8Array", test_U8Array, METH_NOARGS, 0},

        {"test_I16Array", test_I16Array, METH_NOARGS, 0},

        {"test_U16Array", test_U16Array, METH_NOARGS, 0},

        {"test_I32Array", test_I32Array, METH_NOARGS, 0},

        {"test_U32Array", test_U32Array, METH_NOARGS, 0},

        {"test_IArray", test_IArray, METH_NOARGS, 0},

        {"test_UArray", test_UArray, METH_NOARGS, 0},

        {"test_I64Array", test_I64Array, METH_NOARGS, 0},

        {"test_U64Array", test_U64Array, METH_NOARGS, 0},

    {0, 0, 0, 0}
};


static struct PyModuleDef module_PyModuleDef = {
    PyModuleDef_HEAD_INIT,
    "gamut.math._test_api",
    0,
    0,
    module_methods,
    0,
    0,
    0
};


PyMODINIT_FUNC
PyInit__test_api()
{
    return PyModule_Create(&module_PyModuleDef);
}