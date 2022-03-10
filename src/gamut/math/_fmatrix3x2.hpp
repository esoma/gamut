
// generated 2022-03-10 18:59:39.072560 from codegen/math/templates/_matrix.hpp

#ifndef GAMUT_MATH_FMATRIX3X2_HPP
#define GAMUT_MATH_FMATRIX3X2_HPP

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
#include "_fvector2.hpp"


static PyObject *
FMatrix3x2__new__(PyTypeObject *cls, PyObject *args, PyObject *kwds)
{
    if (kwds && PyDict_Size(kwds) != 0)
    {
        PyErr_SetString(
            PyExc_TypeError,
            "FMatrix3x2 does accept any keyword arguments"
        );
        return 0;
    }

    FMatrix3x2Glm *glm = 0;
    auto arg_count = PyTuple_GET_SIZE(args);
    switch (PyTuple_GET_SIZE(args))
    {
        case 0:
        {
            glm = new FMatrix3x2Glm();
            break;
        }
        case 1:
        {
            auto arg = PyTuple_GET_ITEM(args, 0);
            float arg_c = pyobject_to_c_float(arg);
            auto error_occurred = PyErr_Occurred();
            if (error_occurred){ return 0; }
            glm = new FMatrix3x2Glm(arg_c);
            break;
        }
        case 3:
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

            glm = new FMatrix3x2Glm(

                    *((FVector2 *)p_0)->glm,

                    *((FVector2 *)p_1)->glm,

                    *((FVector2 *)p_2)->glm

            );

            break;
        }
        case 6:
        {

                float c_0 = 0;

                float c_1 = 0;

                float c_2 = 0;

                float c_3 = 0;

                float c_4 = 0;

                float c_5 = 0;


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

            glm = new FMatrix3x2Glm(

                    c_0,

                    c_1,

                    c_2,

                    c_3,

                    c_4,

                    c_5

            );
            break;
        }
        default:
        {
            PyErr_Format(
                PyExc_TypeError,
                "invalid number of arguments supplied to FMatrix3x2, expected "
                "0, 1, 3 or 6 (got %zd)",
                arg_count
            );
            return 0;
        }
    }

    FMatrix3x2 *self = (FMatrix3x2*)cls->tp_alloc(cls, 0);
    if (!self)
    {
        delete glm;
        return 0;
    }
    self->glm = glm;

    return (PyObject *)self;
}


static void
FMatrix3x2__dealloc__(FMatrix3x2 *self)
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
FMatrix3x2__hash__(FMatrix3x2 *self)
{
    Py_ssize_t len = 6;
    Py_uhash_t acc = _HASH_XXPRIME_5;
    for (FMatrix3x2Glm::length_type c = 0; c < 2; c++)
    {
        for (FMatrix3x2Glm::length_type r = 0; r < 3; r++)
        {
            Py_uhash_t lane = std::hash<float>{}((*self->glm)[r][c]);
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
FMatrix3x2__repr__(FMatrix3x2 *self)
{
    PyObject *result = 0;


        PyObject *py_0_0 = 0;

        PyObject *py_0_1 = 0;

        PyObject *py_0_2 = 0;



        PyObject *py_1_0 = 0;

        PyObject *py_1_1 = 0;

        PyObject *py_1_2 = 0;





        py_0_0 = c_float_to_pyobject((*self->glm)[0][0]);
        if (!py_0_0){ goto cleanup; }

        py_0_1 = c_float_to_pyobject((*self->glm)[1][0]);
        if (!py_0_1){ goto cleanup; }

        py_0_2 = c_float_to_pyobject((*self->glm)[2][0]);
        if (!py_0_2){ goto cleanup; }



        py_1_0 = c_float_to_pyobject((*self->glm)[0][1]);
        if (!py_1_0){ goto cleanup; }

        py_1_1 = c_float_to_pyobject((*self->glm)[1][1]);
        if (!py_1_1){ goto cleanup; }

        py_1_2 = c_float_to_pyobject((*self->glm)[2][1]);
        if (!py_1_2){ goto cleanup; }



    result = PyUnicode_FromFormat(
        "FMatrix3x2("

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

            py_1_0
            ,



            py_0_1
            ,

            py_1_1
            ,



            py_0_2
            ,

            py_1_2



    );
cleanup:


        Py_XDECREF(py_0_0);

        Py_XDECREF(py_0_1);

        Py_XDECREF(py_0_2);



        Py_XDECREF(py_1_0);

        Py_XDECREF(py_1_1);

        Py_XDECREF(py_1_2);


    return result;
}


static Py_ssize_t
FMatrix3x2__len__(FMatrix3x2 *self)
{
    return 3;
}


static PyObject *
FMatrix3x2__getitem__(FMatrix3x2 *self, Py_ssize_t index)
{
    if (index < 0 || index > 2)
    {
        PyErr_Format(PyExc_IndexError, "index out of range");
        return 0;
    }
    const auto& v = (*self->glm)[(FMatrix3x2Glm::length_type)index];
    return (PyObject *)create_FVector2_from_glm(v);
}


static PyObject *
FMatrix3x2__richcmp__(FMatrix3x2 *self, FMatrix3x2 *other, int op)
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
FMatrix3x2__add__(PyObject *left, PyObject *right)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->FMatrix3x2_PyTypeObject;

    FMatrix3x2Glm matrix;
    if (Py_TYPE(left) == Py_TYPE(right))
    {
        matrix = (*((FMatrix3x2 *)left)->glm) + (*((FMatrix3x2 *)right)->glm);
    }
    else
    {
        if (Py_TYPE(left) == cls)
        {
            auto c_right = pyobject_to_c_float(right);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
            matrix = (*((FMatrix3x2 *)left)->glm) + c_right;
        }
        else
        {
            auto c_left = pyobject_to_c_float(left);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
            matrix = (*((FMatrix3x2 *)right)->glm) + c_left;
        }
    }

    FMatrix3x2 *result = (FMatrix3x2 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new FMatrix3x2Glm(matrix);

    return (PyObject *)result;
}


static PyObject *
FMatrix3x2__sub__(PyObject *left, PyObject *right)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->FMatrix3x2_PyTypeObject;

    FMatrix3x2Glm matrix;
    if (Py_TYPE(left) == Py_TYPE(right))
    {
        matrix = (*((FMatrix3x2 *)left)->glm) - (*((FMatrix3x2 *)right)->glm);
    }
    else
    {
        if (Py_TYPE(left) == cls)
        {
            auto c_right = pyobject_to_c_float(right);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
            matrix = (*((FMatrix3x2 *)left)->glm) - c_right;
        }
        else
        {
            auto c_left = pyobject_to_c_float(left);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }

                matrix = FMatrix3x2Glm(

                        c_left,

                        c_left,

                        c_left,

                        c_left,

                        c_left,

                        c_left

                ) - (*((FMatrix3x2 *)right)->glm);

        }
    }

    FMatrix3x2 *result = (FMatrix3x2 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new FMatrix3x2Glm(matrix);

    return (PyObject *)result;
}


static PyObject *
FMatrix3x2__mul__(PyObject *left, PyObject *right)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->FMatrix3x2_PyTypeObject;

    FMatrix3x2Glm matrix;
    if (Py_TYPE(left) == cls)
    {
        auto c_right = pyobject_to_c_float(right);
        if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
        matrix = (*((FMatrix3x2 *)left)->glm) * c_right;
    }
    else
    {
        auto c_left = pyobject_to_c_float(left);
        if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
        matrix = c_left * (*((FMatrix3x2 *)right)->glm);
    }

    FMatrix3x2 *result = (FMatrix3x2 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new FMatrix3x2Glm(matrix);

    return (PyObject *)result;
}


static PyObject *
FMatrix3x2__matmul__(PyObject *left, PyObject *right)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->FMatrix3x2_PyTypeObject;

    if (Py_TYPE(left) == cls)
    {



        {
            auto right_cls = module_state->FMatrix2x3_PyTypeObject;
            auto result_cls = module_state->FMatrix2x2_PyTypeObject;
            if (Py_TYPE(right) == right_cls)
            {
                FMatrix2x2 *result = (FMatrix2x2 *)result_cls->tp_alloc(result_cls, 0);
                if (!result){ return 0; }
                result->glm = new FMatrix2x2Glm(
                    (*((FMatrix3x2 *)left)->glm) * (*((FMatrix2x3 *)right)->glm)
                );
                return (PyObject *)result;
            }
        }





        {
            auto right_cls = module_state->FMatrix3x3_PyTypeObject;
            auto result_cls = module_state->FMatrix3x2_PyTypeObject;
            if (Py_TYPE(right) == right_cls)
            {
                FMatrix3x2 *result = (FMatrix3x2 *)result_cls->tp_alloc(result_cls, 0);
                if (!result){ return 0; }
                result->glm = new FMatrix3x2Glm(
                    (*((FMatrix3x2 *)left)->glm) * (*((FMatrix3x3 *)right)->glm)
                );
                return (PyObject *)result;
            }
        }





        {
            auto right_cls = module_state->FMatrix4x3_PyTypeObject;
            auto result_cls = module_state->FMatrix4x2_PyTypeObject;
            if (Py_TYPE(right) == right_cls)
            {
                FMatrix4x2 *result = (FMatrix4x2 *)result_cls->tp_alloc(result_cls, 0);
                if (!result){ return 0; }
                result->glm = new FMatrix4x2Glm(
                    (*((FMatrix3x2 *)left)->glm) * (*((FMatrix4x3 *)right)->glm)
                );
                return (PyObject *)result;
            }
        }




        {
            auto row_cls = module_state->FVector3_PyTypeObject;
            auto column_cls = module_state->FVector2_PyTypeObject;
            if (Py_TYPE(right) == row_cls)
            {
                FVector2 *result = (FVector2 *)column_cls->tp_alloc(column_cls, 0);
                if (!result){ return 0; }
                result->glm = new FVector2Glm(
                    (*((FMatrix3x2 *)left)->glm) * (*((FVector3 *)right)->glm)
                );
                return (PyObject *)result;
            }
        }
    }
    else
    {
        auto row_cls = module_state->FVector3_PyTypeObject;
        auto column_cls = module_state->FVector2_PyTypeObject;
        if (Py_TYPE(left) == column_cls)
        {
            FVector3 *result = (FVector3 *)row_cls->tp_alloc(row_cls, 0);
            if (!result){ return 0; }
            result->glm = new FVector3Glm(
                (*((FVector2 *)left)->glm) * (*((FMatrix3x2 *)right)->glm)
            );
            return (PyObject *)result;
        }
    }

    Py_RETURN_NOTIMPLEMENTED;
}

static PyObject *
FMatrix3x2__truediv__(PyObject *left, PyObject *right)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->FMatrix3x2_PyTypeObject;

    FMatrix3x2Glm matrix;
    if (Py_TYPE(left) == cls)
    {


        auto c_right = pyobject_to_c_float(right);
        if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
        matrix = (*((FMatrix3x2 *)left)->glm) / c_right;
    }
    else
    {


        auto c_left = pyobject_to_c_float(left);
        if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
        matrix = c_left / (*((FMatrix3x2 *)right)->glm);
    }

    FMatrix3x2 *result = (FMatrix3x2 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new FMatrix3x2Glm(matrix);

    return (PyObject *)result;
}


static PyObject *
FMatrix3x2__neg__(FMatrix3x2 *self)
{
    auto cls = Py_TYPE(self);

    FMatrix3x2 *result = (FMatrix3x2 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new FMatrix3x2Glm(-(*self->glm));

    return (PyObject *)result;
}


static int
FMatrix3x2_getbufferproc(FMatrix3x2 *self, Py_buffer *view, int flags)
{
    if (flags & PyBUF_WRITABLE)
    {
        PyErr_SetString(PyExc_TypeError, "FMatrix3x2 is read only");
        view->obj = 0;
        return -1;
    }
    view->buf = glm::value_ptr(*self->glm);
    view->obj = (PyObject *)self;
    view->len = sizeof(float) * 6;
    view->readonly = 1;
    view->itemsize = sizeof(float);
    view->format = "f";
    view->ndim = 2;
    static Py_ssize_t shape[] = { 3, 2 };
    view->shape = &shape[0];
    static Py_ssize_t strides[] = {
        sizeof(float) * 2,
        sizeof(float)
    };
    view->strides = &strides[0];
    view->suboffsets = 0;
    view->internal = 0;
    Py_INCREF(self);
    return 0;
}


static PyMemberDef FMatrix3x2_PyMemberDef[] = {
    {"__weaklistoffset__", T_PYSSIZET, offsetof(FMatrix3x2, weakreflist), READONLY},
    {0}
};






static FMatrix2x3 *
FMatrix3x2_transpose(FMatrix3x2 *self, void*)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->FMatrix2x3_PyTypeObject;

    FMatrix2x3Glm matrix = glm::transpose(*self->glm);
    FMatrix2x3 *result = (FMatrix2x3 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new FMatrix2x3Glm(matrix);
    return result;
}



static PyObject *
FMatrix3x2_get_limits(FMatrix3x2 *self, void *)
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


static PyMethodDef FMatrix3x2_PyMethodDef[] = {

    {"transpose", (PyCFunction)FMatrix3x2_transpose, METH_NOARGS, 0},
    {"get_limits", (PyCFunction)FMatrix3x2_get_limits, METH_NOARGS | METH_STATIC, 0},
    {0, 0, 0, 0}
};


static PyType_Slot FMatrix3x2_PyType_Slots [] = {
    {Py_tp_new, (void*)FMatrix3x2__new__},
    {Py_tp_dealloc, (void*)FMatrix3x2__dealloc__},
    {Py_tp_hash, (void*)FMatrix3x2__hash__},
    {Py_tp_repr, (void*)FMatrix3x2__repr__},
    {Py_sq_length, (void*)FMatrix3x2__len__},
    {Py_sq_item, (void*)FMatrix3x2__getitem__},
    {Py_tp_richcompare, (void*)FMatrix3x2__richcmp__},
    {Py_nb_add, (void*)FMatrix3x2__add__},
    {Py_nb_subtract, (void*)FMatrix3x2__sub__},
    {Py_nb_multiply, (void*)FMatrix3x2__mul__},
    {Py_nb_matrix_multiply, (void*)FMatrix3x2__matmul__},
    {Py_nb_true_divide, (void*)FMatrix3x2__truediv__},
    {Py_nb_negative, (void*)FMatrix3x2__neg__},
    {Py_bf_getbuffer, (void*)FMatrix3x2_getbufferproc},
    {Py_tp_members, (void*)FMatrix3x2_PyMemberDef},
    {Py_tp_methods, (void*)FMatrix3x2_PyMethodDef},
    {0, 0},
};


static PyType_Spec FMatrix3x2_PyTypeSpec = {
    "gamut.math.FMatrix3x2",
    sizeof(FMatrix3x2),
    0,
    Py_TPFLAGS_DEFAULT,
    FMatrix3x2_PyType_Slots
};


static PyTypeObject *
define_FMatrix3x2_type(PyObject *module)
{
    PyTypeObject *type = (PyTypeObject *)PyType_FromModuleAndSpec(
        module,
        &FMatrix3x2_PyTypeSpec,
        0
    );
    if (!type){ return 0; }
    // Note:
    // Unlike other functions that steal references, PyModule_AddObject() only
    // decrements the reference count of value on success.
    if (PyModule_AddObject(module, "FMatrix3x2", (PyObject *)type) < 0)
    {
        Py_DECREF(type);
        return 0;
    }
    return type;
}

#endif