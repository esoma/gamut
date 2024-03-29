
// generated from codegen/math/templates/_matrix.hpp

#ifndef GAMUT_MATH_DMATRIX3X4_HPP
#define GAMUT_MATH_DMATRIX3X4_HPP

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
DMatrix3x4__new__(PyTypeObject *cls, PyObject *args, PyObject *kwds)
{
    if (kwds && PyDict_Size(kwds) != 0)
    {
        PyErr_SetString(
            PyExc_TypeError,
            "DMatrix3x4 does accept any keyword arguments"
        );
        return 0;
    }

    DMatrix3x4Glm *glm = 0;
    auto arg_count = PyTuple_GET_SIZE(args);
    switch (PyTuple_GET_SIZE(args))
    {
        case 0:
        {
            glm = new DMatrix3x4Glm();
            break;
        }
        case 1:
        {
            auto arg = PyTuple_GET_ITEM(args, 0);
            double arg_c = pyobject_to_c_double(arg);
            auto error_occurred = PyErr_Occurred();
            if (error_occurred){ return 0; }
            glm = new DMatrix3x4Glm(arg_c);
            break;
        }
        case 3:
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

            glm = new DMatrix3x4Glm(

                    *((DVector4 *)p_0)->glm,

                    *((DVector4 *)p_1)->glm,

                    *((DVector4 *)p_2)->glm

            );

            break;
        }
        case 12:
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

            glm = new DMatrix3x4Glm(

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

                    c_11

            );
            break;
        }
        default:
        {
            PyErr_Format(
                PyExc_TypeError,
                "invalid number of arguments supplied to DMatrix3x4, expected "
                "0, 1, 3 or 12 (got %zd)",
                arg_count
            );
            return 0;
        }
    }

    DMatrix3x4 *self = (DMatrix3x4*)cls->tp_alloc(cls, 0);
    if (!self)
    {
        delete glm;
        return 0;
    }
    self->glm = glm;

    return (PyObject *)self;
}


static void
DMatrix3x4__dealloc__(DMatrix3x4 *self)
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
DMatrix3x4__hash__(DMatrix3x4 *self)
{
    Py_ssize_t len = 12;
    Py_uhash_t acc = _HASH_XXPRIME_5;
    for (DMatrix3x4Glm::length_type c = 0; c < 4; c++)
    {
        for (DMatrix3x4Glm::length_type r = 0; r < 3; r++)
        {
            Py_uhash_t lane = std::hash<double>{}((*self->glm)[r][c]);
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
DMatrix3x4__repr__(DMatrix3x4 *self)
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



        PyObject *py_3_0 = 0;

        PyObject *py_3_1 = 0;

        PyObject *py_3_2 = 0;





        py_0_0 = c_double_to_pyobject((*self->glm)[0][0]);
        if (!py_0_0){ goto cleanup; }

        py_0_1 = c_double_to_pyobject((*self->glm)[1][0]);
        if (!py_0_1){ goto cleanup; }

        py_0_2 = c_double_to_pyobject((*self->glm)[2][0]);
        if (!py_0_2){ goto cleanup; }



        py_1_0 = c_double_to_pyobject((*self->glm)[0][1]);
        if (!py_1_0){ goto cleanup; }

        py_1_1 = c_double_to_pyobject((*self->glm)[1][1]);
        if (!py_1_1){ goto cleanup; }

        py_1_2 = c_double_to_pyobject((*self->glm)[2][1]);
        if (!py_1_2){ goto cleanup; }



        py_2_0 = c_double_to_pyobject((*self->glm)[0][2]);
        if (!py_2_0){ goto cleanup; }

        py_2_1 = c_double_to_pyobject((*self->glm)[1][2]);
        if (!py_2_1){ goto cleanup; }

        py_2_2 = c_double_to_pyobject((*self->glm)[2][2]);
        if (!py_2_2){ goto cleanup; }



        py_3_0 = c_double_to_pyobject((*self->glm)[0][3]);
        if (!py_3_0){ goto cleanup; }

        py_3_1 = c_double_to_pyobject((*self->glm)[1][3]);
        if (!py_3_1){ goto cleanup; }

        py_3_2 = c_double_to_pyobject((*self->glm)[2][3]);
        if (!py_3_2){ goto cleanup; }



    result = PyUnicode_FromFormat(
        "DMatrix3x4("

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



        Py_XDECREF(py_3_0);

        Py_XDECREF(py_3_1);

        Py_XDECREF(py_3_2);


    return result;
}


static Py_ssize_t
DMatrix3x4__len__(DMatrix3x4 *self)
{
    return 3;
}


static PyObject *
DMatrix3x4__getitem__(DMatrix3x4 *self, Py_ssize_t index)
{
    if (index < 0 || index > 2)
    {
        PyErr_Format(PyExc_IndexError, "index out of range");
        return 0;
    }
    const auto& v = (*self->glm)[(DMatrix3x4Glm::length_type)index];
    return (PyObject *)create_DVector4_from_glm(v);
}


static PyObject *
DMatrix3x4__richcmp__(DMatrix3x4 *self, DMatrix3x4 *other, int op)
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
DMatrix3x4__add__(PyObject *left, PyObject *right)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->DMatrix3x4_PyTypeObject;

    DMatrix3x4Glm matrix;
    if (Py_TYPE(left) == Py_TYPE(right))
    {
        matrix = (*((DMatrix3x4 *)left)->glm) + (*((DMatrix3x4 *)right)->glm);
    }
    else
    {
        if (Py_TYPE(left) == cls)
        {
            auto c_right = pyobject_to_c_double(right);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
            matrix = (*((DMatrix3x4 *)left)->glm) + c_right;
        }
        else
        {
            auto c_left = pyobject_to_c_double(left);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
            matrix = (*((DMatrix3x4 *)right)->glm) + c_left;
        }
    }

    DMatrix3x4 *result = (DMatrix3x4 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new DMatrix3x4Glm(matrix);

    return (PyObject *)result;
}


static PyObject *
DMatrix3x4__sub__(PyObject *left, PyObject *right)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->DMatrix3x4_PyTypeObject;

    DMatrix3x4Glm matrix;
    if (Py_TYPE(left) == Py_TYPE(right))
    {
        matrix = (*((DMatrix3x4 *)left)->glm) - (*((DMatrix3x4 *)right)->glm);
    }
    else
    {
        if (Py_TYPE(left) == cls)
        {
            auto c_right = pyobject_to_c_double(right);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
            matrix = (*((DMatrix3x4 *)left)->glm) - c_right;
        }
        else
        {
            auto c_left = pyobject_to_c_double(left);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }

                matrix = DMatrix3x4Glm(

                        c_left,

                        c_left,

                        c_left,

                        c_left,

                        c_left,

                        c_left,

                        c_left,

                        c_left,

                        c_left,

                        c_left,

                        c_left,

                        c_left

                ) - (*((DMatrix3x4 *)right)->glm);

        }
    }

    DMatrix3x4 *result = (DMatrix3x4 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new DMatrix3x4Glm(matrix);

    return (PyObject *)result;
}


static PyObject *
DMatrix3x4__mul__(PyObject *left, PyObject *right)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->DMatrix3x4_PyTypeObject;

    DMatrix3x4Glm matrix;
    if (Py_TYPE(left) == cls)
    {
        auto c_right = pyobject_to_c_double(right);
        if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
        matrix = (*((DMatrix3x4 *)left)->glm) * c_right;
    }
    else
    {
        auto c_left = pyobject_to_c_double(left);
        if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
        matrix = c_left * (*((DMatrix3x4 *)right)->glm);
    }

    DMatrix3x4 *result = (DMatrix3x4 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new DMatrix3x4Glm(matrix);

    return (PyObject *)result;
}


static PyObject *
DMatrix3x4__matmul__(PyObject *left, PyObject *right)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->DMatrix3x4_PyTypeObject;

    if (Py_TYPE(left) == cls)
    {



        {
            auto right_cls = module_state->DMatrix2x3_PyTypeObject;
            auto result_cls = module_state->DMatrix2x4_PyTypeObject;
            if (Py_TYPE(right) == right_cls)
            {
                DMatrix2x4 *result = (DMatrix2x4 *)result_cls->tp_alloc(result_cls, 0);
                if (!result){ return 0; }
                result->glm = new DMatrix2x4Glm(
                    (*((DMatrix3x4 *)left)->glm) * (*((DMatrix2x3 *)right)->glm)
                );
                return (PyObject *)result;
            }
        }





        {
            auto right_cls = module_state->DMatrix3x3_PyTypeObject;
            auto result_cls = module_state->DMatrix3x4_PyTypeObject;
            if (Py_TYPE(right) == right_cls)
            {
                DMatrix3x4 *result = (DMatrix3x4 *)result_cls->tp_alloc(result_cls, 0);
                if (!result){ return 0; }
                result->glm = new DMatrix3x4Glm(
                    (*((DMatrix3x4 *)left)->glm) * (*((DMatrix3x3 *)right)->glm)
                );
                return (PyObject *)result;
            }
        }





        {
            auto right_cls = module_state->DMatrix4x3_PyTypeObject;
            auto result_cls = module_state->DMatrix4x4_PyTypeObject;
            if (Py_TYPE(right) == right_cls)
            {
                DMatrix4x4 *result = (DMatrix4x4 *)result_cls->tp_alloc(result_cls, 0);
                if (!result){ return 0; }
                result->glm = new DMatrix4x4Glm(
                    (*((DMatrix3x4 *)left)->glm) * (*((DMatrix4x3 *)right)->glm)
                );
                return (PyObject *)result;
            }
        }






        {
            auto row_cls = module_state->DVector3_PyTypeObject;
            auto column_cls = module_state->DVector4_PyTypeObject;
            if (Py_TYPE(right) == row_cls)
            {
                DVector4 *result = (DVector4 *)column_cls->tp_alloc(column_cls, 0);
                if (!result){ return 0; }
                result->glm = new DVector4Glm(
                    (*((DMatrix3x4 *)left)->glm) * (*((DVector3 *)right)->glm)
                );
                return (PyObject *)result;
            }
        }
    }
    else
    {


        auto row_cls = module_state->DVector3_PyTypeObject;
        auto column_cls = module_state->DVector4_PyTypeObject;
        if (Py_TYPE(left) == column_cls)
        {
            DVector3 *result = (DVector3 *)row_cls->tp_alloc(row_cls, 0);
            if (!result){ return 0; }
            result->glm = new DVector3Glm(
                (*((DVector4 *)left)->glm) * (*((DMatrix3x4 *)right)->glm)
            );
            return (PyObject *)result;
        }
    }

    Py_RETURN_NOTIMPLEMENTED;
}

static PyObject *
DMatrix3x4__truediv__(PyObject *left, PyObject *right)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->DMatrix3x4_PyTypeObject;

    DMatrix3x4Glm matrix;
    if (Py_TYPE(left) == cls)
    {


        auto c_right = pyobject_to_c_double(right);
        if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
        matrix = (*((DMatrix3x4 *)left)->glm) / c_right;
    }
    else
    {


        auto c_left = pyobject_to_c_double(left);
        if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
        matrix = c_left / (*((DMatrix3x4 *)right)->glm);
    }

    DMatrix3x4 *result = (DMatrix3x4 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new DMatrix3x4Glm(matrix);

    return (PyObject *)result;
}


static PyObject *
DMatrix3x4__neg__(DMatrix3x4 *self)
{
    auto cls = Py_TYPE(self);

    DMatrix3x4 *result = (DMatrix3x4 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new DMatrix3x4Glm(-(*self->glm));

    return (PyObject *)result;
}


static int
DMatrix3x4_getbufferproc(DMatrix3x4 *self, Py_buffer *view, int flags)
{
    if (flags & PyBUF_WRITABLE)
    {
        PyErr_SetString(PyExc_TypeError, "DMatrix3x4 is read only");
        view->obj = 0;
        return -1;
    }
    if ((!(flags & PyBUF_C_CONTIGUOUS)) && flags & PyBUF_F_CONTIGUOUS)
    {
        PyErr_SetString(PyExc_BufferError, "DMatrix3x4 cannot be made Fortran contiguous");
        view->obj = 0;
        return -1;
    }
    view->buf = glm::value_ptr(*self->glm);
    view->obj = (PyObject *)self;
    view->len = sizeof(double) * 12;
    view->readonly = 1;
    view->itemsize = sizeof(double);
    view->ndim = 2;
    if (flags & PyBUF_FORMAT)
    {
        view->format = "d";
    }
    else
    {
        view->format = 0;
    }
    if (flags & PyBUF_ND)
    {
        static Py_ssize_t shape[] = { 3, 4 };
        view->shape = &shape[0];
    }
    else
    {
        view->shape = 0;
    }
    if (flags & PyBUF_STRIDES)
    {
        static Py_ssize_t strides[] = {
            sizeof(double) * 4,
            sizeof(double)
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


static PyMemberDef DMatrix3x4_PyMemberDef[] = {
    {"__weaklistoffset__", T_PYSSIZET, offsetof(DMatrix3x4, weakreflist), READONLY},
    {0}
};


static PyObject *
DMatrix3x4_pointer(DMatrix3x4 *self, void *)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto c_p = module_state->ctypes_c_double_p;
    return PyObject_CallMethod(c_p, "from_address", "n", (Py_ssize_t)&self->glm);
}


static PyGetSetDef DMatrix3x4_PyGetSetDef[] = {
    {"pointer", (getter)DMatrix3x4_pointer, 0, 0, 0},
    {0, 0, 0, 0, 0}
};











static DVector3 *
DMatrix3x4_get_row(DMatrix3x4 *self, PyObject *const *args, Py_ssize_t nargs)
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
    auto row_cls = module_state->DVector3_PyTypeObject;

    auto *result = (DVector3 *)row_cls->tp_alloc(row_cls, 0);
    if (!result){ return 0; }
    auto row = glm::row(*self->glm, index);
    result->glm = new DVector3Glm(row);
    return result;
}



static DMatrix4x3 *
DMatrix3x4_transpose(DMatrix3x4 *self, void*)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->DMatrix4x3_PyTypeObject;

    DMatrix4x3Glm matrix = glm::transpose(*self->glm);
    DMatrix4x3 *result = (DMatrix4x3 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new DMatrix4x3Glm(matrix);
    return result;
}



static PyObject *
DMatrix3x4_get_size(DMatrix3x4 *cls, void *)
{
    return PyLong_FromSize_t(sizeof(double) * 12);
}


static PyObject *
DMatrix3x4_get_limits(DMatrix3x4 *self, void *)
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


static PyObject *
DMatrix3x4_from_buffer(PyTypeObject *cls, PyObject *buffer)
{
    static Py_ssize_t expected_size = sizeof(double) * 12;
    Py_buffer view;
    if (PyObject_GetBuffer(buffer, &view, PyBUF_SIMPLE) == -1){ return 0; }
    auto view_length = view.len;
    if (view_length < expected_size)
    {
        PyBuffer_Release(&view);
        PyErr_Format(PyExc_BufferError, "expected buffer of size %zd, got %zd", expected_size, view_length);
        return 0;
    }

    auto *result = (DMatrix3x4 *)cls->tp_alloc(cls, 0);
    if (!result)
    {
        PyBuffer_Release(&view);
        return 0;
    }
    result->glm = new DMatrix3x4Glm();
    std::memcpy(result->glm, view.buf, expected_size);
    PyBuffer_Release(&view);
    return (PyObject *)result;
}



    static FMatrix3x4 *
    DMatrix3x4_to_fmatrix(DMatrix3x4 *self, void*)
    {
        auto module_state = get_module_state();
        if (!module_state){ return 0; }
        auto cls = module_state->FMatrix3x4_PyTypeObject;

        auto *result = (FMatrix3x4 *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new FMatrix3x4Glm(*self->glm);
        return result;
    }






static PyObject *
DMatrix3x4_get_array_type(PyTypeObject *cls, void*)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto array_type = module_state->DMatrix3x4Array_PyTypeObject;
    Py_INCREF(array_type);
    return (PyObject *)array_type;
}


static PyMethodDef DMatrix3x4_PyMethodDef[] = {




        {"to_fmatrix", (PyCFunction)DMatrix3x4_to_fmatrix, METH_NOARGS, 0},


    {"get_row", (PyCFunction)DMatrix3x4_get_row, METH_FASTCALL, 0},
    {"transpose", (PyCFunction)DMatrix3x4_transpose, METH_NOARGS, 0},
    {"get_limits", (PyCFunction)DMatrix3x4_get_limits, METH_NOARGS | METH_STATIC, 0},
    {"get_size", (PyCFunction)DMatrix3x4_get_size, METH_NOARGS | METH_STATIC, 0},
    {"get_array_type", (PyCFunction)DMatrix3x4_get_array_type, METH_NOARGS | METH_STATIC, 0},
    {"from_buffer", (PyCFunction)DMatrix3x4_from_buffer, METH_O | METH_CLASS, 0},
    {0, 0, 0, 0}
};


static PyType_Slot DMatrix3x4_PyType_Slots [] = {
    {Py_tp_new, (void*)DMatrix3x4__new__},
    {Py_tp_dealloc, (void*)DMatrix3x4__dealloc__},
    {Py_tp_hash, (void*)DMatrix3x4__hash__},
    {Py_tp_repr, (void*)DMatrix3x4__repr__},
    {Py_sq_length, (void*)DMatrix3x4__len__},
    {Py_sq_item, (void*)DMatrix3x4__getitem__},
    {Py_tp_richcompare, (void*)DMatrix3x4__richcmp__},
    {Py_nb_add, (void*)DMatrix3x4__add__},
    {Py_nb_subtract, (void*)DMatrix3x4__sub__},
    {Py_nb_multiply, (void*)DMatrix3x4__mul__},
    {Py_nb_matrix_multiply, (void*)DMatrix3x4__matmul__},
    {Py_nb_true_divide, (void*)DMatrix3x4__truediv__},
    {Py_nb_negative, (void*)DMatrix3x4__neg__},
    {Py_bf_getbuffer, (void*)DMatrix3x4_getbufferproc},
    {Py_tp_getset, (void*)DMatrix3x4_PyGetSetDef},
    {Py_tp_members, (void*)DMatrix3x4_PyMemberDef},
    {Py_tp_methods, (void*)DMatrix3x4_PyMethodDef},
    {0, 0},
};


static PyType_Spec DMatrix3x4_PyTypeSpec = {
    "gamut.math.DMatrix3x4",
    sizeof(DMatrix3x4),
    0,
    Py_TPFLAGS_DEFAULT,
    DMatrix3x4_PyType_Slots
};


static PyTypeObject *
define_DMatrix3x4_type(PyObject *module)
{
    PyTypeObject *type = (PyTypeObject *)PyType_FromModuleAndSpec(
        module,
        &DMatrix3x4_PyTypeSpec,
        0
    );
    if (!type){ return 0; }
    // Note:
    // Unlike other functions that steal references, PyModule_AddObject() only
    // decrements the reference count of value on success.
    if (PyModule_AddObject(module, "DMatrix3x4", (PyObject *)type) < 0)
    {
        Py_DECREF(type);
        return 0;
    }
    return type;
}



static PyObject *
DMatrix3x4Array__new__(PyTypeObject *cls, PyObject *args, PyObject *kwds)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto element_cls = module_state->DMatrix3x4_PyTypeObject;

    if (kwds && PyDict_Size(kwds) != 0)
    {
        PyErr_SetString(
            PyExc_TypeError,
            "DMatrix3x4 does accept any keyword arguments"
        );
        return 0;
    }

    auto arg_count = PyTuple_GET_SIZE(args);
    if (arg_count == 0)
    {
        auto self = (DMatrix3x4Array *)cls->tp_alloc(cls, 0);
        if (!self){ return 0; }
        self->length = 0;
        self->glm = 0;
        return (PyObject *)self;
    }

    auto *self = (DMatrix3x4Array *)cls->tp_alloc(cls, 0);
    if (!self){ return 0; }
    self->length = arg_count;
    self->glm = new DMatrix3x4Glm[arg_count];

    for (int i = 0; i < arg_count; i++)
    {
        auto arg = PyTuple_GET_ITEM(args, i);
        if (Py_TYPE(arg) == element_cls)
        {
            self->glm[i] = *(((DMatrix3x4*)arg)->glm);
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
DMatrix3x4Array__dealloc__(DMatrix3x4Array *self)
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
DMatrix3x4Array__hash__(DMatrix3x4Array *self)
{
    Py_ssize_t len = self->length * 12;
    Py_uhash_t acc = _HASH_XXPRIME_5;
    for (Py_ssize_t i = 0; i < (Py_ssize_t)self->length; i++)
    {
        for (DMatrix3x4Glm::length_type c = 0; c < 4; c++)
        {
            for (DMatrix3x4Glm::length_type r = 0; r < 3; r++)
            {
                Py_uhash_t lane = std::hash<double>{}(self->glm[i][r][c]);
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
DMatrix3x4Array__repr__(DMatrix3x4Array *self)
{
    return PyUnicode_FromFormat("DMatrix3x4Array[%zu]", self->length);
}


static Py_ssize_t
DMatrix3x4Array__len__(DMatrix3x4Array *self)
{
    return self->length;
}


static PyObject *
DMatrix3x4Array__sq_getitem__(DMatrix3x4Array *self, Py_ssize_t index)
{
    if (index < 0 || index > (Py_ssize_t)self->length - 1)
    {
        PyErr_Format(PyExc_IndexError, "index out of range");
        return 0;
    }

    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto element_cls = module_state->DMatrix3x4_PyTypeObject;

    DMatrix3x4 *result = (DMatrix3x4 *)element_cls->tp_alloc(element_cls, 0);
    if (!result){ return 0; }
    result->glm = new DMatrix3x4Glm(self->glm[index]);

    return (PyObject *)result;
}


static PyObject *
DMatrix3x4Array__mp_getitem__(DMatrix3x4Array *self, PyObject *key)
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
        auto *result = (DMatrix3x4Array *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        if (length == 0)
        {
            result->length = 0;
            result->glm = 0;
        }
        else
        {
            result->length = length;
            result->glm = new DMatrix3x4Glm[length];
            for (DMatrix3x4Glm::length_type i = 0; i < length; i++)
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
        auto element_cls = module_state->DMatrix3x4_PyTypeObject;

        DMatrix3x4 *result = (DMatrix3x4 *)element_cls->tp_alloc(element_cls, 0);
        if (!result){ return 0; }
        result->glm = new DMatrix3x4Glm(self->glm[index]);

        return (PyObject *)result;
    }
    PyErr_Format(PyExc_TypeError, "expected int or slice");
    return 0;
}


static PyObject *
DMatrix3x4Array__richcmp__(
    DMatrix3x4Array *self,
    DMatrix3x4Array *other,
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
DMatrix3x4Array__bool__(DMatrix3x4Array *self)
{
    return self->length ? 1 : 0;
}


static int
DMatrix3x4Array_getbufferproc(DMatrix3x4Array *self, Py_buffer *view, int flags)
{
    if (flags & PyBUF_WRITABLE)
    {
        PyErr_SetString(PyExc_TypeError, "DMatrix3x4 is read only");
        view->obj = 0;
        return -1;
    }
    if ((!(flags & PyBUF_C_CONTIGUOUS)) && flags & PyBUF_F_CONTIGUOUS)
    {
        PyErr_SetString(PyExc_BufferError, "DMatrix3x4 cannot be made Fortran contiguous");
        view->obj = 0;
        return -1;
    }
    view->buf = self->glm;
    view->obj = (PyObject *)self;
    view->len = sizeof(double) * 12 * self->length;
    view->readonly = 1;
    view->itemsize = sizeof(double);
    view->ndim = 3;
    if (flags & PyBUF_FORMAT)
    {
        view->format = "d";
    }
    else
    {
        view->format = 0;
    }
    if (flags & PyBUF_ND)
    {
        view->shape = new Py_ssize_t[3] {
            (Py_ssize_t)self->length,
            3,
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
            sizeof(double) * 12,
            sizeof(double) * 4,
            sizeof(double)
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
DMatrix3x4Array_releasebufferproc(DMatrix3x4Array *self, Py_buffer *view)
{
    delete view->shape;
}


static PyMemberDef DMatrix3x4Array_PyMemberDef[] = {
    {"__weaklistoffset__", T_PYSSIZET, offsetof(DMatrix3x4Array, weakreflist), READONLY},
    {0}
};


static PyObject *
DMatrix3x4Array_pointer(DMatrix3x4Array *self, void *)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto c_p = module_state->ctypes_c_double_p;
    return PyObject_CallMethod(c_p, "from_address", "n", (Py_ssize_t)&self->glm);
}


static PyObject *
DMatrix3x4Array_size(DMatrix3x4Array *self, void *)
{
    return PyLong_FromSize_t(sizeof(double) * 12 * self->length);
}


static PyGetSetDef DMatrix3x4Array_PyGetSetDef[] = {
    {"pointer", (getter)DMatrix3x4Array_pointer, 0, 0, 0},
    {"size", (getter)DMatrix3x4Array_size, 0, 0, 0},
    {0, 0, 0, 0, 0}
};


static PyObject *
DMatrix3x4Array_from_buffer(PyTypeObject *cls, PyObject *buffer)
{
    static Py_ssize_t expected_size = sizeof(double);
    Py_buffer view;
    if (PyObject_GetBuffer(buffer, &view, PyBUF_SIMPLE) == -1){ return 0; }
    auto view_length = view.len;
    if (view_length % (sizeof(double) * 12))
    {
        PyBuffer_Release(&view);
        PyErr_Format(PyExc_BufferError, "expected buffer evenly divisible by %zd, got %zd", sizeof(double), view_length);
        return 0;
    }
    auto array_length = view_length / (sizeof(double) * 12);

    auto *result = (DMatrix3x4Array *)cls->tp_alloc(cls, 0);
    if (!result)
    {
        PyBuffer_Release(&view);
        return 0;
    }
    result->length = array_length;
    if (array_length > 0)
    {
        result->glm = new DMatrix3x4Glm[array_length];
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
DMatrix3x4Array_get_component_type(PyTypeObject *cls, PyObject *const *args, Py_ssize_t nargs)
{
    if (nargs != 0)
    {
        PyErr_Format(PyExc_TypeError, "expected 0 arguments, got %zi", nargs);
        return 0;
    }
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto component_type = module_state->DMatrix3x4_PyTypeObject;
    Py_INCREF(component_type);
    return (PyObject *)component_type;
}


static PyMethodDef DMatrix3x4Array_PyMethodDef[] = {
    {"from_buffer", (PyCFunction)DMatrix3x4Array_from_buffer, METH_O | METH_CLASS, 0},
    {"get_component_type", (PyCFunction)DMatrix3x4Array_get_component_type, METH_FASTCALL | METH_CLASS, 0},
    {0, 0, 0, 0}
};


static PyType_Slot DMatrix3x4Array_PyType_Slots [] = {
    {Py_tp_new, (void*)DMatrix3x4Array__new__},
    {Py_tp_dealloc, (void*)DMatrix3x4Array__dealloc__},
    {Py_tp_hash, (void*)DMatrix3x4Array__hash__},
    {Py_tp_repr, (void*)DMatrix3x4Array__repr__},
    {Py_sq_length, (void*)DMatrix3x4Array__len__},
    {Py_sq_item, (void*)DMatrix3x4Array__sq_getitem__},
    {Py_mp_subscript, (void*)DMatrix3x4Array__mp_getitem__},
    {Py_tp_richcompare, (void*)DMatrix3x4Array__richcmp__},
    {Py_nb_bool, (void*)DMatrix3x4Array__bool__},
    {Py_bf_getbuffer, (void*)DMatrix3x4Array_getbufferproc},
    {Py_bf_releasebuffer, (void*)DMatrix3x4Array_releasebufferproc},
    {Py_tp_getset, (void*)DMatrix3x4Array_PyGetSetDef},
    {Py_tp_members, (void*)DMatrix3x4Array_PyMemberDef},
    {Py_tp_methods, (void*)DMatrix3x4Array_PyMethodDef},
    {0, 0},
};


static PyType_Spec DMatrix3x4Array_PyTypeSpec = {
    "gamut.math.DMatrix3x4Array",
    sizeof(DMatrix3x4Array),
    0,
    Py_TPFLAGS_DEFAULT,
    DMatrix3x4Array_PyType_Slots
};


static PyTypeObject *
define_DMatrix3x4Array_type(PyObject *module)
{
    PyTypeObject *type = (PyTypeObject *)PyType_FromModuleAndSpec(
        module,
        &DMatrix3x4Array_PyTypeSpec,
        0
    );
    if (!type){ return 0; }
    // Note:
    // Unlike other functions that steal references, PyModule_AddObject() only
    // decrements the reference count of value on success.
    if (PyModule_AddObject(module, "DMatrix3x4Array", (PyObject *)type) < 0)
    {
        Py_DECREF(type);
        return 0;
    }
    return type;
}


static PyTypeObject *
get_DMatrix3x4_type()
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    return module_state->DMatrix3x4_PyTypeObject;
}


static PyTypeObject *
get_DMatrix3x4Array_type()
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    return module_state->DMatrix3x4Array_PyTypeObject;
}


static PyObject *
create_DMatrix3x4(const double *value)
{

    auto cls = get_DMatrix3x4_type();
    auto result = (DMatrix3x4 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new DMatrix3x4Glm(*(DMatrix3x4Glm *)value);
    return (PyObject *)result;
}


static PyObject *
create_DMatrix3x4Array(size_t length, const double *value)
{
    auto cls = get_DMatrix3x4Array_type();
    auto result = (DMatrix3x4Array *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->length = length;
    if (length > 0)
    {
        result->glm = new DMatrix3x4Glm[length];
        for (size_t i = 0; i < length; i++)
        {
            result->glm[i] = ((DMatrix3x4Glm *)value)[i];
        }
    }
    else
    {
        result->glm = 0;
    }
    return (PyObject *)result;
}


static double *
get_DMatrix3x4_value_ptr(const PyObject *self)
{
    if (Py_TYPE(self) != get_DMatrix3x4_type())
    {
        PyErr_Format(PyExc_TypeError, "expected DMatrix3x4, got %R", self);
        return 0;
    }
    return (double *)((DMatrix3x4 *)self)->glm;
}


static double *
get_DMatrix3x4Array_value_ptr(const PyObject *self)
{
    if (Py_TYPE(self) != get_DMatrix3x4Array_type())
    {
        PyErr_Format(
            PyExc_TypeError,
            "expected DMatrix3x4Array, got %R",
            self
        );
        return 0;
    }
    return (double *)((DMatrix3x4Array *)self)->glm;
}


static size_t
get_DMatrix3x4Array_length(const PyObject *self)
{
    if (Py_TYPE(self) != get_DMatrix3x4Array_type())
    {
        PyErr_Format(
            PyExc_TypeError,
            "expected DMatrix3x4Array, got %R",
            self
        );
        return 0;
    }
    return ((DMatrix3x4Array *)self)->length;
}

#endif