// generated {{ when }}

// python
#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <structmember.h>

{% for type in types %}
    #include "_{{ type.lower() }}.hpp"
{% endfor %}

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


    {% for type in types %}
        if (!define_{{ type }}_type(module)){ goto error; }
    {% endfor %}

    return module;
error:
    Py_CLEAR(module);
    return 0;
}
