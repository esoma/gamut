
// python
#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <structmember.h>

#include <_dvector3.hpp>

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

    if (!define_DVector3_type(module)){ goto error; }

    return module;
error:
    Py_CLEAR(module);
    return 0;
}
