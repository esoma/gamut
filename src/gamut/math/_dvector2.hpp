// generated 2022-03-07 23:13:00.194594 from codegen/math/templates/_vector.hpp

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

typedef glm::vec<2, double, glm::defaultp> DVector2Glm;


struct DVector2
{
    PyObject_HEAD
    PyObject *weakreflist;
    DVector2Glm *glm;
};


static PyObject *
DVector2__new__(PyTypeObject *cls, PyObject *args, PyObject *kwds)
{

        double c_0 = 0;

        double c_1 = 0;


    if (kwds && PyDict_Size(kwds) != 0)
    {
        PyErr_SetString(
            PyExc_TypeError,
            "DVector2 does accept any keyword arguments"
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
            double arg_c = pyobject_to_c_double(arg);
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
                c_0 = pyobject_to_c_double(arg);
                auto error_occurred = PyErr_Occurred();
                if (error_occurred){ return 0; }
            }

            {
                auto arg = PyTuple_GET_ITEM(args, 1);
                c_1 = pyobject_to_c_double(arg);
                auto error_occurred = PyErr_Occurred();
                if (error_occurred){ return 0; }
            }

            break;
        }
        default:
        {
            PyErr_Format(
                PyExc_TypeError,
                "invalid number of arguments supplied to DVector2, expected "
                "0, 1 or 2 (got %zd)",
                arg_count
            );
            return 0;
        }
    }

    DVector2 *self = (DVector2*)cls->tp_alloc(cls, 0);
    if (!self){ return 0; }
    self->glm = new DVector2Glm(

            c_0,

            c_1

    );

    return (PyObject *)self;
}


static void
DVector2__dealloc__(DVector2 *self)
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
DVector2__hash__(DVector2 *self)
{
    Py_ssize_t i, len = 2;
    Py_uhash_t acc = _HASH_XXPRIME_5;
    for (i = 0; i < len; i++)
    {
        Py_uhash_t lane = std::hash<double>{}((*self->glm)[i]);
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
DVector2__repr__(DVector2 *self)
{
    PyObject *result = 0;

        PyObject *py_0 = 0;

        PyObject *py_1 = 0;



        py_0 = c_double_to_pyobject((*self->glm)[0]);
        if (!py_0){ goto cleanup; }

        py_1 = c_double_to_pyobject((*self->glm)[1]);
        if (!py_1){ goto cleanup; }

    result = PyUnicode_FromFormat(
        "DVector2("

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
DVector2__len__(DVector2 *self)
{
    return 2;
}


static PyObject *
DVector2__getitem__(DVector2 *self, Py_ssize_t index)
{
    if (index < 0 || index > 1)
    {
        PyErr_Format(PyExc_IndexError, "index out of range");
        return 0;
    }
    auto c = (*self->glm)[index];
    return c_double_to_pyobject(c);
}


static PyObject *
DVector2__richcmp__(DVector2 *self, DVector2 *other, int op)
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
DVector2__add__(DVector2 *self, PyObject *other)
{
    auto cls = Py_TYPE(self);
    DVector2Glm vector;
    if (Py_TYPE(other) != cls)
    {
        auto c_other = pyobject_to_c_double(other);
        if (PyErr_Occurred()){ Py_RETURN_NOTIMPLEMENTED; }
        vector = (*self->glm) + c_other;
    }
    else
    {
        vector = (*self->glm) + (*((DVector2 *)other)->glm);
    }

    DVector2 *result = (DVector2 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new DVector2Glm(

            vector[0],

            vector[1]

    );

    return (PyObject *)result;
}


static PyObject *
DVector2__sub__(DVector2 *self, PyObject *other)
{
    auto cls = Py_TYPE(self);
    DVector2Glm vector;
    if (Py_TYPE(other) != cls)
    {
        auto c_other = pyobject_to_c_double(other);
        if (PyErr_Occurred()){ Py_RETURN_NOTIMPLEMENTED; }
        vector = (*self->glm) - c_other;
    }
    else
    {
        vector = (*self->glm) - (*((DVector2 *)other)->glm);
    }

    DVector2 *result = (DVector2 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new DVector2Glm(

            vector[0],

            vector[1]

    );

    return (PyObject *)result;
}


static PyObject *
DVector2__mul__(DVector2 *self, PyObject *other)
{
    auto cls = Py_TYPE(self);
    DVector2Glm vector;
    if (Py_TYPE(other) != cls)
    {
        auto c_other = pyobject_to_c_double(other);
        if (PyErr_Occurred()){ Py_RETURN_NOTIMPLEMENTED; }
        vector = (*self->glm) * c_other;
    }
    else
    {
        vector = (*self->glm) * (*((DVector2 *)other)->glm);
    }

    DVector2 *result = (DVector2 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new DVector2Glm(

            vector[0],

            vector[1]

    );

    return (PyObject *)result;
}



    static PyObject *
    DVector2__matmul__(DVector2 *self, DVector2 *other)
    {
        auto cls = Py_TYPE(self);
        if (Py_TYPE(other) != cls){ Py_RETURN_NOTIMPLEMENTED; }
        auto c_result = glm::dot(*self->glm, *other->glm);
        return c_double_to_pyobject(c_result);
    }


    static PyObject *
    DVector2__mod__(DVector2 *self, PyObject *other)
    {
        auto cls = Py_TYPE(self);
        DVector2Glm vector;
        if (Py_TYPE(other) != cls)
        {
            auto c_other = pyobject_to_c_double(other);
            if (PyErr_Occurred()){ Py_RETURN_NOTIMPLEMENTED; }
            vector = glm::mod((*self->glm), c_other);
        }
        else
        {
            vector = glm::mod((*self->glm), (*((DVector2 *)other)->glm));
        }

        DVector2 *result = (DVector2 *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new DVector2Glm(

                vector[0],

                vector[1]

        );

        return (PyObject *)result;
    }


    static PyObject *
    DVector2__pow__(DVector2 *self, PyObject *other)
    {
        auto cls = Py_TYPE(self);
        DVector2Glm vector;
        if (Py_TYPE(other) != cls)
        {
            auto c_other = pyobject_to_c_double(other);
            if (PyErr_Occurred()){ Py_RETURN_NOTIMPLEMENTED; }
            vector = glm::pow((*self->glm), DVector2Glm(c_other));
        }
        else
        {
            vector = glm::pow((*self->glm), (*((DVector2 *)other)->glm));
        }

        DVector2 *result = (DVector2 *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new DVector2Glm(

                vector[0],

                vector[1]

        );

        return (PyObject *)result;
    }




    static PyObject *
    DVector2__truediv__(DVector2 *self, PyObject *other)
    {
        auto cls = Py_TYPE(self);
        DVector2Glm vector;
        if (Py_TYPE(other) != cls)
        {
            auto c_other = pyobject_to_c_double(other);
            if (PyErr_Occurred()){ Py_RETURN_NOTIMPLEMENTED; }

            vector = (*self->glm) / c_other;
        }
        else
        {

            vector = (*self->glm) / (*((DVector2 *)other)->glm);
        }

        DVector2 *result = (DVector2 *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new DVector2Glm(

                vector[0],

                vector[1]

        );

        return (PyObject *)result;
    }




    static PyObject *
    DVector2__neg__(DVector2 *self)
    {
        auto cls = Py_TYPE(self);

            DVector2Glm vector = -(*self->glm);


        DVector2 *result = (DVector2 *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new DVector2Glm(

                vector[0],

                vector[1]

        );

        return (PyObject *)result;
    }



static PyObject *
DVector2__abs__(DVector2 *self)
{
    auto cls = Py_TYPE(self);
    DVector2Glm vector = glm::abs(*self->glm);

    DVector2 *result = (DVector2 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new DVector2Glm(

            vector[0],

            vector[1]

    );

    return (PyObject *)result;
}


static int
DVector2__bool__(DVector2 *self)
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
DVector2_getbufferproc(DVector2 *self, Py_buffer *view, int flags)
{
    if (flags & PyBUF_WRITABLE)
    {
        PyErr_SetString(PyExc_TypeError, "DVector2 is not read only");
        view->obj = 0;
        return -1;
    }
    view->buf = glm::value_ptr(*self->glm);
    view->obj = (PyObject *)self;
    view->len = sizeof(double) * 2;
    view->readonly = 1;
    view->itemsize = sizeof(double);
    view->format = "d";
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
    DVector2_Getter_0(DVector2 *self, void *)
    {
        auto c = (*self->glm)[0];
        return c_double_to_pyobject(c);
    }

    static PyObject *
    DVector2_Getter_1(DVector2 *self, void *)
    {
        auto c = (*self->glm)[1];
        return c_double_to_pyobject(c);
    }




    static PyObject *
    DVector2_magnitude(DVector2 *self, void *)
    {
        auto magnitude = glm::length(*self->glm);
        return c_double_to_pyobject(magnitude);
    }



static PyGetSetDef DVector2_PyGetSetDef[] = {
    {"x", (getter)DVector2_Getter_0, 0, 0, 0},
    {"r", (getter)DVector2_Getter_0, 0, 0, 0},
    {"s", (getter)DVector2_Getter_0, 0, 0, 0},
    {"u", (getter)DVector2_Getter_0, 0, 0, 0},

        {"y", (getter)DVector2_Getter_1, 0, 0, 0},
        {"g", (getter)DVector2_Getter_1, 0, 0, 0},
        {"t", (getter)DVector2_Getter_1, 0, 0, 0},
        {"v", (getter)DVector2_Getter_1, 0, 0, 0},




        {"magnitude", (getter)DVector2_magnitude, 0, 0, 0},

    {0, 0, 0, 0, 0}
};


static PyObject *
DVector2__getattr__(DVector2 *self, PyObject *py_attr)
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
        auto py_c = c_double_to_pyobject((*self->glm)[glm_index]);
        PyTuple_SET_ITEM(result, i, py_c);
    }

    PyErr_Clear();
    return result;
}


static PyMemberDef DVector2_PyMemberDef[] = {
    {"__weaklistoffset__", T_PYSSIZET, offsetof(DVector2, weakreflist), READONLY},
    {0}
};





    static DVector2 *
    DVector2_normalize(DVector2 *self, void*)
    {
        auto cls = Py_TYPE(self);
        auto vector = glm::normalize(*self->glm);
        DVector2 *result = (DVector2 *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new DVector2Glm(

                vector[0],

                vector[1]

        );
        return result;
    }


    static PyObject *
    DVector2_distance(DVector2 *self, DVector2 *other)
    {
        auto cls = Py_TYPE(self);
        if (Py_TYPE(other) != cls)
        {
            PyErr_Format(PyExc_TypeError, "%R is not DVector2", other);
            return 0;
        }
        auto result = glm::distance(*self->glm, *other->glm);
        return c_double_to_pyobject(result);
    }



static PyObject *
DVector2_get_limits(DVector2 *self, void *)
{
    auto c_min = std::numeric_limits<double>::min();
    auto c_max = std::numeric_limits<double>::max();
    auto py_min = c_double_to_pyobject(c_min);
    if (!py_min){ return 0; }
    auto py_max = c_double_to_pyobject(c_max);
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


static PyMethodDef DVector2_PyMethodDef[] = {


        {"normalize", (PyCFunction)DVector2_normalize, METH_NOARGS, 0},
        {"distance", (PyCFunction)DVector2_distance, METH_O, 0},

    {"get_limits", (PyCFunction)DVector2_get_limits, METH_NOARGS | METH_STATIC, 0},
    {0, 0, 0, 0}
};


static PyType_Slot DVector2_PyType_Slots [] = {
    {Py_tp_new, (void*)DVector2__new__},
    {Py_tp_dealloc, (void*)DVector2__dealloc__},
    {Py_tp_hash, (void*)DVector2__hash__},
    {Py_tp_repr, (void*)DVector2__repr__},
    {Py_sq_length, (void*)DVector2__len__},
    {Py_sq_item, (void*)DVector2__getitem__},
    {Py_tp_richcompare, (void*)DVector2__richcmp__},
    {Py_nb_add, (void*)DVector2__add__},
    {Py_nb_subtract, (void*)DVector2__sub__},
    {Py_nb_multiply, (void*)DVector2__mul__},

        {Py_nb_matrix_multiply, (void*)DVector2__matmul__},
        {Py_nb_remainder, (void*)DVector2__mod__},
        {Py_nb_power, (void*)DVector2__pow__},


        {Py_nb_true_divide, (void*)DVector2__truediv__},


        {Py_nb_negative, (void*)DVector2__neg__},

    {Py_nb_absolute, (void*)DVector2__abs__},
    {Py_nb_bool, (void*)DVector2__bool__},
    {Py_bf_getbuffer, (void*)DVector2_getbufferproc},
    {Py_tp_getset, (void*)DVector2_PyGetSetDef},
    {Py_tp_getattro, (void*)DVector2__getattr__},
    {Py_tp_members, (void*)DVector2_PyMemberDef},
    {Py_tp_methods, (void*)DVector2_PyMethodDef},
    {0, 0},
};


static PyType_Spec DVector2_PyTypeSpec = {
    "gamut.math.DVector2",
    sizeof(DVector2),
    0,
    Py_TPFLAGS_DEFAULT,
    DVector2_PyType_Slots
};


static PyTypeObject *
define_DVector2_type(PyObject *module)
{
    PyTypeObject *type = (PyTypeObject *)PyType_FromModuleAndSpec(
        module,
        &DVector2_PyTypeSpec,
        0
    );
    if (!type){ return 0; }
    // Note:
    // Unlike other functions that steal references, PyModule_AddObject() only
    // decrements the reference count of value on success.
    if (PyModule_AddObject(module, "DVector2", (PyObject *)type) < 0)
    {
        Py_DECREF(type);
        return 0;
    }
    return type;
}