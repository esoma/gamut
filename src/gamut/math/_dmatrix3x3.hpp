
// generated 2022-03-09 03:15:33.451545 from codegen/math/templates/_matrix.hpp

#ifndef GAMUT_MATH_DMATRIX3X3_HPP
#define GAMUT_MATH_DMATRIX3X3_HPP

// stdlib
#include <limits>
#include <functional>
// python
#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <structmember.h>
// glm
#include <glm/glm.hpp>
#include <glm/ext.hpp>
// gamut
#include "_modulestate.hpp"
#include "_type.hpp"
#include "_dvector3.hpp"

typedef glm::tmat3x3<double, glm::defaultp> DMatrix3x3Glm;


struct DMatrix3x3
{
    PyObject_HEAD
    PyObject *weakreflist;
    DMatrix3x3Glm *glm;
};


static PyObject *
DMatrix3x3__new__(PyTypeObject *cls, PyObject *args, PyObject *kwds)
{
    if (kwds && PyDict_Size(kwds) != 0)
    {
        PyErr_SetString(
            PyExc_TypeError,
            "DMatrix3x3 does accept any keyword arguments"
        );
        return 0;
    }

    DMatrix3x3Glm *glm = 0;
    auto arg_count = PyTuple_GET_SIZE(args);
    switch (PyTuple_GET_SIZE(args))
    {
        case 0:
        {
            glm = new DMatrix3x3Glm();
            break;
        }
        case 1:
        {
            auto arg = PyTuple_GET_ITEM(args, 0);
            double arg_c = pyobject_to_c_double(arg);
            auto error_occurred = PyErr_Occurred();
            if (error_occurred){ return 0; }
            glm = new DMatrix3x3Glm(arg_c);
            break;
        }
        case 3:
        {
            auto module_state = get_module_state();
            if (!module_state){ return 0; }
            auto column_cls = module_state->DVector3_PyTypeObject;

                PyObject *p_0 = PyTuple_GET_ITEM(args, 0);
                if (Py_TYPE(p_0) != column_cls)
                {
                    PyErr_Format(
                        PyExc_TypeError,
                        "invalid column supplied, expected %R, (got %R)",
                        column_cls,
                        p_0
                    );
                    return 0;
                }

                PyObject *p_1 = PyTuple_GET_ITEM(args, 1);
                if (Py_TYPE(p_1) != column_cls)
                {
                    PyErr_Format(
                        PyExc_TypeError,
                        "invalid column supplied, expected %R, (got %R)",
                        column_cls,
                        p_1
                    );
                    return 0;
                }

                PyObject *p_2 = PyTuple_GET_ITEM(args, 2);
                if (Py_TYPE(p_2) != column_cls)
                {
                    PyErr_Format(
                        PyExc_TypeError,
                        "invalid column supplied, expected %R, (got %R)",
                        column_cls,
                        p_2
                    );
                    return 0;
                }

            glm = new DMatrix3x3Glm(

                    *((DVector3 *)p_0)->glm,

                    *((DVector3 *)p_1)->glm,

                    *((DVector3 *)p_2)->glm

            );

            break;
        }
        case 9:
        {

                double c_0 = 0;

                double c_1 = 0;

                double c_2 = 0;

                double c_3 = 0;

                double c_4 = 0;

                double c_5 = 0;

                double c_6 = 0;

                double c_7 = 0;

                double c_8 = 0;


            {
                auto arg = PyTuple_GET_ITEM(args, 0);
                c_0 = pyobject_to_c_double(arg);
                auto error_occurred = PyErr_Occurred();
                if (error_occurred){ return 0; }
            }

            {
                auto arg = PyTuple_GET_ITEM(args, 1);
                c_1 = pyobject_to_c_double(arg);
                auto error_occurred = PyErr_Occurred();
                if (error_occurred){ return 0; }
            }

            {
                auto arg = PyTuple_GET_ITEM(args, 2);
                c_2 = pyobject_to_c_double(arg);
                auto error_occurred = PyErr_Occurred();
                if (error_occurred){ return 0; }
            }

            {
                auto arg = PyTuple_GET_ITEM(args, 3);
                c_3 = pyobject_to_c_double(arg);
                auto error_occurred = PyErr_Occurred();
                if (error_occurred){ return 0; }
            }

            {
                auto arg = PyTuple_GET_ITEM(args, 4);
                c_4 = pyobject_to_c_double(arg);
                auto error_occurred = PyErr_Occurred();
                if (error_occurred){ return 0; }
            }

            {
                auto arg = PyTuple_GET_ITEM(args, 5);
                c_5 = pyobject_to_c_double(arg);
                auto error_occurred = PyErr_Occurred();
                if (error_occurred){ return 0; }
            }

            {
                auto arg = PyTuple_GET_ITEM(args, 6);
                c_6 = pyobject_to_c_double(arg);
                auto error_occurred = PyErr_Occurred();
                if (error_occurred){ return 0; }
            }

            {
                auto arg = PyTuple_GET_ITEM(args, 7);
                c_7 = pyobject_to_c_double(arg);
                auto error_occurred = PyErr_Occurred();
                if (error_occurred){ return 0; }
            }

            {
                auto arg = PyTuple_GET_ITEM(args, 8);
                c_8 = pyobject_to_c_double(arg);
                auto error_occurred = PyErr_Occurred();
                if (error_occurred){ return 0; }
            }

            glm = new DMatrix3x3Glm(

                    c_0,

                    c_1,

                    c_2,

                    c_3,

                    c_4,

                    c_5,

                    c_6,

                    c_7,

                    c_8

            );
            break;
        }
        default:
        {
            PyErr_Format(
                PyExc_TypeError,
                "invalid number of arguments supplied to DMatrix3x3, expected "
                "0, 1, 3 or 9 (got %zd)",
                arg_count
            );
            return 0;
        }
    }

    DMatrix3x3 *self = (DMatrix3x3*)cls->tp_alloc(cls, 0);
    if (!self)
    {
        delete glm;
        return 0;
    }
    self->glm = glm;

    return (PyObject *)self;
}


static void
DMatrix3x3__dealloc__(DMatrix3x3 *self)
{
    if (self->weakreflist)
    {
        PyObject_ClearWeakRefs((PyObject *)self);
    }

    delete self->glm;

    PyTypeObject *type = Py_TYPE(self);
    type->tp_free(self);
    Py_DECREF(type);
}


// this is roughly copied from how python hashes tuples in 3.11
#if SIZEOF_PY_UHASH_T > 4
#define _HASH_XXPRIME_1 ((Py_uhash_t)11400714785074694791ULL)
#define _HASH_XXPRIME_2 ((Py_uhash_t)14029467366897019727ULL)
#define _HASH_XXPRIME_5 ((Py_uhash_t)2870177450012600261ULL)
#define _HASH_XXROTATE(x) ((x << 31) | (x >> 33))  /* Rotate left 31 bits */
#else
#define _HASH_XXPRIME_1 ((Py_uhash_t)2654435761UL)
#define _HASH_XXPRIME_2 ((Py_uhash_t)2246822519UL)
#define _HASH_XXPRIME_5 ((Py_uhash_t)374761393UL)
#define _HASH_XXROTATE(x) ((x << 13) | (x >> 19))  /* Rotate left 13 bits */
#endif

static Py_hash_t
DMatrix3x3__hash__(DMatrix3x3 *self)
{
    Py_ssize_t len = 9;
    Py_uhash_t acc = _HASH_XXPRIME_5;
    for (size_t c = 0; c < 3; c++)
    {
        for (size_t r = 0; r < 3; r++)
        {
            Py_uhash_t lane = std::hash<double>{}((*self->glm)[c][r]);
            acc += lane * _HASH_XXPRIME_2;
            acc = _HASH_XXROTATE(acc);
            acc *= _HASH_XXPRIME_1;
        }
    }
    acc += len ^ (_HASH_XXPRIME_5 ^ 3527539UL);

    if (acc == (Py_uhash_t)-1) {
        return 1546275796;
    }
    return acc;
}


static PyObject *
DMatrix3x3__repr__(DMatrix3x3 *self)
{
    PyObject *result = 0;


        PyObject *py_0_0 = 0;

        PyObject *py_0_1 = 0;

        PyObject *py_0_2 = 0;



        PyObject *py_1_0 = 0;

        PyObject *py_1_1 = 0;

        PyObject *py_1_2 = 0;



        PyObject *py_2_0 = 0;

        PyObject *py_2_1 = 0;

        PyObject *py_2_2 = 0;





        py_0_0 = c_double_to_pyobject((*self->glm)[0][0]);
        if (!py_0_0){ goto cleanup; }

        py_0_1 = c_double_to_pyobject((*self->glm)[0][1]);
        if (!py_0_1){ goto cleanup; }

        py_0_2 = c_double_to_pyobject((*self->glm)[0][2]);
        if (!py_0_2){ goto cleanup; }



        py_1_0 = c_double_to_pyobject((*self->glm)[1][0]);
        if (!py_1_0){ goto cleanup; }

        py_1_1 = c_double_to_pyobject((*self->glm)[1][1]);
        if (!py_1_1){ goto cleanup; }

        py_1_2 = c_double_to_pyobject((*self->glm)[1][2]);
        if (!py_1_2){ goto cleanup; }



        py_2_0 = c_double_to_pyobject((*self->glm)[2][0]);
        if (!py_2_0){ goto cleanup; }

        py_2_1 = c_double_to_pyobject((*self->glm)[2][1]);
        if (!py_2_1){ goto cleanup; }

        py_2_2 = c_double_to_pyobject((*self->glm)[2][2]);
        if (!py_2_2){ goto cleanup; }



    result = PyUnicode_FromFormat(
        "DMatrix3x3("

        "("

            "%R"
            ", "

            "%R"
            ", "

            "%R"


        ")"

        ", "


        "("

            "%R"
            ", "

            "%R"
            ", "

            "%R"


        ")"

        ", "


        "("

            "%R"
            ", "

            "%R"
            ", "

            "%R"


        ")"


        ")",


            py_0_0
            ,

            py_0_1
            ,

            py_0_2
            ,



            py_1_0
            ,

            py_1_1
            ,

            py_1_2
            ,



            py_2_0
            ,

            py_2_1
            ,

            py_2_2



    );
cleanup:


        Py_XDECREF(py_0_0);

        Py_XDECREF(py_0_1);

        Py_XDECREF(py_0_2);



        Py_XDECREF(py_1_0);

        Py_XDECREF(py_1_1);

        Py_XDECREF(py_1_2);



        Py_XDECREF(py_2_0);

        Py_XDECREF(py_2_1);

        Py_XDECREF(py_2_2);


    return result;
}


static Py_ssize_t
DMatrix3x3__len__(DMatrix3x3 *self)
{
    return 3;
}


static PyObject *
DMatrix3x3__getitem__(DMatrix3x3 *self, Py_ssize_t index)
{
    if (index < 0 || index > 2)
    {
        PyErr_Format(PyExc_IndexError, "index out of range");
        return 0;
    }
    const auto& v = (*self->glm)[index];
    return (PyObject *)create_DVector3_from_glm(v);
}


static PyType_Slot DMatrix3x3_PyType_Slots [] = {
    {Py_tp_new, (void*)DMatrix3x3__new__},
    {Py_tp_dealloc, (void*)DMatrix3x3__dealloc__},
    {Py_tp_hash, (void*)DMatrix3x3__hash__},
    {Py_tp_repr, (void*)DMatrix3x3__repr__},
    {Py_sq_length, (void*)DMatrix3x3__len__},
    {Py_sq_item, (void*)DMatrix3x3__getitem__},
    /*{Py_tp_richcompare, (void*)DMatrix3x3__richcmp__},
    {Py_nb_add, (void*)DMatrix3x3__add__},
    {Py_nb_subtract, (void*)DMatrix3x3__sub__},
    {Py_nb_multiply, (void*)DMatrix3x3__mul__},

        {Py_nb_matrix_multiply, (void*)DMatrix3x3__matmul__},
        {Py_nb_remainder, (void*)DMatrix3x3__mod__},
        {Py_nb_power, (void*)DMatrix3x3__pow__},


        {Py_nb_true_divide, (void*)DMatrix3x3__truediv__},


        {Py_nb_negative, (void*)DMatrix3x3__neg__},

    {Py_nb_absolute, (void*)DMatrix3x3__abs__},
    {Py_nb_bool, (void*)DMatrix3x3__bool__},
    {Py_bf_getbuffer, (void*)DMatrix3x3_getbufferproc},
    {Py_tp_getset, (void*)DMatrix3x3_PyGetSetDef},
    {Py_tp_getattro, (void*)DMatrix3x3__getattr__},
    {Py_tp_members, (void*)DMatrix3x3_PyMemberDef},
    {Py_tp_methods, (void*)DMatrix3x3_PyMethodDef},
    */
    {0, 0},
};


static PyType_Spec DMatrix3x3_PyTypeSpec = {
    "gamut.math.DMatrix3x3",
    sizeof(DMatrix3x3),
    0,
    Py_TPFLAGS_DEFAULT,
    DMatrix3x3_PyType_Slots
};


static PyTypeObject *
define_DMatrix3x3_type(PyObject *module)
{
    PyTypeObject *type = (PyTypeObject *)PyType_FromModuleAndSpec(
        module,
        &DMatrix3x3_PyTypeSpec,
        0
    );
    if (!type){ return 0; }
    // Note:
    // Unlike other functions that steal references, PyModule_AddObject() only
    // decrements the reference count of value on success.
    if (PyModule_AddObject(module, "DMatrix3x3", (PyObject *)type) < 0)
    {
        Py_DECREF(type);
        return 0;
    }
    return type;
}

#endif