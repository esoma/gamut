
// generated 2022-03-11 18:37:26.835467 from codegen/math/templates/_pod.hpp

#ifndef GAMUT_MATH_F_HPP
#define GAMUT_MATH_F_HPP

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
FArray__new__(PyTypeObject *cls, PyObject *args, PyObject *kwds)
{
    if (kwds && PyDict_Size(kwds) != 0)
    {
        PyErr_SetString(
            PyExc_TypeError,
            "F does accept any keyword arguments"
        );
        return 0;
    }

    auto arg_count = PyTuple_GET_SIZE(args);
    if (arg_count == 0)
    {
        auto self = (FArray *)cls->tp_alloc(cls, 0);
        if (!self){ return 0; }
        self->length = 0;
        self->pod = 0;
        return (PyObject *)self;
    }

    auto *self = (FArray *)cls->tp_alloc(cls, 0);
    if (!self){ return 0; }
    self->length = arg_count;
    self->pod = new float[arg_count];

    for (int i = 0; i < arg_count; i++)
    {
        auto arg = PyTuple_GET_ITEM(args, i);
        self->pod[i] = pyobject_to_c_float(arg);
        if (PyErr_Occurred())
        {
            Py_DECREF(self);
            PyErr_Format(
                PyExc_TypeError,
                "invalid type %R, expected float",
                arg
            );
            return 0;
        }
    }

    return (PyObject *)self;
}


static void
FArray__dealloc__(FArray *self)
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
FArray__hash__(FArray *self)
{
    Py_ssize_t len = self->length;
    Py_uhash_t acc = _HASH_XXPRIME_5;
    for (Py_ssize_t i = 0; i < (Py_ssize_t)self->length; i++)
    {
        Py_uhash_t lane = std::hash<float>{}(self->pod[i]);
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
FArray__repr__(FArray *self)
{
    return PyUnicode_FromFormat("FArray[%zu]", self->length);
}


static Py_ssize_t
FArray__len__(FArray *self)
{
    return self->length;
}


static PyObject *
FArray__getitem__(FArray *self, Py_ssize_t index)
{
    if (index < 0 || index > (Py_ssize_t)self->length - 1)
    {
        PyErr_Format(PyExc_IndexError, "index out of range");
        return 0;
    }
    return c_float_to_pyobject(self->pod[index]);
}


static PyObject *
FArray__richcmp__(
    FArray *self,
    FArray *other,
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
FArray__bool__(FArray *self)
{
    return self->length ? 1 : 0;
}


static int
FArray_getbufferproc(FArray *self, Py_buffer *view, int flags)
{
    if (flags & PyBUF_WRITABLE)
    {
        PyErr_SetString(PyExc_TypeError, "F is read only");
        view->obj = 0;
        return -1;
    }
    view->buf = self->pod;
    view->obj = (PyObject *)self;
    view->len = sizeof(float) * self->length;
    view->readonly = 1;
    view->itemsize = sizeof(float);
    view->format = "f";
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
FArray_releasebufferproc(FArray *self, Py_buffer *view)
{
    delete view->shape;
}


static PyMemberDef FArray_PyMemberDef[] = {
    {"__weaklistoffset__", T_PYSSIZET, offsetof(FArray, weakreflist), READONLY},
    {0}
};


static PyType_Slot FArray_PyType_Slots [] = {
    {Py_tp_new, (void*)FArray__new__},
    {Py_tp_dealloc, (void*)FArray__dealloc__},
    {Py_tp_hash, (void*)FArray__hash__},
    {Py_tp_repr, (void*)FArray__repr__},
    {Py_sq_length, (void*)FArray__len__},
    {Py_sq_item, (void*)FArray__getitem__},
    {Py_tp_richcompare, (void*)FArray__richcmp__},
    {Py_nb_bool, (void*)FArray__bool__},
    {Py_bf_getbuffer, (void*)FArray_getbufferproc},
    {Py_bf_releasebuffer, (void*)FArray_releasebufferproc},
    {Py_tp_members, (void*)FArray_PyMemberDef},
    {0, 0},
};


static PyType_Spec FArray_PyTypeSpec = {
    "gamut.math.FArray",
    sizeof(FArray),
    0,
    Py_TPFLAGS_DEFAULT,
    FArray_PyType_Slots
};


static PyTypeObject *
define_FArray_type(PyObject *module)
{
    PyTypeObject *type = (PyTypeObject *)PyType_FromModuleAndSpec(
        module,
        &FArray_PyTypeSpec,
        0
    );
    if (!type){ return 0; }
    // Note:
    // Unlike other functions that steal references, PyModule_AddObject() only
    // decrements the reference count of value on success.
    if (PyModule_AddObject(module, "FArray", (PyObject *)type) < 0)
    {
        Py_DECREF(type);
        return 0;
    }
    return type;
}

#endif