
// generated {{ when }} from codegen/math/templates/_modulestate.hpp

#ifndef GAMUT_MATH_MODULESTATE_HPP
#define GAMUT_MATH_MODULESTATE_HPP

// python
#define PY_SSIZE_T_CLEAN
#include <Python.h>
// gamut
#include "_module.hpp"

struct ModuleState
{
    {% for type in types %}
        PyTypeObject *{{ type }}_PyTypeObject;
        PyTypeObject *{{ type }}Array_PyTypeObject;
    {% endfor %}
    {% for pod_type in pod_types %}
        PyTypeObject *{{ pod_type }}Array_PyTypeObject;
    {% endfor %}
};


static int
ModuleState_traverse(
    struct ModuleState *self,
    visitproc visit,
    void *arg
)
{
    {% for type in types %}
        Py_VISIT(self->{{ type }}_PyTypeObject);
        Py_VISIT(self->{{ type }}Array_PyTypeObject);
    {% endfor %}
    {% for pod_type in pod_types %}
        Py_VISIT(self->{{ pod_type }}Array_PyTypeObject);
    {% endfor %}
    return 0;
}


static int
ModuleState_clear(struct ModuleState *self)
{
    {% for type in types %}
        Py_CLEAR(self->{{ type }}_PyTypeObject);
        Py_CLEAR(self->{{ type }}Array_PyTypeObject);
    {% endfor %}
    {% for pod_type in pod_types %}
        Py_CLEAR(self->{{ pod_type }}Array_PyTypeObject);
    {% endfor %}
    return 0;
}


static ModuleState *
get_module_state()
{
    PyObject *module = get_module();
    if (!module){ return 0; }
    return (ModuleState *)PyModule_GetState(module);
}

#endif