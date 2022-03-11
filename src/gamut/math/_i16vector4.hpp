
// generated 2022-03-10 23:24:28.430931 from codegen/math/templates/_vector.hpp

#ifndef GAMUT_MATH_I16VECTOR4_HPP
#define GAMUT_MATH_I16VECTOR4_HPP

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
#include "_type.hpp"


static PyObject *
I16Vector4__new__(PyTypeObject *cls, PyObject *args, PyObject *kwds)
{

        int16_t c_0 = 0;

        int16_t c_1 = 0;

        int16_t c_2 = 0;

        int16_t c_3 = 0;


    if (kwds && PyDict_Size(kwds) != 0)
    {
        PyErr_SetString(
            PyExc_TypeError,
            "I16Vector4 does accept any keyword arguments"
        );
        return 0;
    }
    auto arg_count = PyTuple_GET_SIZE(args);
    switch (PyTuple_GET_SIZE(args))
    {
        case 0:
        {
            break;
        }
        case 1:
        {
            auto arg = PyTuple_GET_ITEM(args, 0);
            int16_t arg_c = pyobject_to_c_int16_t(arg);
            auto error_occurred = PyErr_Occurred();
            if (error_occurred){ return 0; }

                c_0 = arg_c;

                c_1 = arg_c;

                c_2 = arg_c;

                c_3 = arg_c;

            break;
        }
        case 4:
        {

            {
                auto arg = PyTuple_GET_ITEM(args, 0);
                c_0 = pyobject_to_c_int16_t(arg);
                auto error_occurred = PyErr_Occurred();
                if (error_occurred){ return 0; }
            }

            {
                auto arg = PyTuple_GET_ITEM(args, 1);
                c_1 = pyobject_to_c_int16_t(arg);
                auto error_occurred = PyErr_Occurred();
                if (error_occurred){ return 0; }
            }

            {
                auto arg = PyTuple_GET_ITEM(args, 2);
                c_2 = pyobject_to_c_int16_t(arg);
                auto error_occurred = PyErr_Occurred();
                if (error_occurred){ return 0; }
            }

            {
                auto arg = PyTuple_GET_ITEM(args, 3);
                c_3 = pyobject_to_c_int16_t(arg);
                auto error_occurred = PyErr_Occurred();
                if (error_occurred){ return 0; }
            }

            break;
        }
        default:
        {
            PyErr_Format(
                PyExc_TypeError,
                "invalid number of arguments supplied to I16Vector4, expected "
                "0, 1 or 4 (got %zd)",
                arg_count
            );
            return 0;
        }
    }

    I16Vector4 *self = (I16Vector4*)cls->tp_alloc(cls, 0);
    if (!self){ return 0; }
    self->glm = new I16Vector4Glm(

            c_0,

            c_1,

            c_2,

            c_3

    );

    return (PyObject *)self;
}


static void
I16Vector4__dealloc__(I16Vector4 *self)
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
I16Vector4__hash__(I16Vector4 *self)
{
    Py_ssize_t len = 4;
    Py_uhash_t acc = _HASH_XXPRIME_5;
    for (I16Vector4Glm::length_type i = 0; i < len; i++)
    {
        Py_uhash_t lane = std::hash<int16_t>{}((*self->glm)[i]);
        acc += lane * _HASH_XXPRIME_2;
        acc = _HASH_XXROTATE(acc);
        acc *= _HASH_XXPRIME_1;
    }
    acc += len ^ (_HASH_XXPRIME_5 ^ 3527539UL);

    if (acc == (Py_uhash_t)-1) {
        return 1546275796;
    }
    return acc;
}


static PyObject *
I16Vector4__repr__(I16Vector4 *self)
{
    PyObject *result = 0;

        PyObject *py_0 = 0;

        PyObject *py_1 = 0;

        PyObject *py_2 = 0;

        PyObject *py_3 = 0;



        py_0 = c_int16_t_to_pyobject((*self->glm)[0]);
        if (!py_0){ goto cleanup; }

        py_1 = c_int16_t_to_pyobject((*self->glm)[1]);
        if (!py_1){ goto cleanup; }

        py_2 = c_int16_t_to_pyobject((*self->glm)[2]);
        if (!py_2){ goto cleanup; }

        py_3 = c_int16_t_to_pyobject((*self->glm)[3]);
        if (!py_3){ goto cleanup; }

    result = PyUnicode_FromFormat(
        "I16Vector4("

            "%R, "

            "%R, "

            "%R, "

            "%R"

        ")",

            py_0,

            py_1,

            py_2,

            py_3

    );
cleanup:

        Py_XDECREF(py_0);

        Py_XDECREF(py_1);

        Py_XDECREF(py_2);

        Py_XDECREF(py_3);

    return result;
}


static Py_ssize_t
I16Vector4__len__(I16Vector4 *self)
{
    return 4;
}


static PyObject *
I16Vector4__getitem__(I16Vector4 *self, Py_ssize_t index)
{
    if (index < 0 || index > 3)
    {
        PyErr_Format(PyExc_IndexError, "index out of range");
        return 0;
    }
    auto c = (*self->glm)[(I16Vector4Glm::length_type)index];
    return c_int16_t_to_pyobject(c);
}


static PyObject *
I16Vector4__richcmp__(I16Vector4 *self, I16Vector4 *other, int op)
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
I16Vector4__add__(PyObject *left, PyObject *right)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->I16Vector4_PyTypeObject;

    I16Vector4Glm vector;
    if (Py_TYPE(left) == Py_TYPE(right))
    {
        vector = (*((I16Vector4 *)left)->glm) + (*((I16Vector4 *)right)->glm);
    }
    else
    {
        if (Py_TYPE(left) == cls)
        {
            auto c_right = pyobject_to_c_int16_t(right);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
            vector = (*((I16Vector4 *)left)->glm) + c_right;
        }
        else
        {
            auto c_left = pyobject_to_c_int16_t(left);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
            vector = c_left + (*((I16Vector4 *)right)->glm);
        }
    }

    I16Vector4 *result = (I16Vector4 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new I16Vector4Glm(

            vector[0],

            vector[1],

            vector[2],

            vector[3]

    );

    return (PyObject *)result;
}


static PyObject *
I16Vector4__sub__(PyObject *left, PyObject *right)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->I16Vector4_PyTypeObject;

    I16Vector4Glm vector;
    if (Py_TYPE(left) == Py_TYPE(right))
    {
        vector = (*((I16Vector4 *)left)->glm) - (*((I16Vector4 *)right)->glm);
    }
    else
    {
        if (Py_TYPE(left) == cls)
        {
            auto c_right = pyobject_to_c_int16_t(right);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
            vector = (*((I16Vector4 *)left)->glm) - c_right;
        }
        else
        {
            auto c_left = pyobject_to_c_int16_t(left);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
            vector = c_left - (*((I16Vector4 *)right)->glm);
        }
    }

    I16Vector4 *result = (I16Vector4 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new I16Vector4Glm(

            vector[0],

            vector[1],

            vector[2],

            vector[3]

    );

    return (PyObject *)result;
}


static PyObject *
I16Vector4__mul__(PyObject *left, PyObject *right)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->I16Vector4_PyTypeObject;

    I16Vector4Glm vector;
    if (Py_TYPE(left) == Py_TYPE(right))
    {
        vector = (*((I16Vector4 *)left)->glm) * (*((I16Vector4 *)right)->glm);
    }
    else
    {
        if (Py_TYPE(left) == cls)
        {
            auto c_right = pyobject_to_c_int16_t(right);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
            vector = (*((I16Vector4 *)left)->glm) * c_right;
        }
        else
        {
            auto c_left = pyobject_to_c_int16_t(left);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
            vector = c_left * (*((I16Vector4 *)right)->glm);
        }
    }

    I16Vector4 *result = (I16Vector4 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new I16Vector4Glm(

            vector[0],

            vector[1],

            vector[2],

            vector[3]

    );

    return (PyObject *)result;
}







    static PyObject *
    I16Vector4__truediv__(PyObject *left, PyObject *right)
    {
        auto module_state = get_module_state();
        if (!module_state){ return 0; }
        auto cls = module_state->I16Vector4_PyTypeObject;

        I16Vector4Glm vector;
        if (Py_TYPE(left) == Py_TYPE(right))
        {

                if (

                        (*((I16Vector4 *)right)->glm)[0] == 0 ||

                        (*((I16Vector4 *)right)->glm)[1] == 0 ||

                        (*((I16Vector4 *)right)->glm)[2] == 0 ||

                        (*((I16Vector4 *)right)->glm)[3] == 0

                )
                {
                    PyErr_SetString(PyExc_ZeroDivisionError, "divide by zero");
                    return 0;
                }

            vector = (*((I16Vector4 *)left)->glm) / (*((I16Vector4 *)right)->glm);
        }
        else
        {
            if (Py_TYPE(left) == cls)
            {
                auto c_right = pyobject_to_c_int16_t(right);
                if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }

                    if (c_right == 0)
                    {
                        PyErr_SetString(PyExc_ZeroDivisionError, "divide by zero");
                        return 0;
                    }

                vector = (*((I16Vector4 *)left)->glm) / c_right;
            }
            else
            {
                auto c_left = pyobject_to_c_int16_t(left);
                if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }

                    if (

                            (*((I16Vector4 *)right)->glm)[0] == 0 ||

                            (*((I16Vector4 *)right)->glm)[1] == 0 ||

                            (*((I16Vector4 *)right)->glm)[2] == 0 ||

                            (*((I16Vector4 *)right)->glm)[3] == 0

                    )
                    {
                        PyErr_SetString(PyExc_ZeroDivisionError, "divide by zero");
                        return 0;
                    }

                vector = c_left / (*((I16Vector4 *)right)->glm);
            }
        }

        I16Vector4 *result = (I16Vector4 *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new I16Vector4Glm(

                vector[0],

                vector[1],

                vector[2],

                vector[3]

        );

        return (PyObject *)result;
    }




    static PyObject *
    I16Vector4__neg__(I16Vector4 *self)
    {
        auto cls = Py_TYPE(self);

            I16Vector4Glm vector = -(*self->glm);


        I16Vector4 *result = (I16Vector4 *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new I16Vector4Glm(

                vector[0],

                vector[1],

                vector[2],

                vector[3]

        );

        return (PyObject *)result;
    }



static PyObject *
I16Vector4__abs__(I16Vector4 *self)
{
    auto cls = Py_TYPE(self);
    I16Vector4Glm vector = glm::abs(*self->glm);

    I16Vector4 *result = (I16Vector4 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new I16Vector4Glm(

            vector[0],

            vector[1],

            vector[2],

            vector[3]

    );

    return (PyObject *)result;
}


static int
I16Vector4__bool__(I16Vector4 *self)
{

        if ((*self->glm)[0] == 0)
        {
            return 0;
        }

        if ((*self->glm)[1] == 0)
        {
            return 0;
        }

        if ((*self->glm)[2] == 0)
        {
            return 0;
        }

        if ((*self->glm)[3] == 0)
        {
            return 0;
        }

    return 1;
}


static int
I16Vector4_getbufferproc(I16Vector4 *self, Py_buffer *view, int flags)
{
    if (flags & PyBUF_WRITABLE)
    {
        PyErr_SetString(PyExc_TypeError, "I16Vector4 is read only");
        view->obj = 0;
        return -1;
    }
    view->buf = glm::value_ptr(*self->glm);
    view->obj = (PyObject *)self;
    view->len = sizeof(int16_t) * 4;
    view->readonly = 1;
    view->itemsize = sizeof(int16_t);
    view->format = "=h";
    view->ndim = 1;
    static Py_ssize_t shape = 4;
    view->shape = &shape;
    view->strides = &view->itemsize;
    view->suboffsets = 0;
    view->internal = 0;
    Py_INCREF(self);
    return 0;
}



    static PyObject *
    I16Vector4_Getter_0(I16Vector4 *self, void *)
    {
        auto c = (*self->glm)[0];
        return c_int16_t_to_pyobject(c);
    }

    static PyObject *
    I16Vector4_Getter_1(I16Vector4 *self, void *)
    {
        auto c = (*self->glm)[1];
        return c_int16_t_to_pyobject(c);
    }

    static PyObject *
    I16Vector4_Getter_2(I16Vector4 *self, void *)
    {
        auto c = (*self->glm)[2];
        return c_int16_t_to_pyobject(c);
    }

    static PyObject *
    I16Vector4_Getter_3(I16Vector4 *self, void *)
    {
        auto c = (*self->glm)[3];
        return c_int16_t_to_pyobject(c);
    }






static PyGetSetDef I16Vector4_PyGetSetDef[] = {
    {"x", (getter)I16Vector4_Getter_0, 0, 0, 0},
    {"r", (getter)I16Vector4_Getter_0, 0, 0, 0},
    {"s", (getter)I16Vector4_Getter_0, 0, 0, 0},
    {"u", (getter)I16Vector4_Getter_0, 0, 0, 0},

        {"y", (getter)I16Vector4_Getter_1, 0, 0, 0},
        {"g", (getter)I16Vector4_Getter_1, 0, 0, 0},
        {"t", (getter)I16Vector4_Getter_1, 0, 0, 0},
        {"v", (getter)I16Vector4_Getter_1, 0, 0, 0},


        {"z", (getter)I16Vector4_Getter_2, 0, 0, 0},
        {"b", (getter)I16Vector4_Getter_2, 0, 0, 0},
        {"p", (getter)I16Vector4_Getter_2, 0, 0, 0},


        {"w", (getter)I16Vector4_Getter_3, 0, 0, 0},
        {"a", (getter)I16Vector4_Getter_3, 0, 0, 0},
        {"q", (getter)I16Vector4_Getter_3, 0, 0, 0},


    {0, 0, 0, 0, 0}
};



    static PyObject *
    swizzle_2_I16Vector4(I16Vector4 *self, PyObject *py_attr)
    {
        const char *attr = PyUnicode_AsUTF8(py_attr);
        if (!attr){ return 0; }

        I16Vector2Glm vec;
        for (int i = 0; i < 2; i++)
        {
            char c_name = attr[i];
            int glm_index;
            switch(c_name)
            {
                case 'x':
                case 'r':
                case 's':
                case 'u':
                    glm_index = 0;
                    break;

                    case 'y':
                    case 'g':
                    case 't':
                    case 'v':
                        glm_index = 1;
                        break;


                    case 'z':
                    case 'b':
                    case 'p':
                        glm_index = 2;
                        break;


                    case 'w':
                    case 'a':
                    case 'q':
                        glm_index = 3;
                        break;

                default:
                {
                    PyErr_Format(
                        PyExc_AttributeError,
                        "invalid swizzle: %R", py_attr
                    );
                    return 0;
                }
            }
            vec[i] = (*self->glm)[glm_index];
        }

        auto module_state = get_module_state();
        if (!module_state){ return 0; }
        auto cls = module_state->I16Vector2_PyTypeObject;

        I16Vector2 *result = (I16Vector2 *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new I16Vector2Glm(vec);

        return (PyObject *)result;
    }



    static PyObject *
    swizzle_3_I16Vector4(I16Vector4 *self, PyObject *py_attr)
    {
        const char *attr = PyUnicode_AsUTF8(py_attr);
        if (!attr){ return 0; }

        I16Vector3Glm vec;
        for (int i = 0; i < 3; i++)
        {
            char c_name = attr[i];
            int glm_index;
            switch(c_name)
            {
                case 'x':
                case 'r':
                case 's':
                case 'u':
                    glm_index = 0;
                    break;

                    case 'y':
                    case 'g':
                    case 't':
                    case 'v':
                        glm_index = 1;
                        break;


                    case 'z':
                    case 'b':
                    case 'p':
                        glm_index = 2;
                        break;


                    case 'w':
                    case 'a':
                    case 'q':
                        glm_index = 3;
                        break;

                default:
                {
                    PyErr_Format(
                        PyExc_AttributeError,
                        "invalid swizzle: %R", py_attr
                    );
                    return 0;
                }
            }
            vec[i] = (*self->glm)[glm_index];
        }

        auto module_state = get_module_state();
        if (!module_state){ return 0; }
        auto cls = module_state->I16Vector3_PyTypeObject;

        I16Vector3 *result = (I16Vector3 *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new I16Vector3Glm(vec);

        return (PyObject *)result;
    }



    static PyObject *
    swizzle_4_I16Vector4(I16Vector4 *self, PyObject *py_attr)
    {
        const char *attr = PyUnicode_AsUTF8(py_attr);
        if (!attr){ return 0; }

        I16Vector4Glm vec;
        for (int i = 0; i < 4; i++)
        {
            char c_name = attr[i];
            int glm_index;
            switch(c_name)
            {
                case 'x':
                case 'r':
                case 's':
                case 'u':
                    glm_index = 0;
                    break;

                    case 'y':
                    case 'g':
                    case 't':
                    case 'v':
                        glm_index = 1;
                        break;


                    case 'z':
                    case 'b':
                    case 'p':
                        glm_index = 2;
                        break;


                    case 'w':
                    case 'a':
                    case 'q':
                        glm_index = 3;
                        break;

                default:
                {
                    PyErr_Format(
                        PyExc_AttributeError,
                        "invalid swizzle: %R", py_attr
                    );
                    return 0;
                }
            }
            vec[i] = (*self->glm)[glm_index];
        }

        auto module_state = get_module_state();
        if (!module_state){ return 0; }
        auto cls = module_state->I16Vector4_PyTypeObject;

        I16Vector4 *result = (I16Vector4 *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new I16Vector4Glm(vec);

        return (PyObject *)result;
    }




static PyObject *
I16Vector4__getattr__(I16Vector4 *self, PyObject *py_attr)
{
    PyObject *result = PyObject_GenericGetAttr((PyObject *)self, py_attr);
    if (result != 0){ return result; }

    auto attr_length = PyUnicode_GET_LENGTH(py_attr);
    switch(attr_length)
    {
        case 2:
        {
            PyErr_Clear();
            return swizzle_2_I16Vector4(self, py_attr);
        }
        case 3:
        {
            PyErr_Clear();
            return swizzle_3_I16Vector4(self, py_attr);
        }
        case 4:
        {
            PyErr_Clear();
            return swizzle_4_I16Vector4(self, py_attr);
        }
    }
    return 0;
}


static PyMemberDef I16Vector4_PyMemberDef[] = {
    {"__weaklistoffset__", T_PYSSIZET, offsetof(I16Vector4, weakreflist), READONLY},
    {0}
};





static PyObject *
I16Vector4_get_limits(I16Vector4 *self, void *)
{
    auto c_min = std::numeric_limits<int16_t>::lowest();
    auto c_max = std::numeric_limits<int16_t>::max();
    auto py_min = c_int16_t_to_pyobject(c_min);
    if (!py_min){ return 0; }
    auto py_max = c_int16_t_to_pyobject(c_max);
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


static PyMethodDef I16Vector4_PyMethodDef[] = {

    {"get_limits", (PyCFunction)I16Vector4_get_limits, METH_NOARGS | METH_STATIC, 0},
    {0, 0, 0, 0}
};


static PyType_Slot I16Vector4_PyType_Slots [] = {
    {Py_tp_new, (void*)I16Vector4__new__},
    {Py_tp_dealloc, (void*)I16Vector4__dealloc__},
    {Py_tp_hash, (void*)I16Vector4__hash__},
    {Py_tp_repr, (void*)I16Vector4__repr__},
    {Py_sq_length, (void*)I16Vector4__len__},
    {Py_sq_item, (void*)I16Vector4__getitem__},
    {Py_tp_richcompare, (void*)I16Vector4__richcmp__},
    {Py_nb_add, (void*)I16Vector4__add__},
    {Py_nb_subtract, (void*)I16Vector4__sub__},
    {Py_nb_multiply, (void*)I16Vector4__mul__},


        {Py_nb_true_divide, (void*)I16Vector4__truediv__},


        {Py_nb_negative, (void*)I16Vector4__neg__},

    {Py_nb_absolute, (void*)I16Vector4__abs__},
    {Py_nb_bool, (void*)I16Vector4__bool__},
    {Py_bf_getbuffer, (void*)I16Vector4_getbufferproc},
    {Py_tp_getset, (void*)I16Vector4_PyGetSetDef},
    {Py_tp_getattro, (void*)I16Vector4__getattr__},
    {Py_tp_members, (void*)I16Vector4_PyMemberDef},
    {Py_tp_methods, (void*)I16Vector4_PyMethodDef},
    {0, 0},
};


static PyType_Spec I16Vector4_PyTypeSpec = {
    "gamut.math.I16Vector4",
    sizeof(I16Vector4),
    0,
    Py_TPFLAGS_DEFAULT,
    I16Vector4_PyType_Slots
};


static PyTypeObject *
define_I16Vector4_type(PyObject *module)
{
    PyTypeObject *type = (PyTypeObject *)PyType_FromModuleAndSpec(
        module,
        &I16Vector4_PyTypeSpec,
        0
    );
    if (!type){ return 0; }
    // Note:
    // Unlike other functions that steal references, PyModule_AddObject() only
    // decrements the reference count of value on success.
    if (PyModule_AddObject(module, "I16Vector4", (PyObject *)type) < 0)
    {
        Py_DECREF(type);
        return 0;
    }
    return type;
}


static I16Vector4 *
create_I16Vector4_from_glm(const I16Vector4Glm& glm)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->I16Vector4_PyTypeObject;

    I16Vector4 *result = (I16Vector4 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new I16Vector4Glm(glm);

    return result;
}

#endif