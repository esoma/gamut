
// generated 2022-03-12 02:15:25.040287 from codegen/math/templates/_math.cpp

// python
#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <structmember.h>

#include "_modulestate.hpp"

    #include "_bvector2.hpp"

    #include "_dvector2.hpp"

    #include "_fvector2.hpp"

    #include "_i8vector2.hpp"

    #include "_u8vector2.hpp"

    #include "_i16vector2.hpp"

    #include "_u16vector2.hpp"

    #include "_i32vector2.hpp"

    #include "_u32vector2.hpp"

    #include "_ivector2.hpp"

    #include "_uvector2.hpp"

    #include "_i64vector2.hpp"

    #include "_u64vector2.hpp"

    #include "_bvector3.hpp"

    #include "_dvector3.hpp"

    #include "_fvector3.hpp"

    #include "_i8vector3.hpp"

    #include "_u8vector3.hpp"

    #include "_i16vector3.hpp"

    #include "_u16vector3.hpp"

    #include "_i32vector3.hpp"

    #include "_u32vector3.hpp"

    #include "_ivector3.hpp"

    #include "_uvector3.hpp"

    #include "_i64vector3.hpp"

    #include "_u64vector3.hpp"

    #include "_bvector4.hpp"

    #include "_dvector4.hpp"

    #include "_fvector4.hpp"

    #include "_i8vector4.hpp"

    #include "_u8vector4.hpp"

    #include "_i16vector4.hpp"

    #include "_u16vector4.hpp"

    #include "_i32vector4.hpp"

    #include "_u32vector4.hpp"

    #include "_ivector4.hpp"

    #include "_uvector4.hpp"

    #include "_i64vector4.hpp"

    #include "_u64vector4.hpp"


    #include "_dmatrix2x2.hpp"

    #include "_fmatrix2x2.hpp"

    #include "_dmatrix2x3.hpp"

    #include "_fmatrix2x3.hpp"

    #include "_dmatrix2x4.hpp"

    #include "_fmatrix2x4.hpp"

    #include "_dmatrix3x2.hpp"

    #include "_fmatrix3x2.hpp"

    #include "_dmatrix3x3.hpp"

    #include "_fmatrix3x3.hpp"

    #include "_dmatrix3x4.hpp"

    #include "_fmatrix3x4.hpp"

    #include "_dmatrix4x2.hpp"

    #include "_fmatrix4x2.hpp"

    #include "_dmatrix4x3.hpp"

    #include "_fmatrix4x3.hpp"

    #include "_dmatrix4x4.hpp"

    #include "_fmatrix4x4.hpp"


    #include "_b.hpp"

    #include "_d.hpp"

    #include "_f.hpp"

    #include "_i8.hpp"

    #include "_u8.hpp"

    #include "_i16.hpp"

    #include "_u16.hpp"

    #include "_i32.hpp"

    #include "_u32.hpp"

    #include "_i.hpp"

    #include "_u.hpp"

    #include "_i64.hpp"

    #include "_u64.hpp"

#include "gamut/math.h"


static PyMethodDef module_methods[] = {
    {0, 0, 0, 0}
};


static int
module_traverse(PyObject *self, visitproc visit, void *arg)
{
    ModuleState *state = (ModuleState *)PyModule_GetState(self);
    return ModuleState_traverse(state, visit, arg);
}


static int
module_clear(PyObject *self)
{
    ModuleState *state = (ModuleState *)PyModule_GetState(self);
    return ModuleState_clear(state);
}


static struct PyModuleDef module_PyModuleDef = {
    PyModuleDef_HEAD_INIT,
    "gamut.math._math",
    0,
    sizeof(struct ModuleState),
    module_methods,
    0,
    module_traverse,
    module_clear
};


static void
api_destructor(PyObject *capsule)
{
    GamutMathApi* api = (GamutMathApi*)PyCapsule_GetPointer(
        capsule,
        "gamut.math._math._api"
    );
    delete api;
}


PyMODINIT_FUNC
PyInit__math()
{
    auto api = new GamutMathApi;
    auto api_capsule = PyCapsule_New(
        (void *)api,
        "gamut.math._math._api",
        NULL
    );

    PyObject *module = PyModule_Create(&module_PyModuleDef);
    ModuleState *state = 0;
    if (!module){ goto error; }
    if (PyState_AddModule(module, &module_PyModuleDef) == -1){ goto error; }
    state = (ModuleState *)PyModule_GetState(module);


        {
            PyTypeObject *type = define_BVector2_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->BVector2_PyTypeObject = type;
        }
        {
            PyTypeObject *type = define_BVector2Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->BVector2Array_PyTypeObject = type;
        }
        api->GamutMathBVector2_GetType = get_BVector2_type;
        api->GamutMathBVector2Array_GetType = get_BVector2Array_type;
        api->GamutMathBVector2_Create = create_BVector2;
        api->GamutMathBVector2Array_Create = create_BVector2Array;
        api->GamutMathBVector2_GetValuePointer = get_BVector2_value_ptr;
        api->GamutMathBVector2Array_GetValuePointer = get_BVector2Array_value_ptr;
        api->GamutMathBVector2Array_GetLength = get_BVector2Array_length;

        {
            PyTypeObject *type = define_DVector2_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->DVector2_PyTypeObject = type;
        }
        {
            PyTypeObject *type = define_DVector2Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->DVector2Array_PyTypeObject = type;
        }
        api->GamutMathDVector2_GetType = get_DVector2_type;
        api->GamutMathDVector2Array_GetType = get_DVector2Array_type;
        api->GamutMathDVector2_Create = create_DVector2;
        api->GamutMathDVector2Array_Create = create_DVector2Array;
        api->GamutMathDVector2_GetValuePointer = get_DVector2_value_ptr;
        api->GamutMathDVector2Array_GetValuePointer = get_DVector2Array_value_ptr;
        api->GamutMathDVector2Array_GetLength = get_DVector2Array_length;

        {
            PyTypeObject *type = define_FVector2_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->FVector2_PyTypeObject = type;
        }
        {
            PyTypeObject *type = define_FVector2Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->FVector2Array_PyTypeObject = type;
        }
        api->GamutMathFVector2_GetType = get_FVector2_type;
        api->GamutMathFVector2Array_GetType = get_FVector2Array_type;
        api->GamutMathFVector2_Create = create_FVector2;
        api->GamutMathFVector2Array_Create = create_FVector2Array;
        api->GamutMathFVector2_GetValuePointer = get_FVector2_value_ptr;
        api->GamutMathFVector2Array_GetValuePointer = get_FVector2Array_value_ptr;
        api->GamutMathFVector2Array_GetLength = get_FVector2Array_length;

        {
            PyTypeObject *type = define_I8Vector2_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->I8Vector2_PyTypeObject = type;
        }
        {
            PyTypeObject *type = define_I8Vector2Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->I8Vector2Array_PyTypeObject = type;
        }
        api->GamutMathI8Vector2_GetType = get_I8Vector2_type;
        api->GamutMathI8Vector2Array_GetType = get_I8Vector2Array_type;
        api->GamutMathI8Vector2_Create = create_I8Vector2;
        api->GamutMathI8Vector2Array_Create = create_I8Vector2Array;
        api->GamutMathI8Vector2_GetValuePointer = get_I8Vector2_value_ptr;
        api->GamutMathI8Vector2Array_GetValuePointer = get_I8Vector2Array_value_ptr;
        api->GamutMathI8Vector2Array_GetLength = get_I8Vector2Array_length;

        {
            PyTypeObject *type = define_U8Vector2_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->U8Vector2_PyTypeObject = type;
        }
        {
            PyTypeObject *type = define_U8Vector2Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->U8Vector2Array_PyTypeObject = type;
        }
        api->GamutMathU8Vector2_GetType = get_U8Vector2_type;
        api->GamutMathU8Vector2Array_GetType = get_U8Vector2Array_type;
        api->GamutMathU8Vector2_Create = create_U8Vector2;
        api->GamutMathU8Vector2Array_Create = create_U8Vector2Array;
        api->GamutMathU8Vector2_GetValuePointer = get_U8Vector2_value_ptr;
        api->GamutMathU8Vector2Array_GetValuePointer = get_U8Vector2Array_value_ptr;
        api->GamutMathU8Vector2Array_GetLength = get_U8Vector2Array_length;

        {
            PyTypeObject *type = define_I16Vector2_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->I16Vector2_PyTypeObject = type;
        }
        {
            PyTypeObject *type = define_I16Vector2Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->I16Vector2Array_PyTypeObject = type;
        }
        api->GamutMathI16Vector2_GetType = get_I16Vector2_type;
        api->GamutMathI16Vector2Array_GetType = get_I16Vector2Array_type;
        api->GamutMathI16Vector2_Create = create_I16Vector2;
        api->GamutMathI16Vector2Array_Create = create_I16Vector2Array;
        api->GamutMathI16Vector2_GetValuePointer = get_I16Vector2_value_ptr;
        api->GamutMathI16Vector2Array_GetValuePointer = get_I16Vector2Array_value_ptr;
        api->GamutMathI16Vector2Array_GetLength = get_I16Vector2Array_length;

        {
            PyTypeObject *type = define_U16Vector2_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->U16Vector2_PyTypeObject = type;
        }
        {
            PyTypeObject *type = define_U16Vector2Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->U16Vector2Array_PyTypeObject = type;
        }
        api->GamutMathU16Vector2_GetType = get_U16Vector2_type;
        api->GamutMathU16Vector2Array_GetType = get_U16Vector2Array_type;
        api->GamutMathU16Vector2_Create = create_U16Vector2;
        api->GamutMathU16Vector2Array_Create = create_U16Vector2Array;
        api->GamutMathU16Vector2_GetValuePointer = get_U16Vector2_value_ptr;
        api->GamutMathU16Vector2Array_GetValuePointer = get_U16Vector2Array_value_ptr;
        api->GamutMathU16Vector2Array_GetLength = get_U16Vector2Array_length;

        {
            PyTypeObject *type = define_I32Vector2_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->I32Vector2_PyTypeObject = type;
        }
        {
            PyTypeObject *type = define_I32Vector2Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->I32Vector2Array_PyTypeObject = type;
        }
        api->GamutMathI32Vector2_GetType = get_I32Vector2_type;
        api->GamutMathI32Vector2Array_GetType = get_I32Vector2Array_type;
        api->GamutMathI32Vector2_Create = create_I32Vector2;
        api->GamutMathI32Vector2Array_Create = create_I32Vector2Array;
        api->GamutMathI32Vector2_GetValuePointer = get_I32Vector2_value_ptr;
        api->GamutMathI32Vector2Array_GetValuePointer = get_I32Vector2Array_value_ptr;
        api->GamutMathI32Vector2Array_GetLength = get_I32Vector2Array_length;

        {
            PyTypeObject *type = define_U32Vector2_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->U32Vector2_PyTypeObject = type;
        }
        {
            PyTypeObject *type = define_U32Vector2Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->U32Vector2Array_PyTypeObject = type;
        }
        api->GamutMathU32Vector2_GetType = get_U32Vector2_type;
        api->GamutMathU32Vector2Array_GetType = get_U32Vector2Array_type;
        api->GamutMathU32Vector2_Create = create_U32Vector2;
        api->GamutMathU32Vector2Array_Create = create_U32Vector2Array;
        api->GamutMathU32Vector2_GetValuePointer = get_U32Vector2_value_ptr;
        api->GamutMathU32Vector2Array_GetValuePointer = get_U32Vector2Array_value_ptr;
        api->GamutMathU32Vector2Array_GetLength = get_U32Vector2Array_length;

        {
            PyTypeObject *type = define_IVector2_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->IVector2_PyTypeObject = type;
        }
        {
            PyTypeObject *type = define_IVector2Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->IVector2Array_PyTypeObject = type;
        }
        api->GamutMathIVector2_GetType = get_IVector2_type;
        api->GamutMathIVector2Array_GetType = get_IVector2Array_type;
        api->GamutMathIVector2_Create = create_IVector2;
        api->GamutMathIVector2Array_Create = create_IVector2Array;
        api->GamutMathIVector2_GetValuePointer = get_IVector2_value_ptr;
        api->GamutMathIVector2Array_GetValuePointer = get_IVector2Array_value_ptr;
        api->GamutMathIVector2Array_GetLength = get_IVector2Array_length;

        {
            PyTypeObject *type = define_UVector2_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->UVector2_PyTypeObject = type;
        }
        {
            PyTypeObject *type = define_UVector2Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->UVector2Array_PyTypeObject = type;
        }
        api->GamutMathUVector2_GetType = get_UVector2_type;
        api->GamutMathUVector2Array_GetType = get_UVector2Array_type;
        api->GamutMathUVector2_Create = create_UVector2;
        api->GamutMathUVector2Array_Create = create_UVector2Array;
        api->GamutMathUVector2_GetValuePointer = get_UVector2_value_ptr;
        api->GamutMathUVector2Array_GetValuePointer = get_UVector2Array_value_ptr;
        api->GamutMathUVector2Array_GetLength = get_UVector2Array_length;

        {
            PyTypeObject *type = define_I64Vector2_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->I64Vector2_PyTypeObject = type;
        }
        {
            PyTypeObject *type = define_I64Vector2Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->I64Vector2Array_PyTypeObject = type;
        }
        api->GamutMathI64Vector2_GetType = get_I64Vector2_type;
        api->GamutMathI64Vector2Array_GetType = get_I64Vector2Array_type;
        api->GamutMathI64Vector2_Create = create_I64Vector2;
        api->GamutMathI64Vector2Array_Create = create_I64Vector2Array;
        api->GamutMathI64Vector2_GetValuePointer = get_I64Vector2_value_ptr;
        api->GamutMathI64Vector2Array_GetValuePointer = get_I64Vector2Array_value_ptr;
        api->GamutMathI64Vector2Array_GetLength = get_I64Vector2Array_length;

        {
            PyTypeObject *type = define_U64Vector2_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->U64Vector2_PyTypeObject = type;
        }
        {
            PyTypeObject *type = define_U64Vector2Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->U64Vector2Array_PyTypeObject = type;
        }
        api->GamutMathU64Vector2_GetType = get_U64Vector2_type;
        api->GamutMathU64Vector2Array_GetType = get_U64Vector2Array_type;
        api->GamutMathU64Vector2_Create = create_U64Vector2;
        api->GamutMathU64Vector2Array_Create = create_U64Vector2Array;
        api->GamutMathU64Vector2_GetValuePointer = get_U64Vector2_value_ptr;
        api->GamutMathU64Vector2Array_GetValuePointer = get_U64Vector2Array_value_ptr;
        api->GamutMathU64Vector2Array_GetLength = get_U64Vector2Array_length;

        {
            PyTypeObject *type = define_BVector3_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->BVector3_PyTypeObject = type;
        }
        {
            PyTypeObject *type = define_BVector3Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->BVector3Array_PyTypeObject = type;
        }
        api->GamutMathBVector3_GetType = get_BVector3_type;
        api->GamutMathBVector3Array_GetType = get_BVector3Array_type;
        api->GamutMathBVector3_Create = create_BVector3;
        api->GamutMathBVector3Array_Create = create_BVector3Array;
        api->GamutMathBVector3_GetValuePointer = get_BVector3_value_ptr;
        api->GamutMathBVector3Array_GetValuePointer = get_BVector3Array_value_ptr;
        api->GamutMathBVector3Array_GetLength = get_BVector3Array_length;

        {
            PyTypeObject *type = define_DVector3_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->DVector3_PyTypeObject = type;
        }
        {
            PyTypeObject *type = define_DVector3Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->DVector3Array_PyTypeObject = type;
        }
        api->GamutMathDVector3_GetType = get_DVector3_type;
        api->GamutMathDVector3Array_GetType = get_DVector3Array_type;
        api->GamutMathDVector3_Create = create_DVector3;
        api->GamutMathDVector3Array_Create = create_DVector3Array;
        api->GamutMathDVector3_GetValuePointer = get_DVector3_value_ptr;
        api->GamutMathDVector3Array_GetValuePointer = get_DVector3Array_value_ptr;
        api->GamutMathDVector3Array_GetLength = get_DVector3Array_length;

        {
            PyTypeObject *type = define_FVector3_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->FVector3_PyTypeObject = type;
        }
        {
            PyTypeObject *type = define_FVector3Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->FVector3Array_PyTypeObject = type;
        }
        api->GamutMathFVector3_GetType = get_FVector3_type;
        api->GamutMathFVector3Array_GetType = get_FVector3Array_type;
        api->GamutMathFVector3_Create = create_FVector3;
        api->GamutMathFVector3Array_Create = create_FVector3Array;
        api->GamutMathFVector3_GetValuePointer = get_FVector3_value_ptr;
        api->GamutMathFVector3Array_GetValuePointer = get_FVector3Array_value_ptr;
        api->GamutMathFVector3Array_GetLength = get_FVector3Array_length;

        {
            PyTypeObject *type = define_I8Vector3_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->I8Vector3_PyTypeObject = type;
        }
        {
            PyTypeObject *type = define_I8Vector3Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->I8Vector3Array_PyTypeObject = type;
        }
        api->GamutMathI8Vector3_GetType = get_I8Vector3_type;
        api->GamutMathI8Vector3Array_GetType = get_I8Vector3Array_type;
        api->GamutMathI8Vector3_Create = create_I8Vector3;
        api->GamutMathI8Vector3Array_Create = create_I8Vector3Array;
        api->GamutMathI8Vector3_GetValuePointer = get_I8Vector3_value_ptr;
        api->GamutMathI8Vector3Array_GetValuePointer = get_I8Vector3Array_value_ptr;
        api->GamutMathI8Vector3Array_GetLength = get_I8Vector3Array_length;

        {
            PyTypeObject *type = define_U8Vector3_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->U8Vector3_PyTypeObject = type;
        }
        {
            PyTypeObject *type = define_U8Vector3Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->U8Vector3Array_PyTypeObject = type;
        }
        api->GamutMathU8Vector3_GetType = get_U8Vector3_type;
        api->GamutMathU8Vector3Array_GetType = get_U8Vector3Array_type;
        api->GamutMathU8Vector3_Create = create_U8Vector3;
        api->GamutMathU8Vector3Array_Create = create_U8Vector3Array;
        api->GamutMathU8Vector3_GetValuePointer = get_U8Vector3_value_ptr;
        api->GamutMathU8Vector3Array_GetValuePointer = get_U8Vector3Array_value_ptr;
        api->GamutMathU8Vector3Array_GetLength = get_U8Vector3Array_length;

        {
            PyTypeObject *type = define_I16Vector3_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->I16Vector3_PyTypeObject = type;
        }
        {
            PyTypeObject *type = define_I16Vector3Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->I16Vector3Array_PyTypeObject = type;
        }
        api->GamutMathI16Vector3_GetType = get_I16Vector3_type;
        api->GamutMathI16Vector3Array_GetType = get_I16Vector3Array_type;
        api->GamutMathI16Vector3_Create = create_I16Vector3;
        api->GamutMathI16Vector3Array_Create = create_I16Vector3Array;
        api->GamutMathI16Vector3_GetValuePointer = get_I16Vector3_value_ptr;
        api->GamutMathI16Vector3Array_GetValuePointer = get_I16Vector3Array_value_ptr;
        api->GamutMathI16Vector3Array_GetLength = get_I16Vector3Array_length;

        {
            PyTypeObject *type = define_U16Vector3_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->U16Vector3_PyTypeObject = type;
        }
        {
            PyTypeObject *type = define_U16Vector3Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->U16Vector3Array_PyTypeObject = type;
        }
        api->GamutMathU16Vector3_GetType = get_U16Vector3_type;
        api->GamutMathU16Vector3Array_GetType = get_U16Vector3Array_type;
        api->GamutMathU16Vector3_Create = create_U16Vector3;
        api->GamutMathU16Vector3Array_Create = create_U16Vector3Array;
        api->GamutMathU16Vector3_GetValuePointer = get_U16Vector3_value_ptr;
        api->GamutMathU16Vector3Array_GetValuePointer = get_U16Vector3Array_value_ptr;
        api->GamutMathU16Vector3Array_GetLength = get_U16Vector3Array_length;

        {
            PyTypeObject *type = define_I32Vector3_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->I32Vector3_PyTypeObject = type;
        }
        {
            PyTypeObject *type = define_I32Vector3Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->I32Vector3Array_PyTypeObject = type;
        }
        api->GamutMathI32Vector3_GetType = get_I32Vector3_type;
        api->GamutMathI32Vector3Array_GetType = get_I32Vector3Array_type;
        api->GamutMathI32Vector3_Create = create_I32Vector3;
        api->GamutMathI32Vector3Array_Create = create_I32Vector3Array;
        api->GamutMathI32Vector3_GetValuePointer = get_I32Vector3_value_ptr;
        api->GamutMathI32Vector3Array_GetValuePointer = get_I32Vector3Array_value_ptr;
        api->GamutMathI32Vector3Array_GetLength = get_I32Vector3Array_length;

        {
            PyTypeObject *type = define_U32Vector3_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->U32Vector3_PyTypeObject = type;
        }
        {
            PyTypeObject *type = define_U32Vector3Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->U32Vector3Array_PyTypeObject = type;
        }
        api->GamutMathU32Vector3_GetType = get_U32Vector3_type;
        api->GamutMathU32Vector3Array_GetType = get_U32Vector3Array_type;
        api->GamutMathU32Vector3_Create = create_U32Vector3;
        api->GamutMathU32Vector3Array_Create = create_U32Vector3Array;
        api->GamutMathU32Vector3_GetValuePointer = get_U32Vector3_value_ptr;
        api->GamutMathU32Vector3Array_GetValuePointer = get_U32Vector3Array_value_ptr;
        api->GamutMathU32Vector3Array_GetLength = get_U32Vector3Array_length;

        {
            PyTypeObject *type = define_IVector3_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->IVector3_PyTypeObject = type;
        }
        {
            PyTypeObject *type = define_IVector3Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->IVector3Array_PyTypeObject = type;
        }
        api->GamutMathIVector3_GetType = get_IVector3_type;
        api->GamutMathIVector3Array_GetType = get_IVector3Array_type;
        api->GamutMathIVector3_Create = create_IVector3;
        api->GamutMathIVector3Array_Create = create_IVector3Array;
        api->GamutMathIVector3_GetValuePointer = get_IVector3_value_ptr;
        api->GamutMathIVector3Array_GetValuePointer = get_IVector3Array_value_ptr;
        api->GamutMathIVector3Array_GetLength = get_IVector3Array_length;

        {
            PyTypeObject *type = define_UVector3_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->UVector3_PyTypeObject = type;
        }
        {
            PyTypeObject *type = define_UVector3Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->UVector3Array_PyTypeObject = type;
        }
        api->GamutMathUVector3_GetType = get_UVector3_type;
        api->GamutMathUVector3Array_GetType = get_UVector3Array_type;
        api->GamutMathUVector3_Create = create_UVector3;
        api->GamutMathUVector3Array_Create = create_UVector3Array;
        api->GamutMathUVector3_GetValuePointer = get_UVector3_value_ptr;
        api->GamutMathUVector3Array_GetValuePointer = get_UVector3Array_value_ptr;
        api->GamutMathUVector3Array_GetLength = get_UVector3Array_length;

        {
            PyTypeObject *type = define_I64Vector3_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->I64Vector3_PyTypeObject = type;
        }
        {
            PyTypeObject *type = define_I64Vector3Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->I64Vector3Array_PyTypeObject = type;
        }
        api->GamutMathI64Vector3_GetType = get_I64Vector3_type;
        api->GamutMathI64Vector3Array_GetType = get_I64Vector3Array_type;
        api->GamutMathI64Vector3_Create = create_I64Vector3;
        api->GamutMathI64Vector3Array_Create = create_I64Vector3Array;
        api->GamutMathI64Vector3_GetValuePointer = get_I64Vector3_value_ptr;
        api->GamutMathI64Vector3Array_GetValuePointer = get_I64Vector3Array_value_ptr;
        api->GamutMathI64Vector3Array_GetLength = get_I64Vector3Array_length;

        {
            PyTypeObject *type = define_U64Vector3_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->U64Vector3_PyTypeObject = type;
        }
        {
            PyTypeObject *type = define_U64Vector3Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->U64Vector3Array_PyTypeObject = type;
        }
        api->GamutMathU64Vector3_GetType = get_U64Vector3_type;
        api->GamutMathU64Vector3Array_GetType = get_U64Vector3Array_type;
        api->GamutMathU64Vector3_Create = create_U64Vector3;
        api->GamutMathU64Vector3Array_Create = create_U64Vector3Array;
        api->GamutMathU64Vector3_GetValuePointer = get_U64Vector3_value_ptr;
        api->GamutMathU64Vector3Array_GetValuePointer = get_U64Vector3Array_value_ptr;
        api->GamutMathU64Vector3Array_GetLength = get_U64Vector3Array_length;

        {
            PyTypeObject *type = define_BVector4_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->BVector4_PyTypeObject = type;
        }
        {
            PyTypeObject *type = define_BVector4Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->BVector4Array_PyTypeObject = type;
        }
        api->GamutMathBVector4_GetType = get_BVector4_type;
        api->GamutMathBVector4Array_GetType = get_BVector4Array_type;
        api->GamutMathBVector4_Create = create_BVector4;
        api->GamutMathBVector4Array_Create = create_BVector4Array;
        api->GamutMathBVector4_GetValuePointer = get_BVector4_value_ptr;
        api->GamutMathBVector4Array_GetValuePointer = get_BVector4Array_value_ptr;
        api->GamutMathBVector4Array_GetLength = get_BVector4Array_length;

        {
            PyTypeObject *type = define_DVector4_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->DVector4_PyTypeObject = type;
        }
        {
            PyTypeObject *type = define_DVector4Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->DVector4Array_PyTypeObject = type;
        }
        api->GamutMathDVector4_GetType = get_DVector4_type;
        api->GamutMathDVector4Array_GetType = get_DVector4Array_type;
        api->GamutMathDVector4_Create = create_DVector4;
        api->GamutMathDVector4Array_Create = create_DVector4Array;
        api->GamutMathDVector4_GetValuePointer = get_DVector4_value_ptr;
        api->GamutMathDVector4Array_GetValuePointer = get_DVector4Array_value_ptr;
        api->GamutMathDVector4Array_GetLength = get_DVector4Array_length;

        {
            PyTypeObject *type = define_FVector4_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->FVector4_PyTypeObject = type;
        }
        {
            PyTypeObject *type = define_FVector4Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->FVector4Array_PyTypeObject = type;
        }
        api->GamutMathFVector4_GetType = get_FVector4_type;
        api->GamutMathFVector4Array_GetType = get_FVector4Array_type;
        api->GamutMathFVector4_Create = create_FVector4;
        api->GamutMathFVector4Array_Create = create_FVector4Array;
        api->GamutMathFVector4_GetValuePointer = get_FVector4_value_ptr;
        api->GamutMathFVector4Array_GetValuePointer = get_FVector4Array_value_ptr;
        api->GamutMathFVector4Array_GetLength = get_FVector4Array_length;

        {
            PyTypeObject *type = define_I8Vector4_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->I8Vector4_PyTypeObject = type;
        }
        {
            PyTypeObject *type = define_I8Vector4Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->I8Vector4Array_PyTypeObject = type;
        }
        api->GamutMathI8Vector4_GetType = get_I8Vector4_type;
        api->GamutMathI8Vector4Array_GetType = get_I8Vector4Array_type;
        api->GamutMathI8Vector4_Create = create_I8Vector4;
        api->GamutMathI8Vector4Array_Create = create_I8Vector4Array;
        api->GamutMathI8Vector4_GetValuePointer = get_I8Vector4_value_ptr;
        api->GamutMathI8Vector4Array_GetValuePointer = get_I8Vector4Array_value_ptr;
        api->GamutMathI8Vector4Array_GetLength = get_I8Vector4Array_length;

        {
            PyTypeObject *type = define_U8Vector4_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->U8Vector4_PyTypeObject = type;
        }
        {
            PyTypeObject *type = define_U8Vector4Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->U8Vector4Array_PyTypeObject = type;
        }
        api->GamutMathU8Vector4_GetType = get_U8Vector4_type;
        api->GamutMathU8Vector4Array_GetType = get_U8Vector4Array_type;
        api->GamutMathU8Vector4_Create = create_U8Vector4;
        api->GamutMathU8Vector4Array_Create = create_U8Vector4Array;
        api->GamutMathU8Vector4_GetValuePointer = get_U8Vector4_value_ptr;
        api->GamutMathU8Vector4Array_GetValuePointer = get_U8Vector4Array_value_ptr;
        api->GamutMathU8Vector4Array_GetLength = get_U8Vector4Array_length;

        {
            PyTypeObject *type = define_I16Vector4_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->I16Vector4_PyTypeObject = type;
        }
        {
            PyTypeObject *type = define_I16Vector4Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->I16Vector4Array_PyTypeObject = type;
        }
        api->GamutMathI16Vector4_GetType = get_I16Vector4_type;
        api->GamutMathI16Vector4Array_GetType = get_I16Vector4Array_type;
        api->GamutMathI16Vector4_Create = create_I16Vector4;
        api->GamutMathI16Vector4Array_Create = create_I16Vector4Array;
        api->GamutMathI16Vector4_GetValuePointer = get_I16Vector4_value_ptr;
        api->GamutMathI16Vector4Array_GetValuePointer = get_I16Vector4Array_value_ptr;
        api->GamutMathI16Vector4Array_GetLength = get_I16Vector4Array_length;

        {
            PyTypeObject *type = define_U16Vector4_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->U16Vector4_PyTypeObject = type;
        }
        {
            PyTypeObject *type = define_U16Vector4Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->U16Vector4Array_PyTypeObject = type;
        }
        api->GamutMathU16Vector4_GetType = get_U16Vector4_type;
        api->GamutMathU16Vector4Array_GetType = get_U16Vector4Array_type;
        api->GamutMathU16Vector4_Create = create_U16Vector4;
        api->GamutMathU16Vector4Array_Create = create_U16Vector4Array;
        api->GamutMathU16Vector4_GetValuePointer = get_U16Vector4_value_ptr;
        api->GamutMathU16Vector4Array_GetValuePointer = get_U16Vector4Array_value_ptr;
        api->GamutMathU16Vector4Array_GetLength = get_U16Vector4Array_length;

        {
            PyTypeObject *type = define_I32Vector4_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->I32Vector4_PyTypeObject = type;
        }
        {
            PyTypeObject *type = define_I32Vector4Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->I32Vector4Array_PyTypeObject = type;
        }
        api->GamutMathI32Vector4_GetType = get_I32Vector4_type;
        api->GamutMathI32Vector4Array_GetType = get_I32Vector4Array_type;
        api->GamutMathI32Vector4_Create = create_I32Vector4;
        api->GamutMathI32Vector4Array_Create = create_I32Vector4Array;
        api->GamutMathI32Vector4_GetValuePointer = get_I32Vector4_value_ptr;
        api->GamutMathI32Vector4Array_GetValuePointer = get_I32Vector4Array_value_ptr;
        api->GamutMathI32Vector4Array_GetLength = get_I32Vector4Array_length;

        {
            PyTypeObject *type = define_U32Vector4_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->U32Vector4_PyTypeObject = type;
        }
        {
            PyTypeObject *type = define_U32Vector4Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->U32Vector4Array_PyTypeObject = type;
        }
        api->GamutMathU32Vector4_GetType = get_U32Vector4_type;
        api->GamutMathU32Vector4Array_GetType = get_U32Vector4Array_type;
        api->GamutMathU32Vector4_Create = create_U32Vector4;
        api->GamutMathU32Vector4Array_Create = create_U32Vector4Array;
        api->GamutMathU32Vector4_GetValuePointer = get_U32Vector4_value_ptr;
        api->GamutMathU32Vector4Array_GetValuePointer = get_U32Vector4Array_value_ptr;
        api->GamutMathU32Vector4Array_GetLength = get_U32Vector4Array_length;

        {
            PyTypeObject *type = define_IVector4_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->IVector4_PyTypeObject = type;
        }
        {
            PyTypeObject *type = define_IVector4Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->IVector4Array_PyTypeObject = type;
        }
        api->GamutMathIVector4_GetType = get_IVector4_type;
        api->GamutMathIVector4Array_GetType = get_IVector4Array_type;
        api->GamutMathIVector4_Create = create_IVector4;
        api->GamutMathIVector4Array_Create = create_IVector4Array;
        api->GamutMathIVector4_GetValuePointer = get_IVector4_value_ptr;
        api->GamutMathIVector4Array_GetValuePointer = get_IVector4Array_value_ptr;
        api->GamutMathIVector4Array_GetLength = get_IVector4Array_length;

        {
            PyTypeObject *type = define_UVector4_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->UVector4_PyTypeObject = type;
        }
        {
            PyTypeObject *type = define_UVector4Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->UVector4Array_PyTypeObject = type;
        }
        api->GamutMathUVector4_GetType = get_UVector4_type;
        api->GamutMathUVector4Array_GetType = get_UVector4Array_type;
        api->GamutMathUVector4_Create = create_UVector4;
        api->GamutMathUVector4Array_Create = create_UVector4Array;
        api->GamutMathUVector4_GetValuePointer = get_UVector4_value_ptr;
        api->GamutMathUVector4Array_GetValuePointer = get_UVector4Array_value_ptr;
        api->GamutMathUVector4Array_GetLength = get_UVector4Array_length;

        {
            PyTypeObject *type = define_I64Vector4_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->I64Vector4_PyTypeObject = type;
        }
        {
            PyTypeObject *type = define_I64Vector4Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->I64Vector4Array_PyTypeObject = type;
        }
        api->GamutMathI64Vector4_GetType = get_I64Vector4_type;
        api->GamutMathI64Vector4Array_GetType = get_I64Vector4Array_type;
        api->GamutMathI64Vector4_Create = create_I64Vector4;
        api->GamutMathI64Vector4Array_Create = create_I64Vector4Array;
        api->GamutMathI64Vector4_GetValuePointer = get_I64Vector4_value_ptr;
        api->GamutMathI64Vector4Array_GetValuePointer = get_I64Vector4Array_value_ptr;
        api->GamutMathI64Vector4Array_GetLength = get_I64Vector4Array_length;

        {
            PyTypeObject *type = define_U64Vector4_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->U64Vector4_PyTypeObject = type;
        }
        {
            PyTypeObject *type = define_U64Vector4Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->U64Vector4Array_PyTypeObject = type;
        }
        api->GamutMathU64Vector4_GetType = get_U64Vector4_type;
        api->GamutMathU64Vector4Array_GetType = get_U64Vector4Array_type;
        api->GamutMathU64Vector4_Create = create_U64Vector4;
        api->GamutMathU64Vector4Array_Create = create_U64Vector4Array;
        api->GamutMathU64Vector4_GetValuePointer = get_U64Vector4_value_ptr;
        api->GamutMathU64Vector4Array_GetValuePointer = get_U64Vector4Array_value_ptr;
        api->GamutMathU64Vector4Array_GetLength = get_U64Vector4Array_length;


        {
            PyTypeObject *type = define_DMatrix2x2_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->DMatrix2x2_PyTypeObject = type;
        }
        {
            PyTypeObject *type = define_DMatrix2x2Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->DMatrix2x2Array_PyTypeObject = type;
        }
        api->GamutMathDMatrix2x2_GetType = get_DMatrix2x2_type;
        api->GamutMathDMatrix2x2Array_GetType = get_DMatrix2x2Array_type;
        api->GamutMathDMatrix2x2_Create = create_DMatrix2x2;
        api->GamutMathDMatrix2x2Array_Create = create_DMatrix2x2Array;
        api->GamutMathDMatrix2x2_GetValuePointer = get_DMatrix2x2_value_ptr;
        api->GamutMathDMatrix2x2Array_GetValuePointer = get_DMatrix2x2Array_value_ptr;
        api->GamutMathDMatrix2x2Array_GetLength = get_DMatrix2x2Array_length;

        {
            PyTypeObject *type = define_FMatrix2x2_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->FMatrix2x2_PyTypeObject = type;
        }
        {
            PyTypeObject *type = define_FMatrix2x2Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->FMatrix2x2Array_PyTypeObject = type;
        }
        api->GamutMathFMatrix2x2_GetType = get_FMatrix2x2_type;
        api->GamutMathFMatrix2x2Array_GetType = get_FMatrix2x2Array_type;
        api->GamutMathFMatrix2x2_Create = create_FMatrix2x2;
        api->GamutMathFMatrix2x2Array_Create = create_FMatrix2x2Array;
        api->GamutMathFMatrix2x2_GetValuePointer = get_FMatrix2x2_value_ptr;
        api->GamutMathFMatrix2x2Array_GetValuePointer = get_FMatrix2x2Array_value_ptr;
        api->GamutMathFMatrix2x2Array_GetLength = get_FMatrix2x2Array_length;

        {
            PyTypeObject *type = define_DMatrix2x3_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->DMatrix2x3_PyTypeObject = type;
        }
        {
            PyTypeObject *type = define_DMatrix2x3Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->DMatrix2x3Array_PyTypeObject = type;
        }
        api->GamutMathDMatrix2x3_GetType = get_DMatrix2x3_type;
        api->GamutMathDMatrix2x3Array_GetType = get_DMatrix2x3Array_type;
        api->GamutMathDMatrix2x3_Create = create_DMatrix2x3;
        api->GamutMathDMatrix2x3Array_Create = create_DMatrix2x3Array;
        api->GamutMathDMatrix2x3_GetValuePointer = get_DMatrix2x3_value_ptr;
        api->GamutMathDMatrix2x3Array_GetValuePointer = get_DMatrix2x3Array_value_ptr;
        api->GamutMathDMatrix2x3Array_GetLength = get_DMatrix2x3Array_length;

        {
            PyTypeObject *type = define_FMatrix2x3_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->FMatrix2x3_PyTypeObject = type;
        }
        {
            PyTypeObject *type = define_FMatrix2x3Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->FMatrix2x3Array_PyTypeObject = type;
        }
        api->GamutMathFMatrix2x3_GetType = get_FMatrix2x3_type;
        api->GamutMathFMatrix2x3Array_GetType = get_FMatrix2x3Array_type;
        api->GamutMathFMatrix2x3_Create = create_FMatrix2x3;
        api->GamutMathFMatrix2x3Array_Create = create_FMatrix2x3Array;
        api->GamutMathFMatrix2x3_GetValuePointer = get_FMatrix2x3_value_ptr;
        api->GamutMathFMatrix2x3Array_GetValuePointer = get_FMatrix2x3Array_value_ptr;
        api->GamutMathFMatrix2x3Array_GetLength = get_FMatrix2x3Array_length;

        {
            PyTypeObject *type = define_DMatrix2x4_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->DMatrix2x4_PyTypeObject = type;
        }
        {
            PyTypeObject *type = define_DMatrix2x4Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->DMatrix2x4Array_PyTypeObject = type;
        }
        api->GamutMathDMatrix2x4_GetType = get_DMatrix2x4_type;
        api->GamutMathDMatrix2x4Array_GetType = get_DMatrix2x4Array_type;
        api->GamutMathDMatrix2x4_Create = create_DMatrix2x4;
        api->GamutMathDMatrix2x4Array_Create = create_DMatrix2x4Array;
        api->GamutMathDMatrix2x4_GetValuePointer = get_DMatrix2x4_value_ptr;
        api->GamutMathDMatrix2x4Array_GetValuePointer = get_DMatrix2x4Array_value_ptr;
        api->GamutMathDMatrix2x4Array_GetLength = get_DMatrix2x4Array_length;

        {
            PyTypeObject *type = define_FMatrix2x4_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->FMatrix2x4_PyTypeObject = type;
        }
        {
            PyTypeObject *type = define_FMatrix2x4Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->FMatrix2x4Array_PyTypeObject = type;
        }
        api->GamutMathFMatrix2x4_GetType = get_FMatrix2x4_type;
        api->GamutMathFMatrix2x4Array_GetType = get_FMatrix2x4Array_type;
        api->GamutMathFMatrix2x4_Create = create_FMatrix2x4;
        api->GamutMathFMatrix2x4Array_Create = create_FMatrix2x4Array;
        api->GamutMathFMatrix2x4_GetValuePointer = get_FMatrix2x4_value_ptr;
        api->GamutMathFMatrix2x4Array_GetValuePointer = get_FMatrix2x4Array_value_ptr;
        api->GamutMathFMatrix2x4Array_GetLength = get_FMatrix2x4Array_length;

        {
            PyTypeObject *type = define_DMatrix3x2_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->DMatrix3x2_PyTypeObject = type;
        }
        {
            PyTypeObject *type = define_DMatrix3x2Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->DMatrix3x2Array_PyTypeObject = type;
        }
        api->GamutMathDMatrix3x2_GetType = get_DMatrix3x2_type;
        api->GamutMathDMatrix3x2Array_GetType = get_DMatrix3x2Array_type;
        api->GamutMathDMatrix3x2_Create = create_DMatrix3x2;
        api->GamutMathDMatrix3x2Array_Create = create_DMatrix3x2Array;
        api->GamutMathDMatrix3x2_GetValuePointer = get_DMatrix3x2_value_ptr;
        api->GamutMathDMatrix3x2Array_GetValuePointer = get_DMatrix3x2Array_value_ptr;
        api->GamutMathDMatrix3x2Array_GetLength = get_DMatrix3x2Array_length;

        {
            PyTypeObject *type = define_FMatrix3x2_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->FMatrix3x2_PyTypeObject = type;
        }
        {
            PyTypeObject *type = define_FMatrix3x2Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->FMatrix3x2Array_PyTypeObject = type;
        }
        api->GamutMathFMatrix3x2_GetType = get_FMatrix3x2_type;
        api->GamutMathFMatrix3x2Array_GetType = get_FMatrix3x2Array_type;
        api->GamutMathFMatrix3x2_Create = create_FMatrix3x2;
        api->GamutMathFMatrix3x2Array_Create = create_FMatrix3x2Array;
        api->GamutMathFMatrix3x2_GetValuePointer = get_FMatrix3x2_value_ptr;
        api->GamutMathFMatrix3x2Array_GetValuePointer = get_FMatrix3x2Array_value_ptr;
        api->GamutMathFMatrix3x2Array_GetLength = get_FMatrix3x2Array_length;

        {
            PyTypeObject *type = define_DMatrix3x3_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->DMatrix3x3_PyTypeObject = type;
        }
        {
            PyTypeObject *type = define_DMatrix3x3Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->DMatrix3x3Array_PyTypeObject = type;
        }
        api->GamutMathDMatrix3x3_GetType = get_DMatrix3x3_type;
        api->GamutMathDMatrix3x3Array_GetType = get_DMatrix3x3Array_type;
        api->GamutMathDMatrix3x3_Create = create_DMatrix3x3;
        api->GamutMathDMatrix3x3Array_Create = create_DMatrix3x3Array;
        api->GamutMathDMatrix3x3_GetValuePointer = get_DMatrix3x3_value_ptr;
        api->GamutMathDMatrix3x3Array_GetValuePointer = get_DMatrix3x3Array_value_ptr;
        api->GamutMathDMatrix3x3Array_GetLength = get_DMatrix3x3Array_length;

        {
            PyTypeObject *type = define_FMatrix3x3_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->FMatrix3x3_PyTypeObject = type;
        }
        {
            PyTypeObject *type = define_FMatrix3x3Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->FMatrix3x3Array_PyTypeObject = type;
        }
        api->GamutMathFMatrix3x3_GetType = get_FMatrix3x3_type;
        api->GamutMathFMatrix3x3Array_GetType = get_FMatrix3x3Array_type;
        api->GamutMathFMatrix3x3_Create = create_FMatrix3x3;
        api->GamutMathFMatrix3x3Array_Create = create_FMatrix3x3Array;
        api->GamutMathFMatrix3x3_GetValuePointer = get_FMatrix3x3_value_ptr;
        api->GamutMathFMatrix3x3Array_GetValuePointer = get_FMatrix3x3Array_value_ptr;
        api->GamutMathFMatrix3x3Array_GetLength = get_FMatrix3x3Array_length;

        {
            PyTypeObject *type = define_DMatrix3x4_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->DMatrix3x4_PyTypeObject = type;
        }
        {
            PyTypeObject *type = define_DMatrix3x4Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->DMatrix3x4Array_PyTypeObject = type;
        }
        api->GamutMathDMatrix3x4_GetType = get_DMatrix3x4_type;
        api->GamutMathDMatrix3x4Array_GetType = get_DMatrix3x4Array_type;
        api->GamutMathDMatrix3x4_Create = create_DMatrix3x4;
        api->GamutMathDMatrix3x4Array_Create = create_DMatrix3x4Array;
        api->GamutMathDMatrix3x4_GetValuePointer = get_DMatrix3x4_value_ptr;
        api->GamutMathDMatrix3x4Array_GetValuePointer = get_DMatrix3x4Array_value_ptr;
        api->GamutMathDMatrix3x4Array_GetLength = get_DMatrix3x4Array_length;

        {
            PyTypeObject *type = define_FMatrix3x4_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->FMatrix3x4_PyTypeObject = type;
        }
        {
            PyTypeObject *type = define_FMatrix3x4Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->FMatrix3x4Array_PyTypeObject = type;
        }
        api->GamutMathFMatrix3x4_GetType = get_FMatrix3x4_type;
        api->GamutMathFMatrix3x4Array_GetType = get_FMatrix3x4Array_type;
        api->GamutMathFMatrix3x4_Create = create_FMatrix3x4;
        api->GamutMathFMatrix3x4Array_Create = create_FMatrix3x4Array;
        api->GamutMathFMatrix3x4_GetValuePointer = get_FMatrix3x4_value_ptr;
        api->GamutMathFMatrix3x4Array_GetValuePointer = get_FMatrix3x4Array_value_ptr;
        api->GamutMathFMatrix3x4Array_GetLength = get_FMatrix3x4Array_length;

        {
            PyTypeObject *type = define_DMatrix4x2_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->DMatrix4x2_PyTypeObject = type;
        }
        {
            PyTypeObject *type = define_DMatrix4x2Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->DMatrix4x2Array_PyTypeObject = type;
        }
        api->GamutMathDMatrix4x2_GetType = get_DMatrix4x2_type;
        api->GamutMathDMatrix4x2Array_GetType = get_DMatrix4x2Array_type;
        api->GamutMathDMatrix4x2_Create = create_DMatrix4x2;
        api->GamutMathDMatrix4x2Array_Create = create_DMatrix4x2Array;
        api->GamutMathDMatrix4x2_GetValuePointer = get_DMatrix4x2_value_ptr;
        api->GamutMathDMatrix4x2Array_GetValuePointer = get_DMatrix4x2Array_value_ptr;
        api->GamutMathDMatrix4x2Array_GetLength = get_DMatrix4x2Array_length;

        {
            PyTypeObject *type = define_FMatrix4x2_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->FMatrix4x2_PyTypeObject = type;
        }
        {
            PyTypeObject *type = define_FMatrix4x2Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->FMatrix4x2Array_PyTypeObject = type;
        }
        api->GamutMathFMatrix4x2_GetType = get_FMatrix4x2_type;
        api->GamutMathFMatrix4x2Array_GetType = get_FMatrix4x2Array_type;
        api->GamutMathFMatrix4x2_Create = create_FMatrix4x2;
        api->GamutMathFMatrix4x2Array_Create = create_FMatrix4x2Array;
        api->GamutMathFMatrix4x2_GetValuePointer = get_FMatrix4x2_value_ptr;
        api->GamutMathFMatrix4x2Array_GetValuePointer = get_FMatrix4x2Array_value_ptr;
        api->GamutMathFMatrix4x2Array_GetLength = get_FMatrix4x2Array_length;

        {
            PyTypeObject *type = define_DMatrix4x3_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->DMatrix4x3_PyTypeObject = type;
        }
        {
            PyTypeObject *type = define_DMatrix4x3Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->DMatrix4x3Array_PyTypeObject = type;
        }
        api->GamutMathDMatrix4x3_GetType = get_DMatrix4x3_type;
        api->GamutMathDMatrix4x3Array_GetType = get_DMatrix4x3Array_type;
        api->GamutMathDMatrix4x3_Create = create_DMatrix4x3;
        api->GamutMathDMatrix4x3Array_Create = create_DMatrix4x3Array;
        api->GamutMathDMatrix4x3_GetValuePointer = get_DMatrix4x3_value_ptr;
        api->GamutMathDMatrix4x3Array_GetValuePointer = get_DMatrix4x3Array_value_ptr;
        api->GamutMathDMatrix4x3Array_GetLength = get_DMatrix4x3Array_length;

        {
            PyTypeObject *type = define_FMatrix4x3_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->FMatrix4x3_PyTypeObject = type;
        }
        {
            PyTypeObject *type = define_FMatrix4x3Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->FMatrix4x3Array_PyTypeObject = type;
        }
        api->GamutMathFMatrix4x3_GetType = get_FMatrix4x3_type;
        api->GamutMathFMatrix4x3Array_GetType = get_FMatrix4x3Array_type;
        api->GamutMathFMatrix4x3_Create = create_FMatrix4x3;
        api->GamutMathFMatrix4x3Array_Create = create_FMatrix4x3Array;
        api->GamutMathFMatrix4x3_GetValuePointer = get_FMatrix4x3_value_ptr;
        api->GamutMathFMatrix4x3Array_GetValuePointer = get_FMatrix4x3Array_value_ptr;
        api->GamutMathFMatrix4x3Array_GetLength = get_FMatrix4x3Array_length;

        {
            PyTypeObject *type = define_DMatrix4x4_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->DMatrix4x4_PyTypeObject = type;
        }
        {
            PyTypeObject *type = define_DMatrix4x4Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->DMatrix4x4Array_PyTypeObject = type;
        }
        api->GamutMathDMatrix4x4_GetType = get_DMatrix4x4_type;
        api->GamutMathDMatrix4x4Array_GetType = get_DMatrix4x4Array_type;
        api->GamutMathDMatrix4x4_Create = create_DMatrix4x4;
        api->GamutMathDMatrix4x4Array_Create = create_DMatrix4x4Array;
        api->GamutMathDMatrix4x4_GetValuePointer = get_DMatrix4x4_value_ptr;
        api->GamutMathDMatrix4x4Array_GetValuePointer = get_DMatrix4x4Array_value_ptr;
        api->GamutMathDMatrix4x4Array_GetLength = get_DMatrix4x4Array_length;

        {
            PyTypeObject *type = define_FMatrix4x4_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->FMatrix4x4_PyTypeObject = type;
        }
        {
            PyTypeObject *type = define_FMatrix4x4Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->FMatrix4x4Array_PyTypeObject = type;
        }
        api->GamutMathFMatrix4x4_GetType = get_FMatrix4x4_type;
        api->GamutMathFMatrix4x4Array_GetType = get_FMatrix4x4Array_type;
        api->GamutMathFMatrix4x4_Create = create_FMatrix4x4;
        api->GamutMathFMatrix4x4Array_Create = create_FMatrix4x4Array;
        api->GamutMathFMatrix4x4_GetValuePointer = get_FMatrix4x4_value_ptr;
        api->GamutMathFMatrix4x4Array_GetValuePointer = get_FMatrix4x4Array_value_ptr;
        api->GamutMathFMatrix4x4Array_GetLength = get_FMatrix4x4Array_length;


        {
            PyTypeObject *type = define_BArray_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->BArray_PyTypeObject = type;
        }
        api->GamutMathBArray_GetType = get_BArray_type;
        api->GamutMathBArray_Create = create_BArray;
        api->GamutMathBArray_GetValuePointer = get_BArray_value_ptr;
        api->GamutMathBArray_GetLength = get_BArray_length;

        {
            PyTypeObject *type = define_DArray_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->DArray_PyTypeObject = type;
        }
        api->GamutMathDArray_GetType = get_DArray_type;
        api->GamutMathDArray_Create = create_DArray;
        api->GamutMathDArray_GetValuePointer = get_DArray_value_ptr;
        api->GamutMathDArray_GetLength = get_DArray_length;

        {
            PyTypeObject *type = define_FArray_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->FArray_PyTypeObject = type;
        }
        api->GamutMathFArray_GetType = get_FArray_type;
        api->GamutMathFArray_Create = create_FArray;
        api->GamutMathFArray_GetValuePointer = get_FArray_value_ptr;
        api->GamutMathFArray_GetLength = get_FArray_length;

        {
            PyTypeObject *type = define_I8Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->I8Array_PyTypeObject = type;
        }
        api->GamutMathI8Array_GetType = get_I8Array_type;
        api->GamutMathI8Array_Create = create_I8Array;
        api->GamutMathI8Array_GetValuePointer = get_I8Array_value_ptr;
        api->GamutMathI8Array_GetLength = get_I8Array_length;

        {
            PyTypeObject *type = define_U8Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->U8Array_PyTypeObject = type;
        }
        api->GamutMathU8Array_GetType = get_U8Array_type;
        api->GamutMathU8Array_Create = create_U8Array;
        api->GamutMathU8Array_GetValuePointer = get_U8Array_value_ptr;
        api->GamutMathU8Array_GetLength = get_U8Array_length;

        {
            PyTypeObject *type = define_I16Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->I16Array_PyTypeObject = type;
        }
        api->GamutMathI16Array_GetType = get_I16Array_type;
        api->GamutMathI16Array_Create = create_I16Array;
        api->GamutMathI16Array_GetValuePointer = get_I16Array_value_ptr;
        api->GamutMathI16Array_GetLength = get_I16Array_length;

        {
            PyTypeObject *type = define_U16Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->U16Array_PyTypeObject = type;
        }
        api->GamutMathU16Array_GetType = get_U16Array_type;
        api->GamutMathU16Array_Create = create_U16Array;
        api->GamutMathU16Array_GetValuePointer = get_U16Array_value_ptr;
        api->GamutMathU16Array_GetLength = get_U16Array_length;

        {
            PyTypeObject *type = define_I32Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->I32Array_PyTypeObject = type;
        }
        api->GamutMathI32Array_GetType = get_I32Array_type;
        api->GamutMathI32Array_Create = create_I32Array;
        api->GamutMathI32Array_GetValuePointer = get_I32Array_value_ptr;
        api->GamutMathI32Array_GetLength = get_I32Array_length;

        {
            PyTypeObject *type = define_U32Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->U32Array_PyTypeObject = type;
        }
        api->GamutMathU32Array_GetType = get_U32Array_type;
        api->GamutMathU32Array_Create = create_U32Array;
        api->GamutMathU32Array_GetValuePointer = get_U32Array_value_ptr;
        api->GamutMathU32Array_GetLength = get_U32Array_length;

        {
            PyTypeObject *type = define_IArray_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->IArray_PyTypeObject = type;
        }
        api->GamutMathIArray_GetType = get_IArray_type;
        api->GamutMathIArray_Create = create_IArray;
        api->GamutMathIArray_GetValuePointer = get_IArray_value_ptr;
        api->GamutMathIArray_GetLength = get_IArray_length;

        {
            PyTypeObject *type = define_UArray_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->UArray_PyTypeObject = type;
        }
        api->GamutMathUArray_GetType = get_UArray_type;
        api->GamutMathUArray_Create = create_UArray;
        api->GamutMathUArray_GetValuePointer = get_UArray_value_ptr;
        api->GamutMathUArray_GetLength = get_UArray_length;

        {
            PyTypeObject *type = define_I64Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->I64Array_PyTypeObject = type;
        }
        api->GamutMathI64Array_GetType = get_I64Array_type;
        api->GamutMathI64Array_Create = create_I64Array;
        api->GamutMathI64Array_GetValuePointer = get_I64Array_value_ptr;
        api->GamutMathI64Array_GetLength = get_I64Array_length;

        {
            PyTypeObject *type = define_U64Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->U64Array_PyTypeObject = type;
        }
        api->GamutMathU64Array_GetType = get_U64Array_type;
        api->GamutMathU64Array_Create = create_U64Array;
        api->GamutMathU64Array_GetValuePointer = get_U64Array_value_ptr;
        api->GamutMathU64Array_GetLength = get_U64Array_length;


    if (PyModule_AddObject(module, "_api", api_capsule) < 0){ goto error; }

    return module;
error:
    delete api;
    Py_DECREF(api_capsule);
    Py_CLEAR(module);
    return 0;
}


static PyObject *
get_module()
{
    PyObject *module = PyState_FindModule(&module_PyModuleDef);
    if (!module)
    {
        return PyErr_Format(PyExc_RuntimeError, "math module not ready");
    }
    return module;
}