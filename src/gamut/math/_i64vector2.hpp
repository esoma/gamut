
// generated 2022-03-10 23:24:28.417431 from codegen/math/templates/_vector.hpp

#ifndef GAMUT_MATH_I64VECTOR2_HPP
#define GAMUT_MATH_I64VECTOR2_HPP

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
I64Vector2__new__(PyTypeObject *cls, PyObject *args, PyObject *kwds)
{

        int64_t c_0 = 0;

        int64_t c_1 = 0;


    if (kwds && PyDict_Size(kwds) != 0)
    {
        PyErr_SetString(
            PyExc_TypeError,
            "I64Vector2 does accept any keyword arguments"
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
            int64_t arg_c = pyobject_to_c_int64_t(arg);
            auto error_occurred = PyErr_Occurred();
            if (error_occurred){ return 0; }

                c_0 = arg_c;

                c_1 = arg_c;

            break;
        }
        case 2:
        {

            {
                auto arg = PyTuple_GET_ITEM(args, 0);
                c_0 = pyobject_to_c_int64_t(arg);
                auto error_occurred = PyErr_Occurred();
                if (error_occurred){ return 0; }
            }

            {
                auto arg = PyTuple_GET_ITEM(args, 1);
                c_1 = pyobject_to_c_int64_t(arg);
                auto error_occurred = PyErr_Occurred();
                if (error_occurred){ return 0; }
            }

            break;
        }
        default:
        {
            PyErr_Format(
                PyExc_TypeError,
                "invalid number of arguments supplied to I64Vector2, expected "
                "0, 1 or 2 (got %zd)",
                arg_count
            );
            return 0;
        }
    }

    I64Vector2 *self = (I64Vector2*)cls->tp_alloc(cls, 0);
    if (!self){ return 0; }
    self->glm = new I64Vector2Glm(

            c_0,

            c_1

    );

    return (PyObject *)self;
}


static void
I64Vector2__dealloc__(I64Vector2 *self)
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
I64Vector2__hash__(I64Vector2 *self)
{
    Py_ssize_t len = 2;
    Py_uhash_t acc = _HASH_XXPRIME_5;
    for (I64Vector2Glm::length_type i = 0; i < len; i++)
    {
        Py_uhash_t lane = std::hash<int64_t>{}((*self->glm)[i]);
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
I64Vector2__repr__(I64Vector2 *self)
{
    PyObject *result = 0;

        PyObject *py_0 = 0;

        PyObject *py_1 = 0;



        py_0 = c_int64_t_to_pyobject((*self->glm)[0]);
        if (!py_0){ goto cleanup; }

        py_1 = c_int64_t_to_pyobject((*self->glm)[1]);
        if (!py_1){ goto cleanup; }

    result = PyUnicode_FromFormat(
        "I64Vector2("

            "%R, "

            "%R"

        ")",

            py_0,

            py_1

    );
cleanup:

        Py_XDECREF(py_0);

        Py_XDECREF(py_1);

    return result;
}


static Py_ssize_t
I64Vector2__len__(I64Vector2 *self)
{
    return 2;
}


static PyObject *
I64Vector2__getitem__(I64Vector2 *self, Py_ssize_t index)
{
    if (index < 0 || index > 1)
    {
        PyErr_Format(PyExc_IndexError, "index out of range");
        return 0;
    }
    auto c = (*self->glm)[(I64Vector2Glm::length_type)index];
    return c_int64_t_to_pyobject(c);
}


static PyObject *
I64Vector2__richcmp__(I64Vector2 *self, I64Vector2 *other, int op)
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
I64Vector2__add__(PyObject *left, PyObject *right)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->I64Vector2_PyTypeObject;

    I64Vector2Glm vector;
    if (Py_TYPE(left) == Py_TYPE(right))
    {
        vector = (*((I64Vector2 *)left)->glm) + (*((I64Vector2 *)right)->glm);
    }
    else
    {
        if (Py_TYPE(left) == cls)
        {
            auto c_right = pyobject_to_c_int64_t(right);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
            vector = (*((I64Vector2 *)left)->glm) + c_right;
        }
        else
        {
            auto c_left = pyobject_to_c_int64_t(left);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
            vector = c_left + (*((I64Vector2 *)right)->glm);
        }
    }

    I64Vector2 *result = (I64Vector2 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new I64Vector2Glm(

            vector[0],

            vector[1]

    );

    return (PyObject *)result;
}


static PyObject *
I64Vector2__sub__(PyObject *left, PyObject *right)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->I64Vector2_PyTypeObject;

    I64Vector2Glm vector;
    if (Py_TYPE(left) == Py_TYPE(right))
    {
        vector = (*((I64Vector2 *)left)->glm) - (*((I64Vector2 *)right)->glm);
    }
    else
    {
        if (Py_TYPE(left) == cls)
        {
            auto c_right = pyobject_to_c_int64_t(right);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
            vector = (*((I64Vector2 *)left)->glm) - c_right;
        }
        else
        {
            auto c_left = pyobject_to_c_int64_t(left);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
            vector = c_left - (*((I64Vector2 *)right)->glm);
        }
    }

    I64Vector2 *result = (I64Vector2 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new I64Vector2Glm(

            vector[0],

            vector[1]

    );

    return (PyObject *)result;
}


static PyObject *
I64Vector2__mul__(PyObject *left, PyObject *right)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->I64Vector2_PyTypeObject;

    I64Vector2Glm vector;
    if (Py_TYPE(left) == Py_TYPE(right))
    {
        vector = (*((I64Vector2 *)left)->glm) * (*((I64Vector2 *)right)->glm);
    }
    else
    {
        if (Py_TYPE(left) == cls)
        {
            auto c_right = pyobject_to_c_int64_t(right);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
            vector = (*((I64Vector2 *)left)->glm) * c_right;
        }
        else
        {
            auto c_left = pyobject_to_c_int64_t(left);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
            vector = c_left * (*((I64Vector2 *)right)->glm);
        }
    }

    I64Vector2 *result = (I64Vector2 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new I64Vector2Glm(

            vector[0],

            vector[1]

    );

    return (PyObject *)result;
}







    static PyObject *
    I64Vector2__truediv__(PyObject *left, PyObject *right)
    {
        auto module_state = get_module_state();
        if (!module_state){ return 0; }
        auto cls = module_state->I64Vector2_PyTypeObject;

        I64Vector2Glm vector;
        if (Py_TYPE(left) == Py_TYPE(right))
        {

                if (

                        (*((I64Vector2 *)right)->glm)[0] == 0 ||

                        (*((I64Vector2 *)right)->glm)[1] == 0

                )
                {
                    PyErr_SetString(PyExc_ZeroDivisionError, "divide by zero");
                    return 0;
                }

            vector = (*((I64Vector2 *)left)->glm) / (*((I64Vector2 *)right)->glm);
        }
        else
        {
            if (Py_TYPE(left) == cls)
            {
                auto c_right = pyobject_to_c_int64_t(right);
                if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }

                    if (c_right == 0)
                    {
                        PyErr_SetString(PyExc_ZeroDivisionError, "divide by zero");
                        return 0;
                    }

                vector = (*((I64Vector2 *)left)->glm) / c_right;
            }
            else
            {
                auto c_left = pyobject_to_c_int64_t(left);
                if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }

                    if (

                            (*((I64Vector2 *)right)->glm)[0] == 0 ||

                            (*((I64Vector2 *)right)->glm)[1] == 0

                    )
                    {
                        PyErr_SetString(PyExc_ZeroDivisionError, "divide by zero");
                        return 0;
                    }

                vector = c_left / (*((I64Vector2 *)right)->glm);
            }
        }

        I64Vector2 *result = (I64Vector2 *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new I64Vector2Glm(

                vector[0],

                vector[1]

        );

        return (PyObject *)result;
    }




    static PyObject *
    I64Vector2__neg__(I64Vector2 *self)
    {
        auto cls = Py_TYPE(self);

            I64Vector2Glm vector = -(*self->glm);


        I64Vector2 *result = (I64Vector2 *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new I64Vector2Glm(

                vector[0],

                vector[1]

        );

        return (PyObject *)result;
    }



static PyObject *
I64Vector2__abs__(I64Vector2 *self)
{
    auto cls = Py_TYPE(self);
    I64Vector2Glm vector = glm::abs(*self->glm);

    I64Vector2 *result = (I64Vector2 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new I64Vector2Glm(

            vector[0],

            vector[1]

    );

    return (PyObject *)result;
}


static int
I64Vector2__bool__(I64Vector2 *self)
{

        if ((*self->glm)[0] == 0)
        {
            return 0;
        }

        if ((*self->glm)[1] == 0)
        {
            return 0;
        }

    return 1;
}


static int
I64Vector2_getbufferproc(I64Vector2 *self, Py_buffer *view, int flags)
{
    if (flags & PyBUF_WRITABLE)
    {
        PyErr_SetString(PyExc_TypeError, "I64Vector2 is read only");
        view->obj = 0;
        return -1;
    }
    view->buf = glm::value_ptr(*self->glm);
    view->obj = (PyObject *)self;
    view->len = sizeof(int64_t) * 2;
    view->readonly = 1;
    view->itemsize = sizeof(int64_t);
    view->format = "=q";
    view->ndim = 1;
    static Py_ssize_t shape = 2;
    view->shape = &shape;
    view->strides = &view->itemsize;
    view->suboffsets = 0;
    view->internal = 0;
    Py_INCREF(self);
    return 0;
}



    static PyObject *
    I64Vector2_Getter_0(I64Vector2 *self, void *)
    {
        auto c = (*self->glm)[0];
        return c_int64_t_to_pyobject(c);
    }

    static PyObject *
    I64Vector2_Getter_1(I64Vector2 *self, void *)
    {
        auto c = (*self->glm)[1];
        return c_int64_t_to_pyobject(c);
    }






static PyGetSetDef I64Vector2_PyGetSetDef[] = {
    {"x", (getter)I64Vector2_Getter_0, 0, 0, 0},
    {"r", (getter)I64Vector2_Getter_0, 0, 0, 0},
    {"s", (getter)I64Vector2_Getter_0, 0, 0, 0},
    {"u", (getter)I64Vector2_Getter_0, 0, 0, 0},

        {"y", (getter)I64Vector2_Getter_1, 0, 0, 0},
        {"g", (getter)I64Vector2_Getter_1, 0, 0, 0},
        {"t", (getter)I64Vector2_Getter_1, 0, 0, 0},
        {"v", (getter)I64Vector2_Getter_1, 0, 0, 0},




    {0, 0, 0, 0, 0}
};



    static PyObject *
    swizzle_2_I64Vector2(I64Vector2 *self, PyObject *py_attr)
    {
        const char *attr = PyUnicode_AsUTF8(py_attr);
        if (!attr){ return 0; }

        I64Vector2Glm vec;
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
        auto cls = module_state->I64Vector2_PyTypeObject;

        I64Vector2 *result = (I64Vector2 *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new I64Vector2Glm(vec);

        return (PyObject *)result;
    }



    static PyObject *
    swizzle_3_I64Vector2(I64Vector2 *self, PyObject *py_attr)
    {
        const char *attr = PyUnicode_AsUTF8(py_attr);
        if (!attr){ return 0; }

        I64Vector3Glm vec;
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
        auto cls = module_state->I64Vector3_PyTypeObject;

        I64Vector3 *result = (I64Vector3 *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new I64Vector3Glm(vec);

        return (PyObject *)result;
    }



    static PyObject *
    swizzle_4_I64Vector2(I64Vector2 *self, PyObject *py_attr)
    {
        const char *attr = PyUnicode_AsUTF8(py_attr);
        if (!attr){ return 0; }

        I64Vector4Glm vec;
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
        auto cls = module_state->I64Vector4_PyTypeObject;

        I64Vector4 *result = (I64Vector4 *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new I64Vector4Glm(vec);

        return (PyObject *)result;
    }




static PyObject *
I64Vector2__getattr__(I64Vector2 *self, PyObject *py_attr)
{
    PyObject *result = PyObject_GenericGetAttr((PyObject *)self, py_attr);
    if (result != 0){ return result; }

    auto attr_length = PyUnicode_GET_LENGTH(py_attr);
    switch(attr_length)
    {
        case 2:
        {
            PyErr_Clear();
            return swizzle_2_I64Vector2(self, py_attr);
        }
        case 3:
        {
            PyErr_Clear();
            return swizzle_3_I64Vector2(self, py_attr);
        }
        case 4:
        {
            PyErr_Clear();
            return swizzle_4_I64Vector2(self, py_attr);
        }
    }
    return 0;
}


static PyMemberDef I64Vector2_PyMemberDef[] = {
    {"__weaklistoffset__", T_PYSSIZET, offsetof(I64Vector2, weakreflist), READONLY},
    {0}
};





static PyObject *
I64Vector2_get_limits(I64Vector2 *self, void *)
{
    auto c_min = std::numeric_limits<int64_t>::lowest();
    auto c_max = std::numeric_limits<int64_t>::max();
    auto py_min = c_int64_t_to_pyobject(c_min);
    if (!py_min){ return 0; }
    auto py_max = c_int64_t_to_pyobject(c_max);
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


static PyMethodDef I64Vector2_PyMethodDef[] = {

    {"get_limits", (PyCFunction)I64Vector2_get_limits, METH_NOARGS | METH_STATIC, 0},
    {0, 0, 0, 0}
};


static PyType_Slot I64Vector2_PyType_Slots [] = {
    {Py_tp_new, (void*)I64Vector2__new__},
    {Py_tp_dealloc, (void*)I64Vector2__dealloc__},
    {Py_tp_hash, (void*)I64Vector2__hash__},
    {Py_tp_repr, (void*)I64Vector2__repr__},
    {Py_sq_length, (void*)I64Vector2__len__},
    {Py_sq_item, (void*)I64Vector2__getitem__},
    {Py_tp_richcompare, (void*)I64Vector2__richcmp__},
    {Py_nb_add, (void*)I64Vector2__add__},
    {Py_nb_subtract, (void*)I64Vector2__sub__},
    {Py_nb_multiply, (void*)I64Vector2__mul__},


        {Py_nb_true_divide, (void*)I64Vector2__truediv__},


        {Py_nb_negative, (void*)I64Vector2__neg__},

    {Py_nb_absolute, (void*)I64Vector2__abs__},
    {Py_nb_bool, (void*)I64Vector2__bool__},
    {Py_bf_getbuffer, (void*)I64Vector2_getbufferproc},
    {Py_tp_getset, (void*)I64Vector2_PyGetSetDef},
    {Py_tp_getattro, (void*)I64Vector2__getattr__},
    {Py_tp_members, (void*)I64Vector2_PyMemberDef},
    {Py_tp_methods, (void*)I64Vector2_PyMethodDef},
    {0, 0},
};


static PyType_Spec I64Vector2_PyTypeSpec = {
    "gamut.math.I64Vector2",
    sizeof(I64Vector2),
    0,
    Py_TPFLAGS_DEFAULT,
    I64Vector2_PyType_Slots
};


static PyTypeObject *
define_I64Vector2_type(PyObject *module)
{
    PyTypeObject *type = (PyTypeObject *)PyType_FromModuleAndSpec(
        module,
        &I64Vector2_PyTypeSpec,
        0
    );
    if (!type){ return 0; }
    // Note:
    // Unlike other functions that steal references, PyModule_AddObject() only
    // decrements the reference count of value on success.
    if (PyModule_AddObject(module, "I64Vector2", (PyObject *)type) < 0)
    {
        Py_DECREF(type);
        return 0;
    }
    return type;
}


static I64Vector2 *
create_I64Vector2_from_glm(const I64Vector2Glm& glm)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->I64Vector2_PyTypeObject;

    I64Vector2 *result = (I64Vector2 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new I64Vector2Glm(glm);

    return result;
}

#endif