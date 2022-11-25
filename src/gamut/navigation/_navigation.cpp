
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
// detour
#include "DetourNavMesh.h"
#include "DetourNavMeshBuilder.h"
#include "DetourNavMeshQuery.h"

#define ASSERT(x) if (!(x)){ std::cout << "ASSERTION FAILURE: " << __FILE__ << ":" << __LINE__ << std::endl; exit(1); }

// Python Structures
// ----------------------------------------------------------------------------


struct ModuleState
{
    struct GamutMathApi *math_api;
    PyTypeObject *CompactHeightField_PyTypeObject;
    PyTypeObject *ContourSet_PyTypeObject;
    PyTypeObject *DetailMesh_PyTypeObject;
    PyTypeObject *HeightField_PyTypeObject;
    PyTypeObject *Mesh_PyTypeObject;
    PyTypeObject *NavigationMesh_PyTypeObject;
};


struct CompactHeightField
{
    PyObject_HEAD
    rcCompactHeightfield *rc;
    int max_actor_radius;
    int max_traversable_ledge_height;
    int min_actor_height;
};


struct ContourSet
{
    PyObject_HEAD
    rcContourSet *rc;
    int max_actor_radius;
    int max_traversable_ledge_height;
    int min_actor_height;
};


struct DetailMesh
{
    PyObject_HEAD
    rcPolyMeshDetail *rc;
};


struct HeightField
{
    PyObject_HEAD
    rcHeightfield *rc;
    int max_traversable_ledge_height;
    int min_actor_height;
};


struct Mesh
{
    PyObject_HEAD
    rcPolyMesh *rc;
    int max_actor_radius;
    int max_traversable_ledge_height;
    int min_actor_height;
};


struct NavigationMesh
{
    PyObject_HEAD
    dtNavMesh *dt;
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
        height_field->min_actor_height,
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
    self->max_actor_radius = 0;
    self->min_actor_height = height_field->min_actor_height;
    self->max_traversable_ledge_height =
        height_field->max_traversable_ledge_height;

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
    if (nargs != 1)
    {
        return PyErr_Format(
            PyExc_TypeError,
            "expected 1 arg: amount"
        );
    }
    int amount = PyLong_AsLong(args[0]);
    if (PyErr_Occurred()){ return 0; }
    if (amount < 0 || amount >= 255)
    {
         return PyErr_Format(
            PyExc_ValueError,
            "expected: 0 < amount < 255"
        );
    }

    rcContext ctx;
    if (!rcErodeWalkableArea(
        &ctx,
        amount,
        *self->rc
    ))
    {
        return PyErr_Format(
            PyExc_RuntimeError,
            "failed to erode recast compact height field"
        );
    }
    self->max_actor_radius += amount;

    Py_RETURN_NONE;
}


static PyObject *
CompactHeightField_partition_layers(
    CompactHeightField *self,
    PyObject *const *args,
    Py_ssize_t nargs
)
{
    if (nargs != 2)
    {
        return PyErr_Format(
            PyExc_TypeError,
            "expected 2 args: border_size, minimum_region_area"
        );
    }
    int border_size = PyLong_AsLong(args[0]);
    if (PyErr_Occurred()){ return 0; }
    if (border_size < 0)
    {
         return PyErr_Format(PyExc_ValueError, "expected: border_size >= 0");
    }

    int minimum_region_area = PyLong_AsLong(args[1]);
    if (PyErr_Occurred()){ return 0; }
    if (minimum_region_area < 0)
    {
         return PyErr_Format(
            PyExc_ValueError,
            "expected: minimum_region_area >= 0"
        );
    }

    rcContext ctx;
    if (!rcBuildLayerRegions(
        &ctx,
        *self->rc,
        border_size,
        minimum_region_area
    ))
    {
        return PyErr_Format(
            PyExc_RuntimeError,
            "failed to build regions"
        );
    }

    Py_RETURN_NONE;
}


static PyObject *
CompactHeightField_partition_monotone(
    CompactHeightField *self,
    PyObject *const *args,
    Py_ssize_t nargs
)
{
    if (nargs != 3)
    {
        return PyErr_Format(
            PyExc_TypeError,
            "expected 3 args: border_size, minimum_region_area, "
            "merge_region_area"
        );
    }
    int border_size = PyLong_AsLong(args[0]);
    if (PyErr_Occurred()){ return 0; }
    if (border_size < 0)
    {
         return PyErr_Format(PyExc_ValueError, "expected: border_size >= 0");
    }

    int minimum_region_area = PyLong_AsLong(args[1]);
    if (PyErr_Occurred()){ return 0; }
    if (minimum_region_area < 0)
    {
         return PyErr_Format(
            PyExc_ValueError,
            "expected: minimum_region_area >= 0"
        );
    }

    int merge_region_area = PyLong_AsLong(args[2]);
    if (PyErr_Occurred()){ return 0; }
    if (merge_region_area < 0)
    {
         return PyErr_Format(
            PyExc_ValueError,
            "expected: merge_region_area >= 0"
        );
    }

    rcContext ctx;
    if (!rcBuildRegionsMonotone(
        &ctx,
        *self->rc,
        border_size,
        minimum_region_area,
        merge_region_area
    ))
    {
        return PyErr_Format(
            PyExc_RuntimeError,
            "failed to build regions"
        );
    }

    Py_RETURN_NONE;
}


static PyObject *
CompactHeightField_partition_watershed(
    CompactHeightField *self,
    PyObject *const *args,
    Py_ssize_t nargs
)
{
    if (nargs != 3)
    {
        return PyErr_Format(
            PyExc_TypeError,
            "expected 3 args: border_size, minimum_region_area, "
            "merge_region_area"
        );
    }
    int border_size = PyLong_AsLong(args[0]);
    if (PyErr_Occurred()){ return 0; }
    if (border_size < 0)
    {
         return PyErr_Format(PyExc_ValueError, "expected: border_size >= 0");
    }

    int minimum_region_area = PyLong_AsLong(args[1]);
    if (PyErr_Occurred()){ return 0; }
    if (minimum_region_area < 0)
    {
         return PyErr_Format(
            PyExc_ValueError,
            "expected: minimum_region_area >= 0"
        );
    }

    int merge_region_area = PyLong_AsLong(args[2]);
    if (PyErr_Occurred()){ return 0; }
    if (merge_region_area < 0)
    {
         return PyErr_Format(
            PyExc_ValueError,
            "expected: merge_region_area >= 0"
        );
    }

    rcContext ctx;
    if (!rcBuildDistanceField(&ctx, *self->rc))
    {
        return PyErr_Format(
            PyExc_RuntimeError,
            "failed to build distance field"
        );
    }
    if (!rcBuildRegions(
        &ctx,
        *self->rc,
        border_size,
        minimum_region_area,
        merge_region_area
    ))
    {
        return PyErr_Format(
            PyExc_RuntimeError,
            "failed to build regions"
        );
    }

    Py_RETURN_NONE;
}


static PyMethodDef CompactHeightField_PyMethodDef[] = {
    {"erode", (PyCFunction)CompactHeightField_erode, METH_FASTCALL, 0},
    {
        "partition_layers",
        (PyCFunction)CompactHeightField_partition_layers,
        METH_FASTCALL,
        0
    },
    {
        "partition_monotone",
        (PyCFunction)CompactHeightField_partition_monotone,
        METH_FASTCALL,
        0
    },
    {
        "partition_watershed",
        (PyCFunction)CompactHeightField_partition_watershed,
        METH_FASTCALL,
        0
    },
    //mark convex volumes?
    {0, 0, 0, 0}
};


static PyObject *
CompactHeightField_Getter_spans(CompactHeightField *self, void *)
{
    auto state = get_module_state();
    PyObject *py_result = PyList_New(0);
    if (!py_result){ return 0; }
    for (int z = 0; z < self->rc->height; ++z)
    {
        for (int x = 0; x < self->rc->width; ++x)
        {
            float min[] = {
                self->rc->bmin[0] + x * self->rc->cs,
                0,
                self->rc->bmin[2] + z * self->rc->cs
            };
            float max[] = {
                min[0] + self->rc->cs,
                0,
                min[2] + self->rc->cs
            };
            const rcCompactCell &cell = self->rc->cells[
                x + z * self->rc->width
            ];
            for (
                unsigned int i = cell.index,
                ni = cell.index + cell.count;
                i < ni;
                ++i
            )
            {
                const rcCompactSpan& span = self->rc->spans[i];
                min[1] = self->rc->bmin[1] + span.y * self->rc->ch;
                max[1] = min[1] + self->rc->ch;

                PyObject *py_span = PyTuple_New(4);
                if (!py_span){ goto error; }
                if (PyList_Append(py_result, py_span) != 0)
                {
                    Py_DECREF(py_span);
                    goto error;
                }

                PyObject *py_min = state->math_api->FVector3_Create(min);
                if (!py_min){ goto error; }
                PyTuple_SET_ITEM(py_span, 0, py_min);

                PyObject *py_max = state->math_api->FVector3_Create(max);
                if (!py_max){ goto error; }
                PyTuple_SET_ITEM(py_span, 1, py_max);

                PyObject *py_walkable = PyBool_FromLong(
                    self->rc->areas[i] & RC_WALKABLE_AREA
                );
                if (!py_walkable){ goto error; }
                PyTuple_SET_ITEM(py_span, 2, py_walkable);

                PyObject *py_region_id = PyLong_FromUnsignedLong(span.reg);
                if (!py_region_id){ goto error; }
                PyTuple_SET_ITEM(py_span, 3, py_region_id);

                continue;
error:
                Py_DECREF(py_result);
                return 0;
            }
        }
    }
    return py_result;
}


static PyGetSetDef CompactHeightField_PyGetSetDef[] = {
    {
        "spans",
        (getter)CompactHeightField_Getter_spans,
        0,
        0,
        0
    },
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


// ContourSet
// ----------------------------------------------------------------------------


static PyObject *
ContourSet___new__(PyTypeObject *cls, PyObject *args, PyObject *kwds)
{
    PyObject *py_compact_height_field;
    float max_simplification_error;
    int max_edge_length;
    static char *kwlist[] = {
        "compact_height_field",
        "max_simplification_error",
        "max_edge_length",
        NULL
    };
    if (!PyArg_ParseTupleAndKeywords(
        args, kwds, "Ofi|", kwlist,
        &py_compact_height_field,
        &max_simplification_error,
        &max_edge_length
    )){ return 0; }

    auto state = get_module_state();
    ASSERT(
        Py_TYPE(py_compact_height_field) ==
        state->CompactHeightField_PyTypeObject
    );
    CompactHeightField *compact_height_field =
        (CompactHeightField *)py_compact_height_field;

    rcContext ctx;
    ContourSet *self = (ContourSet*)cls->tp_alloc(cls, 0);
    self->rc = rcAllocContourSet();
    if (!self->rc)
    {
        return PyErr_Format(
            PyExc_MemoryError,
            "failed to allocate recast contour set"
        );
    }
    if (!rcBuildContours(
        &ctx,
        *compact_height_field->rc,
        max_simplification_error,
        max_edge_length,
        *self->rc
    ))
	{
		return PyErr_Format(
            PyExc_RuntimeError,
            "failed build recast contour set"
        );
	}
    self->max_actor_radius = compact_height_field->max_actor_radius;
    self->max_traversable_ledge_height =
        compact_height_field->max_traversable_ledge_height;
    self->min_actor_height = compact_height_field->min_actor_height;

    return (PyObject *)self;
}


static void
ContourSet___dealloc__(ContourSet *self)
{
    if (self->rc)
    {
        rcFreeContourSet(self->rc);
        self->rc = 0;
    }

    PyTypeObject *type = Py_TYPE(self);
    type->tp_free(self);
    Py_DECREF(type);
}


static PyMemberDef ContourSet_PyMemberDef[] = {
    {0, 0, 0, 0}
};


static PyMethodDef ContourSet_PyMethodDef[] = {
    {0, 0, 0, 0}
};


static PyGetSetDef ContourSet_PyGetSetDef[] = {
    {0, 0, 0, 0, 0}
};


static PyType_Slot ContourSet_PyType_Slots [] = {
    {Py_tp_new, (void*)ContourSet___new__},
    {Py_tp_dealloc, (void*)ContourSet___dealloc__},
    {Py_tp_members, (void*)ContourSet_PyMemberDef},
    {Py_tp_methods, (void*)ContourSet_PyMethodDef},
    {Py_tp_getset, (void*)ContourSet_PyGetSetDef},
    {0, 0},
};


static PyType_Spec ContourSet_PyTypeSpec = {
    "gamut.navigation._navigation.ContourSet",
    sizeof(ContourSet),
    0,
    Py_TPFLAGS_DEFAULT,
    ContourSet_PyType_Slots
};


static PyTypeObject *
define_contour_set_type(PyObject *module)
{
    ASSERT(module);
    PyTypeObject *type = (PyTypeObject *)PyType_FromModuleAndSpec(
        module,
        &ContourSet_PyTypeSpec,
        0
    );
    if (!type){ return 0; }
    // Note:
    // Unlike other functions that steal references, PyModule_AddObject() only
    // decrements the reference count of value on success.
    if (PyModule_AddObject(module, "ContourSet", (PyObject *)type) < 0)
    {
        Py_DECREF(type);
        return 0;
    }
    return type;
};


// DetailMesh
// ----------------------------------------------------------------------------


static PyObject *
DetailMesh___new__(PyTypeObject *cls, PyObject *args, PyObject *kwds)
{
    auto state = get_module_state();
    PyObject *py_mesh;
    PyObject *py_compact_height_field;
    float sample_distance;
    float sample_max_distance_error;
    static char *kwlist[] = {
        "mesh",
        "compact_height_field",
        "sample_distance",
        "sample_max_distance_error",
        NULL
    };
    if (!PyArg_ParseTupleAndKeywords(
        args, kwds, "OOff|", kwlist,
        &py_mesh,
        &py_compact_height_field,
        &sample_distance,
        &sample_max_distance_error
    )){ return 0; }

    if (Py_TYPE(py_mesh) != state->Mesh_PyTypeObject)
    {
        return PyErr_Format(PyExc_TypeError, "expected Mesh");
    }
    Mesh *mesh = (Mesh *)py_mesh;

    if (Py_TYPE(py_compact_height_field) != state->CompactHeightField_PyTypeObject)
    {
        return PyErr_Format(PyExc_TypeError, "expected CompactHeightField");
    }
    CompactHeightField *compact_height_field =
        (CompactHeightField *)py_compact_height_field;

    if (sample_distance < 0)
    {
        return PyErr_Format(
            PyExc_ValueError,
            "expected: sample_distance >= 0"
        );
    }
    if (sample_max_distance_error < 0)
    {
        return PyErr_Format(
            PyExc_ValueError,
            "expected: sample_max_distance_error >= 0"
        );
    }

    rcContext ctx;
    DetailMesh *self = (DetailMesh*)cls->tp_alloc(cls, 0);
    self->rc = rcAllocPolyMeshDetail();
    if (!self->rc)
    {
        return PyErr_Format(
            PyExc_MemoryError,
            "failed to allocate recast poly detail mesh"
        );
    }
    if (!rcBuildPolyMeshDetail(
        &ctx,
        *mesh->rc,
        *compact_height_field->rc,
        sample_distance,
        sample_max_distance_error,
        *self->rc
    ))
	{
		return PyErr_Format(
            PyExc_RuntimeError,
            "failed build recast poly detail mesh"
        );
	}

    return (PyObject *)self;
}


static void
DetailMesh___dealloc__(DetailMesh *self)
{
    if (self->rc)
    {
        rcFreePolyMeshDetail(self->rc);
        self->rc = 0;
    }

    PyTypeObject *type = Py_TYPE(self);
    type->tp_free(self);
    Py_DECREF(type);
}


static PyMemberDef DetailMesh_PyMemberDef[] = {
    {0, 0, 0, 0}
};


static PyMethodDef DetailMesh_PyMethodDef[] = {
    {0, 0, 0, 0}
};


static PyObject *
DetailMesh_Getter_meshes(DetailMesh *self, void *)
{
    auto state = get_module_state();
    PyObject *py_result = PyList_New(0);
    if (!py_result){ return 0; }
    for (int i = 0; i < self->rc->nmeshes; ++i)
    {
        auto base_vertex_index = self->rc->meshes[i * 4];
        auto vertices = &self->rc->verts[base_vertex_index * 3];

        auto base_tri_index = self->rc->meshes[i * 4 + 2];
        auto tris = &self->rc->tris[base_tri_index * 4];

        auto tri_count = self->rc->meshes[i * 4 + 3];

        PyObject *py_vertices = PyList_New(0);
        if (!py_vertices){ goto error; }
        if (PyList_Append(py_result, py_vertices) != 0)
        {
            Py_DECREF(py_vertices);
            goto error;
        }

        for (unsigned char j = 0; j < tri_count; ++j)
        {
            auto tri = &tris[j * 4];
            for (int v = 0; v < 3; ++v)
            {
                float *vertex = &vertices[tri[v] * 3];
                PyObject *py_vertex = state->math_api->FVector3_Create(vertex);
                if (!py_vertex){ goto error; }
                if (PyList_Append(py_vertices, py_vertex) != 0)
                {
                    Py_DECREF(py_vertex);
                    goto error;
                }
            }
        }
    }
    return py_result;
error:
    Py_DECREF(py_result);
    return 0;
}


static PyGetSetDef DetailMesh_PyGetSetDef[] = {
    {
        "meshes",
        (getter)DetailMesh_Getter_meshes,
        0,
        0,
        0
    },
    {0, 0, 0, 0, 0}
};


static PyType_Slot DetailMesh_PyType_Slots [] = {
    {Py_tp_new, (void*)DetailMesh___new__},
    {Py_tp_dealloc, (void*)DetailMesh___dealloc__},
    {Py_tp_members, (void*)DetailMesh_PyMemberDef},
    {Py_tp_methods, (void*)DetailMesh_PyMethodDef},
    {Py_tp_getset, (void*)DetailMesh_PyGetSetDef},
    {0, 0},
};


static PyType_Spec DetailMesh_PyTypeSpec = {
    "gamut.navigation._navigation.DetailMesh",
    sizeof(DetailMesh),
    0,
    Py_TPFLAGS_DEFAULT,
    DetailMesh_PyType_Slots
};


static PyTypeObject *
define_detail_mesh_type(PyObject *module)
{
    ASSERT(module);
    PyTypeObject *type = (PyTypeObject *)PyType_FromModuleAndSpec(
        module,
        &DetailMesh_PyTypeSpec,
        0
    );
    if (!type){ return 0; }
    // Note:
    // Unlike other functions that steal references, PyModule_AddObject() only
    // decrements the reference count of value on success.
    if (PyModule_AddObject(module, "DetailMesh", (PyObject *)type) < 0)
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
    int min_actor_height;
    static char *kwlist[] = {
        "width",
        "height",
        "aabb_min",
        "aabb_max",
        "xz_cell_size",
        "y_cell_size",
        "max_traversable_ledge_height",
        "min_actor_height",
        NULL
    };
    if (!PyArg_ParseTupleAndKeywords(
        args, kwds, "iiOOffii|", kwlist,
        &width, &height,
        &py_aabb_min, &py_aabb_max,
        &xz_cell_size, &y_cell_size,
        &max_traversable_ledge_height,
        &min_actor_height
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
    self->min_actor_height = min_actor_height;
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
        self->min_actor_height,
        self->max_traversable_ledge_height,
        *self->rc
    );
    rcFilterWalkableLowHeightSpans(
        &ctx,
        self->min_actor_height,
        *self->rc
    );

    Py_RETURN_NONE;
}


static PyMethodDef HeightField_PyMethodDef[] = {
    {"add_triangles", (PyCFunction)HeightField_add_triangles, METH_FASTCALL, 0},
    {"filter", (PyCFunction)HeightField_filter, METH_FASTCALL, 0},
    {0, 0, 0, 0}
};


static PyObject *
HeightField_Getter_aabb_max(HeightField *self, void *)
{
    auto state = get_module_state();
    return state->math_api->FVector3_Create(self->rc->bmax);
}


static PyObject *
HeightField_Getter_aabb_min(HeightField *self, void *)
{
    auto state = get_module_state();
    return state->math_api->FVector3_Create(self->rc->bmin);
}


static PyObject *
HeightField_Getter_height(HeightField *self, void *)
{
    return PyLong_FromLong(self->rc->height);
}


static PyObject *
HeightField_Getter_spans(HeightField *self, void *)
{
    auto state = get_module_state();
    PyObject *py_result = PyList_New(0);
    if (!py_result){ return 0; }
    for (int z = 0; z < self->rc->height; ++z)
    {
        for (int x = 0; x < self->rc->width; ++x)
        {
            const rcSpan *span = self->rc->spans[x + z * self->rc->width];
            float min[] = {
                self->rc->bmin[0] + x * self->rc->cs,
                0,
                self->rc->bmin[2] + z * self->rc->cs
            };
            float max[] = {
                min[0] + self->rc->cs,
                0,
                min[2] + self->rc->cs
            };
            while (span)
            {
                min[1] = self->rc->bmin[1] + span->smin * self->rc->ch;
                max[1] = self->rc->bmin[1] + span->smax * self->rc->ch;

                PyObject *py_span = PyTuple_New(3);
                if (!py_span){ goto error; }
                if (PyList_Append(py_result, py_span) != 0)
                {
                    Py_DECREF(py_span);
                    goto error;
                }

                PyObject *py_min = state->math_api->FVector3_Create(min);
                if (!py_min){ goto error; }
                PyTuple_SET_ITEM(py_span, 0, py_min);

                PyObject *py_max = state->math_api->FVector3_Create(max);
                if (!py_max){ goto error; }
                PyTuple_SET_ITEM(py_span, 1, py_max);

                PyObject *py_walkable = PyBool_FromLong(
                    span->area & RC_WALKABLE_AREA
                );
                if (!py_walkable){ goto error; }
                PyTuple_SET_ITEM(py_span, 2, py_walkable);

                span = span->next;
                continue;
error:
                Py_DECREF(py_result);
                return 0;
            }
        }
    }
    return py_result;
}


static PyObject *
HeightField_Getter_width(HeightField *self, void *)
{
    return PyLong_FromLong(self->rc->width);
}


static PyGetSetDef HeightField_PyGetSetDef[] = {
    {
        "aabb_max",
        (getter)HeightField_Getter_aabb_max,
        0,
        0,
        0
    },
    {
        "aabb_min",
        (getter)HeightField_Getter_aabb_min,
        0,
        0,
        0
    },
    {
        "height",
        (getter)HeightField_Getter_height,
        0,
        0,
        0
    },
    {
        "spans",
        (getter)HeightField_Getter_spans,
        0,
        0,
        0
    },
    {
        "width",
        (getter)HeightField_Getter_width,
        0,
        0,
        0
    },
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
    auto state = get_module_state();
    PyObject *py_contour_set;
    int max_vertices_per_polygon;
    static char *kwlist[] = {
        "contour_set",
        "max_vertices_per_polygon",
        NULL
    };
    if (!PyArg_ParseTupleAndKeywords(
        args, kwds, "Oi|", kwlist,
        &py_contour_set,
        &max_vertices_per_polygon
    )){ return 0; }

    if (Py_TYPE(py_contour_set) != state->ContourSet_PyTypeObject)
    {
        return PyErr_Format(PyExc_TypeError, "expected: ContourSet");
    }
    ContourSet *contour_set = (ContourSet *)py_contour_set;
    if (max_vertices_per_polygon < 3)
    {
        return PyErr_Format(
            PyExc_ValueError,
            "expected: max_vertices_per_polygon >= 3"
        );
    }

    rcContext ctx;
    Mesh *self = (Mesh*)cls->tp_alloc(cls, 0);
    self->rc = rcAllocPolyMesh();
    if (!self->rc)
    {
        return PyErr_Format(
            PyExc_MemoryError,
            "failed to allocate recast poly mesh"
        );
    }
    if (!rcBuildPolyMesh(
        &ctx,
        *contour_set->rc,
        max_vertices_per_polygon,
        *self->rc
    ))
	{
		return PyErr_Format(
            PyExc_RuntimeError,
            "failed build recast poly mesh"
        );
	}
    self->max_actor_radius = contour_set->max_actor_radius;
    self->max_traversable_ledge_height =
        contour_set->max_traversable_ledge_height;
    self->min_actor_height = contour_set->min_actor_height;

    // XXX
    for (int i = 0; i < self->rc->npolys; ++i)
    {
        self->rc->flags[i] = 1;
    }

    return (PyObject *)self;
}


static void
Mesh___dealloc__(Mesh *self)
{
    if (self->rc)
    {
        rcFreePolyMesh(self->rc);
        self->rc = 0;
    }

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


static PyObject *
Mesh_Getter_polygons(Mesh *self, void *)
{
    auto state = get_module_state();
    PyObject *py_result = PyList_New(0);
    if (!py_result){ return 0; }
    for (int i = 0; i < self->rc->npolys; ++i)
    {
        PyObject *py_polygon = PyTuple_New(3);
        if (!py_polygon){ goto error; }
        if (PyList_Append(py_result, py_polygon) != 0)
        {
            Py_DECREF(py_polygon);
            goto error;
        }

        PyObject *py_walkable = PyBool_FromLong(
            self->rc->areas[i] & RC_WALKABLE_AREA
        );
        if (!py_walkable){ goto error; }
        PyTuple_SET_ITEM(py_polygon, 0, py_walkable);

        PyObject *py_region = PyLong_FromUnsignedLong(self->rc->regs[i]);
        if (!py_region){ goto error; }
        PyTuple_SET_ITEM(py_polygon, 1, py_region);

        const unsigned short *poly = &self->rc->polys[i * self->rc->nvp * 2];
        PyObject *py_vertices = PyList_New(0);
        if (!py_vertices){ goto error; }
        PyTuple_SET_ITEM(py_polygon, 2, py_vertices);
        for (int j = 0; j < self->rc->nvp; ++j)
        {
            if (poly[j] == RC_MESH_NULL_IDX){ break; }
            auto vertex_indexes = &self->rc->verts[poly[j] * 3];
            float vertex[] = {
                self->rc->bmin[0] + vertex_indexes[0] * self->rc->cs,
                self->rc->bmin[1] + vertex_indexes[1] * self->rc->ch,
                self->rc->bmin[2] + vertex_indexes[2] * self->rc->cs
            };
            PyObject *py_vertex = state->math_api->FVector3_Create(vertex);
            if (!py_vertex){ goto error; }
            if (PyList_Append(py_vertices, py_vertex) != 0)
            {
                Py_DECREF(py_vertex);
                goto error;
            }
        }
    }
    return py_result;
error:
    Py_DECREF(py_result);
    return 0;
}


static PyGetSetDef Mesh_PyGetSetDef[] = {
    {
        "polygons",
        (getter)Mesh_Getter_polygons,
        0,
        0,
        0
    },
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


// NavigationMesh
// ----------------------------------------------------------------------------


static PyObject *
NavigationMesh___new__(PyTypeObject *cls, PyObject *args, PyObject *kwds)
{
    auto state = get_module_state();
    PyObject *py_mesh;
    PyObject *py_detail_mesh = 0;
    static char *kwlist[] = {
        "mesh",
        "detail_mesh",
        NULL
    };
    if (!PyArg_ParseTupleAndKeywords(
        args, kwds, "O|$O", kwlist,
        &py_mesh,
        &py_detail_mesh
    )){ return 0; }

    if (Py_TYPE(py_mesh) != state->Mesh_PyTypeObject)
    {
        return PyErr_Format(PyExc_TypeError, "expected Mesh");
    }
    Mesh *mesh = (Mesh *)py_mesh;

    if (mesh->rc->nverts >= 0xffff)
    {
        // The vertex indices are ushorts, and cannot point to more than 0xffff vertices.
		return PyErr_Format(
            PyExc_ValueError,
            "Mesh has too many vertices"
        );
    }

    DetailMesh *detail_mesh = 0;
    if (py_detail_mesh)
    {
        if (Py_TYPE(py_detail_mesh) != state->DetailMesh_PyTypeObject)
        {
            return PyErr_Format(PyExc_TypeError, "expected DetailMesh");
        }
        detail_mesh = (DetailMesh *)py_detail_mesh;
    }

    NavigationMesh *self = (NavigationMesh*)cls->tp_alloc(cls, 0);
    self->dt = dtAllocNavMesh();
    if (!self->dt)
    {
        return PyErr_Format(
            PyExc_MemoryError,
            "failed to allocate detour nav mesh"
        );
    }

    dtNavMeshCreateParams params;
    memset(&params, 0, sizeof(params));
    params.verts = mesh->rc->verts;
    params.vertCount = mesh->rc->nverts;
    params.polys = mesh->rc->polys;
    params.polyAreas = mesh->rc->areas;
    params.polyFlags = mesh->rc->flags;
    params.polyCount = mesh->rc->npolys;
    params.nvp = mesh->rc->nvp;
    rcVcopy(params.bmin, mesh->rc->bmin);
    rcVcopy(params.bmax, mesh->rc->bmax);
    params.cs = mesh->rc->cs;
    params.ch = mesh->rc->ch;
    // ?
    params.walkableHeight = mesh->min_actor_height * mesh->rc->ch;
    params.walkableRadius = mesh->max_actor_radius * mesh->rc->cs;
    params.walkableClimb = mesh->max_traversable_ledge_height * mesh->rc->ch;
    if (detail_mesh)
    {
        params.detailMeshes = detail_mesh->rc->meshes;
        params.detailVerts = detail_mesh->rc->verts;
        params.detailVertsCount = detail_mesh->rc->nverts;
        params.detailTris = detail_mesh->rc->tris;
        params.detailTriCount = detail_mesh->rc->ntris;
    }
    params.buildBvTree = true;

    unsigned char* data = 0;
    int data_size = 0;
    if (!dtCreateNavMeshData(&params, &data, &data_size))
    {
        return PyErr_Format(
            PyExc_RuntimeError,
            "failed to build detour nav mesh data"
        );
    }

    auto dt_status = self->dt->init(data, data_size, DT_TILE_FREE_DATA);
    if (dtStatusFailed(dt_status))
    {
        dtFree(data);
        return PyErr_Format(
            PyExc_RuntimeError,
            "failed to initialize detour nav mesh"
        );
    }

    return (PyObject *)self;
}


static void
NavigationMesh___dealloc__(NavigationMesh *self)
{
    if (self->dt)
    {
        dtFreeNavMesh(self->dt);
        self->dt = 0;
    }

    PyTypeObject *type = Py_TYPE(self);
    type->tp_free(self);
    Py_DECREF(type);
}


static PyMemberDef NavigationMesh_PyMemberDef[] = {
    {0, 0, 0, 0}
};


static PyObject *
NavigationMesh_find_nearest_polygon(
    NavigationMesh *self,
    PyObject *const *args,
    Py_ssize_t nargs
)
{
    auto state = get_module_state();
    if (nargs != 2)
    {
        return PyErr_Format(
            PyExc_TypeError,
            "expected 2 args: point, extents"
        );
    }

    float *point = state->math_api->FVector3_GetValuePointer(args[0]);
    if (!point){ return 0; }

    float *extents = state->math_api->FVector3_GetValuePointer(args[1]);
    if (!extents){ return 0; }

    dtNavMeshQuery query;
    query.init(self->dt, 2048);
    dtQueryFilter filter;
    dtPolyRef nearest_poly;
    float nearest_point[3];
    auto dt_status = query.findNearestPoly(
        point,
        extents,
        &filter,
        &nearest_poly,
        nearest_point
    );
    if (dtStatusFailed(dt_status))
    {
        return PyErr_Format(
            PyExc_RuntimeError,
            "failed to find nearest poly"
        );
    }

    if (nearest_poly == 0)
    {
        return PyTuple_Pack(2, Py_None, Py_None);
    }

    auto py_result = PyTuple_New(2);

    auto py_nearest_poly = PyLong_FromUnsignedLong(nearest_poly);
    if (!py_nearest_poly)
    {
        Py_DECREF(py_result);
        return 0;
    }
    PyTuple_SET_ITEM(py_result, 0, py_nearest_poly);

    auto py_nearest_point = state->math_api->FVector3_Create(nearest_point);
    if (!py_nearest_point)
    {
        Py_DECREF(py_result);
        return 0;
    }
    PyTuple_SET_ITEM(py_result, 1, py_nearest_point);

    return py_result;
}



static PyObject *
NavigationMesh_find_path(
    NavigationMesh *self,
    PyObject *const *args,
    Py_ssize_t nargs
)
{
    auto state = get_module_state();
    if (nargs != 4)
    {
        return PyErr_Format(
            PyExc_TypeError,
            "expected 4 args: start_poly, start_position, end_poly, "
            "end_position"
        );
    }

    dtPolyRef start_poly = PyLong_AsUnsignedLong(args[0]);
    if (PyErr_Occurred()){ return 0; }

    float *start_position = state->math_api->FVector3_GetValuePointer(args[1]);
    if (!start_position){ return 0; }

    dtPolyRef end_poly = PyLong_AsUnsignedLong(args[2]);
    if (PyErr_Occurred()){ return 0; }

    float *end_position = state->math_api->FVector3_GetValuePointer(args[3]);
    if (!end_position){ return 0; }

    dtNavMeshQuery query;
    query.init(self->dt, 2048);
    dtQueryFilter filter;
    static const int PATH_SIZE = 1000;
    dtPolyRef path[PATH_SIZE];
    int path_count;
    auto dt_status = query.findPath(
        start_poly,
        end_poly,
        start_position,
        end_position,
        &filter,
        path,
        &path_count,
        PATH_SIZE
    );
    if (dtStatusFailed(dt_status))
    {
        return PyErr_Format(
            PyExc_RuntimeError,
            "failed to find path"
        );
    }

    static const int STRAIGHT_PATH_SIZE = 1000;
    float straight_path[STRAIGHT_PATH_SIZE * 3];
    int straight_path_count;
    dt_status = query.findStraightPath(
        start_position,
        end_position,
        path,
        path_count,
        straight_path,
        0,
        0,
        &straight_path_count,
        STRAIGHT_PATH_SIZE,
        DT_STRAIGHTPATH_ALL_CROSSINGS
    );
    if (dtStatusFailed(dt_status))
    {
        return PyErr_Format(
            PyExc_RuntimeError,
            "failed to find straight path"
        );
    }

    auto py_result = PyTuple_New(straight_path_count);
    for (int i = 0; i < straight_path_count; ++i)
    {
        auto vertex = &straight_path[i * 3];
        auto py_vertex = state->math_api->FVector3_Create(vertex);
        if (!py_vertex)
        {
            Py_DECREF(py_result);
            return 0;
        }
        PyTuple_SetItem(py_result, i, py_vertex);
    }
    return py_result;
}


static PyMethodDef NavigationMesh_PyMethodDef[] = {
    {
        "find_nearest_polygon",
        (PyCFunction)NavigationMesh_find_nearest_polygon,
        METH_FASTCALL,
        0
    },
    {
        "find_path",
        (PyCFunction)NavigationMesh_find_path,
        METH_FASTCALL,
        0
    },
    {0, 0, 0, 0}
};


static PyGetSetDef NavigationMesh_PyGetSetDef[] = {
    {0, 0, 0, 0, 0}
};


static PyType_Slot NavigationMesh_PyType_Slots [] = {
    {Py_tp_new, (void*)NavigationMesh___new__},
    {Py_tp_dealloc, (void*)NavigationMesh___dealloc__},
    {Py_tp_members, (void*)NavigationMesh_PyMemberDef},
    {Py_tp_methods, (void*)NavigationMesh_PyMethodDef},
    {Py_tp_getset, (void*)NavigationMesh_PyGetSetDef},
    {0, 0},
};


static PyType_Spec NavigationMesh_PyTypeSpec = {
    "gamut.navigation._navigation.NavigationMesh",
    sizeof(NavigationMesh),
    0,
    Py_TPFLAGS_DEFAULT,
    NavigationMesh_PyType_Slots
};


static PyTypeObject *
define_navigation_mesh_type(PyObject *module)
{
    ASSERT(module);
    PyTypeObject *type = (PyTypeObject *)PyType_FromModuleAndSpec(
        module,
        &NavigationMesh_PyTypeSpec,
        0
    );
    if (!type){ return 0; }
    // Note:
    // Unlike other functions that steal references, PyModule_AddObject() only
    // decrements the reference count of value on success.
    if (PyModule_AddObject(module, "NavigationMesh", (PyObject *)type) < 0)
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
    Py_VISIT(state->CompactHeightField_PyTypeObject);
    Py_VISIT(state->ContourSet_PyTypeObject);
    Py_VISIT(state->HeightField_PyTypeObject);
    Py_VISIT(state->Mesh_PyTypeObject);
    Py_VISIT(state->NavigationMesh_PyTypeObject);
    return 0;
}


static int
module_clear(PyObject *self)
{
    ModuleState *state = (ModuleState *)PyModule_GetState(self);
    Py_CLEAR(state->CompactHeightField_PyTypeObject);
    Py_CLEAR(state->ContourSet_PyTypeObject);
    Py_CLEAR(state->HeightField_PyTypeObject);
    Py_CLEAR(state->Mesh_PyTypeObject);
    Py_CLEAR(state->NavigationMesh_PyTypeObject);
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

    PyTypeObject *py_compact_height_field_type =
        define_compact_height_field_type(module);
    {
        if (!py_compact_height_field_type){ goto error; }
        Py_INCREF(py_compact_height_field_type);
        state->CompactHeightField_PyTypeObject = py_compact_height_field_type;
    }

    if (!define_contour_set_type(module)){ goto error; }
    PyTypeObject *py_countour_set_type = define_contour_set_type(module);
    {
        if (!py_countour_set_type){ goto error; }
        Py_INCREF(py_countour_set_type);
        state->ContourSet_PyTypeObject = py_countour_set_type;
    }

    PyTypeObject *py_detail_mesh_type = define_detail_mesh_type(module);
    {
        if (!py_detail_mesh_type){ goto error; }
        Py_INCREF(py_detail_mesh_type);
        state->DetailMesh_PyTypeObject = py_detail_mesh_type;
    }

    PyTypeObject *py_height_field_type = define_height_field_type(module);
    {
        if (!py_height_field_type){ goto error; }
        Py_INCREF(py_height_field_type);
        state->HeightField_PyTypeObject = py_height_field_type;
    }

    PyTypeObject *py_mesh_type = define_mesh_type(module);
    {
        if (!py_mesh_type){ goto error; }
        Py_INCREF(py_mesh_type);
        state->Mesh_PyTypeObject = py_mesh_type;
    }

    PyTypeObject *py_navigation_mesh_type = define_navigation_mesh_type(module);
    {
        if (!py_navigation_mesh_type){ goto error; }
        Py_INCREF(py_navigation_mesh_type);
        state->NavigationMesh_PyTypeObject = py_navigation_mesh_type;
    }

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

