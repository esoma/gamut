// generated 2022-03-07 23:13:00.220094 from codegen/math/templates/_math.hpp

// python
#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <structmember.h>


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


// module
// ----------------------------------------------------------------------------

static PyMethodDef module_methods[] = {
    {0, 0, 0, 0}
};

static struct PyModuleDef module_PyModuleDef = {
    PyModuleDef_HEAD_INIT,
    "gamut.math._math",
    0,
    0,
    module_methods,
    0,
    0,
    0
};


PyMODINIT_FUNC
PyInit__math()
{
    PyObject *module = PyModule_Create(&module_PyModuleDef);
    if (!module){ goto error; }



        if (!define_BVector2_type(module)){ goto error; }

        if (!define_DVector2_type(module)){ goto error; }

        if (!define_FVector2_type(module)){ goto error; }

        if (!define_I8Vector2_type(module)){ goto error; }

        if (!define_U8Vector2_type(module)){ goto error; }

        if (!define_I16Vector2_type(module)){ goto error; }

        if (!define_U16Vector2_type(module)){ goto error; }

        if (!define_I32Vector2_type(module)){ goto error; }

        if (!define_U32Vector2_type(module)){ goto error; }

        if (!define_IVector2_type(module)){ goto error; }

        if (!define_UVector2_type(module)){ goto error; }

        if (!define_I64Vector2_type(module)){ goto error; }

        if (!define_U64Vector2_type(module)){ goto error; }

        if (!define_BVector3_type(module)){ goto error; }

        if (!define_DVector3_type(module)){ goto error; }

        if (!define_FVector3_type(module)){ goto error; }

        if (!define_I8Vector3_type(module)){ goto error; }

        if (!define_U8Vector3_type(module)){ goto error; }

        if (!define_I16Vector3_type(module)){ goto error; }

        if (!define_U16Vector3_type(module)){ goto error; }

        if (!define_I32Vector3_type(module)){ goto error; }

        if (!define_U32Vector3_type(module)){ goto error; }

        if (!define_IVector3_type(module)){ goto error; }

        if (!define_UVector3_type(module)){ goto error; }

        if (!define_I64Vector3_type(module)){ goto error; }

        if (!define_U64Vector3_type(module)){ goto error; }

        if (!define_BVector4_type(module)){ goto error; }

        if (!define_DVector4_type(module)){ goto error; }

        if (!define_FVector4_type(module)){ goto error; }

        if (!define_I8Vector4_type(module)){ goto error; }

        if (!define_U8Vector4_type(module)){ goto error; }

        if (!define_I16Vector4_type(module)){ goto error; }

        if (!define_U16Vector4_type(module)){ goto error; }

        if (!define_I32Vector4_type(module)){ goto error; }

        if (!define_U32Vector4_type(module)){ goto error; }

        if (!define_IVector4_type(module)){ goto error; }

        if (!define_UVector4_type(module)){ goto error; }

        if (!define_I64Vector4_type(module)){ goto error; }

        if (!define_U64Vector4_type(module)){ goto error; }


    return module;
error:
    Py_CLEAR(module);
    return 0;
}