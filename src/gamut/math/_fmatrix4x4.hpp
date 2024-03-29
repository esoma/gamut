
// generated from codegen/math/templates/_matrix.hpp

#ifndef GAMUT_MATH_FMATRIX4X4_HPP
#define GAMUT_MATH_FMATRIX4X4_HPP

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
#include "_vectortype.hpp"
#include "_matrixtype.hpp"
#include "_type.hpp"


static PyObject *
FMatrix4x4__new__(PyTypeObject *cls, PyObject *args, PyObject *kwds)
{
    if (kwds && PyDict_Size(kwds) != 0)
    {
        PyErr_SetString(
            PyExc_TypeError,
            "FMatrix4x4 does accept any keyword arguments"
        );
        return 0;
    }

    FMatrix4x4Glm *glm = 0;
    auto arg_count = PyTuple_GET_SIZE(args);
    switch (PyTuple_GET_SIZE(args))
    {
        case 0:
        {
            glm = new FMatrix4x4Glm();
            break;
        }
        case 1:
        {
            auto arg = PyTuple_GET_ITEM(args, 0);
            float arg_c = pyobject_to_c_float(arg);
            auto error_occurred = PyErr_Occurred();
            if (error_occurred){ return 0; }
            glm = new FMatrix4x4Glm(arg_c);
            break;
        }
        case 4:
        {
            auto module_state = get_module_state();
            if (!module_state){ return 0; }
            auto column_cls = module_state->FVector4_PyTypeObject;

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

            glm = new FMatrix4x4Glm(

                    *((FVector4 *)p_0)->glm,

                    *((FVector4 *)p_1)->glm,

                    *((FVector4 *)p_2)->glm,

                    *((FVector4 *)p_3)->glm

            );

            break;
        }
        case 16:
        {

                float c_0 = 0;

                float c_1 = 0;

                float c_2 = 0;

                float c_3 = 0;

                float c_4 = 0;

                float c_5 = 0;

                float c_6 = 0;

                float c_7 = 0;

                float c_8 = 0;

                float c_9 = 0;

                float c_10 = 0;

                float c_11 = 0;

                float c_12 = 0;

                float c_13 = 0;

                float c_14 = 0;

                float c_15 = 0;


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

            {
                auto arg = PyTuple_GET_ITEM(args, 8);
                c_8 = pyobject_to_c_float(arg);
                auto error_occurred = PyErr_Occurred();
                if (error_occurred){ return 0; }
            }

            {
                auto arg = PyTuple_GET_ITEM(args, 9);
                c_9 = pyobject_to_c_float(arg);
                auto error_occurred = PyErr_Occurred();
                if (error_occurred){ return 0; }
            }

            {
                auto arg = PyTuple_GET_ITEM(args, 10);
                c_10 = pyobject_to_c_float(arg);
                auto error_occurred = PyErr_Occurred();
                if (error_occurred){ return 0; }
            }

            {
                auto arg = PyTuple_GET_ITEM(args, 11);
                c_11 = pyobject_to_c_float(arg);
                auto error_occurred = PyErr_Occurred();
                if (error_occurred){ return 0; }
            }

            {
                auto arg = PyTuple_GET_ITEM(args, 12);
                c_12 = pyobject_to_c_float(arg);
                auto error_occurred = PyErr_Occurred();
                if (error_occurred){ return 0; }
            }

            {
                auto arg = PyTuple_GET_ITEM(args, 13);
                c_13 = pyobject_to_c_float(arg);
                auto error_occurred = PyErr_Occurred();
                if (error_occurred){ return 0; }
            }

            {
                auto arg = PyTuple_GET_ITEM(args, 14);
                c_14 = pyobject_to_c_float(arg);
                auto error_occurred = PyErr_Occurred();
                if (error_occurred){ return 0; }
            }

            {
                auto arg = PyTuple_GET_ITEM(args, 15);
                c_15 = pyobject_to_c_float(arg);
                auto error_occurred = PyErr_Occurred();
                if (error_occurred){ return 0; }
            }

            glm = new FMatrix4x4Glm(

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
                "invalid number of arguments supplied to FMatrix4x4, expected "
                "0, 1, 4 or 16 (got %zd)",
                arg_count
            );
            return 0;
        }
    }

    FMatrix4x4 *self = (FMatrix4x4*)cls->tp_alloc(cls, 0);
    if (!self)
    {
        delete glm;
        return 0;
    }
    self->glm = glm;

    return (PyObject *)self;
}


static void
FMatrix4x4__dealloc__(FMatrix4x4 *self)
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
FMatrix4x4__hash__(FMatrix4x4 *self)
{
    Py_ssize_t len = 16;
    Py_uhash_t acc = _HASH_XXPRIME_5;
    for (FMatrix4x4Glm::length_type c = 0; c < 4; c++)
    {
        for (FMatrix4x4Glm::length_type r = 0; r < 4; r++)
        {
            Py_uhash_t lane = std::hash<float>{}((*self->glm)[r][c]);
            acc += lane * _HASH_XXPRIME_2;
            acc = _HASH_XXROTATE(acc);
            acc *= _HASH_XXPRIME_1;
        }
        acc += len ^ (_HASH_XXPRIME_5 ^ 3527539UL);
    }

    if (acc == (Py_uhash_t)-1) {
        return 1546275796;
    }
    return acc;
}


static PyObject *
FMatrix4x4__repr__(FMatrix4x4 *self)
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





        py_0_0 = c_float_to_pyobject((*self->glm)[0][0]);
        if (!py_0_0){ goto cleanup; }

        py_0_1 = c_float_to_pyobject((*self->glm)[1][0]);
        if (!py_0_1){ goto cleanup; }

        py_0_2 = c_float_to_pyobject((*self->glm)[2][0]);
        if (!py_0_2){ goto cleanup; }

        py_0_3 = c_float_to_pyobject((*self->glm)[3][0]);
        if (!py_0_3){ goto cleanup; }



        py_1_0 = c_float_to_pyobject((*self->glm)[0][1]);
        if (!py_1_0){ goto cleanup; }

        py_1_1 = c_float_to_pyobject((*self->glm)[1][1]);
        if (!py_1_1){ goto cleanup; }

        py_1_2 = c_float_to_pyobject((*self->glm)[2][1]);
        if (!py_1_2){ goto cleanup; }

        py_1_3 = c_float_to_pyobject((*self->glm)[3][1]);
        if (!py_1_3){ goto cleanup; }



        py_2_0 = c_float_to_pyobject((*self->glm)[0][2]);
        if (!py_2_0){ goto cleanup; }

        py_2_1 = c_float_to_pyobject((*self->glm)[1][2]);
        if (!py_2_1){ goto cleanup; }

        py_2_2 = c_float_to_pyobject((*self->glm)[2][2]);
        if (!py_2_2){ goto cleanup; }

        py_2_3 = c_float_to_pyobject((*self->glm)[3][2]);
        if (!py_2_3){ goto cleanup; }



        py_3_0 = c_float_to_pyobject((*self->glm)[0][3]);
        if (!py_3_0){ goto cleanup; }

        py_3_1 = c_float_to_pyobject((*self->glm)[1][3]);
        if (!py_3_1){ goto cleanup; }

        py_3_2 = c_float_to_pyobject((*self->glm)[2][3]);
        if (!py_3_2){ goto cleanup; }

        py_3_3 = c_float_to_pyobject((*self->glm)[3][3]);
        if (!py_3_3){ goto cleanup; }



    result = PyUnicode_FromFormat(
        "FMatrix4x4("

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
FMatrix4x4__len__(FMatrix4x4 *self)
{
    return 4;
}


static PyObject *
FMatrix4x4__getitem__(FMatrix4x4 *self, Py_ssize_t index)
{
    if (index < 0 || index > 3)
    {
        PyErr_Format(PyExc_IndexError, "index out of range");
        return 0;
    }
    const auto& v = (*self->glm)[(FMatrix4x4Glm::length_type)index];
    return (PyObject *)create_FVector4_from_glm(v);
}


static PyObject *
FMatrix4x4__richcmp__(FMatrix4x4 *self, FMatrix4x4 *other, int op)
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
FMatrix4x4__add__(PyObject *left, PyObject *right)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->FMatrix4x4_PyTypeObject;

    FMatrix4x4Glm matrix;
    if (Py_TYPE(left) == Py_TYPE(right))
    {
        matrix = (*((FMatrix4x4 *)left)->glm) + (*((FMatrix4x4 *)right)->glm);
    }
    else
    {
        if (Py_TYPE(left) == cls)
        {
            auto c_right = pyobject_to_c_float(right);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
            matrix = (*((FMatrix4x4 *)left)->glm) + c_right;
        }
        else
        {
            auto c_left = pyobject_to_c_float(left);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
            matrix = (*((FMatrix4x4 *)right)->glm) + c_left;
        }
    }

    FMatrix4x4 *result = (FMatrix4x4 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new FMatrix4x4Glm(matrix);

    return (PyObject *)result;
}


static PyObject *
FMatrix4x4__sub__(PyObject *left, PyObject *right)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->FMatrix4x4_PyTypeObject;

    FMatrix4x4Glm matrix;
    if (Py_TYPE(left) == Py_TYPE(right))
    {
        matrix = (*((FMatrix4x4 *)left)->glm) - (*((FMatrix4x4 *)right)->glm);
    }
    else
    {
        if (Py_TYPE(left) == cls)
        {
            auto c_right = pyobject_to_c_float(right);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
            matrix = (*((FMatrix4x4 *)left)->glm) - c_right;
        }
        else
        {
            auto c_left = pyobject_to_c_float(left);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }

                matrix = c_left - (*((FMatrix4x4 *)right)->glm);

        }
    }

    FMatrix4x4 *result = (FMatrix4x4 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new FMatrix4x4Glm(matrix);

    return (PyObject *)result;
}


static PyObject *
FMatrix4x4__mul__(PyObject *left, PyObject *right)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->FMatrix4x4_PyTypeObject;

    FMatrix4x4Glm matrix;
    if (Py_TYPE(left) == cls)
    {
        auto c_right = pyobject_to_c_float(right);
        if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
        matrix = (*((FMatrix4x4 *)left)->glm) * c_right;
    }
    else
    {
        auto c_left = pyobject_to_c_float(left);
        if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
        matrix = c_left * (*((FMatrix4x4 *)right)->glm);
    }

    FMatrix4x4 *result = (FMatrix4x4 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new FMatrix4x4Glm(matrix);

    return (PyObject *)result;
}


static PyObject *
FMatrix4x4__matmul__(PyObject *left, PyObject *right)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->FMatrix4x4_PyTypeObject;

    if (Py_TYPE(left) == cls)
    {



        {
            auto right_cls = module_state->FMatrix2x4_PyTypeObject;
            auto result_cls = module_state->FMatrix2x4_PyTypeObject;
            if (Py_TYPE(right) == right_cls)
            {
                FMatrix2x4 *result = (FMatrix2x4 *)result_cls->tp_alloc(result_cls, 0);
                if (!result){ return 0; }
                result->glm = new FMatrix2x4Glm(
                    (*((FMatrix4x4 *)left)->glm) * (*((FMatrix2x4 *)right)->glm)
                );
                return (PyObject *)result;
            }
        }





        {
            auto right_cls = module_state->FMatrix3x4_PyTypeObject;
            auto result_cls = module_state->FMatrix3x4_PyTypeObject;
            if (Py_TYPE(right) == right_cls)
            {
                FMatrix3x4 *result = (FMatrix3x4 *)result_cls->tp_alloc(result_cls, 0);
                if (!result){ return 0; }
                result->glm = new FMatrix3x4Glm(
                    (*((FMatrix4x4 *)left)->glm) * (*((FMatrix3x4 *)right)->glm)
                );
                return (PyObject *)result;
            }
        }





        {
            auto right_cls = module_state->FMatrix4x4_PyTypeObject;
            auto result_cls = module_state->FMatrix4x4_PyTypeObject;
            if (Py_TYPE(right) == right_cls)
            {
                FMatrix4x4 *result = (FMatrix4x4 *)result_cls->tp_alloc(result_cls, 0);
                if (!result){ return 0; }
                result->glm = new FMatrix4x4Glm(
                    (*((FMatrix4x4 *)left)->glm) * (*((FMatrix4x4 *)right)->glm)
                );
                return (PyObject *)result;
            }
        }





        {
            auto vector3_cls = module_state->FVector3_PyTypeObject;
            if (Py_TYPE(right) == vector3_cls)
            {
                auto result = (FVector3 *)vector3_cls->tp_alloc(vector3_cls, 0);
                if (!result){ return 0; }
                result->glm = new FVector3Glm(
                    (*((FMatrix4x4 *)left)->glm) * FVector4Glm(
                        *((FVector3 *)right)->glm,
                        1
                    )
                );
                return (PyObject *)result;
            }
        }


        {
            auto row_cls = module_state->FVector4_PyTypeObject;
            auto column_cls = module_state->FVector4_PyTypeObject;
            if (Py_TYPE(right) == row_cls)
            {
                FVector4 *result = (FVector4 *)column_cls->tp_alloc(column_cls, 0);
                if (!result){ return 0; }
                result->glm = new FVector4Glm(
                    (*((FMatrix4x4 *)left)->glm) * (*((FVector4 *)right)->glm)
                );
                return (PyObject *)result;
            }
        }
    }
    else
    {

        {
            auto vector3_cls = module_state->FVector3_PyTypeObject;
            if (Py_TYPE(left) == vector3_cls)
            {
                auto result = (FVector3 *)vector3_cls->tp_alloc(vector3_cls, 0);
                if (!result){ return 0; }
                result->glm = new FVector3Glm(
                     FVector4Glm(
                        *((FVector3 *)left)->glm,
                        1
                    ) * (*((FMatrix4x4 *)right)->glm)
                );
                return (PyObject *)result;
            }
        }


        auto row_cls = module_state->FVector4_PyTypeObject;
        auto column_cls = module_state->FVector4_PyTypeObject;
        if (Py_TYPE(left) == column_cls)
        {
            FVector4 *result = (FVector4 *)row_cls->tp_alloc(row_cls, 0);
            if (!result){ return 0; }
            result->glm = new FVector4Glm(
                (*((FVector4 *)left)->glm) * (*((FMatrix4x4 *)right)->glm)
            );
            return (PyObject *)result;
        }
    }

    Py_RETURN_NOTIMPLEMENTED;
}

static PyObject *
FMatrix4x4__truediv__(PyObject *left, PyObject *right)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->FMatrix4x4_PyTypeObject;

    FMatrix4x4Glm matrix;
    if (Py_TYPE(left) == cls)
    {

        if (Py_TYPE(right) == cls)
        {
            FMatrix4x4 *result = (FMatrix4x4 *)cls->tp_alloc(cls, 0);
            if (!result){ return 0; }
            result->glm = new FMatrix4x4Glm(
                (*((FMatrix4x4 *)left)->glm) / (*((FMatrix4x4 *)right)->glm)
            );
            return (PyObject *)result;
        }

        {
            auto row_cls = module_state->FVector4_PyTypeObject;
            if (Py_TYPE(right) == row_cls)
            {
                FVector4 *result = (FVector4 *)row_cls->tp_alloc(row_cls, 0);
                if (!result){ return 0; }
                result->glm = new FVector4Glm(
                    (*((FMatrix4x4 *)left)->glm) / (*((FVector4 *)right)->glm)
                );
                return (PyObject *)result;
            }
        }


        auto c_right = pyobject_to_c_float(right);
        if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
        matrix = (*((FMatrix4x4 *)left)->glm) / c_right;
    }
    else
    {

        {
            auto row_cls = module_state->FVector4_PyTypeObject;
            if (Py_TYPE(left) == row_cls)
            {
                FVector4 *result = (FVector4 *)row_cls->tp_alloc(row_cls, 0);
                if (!result){ return 0; }
                result->glm = new FVector4Glm(
                    (*((FVector4 *)left)->glm) / (*((FMatrix4x4 *)right)->glm)
                );
                return (PyObject *)result;
            }
        }


        auto c_left = pyobject_to_c_float(left);
        if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
        matrix = c_left / (*((FMatrix4x4 *)right)->glm);
    }

    FMatrix4x4 *result = (FMatrix4x4 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new FMatrix4x4Glm(matrix);

    return (PyObject *)result;
}


static PyObject *
FMatrix4x4__neg__(FMatrix4x4 *self)
{
    auto cls = Py_TYPE(self);

    FMatrix4x4 *result = (FMatrix4x4 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new FMatrix4x4Glm(-(*self->glm));

    return (PyObject *)result;
}


static int
FMatrix4x4_getbufferproc(FMatrix4x4 *self, Py_buffer *view, int flags)
{
    if (flags & PyBUF_WRITABLE)
    {
        PyErr_SetString(PyExc_TypeError, "FMatrix4x4 is read only");
        view->obj = 0;
        return -1;
    }
    if ((!(flags & PyBUF_C_CONTIGUOUS)) && flags & PyBUF_F_CONTIGUOUS)
    {
        PyErr_SetString(PyExc_BufferError, "FMatrix4x4 cannot be made Fortran contiguous");
        view->obj = 0;
        return -1;
    }
    view->buf = glm::value_ptr(*self->glm);
    view->obj = (PyObject *)self;
    view->len = sizeof(float) * 16;
    view->readonly = 1;
    view->itemsize = sizeof(float);
    view->ndim = 2;
    if (flags & PyBUF_FORMAT)
    {
        view->format = "f";
    }
    else
    {
        view->format = 0;
    }
    if (flags & PyBUF_ND)
    {
        static Py_ssize_t shape[] = { 4, 4 };
        view->shape = &shape[0];
    }
    else
    {
        view->shape = 0;
    }
    if (flags & PyBUF_STRIDES)
    {
        static Py_ssize_t strides[] = {
            sizeof(float) * 4,
            sizeof(float)
        };
        view->strides = &strides[0];
    }
    else
    {
        view->strides = 0;
    }
    view->suboffsets = 0;
    view->internal = 0;
    Py_INCREF(self);
    return 0;
}


static PyMemberDef FMatrix4x4_PyMemberDef[] = {
    {"__weaklistoffset__", T_PYSSIZET, offsetof(FMatrix4x4, weakreflist), READONLY},
    {0}
};


static PyObject *
FMatrix4x4_pointer(FMatrix4x4 *self, void *)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto c_p = module_state->ctypes_c_float_p;
    return PyObject_CallMethod(c_p, "from_address", "n", (Py_ssize_t)&self->glm);
}


static PyGetSetDef FMatrix4x4_PyGetSetDef[] = {
    {"pointer", (getter)FMatrix4x4_pointer, 0, 0, 0},
    {0, 0, 0, 0, 0}
};



    static FMatrix4x4 *
    FMatrix4x4_inverse(FMatrix4x4 *self, void*)
    {
        auto cls = Py_TYPE(self);
        auto matrix = glm::inverse(*self->glm);
        FMatrix4x4 *result = (FMatrix4x4 *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new FMatrix4x4Glm(matrix);
        return result;
    }




    static FMatrix4x4 *
    FMatrix4x4_rotate(FMatrix4x4 *self, PyObject *const *args, Py_ssize_t nargs)
    {
        if (nargs != 2)
        {
            PyErr_Format(PyExc_TypeError, "expected 2 arguments, got %zi", nargs);
            return 0;
        }

        float angle = (float)PyFloat_AsDouble(args[0]);
        if (PyErr_Occurred()){ return 0; }

        auto module_state = get_module_state();
        if (!module_state){ return 0; }
        auto vector_cls = module_state->FVector3_PyTypeObject;
        if (Py_TYPE(args[1]) != vector_cls)
        {
            PyErr_Format(PyExc_TypeError, "expected FVector3, got %R", args[0]);
            return 0;
        }
        FVector3 *vector = (FVector3 *)args[1];

        auto matrix = glm::rotate(*self->glm, angle, *vector->glm);

        auto cls = Py_TYPE(self);
        auto *result = (FMatrix4x4 *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new FMatrix4x4Glm(matrix);
        return result;
    }

    static FMatrix4x4 *
    FMatrix4x4_scale(FMatrix4x4 *self, PyObject *const *args, Py_ssize_t nargs)
    {
        if (nargs != 1)
        {
            PyErr_Format(PyExc_TypeError, "expected 1 argument, got %zi", nargs);
            return 0;
        }

        auto module_state = get_module_state();
        if (!module_state){ return 0; }
        auto vector_cls = module_state->FVector3_PyTypeObject;
        if (Py_TYPE(args[0]) != vector_cls)
        {
            PyErr_Format(PyExc_TypeError, "expected FVector3, got %R", args[0]);
            return 0;
        }
        FVector3 *vector = (FVector3 *)args[0];

        auto matrix = glm::scale(*self->glm, *vector->glm);

        auto cls = Py_TYPE(self);
        auto *result = (FMatrix4x4 *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new FMatrix4x4Glm(matrix);
        return result;
    }

    static FMatrix4x4 *
    FMatrix4x4_translate(FMatrix4x4 *self, PyObject *const *args, Py_ssize_t nargs)
    {
        if (nargs != 1)
        {
            PyErr_Format(PyExc_TypeError, "expected 1 argument, got %zi", nargs);
            return 0;
        }

        auto module_state = get_module_state();
        if (!module_state){ return 0; }
        auto vector_cls = module_state->FVector3_PyTypeObject;
        if (Py_TYPE(args[0]) != vector_cls)
        {
            PyErr_Format(PyExc_TypeError, "expected FVector3, got %R", args[0]);
            return 0;
        }
        FVector3 *vector = (FVector3 *)args[0];

        auto matrix = glm::translate(*self->glm, *vector->glm);

        auto cls = Py_TYPE(self);
        auto *result = (FMatrix4x4 *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new FMatrix4x4Glm(matrix);
        return result;
    }

    static FMatrix4x4 *
    FMatrix4x4_perspective(PyTypeObject *cls, PyObject *const *args, Py_ssize_t nargs)
    {
        if (nargs != 4)
        {
            PyErr_Format(PyExc_TypeError, "expected 4 argument, got %zi", nargs);
            return 0;
        }

        double fov = PyFloat_AsDouble(args[0]);
        if (PyErr_Occurred()){ return 0; }
        double aspect = PyFloat_AsDouble(args[1]);
        if (PyErr_Occurred()){ return 0; }
        double near = PyFloat_AsDouble(args[2]);
        if (PyErr_Occurred()){ return 0; }
        double far = PyFloat_AsDouble(args[3]);
        if (PyErr_Occurred()){ return 0; }

        auto *result = (FMatrix4x4 *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new FMatrix4x4Glm(glm::perspective(fov, aspect, near, far));
        return result;
    }

    static FMatrix4x4 *
    FMatrix4x4_orthographic(PyTypeObject *cls, PyObject *const *args, Py_ssize_t nargs)
    {
        if (nargs != 6)
        {
            PyErr_Format(PyExc_TypeError, "expected 6 argument, got %zi", nargs);
            return 0;
        }

        double left = PyFloat_AsDouble(args[0]);
        if (PyErr_Occurred()){ return 0; }
        double right = PyFloat_AsDouble(args[1]);
        if (PyErr_Occurred()){ return 0; }
        double bottom = PyFloat_AsDouble(args[2]);
        if (PyErr_Occurred()){ return 0; }
        double top = PyFloat_AsDouble(args[3]);
        if (PyErr_Occurred()){ return 0; }
        double near = PyFloat_AsDouble(args[4]);
        if (PyErr_Occurred()){ return 0; }
        double far = PyFloat_AsDouble(args[5]);
        if (PyErr_Occurred()){ return 0; }

        auto *result = (FMatrix4x4 *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new FMatrix4x4Glm(glm::ortho(left, right, bottom, top, near, far));
        return result;
    }

    static FMatrix4x4 *
    FMatrix4x4_look_at(PyTypeObject *cls, PyObject *const *args, Py_ssize_t nargs)
    {
        if (nargs != 3)
        {
            PyErr_Format(PyExc_TypeError, "expected 3 argument, got %zi", nargs);
            return 0;
        }

        auto module_state = get_module_state();
        if (!module_state){ return 0; }
        auto vec3_cls = module_state->FVector3_PyTypeObject;

        if (Py_TYPE(args[0]) != vec3_cls)
        {
            PyErr_Format(PyExc_TypeError, "expected FVector3 for eye, got %R", args[0]);
            return 0;
        }
        auto eye = (FVector3 *)args[0];
        if (Py_TYPE(args[1]) != vec3_cls)
        {
            PyErr_Format(PyExc_TypeError, "expected FVector3 for center, got %R", args[1]);
            return 0;
        }
        auto center = (FVector3 *)args[1];
        if (Py_TYPE(args[2]) != vec3_cls)
        {
            PyErr_Format(PyExc_TypeError, "expected FVector3 for up, got %R", args[2]);
            return 0;
        }
        auto up = (FVector3 *)args[2];

        auto *result = (FMatrix4x4 *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new FMatrix4x4Glm(glm::lookAt(*eye->glm, *center->glm, *up->glm));
        return result;
    }

    static FMatrix3x3 *
    FMatrix4x4_to_matrix3(FMatrix4x4 *self, void*)
    {
        auto module_state = get_module_state();
        if (!module_state){ return 0; }
        auto cls = module_state->FMatrix3x3_PyTypeObject;

        auto *result = (FMatrix3x3 *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new FMatrix3x3Glm(*self->glm);
        return result;
    }




    static FQuaternion *
    FMatrix4x4_to_quaternion(FMatrix4x4 *self, void*)
    {
        auto module_state = get_module_state();
        if (!module_state){ return 0; }
        auto cls = module_state->FQuaternion_PyTypeObject;

        auto *result = (FQuaternion *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new FQuaternionGlm(glm::quat_cast(*self->glm));
        return result;
    }



static FVector4 *
FMatrix4x4_get_row(FMatrix4x4 *self, PyObject *const *args, Py_ssize_t nargs)
{
    if (nargs != 1)
    {
        PyErr_Format(PyExc_TypeError, "expected 1 argument, got %zi", nargs);
        return 0;
    }

    auto index = PyLong_AsLong(args[0]);
    if (PyErr_Occurred()){ return 0; }
    if (index < 0 || index > 3)
    {
        PyErr_Format(PyExc_IndexError, "index out of range");
        return 0;
    }

    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto row_cls = module_state->FVector4_PyTypeObject;

    auto *result = (FVector4 *)row_cls->tp_alloc(row_cls, 0);
    if (!result){ return 0; }
    auto row = glm::row(*self->glm, index);
    result->glm = new FVector4Glm(row);
    return result;
}



static FMatrix4x4 *
FMatrix4x4_transpose(FMatrix4x4 *self, void*)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->FMatrix4x4_PyTypeObject;

    FMatrix4x4Glm matrix = glm::transpose(*self->glm);
    FMatrix4x4 *result = (FMatrix4x4 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new FMatrix4x4Glm(matrix);
    return result;
}



static PyObject *
FMatrix4x4_get_size(FMatrix4x4 *cls, void *)
{
    return PyLong_FromSize_t(sizeof(float) * 16);
}


static PyObject *
FMatrix4x4_get_limits(FMatrix4x4 *self, void *)
{
    auto c_min = std::numeric_limits<float>::lowest();
    auto c_max = std::numeric_limits<float>::max();
    auto py_min = c_float_to_pyobject(c_min);
    if (!py_min){ return 0; }
    auto py_max = c_float_to_pyobject(c_max);
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


static PyObject *
FMatrix4x4_from_buffer(PyTypeObject *cls, PyObject *buffer)
{
    static Py_ssize_t expected_size = sizeof(float) * 16;
    Py_buffer view;
    if (PyObject_GetBuffer(buffer, &view, PyBUF_SIMPLE) == -1){ return 0; }
    auto view_length = view.len;
    if (view_length < expected_size)
    {
        PyBuffer_Release(&view);
        PyErr_Format(PyExc_BufferError, "expected buffer of size %zd, got %zd", expected_size, view_length);
        return 0;
    }

    auto *result = (FMatrix4x4 *)cls->tp_alloc(cls, 0);
    if (!result)
    {
        PyBuffer_Release(&view);
        return 0;
    }
    result->glm = new FMatrix4x4Glm();
    std::memcpy(result->glm, view.buf, expected_size);
    PyBuffer_Release(&view);
    return (PyObject *)result;
}






    static DMatrix4x4 *
    FMatrix4x4_to_dmatrix(FMatrix4x4 *self, void*)
    {
        auto module_state = get_module_state();
        if (!module_state){ return 0; }
        auto cls = module_state->DMatrix4x4_PyTypeObject;

        auto *result = (DMatrix4x4 *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new DMatrix4x4Glm(*self->glm);
        return result;
    }



static PyObject *
FMatrix4x4_get_array_type(PyTypeObject *cls, void*)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto array_type = module_state->FMatrix4x4Array_PyTypeObject;
    Py_INCREF(array_type);
    return (PyObject *)array_type;
}


static PyMethodDef FMatrix4x4_PyMethodDef[] = {

        {"inverse", (PyCFunction)FMatrix4x4_inverse, METH_NOARGS, 0},


        {"rotate", (PyCFunction)FMatrix4x4_rotate, METH_FASTCALL, 0},
        {"scale", (PyCFunction)FMatrix4x4_scale, METH_FASTCALL, 0},
        {"translate", (PyCFunction)FMatrix4x4_translate, METH_FASTCALL, 0},
        {"perspective", (PyCFunction)FMatrix4x4_perspective, METH_CLASS | METH_FASTCALL, 0},
        {"orthographic", (PyCFunction)FMatrix4x4_orthographic, METH_CLASS | METH_FASTCALL, 0},
        {"look_at", (PyCFunction)FMatrix4x4_look_at, METH_CLASS | METH_FASTCALL, 0},
        {"to_matrix3", (PyCFunction)FMatrix4x4_to_matrix3, METH_NOARGS, 0},


        {"to_quaternion", (PyCFunction)FMatrix4x4_to_quaternion, METH_NOARGS, 0},



        {"to_dmatrix", (PyCFunction)FMatrix4x4_to_dmatrix, METH_NOARGS, 0},

    {"get_row", (PyCFunction)FMatrix4x4_get_row, METH_FASTCALL, 0},
    {"transpose", (PyCFunction)FMatrix4x4_transpose, METH_NOARGS, 0},
    {"get_limits", (PyCFunction)FMatrix4x4_get_limits, METH_NOARGS | METH_STATIC, 0},
    {"get_size", (PyCFunction)FMatrix4x4_get_size, METH_NOARGS | METH_STATIC, 0},
    {"get_array_type", (PyCFunction)FMatrix4x4_get_array_type, METH_NOARGS | METH_STATIC, 0},
    {"from_buffer", (PyCFunction)FMatrix4x4_from_buffer, METH_O | METH_CLASS, 0},
    {0, 0, 0, 0}
};


static PyType_Slot FMatrix4x4_PyType_Slots [] = {
    {Py_tp_new, (void*)FMatrix4x4__new__},
    {Py_tp_dealloc, (void*)FMatrix4x4__dealloc__},
    {Py_tp_hash, (void*)FMatrix4x4__hash__},
    {Py_tp_repr, (void*)FMatrix4x4__repr__},
    {Py_sq_length, (void*)FMatrix4x4__len__},
    {Py_sq_item, (void*)FMatrix4x4__getitem__},
    {Py_tp_richcompare, (void*)FMatrix4x4__richcmp__},
    {Py_nb_add, (void*)FMatrix4x4__add__},
    {Py_nb_subtract, (void*)FMatrix4x4__sub__},
    {Py_nb_multiply, (void*)FMatrix4x4__mul__},
    {Py_nb_matrix_multiply, (void*)FMatrix4x4__matmul__},
    {Py_nb_true_divide, (void*)FMatrix4x4__truediv__},
    {Py_nb_negative, (void*)FMatrix4x4__neg__},
    {Py_bf_getbuffer, (void*)FMatrix4x4_getbufferproc},
    {Py_tp_getset, (void*)FMatrix4x4_PyGetSetDef},
    {Py_tp_members, (void*)FMatrix4x4_PyMemberDef},
    {Py_tp_methods, (void*)FMatrix4x4_PyMethodDef},
    {0, 0},
};


static PyType_Spec FMatrix4x4_PyTypeSpec = {
    "gamut.math.FMatrix4x4",
    sizeof(FMatrix4x4),
    0,
    Py_TPFLAGS_DEFAULT,
    FMatrix4x4_PyType_Slots
};


static PyTypeObject *
define_FMatrix4x4_type(PyObject *module)
{
    PyTypeObject *type = (PyTypeObject *)PyType_FromModuleAndSpec(
        module,
        &FMatrix4x4_PyTypeSpec,
        0
    );
    if (!type){ return 0; }
    // Note:
    // Unlike other functions that steal references, PyModule_AddObject() only
    // decrements the reference count of value on success.
    if (PyModule_AddObject(module, "FMatrix4x4", (PyObject *)type) < 0)
    {
        Py_DECREF(type);
        return 0;
    }
    return type;
}



static PyObject *
FMatrix4x4Array__new__(PyTypeObject *cls, PyObject *args, PyObject *kwds)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto element_cls = module_state->FMatrix4x4_PyTypeObject;

    if (kwds && PyDict_Size(kwds) != 0)
    {
        PyErr_SetString(
            PyExc_TypeError,
            "FMatrix4x4 does accept any keyword arguments"
        );
        return 0;
    }

    auto arg_count = PyTuple_GET_SIZE(args);
    if (arg_count == 0)
    {
        auto self = (FMatrix4x4Array *)cls->tp_alloc(cls, 0);
        if (!self){ return 0; }
        self->length = 0;
        self->glm = 0;
        return (PyObject *)self;
    }

    auto *self = (FMatrix4x4Array *)cls->tp_alloc(cls, 0);
    if (!self){ return 0; }
    self->length = arg_count;
    self->glm = new FMatrix4x4Glm[arg_count];

    for (int i = 0; i < arg_count; i++)
    {
        auto arg = PyTuple_GET_ITEM(args, i);
        if (Py_TYPE(arg) == element_cls)
        {
            self->glm[i] = *(((FMatrix4x4*)arg)->glm);
        }
        else
        {
            Py_DECREF(self);
            PyErr_Format(
                PyExc_TypeError,
                "invalid type %R, expected %R",
                arg,
                element_cls
            );
            return 0;
        }
    }

    return (PyObject *)self;
}


static void
FMatrix4x4Array__dealloc__(FMatrix4x4Array *self)
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


static Py_hash_t
FMatrix4x4Array__hash__(FMatrix4x4Array *self)
{
    Py_ssize_t len = self->length * 16;
    Py_uhash_t acc = _HASH_XXPRIME_5;
    for (Py_ssize_t i = 0; i < (Py_ssize_t)self->length; i++)
    {
        for (FMatrix4x4Glm::length_type c = 0; c < 4; c++)
        {
            for (FMatrix4x4Glm::length_type r = 0; r < 4; r++)
            {
                Py_uhash_t lane = std::hash<float>{}(self->glm[i][r][c]);
                acc += lane * _HASH_XXPRIME_2;
                acc = _HASH_XXROTATE(acc);
                acc *= _HASH_XXPRIME_1;
            }
            acc += len ^ (_HASH_XXPRIME_5 ^ 3527539UL);
        }
    }

    if (acc == (Py_uhash_t)-1) {
        return 1546275796;
    }
    return acc;
}


static PyObject *
FMatrix4x4Array__repr__(FMatrix4x4Array *self)
{
    return PyUnicode_FromFormat("FMatrix4x4Array[%zu]", self->length);
}


static Py_ssize_t
FMatrix4x4Array__len__(FMatrix4x4Array *self)
{
    return self->length;
}


static PyObject *
FMatrix4x4Array__sq_getitem__(FMatrix4x4Array *self, Py_ssize_t index)
{
    if (index < 0 || index > (Py_ssize_t)self->length - 1)
    {
        PyErr_Format(PyExc_IndexError, "index out of range");
        return 0;
    }

    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto element_cls = module_state->FMatrix4x4_PyTypeObject;

    FMatrix4x4 *result = (FMatrix4x4 *)element_cls->tp_alloc(element_cls, 0);
    if (!result){ return 0; }
    result->glm = new FMatrix4x4Glm(self->glm[index]);

    return (PyObject *)result;
}


static PyObject *
FMatrix4x4Array__mp_getitem__(FMatrix4x4Array *self, PyObject *key)
{
    if (PySlice_Check(key))
    {
        Py_ssize_t start;
        Py_ssize_t stop;
        Py_ssize_t step;
        Py_ssize_t length;
        if (PySlice_GetIndicesEx(key, self->length, &start, &stop, &step, &length) != 0)
        {
            return 0;
        }
        auto cls = Py_TYPE(self);
        auto *result = (FMatrix4x4Array *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        if (length == 0)
        {
            result->length = 0;
            result->glm = 0;
        }
        else
        {
            result->length = length;
            result->glm = new FMatrix4x4Glm[length];
            for (FMatrix4x4Glm::length_type i = 0; i < length; i++)
            {
                result->glm[i] = self->glm[start + (i * step)];
            }
        }
        return (PyObject *)result;
    }
    else if (PyLong_Check(key))
    {
        auto index = PyLong_AsSsize_t(key);
        if (PyErr_Occurred()){ return 0; }
        if (index < 0)
        {
            index = (Py_ssize_t)self->length + index;
        }
        if (index < 0 || index > (Py_ssize_t)self->length - 1)
        {
            PyErr_Format(PyExc_IndexError, "index out of range");
            return 0;
        }
        auto module_state = get_module_state();
        if (!module_state){ return 0; }
        auto element_cls = module_state->FMatrix4x4_PyTypeObject;

        FMatrix4x4 *result = (FMatrix4x4 *)element_cls->tp_alloc(element_cls, 0);
        if (!result){ return 0; }
        result->glm = new FMatrix4x4Glm(self->glm[index]);

        return (PyObject *)result;
    }
    PyErr_Format(PyExc_TypeError, "expected int or slice");
    return 0;
}


static PyObject *
FMatrix4x4Array__richcmp__(
    FMatrix4x4Array *self,
    FMatrix4x4Array *other,
    int op
)
{
    if (Py_TYPE(self) != Py_TYPE(other))
    {
        Py_RETURN_NOTIMPLEMENTED;
    }

    switch(op)
    {
        case Py_EQ:
        {
            if (self->length == other->length)
            {
                for (size_t i = 0; i < self->length; i++)
                {
                    if (self->glm[i] != other->glm[i])
                    {
                        Py_RETURN_FALSE;
                    }
                }
                Py_RETURN_TRUE;
            }
            else
            {
                Py_RETURN_FALSE;
            }
        }
        case Py_NE:
        {
            if (self->length != other->length)
            {
                Py_RETURN_TRUE;
            }
            else
            {
                for (size_t i = 0; i < self->length; i++)
                {
                    if (self->glm[i] != other->glm[i])
                    {
                        Py_RETURN_TRUE;
                    }
                }
                Py_RETURN_FALSE;
            }
        }
    }
    Py_RETURN_NOTIMPLEMENTED;
}


static int
FMatrix4x4Array__bool__(FMatrix4x4Array *self)
{
    return self->length ? 1 : 0;
}


static int
FMatrix4x4Array_getbufferproc(FMatrix4x4Array *self, Py_buffer *view, int flags)
{
    if (flags & PyBUF_WRITABLE)
    {
        PyErr_SetString(PyExc_TypeError, "FMatrix4x4 is read only");
        view->obj = 0;
        return -1;
    }
    if ((!(flags & PyBUF_C_CONTIGUOUS)) && flags & PyBUF_F_CONTIGUOUS)
    {
        PyErr_SetString(PyExc_BufferError, "FMatrix4x4 cannot be made Fortran contiguous");
        view->obj = 0;
        return -1;
    }
    view->buf = self->glm;
    view->obj = (PyObject *)self;
    view->len = sizeof(float) * 16 * self->length;
    view->readonly = 1;
    view->itemsize = sizeof(float);
    view->ndim = 3;
    if (flags & PyBUF_FORMAT)
    {
        view->format = "f";
    }
    else
    {
        view->format = 0;
    }
    if (flags & PyBUF_ND)
    {
        view->shape = new Py_ssize_t[3] {
            (Py_ssize_t)self->length,
            4,
            4
        };
    }
    else
    {
        view->shape = 0;
    }
    if (flags & PyBUF_STRIDES)
    {
        static Py_ssize_t strides[] = {
            sizeof(float) * 16,
            sizeof(float) * 4,
            sizeof(float)
        };
        view->strides = &strides[0];
    }
    else
    {
        view->strides = 0;
    }
    view->suboffsets = 0;
    view->internal = 0;
    Py_INCREF(self);
    return 0;
}


static void
FMatrix4x4Array_releasebufferproc(FMatrix4x4Array *self, Py_buffer *view)
{
    delete view->shape;
}


static PyMemberDef FMatrix4x4Array_PyMemberDef[] = {
    {"__weaklistoffset__", T_PYSSIZET, offsetof(FMatrix4x4Array, weakreflist), READONLY},
    {0}
};


static PyObject *
FMatrix4x4Array_pointer(FMatrix4x4Array *self, void *)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto c_p = module_state->ctypes_c_float_p;
    return PyObject_CallMethod(c_p, "from_address", "n", (Py_ssize_t)&self->glm);
}


static PyObject *
FMatrix4x4Array_size(FMatrix4x4Array *self, void *)
{
    return PyLong_FromSize_t(sizeof(float) * 16 * self->length);
}


static PyGetSetDef FMatrix4x4Array_PyGetSetDef[] = {
    {"pointer", (getter)FMatrix4x4Array_pointer, 0, 0, 0},
    {"size", (getter)FMatrix4x4Array_size, 0, 0, 0},
    {0, 0, 0, 0, 0}
};


static PyObject *
FMatrix4x4Array_from_buffer(PyTypeObject *cls, PyObject *buffer)
{
    static Py_ssize_t expected_size = sizeof(float);
    Py_buffer view;
    if (PyObject_GetBuffer(buffer, &view, PyBUF_SIMPLE) == -1){ return 0; }
    auto view_length = view.len;
    if (view_length % (sizeof(float) * 16))
    {
        PyBuffer_Release(&view);
        PyErr_Format(PyExc_BufferError, "expected buffer evenly divisible by %zd, got %zd", sizeof(float), view_length);
        return 0;
    }
    auto array_length = view_length / (sizeof(float) * 16);

    auto *result = (FMatrix4x4Array *)cls->tp_alloc(cls, 0);
    if (!result)
    {
        PyBuffer_Release(&view);
        return 0;
    }
    result->length = array_length;
    if (array_length > 0)
    {
        result->glm = new FMatrix4x4Glm[array_length];
        std::memcpy(result->glm, view.buf, view_length);
    }
    else
    {
        result->glm = 0;
    }
    PyBuffer_Release(&view);
    return (PyObject *)result;
}


static PyObject *
FMatrix4x4Array_get_component_type(PyTypeObject *cls, PyObject *const *args, Py_ssize_t nargs)
{
    if (nargs != 0)
    {
        PyErr_Format(PyExc_TypeError, "expected 0 arguments, got %zi", nargs);
        return 0;
    }
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto component_type = module_state->FMatrix4x4_PyTypeObject;
    Py_INCREF(component_type);
    return (PyObject *)component_type;
}


static PyMethodDef FMatrix4x4Array_PyMethodDef[] = {
    {"from_buffer", (PyCFunction)FMatrix4x4Array_from_buffer, METH_O | METH_CLASS, 0},
    {"get_component_type", (PyCFunction)FMatrix4x4Array_get_component_type, METH_FASTCALL | METH_CLASS, 0},
    {0, 0, 0, 0}
};


static PyType_Slot FMatrix4x4Array_PyType_Slots [] = {
    {Py_tp_new, (void*)FMatrix4x4Array__new__},
    {Py_tp_dealloc, (void*)FMatrix4x4Array__dealloc__},
    {Py_tp_hash, (void*)FMatrix4x4Array__hash__},
    {Py_tp_repr, (void*)FMatrix4x4Array__repr__},
    {Py_sq_length, (void*)FMatrix4x4Array__len__},
    {Py_sq_item, (void*)FMatrix4x4Array__sq_getitem__},
    {Py_mp_subscript, (void*)FMatrix4x4Array__mp_getitem__},
    {Py_tp_richcompare, (void*)FMatrix4x4Array__richcmp__},
    {Py_nb_bool, (void*)FMatrix4x4Array__bool__},
    {Py_bf_getbuffer, (void*)FMatrix4x4Array_getbufferproc},
    {Py_bf_releasebuffer, (void*)FMatrix4x4Array_releasebufferproc},
    {Py_tp_getset, (void*)FMatrix4x4Array_PyGetSetDef},
    {Py_tp_members, (void*)FMatrix4x4Array_PyMemberDef},
    {Py_tp_methods, (void*)FMatrix4x4Array_PyMethodDef},
    {0, 0},
};


static PyType_Spec FMatrix4x4Array_PyTypeSpec = {
    "gamut.math.FMatrix4x4Array",
    sizeof(FMatrix4x4Array),
    0,
    Py_TPFLAGS_DEFAULT,
    FMatrix4x4Array_PyType_Slots
};


static PyTypeObject *
define_FMatrix4x4Array_type(PyObject *module)
{
    PyTypeObject *type = (PyTypeObject *)PyType_FromModuleAndSpec(
        module,
        &FMatrix4x4Array_PyTypeSpec,
        0
    );
    if (!type){ return 0; }
    // Note:
    // Unlike other functions that steal references, PyModule_AddObject() only
    // decrements the reference count of value on success.
    if (PyModule_AddObject(module, "FMatrix4x4Array", (PyObject *)type) < 0)
    {
        Py_DECREF(type);
        return 0;
    }
    return type;
}


static PyTypeObject *
get_FMatrix4x4_type()
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    return module_state->FMatrix4x4_PyTypeObject;
}


static PyTypeObject *
get_FMatrix4x4Array_type()
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    return module_state->FMatrix4x4Array_PyTypeObject;
}


static PyObject *
create_FMatrix4x4(const float *value)
{

    auto cls = get_FMatrix4x4_type();
    auto result = (FMatrix4x4 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new FMatrix4x4Glm(*(FMatrix4x4Glm *)value);
    return (PyObject *)result;
}


static PyObject *
create_FMatrix4x4Array(size_t length, const float *value)
{
    auto cls = get_FMatrix4x4Array_type();
    auto result = (FMatrix4x4Array *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->length = length;
    if (length > 0)
    {
        result->glm = new FMatrix4x4Glm[length];
        for (size_t i = 0; i < length; i++)
        {
            result->glm[i] = ((FMatrix4x4Glm *)value)[i];
        }
    }
    else
    {
        result->glm = 0;
    }
    return (PyObject *)result;
}


static float *
get_FMatrix4x4_value_ptr(const PyObject *self)
{
    if (Py_TYPE(self) != get_FMatrix4x4_type())
    {
        PyErr_Format(PyExc_TypeError, "expected FMatrix4x4, got %R", self);
        return 0;
    }
    return (float *)((FMatrix4x4 *)self)->glm;
}


static float *
get_FMatrix4x4Array_value_ptr(const PyObject *self)
{
    if (Py_TYPE(self) != get_FMatrix4x4Array_type())
    {
        PyErr_Format(
            PyExc_TypeError,
            "expected FMatrix4x4Array, got %R",
            self
        );
        return 0;
    }
    return (float *)((FMatrix4x4Array *)self)->glm;
}


static size_t
get_FMatrix4x4Array_length(const PyObject *self)
{
    if (Py_TYPE(self) != get_FMatrix4x4Array_type())
    {
        PyErr_Format(
            PyExc_TypeError,
            "expected FMatrix4x4Array, got %R",
            self
        );
        return 0;
    }
    return ((FMatrix4x4Array *)self)->length;
}

#endif