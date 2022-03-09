
// generated 2022-03-09 03:15:33.450046 from codegen/math/templates/_matrix.hpp

#ifndef GAMUT_MATH_FVECTOR4X2_HPP
#define GAMUT_MATH_FVECTOR4X2_HPP

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
#include "_fvector2.hpp"

typedef glm::tmat4x2<float, glm::defaultp> FVector4x2Glm;


struct FVector4x2
{
    PyObject_HEAD
    PyObject *weakreflist;
    FVector4x2Glm *glm;
};


static PyObject *
FVector4x2__new__(PyTypeObject *cls, PyObject *args, PyObject *kwds)
{
    if (kwds && PyDict_Size(kwds) != 0)
    {
        PyErr_SetString(
            PyExc_TypeError,
            "FVector4x2 does accept any keyword arguments"
        );
        return 0;
    }

    FVector4x2Glm *glm = 0;
    auto arg_count = PyTuple_GET_SIZE(args);
    switch (PyTuple_GET_SIZE(args))
    {
        case 0:
        {
            glm = new FVector4x2Glm();
            break;
        }
        case 1:
        {
            auto arg = PyTuple_GET_ITEM(args, 0);
            float arg_c = pyobject_to_c_float(arg);
            auto error_occurred = PyErr_Occurred();
            if (error_occurred){ return 0; }
            glm = new FVector4x2Glm(arg_c);
            break;
        }
        case 4:
        {
            auto module_state = get_module_state();
            if (!module_state){ return 0; }
            auto column_cls = module_state->FVector2_PyTypeObject;

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

                PyObject *p_3 = PyTuple_GET_ITEM(args, 3);
                if (Py_TYPE(p_3) != column_cls)
                {
                    PyErr_Format(
                        PyExc_TypeError,
                        "invalid column supplied, expected %R, (got %R)",
                        column_cls,
                        p_3
                    );
                    return 0;
                }

            glm = new FVector4x2Glm(

                    *((FVector2 *)p_0)->glm,

                    *((FVector2 *)p_1)->glm,

                    *((FVector2 *)p_2)->glm,

                    *((FVector2 *)p_3)->glm

            );

            break;
        }
        case 8:
        {

                float c_0 = 0;

                float c_1 = 0;

                float c_2 = 0;

                float c_3 = 0;

                float c_4 = 0;

                float c_5 = 0;

                float c_6 = 0;

                float c_7 = 0;


            {
                auto arg = PyTuple_GET_ITEM(args, 0);
                c_0 = pyobject_to_c_float(arg);
                auto error_occurred = PyErr_Occurred();
                if (error_occurred){ return 0; }
            }

            {
                auto arg = PyTuple_GET_ITEM(args, 1);
                c_1 = pyobject_to_c_float(arg);
                auto error_occurred = PyErr_Occurred();
                if (error_occurred){ return 0; }
            }

            {
                auto arg = PyTuple_GET_ITEM(args, 2);
                c_2 = pyobject_to_c_float(arg);
                auto error_occurred = PyErr_Occurred();
                if (error_occurred){ return 0; }
            }

            {
                auto arg = PyTuple_GET_ITEM(args, 3);
                c_3 = pyobject_to_c_float(arg);
                auto error_occurred = PyErr_Occurred();
                if (error_occurred){ return 0; }
            }

            {
                auto arg = PyTuple_GET_ITEM(args, 4);
                c_4 = pyobject_to_c_float(arg);
                auto error_occurred = PyErr_Occurred();
                if (error_occurred){ return 0; }
            }

            {
                auto arg = PyTuple_GET_ITEM(args, 5);
                c_5 = pyobject_to_c_float(arg);
                auto error_occurred = PyErr_Occurred();
                if (error_occurred){ return 0; }
            }

            {
                auto arg = PyTuple_GET_ITEM(args, 6);
                c_6 = pyobject_to_c_float(arg);
                auto error_occurred = PyErr_Occurred();
                if (error_occurred){ return 0; }
            }

            {
                auto arg = PyTuple_GET_ITEM(args, 7);
                c_7 = pyobject_to_c_float(arg);
                auto error_occurred = PyErr_Occurred();
                if (error_occurred){ return 0; }
            }

            glm = new FVector4x2Glm(

                    c_0,

                    c_1,

                    c_2,

                    c_3,

                    c_4,

                    c_5,

                    c_6,

                    c_7

            );
            break;
        }
        default:
        {
            PyErr_Format(
                PyExc_TypeError,
                "invalid number of arguments supplied to FVector4x2, expected "
                "0, 1, 4 or 8 (got %zd)",
                arg_count
            );
            return 0;
        }
    }

    FVector4x2 *self = (FVector4x2*)cls->tp_alloc(cls, 0);
    if (!self)
    {
        delete glm;
        return 0;
    }
    self->glm = glm;

    return (PyObject *)self;
}


static void
FVector4x2__dealloc__(FVector4x2 *self)
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
FVector4x2__hash__(FVector4x2 *self)
{
    Py_ssize_t len = 8;
    Py_uhash_t acc = _HASH_XXPRIME_5;
    for (size_t c = 0; c < 4; c++)
    {
        for (size_t r = 0; r < 2; r++)
        {
            Py_uhash_t lane = std::hash<float>{}((*self->glm)[c][r]);
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
FVector4x2__repr__(FVector4x2 *self)
{
    PyObject *result = 0;


        PyObject *py_0_0 = 0;

        PyObject *py_0_1 = 0;



        PyObject *py_1_0 = 0;

        PyObject *py_1_1 = 0;



        PyObject *py_2_0 = 0;

        PyObject *py_2_1 = 0;



        PyObject *py_3_0 = 0;

        PyObject *py_3_1 = 0;





        py_0_0 = c_float_to_pyobject((*self->glm)[0][0]);
        if (!py_0_0){ goto cleanup; }

        py_0_1 = c_float_to_pyobject((*self->glm)[0][1]);
        if (!py_0_1){ goto cleanup; }



        py_1_0 = c_float_to_pyobject((*self->glm)[1][0]);
        if (!py_1_0){ goto cleanup; }

        py_1_1 = c_float_to_pyobject((*self->glm)[1][1]);
        if (!py_1_1){ goto cleanup; }



        py_2_0 = c_float_to_pyobject((*self->glm)[2][0]);
        if (!py_2_0){ goto cleanup; }

        py_2_1 = c_float_to_pyobject((*self->glm)[2][1]);
        if (!py_2_1){ goto cleanup; }



        py_3_0 = c_float_to_pyobject((*self->glm)[3][0]);
        if (!py_3_0){ goto cleanup; }

        py_3_1 = c_float_to_pyobject((*self->glm)[3][1]);
        if (!py_3_1){ goto cleanup; }



    result = PyUnicode_FromFormat(
        "FVector4x2("

        "("

            "%R"
            ", "

            "%R"


        ")"

        ", "


        "("

            "%R"
            ", "

            "%R"


        ")"

        ", "


        "("

            "%R"
            ", "

            "%R"


        ")"

        ", "


        "("

            "%R"
            ", "

            "%R"


        ")"


        ")",


            py_0_0
            ,

            py_0_1
            ,



            py_1_0
            ,

            py_1_1
            ,



            py_2_0
            ,

            py_2_1
            ,



            py_3_0
            ,

            py_3_1



    );
cleanup:


        Py_XDECREF(py_0_0);

        Py_XDECREF(py_0_1);



        Py_XDECREF(py_1_0);

        Py_XDECREF(py_1_1);



        Py_XDECREF(py_2_0);

        Py_XDECREF(py_2_1);



        Py_XDECREF(py_3_0);

        Py_XDECREF(py_3_1);


    return result;
}


static Py_ssize_t
FVector4x2__len__(FVector4x2 *self)
{
    return 4;
}


static PyObject *
FVector4x2__getitem__(FVector4x2 *self, Py_ssize_t index)
{
    if (index < 0 || index > 3)
    {
        PyErr_Format(PyExc_IndexError, "index out of range");
        return 0;
    }
    const auto& v = (*self->glm)[index];
    return (PyObject *)create_FVector2_from_glm(v);
}


static PyType_Slot FVector4x2_PyType_Slots [] = {
    {Py_tp_new, (void*)FVector4x2__new__},
    {Py_tp_dealloc, (void*)FVector4x2__dealloc__},
    {Py_tp_hash, (void*)FVector4x2__hash__},
    {Py_tp_repr, (void*)FVector4x2__repr__},
    {Py_sq_length, (void*)FVector4x2__len__},
    {Py_sq_item, (void*)FVector4x2__getitem__},
    /*{Py_tp_richcompare, (void*)FVector4x2__richcmp__},
    {Py_nb_add, (void*)FVector4x2__add__},
    {Py_nb_subtract, (void*)FVector4x2__sub__},
    {Py_nb_multiply, (void*)FVector4x2__mul__},

        {Py_nb_matrix_multiply, (void*)FVector4x2__matmul__},
        {Py_nb_remainder, (void*)FVector4x2__mod__},
        {Py_nb_power, (void*)FVector4x2__pow__},


        {Py_nb_true_divide, (void*)FVector4x2__truediv__},


        {Py_nb_negative, (void*)FVector4x2__neg__},

    {Py_nb_absolute, (void*)FVector4x2__abs__},
    {Py_nb_bool, (void*)FVector4x2__bool__},
    {Py_bf_getbuffer, (void*)FVector4x2_getbufferproc},
    {Py_tp_getset, (void*)FVector4x2_PyGetSetDef},
    {Py_tp_getattro, (void*)FVector4x2__getattr__},
    {Py_tp_members, (void*)FVector4x2_PyMemberDef},
    {Py_tp_methods, (void*)FVector4x2_PyMethodDef},
    */
    {0, 0},
};


static PyType_Spec FVector4x2_PyTypeSpec = {
    "gamut.math.FVector4x2",
    sizeof(FVector4x2),
    0,
    Py_TPFLAGS_DEFAULT,
    FVector4x2_PyType_Slots
};


static PyTypeObject *
define_FVector4x2_type(PyObject *module)
{
    PyTypeObject *type = (PyTypeObject *)PyType_FromModuleAndSpec(
        module,
        &FVector4x2_PyTypeSpec,
        0
    );
    if (!type){ return 0; }
    // Note:
    // Unlike other functions that steal references, PyModule_AddObject() only
    // decrements the reference count of value on success.
    if (PyModule_AddObject(module, "FVector4x2", (PyObject *)type) < 0)
    {
        Py_DECREF(type);
        return 0;
    }
    return type;
}

#endif