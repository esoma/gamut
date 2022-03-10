
// generated 2022-03-10 18:59:39.079561 from codegen/math/templates/_matrix.hpp

#ifndef GAMUT_MATH_DMATRIX4X4_HPP
#define GAMUT_MATH_DMATRIX4X4_HPP

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
#include "_matrixtype.hpp"
#include "_type.hpp"
#include "_dvector4.hpp"


static PyObject *
DMatrix4x4__new__(PyTypeObject *cls, PyObject *args, PyObject *kwds)
{
    if (kwds && PyDict_Size(kwds) != 0)
    {
        PyErr_SetString(
            PyExc_TypeError,
            "DMatrix4x4 does accept any keyword arguments"
        );
        return 0;
    }

    DMatrix4x4Glm *glm = 0;
    auto arg_count = PyTuple_GET_SIZE(args);
    switch (PyTuple_GET_SIZE(args))
    {
        case 0:
        {
            glm = new DMatrix4x4Glm();
            break;
        }
        case 1:
        {
            auto arg = PyTuple_GET_ITEM(args, 0);
            double arg_c = pyobject_to_c_double(arg);
            auto error_occurred = PyErr_Occurred();
            if (error_occurred){ return 0; }
            glm = new DMatrix4x4Glm(arg_c);
            break;
        }
        case 4:
        {
            auto module_state = get_module_state();
            if (!module_state){ return 0; }
            auto column_cls = module_state->DVector4_PyTypeObject;

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

            glm = new DMatrix4x4Glm(

                    *((DVector4 *)p_0)->glm,

                    *((DVector4 *)p_1)->glm,

                    *((DVector4 *)p_2)->glm,

                    *((DVector4 *)p_3)->glm

            );

            break;
        }
        case 16:
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

                double c_9 = 0;

                double c_10 = 0;

                double c_11 = 0;

                double c_12 = 0;

                double c_13 = 0;

                double c_14 = 0;

                double c_15 = 0;


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

            {
                auto arg = PyTuple_GET_ITEM(args, 9);
                c_9 = pyobject_to_c_double(arg);
                auto error_occurred = PyErr_Occurred();
                if (error_occurred){ return 0; }
            }

            {
                auto arg = PyTuple_GET_ITEM(args, 10);
                c_10 = pyobject_to_c_double(arg);
                auto error_occurred = PyErr_Occurred();
                if (error_occurred){ return 0; }
            }

            {
                auto arg = PyTuple_GET_ITEM(args, 11);
                c_11 = pyobject_to_c_double(arg);
                auto error_occurred = PyErr_Occurred();
                if (error_occurred){ return 0; }
            }

            {
                auto arg = PyTuple_GET_ITEM(args, 12);
                c_12 = pyobject_to_c_double(arg);
                auto error_occurred = PyErr_Occurred();
                if (error_occurred){ return 0; }
            }

            {
                auto arg = PyTuple_GET_ITEM(args, 13);
                c_13 = pyobject_to_c_double(arg);
                auto error_occurred = PyErr_Occurred();
                if (error_occurred){ return 0; }
            }

            {
                auto arg = PyTuple_GET_ITEM(args, 14);
                c_14 = pyobject_to_c_double(arg);
                auto error_occurred = PyErr_Occurred();
                if (error_occurred){ return 0; }
            }

            {
                auto arg = PyTuple_GET_ITEM(args, 15);
                c_15 = pyobject_to_c_double(arg);
                auto error_occurred = PyErr_Occurred();
                if (error_occurred){ return 0; }
            }

            glm = new DMatrix4x4Glm(

                    c_0,

                    c_1,

                    c_2,

                    c_3,

                    c_4,

                    c_5,

                    c_6,

                    c_7,

                    c_8,

                    c_9,

                    c_10,

                    c_11,

                    c_12,

                    c_13,

                    c_14,

                    c_15

            );
            break;
        }
        default:
        {
            PyErr_Format(
                PyExc_TypeError,
                "invalid number of arguments supplied to DMatrix4x4, expected "
                "0, 1, 4 or 16 (got %zd)",
                arg_count
            );
            return 0;
        }
    }

    DMatrix4x4 *self = (DMatrix4x4*)cls->tp_alloc(cls, 0);
    if (!self)
    {
        delete glm;
        return 0;
    }
    self->glm = glm;

    return (PyObject *)self;
}


static void
DMatrix4x4__dealloc__(DMatrix4x4 *self)
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
DMatrix4x4__hash__(DMatrix4x4 *self)
{
    Py_ssize_t len = 16;
    Py_uhash_t acc = _HASH_XXPRIME_5;
    for (DMatrix4x4Glm::length_type c = 0; c < 4; c++)
    {
        for (DMatrix4x4Glm::length_type r = 0; r < 4; r++)
        {
            Py_uhash_t lane = std::hash<double>{}((*self->glm)[r][c]);
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
DMatrix4x4__repr__(DMatrix4x4 *self)
{
    PyObject *result = 0;


        PyObject *py_0_0 = 0;

        PyObject *py_0_1 = 0;

        PyObject *py_0_2 = 0;

        PyObject *py_0_3 = 0;



        PyObject *py_1_0 = 0;

        PyObject *py_1_1 = 0;

        PyObject *py_1_2 = 0;

        PyObject *py_1_3 = 0;



        PyObject *py_2_0 = 0;

        PyObject *py_2_1 = 0;

        PyObject *py_2_2 = 0;

        PyObject *py_2_3 = 0;



        PyObject *py_3_0 = 0;

        PyObject *py_3_1 = 0;

        PyObject *py_3_2 = 0;

        PyObject *py_3_3 = 0;





        py_0_0 = c_double_to_pyobject((*self->glm)[0][0]);
        if (!py_0_0){ goto cleanup; }

        py_0_1 = c_double_to_pyobject((*self->glm)[1][0]);
        if (!py_0_1){ goto cleanup; }

        py_0_2 = c_double_to_pyobject((*self->glm)[2][0]);
        if (!py_0_2){ goto cleanup; }

        py_0_3 = c_double_to_pyobject((*self->glm)[3][0]);
        if (!py_0_3){ goto cleanup; }



        py_1_0 = c_double_to_pyobject((*self->glm)[0][1]);
        if (!py_1_0){ goto cleanup; }

        py_1_1 = c_double_to_pyobject((*self->glm)[1][1]);
        if (!py_1_1){ goto cleanup; }

        py_1_2 = c_double_to_pyobject((*self->glm)[2][1]);
        if (!py_1_2){ goto cleanup; }

        py_1_3 = c_double_to_pyobject((*self->glm)[3][1]);
        if (!py_1_3){ goto cleanup; }



        py_2_0 = c_double_to_pyobject((*self->glm)[0][2]);
        if (!py_2_0){ goto cleanup; }

        py_2_1 = c_double_to_pyobject((*self->glm)[1][2]);
        if (!py_2_1){ goto cleanup; }

        py_2_2 = c_double_to_pyobject((*self->glm)[2][2]);
        if (!py_2_2){ goto cleanup; }

        py_2_3 = c_double_to_pyobject((*self->glm)[3][2]);
        if (!py_2_3){ goto cleanup; }



        py_3_0 = c_double_to_pyobject((*self->glm)[0][3]);
        if (!py_3_0){ goto cleanup; }

        py_3_1 = c_double_to_pyobject((*self->glm)[1][3]);
        if (!py_3_1){ goto cleanup; }

        py_3_2 = c_double_to_pyobject((*self->glm)[2][3]);
        if (!py_3_2){ goto cleanup; }

        py_3_3 = c_double_to_pyobject((*self->glm)[3][3]);
        if (!py_3_3){ goto cleanup; }



    result = PyUnicode_FromFormat(
        "DMatrix4x4("

        "("

            "%R"
            ", "

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
            ", "

            "%R"


        ")"


        ")",


            py_0_0
            ,

            py_1_0
            ,

            py_2_0
            ,

            py_3_0
            ,



            py_0_1
            ,

            py_1_1
            ,

            py_2_1
            ,

            py_3_1
            ,



            py_0_2
            ,

            py_1_2
            ,

            py_2_2
            ,

            py_3_2
            ,



            py_0_3
            ,

            py_1_3
            ,

            py_2_3
            ,

            py_3_3



    );
cleanup:


        Py_XDECREF(py_0_0);

        Py_XDECREF(py_0_1);

        Py_XDECREF(py_0_2);

        Py_XDECREF(py_0_3);



        Py_XDECREF(py_1_0);

        Py_XDECREF(py_1_1);

        Py_XDECREF(py_1_2);

        Py_XDECREF(py_1_3);



        Py_XDECREF(py_2_0);

        Py_XDECREF(py_2_1);

        Py_XDECREF(py_2_2);

        Py_XDECREF(py_2_3);



        Py_XDECREF(py_3_0);

        Py_XDECREF(py_3_1);

        Py_XDECREF(py_3_2);

        Py_XDECREF(py_3_3);


    return result;
}


static Py_ssize_t
DMatrix4x4__len__(DMatrix4x4 *self)
{
    return 4;
}


static PyObject *
DMatrix4x4__getitem__(DMatrix4x4 *self, Py_ssize_t index)
{
    if (index < 0 || index > 3)
    {
        PyErr_Format(PyExc_IndexError, "index out of range");
        return 0;
    }
    const auto& v = (*self->glm)[(DMatrix4x4Glm::length_type)index];
    return (PyObject *)create_DVector4_from_glm(v);
}


static PyObject *
DMatrix4x4__richcmp__(DMatrix4x4 *self, DMatrix4x4 *other, int op)
{
    if (Py_TYPE(self) != Py_TYPE(other))
    {
        Py_RETURN_NOTIMPLEMENTED;
    }

    switch(op)
    {
        case Py_EQ:
        {
            if ((*self->glm) == (*other->glm))
            {
                Py_RETURN_TRUE;
            }
            else
            {
                Py_RETURN_FALSE;
            }
        }
        case Py_NE:
        {
            if ((*self->glm) != (*other->glm))
            {
                Py_RETURN_TRUE;
            }
            else
            {
                Py_RETURN_FALSE;
            }
        }
    }
    Py_RETURN_NOTIMPLEMENTED;
}


static PyObject *
DMatrix4x4__add__(PyObject *left, PyObject *right)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->DMatrix4x4_PyTypeObject;

    DMatrix4x4Glm matrix;
    if (Py_TYPE(left) == Py_TYPE(right))
    {
        matrix = (*((DMatrix4x4 *)left)->glm) + (*((DMatrix4x4 *)right)->glm);
    }
    else
    {
        if (Py_TYPE(left) == cls)
        {
            auto c_right = pyobject_to_c_double(right);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
            matrix = (*((DMatrix4x4 *)left)->glm) + c_right;
        }
        else
        {
            auto c_left = pyobject_to_c_double(left);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
            matrix = (*((DMatrix4x4 *)right)->glm) + c_left;
        }
    }

    DMatrix4x4 *result = (DMatrix4x4 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new DMatrix4x4Glm(matrix);

    return (PyObject *)result;
}


static PyObject *
DMatrix4x4__sub__(PyObject *left, PyObject *right)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->DMatrix4x4_PyTypeObject;

    DMatrix4x4Glm matrix;
    if (Py_TYPE(left) == Py_TYPE(right))
    {
        matrix = (*((DMatrix4x4 *)left)->glm) - (*((DMatrix4x4 *)right)->glm);
    }
    else
    {
        if (Py_TYPE(left) == cls)
        {
            auto c_right = pyobject_to_c_double(right);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
            matrix = (*((DMatrix4x4 *)left)->glm) - c_right;
        }
        else
        {
            auto c_left = pyobject_to_c_double(left);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }

                matrix = c_left - (*((DMatrix4x4 *)right)->glm);

        }
    }

    DMatrix4x4 *result = (DMatrix4x4 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new DMatrix4x4Glm(matrix);

    return (PyObject *)result;
}


static PyObject *
DMatrix4x4__mul__(PyObject *left, PyObject *right)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->DMatrix4x4_PyTypeObject;

    DMatrix4x4Glm matrix;
    if (Py_TYPE(left) == cls)
    {
        auto c_right = pyobject_to_c_double(right);
        if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
        matrix = (*((DMatrix4x4 *)left)->glm) * c_right;
    }
    else
    {
        auto c_left = pyobject_to_c_double(left);
        if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
        matrix = c_left * (*((DMatrix4x4 *)right)->glm);
    }

    DMatrix4x4 *result = (DMatrix4x4 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new DMatrix4x4Glm(matrix);

    return (PyObject *)result;
}


static PyObject *
DMatrix4x4__matmul__(PyObject *left, PyObject *right)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->DMatrix4x4_PyTypeObject;

    if (Py_TYPE(left) == cls)
    {



        {
            auto right_cls = module_state->DMatrix2x4_PyTypeObject;
            auto result_cls = module_state->DMatrix2x4_PyTypeObject;
            if (Py_TYPE(right) == right_cls)
            {
                DMatrix2x4 *result = (DMatrix2x4 *)result_cls->tp_alloc(result_cls, 0);
                if (!result){ return 0; }
                result->glm = new DMatrix2x4Glm(
                    (*((DMatrix4x4 *)left)->glm) * (*((DMatrix2x4 *)right)->glm)
                );
                return (PyObject *)result;
            }
        }





        {
            auto right_cls = module_state->DMatrix3x4_PyTypeObject;
            auto result_cls = module_state->DMatrix3x4_PyTypeObject;
            if (Py_TYPE(right) == right_cls)
            {
                DMatrix3x4 *result = (DMatrix3x4 *)result_cls->tp_alloc(result_cls, 0);
                if (!result){ return 0; }
                result->glm = new DMatrix3x4Glm(
                    (*((DMatrix4x4 *)left)->glm) * (*((DMatrix3x4 *)right)->glm)
                );
                return (PyObject *)result;
            }
        }





        {
            auto right_cls = module_state->DMatrix4x4_PyTypeObject;
            auto result_cls = module_state->DMatrix4x4_PyTypeObject;
            if (Py_TYPE(right) == right_cls)
            {
                DMatrix4x4 *result = (DMatrix4x4 *)result_cls->tp_alloc(result_cls, 0);
                if (!result){ return 0; }
                result->glm = new DMatrix4x4Glm(
                    (*((DMatrix4x4 *)left)->glm) * (*((DMatrix4x4 *)right)->glm)
                );
                return (PyObject *)result;
            }
        }




        {
            auto row_cls = module_state->DVector4_PyTypeObject;
            auto column_cls = module_state->DVector4_PyTypeObject;
            if (Py_TYPE(right) == row_cls)
            {
                DVector4 *result = (DVector4 *)column_cls->tp_alloc(column_cls, 0);
                if (!result){ return 0; }
                result->glm = new DVector4Glm(
                    (*((DMatrix4x4 *)left)->glm) * (*((DVector4 *)right)->glm)
                );
                return (PyObject *)result;
            }
        }
    }
    else
    {
        auto row_cls = module_state->DVector4_PyTypeObject;
        auto column_cls = module_state->DVector4_PyTypeObject;
        if (Py_TYPE(left) == column_cls)
        {
            DVector4 *result = (DVector4 *)row_cls->tp_alloc(row_cls, 0);
            if (!result){ return 0; }
            result->glm = new DVector4Glm(
                (*((DVector4 *)left)->glm) * (*((DMatrix4x4 *)right)->glm)
            );
            return (PyObject *)result;
        }
    }

    Py_RETURN_NOTIMPLEMENTED;
}

static PyObject *
DMatrix4x4__truediv__(PyObject *left, PyObject *right)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->DMatrix4x4_PyTypeObject;

    DMatrix4x4Glm matrix;
    if (Py_TYPE(left) == cls)
    {

        if (Py_TYPE(right) == cls)
        {
            DMatrix4x4 *result = (DMatrix4x4 *)cls->tp_alloc(cls, 0);
            if (!result){ return 0; }
            result->glm = new DMatrix4x4Glm(
                (*((DMatrix4x4 *)left)->glm) / (*((DMatrix4x4 *)right)->glm)
            );
            return (PyObject *)result;
        }

        {
            auto row_cls = module_state->DVector4_PyTypeObject;
            if (Py_TYPE(right) == row_cls)
            {
                DVector4 *result = (DVector4 *)row_cls->tp_alloc(row_cls, 0);
                if (!result){ return 0; }
                result->glm = new DVector4Glm(
                    (*((DMatrix4x4 *)left)->glm) / (*((DVector4 *)right)->glm)
                );
                return (PyObject *)result;
            }
        }


        auto c_right = pyobject_to_c_double(right);
        if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
        matrix = (*((DMatrix4x4 *)left)->glm) / c_right;
    }
    else
    {

        {
            auto row_cls = module_state->DVector4_PyTypeObject;
            if (Py_TYPE(left) == row_cls)
            {
                DVector4 *result = (DVector4 *)row_cls->tp_alloc(row_cls, 0);
                if (!result){ return 0; }
                result->glm = new DVector4Glm(
                    (*((DVector4 *)left)->glm) / (*((DMatrix4x4 *)right)->glm)
                );
                return (PyObject *)result;
            }
        }


        auto c_left = pyobject_to_c_double(left);
        if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
        matrix = c_left / (*((DMatrix4x4 *)right)->glm);
    }

    DMatrix4x4 *result = (DMatrix4x4 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new DMatrix4x4Glm(matrix);

    return (PyObject *)result;
}


static PyObject *
DMatrix4x4__neg__(DMatrix4x4 *self)
{
    auto cls = Py_TYPE(self);

    DMatrix4x4 *result = (DMatrix4x4 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new DMatrix4x4Glm(-(*self->glm));

    return (PyObject *)result;
}


static int
DMatrix4x4_getbufferproc(DMatrix4x4 *self, Py_buffer *view, int flags)
{
    if (flags & PyBUF_WRITABLE)
    {
        PyErr_SetString(PyExc_TypeError, "DMatrix4x4 is read only");
        view->obj = 0;
        return -1;
    }
    view->buf = glm::value_ptr(*self->glm);
    view->obj = (PyObject *)self;
    view->len = sizeof(double) * 16;
    view->readonly = 1;
    view->itemsize = sizeof(double);
    view->format = "d";
    view->ndim = 2;
    static Py_ssize_t shape[] = { 4, 4 };
    view->shape = &shape[0];
    static Py_ssize_t strides[] = {
        sizeof(double) * 4,
        sizeof(double)
    };
    view->strides = &strides[0];
    view->suboffsets = 0;
    view->internal = 0;
    Py_INCREF(self);
    return 0;
}


static PyMemberDef DMatrix4x4_PyMemberDef[] = {
    {"__weaklistoffset__", T_PYSSIZET, offsetof(DMatrix4x4, weakreflist), READONLY},
    {0}
};



    static DMatrix4x4 *
    DMatrix4x4_inverse(DMatrix4x4 *self, void*)
    {
        auto cls = Py_TYPE(self);
        auto matrix = glm::inverse(*self->glm);
        DMatrix4x4 *result = (DMatrix4x4 *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new DMatrix4x4Glm(matrix);
        return result;
    }




static DMatrix4x4 *
DMatrix4x4_transpose(DMatrix4x4 *self, void*)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->DMatrix4x4_PyTypeObject;

    DMatrix4x4Glm matrix = glm::transpose(*self->glm);
    DMatrix4x4 *result = (DMatrix4x4 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new DMatrix4x4Glm(matrix);
    return result;
}



static PyObject *
DMatrix4x4_get_limits(DMatrix4x4 *self, void *)
{
    auto c_min = std::numeric_limits<double>::lowest();
    auto c_max = std::numeric_limits<double>::max();
    auto py_min = c_double_to_pyobject(c_min);
    if (!py_min){ return 0; }
    auto py_max = c_double_to_pyobject(c_max);
    if (!py_max)
    {
        Py_DECREF(py_min);
        return 0;
    }
    auto result = PyTuple_New(2);
    if (!result)
    {
        Py_DECREF(py_min);
        Py_DECREF(py_max);
        return 0;
    }
    PyTuple_SET_ITEM(result, 0, py_min);
    PyTuple_SET_ITEM(result, 1, py_max);
    return result;
}


static PyMethodDef DMatrix4x4_PyMethodDef[] = {

        {"inverse", (PyCFunction)DMatrix4x4_inverse, METH_NOARGS, 0},

    {"transpose", (PyCFunction)DMatrix4x4_transpose, METH_NOARGS, 0},
    {"get_limits", (PyCFunction)DMatrix4x4_get_limits, METH_NOARGS | METH_STATIC, 0},
    {0, 0, 0, 0}
};


static PyType_Slot DMatrix4x4_PyType_Slots [] = {
    {Py_tp_new, (void*)DMatrix4x4__new__},
    {Py_tp_dealloc, (void*)DMatrix4x4__dealloc__},
    {Py_tp_hash, (void*)DMatrix4x4__hash__},
    {Py_tp_repr, (void*)DMatrix4x4__repr__},
    {Py_sq_length, (void*)DMatrix4x4__len__},
    {Py_sq_item, (void*)DMatrix4x4__getitem__},
    {Py_tp_richcompare, (void*)DMatrix4x4__richcmp__},
    {Py_nb_add, (void*)DMatrix4x4__add__},
    {Py_nb_subtract, (void*)DMatrix4x4__sub__},
    {Py_nb_multiply, (void*)DMatrix4x4__mul__},
    {Py_nb_matrix_multiply, (void*)DMatrix4x4__matmul__},
    {Py_nb_true_divide, (void*)DMatrix4x4__truediv__},
    {Py_nb_negative, (void*)DMatrix4x4__neg__},
    {Py_bf_getbuffer, (void*)DMatrix4x4_getbufferproc},
    {Py_tp_members, (void*)DMatrix4x4_PyMemberDef},
    {Py_tp_methods, (void*)DMatrix4x4_PyMethodDef},
    {0, 0},
};


static PyType_Spec DMatrix4x4_PyTypeSpec = {
    "gamut.math.DMatrix4x4",
    sizeof(DMatrix4x4),
    0,
    Py_TPFLAGS_DEFAULT,
    DMatrix4x4_PyType_Slots
};


static PyTypeObject *
define_DMatrix4x4_type(PyObject *module)
{
    PyTypeObject *type = (PyTypeObject *)PyType_FromModuleAndSpec(
        module,
        &DMatrix4x4_PyTypeSpec,
        0
    );
    if (!type){ return 0; }
    // Note:
    // Unlike other functions that steal references, PyModule_AddObject() only
    // decrements the reference count of value on success.
    if (PyModule_AddObject(module, "DMatrix4x4", (PyObject *)type) < 0)
    {
        Py_DECREF(type);
        return 0;
    }
    return type;
}

#endif