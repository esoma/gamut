// generated 2022-03-07 23:13:00.217095 from codegen/math/templates/_vector.hpp

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

typedef glm::vec<4, unsigned int, glm::defaultp> UVector4Glm;


struct UVector4
{
    PyObject_HEAD
    PyObject *weakreflist;
    UVector4Glm *glm;
};


static PyObject *
UVector4__new__(PyTypeObject *cls, PyObject *args, PyObject *kwds)
{

        unsigned int c_0 = 0;

        unsigned int c_1 = 0;

        unsigned int c_2 = 0;

        unsigned int c_3 = 0;


    if (kwds && PyDict_Size(kwds) != 0)
    {
        PyErr_SetString(
            PyExc_TypeError,
            "UVector4 does accept any keyword arguments"
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

                c_2 = arg_c;

                c_3 = arg_c;

            break;
        }
        case 4:
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

            {
                auto arg = PyTuple_GET_ITEM(args, 2);
                c_2 = pyobject_to_c_unsigned_int(arg);
                auto error_occurred = PyErr_Occurred();
                if (error_occurred){ return 0; }
            }

            {
                auto arg = PyTuple_GET_ITEM(args, 3);
                c_3 = pyobject_to_c_unsigned_int(arg);
                auto error_occurred = PyErr_Occurred();
                if (error_occurred){ return 0; }
            }

            break;
        }
        default:
        {
            PyErr_Format(
                PyExc_TypeError,
                "invalid number of arguments supplied to UVector4, expected "
                "0, 1 or 4 (got %zd)",
                arg_count
            );
            return 0;
        }
    }

    UVector4 *self = (UVector4*)cls->tp_alloc(cls, 0);
    if (!self){ return 0; }
    self->glm = new UVector4Glm(

            c_0,

            c_1,

            c_2,

            c_3

    );

    return (PyObject *)self;
}


static void
UVector4__dealloc__(UVector4 *self)
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
UVector4__hash__(UVector4 *self)
{
    Py_ssize_t i, len = 4;
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
UVector4__repr__(UVector4 *self)
{
    PyObject *result = 0;

        PyObject *py_0 = 0;

        PyObject *py_1 = 0;

        PyObject *py_2 = 0;

        PyObject *py_3 = 0;



        py_0 = c_unsigned_int_to_pyobject((*self->glm)[0]);
        if (!py_0){ goto cleanup; }

        py_1 = c_unsigned_int_to_pyobject((*self->glm)[1]);
        if (!py_1){ goto cleanup; }

        py_2 = c_unsigned_int_to_pyobject((*self->glm)[2]);
        if (!py_2){ goto cleanup; }

        py_3 = c_unsigned_int_to_pyobject((*self->glm)[3]);
        if (!py_3){ goto cleanup; }

    result = PyUnicode_FromFormat(
        "UVector4("

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
UVector4__len__(UVector4 *self)
{
    return 4;
}


static PyObject *
UVector4__getitem__(UVector4 *self, Py_ssize_t index)
{
    if (index < 0 || index > 3)
    {
        PyErr_Format(PyExc_IndexError, "index out of range");
        return 0;
    }
    auto c = (*self->glm)[index];
    return c_unsigned_int_to_pyobject(c);
}


static PyObject *
UVector4__richcmp__(UVector4 *self, UVector4 *other, int op)
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
UVector4__add__(UVector4 *self, PyObject *other)
{
    auto cls = Py_TYPE(self);
    UVector4Glm vector;
    if (Py_TYPE(other) != cls)
    {
        auto c_other = pyobject_to_c_unsigned_int(other);
        if (PyErr_Occurred()){ Py_RETURN_NOTIMPLEMENTED; }
        vector = (*self->glm) + c_other;
    }
    else
    {
        vector = (*self->glm) + (*((UVector4 *)other)->glm);
    }

    UVector4 *result = (UVector4 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new UVector4Glm(

            vector[0],

            vector[1],

            vector[2],

            vector[3]

    );

    return (PyObject *)result;
}


static PyObject *
UVector4__sub__(UVector4 *self, PyObject *other)
{
    auto cls = Py_TYPE(self);
    UVector4Glm vector;
    if (Py_TYPE(other) != cls)
    {
        auto c_other = pyobject_to_c_unsigned_int(other);
        if (PyErr_Occurred()){ Py_RETURN_NOTIMPLEMENTED; }
        vector = (*self->glm) - c_other;
    }
    else
    {
        vector = (*self->glm) - (*((UVector4 *)other)->glm);
    }

    UVector4 *result = (UVector4 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new UVector4Glm(

            vector[0],

            vector[1],

            vector[2],

            vector[3]

    );

    return (PyObject *)result;
}


static PyObject *
UVector4__mul__(UVector4 *self, PyObject *other)
{
    auto cls = Py_TYPE(self);
    UVector4Glm vector;
    if (Py_TYPE(other) != cls)
    {
        auto c_other = pyobject_to_c_unsigned_int(other);
        if (PyErr_Occurred()){ Py_RETURN_NOTIMPLEMENTED; }
        vector = (*self->glm) * c_other;
    }
    else
    {
        vector = (*self->glm) * (*((UVector4 *)other)->glm);
    }

    UVector4 *result = (UVector4 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new UVector4Glm(

            vector[0],

            vector[1],

            vector[2],

            vector[3]

    );

    return (PyObject *)result;
}






    static PyObject *
    UVector4__truediv__(UVector4 *self, PyObject *other)
    {
        auto cls = Py_TYPE(self);
        UVector4Glm vector;
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

                        (*((UVector4 *)other)->glm)[0] == 0 ||

                        (*((UVector4 *)other)->glm)[1] == 0 ||

                        (*((UVector4 *)other)->glm)[2] == 0 ||

                        (*((UVector4 *)other)->glm)[3] == 0

                )
                {
                    PyErr_SetString(PyExc_ZeroDivisionError, "divide by zero");
                    return 0;
                }

            vector = (*self->glm) / (*((UVector4 *)other)->glm);
        }

        UVector4 *result = (UVector4 *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new UVector4Glm(

                vector[0],

                vector[1],

                vector[2],

                vector[3]

        );

        return (PyObject *)result;
    }






static PyObject *
UVector4__abs__(UVector4 *self)
{
    auto cls = Py_TYPE(self);
    UVector4Glm vector = glm::abs(*self->glm);

    UVector4 *result = (UVector4 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new UVector4Glm(

            vector[0],

            vector[1],

            vector[2],

            vector[3]

    );

    return (PyObject *)result;
}


static int
UVector4__bool__(UVector4 *self)
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
UVector4_getbufferproc(UVector4 *self, Py_buffer *view, int flags)
{
    if (flags & PyBUF_WRITABLE)
    {
        PyErr_SetString(PyExc_TypeError, "UVector4 is not read only");
        view->obj = 0;
        return -1;
    }
    view->buf = glm::value_ptr(*self->glm);
    view->obj = (PyObject *)self;
    view->len = sizeof(unsigned int) * 4;
    view->readonly = 1;
    view->itemsize = sizeof(unsigned int);
    view->format = "I";
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
    UVector4_Getter_0(UVector4 *self, void *)
    {
        auto c = (*self->glm)[0];
        return c_unsigned_int_to_pyobject(c);
    }

    static PyObject *
    UVector4_Getter_1(UVector4 *self, void *)
    {
        auto c = (*self->glm)[1];
        return c_unsigned_int_to_pyobject(c);
    }

    static PyObject *
    UVector4_Getter_2(UVector4 *self, void *)
    {
        auto c = (*self->glm)[2];
        return c_unsigned_int_to_pyobject(c);
    }

    static PyObject *
    UVector4_Getter_3(UVector4 *self, void *)
    {
        auto c = (*self->glm)[3];
        return c_unsigned_int_to_pyobject(c);
    }






static PyGetSetDef UVector4_PyGetSetDef[] = {
    {"x", (getter)UVector4_Getter_0, 0, 0, 0},
    {"r", (getter)UVector4_Getter_0, 0, 0, 0},
    {"s", (getter)UVector4_Getter_0, 0, 0, 0},
    {"u", (getter)UVector4_Getter_0, 0, 0, 0},

        {"y", (getter)UVector4_Getter_1, 0, 0, 0},
        {"g", (getter)UVector4_Getter_1, 0, 0, 0},
        {"t", (getter)UVector4_Getter_1, 0, 0, 0},
        {"v", (getter)UVector4_Getter_1, 0, 0, 0},


        {"z", (getter)UVector4_Getter_2, 0, 0, 0},
        {"b", (getter)UVector4_Getter_2, 0, 0, 0},
        {"p", (getter)UVector4_Getter_2, 0, 0, 0},


        {"w", (getter)UVector4_Getter_3, 0, 0, 0},
        {"a", (getter)UVector4_Getter_3, 0, 0, 0},
        {"q", (getter)UVector4_Getter_3, 0, 0, 0},


    {0, 0, 0, 0, 0}
};


static PyObject *
UVector4__getattr__(UVector4 *self, PyObject *py_attr)
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


static PyMemberDef UVector4_PyMemberDef[] = {
    {"__weaklistoffset__", T_PYSSIZET, offsetof(UVector4, weakreflist), READONLY},
    {0}
};





static PyObject *
UVector4_get_limits(UVector4 *self, void *)
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


static PyMethodDef UVector4_PyMethodDef[] = {

    {"get_limits", (PyCFunction)UVector4_get_limits, METH_NOARGS | METH_STATIC, 0},
    {0, 0, 0, 0}
};


static PyType_Slot UVector4_PyType_Slots [] = {
    {Py_tp_new, (void*)UVector4__new__},
    {Py_tp_dealloc, (void*)UVector4__dealloc__},
    {Py_tp_hash, (void*)UVector4__hash__},
    {Py_tp_repr, (void*)UVector4__repr__},
    {Py_sq_length, (void*)UVector4__len__},
    {Py_sq_item, (void*)UVector4__getitem__},
    {Py_tp_richcompare, (void*)UVector4__richcmp__},
    {Py_nb_add, (void*)UVector4__add__},
    {Py_nb_subtract, (void*)UVector4__sub__},
    {Py_nb_multiply, (void*)UVector4__mul__},


        {Py_nb_true_divide, (void*)UVector4__truediv__},


    {Py_nb_absolute, (void*)UVector4__abs__},
    {Py_nb_bool, (void*)UVector4__bool__},
    {Py_bf_getbuffer, (void*)UVector4_getbufferproc},
    {Py_tp_getset, (void*)UVector4_PyGetSetDef},
    {Py_tp_getattro, (void*)UVector4__getattr__},
    {Py_tp_members, (void*)UVector4_PyMemberDef},
    {Py_tp_methods, (void*)UVector4_PyMethodDef},
    {0, 0},
};


static PyType_Spec UVector4_PyTypeSpec = {
    "gamut.math.UVector4",
    sizeof(UVector4),
    0,
    Py_TPFLAGS_DEFAULT,
    UVector4_PyType_Slots
};


static PyTypeObject *
define_UVector4_type(PyObject *module)
{
    PyTypeObject *type = (PyTypeObject *)PyType_FromModuleAndSpec(
        module,
        &UVector4_PyTypeSpec,
        0
    );
    if (!type){ return 0; }
    // Note:
    // Unlike other functions that steal references, PyModule_AddObject() only
    // decrements the reference count of value on success.
    if (PyModule_AddObject(module, "UVector4", (PyObject *)type) < 0)
    {
        Py_DECREF(type);
        return 0;
    }
    return type;
}