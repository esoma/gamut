// generated 2022-03-07 03:05:30.759874

// python
#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <structmember.h>


    #include "_fvector2.hpp"

    #include "_dvector2.hpp"

    #include "_fvector3.hpp"

    #include "_dvector3.hpp"

    #include "_fvector4.hpp"

    #include "_dvector4.hpp"


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



        if (!define_FVector2_type(module)){ goto error; }

        if (!define_DVector2_type(module)){ goto error; }

        if (!define_FVector3_type(module)){ goto error; }

        if (!define_DVector3_type(module)){ goto error; }

        if (!define_FVector4_type(module)){ goto error; }

        if (!define_DVector4_type(module)){ goto error; }


    return module;
error:
    Py_CLEAR(module);
    return 0;
}