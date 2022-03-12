
// generated {{ when }} from codegen/math/templates/_math.cpp

// python
#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <structmember.h>

#include "_modulestate.hpp"
{% for type in vector_types %}
    #include "_{{ type.lower() }}.hpp"
{% endfor %}
{% for type in matrix_types %}
    #include "_{{ type.lower() }}.hpp"
{% endfor %}
{% for type in pod_types %}
    #include "_{{ type.lower() }}.hpp"
{% endfor %}
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

    {% for type in vector_types %}
        {
            PyTypeObject *type = define_{{ type }}_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->{{ type }}_PyTypeObject = type;
        }
        {
            PyTypeObject *type = define_{{ type }}Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->{{ type }}Array_PyTypeObject = type;
        }
        api->GamutMath{{ type }}_GetType = get_{{ type }}_type;
        api->GamutMath{{ type }}Array_GetType = get_{{ type }}Array_type;
        api->GamutMath{{ type }}_Create = create_{{ type }};
        api->GamutMath{{ type }}Array_Create = create_{{ type }}Array;
        api->GamutMath{{ type }}_GetValuePointer = get_{{ type }}_value_ptr;
        api->GamutMath{{ type }}Array_GetValuePointer = get_{{ type }}Array_value_ptr;
        api->GamutMath{{ type }}Array_GetLength = get_{{ type }}Array_length;
    {% endfor %}
    {% for type in matrix_types %}
        {
            PyTypeObject *type = define_{{ type }}_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->{{ type }}_PyTypeObject = type;
        }
        {
            PyTypeObject *type = define_{{ type }}Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->{{ type }}Array_PyTypeObject = type;
        }
        api->GamutMath{{ type }}_GetType = get_{{ type }}_type;
        api->GamutMath{{ type }}Array_GetType = get_{{ type }}Array_type;
        api->GamutMath{{ type }}_Create = create_{{ type }};
        api->GamutMath{{ type }}Array_Create = create_{{ type }}Array;
        api->GamutMath{{ type }}_GetValuePointer = get_{{ type }}_value_ptr;
        api->GamutMath{{ type }}Array_GetValuePointer = get_{{ type }}Array_value_ptr;
        api->GamutMath{{ type }}Array_GetLength = get_{{ type }}Array_length;
    {% endfor %}
    {% for type in pod_types %}
        {
            PyTypeObject *type = define_{{ type }}Array_type(module);
            if (!type){ goto error; }
            Py_INCREF(type);
            state->{{ type }}Array_PyTypeObject = type;
        }
        api->GamutMath{{ type }}Array_GetType = get_{{ type }}Array_type;
        api->GamutMath{{ type }}Array_Create = create_{{ type }}Array;
        api->GamutMath{{ type }}Array_GetValuePointer = get_{{ type }}Array_value_ptr;
        api->GamutMath{{ type }}Array_GetLength = get_{{ type }}Array_length;
    {% endfor %}

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
