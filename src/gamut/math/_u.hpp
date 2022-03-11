
// generated 2022-03-11 18:37:26.837966 from codegen/math/templates/_pod.hpp

#ifndef GAMUT_MATH_U_HPP
#define GAMUT_MATH_U_HPP

// stdlib
#include <limits>
#include <functional>
// python
#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <structmember.h>
// gamut
#include "_modulestate.hpp"
#include "_podtype.hpp"
#include "_type.hpp"


static PyObject *
UArray__new__(PyTypeObject *cls, PyObject *args, PyObject *kwds)
{
    if (kwds && PyDict_Size(kwds) != 0)
    {
        PyErr_SetString(
            PyExc_TypeError,
            "U does accept any keyword arguments"
        );
        return 0;
    }

    auto arg_count = PyTuple_GET_SIZE(args);
    if (arg_count == 0)
    {
        auto self = (UArray *)cls->tp_alloc(cls, 0);
        if (!self){ return 0; }
        self->length = 0;
        self->pod = 0;
        return (PyObject *)self;
    }

    auto *self = (UArray *)cls->tp_alloc(cls, 0);
    if (!self){ return 0; }
    self->length = arg_count;
    self->pod = new unsigned int[arg_count];

    for (int i = 0; i < arg_count; i++)
    {
        auto arg = PyTuple_GET_ITEM(args, i);
        self->pod[i] = pyobject_to_c_unsigned_int(arg);
        if (PyErr_Occurred())
        {
            Py_DECREF(self);
            PyErr_Format(
                PyExc_TypeError,
                "invalid type %R, expected unsigned int",
                arg
            );
            return 0;
        }
    }

    return (PyObject *)self;
}


static void
UArray__dealloc__(UArray *self)
{
    if (self->weakreflist)
    {
        PyObject_ClearWeakRefs((PyObject *)self);
    }

    delete self->pod;

    PyTypeObject *type = Py_TYPE(self);
    type->tp_free(self);
    Py_DECREF(type);
}


static Py_hash_t
UArray__hash__(UArray *self)
{
    Py_ssize_t len = self->length;
    Py_uhash_t acc = _HASH_XXPRIME_5;
    for (Py_ssize_t i = 0; i < (Py_ssize_t)self->length; i++)
    {
        Py_uhash_t lane = std::hash<unsigned int>{}(self->pod[i]);
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
UArray__repr__(UArray *self)
{
    return PyUnicode_FromFormat("UArray[%zu]", self->length);
}


static Py_ssize_t
UArray__len__(UArray *self)
{
    return self->length;
}


static PyObject *
UArray__getitem__(UArray *self, Py_ssize_t index)
{
    if (index < 0 || index > (Py_ssize_t)self->length - 1)
    {
        PyErr_Format(PyExc_IndexError, "index out of range");
        return 0;
    }
    return c_unsigned_int_to_pyobject(self->pod[index]);
}


static PyObject *
UArray__richcmp__(
    UArray *self,
    UArray *other,
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
                    if (self->pod[i] != other->pod[i])
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
                    if (self->pod[i] != other->pod[i])
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
UArray__bool__(UArray *self)
{
    return self->length ? 1 : 0;
}


static int
UArray_getbufferproc(UArray *self, Py_buffer *view, int flags)
{
    if (flags & PyBUF_WRITABLE)
    {
        PyErr_SetString(PyExc_TypeError, "U is read only");
        view->obj = 0;
        return -1;
    }
    view->buf = self->pod;
    view->obj = (PyObject *)self;
    view->len = sizeof(unsigned int) * self->length;
    view->readonly = 1;
    view->itemsize = sizeof(unsigned int);
    view->format = "I";
    view->ndim = 1;
    view->shape = new Py_ssize_t[1] {
        (Py_ssize_t)self->length
    };
    view->strides = &view->itemsize;
    view->suboffsets = 0;
    view->internal = 0;
    Py_INCREF(self);
    return 0;
}


static void
UArray_releasebufferproc(UArray *self, Py_buffer *view)
{
    delete view->shape;
}


static PyMemberDef UArray_PyMemberDef[] = {
    {"__weaklistoffset__", T_PYSSIZET, offsetof(UArray, weakreflist), READONLY},
    {0}
};


static PyType_Slot UArray_PyType_Slots [] = {
    {Py_tp_new, (void*)UArray__new__},
    {Py_tp_dealloc, (void*)UArray__dealloc__},
    {Py_tp_hash, (void*)UArray__hash__},
    {Py_tp_repr, (void*)UArray__repr__},
    {Py_sq_length, (void*)UArray__len__},
    {Py_sq_item, (void*)UArray__getitem__},
    {Py_tp_richcompare, (void*)UArray__richcmp__},
    {Py_nb_bool, (void*)UArray__bool__},
    {Py_bf_getbuffer, (void*)UArray_getbufferproc},
    {Py_bf_releasebuffer, (void*)UArray_releasebufferproc},
    {Py_tp_members, (void*)UArray_PyMemberDef},
    {0, 0},
};


static PyType_Spec UArray_PyTypeSpec = {
    "gamut.math.UArray",
    sizeof(UArray),
    0,
    Py_TPFLAGS_DEFAULT,
    UArray_PyType_Slots
};


static PyTypeObject *
define_UArray_type(PyObject *module)
{
    PyTypeObject *type = (PyTypeObject *)PyType_FromModuleAndSpec(
        module,
        &UArray_PyTypeSpec,
        0
    );
    if (!type){ return 0; }
    // Note:
    // Unlike other functions that steal references, PyModule_AddObject() only
    // decrements the reference count of value on success.
    if (PyModule_AddObject(module, "UArray", (PyObject *)type) < 0)
    {
        Py_DECREF(type);
        return 0;
    }
    return type;
}

#endif