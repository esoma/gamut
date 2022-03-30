
// python
#define PY_SSIZE_T_CLEAN
#include <Python.h>
// cdt
#include "CDT.h"
// gamut
#include "gamut/math.h"
// glm
#include <glm/glm.hpp>


struct ModuleState
{
    GamutMathApi *math_api;
};


static ModuleState *get_module_state();


static PyObject *
triangulate(PyObject *self, PyObject *const *args, Py_ssize_t nargs)
noexcept
{
    auto state = get_module_state();

    CDT::Triangulation<double> cdt;
    std::vector<CDT::V2d<double>> vertices;
    std::vector<CDT::Edge> edges;

    CDT::VertInd index_offset = 0;
    for (Py_ssize_t i = 0; i < nargs; i++)
    {
        PyObject *py_positions = args[i];
        glm::dvec2 *positions = (glm::dvec2 *)state->math_api->DVector2Array_GetValuePointer(py_positions);
        size_t position_count = state->math_api->DVector2Array_GetLength(py_positions);
        for (size_t v = 0; v < position_count; v++)
        {
            vertices.push_back(CDT::V2d<double>{positions[v].x, positions[v].y});
            if (v == position_count - 1)
            {
                edges.push_back(CDT::Edge(index_offset + v, index_offset));
            }
            else
            {
                edges.push_back(CDT::Edge(index_offset + v, index_offset + v + 1));
            }
        }
        index_offset = vertices.size();
    }

    cdt.insertVertices(vertices);
    cdt.insertEdges(edges);
    cdt.eraseOuterTrianglesAndHoles();

    auto positions_array = state->math_api->DVector2Array_Create(
        cdt.vertices.size(),
        (double *)cdt.vertices.data()
    );
    if (!positions_array){ return 0; }

    std::vector<glm::uvec3> indexes;
    for (
        auto iter = cdt.triangles.begin();
        iter != cdt.triangles.end();
        ++iter
    )
    {
        indexes.push_back(glm::uvec3(
            iter->vertices[0],
            iter->vertices[1],
            iter->vertices[2]
        ));
    }
    auto indexes_array = state->math_api->UVector3Array_Create(
        indexes.size(),
        (unsigned int *)indexes.data()
    );
    if (!indexes_array)
    {
        Py_DECREF(positions_array);
        return 0;
    }
    return PyTuple_Pack(2, positions_array, indexes_array);
}


static PyMethodDef module_PyMethodDef[] = {
    {"triangulate", (PyCFunction)triangulate, METH_FASTCALL, 0},
    {0, 0, 0, 0}
};


static void
module_free(void* self)
{
    GamutMathApi_Release();
}


static struct PyModuleDef module_PyModuleDef = {
    PyModuleDef_HEAD_INIT,
    "gamut.geometry._triangulate",
    0,
    sizeof(struct ModuleState),
    module_PyMethodDef,
    0,
    0,
    0,
    module_free
};


PyMODINIT_FUNC
PyInit__triangulate()
{
    ModuleState *state = 0;
    PyObject *module = PyModule_Create(&module_PyModuleDef);
    if (!module){ goto error; }

    if (PyState_AddModule(module, &module_PyModuleDef) == -1){ goto error; }
    state = (ModuleState *)PyModule_GetState(module);

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
        return PyErr_Format(PyExc_RuntimeError, "physics module not ready");
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
