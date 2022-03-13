
// generated 2022-03-13 19:38:42.320772 from codegen/math/templates/_pod.hpp

#ifndef GAMUT_MATH_U32_HPP
#define GAMUT_MATH_U32_HPP

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
U32Array__new__(PyTypeObject *cls, PyObject *args, PyObject *kwds)
{
    if (kwds && PyDict_Size(kwds) != 0)
    {
        PyErr_SetString(
            PyExc_TypeError,
            "U32 does accept any keyword arguments"
        );
        return 0;
    }

    auto arg_count = PyTuple_GET_SIZE(args);
    if (arg_count == 0)
    {
        auto self = (U32Array *)cls->tp_alloc(cls, 0);
        if (!self){ return 0; }
        self->length = 0;
        self->pod = 0;
        return (PyObject *)self;
    }

    auto *self = (U32Array *)cls->tp_alloc(cls, 0);
    if (!self){ return 0; }
    self->length = arg_count;
    self->pod = new uint32_t[arg_count];

    for (int i = 0; i < arg_count; i++)
    {
        auto arg = PyTuple_GET_ITEM(args, i);
        self->pod[i] = pyobject_to_c_uint32_t(arg);
        if (PyErr_Occurred())
        {
            Py_DECREF(self);
            PyErr_Format(
                PyExc_TypeError,
                "invalid type %R, expected uint32_t",
                arg
            );
            return 0;
        }
    }

    return (PyObject *)self;
}


static void
U32Array__dealloc__(U32Array *self)
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
U32Array__hash__(U32Array *self)
{
    Py_ssize_t len = self->length;
    Py_uhash_t acc = _HASH_XXPRIME_5;
    for (Py_ssize_t i = 0; i < (Py_ssize_t)self->length; i++)
    {
        Py_uhash_t lane = std::hash<uint32_t>{}(self->pod[i]);
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
U32Array__repr__(U32Array *self)
{
    return PyUnicode_FromFormat("U32Array[%zu]", self->length);
}


static Py_ssize_t
U32Array__len__(U32Array *self)
{
    return self->length;
}


static PyObject *
U32Array__getitem__(U32Array *self, Py_ssize_t index)
{
    if (index < 0 || index > (Py_ssize_t)self->length - 1)
    {
        PyErr_Format(PyExc_IndexError, "index out of range");
        return 0;
    }
    return c_uint32_t_to_pyobject(self->pod[index]);
}


static PyObject *
U32Array__richcmp__(
    U32Array *self,
    U32Array *other,
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
U32Array__bool__(U32Array *self)
{
    return self->length ? 1 : 0;
}


static int
U32Array_getbufferproc(U32Array *self, Py_buffer *view, int flags)
{
    if (flags & PyBUF_WRITABLE)
    {
        PyErr_SetString(PyExc_TypeError, "U32 is read only");
        view->obj = 0;
        return -1;
    }
    view->buf = self->pod;
    view->obj = (PyObject *)self;
    view->len = sizeof(uint32_t) * self->length;
    view->readonly = 1;
    view->itemsize = sizeof(uint32_t);
    view->format = "=I";
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
U32Array_releasebufferproc(U32Array *self, Py_buffer *view)
{
    delete view->shape;
}


static PyMemberDef U32Array_PyMemberDef[] = {
    {"__weaklistoffset__", T_PYSSIZET, offsetof(U32Array, weakreflist), READONLY},
    {0}
};


static PyObject *
U32Array_pointer(U32Array *self, void *)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto c_p = module_state->ctypes_c_uint32_t_p;
    return PyObject_CallMethod(c_p, "from_address", "n", (Py_ssize_t)&self->pod);
}


static PyGetSetDef U32Array_PyGetSetDef[] = {
    {"pointer", (getter)U32Array_pointer, 0, 0, 0},
    {0, 0, 0, 0, 0}
};


static PyType_Slot U32Array_PyType_Slots [] = {
    {Py_tp_new, (void*)U32Array__new__},
    {Py_tp_dealloc, (void*)U32Array__dealloc__},
    {Py_tp_hash, (void*)U32Array__hash__},
    {Py_tp_repr, (void*)U32Array__repr__},
    {Py_sq_length, (void*)U32Array__len__},
    {Py_sq_item, (void*)U32Array__getitem__},
    {Py_tp_richcompare, (void*)U32Array__richcmp__},
    {Py_nb_bool, (void*)U32Array__bool__},
    {Py_bf_getbuffer, (void*)U32Array_getbufferproc},
    {Py_bf_releasebuffer, (void*)U32Array_releasebufferproc},
    {Py_tp_getset, (void*)U32Array_PyGetSetDef},
    {Py_tp_members, (void*)U32Array_PyMemberDef},
    {0, 0},
};


static PyType_Spec U32Array_PyTypeSpec = {
    "gamut.math.U32Array",
    sizeof(U32Array),
    0,
    Py_TPFLAGS_DEFAULT,
    U32Array_PyType_Slots
};


static PyTypeObject *
define_U32Array_type(PyObject *module)
{
    PyTypeObject *type = (PyTypeObject *)PyType_FromModuleAndSpec(
        module,
        &U32Array_PyTypeSpec,
        0
    );
    if (!type){ return 0; }
    // Note:
    // Unlike other functions that steal references, PyModule_AddObject() only
    // decrements the reference count of value on success.
    if (PyModule_AddObject(module, "U32Array", (PyObject *)type) < 0)
    {
        Py_DECREF(type);
        return 0;
    }
    return type;
}


static PyTypeObject *
get_U32Array_type()
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    return module_state->U32Array_PyTypeObject;
}


static PyObject *
create_U32Array(size_t length, const uint32_t *value)
{
    auto cls = get_U32Array_type();
    auto result = (U32Array *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->length = length;
    if (length > 0)
    {
        result->pod = new uint32_t[length];
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


static uint32_t *
get_U32Array_value_ptr(const PyObject *self)
{
    if (Py_TYPE(self) != get_U32Array_type())
    {
        PyErr_Format(
            PyExc_TypeError,
            "expected U32Array, got %R",
            self
        );
        return 0;
    }
    return ((U32Array *)self)->pod;
}


static size_t
get_U32Array_length(const PyObject *self)
{
    if (Py_TYPE(self) != get_U32Array_type())
    {
        PyErr_Format(
            PyExc_TypeError,
            "expected U32Array, got %R",
            self
        );
        return 0;
    }
    return ((U32Array *)self)->length;
}

#endif