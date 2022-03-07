// generated 2022-03-07 23:13:00.201095 from codegen/math/templates/_vector.hpp

#include <stdio.h>
#include <iostream>

// stdlib
#include <limits>
// python
#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <structmember.h>
// glm
#include <glm/glm.hpp>
#include <glm/ext.hpp>
// gamut
#include "_type.hpp"

typedef glm::vec<2, unsigned int, glm::defaultp> UVector2Glm;


struct UVector2
{
    PyObject_HEAD
    PyObject *weakreflist;
    UVector2Glm *glm;
};


static PyObject *
UVector2__new__(PyTypeObject *cls, PyObject *args, PyObject *kwds)
{

        unsigned int c_0 = 0;

        unsigned int c_1 = 0;


    if (kwds && PyDict_Size(kwds) != 0)
    {
        PyErr_SetString(
            PyExc_TypeError,
            "UVector2 does accept any keyword arguments"
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
            unsigned int arg_c = pyobject_to_c_unsigned_int(arg);
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
                c_0 = pyobject_to_c_unsigned_int(arg);
                auto error_occurred = PyErr_Occurred();
                if (error_occurred){ return 0; }
            }

            {
                auto arg = PyTuple_GET_ITEM(args, 1);
                c_1 = pyobject_to_c_unsigned_int(arg);
                auto error_occurred = PyErr_Occurred();
                if (error_occurred){ return 0; }
            }

            break;
        }
        default:
        {
            PyErr_Format(
                PyExc_TypeError,
                "invalid number of arguments supplied to UVector2, expected "
                "0, 1 or 2 (got %zd)",
                arg_count
            );
            return 0;
        }
    }

    UVector2 *self = (UVector2*)cls->tp_alloc(cls, 0);
    if (!self){ return 0; }
    self->glm = new UVector2Glm(

            c_0,

            c_1

    );

    return (PyObject *)self;
}


static void
UVector2__dealloc__(UVector2 *self)
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
UVector2__hash__(UVector2 *self)
{
    Py_ssize_t i, len = 2;
    Py_uhash_t acc = _HASH_XXPRIME_5;
    for (i = 0; i < len; i++)
    {
        Py_uhash_t lane = std::hash<unsigned int>{}((*self->glm)[i]);
        if (lane == (Py_uhash_t)-1)
        {
            return -1;
        }
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
UVector2__repr__(UVector2 *self)
{
    PyObject *result = 0;

        PyObject *py_0 = 0;

        PyObject *py_1 = 0;



        py_0 = c_unsigned_int_to_pyobject((*self->glm)[0]);
        if (!py_0){ goto cleanup; }

        py_1 = c_unsigned_int_to_pyobject((*self->glm)[1]);
        if (!py_1){ goto cleanup; }

    result = PyUnicode_FromFormat(
        "UVector2("

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
UVector2__len__(UVector2 *self)
{
    return 2;
}


static PyObject *
UVector2__getitem__(UVector2 *self, Py_ssize_t index)
{
    if (index < 0 || index > 1)
    {
        PyErr_Format(PyExc_IndexError, "index out of range");
        return 0;
    }
    auto c = (*self->glm)[index];
    return c_unsigned_int_to_pyobject(c);
}


static PyObject *
UVector2__richcmp__(UVector2 *self, UVector2 *other, int op)
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
UVector2__add__(UVector2 *self, PyObject *other)
{
    auto cls = Py_TYPE(self);
    UVector2Glm vector;
    if (Py_TYPE(other) != cls)
    {
        auto c_other = pyobject_to_c_unsigned_int(other);
        if (PyErr_Occurred()){ Py_RETURN_NOTIMPLEMENTED; }
        vector = (*self->glm) + c_other;
    }
    else
    {
        vector = (*self->glm) + (*((UVector2 *)other)->glm);
    }

    UVector2 *result = (UVector2 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new UVector2Glm(

            vector[0],

            vector[1]

    );

    return (PyObject *)result;
}


static PyObject *
UVector2__sub__(UVector2 *self, PyObject *other)
{
    auto cls = Py_TYPE(self);
    UVector2Glm vector;
    if (Py_TYPE(other) != cls)
    {
        auto c_other = pyobject_to_c_unsigned_int(other);
        if (PyErr_Occurred()){ Py_RETURN_NOTIMPLEMENTED; }
        vector = (*self->glm) - c_other;
    }
    else
    {
        vector = (*self->glm) - (*((UVector2 *)other)->glm);
    }

    UVector2 *result = (UVector2 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new UVector2Glm(

            vector[0],

            vector[1]

    );

    return (PyObject *)result;
}


static PyObject *
UVector2__mul__(UVector2 *self, PyObject *other)
{
    auto cls = Py_TYPE(self);
    UVector2Glm vector;
    if (Py_TYPE(other) != cls)
    {
        auto c_other = pyobject_to_c_unsigned_int(other);
        if (PyErr_Occurred()){ Py_RETURN_NOTIMPLEMENTED; }
        vector = (*self->glm) * c_other;
    }
    else
    {
        vector = (*self->glm) * (*((UVector2 *)other)->glm);
    }

    UVector2 *result = (UVector2 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new UVector2Glm(

            vector[0],

            vector[1]

    );

    return (PyObject *)result;
}






    static PyObject *
    UVector2__truediv__(UVector2 *self, PyObject *other)
    {
        auto cls = Py_TYPE(self);
        UVector2Glm vector;
        if (Py_TYPE(other) != cls)
        {
            auto c_other = pyobject_to_c_unsigned_int(other);
            if (PyErr_Occurred()){ Py_RETURN_NOTIMPLEMENTED; }

                if (c_other == 0)
                {
                    PyErr_SetString(PyExc_ZeroDivisionError, "divide by zero");
                    return 0;
                }

            vector = (*self->glm) / c_other;
        }
        else
        {

                if (

                        (*((UVector2 *)other)->glm)[0] == 0 ||

                        (*((UVector2 *)other)->glm)[1] == 0

                )
                {
                    PyErr_SetString(PyExc_ZeroDivisionError, "divide by zero");
                    return 0;
                }

            vector = (*self->glm) / (*((UVector2 *)other)->glm);
        }

        UVector2 *result = (UVector2 *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new UVector2Glm(

                vector[0],

                vector[1]

        );

        return (PyObject *)result;
    }






static PyObject *
UVector2__abs__(UVector2 *self)
{
    auto cls = Py_TYPE(self);
    UVector2Glm vector = glm::abs(*self->glm);

    UVector2 *result = (UVector2 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new UVector2Glm(

            vector[0],

            vector[1]

    );

    return (PyObject *)result;
}


static int
UVector2__bool__(UVector2 *self)
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
UVector2_getbufferproc(UVector2 *self, Py_buffer *view, int flags)
{
    if (flags & PyBUF_WRITABLE)
    {
        PyErr_SetString(PyExc_TypeError, "UVector2 is not read only");
        view->obj = 0;
        return -1;
    }
    view->buf = glm::value_ptr(*self->glm);
    view->obj = (PyObject *)self;
    view->len = sizeof(unsigned int) * 2;
    view->readonly = 1;
    view->itemsize = sizeof(unsigned int);
    view->format = "I";
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
    UVector2_Getter_0(UVector2 *self, void *)
    {
        auto c = (*self->glm)[0];
        return c_unsigned_int_to_pyobject(c);
    }

    static PyObject *
    UVector2_Getter_1(UVector2 *self, void *)
    {
        auto c = (*self->glm)[1];
        return c_unsigned_int_to_pyobject(c);
    }






static PyGetSetDef UVector2_PyGetSetDef[] = {
    {"x", (getter)UVector2_Getter_0, 0, 0, 0},
    {"r", (getter)UVector2_Getter_0, 0, 0, 0},
    {"s", (getter)UVector2_Getter_0, 0, 0, 0},
    {"u", (getter)UVector2_Getter_0, 0, 0, 0},

        {"y", (getter)UVector2_Getter_1, 0, 0, 0},
        {"g", (getter)UVector2_Getter_1, 0, 0, 0},
        {"t", (getter)UVector2_Getter_1, 0, 0, 0},
        {"v", (getter)UVector2_Getter_1, 0, 0, 0},




    {0, 0, 0, 0, 0}
};


static PyObject *
UVector2__getattr__(UVector2 *self, PyObject *py_attr)
{
    PyObject *result = PyObject_GenericGetAttr((PyObject *)self, py_attr);
    if (result != 0){ return result; }

    auto attr_length = PyUnicode_GET_LENGTH(py_attr);
    if (attr_length == 1){ return 0; }

    result = PyTuple_New(attr_length);
    if (!result){ return 0; }

    const char *attr = PyUnicode_AsUTF8(py_attr);
    if (!attr){ return 0; }
    for (size_t i = 0; i < attr_length; i++)
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
                Py_DECREF(result);
                return 0;
            }
        }
        auto py_c = c_unsigned_int_to_pyobject((*self->glm)[glm_index]);
        PyTuple_SET_ITEM(result, i, py_c);
    }

    PyErr_Clear();
    return result;
}


static PyMemberDef UVector2_PyMemberDef[] = {
    {"__weaklistoffset__", T_PYSSIZET, offsetof(UVector2, weakreflist), READONLY},
    {0}
};





static PyObject *
UVector2_get_limits(UVector2 *self, void *)
{
    auto c_min = std::numeric_limits<unsigned int>::min();
    auto c_max = std::numeric_limits<unsigned int>::max();
    auto py_min = c_unsigned_int_to_pyobject(c_min);
    if (!py_min){ return 0; }
    auto py_max = c_unsigned_int_to_pyobject(c_max);
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


static PyMethodDef UVector2_PyMethodDef[] = {

    {"get_limits", (PyCFunction)UVector2_get_limits, METH_NOARGS | METH_STATIC, 0},
    {0, 0, 0, 0}
};


static PyType_Slot UVector2_PyType_Slots [] = {
    {Py_tp_new, (void*)UVector2__new__},
    {Py_tp_dealloc, (void*)UVector2__dealloc__},
    {Py_tp_hash, (void*)UVector2__hash__},
    {Py_tp_repr, (void*)UVector2__repr__},
    {Py_sq_length, (void*)UVector2__len__},
    {Py_sq_item, (void*)UVector2__getitem__},
    {Py_tp_richcompare, (void*)UVector2__richcmp__},
    {Py_nb_add, (void*)UVector2__add__},
    {Py_nb_subtract, (void*)UVector2__sub__},
    {Py_nb_multiply, (void*)UVector2__mul__},


        {Py_nb_true_divide, (void*)UVector2__truediv__},


    {Py_nb_absolute, (void*)UVector2__abs__},
    {Py_nb_bool, (void*)UVector2__bool__},
    {Py_bf_getbuffer, (void*)UVector2_getbufferproc},
    {Py_tp_getset, (void*)UVector2_PyGetSetDef},
    {Py_tp_getattro, (void*)UVector2__getattr__},
    {Py_tp_members, (void*)UVector2_PyMemberDef},
    {Py_tp_methods, (void*)UVector2_PyMethodDef},
    {0, 0},
};


static PyType_Spec UVector2_PyTypeSpec = {
    "gamut.math.UVector2",
    sizeof(UVector2),
    0,
    Py_TPFLAGS_DEFAULT,
    UVector2_PyType_Slots
};


static PyTypeObject *
define_UVector2_type(PyObject *module)
{
    PyTypeObject *type = (PyTypeObject *)PyType_FromModuleAndSpec(
        module,
        &UVector2_PyTypeSpec,
        0
    );
    if (!type){ return 0; }
    // Note:
    // Unlike other functions that steal references, PyModule_AddObject() only
    // decrements the reference count of value on success.
    if (PyModule_AddObject(module, "UVector2", (PyObject *)type) < 0)
    {
        Py_DECREF(type);
        return 0;
    }
    return type;
}