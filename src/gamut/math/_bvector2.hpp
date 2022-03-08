// generated 2022-03-08 17:09:59.370669 from codegen/math/templates/_vector.hpp

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
#include "_modulestate.hpp"
#include "_type.hpp"

typedef glm::vec<2, bool, glm::defaultp> BVector2Glm;


struct BVector2
{
    PyObject_HEAD
    PyObject *weakreflist;
    BVector2Glm *glm;
};


static PyObject *
BVector2__new__(PyTypeObject *cls, PyObject *args, PyObject *kwds)
{

        bool c_0 = 0;

        bool c_1 = 0;


    if (kwds && PyDict_Size(kwds) != 0)
    {
        PyErr_SetString(
            PyExc_TypeError,
            "BVector2 does accept any keyword arguments"
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
            bool arg_c = pyobject_to_c_bool(arg);
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
                c_0 = pyobject_to_c_bool(arg);
                auto error_occurred = PyErr_Occurred();
                if (error_occurred){ return 0; }
            }

            {
                auto arg = PyTuple_GET_ITEM(args, 1);
                c_1 = pyobject_to_c_bool(arg);
                auto error_occurred = PyErr_Occurred();
                if (error_occurred){ return 0; }
            }

            break;
        }
        default:
        {
            PyErr_Format(
                PyExc_TypeError,
                "invalid number of arguments supplied to BVector2, expected "
                "0, 1 or 2 (got %zd)",
                arg_count
            );
            return 0;
        }
    }

    BVector2 *self = (BVector2*)cls->tp_alloc(cls, 0);
    if (!self){ return 0; }
    self->glm = new BVector2Glm(

            c_0,

            c_1

    );

    return (PyObject *)self;
}


static void
BVector2__dealloc__(BVector2 *self)
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
BVector2__hash__(BVector2 *self)
{
    Py_ssize_t i, len = 2;
    Py_uhash_t acc = _HASH_XXPRIME_5;
    for (i = 0; i < len; i++)
    {
        Py_uhash_t lane = std::hash<bool>{}((*self->glm)[i]);
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
BVector2__repr__(BVector2 *self)
{
    PyObject *result = 0;

        PyObject *py_0 = 0;

        PyObject *py_1 = 0;



        py_0 = c_bool_to_pyobject((*self->glm)[0]);
        if (!py_0){ goto cleanup; }

        py_1 = c_bool_to_pyobject((*self->glm)[1]);
        if (!py_1){ goto cleanup; }

    result = PyUnicode_FromFormat(
        "BVector2("

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
BVector2__len__(BVector2 *self)
{
    return 2;
}


static PyObject *
BVector2__getitem__(BVector2 *self, Py_ssize_t index)
{
    if (index < 0 || index > 1)
    {
        PyErr_Format(PyExc_IndexError, "index out of range");
        return 0;
    }
    auto c = (*self->glm)[index];
    return c_bool_to_pyobject(c);
}


static PyObject *
BVector2__richcmp__(BVector2 *self, BVector2 *other, int op)
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
BVector2__add__(PyObject *left, PyObject *right)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->BVector2_PyTypeObject;

    BVector2Glm vector;
    if (Py_TYPE(left) == Py_TYPE(right))
    {
        vector = (*((BVector2 *)left)->glm) + (*((BVector2 *)right)->glm);
    }
    else
    {
        if (Py_TYPE(left) == cls)
        {
            auto c_right = pyobject_to_c_bool(right);
            if (PyErr_Occurred()){ Py_RETURN_NOTIMPLEMENTED; }
            vector = (*((BVector2 *)left)->glm) + c_right;
        }
        else
        {
            auto c_left = pyobject_to_c_bool(left);
            if (PyErr_Occurred()){ Py_RETURN_NOTIMPLEMENTED; }
            vector = c_left + (*((BVector2 *)right)->glm);
        }
    }

    BVector2 *result = (BVector2 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new BVector2Glm(

            vector[0],

            vector[1]

    );

    return (PyObject *)result;
}


static PyObject *
BVector2__sub__(PyObject *left, PyObject *right)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->BVector2_PyTypeObject;

    BVector2Glm vector;
    if (Py_TYPE(left) == Py_TYPE(right))
    {
        vector = (*((BVector2 *)left)->glm) - (*((BVector2 *)right)->glm);
    }
    else
    {
        if (Py_TYPE(left) == cls)
        {
            auto c_right = pyobject_to_c_bool(right);
            if (PyErr_Occurred()){ Py_RETURN_NOTIMPLEMENTED; }
            vector = (*((BVector2 *)left)->glm) - c_right;
        }
        else
        {
            auto c_left = pyobject_to_c_bool(left);
            if (PyErr_Occurred()){ Py_RETURN_NOTIMPLEMENTED; }
            vector = c_left - (*((BVector2 *)right)->glm);
        }
    }

    BVector2 *result = (BVector2 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new BVector2Glm(

            vector[0],

            vector[1]

    );

    return (PyObject *)result;
}


static PyObject *
BVector2__mul__(PyObject *left, PyObject *right)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->BVector2_PyTypeObject;

    BVector2Glm vector;
    if (Py_TYPE(left) == Py_TYPE(right))
    {
        vector = (*((BVector2 *)left)->glm) * (*((BVector2 *)right)->glm);
    }
    else
    {
        if (Py_TYPE(left) == cls)
        {
            auto c_right = pyobject_to_c_bool(right);
            if (PyErr_Occurred()){ Py_RETURN_NOTIMPLEMENTED; }
            vector = (*((BVector2 *)left)->glm) * c_right;
        }
        else
        {
            auto c_left = pyobject_to_c_bool(left);
            if (PyErr_Occurred()){ Py_RETURN_NOTIMPLEMENTED; }
            vector = c_left * (*((BVector2 *)right)->glm);
        }
    }

    BVector2 *result = (BVector2 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new BVector2Glm(

            vector[0],

            vector[1]

    );

    return (PyObject *)result;
}









    static PyObject *
    BVector2__neg__(BVector2 *self)
    {
        auto cls = Py_TYPE(self);

            BVector2Glm vector = (*self->glm);


        BVector2 *result = (BVector2 *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new BVector2Glm(

                vector[0],

                vector[1]

        );

        return (PyObject *)result;
    }



static PyObject *
BVector2__abs__(BVector2 *self)
{
    auto cls = Py_TYPE(self);
    BVector2Glm vector = glm::abs(*self->glm);

    BVector2 *result = (BVector2 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new BVector2Glm(

            vector[0],

            vector[1]

    );

    return (PyObject *)result;
}


static int
BVector2__bool__(BVector2 *self)
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
BVector2_getbufferproc(BVector2 *self, Py_buffer *view, int flags)
{
    if (flags & PyBUF_WRITABLE)
    {
        PyErr_SetString(PyExc_TypeError, "BVector2 is not read only");
        view->obj = 0;
        return -1;
    }
    view->buf = glm::value_ptr(*self->glm);
    view->obj = (PyObject *)self;
    view->len = sizeof(bool) * 2;
    view->readonly = 1;
    view->itemsize = sizeof(bool);
    view->format = "?";
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
    BVector2_Getter_0(BVector2 *self, void *)
    {
        auto c = (*self->glm)[0];
        return c_bool_to_pyobject(c);
    }

    static PyObject *
    BVector2_Getter_1(BVector2 *self, void *)
    {
        auto c = (*self->glm)[1];
        return c_bool_to_pyobject(c);
    }






static PyGetSetDef BVector2_PyGetSetDef[] = {
    {"x", (getter)BVector2_Getter_0, 0, 0, 0},
    {"r", (getter)BVector2_Getter_0, 0, 0, 0},
    {"s", (getter)BVector2_Getter_0, 0, 0, 0},
    {"u", (getter)BVector2_Getter_0, 0, 0, 0},

        {"y", (getter)BVector2_Getter_1, 0, 0, 0},
        {"g", (getter)BVector2_Getter_1, 0, 0, 0},
        {"t", (getter)BVector2_Getter_1, 0, 0, 0},
        {"v", (getter)BVector2_Getter_1, 0, 0, 0},




    {0, 0, 0, 0, 0}
};


static PyObject *
BVector2__getattr__(BVector2 *self, PyObject *py_attr)
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
        auto py_c = c_bool_to_pyobject((*self->glm)[glm_index]);
        PyTuple_SET_ITEM(result, i, py_c);
    }

    PyErr_Clear();
    return result;
}


static PyMemberDef BVector2_PyMemberDef[] = {
    {"__weaklistoffset__", T_PYSSIZET, offsetof(BVector2, weakreflist), READONLY},
    {0}
};





static PyObject *
BVector2_get_limits(BVector2 *self, void *)
{
    auto c_min = std::numeric_limits<bool>::lowest();
    auto c_max = std::numeric_limits<bool>::max();
    auto py_min = c_bool_to_pyobject(c_min);
    if (!py_min){ return 0; }
    auto py_max = c_bool_to_pyobject(c_max);
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


static PyMethodDef BVector2_PyMethodDef[] = {

    {"get_limits", (PyCFunction)BVector2_get_limits, METH_NOARGS | METH_STATIC, 0},
    {0, 0, 0, 0}
};


static PyType_Slot BVector2_PyType_Slots [] = {
    {Py_tp_new, (void*)BVector2__new__},
    {Py_tp_dealloc, (void*)BVector2__dealloc__},
    {Py_tp_hash, (void*)BVector2__hash__},
    {Py_tp_repr, (void*)BVector2__repr__},
    {Py_sq_length, (void*)BVector2__len__},
    {Py_sq_item, (void*)BVector2__getitem__},
    {Py_tp_richcompare, (void*)BVector2__richcmp__},
    {Py_nb_add, (void*)BVector2__add__},
    {Py_nb_subtract, (void*)BVector2__sub__},
    {Py_nb_multiply, (void*)BVector2__mul__},



        {Py_nb_negative, (void*)BVector2__neg__},

    {Py_nb_absolute, (void*)BVector2__abs__},
    {Py_nb_bool, (void*)BVector2__bool__},
    {Py_bf_getbuffer, (void*)BVector2_getbufferproc},
    {Py_tp_getset, (void*)BVector2_PyGetSetDef},
    {Py_tp_getattro, (void*)BVector2__getattr__},
    {Py_tp_members, (void*)BVector2_PyMemberDef},
    {Py_tp_methods, (void*)BVector2_PyMethodDef},
    {0, 0},
};


static PyType_Spec BVector2_PyTypeSpec = {
    "gamut.math.BVector2",
    sizeof(BVector2),
    0,
    Py_TPFLAGS_DEFAULT,
    BVector2_PyType_Slots
};


static PyTypeObject *
define_BVector2_type(PyObject *module)
{
    PyTypeObject *type = (PyTypeObject *)PyType_FromModuleAndSpec(
        module,
        &BVector2_PyTypeSpec,
        0
    );
    if (!type){ return 0; }
    // Note:
    // Unlike other functions that steal references, PyModule_AddObject() only
    // decrements the reference count of value on success.
    if (PyModule_AddObject(module, "BVector2", (PyObject *)type) < 0)
    {
        Py_DECREF(type);
        return 0;
    }
    return type;
}