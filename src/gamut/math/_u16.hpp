
// generated 2022-03-12 02:15:25.029787 from codegen/math/templates/_pod.hpp

#ifndef GAMUT_MATH_U16_HPP
#define GAMUT_MATH_U16_HPP

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
U16Array__new__(PyTypeObject *cls, PyObject *args, PyObject *kwds)
{
    if (kwds && PyDict_Size(kwds) != 0)
    {
        PyErr_SetString(
            PyExc_TypeError,
            "U16 does accept any keyword arguments"
        );
        return 0;
    }

    auto arg_count = PyTuple_GET_SIZE(args);
    if (arg_count == 0)
    {
        auto self = (U16Array *)cls->tp_alloc(cls, 0);
        if (!self){ return 0; }
        self->length = 0;
        self->pod = 0;
        return (PyObject *)self;
    }

    auto *self = (U16Array *)cls->tp_alloc(cls, 0);
    if (!self){ return 0; }
    self->length = arg_count;
    self->pod = new uint16_t[arg_count];

    for (int i = 0; i < arg_count; i++)
    {
        auto arg = PyTuple_GET_ITEM(args, i);
        self->pod[i] = pyobject_to_c_uint16_t(arg);
        if (PyErr_Occurred())
        {
            Py_DECREF(self);
            PyErr_Format(
                PyExc_TypeError,
                "invalid type %R, expected uint16_t",
                arg
            );
            return 0;
        }
    }

    return (PyObject *)self;
}


static void
U16Array__dealloc__(U16Array *self)
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
U16Array__hash__(U16Array *self)
{
    Py_ssize_t len = self->length;
    Py_uhash_t acc = _HASH_XXPRIME_5;
    for (Py_ssize_t i = 0; i < (Py_ssize_t)self->length; i++)
    {
        Py_uhash_t lane = std::hash<uint16_t>{}(self->pod[i]);
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
U16Array__repr__(U16Array *self)
{
    return PyUnicode_FromFormat("U16Array[%zu]", self->length);
}


static Py_ssize_t
U16Array__len__(U16Array *self)
{
    return self->length;
}


static PyObject *
U16Array__getitem__(U16Array *self, Py_ssize_t index)
{
    if (index < 0 || index > (Py_ssize_t)self->length - 1)
    {
        PyErr_Format(PyExc_IndexError, "index out of range");
        return 0;
    }
    return c_uint16_t_to_pyobject(self->pod[index]);
}


static PyObject *
U16Array__richcmp__(
    U16Array *self,
    U16Array *other,
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
U16Array__bool__(U16Array *self)
{
    return self->length ? 1 : 0;
}


static int
U16Array_getbufferproc(U16Array *self, Py_buffer *view, int flags)
{
    if (flags & PyBUF_WRITABLE)
    {
        PyErr_SetString(PyExc_TypeError, "U16 is read only");
        view->obj = 0;
        return -1;
    }
    view->buf = self->pod;
    view->obj = (PyObject *)self;
    view->len = sizeof(uint16_t) * self->length;
    view->readonly = 1;
    view->itemsize = sizeof(uint16_t);
    view->format = "=H";
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
U16Array_releasebufferproc(U16Array *self, Py_buffer *view)
{
    delete view->shape;
}


static PyMemberDef U16Array_PyMemberDef[] = {
    {"__weaklistoffset__", T_PYSSIZET, offsetof(U16Array, weakreflist), READONLY},
    {0}
};


static PyType_Slot U16Array_PyType_Slots [] = {
    {Py_tp_new, (void*)U16Array__new__},
    {Py_tp_dealloc, (void*)U16Array__dealloc__},
    {Py_tp_hash, (void*)U16Array__hash__},
    {Py_tp_repr, (void*)U16Array__repr__},
    {Py_sq_length, (void*)U16Array__len__},
    {Py_sq_item, (void*)U16Array__getitem__},
    {Py_tp_richcompare, (void*)U16Array__richcmp__},
    {Py_nb_bool, (void*)U16Array__bool__},
    {Py_bf_getbuffer, (void*)U16Array_getbufferproc},
    {Py_bf_releasebuffer, (void*)U16Array_releasebufferproc},
    {Py_tp_members, (void*)U16Array_PyMemberDef},
    {0, 0},
};


static PyType_Spec U16Array_PyTypeSpec = {
    "gamut.math.U16Array",
    sizeof(U16Array),
    0,
    Py_TPFLAGS_DEFAULT,
    U16Array_PyType_Slots
};


static PyTypeObject *
define_U16Array_type(PyObject *module)
{
    PyTypeObject *type = (PyTypeObject *)PyType_FromModuleAndSpec(
        module,
        &U16Array_PyTypeSpec,
        0
    );
    if (!type){ return 0; }
    // Note:
    // Unlike other functions that steal references, PyModule_AddObject() only
    // decrements the reference count of value on success.
    if (PyModule_AddObject(module, "U16Array", (PyObject *)type) < 0)
    {
        Py_DECREF(type);
        return 0;
    }
    return type;
}


static PyTypeObject *
get_U16Array_type()
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    return module_state->U16Array_PyTypeObject;
}


static PyObject *
create_U16Array(size_t length, uint16_t *value)
{
    auto cls = get_U16Array_type();
    auto result = (U16Array *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->length = length;
    if (length > 0)
    {
        result->pod = new uint16_t[length];
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


static uint16_t *
get_U16Array_value_ptr(PyObject *self)
{
    if (Py_TYPE(self) != get_U16Array_type())
    {
        PyErr_Format(
            PyExc_TypeError,
            "expected U16Array, got %R",
            self
        );
        return 0;
    }
    return ((U16Array *)self)->pod;
}


static size_t
get_U16Array_length(PyObject *self)
{
    if (Py_TYPE(self) != get_U16Array_type())
    {
        PyErr_Format(
            PyExc_TypeError,
            "expected U16Array, got %R",
            self
        );
        return 0;
    }
    return ((U16Array *)self)->length;
}

#endif