
// python
#define PY_SSIZE_T_CLEAN
#include <Python.h>
// cgal
#define CGAL_DISABLE_GMP 1
#include <CGAL/Exact_predicates_inexact_constructions_kernel.h>
#include <CGAL/Constrained_Delaunay_triangulation_2.h>
#include <CGAL/Triangulation_face_base_with_info_2.h>
#include <CGAL/Polygon_with_holes_2.h>
#include <CGAL/Boolean_set_operations_2.h>
// gamut
#include "gamut/math.h"
// glm
#include <glm/glm.hpp>


struct ModuleState
{
    GamutMathApi *math_api;
};


static ModuleState *get_module_state();



struct FaceInfo2{};

typedef CGAL::Exact_predicates_inexact_constructions_kernel K;
typedef CGAL::Triangulation_vertex_base_2<K> Vb;
typedef CGAL::Triangulation_face_base_with_info_2<FaceInfo2, K> Fbb;
typedef CGAL::Constrained_triangulation_face_base_2<K, Fbb> Fb;
typedef CGAL::Polygon_with_holes_2<K> PolygonWithHoles;
typedef CGAL::Polygon_2<K> Polygon;
typedef CGAL::Point_2<K> Point;
typedef CGAL::Ray_2<K> Ray;
typedef CGAL::Triangulation_data_structure_2<Vb, Fb> TDS;
typedef CGAL::Exact_predicates_tag Itag;
typedef CGAL::Constrained_Delaunay_triangulation_2<K, TDS, Itag> CDT;
typedef CDT::Face_handle Face_handle;


static bool
cgal_point_in_cgal_polygon(Point& point, Polygon& polygon)
{
    auto out_side = (
        polygon.orientation() == CGAL::POSITIVE ?
        CGAL::ON_NEGATIVE_SIDE : CGAL::ON_POSITIVE_SIDE
    );
    return polygon.oriented_side(point) != out_side;
}


struct GlmDVec2Hash
{
    std::size_t operator()(glm::dvec2 const& v) const noexcept
    {
        std::size_t h1 = std::hash<double>{}(v.x);
        std::size_t h2 = std::hash<double>{}(v.y);
        return h1 ^ (h2 << 1);
    }
};


static PyObject *
triangulate(PyObject *self, PyObject *const *args, Py_ssize_t nargs)
{
    auto state = get_module_state();

    Polygon exterior;
    {
        PyObject *py_vertices = args[0];
        glm::dvec2 *vertices = (glm::dvec2 *)state->math_api->GamutMathDVector2Array_GetValuePointer(py_vertices);
        size_t vertex_count = state->math_api->GamutMathDVector2Array_GetLength(py_vertices);
        for (size_t v = 0; v < vertex_count; v++)
        {
            exterior.push_back(Point(vertices[v].x, vertices[v].y));
        }
    }
    std::vector<Polygon> holes(nargs - 1);
    {
        for (Py_ssize_t i = 1; i < nargs; i++)
        {
            Polygon& hole = holes[i - 1];
            PyObject *py_vertices = args[i];
            glm::dvec2 *vertices = (glm::dvec2 *)state->math_api->GamutMathDVector2Array_GetValuePointer(py_vertices);
            size_t vertex_count = state->math_api->GamutMathDVector2Array_GetLength(py_vertices);
            for (size_t v = 0; v < vertex_count; v++)
            {
                hole.push_back(Point(vertices[v].x, vertices[v].y));
            }
        }
    }
    PolygonWithHoles polygon(exterior, holes.begin(), holes.end());

    CDT cdt;
    {
        cdt.insert_constraint(
            polygon.outer_boundary().vertices_begin(),
            polygon.outer_boundary().vertices_end(),
            true
        );
        for (
            auto iter = polygon.holes_begin();
            iter != polygon.holes_end();
            ++iter
        )
        {
            auto& hole = *iter;
            cdt.insert_constraint(
                hole.vertices_begin(),
                hole.vertices_end(),
                true
            );
        }
    }

    std::unordered_map<glm::dvec2, unsigned int, GlmDVec2Hash> position_indexes;
    std::vector<glm::dvec2> positions;
    std::vector<glm::uvec3> indexes;
    unsigned int next_index = 0;

    for (Face_handle f: cdt.finite_face_handles())
    {
        Point points[3] = {
            f->vertex(0)->point(),
            f->vertex(1)->point(),
            f->vertex(2)->point()
        };
        Point center(
            (points[0].x() + points[1].x() + points[2].x()) / 3,
            (points[0].y() + points[1].y() + points[2].y()) / 3
        );
        {
            if (cgal_point_in_cgal_polygon(center, polygon.outer_boundary()))
            {
                bool in_hole = false;
                for (
                    auto iter = polygon.holes_begin();
                    iter != polygon.holes_end();
                    ++iter
                )
                {
                    auto &hole = *iter;
                    if (cgal_point_in_cgal_polygon(center, hole))
                    {
                        in_hole = true;
                        break;
                    }
                }
                if (!in_hole)
                {
                    glm::uvec3 triangle_indexes;
                    for (glm::uvec3::length_type i = 0; i < 3; i++)
                    {
                        glm::dvec2 vec(points[i].x(), points[i].y());
                        auto iter = position_indexes.find(vec);
                        if (iter == position_indexes.end())
                        {
                            position_indexes[vec] = next_index;
                            positions.push_back(vec);
                            triangle_indexes[i] = next_index;
                            next_index += 1;
                        }
                        else
                        {
                            triangle_indexes[i] = iter->second;
                        }
                    }
                    indexes.push_back(triangle_indexes);
                }
            }
        }
    }

    auto positions_array = state->math_api->GamutMathDVector2Array_Create(
        positions.size(),
        (double *)positions.data()
    );
    if (!positions_array){ return 0; }
    auto indexes_array = state->math_api->GamutMathUVector3Array_Create(
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
