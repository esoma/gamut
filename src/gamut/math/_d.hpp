
// generated 2022-03-12 02:15:25.028287 from codegen/math/templates/_pod.hpp

#ifndef GAMUT_MATH_D_HPP
#define GAMUT_MATH_D_HPP

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
DArray__new__(PyTypeObject *cls, PyObject *args, PyObject *kwds)
{
    if (kwds && PyDict_Size(kwds) != 0)
    {
        PyErr_SetString(
            PyExc_TypeError,
            "D does accept any keyword arguments"
        );
        return 0;
    }

    auto arg_count = PyTuple_GET_SIZE(args);
    if (arg_count == 0)
    {
        auto self = (DArray *)cls->tp_alloc(cls, 0);
        if (!self){ return 0; }
        self->length = 0;
        self->pod = 0;
        return (PyObject *)self;
    }

    auto *self = (DArray *)cls->tp_alloc(cls, 0);
    if (!self){ return 0; }
    self->length = arg_count;
    self->pod = new double[arg_count];

    for (int i = 0; i < arg_count; i++)
    {
        auto arg = PyTuple_GET_ITEM(args, i);
        self->pod[i] = pyobject_to_c_double(arg);
        if (PyErr_Occurred())
        {
            Py_DECREF(self);
            PyErr_Format(
                PyExc_TypeError,
                "invalid type %R, expected double",
                arg
            );
            return 0;
        }
    }

    return (PyObject *)self;
}


static void
DArray__dealloc__(DArray *self)
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
DArray__hash__(DArray *self)
{
    Py_ssize_t len = self->length;
    Py_uhash_t acc = _HASH_XXPRIME_5;
    for (Py_ssize_t i = 0; i < (Py_ssize_t)self->length; i++)
    {
        Py_uhash_t lane = std::hash<double>{}(self->pod[i]);
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
DArray__repr__(DArray *self)
{
    return PyUnicode_FromFormat("DArray[%zu]", self->length);
}


static Py_ssize_t
DArray__len__(DArray *self)
{
    return self->length;
}


static PyObject *
DArray__getitem__(DArray *self, Py_ssize_t index)
{
    if (index < 0 || index > (Py_ssize_t)self->length - 1)
    {
        PyErr_Format(PyExc_IndexError, "index out of range");
        return 0;
    }
    return c_double_to_pyobject(self->pod[index]);
}


static PyObject *
DArray__richcmp__(
    DArray *self,
    DArray *other,
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
DArray__bool__(DArray *self)
{
    return self->length ? 1 : 0;
}


static int
DArray_getbufferproc(DArray *self, Py_buffer *view, int flags)
{
    if (flags & PyBUF_WRITABLE)
    {
        PyErr_SetString(PyExc_TypeError, "D is read only");
        view->obj = 0;
        return -1;
    }
    view->buf = self->pod;
    view->obj = (PyObject *)self;
    view->len = sizeof(double) * self->length;
    view->readonly = 1;
    view->itemsize = sizeof(double);
    view->format = "d";
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
DArray_releasebufferproc(DArray *self, Py_buffer *view)
{
    delete view->shape;
}


static PyMemberDef DArray_PyMemberDef[] = {
    {"__weaklistoffset__", T_PYSSIZET, offsetof(DArray, weakreflist), READONLY},
    {0}
};


static PyType_Slot DArray_PyType_Slots [] = {
    {Py_tp_new, (void*)DArray__new__},
    {Py_tp_dealloc, (void*)DArray__dealloc__},
    {Py_tp_hash, (void*)DArray__hash__},
    {Py_tp_repr, (void*)DArray__repr__},
    {Py_sq_length, (void*)DArray__len__},
    {Py_sq_item, (void*)DArray__getitem__},
    {Py_tp_richcompare, (void*)DArray__richcmp__},
    {Py_nb_bool, (void*)DArray__bool__},
    {Py_bf_getbuffer, (void*)DArray_getbufferproc},
    {Py_bf_releasebuffer, (void*)DArray_releasebufferproc},
    {Py_tp_members, (void*)DArray_PyMemberDef},
    {0, 0},
};


static PyType_Spec DArray_PyTypeSpec = {
    "gamut.math.DArray",
    sizeof(DArray),
    0,
    Py_TPFLAGS_DEFAULT,
    DArray_PyType_Slots
};


static PyTypeObject *
define_DArray_type(PyObject *module)
{
    PyTypeObject *type = (PyTypeObject *)PyType_FromModuleAndSpec(
        module,
        &DArray_PyTypeSpec,
        0
    );
    if (!type){ return 0; }
    // Note:
    // Unlike other functions that steal references, PyModule_AddObject() only
    // decrements the reference count of value on success.
    if (PyModule_AddObject(module, "DArray", (PyObject *)type) < 0)
    {
        Py_DECREF(type);
        return 0;
    }
    return type;
}


static PyTypeObject *
get_DArray_type()
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    return module_state->DArray_PyTypeObject;
}


static PyObject *
create_DArray(size_t length, double *value)
{
    auto cls = get_DArray_type();
    auto result = (DArray *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->length = length;
    if (length > 0)
    {
        result->pod = new double[length];
        for (size_t i = 0; i < length; i++)
        {
            result->pod[i] = value[i];
        }
    }
    else
    {
        result->pod = 0;
    }
    return (PyObject *)result;
}


static double *
get_DArray_value_ptr(PyObject *self)
{
    if (Py_TYPE(self) != get_DArray_type())
    {
        PyErr_Format(
            PyExc_TypeError,
            "expected DArray, got %R",
            self
        );
        return 0;
    }
    return ((DArray *)self)->pod;
}


static size_t
get_DArray_length(PyObject *self)
{
    if (Py_TYPE(self) != get_DArray_type())
    {
        PyErr_Format(
            PyExc_TypeError,
            "expected DArray, got %R",
            self
        );
        return 0;
    }
    return ((DArray *)self)->length;
}

#endif