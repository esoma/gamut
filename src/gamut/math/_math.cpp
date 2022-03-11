
// generated 2022-03-11 18:37:26.844466 from codegen/math/templates/_math.hpp

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


PyMODINIT_FUNC
PyInit__math()
{
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


    {
        PyTypeObject *type = define_BArray_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->BArray_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_DArray_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->DArray_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_FArray_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->FArray_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_I8Array_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->I8Array_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_U8Array_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->U8Array_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_I16Array_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->I16Array_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_U16Array_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->U16Array_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_I32Array_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->I32Array_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_U32Array_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->U32Array_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_IArray_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->IArray_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_UArray_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->UArray_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_I64Array_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->I64Array_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_U64Array_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->U64Array_PyTypeObject = type;
    }


    return module;
error:
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