
// generated 2022-03-10 23:24:28.481931 from codegen/math/templates/_math.hpp

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
        PyTypeObject *type = define_DVector2_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->DVector2_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_FVector2_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->FVector2_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_I8Vector2_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->I8Vector2_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_U8Vector2_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->U8Vector2_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_I16Vector2_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->I16Vector2_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_U16Vector2_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->U16Vector2_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_I32Vector2_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->I32Vector2_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_U32Vector2_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->U32Vector2_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_IVector2_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->IVector2_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_UVector2_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->UVector2_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_I64Vector2_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->I64Vector2_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_U64Vector2_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->U64Vector2_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_BVector3_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->BVector3_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_DVector3_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->DVector3_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_FVector3_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->FVector3_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_I8Vector3_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->I8Vector3_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_U8Vector3_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->U8Vector3_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_I16Vector3_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->I16Vector3_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_U16Vector3_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->U16Vector3_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_I32Vector3_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->I32Vector3_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_U32Vector3_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->U32Vector3_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_IVector3_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->IVector3_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_UVector3_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->UVector3_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_I64Vector3_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->I64Vector3_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_U64Vector3_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->U64Vector3_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_BVector4_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->BVector4_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_DVector4_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->DVector4_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_FVector4_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->FVector4_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_I8Vector4_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->I8Vector4_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_U8Vector4_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->U8Vector4_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_I16Vector4_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->I16Vector4_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_U16Vector4_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->U16Vector4_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_I32Vector4_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->I32Vector4_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_U32Vector4_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->U32Vector4_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_IVector4_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->IVector4_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_UVector4_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->UVector4_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_I64Vector4_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->I64Vector4_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_U64Vector4_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->U64Vector4_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_DMatrix2x2_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->DMatrix2x2_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_FMatrix2x2_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->FMatrix2x2_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_DMatrix2x3_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->DMatrix2x3_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_FMatrix2x3_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->FMatrix2x3_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_DMatrix2x4_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->DMatrix2x4_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_FMatrix2x4_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->FMatrix2x4_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_DMatrix3x2_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->DMatrix3x2_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_FMatrix3x2_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->FMatrix3x2_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_DMatrix3x3_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->DMatrix3x3_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_FMatrix3x3_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->FMatrix3x3_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_DMatrix3x4_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->DMatrix3x4_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_FMatrix3x4_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->FMatrix3x4_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_DMatrix4x2_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->DMatrix4x2_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_FMatrix4x2_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->FMatrix4x2_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_DMatrix4x3_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->DMatrix4x3_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_FMatrix4x3_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->FMatrix4x3_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_DMatrix4x4_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->DMatrix4x4_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_FMatrix4x4_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->FMatrix4x4_PyTypeObject = type;
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