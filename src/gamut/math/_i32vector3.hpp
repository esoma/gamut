
// generated 2022-03-26 19:22:10.938477 from codegen/math/templates/_vector.hpp

#ifndef GAMUT_MATH_I32VECTOR3_HPP
#define GAMUT_MATH_I32VECTOR3_HPP

// stdlib
#include <limits>
#include <functional>
// python
#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <structmember.h>
// glm
#include <glm/glm.hpp>
#include <glm/gtx/compatibility.hpp>
#include <glm/ext.hpp>
// gamut
#include "_modulestate.hpp"
#include "_quaterniontype.hpp"
#include "_vectortype.hpp"
#include "_type.hpp"


static PyObject *
I32Vector3__new__(PyTypeObject *cls, PyObject *args, PyObject *kwds)
{

        int32_t c_0 = 0;

        int32_t c_1 = 0;

        int32_t c_2 = 0;


    if (kwds && PyDict_Size(kwds) != 0)
    {
        PyErr_SetString(
            PyExc_TypeError,
            "I32Vector3 does accept any keyword arguments"
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
            int32_t arg_c = pyobject_to_c_int32_t(arg);
            auto error_occurred = PyErr_Occurred();
            if (error_occurred){ return 0; }

                c_0 = arg_c;

                c_1 = arg_c;

                c_2 = arg_c;

            break;
        }

            case 3:
            {

                {
                    auto arg = PyTuple_GET_ITEM(args, 0);
                    c_0 = pyobject_to_c_int32_t(arg);
                    auto error_occurred = PyErr_Occurred();
                    if (error_occurred){ return 0; }
                }

                {
                    auto arg = PyTuple_GET_ITEM(args, 1);
                    c_1 = pyobject_to_c_int32_t(arg);
                    auto error_occurred = PyErr_Occurred();
                    if (error_occurred){ return 0; }
                }

                {
                    auto arg = PyTuple_GET_ITEM(args, 2);
                    c_2 = pyobject_to_c_int32_t(arg);
                    auto error_occurred = PyErr_Occurred();
                    if (error_occurred){ return 0; }
                }

                break;
            }

        default:
        {
            PyErr_Format(
                PyExc_TypeError,
                "invalid number of arguments supplied to I32Vector3, expected "
                "0, 1 or 3 (got %zd)",
                arg_count
            );
            return 0;
        }
    }

    I32Vector3 *self = (I32Vector3*)cls->tp_alloc(cls, 0);
    if (!self){ return 0; }
    self->glm = new I32Vector3Glm(

            c_0,

            c_1,

            c_2

    );

    return (PyObject *)self;
}


static void
I32Vector3__dealloc__(I32Vector3 *self)
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
I32Vector3__hash__(I32Vector3 *self)
{
    Py_ssize_t len = 3;
    Py_uhash_t acc = _HASH_XXPRIME_5;
    for (I32Vector3Glm::length_type i = 0; i < len; i++)
    {
        Py_uhash_t lane = std::hash<int32_t>{}((*self->glm)[i]);
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
I32Vector3__repr__(I32Vector3 *self)
{
    PyObject *result = 0;

        PyObject *py_0 = 0;

        PyObject *py_1 = 0;

        PyObject *py_2 = 0;



        py_0 = c_int32_t_to_pyobject((*self->glm)[0]);
        if (!py_0){ goto cleanup; }

        py_1 = c_int32_t_to_pyobject((*self->glm)[1]);
        if (!py_1){ goto cleanup; }

        py_2 = c_int32_t_to_pyobject((*self->glm)[2]);
        if (!py_2){ goto cleanup; }

    result = PyUnicode_FromFormat(
        "I32Vector3("

            "%R, "

            "%R, "

            "%R"

        ")",

            py_0,

            py_1,

            py_2

    );
cleanup:

        Py_XDECREF(py_0);

        Py_XDECREF(py_1);

        Py_XDECREF(py_2);

    return result;
}


static Py_ssize_t
I32Vector3__len__(I32Vector3 *self)
{
    return 3;
}


static PyObject *
I32Vector3__getitem__(I32Vector3 *self, Py_ssize_t index)
{
    if (index < 0 || index > 2)
    {
        PyErr_Format(PyExc_IndexError, "index out of range");
        return 0;
    }
    auto c = (*self->glm)[(I32Vector3Glm::length_type)index];
    return c_int32_t_to_pyobject(c);
}


static PyObject *
I32Vector3__richcmp__(I32Vector3 *self, I32Vector3 *other, int op)
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
I32Vector3__add__(PyObject *left, PyObject *right)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->I32Vector3_PyTypeObject;

    I32Vector3Glm vector;
    if (Py_TYPE(left) == Py_TYPE(right))
    {
        vector = (*((I32Vector3 *)left)->glm) + (*((I32Vector3 *)right)->glm);
    }
    else
    {
        if (Py_TYPE(left) == cls)
        {
            auto c_right = pyobject_to_c_int32_t(right);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
            vector = (*((I32Vector3 *)left)->glm) + c_right;
        }
        else
        {
            auto c_left = pyobject_to_c_int32_t(left);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
            vector = c_left + (*((I32Vector3 *)right)->glm);
        }
    }

    I32Vector3 *result = (I32Vector3 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new I32Vector3Glm(

            vector[0],

            vector[1],

            vector[2]

    );

    return (PyObject *)result;
}


static PyObject *
I32Vector3__sub__(PyObject *left, PyObject *right)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->I32Vector3_PyTypeObject;

    I32Vector3Glm vector;
    if (Py_TYPE(left) == Py_TYPE(right))
    {
        vector = (*((I32Vector3 *)left)->glm) - (*((I32Vector3 *)right)->glm);
    }
    else
    {
        if (Py_TYPE(left) == cls)
        {
            auto c_right = pyobject_to_c_int32_t(right);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
            vector = (*((I32Vector3 *)left)->glm) - c_right;
        }
        else
        {
            auto c_left = pyobject_to_c_int32_t(left);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
            vector = c_left - (*((I32Vector3 *)right)->glm);
        }
    }

    I32Vector3 *result = (I32Vector3 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new I32Vector3Glm(

            vector[0],

            vector[1],

            vector[2]

    );

    return (PyObject *)result;
}


static PyObject *
I32Vector3__mul__(PyObject *left, PyObject *right)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->I32Vector3_PyTypeObject;

    I32Vector3Glm vector;
    if (Py_TYPE(left) == Py_TYPE(right))
    {
        vector = (*((I32Vector3 *)left)->glm) * (*((I32Vector3 *)right)->glm);
    }
    else
    {
        if (Py_TYPE(left) == cls)
        {
            auto c_right = pyobject_to_c_int32_t(right);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
            vector = (*((I32Vector3 *)left)->glm) * c_right;
        }
        else
        {
            auto c_left = pyobject_to_c_int32_t(left);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
            vector = c_left * (*((I32Vector3 *)right)->glm);
        }
    }

    I32Vector3 *result = (I32Vector3 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new I32Vector3Glm(

            vector[0],

            vector[1],

            vector[2]

    );

    return (PyObject *)result;
}







    static PyObject *
    I32Vector3__truediv__(PyObject *left, PyObject *right)
    {
        auto module_state = get_module_state();
        if (!module_state){ return 0; }
        auto cls = module_state->I32Vector3_PyTypeObject;

        I32Vector3Glm vector;
        if (Py_TYPE(left) == Py_TYPE(right))
        {

                if (

                        (*((I32Vector3 *)right)->glm)[0] == 0 ||

                        (*((I32Vector3 *)right)->glm)[1] == 0 ||

                        (*((I32Vector3 *)right)->glm)[2] == 0

                )
                {
                    PyErr_SetString(PyExc_ZeroDivisionError, "divide by zero");
                    return 0;
                }

            vector = (*((I32Vector3 *)left)->glm) / (*((I32Vector3 *)right)->glm);
        }
        else
        {
            if (Py_TYPE(left) == cls)
            {
                auto c_right = pyobject_to_c_int32_t(right);
                if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }

                    if (c_right == 0)
                    {
                        PyErr_SetString(PyExc_ZeroDivisionError, "divide by zero");
                        return 0;
                    }

                vector = (*((I32Vector3 *)left)->glm) / c_right;
            }
            else
            {
                auto c_left = pyobject_to_c_int32_t(left);
                if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }

                    if (

                            (*((I32Vector3 *)right)->glm)[0] == 0 ||

                            (*((I32Vector3 *)right)->glm)[1] == 0 ||

                            (*((I32Vector3 *)right)->glm)[2] == 0

                    )
                    {
                        PyErr_SetString(PyExc_ZeroDivisionError, "divide by zero");
                        return 0;
                    }

                vector = c_left / (*((I32Vector3 *)right)->glm);
            }
        }

        I32Vector3 *result = (I32Vector3 *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new I32Vector3Glm(

                vector[0],

                vector[1],

                vector[2]

        );

        return (PyObject *)result;
    }




    static PyObject *
    I32Vector3__neg__(I32Vector3 *self)
    {
        auto cls = Py_TYPE(self);

            I32Vector3Glm vector = -(*self->glm);


        I32Vector3 *result = (I32Vector3 *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new I32Vector3Glm(

                vector[0],

                vector[1],

                vector[2]

        );

        return (PyObject *)result;
    }



static PyObject *
I32Vector3__abs__(I32Vector3 *self)
{
    auto cls = Py_TYPE(self);
    I32Vector3Glm vector = glm::abs(*self->glm);

    I32Vector3 *result = (I32Vector3 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new I32Vector3Glm(

            vector[0],

            vector[1],

            vector[2]

    );

    return (PyObject *)result;
}


static int
I32Vector3__bool__(I32Vector3 *self)
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

    return 1;
}


static int
I32Vector3_getbufferproc(I32Vector3 *self, Py_buffer *view, int flags)
{
    if (flags & PyBUF_WRITABLE)
    {
        PyErr_SetString(PyExc_TypeError, "I32Vector3 is read only");
        view->obj = 0;
        return -1;
    }
    view->buf = self->glm;
    view->obj = (PyObject *)self;
    view->len = sizeof(int32_t) * 3;
    view->readonly = 1;
    view->itemsize = sizeof(int32_t);
    view->ndim = 1;
    if (flags & PyBUF_FORMAT)
    {
        view->format = "=i";
    }
    else
    {
        view->format = 0;
    }
    if (flags & PyBUF_ND)
    {
        static Py_ssize_t shape = 3;
        view->shape = &shape;
    }
    else
    {
        view->shape = 0;
    }
    if (flags & PyBUF_STRIDES)
    {
        view->strides = &view->itemsize;
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



    static PyObject *
    I32Vector3_Getter_0(I32Vector3 *self, void *)
    {
        auto c = (*self->glm)[0];
        return c_int32_t_to_pyobject(c);
    }

    static PyObject *
    I32Vector3_Getter_1(I32Vector3 *self, void *)
    {
        auto c = (*self->glm)[1];
        return c_int32_t_to_pyobject(c);
    }

    static PyObject *
    I32Vector3_Getter_2(I32Vector3 *self, void *)
    {
        auto c = (*self->glm)[2];
        return c_int32_t_to_pyobject(c);
    }






static PyObject *
I32Vector3_pointer(I32Vector3 *self, void *)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto c_p = module_state->ctypes_c_int32_t_p;
    return PyObject_CallMethod(c_p, "from_address", "n", (Py_ssize_t)&self->glm);
}


static PyGetSetDef I32Vector3_PyGetSetDef[] = {
    {"x", (getter)I32Vector3_Getter_0, 0, 0, 0},
    {"r", (getter)I32Vector3_Getter_0, 0, 0, 0},
    {"s", (getter)I32Vector3_Getter_0, 0, 0, 0},
    {"u", (getter)I32Vector3_Getter_0, 0, 0, 0},

        {"y", (getter)I32Vector3_Getter_1, 0, 0, 0},
        {"g", (getter)I32Vector3_Getter_1, 0, 0, 0},
        {"t", (getter)I32Vector3_Getter_1, 0, 0, 0},
        {"v", (getter)I32Vector3_Getter_1, 0, 0, 0},


        {"z", (getter)I32Vector3_Getter_2, 0, 0, 0},
        {"b", (getter)I32Vector3_Getter_2, 0, 0, 0},
        {"p", (getter)I32Vector3_Getter_2, 0, 0, 0},



    {"pointer", (getter)I32Vector3_pointer, 0, 0, 0},
    {0, 0, 0, 0, 0}
};



    static PyObject *
    swizzle_2_I32Vector3(I32Vector3 *self, PyObject *py_attr)
    {
        const char *attr = PyUnicode_AsUTF8(py_attr);
        if (!attr){ return 0; }

        I32Vector2Glm vec;
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
        auto cls = module_state->I32Vector2_PyTypeObject;

        I32Vector2 *result = (I32Vector2 *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new I32Vector2Glm(vec);

        return (PyObject *)result;
    }



    static PyObject *
    swizzle_3_I32Vector3(I32Vector3 *self, PyObject *py_attr)
    {
        const char *attr = PyUnicode_AsUTF8(py_attr);
        if (!attr){ return 0; }

        I32Vector3Glm vec;
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
        auto cls = module_state->I32Vector3_PyTypeObject;

        I32Vector3 *result = (I32Vector3 *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new I32Vector3Glm(vec);

        return (PyObject *)result;
    }



    static PyObject *
    swizzle_4_I32Vector3(I32Vector3 *self, PyObject *py_attr)
    {
        const char *attr = PyUnicode_AsUTF8(py_attr);
        if (!attr){ return 0; }

        I32Vector4Glm vec;
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
        auto cls = module_state->I32Vector4_PyTypeObject;

        I32Vector4 *result = (I32Vector4 *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new I32Vector4Glm(vec);

        return (PyObject *)result;
    }




static PyObject *
I32Vector3__getattr__(I32Vector3 *self, PyObject *py_attr)
{
    PyObject *result = PyObject_GenericGetAttr((PyObject *)self, py_attr);
    if (result != 0){ return result; }

    auto attr_length = PyUnicode_GET_LENGTH(py_attr);
    switch(attr_length)
    {
        case 2:
        {
            PyErr_Clear();
            return swizzle_2_I32Vector3(self, py_attr);
        }
        case 3:
        {
            PyErr_Clear();
            return swizzle_3_I32Vector3(self, py_attr);
        }
        case 4:
        {
            PyErr_Clear();
            return swizzle_4_I32Vector3(self, py_attr);
        }
    }
    return 0;
}


static PyMemberDef I32Vector3_PyMemberDef[] = {
    {"__weaklistoffset__", T_PYSSIZET, offsetof(I32Vector3, weakreflist), READONLY},
    {0}
};





static PyObject *
I32Vector3_min(I32Vector3 *self, PyObject *min)
{
    auto c_min = pyobject_to_c_int32_t(min);
    if (PyErr_Occurred()){ return 0; }
    auto cls = Py_TYPE(self);
    auto vector = glm::min(*self->glm, c_min);
    I32Vector3 *result = (I32Vector3 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new I32Vector3Glm(vector);
    return (PyObject *)result;
}


static PyObject *
I32Vector3_max(I32Vector3 *self, PyObject *max)
{
    auto c_max = pyobject_to_c_int32_t(max);
    if (PyErr_Occurred()){ return 0; }
    auto cls = Py_TYPE(self);
    auto vector = glm::max(*self->glm, c_max);
    I32Vector3 *result = (I32Vector3 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new I32Vector3Glm(vector);
    return (PyObject *)result;
}


static PyObject *
I32Vector3_clamp(I32Vector3 *self, PyObject *const *args, Py_ssize_t nargs)
{
    if (nargs != 2)
    {
        PyErr_Format(PyExc_TypeError, "expected 2 arguments, got %zi", nargs);
        return 0;
    }
    auto c_min = pyobject_to_c_int32_t(args[0]);
    if (PyErr_Occurred()){ return 0; }
    auto c_max = pyobject_to_c_int32_t(args[1]);
    if (PyErr_Occurred()){ return 0; }

    auto cls = Py_TYPE(self);
    auto vector = glm::clamp(*self->glm, c_min, c_max);
    I32Vector3 *result = (I32Vector3 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new I32Vector3Glm(vector);
    return (PyObject *)result;
}


static PyObject *
I32Vector3_get_size(I32Vector3 *cls, void *)
{
    return PyLong_FromSize_t(sizeof(int32_t) * 3);
}


static PyObject *
I32Vector3_get_limits(I32Vector3 *cls, void *)
{
    auto c_min = std::numeric_limits<int32_t>::lowest();
    auto c_max = std::numeric_limits<int32_t>::max();
    auto py_min = c_int32_t_to_pyobject(c_min);
    if (!py_min){ return 0; }
    auto py_max = c_int32_t_to_pyobject(c_max);
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
I32Vector3_from_buffer(PyTypeObject *cls, PyObject *buffer)
{
    static Py_ssize_t expected_size = sizeof(int32_t) * 3;
    Py_buffer view;
    if (PyObject_GetBuffer(buffer, &view, PyBUF_SIMPLE) == -1){ return 0; }
    auto view_length = view.len;
    if (view_length < expected_size)
    {
        PyBuffer_Release(&view);
        PyErr_Format(PyExc_BufferError, "expected buffer of size %zd, got %zd", expected_size, view_length);
        return 0;
    }

    auto *result = (I32Vector3 *)cls->tp_alloc(cls, 0);
    if (!result)
    {
        PyBuffer_Release(&view);
        return 0;
    }
    result->glm = new I32Vector3Glm();
    std::memcpy(result->glm, view.buf, expected_size);
    PyBuffer_Release(&view);
    return (PyObject *)result;
}


static PyMethodDef I32Vector3_PyMethodDef[] = {

    {"min", (PyCFunction)I32Vector3_min, METH_O, 0},
    {"max", (PyCFunction)I32Vector3_max, METH_O, 0},
    {"clamp", (PyCFunction)I32Vector3_clamp, METH_FASTCALL, 0},
    {"get_limits", (PyCFunction)I32Vector3_get_limits, METH_NOARGS | METH_STATIC, 0},
    {"get_size", (PyCFunction)I32Vector3_get_size, METH_NOARGS | METH_STATIC, 0},
    {"from_buffer", (PyCFunction)I32Vector3_from_buffer, METH_O | METH_CLASS, 0},
    {0, 0, 0, 0}
};


static PyType_Slot I32Vector3_PyType_Slots [] = {
    {Py_tp_new, (void*)I32Vector3__new__},
    {Py_tp_dealloc, (void*)I32Vector3__dealloc__},
    {Py_tp_hash, (void*)I32Vector3__hash__},
    {Py_tp_repr, (void*)I32Vector3__repr__},
    {Py_sq_length, (void*)I32Vector3__len__},
    {Py_sq_item, (void*)I32Vector3__getitem__},
    {Py_tp_richcompare, (void*)I32Vector3__richcmp__},
    {Py_nb_add, (void*)I32Vector3__add__},
    {Py_nb_subtract, (void*)I32Vector3__sub__},
    {Py_nb_multiply, (void*)I32Vector3__mul__},


        {Py_nb_true_divide, (void*)I32Vector3__truediv__},


        {Py_nb_negative, (void*)I32Vector3__neg__},

    {Py_nb_absolute, (void*)I32Vector3__abs__},
    {Py_nb_bool, (void*)I32Vector3__bool__},
    {Py_bf_getbuffer, (void*)I32Vector3_getbufferproc},
    {Py_tp_getset, (void*)I32Vector3_PyGetSetDef},
    {Py_tp_getattro, (void*)I32Vector3__getattr__},
    {Py_tp_members, (void*)I32Vector3_PyMemberDef},
    {Py_tp_methods, (void*)I32Vector3_PyMethodDef},
    {0, 0},
};


static PyType_Spec I32Vector3_PyTypeSpec = {
    "gamut.math.I32Vector3",
    sizeof(I32Vector3),
    0,
    Py_TPFLAGS_DEFAULT,
    I32Vector3_PyType_Slots
};


static PyTypeObject *
define_I32Vector3_type(PyObject *module)
{
    PyTypeObject *type = (PyTypeObject *)PyType_FromModuleAndSpec(
        module,
        &I32Vector3_PyTypeSpec,
        0
    );
    if (!type){ return 0; }
    // Note:
    // Unlike other functions that steal references, PyModule_AddObject() only
    // decrements the reference count of value on success.
    if (PyModule_AddObject(module, "I32Vector3", (PyObject *)type) < 0)
    {
        Py_DECREF(type);
        return 0;
    }
    return type;
}




static PyObject *
I32Vector3Array__new__(PyTypeObject *cls, PyObject *args, PyObject *kwds)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto element_cls = module_state->I32Vector3_PyTypeObject;

    if (kwds && PyDict_Size(kwds) != 0)
    {
        PyErr_SetString(
            PyExc_TypeError,
            "I32Vector3 does accept any keyword arguments"
        );
        return 0;
    }

    auto arg_count = PyTuple_GET_SIZE(args);
    if (arg_count == 0)
    {
        auto self = (I32Vector3Array *)cls->tp_alloc(cls, 0);
        if (!self){ return 0; }
        self->length = 0;
        self->glm = 0;
        return (PyObject *)self;
    }

    auto *self = (I32Vector3Array *)cls->tp_alloc(cls, 0);
    if (!self){ return 0; }
    self->length = arg_count;
    self->glm = new I32Vector3Glm[arg_count];

    for (int i = 0; i < arg_count; i++)
    {
        auto arg = PyTuple_GET_ITEM(args, i);
        if (Py_TYPE(arg) == element_cls)
        {
            self->glm[i] = *(((I32Vector3*)arg)->glm);
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
I32Vector3Array__dealloc__(I32Vector3Array *self)
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
I32Vector3Array__hash__(I32Vector3Array *self)
{
    Py_ssize_t len = self->length * 3;
    Py_uhash_t acc = _HASH_XXPRIME_5;
    for (Py_ssize_t i = 0; i < (Py_ssize_t)self->length; i++)
    {
        for (I32Vector3Glm::length_type j = 0; j < 3; j++)
        {
            Py_uhash_t lane = std::hash<int32_t>{}(self->glm[i][j]);
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
I32Vector3Array__repr__(I32Vector3Array *self)
{
    return PyUnicode_FromFormat("I32Vector3Array[%zu]", self->length);
}


static Py_ssize_t
I32Vector3Array__len__(I32Vector3Array *self)
{
    return self->length;
}


static PyObject *
I32Vector3Array__sq_getitem__(I32Vector3Array *self, Py_ssize_t index)
{
    if (index < 0 || index > (Py_ssize_t)self->length - 1)
    {
        PyErr_Format(PyExc_IndexError, "index out of range");
        return 0;
    }

    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto element_cls = module_state->I32Vector3_PyTypeObject;

    I32Vector3 *result = (I32Vector3 *)element_cls->tp_alloc(element_cls, 0);
    if (!result){ return 0; }
    result->glm = new I32Vector3Glm(self->glm[index]);

    return (PyObject *)result;
}


static PyObject *
I32Vector3Array__mp_getitem__(I32Vector3Array *self, PyObject *key)
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
        auto *result = (I32Vector3Array *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        if (length == 0)
        {
            result->length = 0;
            result->glm = 0;
        }
        else
        {
            result->length = length;
            result->glm = new I32Vector3Glm[length];
            for (I32Vector3Glm::length_type i = 0; i < length; i++)
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
        auto element_cls = module_state->I32Vector3_PyTypeObject;

        I32Vector3 *result = (I32Vector3 *)element_cls->tp_alloc(element_cls, 0);
        if (!result){ return 0; }
        result->glm = new I32Vector3Glm(self->glm[index]);

        return (PyObject *)result;
    }
    PyErr_Format(PyExc_TypeError, "expected int or slice");
    return 0;
}


static PyObject *
I32Vector3Array__richcmp__(
    I32Vector3Array *self,
    I32Vector3Array *other,
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
I32Vector3Array__bool__(I32Vector3Array *self)
{
    return self->length ? 1 : 0;
}


static int
I32Vector3Array_getbufferproc(I32Vector3Array *self, Py_buffer *view, int flags)
{
    if (flags & PyBUF_WRITABLE)
    {
        PyErr_SetString(PyExc_BufferError, "I32Vector3 is read only");
        view->obj = 0;
        return -1;
    }

        if ((!(flags & PyBUF_C_CONTIGUOUS)) && flags & PyBUF_F_CONTIGUOUS)
        {
            PyErr_SetString(PyExc_BufferError, "I32Vector3 cannot be made Fortran contiguous");
            view->obj = 0;
            return -1;
        }

    view->buf = self->glm;
    view->obj = (PyObject *)self;
    view->len = sizeof(int32_t) * 3 * self->length;
    view->readonly = 1;
    view->itemsize = sizeof(int32_t);
    view->ndim = 2;
    if (flags & PyBUF_FORMAT)
    {
        view->format = "=i";
    }
    else
    {
        view->format = 0;
    }
    if (flags & PyBUF_ND)
    {
        view->shape = new Py_ssize_t[2] {
            (Py_ssize_t)self->length,
            3
        };
    }
    else
    {
        view->shape = 0;
    }
    if (flags & PyBUF_STRIDES)
    {
        static Py_ssize_t strides[] = {
            sizeof(int32_t) * 3,
            sizeof(int32_t)
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
I32Vector3Array_releasebufferproc(I32Vector3Array *self, Py_buffer *view)
{
    delete view->shape;
}


static PyMemberDef I32Vector3Array_PyMemberDef[] = {
    {"__weaklistoffset__", T_PYSSIZET, offsetof(I32Vector3Array, weakreflist), READONLY},
    {0}
};


static PyObject *
I32Vector3Array_pointer(I32Vector3Array *self, void *)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto c_p = module_state->ctypes_c_int32_t_p;
    return PyObject_CallMethod(c_p, "from_address", "n", (Py_ssize_t)&self->glm);
}


static PyObject *
I32Vector3Array_size(I32Vector3Array *self, void *)
{
    return PyLong_FromSize_t(sizeof(int32_t) * 3 * self->length);
}


static PyGetSetDef I32Vector3Array_PyGetSetDef[] = {
    {"pointer", (getter)I32Vector3Array_pointer, 0, 0, 0},
    {"size", (getter)I32Vector3Array_size, 0, 0, 0},
    {0, 0, 0, 0, 0}
};


static PyObject *
I32Vector3Array_from_buffer(PyTypeObject *cls, PyObject *buffer)
{
    static Py_ssize_t expected_size = sizeof(int32_t);
    Py_buffer view;
    if (PyObject_GetBuffer(buffer, &view, PyBUF_SIMPLE) == -1){ return 0; }
    auto view_length = view.len;
    if (view_length % (sizeof(int32_t) * 3))
    {
        PyBuffer_Release(&view);
        PyErr_Format(PyExc_BufferError, "expected buffer evenly divisible by %zd, got %zd", sizeof(int32_t), view_length);
        return 0;
    }
    auto array_length = view_length / (sizeof(int32_t) * 3);

    auto *result = (I32Vector3Array *)cls->tp_alloc(cls, 0);
    if (!result)
    {
        PyBuffer_Release(&view);
        return 0;
    }
    result->length = array_length;
    if (array_length > 0)
    {
        result->glm = new I32Vector3Glm[array_length];
        std::memcpy(result->glm, view.buf, view_length);
    }
    else
    {
        result->glm = 0;
    }
    PyBuffer_Release(&view);
    return (PyObject *)result;
}


static PyMethodDef I32Vector3Array_PyMethodDef[] = {
    {"from_buffer", (PyCFunction)I32Vector3Array_from_buffer, METH_O | METH_CLASS, 0},
    {0, 0, 0, 0}
};


static PyType_Slot I32Vector3Array_PyType_Slots [] = {
    {Py_tp_new, (void*)I32Vector3Array__new__},
    {Py_tp_dealloc, (void*)I32Vector3Array__dealloc__},
    {Py_tp_hash, (void*)I32Vector3Array__hash__},
    {Py_tp_repr, (void*)I32Vector3Array__repr__},
    {Py_sq_length, (void*)I32Vector3Array__len__},
    {Py_sq_item, (void*)I32Vector3Array__sq_getitem__},
    {Py_mp_subscript, (void*)I32Vector3Array__mp_getitem__},
    {Py_tp_richcompare, (void*)I32Vector3Array__richcmp__},
    {Py_nb_bool, (void*)I32Vector3Array__bool__},
    {Py_bf_getbuffer, (void*)I32Vector3Array_getbufferproc},
    {Py_bf_releasebuffer, (void*)I32Vector3Array_releasebufferproc},
    {Py_tp_getset, (void*)I32Vector3Array_PyGetSetDef},
    {Py_tp_members, (void*)I32Vector3Array_PyMemberDef},
    {Py_tp_methods, (void*)I32Vector3Array_PyMethodDef},
    {0, 0},
};


static PyType_Spec I32Vector3Array_PyTypeSpec = {
    "gamut.math.I32Vector3Array",
    sizeof(I32Vector3Array),
    0,
    Py_TPFLAGS_DEFAULT,
    I32Vector3Array_PyType_Slots
};


static PyTypeObject *
define_I32Vector3Array_type(PyObject *module)
{
    PyTypeObject *type = (PyTypeObject *)PyType_FromModuleAndSpec(
        module,
        &I32Vector3Array_PyTypeSpec,
        0
    );
    if (!type){ return 0; }
    // Note:
    // Unlike other functions that steal references, PyModule_AddObject() only
    // decrements the reference count of value on success.
    if (PyModule_AddObject(module, "I32Vector3Array", (PyObject *)type) < 0)
    {
        Py_DECREF(type);
        return 0;
    }
    return type;
}


static PyTypeObject *
get_I32Vector3_type()
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    return module_state->I32Vector3_PyTypeObject;
}


static PyTypeObject *
get_I32Vector3Array_type()
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    return module_state->I32Vector3Array_PyTypeObject;
}


static PyObject *
create_I32Vector3(const int32_t *value)
{
    auto cls = get_I32Vector3_type();
    auto result = (I32Vector3 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new I32Vector3Glm(*(I32Vector3Glm *)value);
    return (PyObject *)result;
}


static PyObject *
create_I32Vector3Array(size_t length, const int32_t *value)
{
    auto cls = get_I32Vector3Array_type();
    auto result = (I32Vector3Array *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->length = length;
    if (length > 0)
    {
        result->glm = new I32Vector3Glm[length];
        for (size_t i = 0; i < length; i++)
        {
            result->glm[i] = ((I32Vector3Glm *)value)[i];
        }
    }
    else
    {
        result->glm = 0;
    }
    return (PyObject *)result;
}


static int32_t *
get_I32Vector3_value_ptr(const PyObject *self)
{
    if (Py_TYPE(self) != get_I32Vector3_type())
    {
        PyErr_Format(PyExc_TypeError, "expected I32Vector3, got %R", self);
        return 0;
    }
    return (int32_t *)((I32Vector3 *)self)->glm;
}


static int32_t *
get_I32Vector3Array_value_ptr(const PyObject *self)
{
    if (Py_TYPE(self) != get_I32Vector3Array_type())
    {
        PyErr_Format(
            PyExc_TypeError,
            "expected I32Vector3Array, got %R",
            self
        );
        return 0;
    }
    return (int32_t *)((I32Vector3Array *)self)->glm;
}


static size_t
get_I32Vector3Array_length(const PyObject *self)
{
    if (Py_TYPE(self) != get_I32Vector3Array_type())
    {
        PyErr_Format(
            PyExc_TypeError,
            "expected I32Vector3Array, got %R",
            self
        );
        return 0;
    }
    return ((I32Vector3Array *)self)->length;
}

#endif