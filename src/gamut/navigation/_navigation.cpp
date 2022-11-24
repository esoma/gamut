
// python
#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <structmember.h>
// stdlib
#include <iostream>
// gamut
#include "gamut/math.h"
// recast
#include "Recast.h"

#define ASSERT(x) if (!(x)){ std::cout << "ASSERTION FAILURE: " << __FILE__ << ":" << __LINE__ << std::endl; exit(1); }

// Python Structures
// ----------------------------------------------------------------------------


struct ModuleState
{
    struct GamutMathApi *math_api;
    PyTypeObject *HeightField_PyTypeObject;
};


struct CompactHeightField
{
    PyObject_HEAD
    rcCompactHeightfield *rc;
};


struct HeightField
{
    PyObject_HEAD
    rcHeightfield *rc;
    int max_traversable_ledge_height;
    int minimum_actor_height;
};


struct Mesh
{
    PyObject_HEAD
    rcConfig rc_config;
};


static ModuleState *get_module_state();


// CompactHeightField
// ----------------------------------------------------------------------------


static PyObject *
CompactHeightField___new__(PyTypeObject *cls, PyObject *args, PyObject *kwds)
{
    PyObject *py_height_field;
    static char *kwlist[] = {
        "height_field",
        NULL
    };
    if (!PyArg_ParseTupleAndKeywords(
        args, kwds, "O|", kwlist,
        &py_height_field
    )){ return 0; }

    auto state = get_module_state();
    ASSERT(Py_TYPE(py_height_field) == state->HeightField_PyTypeObject);
    HeightField *height_field = (HeightField *)py_height_field;

    int max_traversable_ledge_height = 1;
    int minimum_actor_height = 2;

    rcContext ctx;
    CompactHeightField *self = (CompactHeightField*)cls->tp_alloc(cls, 0);
    self->rc = rcAllocCompactHeightfield();
    if (!self->rc)
    {
        return PyErr_Format(
            PyExc_MemoryError,
            "failed to allocate recast compact height field"
        );
    }
    if (!rcBuildCompactHeightfield(
        &ctx,
        height_field->minimum_actor_height,
        height_field->max_traversable_ledge_height,
        *height_field->rc,
        *self->rc
    ))
	{
		return PyErr_Format(
            PyExc_RuntimeError,
            "failed build recast compact height field"
        );
	}

    return (PyObject *)self;
}


static void
CompactHeightField___dealloc__(CompactHeightField *self)
{
    if (self->rc)
    {
        rcFreeCompactHeightfield(self->rc);
        self->rc = 0;
    }

    PyTypeObject *type = Py_TYPE(self);
    type->tp_free(self);
    Py_DECREF(type);
}


static PyMemberDef CompactHeightField_PyMemberDef[] = {
    {0, 0, 0, 0}
};


static PyObject *
CompactHeightField_erode(
    CompactHeightField *self,
    PyObject *const *args,
    Py_ssize_t nargs
)
{
    ASSERT(nargs == 1);
    int max_actor_radius = PyLong_AsLong(args[0]);
    if (max_actor_radius == -1 && PyErr_Occurred())
    {
        return 0;
    }
    if (max_actor_radius < 0 || max_actor_radius >= 255)
    {
         return PyErr_Format(
            PyExc_ValueError,
            "expected: 0 < max_actor_radius < 255"
        );
    }

    rcContext ctx;
    if (!rcErodeWalkableArea(
        &ctx,
        max_actor_radius,
        *self->rc
    ))
    {
        return PyErr_Format(
            PyExc_RuntimeError,
            "failed to erode recast compact height field"
        );
    }

    Py_RETURN_NONE;
}


static PyMethodDef CompactHeightField_PyMethodDef[] = {
    {"erode", (PyCFunction)CompactHeightField_erode, METH_FASTCALL, 0},
    {0, 0, 0, 0}
};


static PyGetSetDef CompactHeightField_PyGetSetDef[] = {
    {0, 0, 0, 0, 0}
};


static PyType_Slot CompactHeightField_PyType_Slots [] = {
    {Py_tp_new, (void*)CompactHeightField___new__},
    {Py_tp_dealloc, (void*)CompactHeightField___dealloc__},
    {Py_tp_members, (void*)CompactHeightField_PyMemberDef},
    {Py_tp_methods, (void*)CompactHeightField_PyMethodDef},
    {Py_tp_getset, (void*)CompactHeightField_PyGetSetDef},
    {0, 0},
};


static PyType_Spec CompactHeightField_PyTypeSpec = {
    "gamut.navigation._navigation.CompactHeightField",
    sizeof(CompactHeightField),
    0,
    Py_TPFLAGS_DEFAULT,
    CompactHeightField_PyType_Slots
};


static PyTypeObject *
define_compact_height_field_type(PyObject *module)
{
    ASSERT(module);
    PyTypeObject *type = (PyTypeObject *)PyType_FromModuleAndSpec(
        module,
        &CompactHeightField_PyTypeSpec,
        0
    );
    if (!type){ return 0; }
    // Note:
    // Unlike other functions that steal references, PyModule_AddObject() only
    // decrements the reference count of value on success.
    if (PyModule_AddObject(module, "CompactHeightField", (PyObject *)type) < 0)
    {
        Py_DECREF(type);
        return 0;
    }
    return type;
};


// HeightField
// ----------------------------------------------------------------------------


static PyObject *
HeightField___new__(PyTypeObject *cls, PyObject *args, PyObject *kwds)
{
    int width;
    int height;
    PyObject *py_aabb_min;
    PyObject *py_aabb_max;
    float xz_cell_size;
    float y_cell_size;
    int max_traversable_ledge_height;
    int minimum_actor_height;
    static char *kwlist[] = {
        "width",
        "height",
        "aabb_min",
        "aabb_max",
        "xz_cell_size",
        "y_cell_size",
        "max_traversable_ledge_height",
        "minimum_actor_height",
        NULL
    };
    if (!PyArg_ParseTupleAndKeywords(
        args, kwds, "iiOOffii|", kwlist,
        &width, &height,
        &py_aabb_min, &py_aabb_max,
        &xz_cell_size, &y_cell_size,
        &max_traversable_ledge_height,
        &minimum_actor_height
    )){ return 0; }

    auto state = get_module_state();
    float *aabb_min = state->math_api->FVector3_GetValuePointer(py_aabb_min);
    if (!aabb_min){ return 0; }
    float *aabb_max = state->math_api->FVector3_GetValuePointer(py_aabb_max);
    if (!aabb_max){ return 0; }

    rcContext ctx;
    HeightField *self = (HeightField*)cls->tp_alloc(cls, 0);
    self->rc = rcAllocHeightfield();
    self->max_traversable_ledge_height = max_traversable_ledge_height;
    self->minimum_actor_height = minimum_actor_height;
    if (!self->rc)
    {
        return PyErr_Format(
            PyExc_MemoryError,
            "failed to allocate recast height field"
        );
    }
    if (!rcCreateHeightfield(
        &ctx,
        *self->rc,
        width,
        height,
        aabb_min,
        aabb_max,
        xz_cell_size,
        y_cell_size
    ))
	{
		return PyErr_Format(
            PyExc_RuntimeError,
            "failed create recast height field"
        );
	}

    return (PyObject *)self;
}


static void
HeightField___dealloc__(HeightField *self)
{
    if (self->rc)
    {
        rcFreeHeightField(self->rc);
        self->rc = 0;
    }

    PyTypeObject *type = Py_TYPE(self);
    type->tp_free(self);
    Py_DECREF(type);
}


static PyMemberDef HeightField_PyMemberDef[] = {
    {0, 0, 0, 0}
};


static PyObject *
HeightField_add_triangles(
    HeightField *self,
    PyObject *const *args,
    Py_ssize_t nargs
)
{
    auto state = get_module_state();
    ASSERT(nargs == 1);

    rcContext ctx;
    PyObject *tris = PyObject_GetIter(args[0]);
    ASSERT(tris);
    PyObject *tri;
    while (tri = PyIter_Next(tris))
    {
        PyObject *py_v0 = 0;
        PyObject *py_v1 = 0;
        PyObject *py_v2 = 0;

        py_v0 = PySequence_GetItem(tri, 0);
        if (!py_v0){ goto loop_error; }
        float *v0 = state->math_api->FVector3_GetValuePointer(py_v0);
        if (!v0){ goto loop_error; }

        py_v1 = PySequence_GetItem(tri, 1);
        if (!py_v1){ goto loop_error; }
        float *v1 = state->math_api->FVector3_GetValuePointer(py_v1);
        if (!v1){ goto loop_error; }

        py_v2 = PySequence_GetItem(tri, 2);
        if (!py_v2){ goto loop_error; }
        float *v2 = state->math_api->FVector3_GetValuePointer(py_v2);
        if (!v2){ goto loop_error; }
        rcRasterizeTriangle(
            &ctx,
            v0, v1, v2,
            RC_WALKABLE_AREA,
            *self->rc,
            self->max_traversable_ledge_height
        );

        Py_DECREF(py_v0);
        Py_DECREF(py_v1);
        Py_DECREF(py_v2);
        Py_DECREF(tri);
        continue;
loop_error:
        Py_XDECREF(py_v0);
        Py_XDECREF(py_v1);
        Py_XDECREF(py_v2);
        Py_DECREF(tri);
        Py_DECREF(tris);
        return 0;
    }
    Py_DECREF(tris);
    Py_RETURN_NONE;
}


static PyObject *
HeightField_filter(
    HeightField *self,
    PyObject *const *args,
    Py_ssize_t nargs
)
{
    ASSERT(nargs == 0);

    rcContext ctx;
    rcFilterLowHangingWalkableObstacles(
        &ctx,
        self->max_traversable_ledge_height,
        *self->rc
    );
    rcFilterLedgeSpans(
        &ctx,
        self->minimum_actor_height,
        self->max_traversable_ledge_height,
        *self->rc
    );
    rcFilterWalkableLowHeightSpans(
        &ctx,
        self->minimum_actor_height,
        *self->rc
    );

    Py_RETURN_NONE;
}


static PyMethodDef HeightField_PyMethodDef[] = {
    {"add_triangles", (PyCFunction)HeightField_add_triangles, METH_FASTCALL, 0},
    {"filter", (PyCFunction)HeightField_filter, METH_FASTCALL, 0},
    {0, 0, 0, 0}
};


static PyGetSetDef HeightField_PyGetSetDef[] = {
    {0, 0, 0, 0, 0}
};


static PyType_Slot HeightField_PyType_Slots [] = {
    {Py_tp_new, (void*)HeightField___new__},
    {Py_tp_dealloc, (void*)HeightField___dealloc__},
    {Py_tp_members, (void*)HeightField_PyMemberDef},
    {Py_tp_methods, (void*)HeightField_PyMethodDef},
    {Py_tp_getset, (void*)HeightField_PyGetSetDef},
    {0, 0},
};


static PyType_Spec HeightField_PyTypeSpec = {
    "gamut.navigation._navigation.HeightField",
    sizeof(HeightField),
    0,
    Py_TPFLAGS_DEFAULT,
    HeightField_PyType_Slots
};


static PyTypeObject *
define_height_field_type(PyObject *module)
{
    ASSERT(module);
    PyTypeObject *type = (PyTypeObject *)PyType_FromModuleAndSpec(
        module,
        &HeightField_PyTypeSpec,
        0
    );
    if (!type){ return 0; }
    // Note:
    // Unlike other functions that steal references, PyModule_AddObject() only
    // decrements the reference count of value on success.
    if (PyModule_AddObject(module, "HeightField", (PyObject *)type) < 0)
    {
        Py_DECREF(type);
        return 0;
    }
    return type;
};


// Mesh
// ----------------------------------------------------------------------------


static PyObject *
Mesh___new__(PyTypeObject *cls, PyObject *args, PyObject *kwds)
{
    static char *kwlist[] = {NULL};
    if (!PyArg_ParseTupleAndKeywords(
        args, kwds, "", kwlist
    )){ return 0; }

    Mesh *self = (Mesh*)cls->tp_alloc(cls, 0);

    return (PyObject *)self;
}


static void
Mesh___dealloc__(Mesh *self)
{
    PyTypeObject *type = Py_TYPE(self);
    type->tp_free(self);
    Py_DECREF(type);
}


static PyMemberDef Mesh_PyMemberDef[] = {
    {0, 0, 0, 0}
};


static PyMethodDef Mesh_PyMethodDef[] = {
    {0, 0, 0, 0}
};


static PyGetSetDef Mesh_PyGetSetDef[] = {
    {0, 0, 0, 0, 0}
};


static PyType_Slot Mesh_PyType_Slots [] = {
    {Py_tp_new, (void*)Mesh___new__},
    {Py_tp_dealloc, (void*)Mesh___dealloc__},
    {Py_tp_members, (void*)Mesh_PyMemberDef},
    {Py_tp_methods, (void*)Mesh_PyMethodDef},
    {Py_tp_getset, (void*)Mesh_PyGetSetDef},
    {0, 0},
};


static PyType_Spec Mesh_PyTypeSpec = {
    "gamut.navigation._navigation.Mesh",
    sizeof(Mesh),
    0,
    Py_TPFLAGS_DEFAULT,
    Mesh_PyType_Slots
};


static PyTypeObject *
define_mesh_type(PyObject *module)
{
    ASSERT(module);
    PyTypeObject *type = (PyTypeObject *)PyType_FromModuleAndSpec(
        module,
        &Mesh_PyTypeSpec,
        0
    );
    if (!type){ return 0; }
    // Note:
    // Unlike other functions that steal references, PyModule_AddObject() only
    // decrements the reference count of value on success.
    if (PyModule_AddObject(module, "Mesh", (PyObject *)type) < 0)
    {
        Py_DECREF(type);
        return 0;
    }
    return type;
};

// module
// ----------------------------------------------------------------------------

static PyMethodDef module_methods[] = {
    {0, 0, 0, 0}
};


static int
module_traverse(
    PyObject *self,
    visitproc visit,
    void *arg
)
{
    ModuleState *state = (ModuleState *)PyModule_GetState(self);
    Py_VISIT(state->HeightField_PyTypeObject);
    return 0;
}


static int
module_clear(PyObject *self)
{
    ModuleState *state = (ModuleState *)PyModule_GetState(self);
    Py_CLEAR(state->HeightField_PyTypeObject);
    return 0;
}


static void
module_free(void* self)
{
    GamutMathApi_Release();
}


static struct PyModuleDef module_PyModuleDef = {
    PyModuleDef_HEAD_INIT,
    "gamut.navigation._navigation",
    0,
    sizeof(struct ModuleState),
    module_methods,
    0,
    module_traverse,
    module_clear,
    module_free
};


PyMODINIT_FUNC
PyInit__navigation()
{
    ModuleState *state = 0;
    PyObject *module = PyModule_Create(&module_PyModuleDef);
    if (!module){ goto error; }

    if (PyState_AddModule(module, &module_PyModuleDef) == -1){ goto error; }
    state = (ModuleState *)PyModule_GetState(module);

    if (!define_compact_height_field_type(module)){ goto error; }

    PyTypeObject *py_height_field_type = define_height_field_type(module);
    {
        if (!py_height_field_type){ goto error; }
        Py_INCREF(py_height_field_type);
        state->HeightField_PyTypeObject = py_height_field_type;
    }

    if (!define_mesh_type(module)){ goto error; }

    state->math_api = GamutMathApi_Get();
    if (!state->math_api){ goto error; }

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
        return PyErr_Format(PyExc_RuntimeError, "navigation module not ready");
    }
    return module;
}


static ModuleState *
get_module_state()
{
    PyObject *module = get_module();
    if (!module){ return 0; }
    return (ModuleState *)PyModule_GetState(module);
}

