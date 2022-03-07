// generated 2022-03-07 03:05:30.756874

#include <stdio.h>
#include <iostream>

// python
#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <structmember.h>
// glm
#include <glm/glm.hpp>
#include <glm/ext.hpp>
#include <glm/detail/type_vec3.hpp>
// gamut
#include "_type.hpp"

typedef glm::vec<3, float, glm::defaultp> FVector3Glm;


struct FVector3
{
    PyObject_HEAD
    PyObject *weakreflist;
    FVector3Glm *glm;
};


static PyObject *
FVector3__new__(PyTypeObject *cls, PyObject *args, PyObject *kwds)
{

        float c_0 = 0;

        float c_1 = 0;

        float c_2 = 0;


    if (kwds && PyDict_Size(kwds) != 0)
    {
        PyErr_SetString(
            PyExc_TypeError,
            "FVector3 does accept any keyword arguments"
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
            float arg_c = pyobject_to_c_float(arg);
            auto error_occurred = PyErr_Occurred();
            if (error_occurred){ return 0; }

                c_0 = arg_c;

                c_1 = arg_c;

                c_2 = arg_c;

            break;
        }
        case 3:
        {

            {
                auto arg = PyTuple_GET_ITEM(args, 0);
                c_0 = pyobject_to_c_float(arg);
                auto error_occurred = PyErr_Occurred();
                if (error_occurred){ return 0; }
            }

            {
                auto arg = PyTuple_GET_ITEM(args, 1);
                c_1 = pyobject_to_c_float(arg);
                auto error_occurred = PyErr_Occurred();
                if (error_occurred){ return 0; }
            }

            {
                auto arg = PyTuple_GET_ITEM(args, 2);
                c_2 = pyobject_to_c_float(arg);
                auto error_occurred = PyErr_Occurred();
                if (error_occurred){ return 0; }
            }

            break;
        }
        default:
        {
            PyErr_Format(
                PyExc_TypeError,
                "invalid number of arguments supplied to FVector3, expected "
                "0, 1 or 3 (got %zd)",
                arg_count
            );
            return 0;
        }
    }

    FVector3 *self = (FVector3*)cls->tp_alloc(cls, 0);
    if (!self){ return 0; }
    self->glm = new FVector3Glm(

            c_0,

            c_1,

            c_2

    );

    return (PyObject *)self;
}


static void
FVector3__dealloc__(FVector3 *self)
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


static Py_hash_t
FVector3__hash__(FVector3 *self)
{
    Py_hash_t hash = 0;

        hash ^= (Py_hash_t)(*self->glm)[0];

        hash ^= (Py_hash_t)(*self->glm)[1];

        hash ^= (Py_hash_t)(*self->glm)[2];

    if (hash == -1){ hash = -123456789; }
    return hash;
}


static PyObject *
FVector3__repr__(FVector3 *self)
{
    PyObject *result = 0;

        PyObject *py_0 = 0;

        PyObject *py_1 = 0;

        PyObject *py_2 = 0;



        py_0 = c_float_to_pyobject((*self->glm)[0]);
        if (!py_0){ goto cleanup; }

        py_1 = c_float_to_pyobject((*self->glm)[1]);
        if (!py_1){ goto cleanup; }

        py_2 = c_float_to_pyobject((*self->glm)[2]);
        if (!py_2){ goto cleanup; }

    result = PyUnicode_FromFormat(
        "FVector3("

            "%R, "

            "%R, "

            "%R"

        ")",

            py_0,

            py_1,

            py_2

    );
cleanup:

        Py_XDECREF(py_0);

        Py_XDECREF(py_1);

        Py_XDECREF(py_2);

    return result;
}


static Py_ssize_t
FVector3__len__(FVector3 *self)
{
    return 3;
}


static PyObject *
FVector3__getitem__(FVector3 *self, Py_ssize_t index)
{
    if (index < 0 || index > 2)
    {
        PyErr_Format(PyExc_IndexError, "index out of range");
        return 0;
    }
    auto c = (*self->glm)[index];
    return c_float_to_pyobject(c);
}


static PyObject *
FVector3__richcmp__(FVector3 *self, FVector3 *other, int op)
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
FVector3__add__(FVector3 *self, PyObject *other)
{
    auto cls = Py_TYPE(self);
    FVector3Glm vector;
    if (Py_TYPE(other) != cls)
    {
        auto c_other = pyobject_to_c_float(other);
        if (PyErr_Occurred()){ Py_RETURN_NOTIMPLEMENTED; }
        vector = (*self->glm) + c_other;
    }
    else
    {
        vector = (*self->glm) + (*((FVector3 *)other)->glm);
    }

    FVector3 *result = (FVector3 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new FVector3Glm(

            vector[0],

            vector[1],

            vector[2]

    );

    return (PyObject *)result;
}


static PyObject *
FVector3__sub__(FVector3 *self, PyObject *other)
{
    auto cls = Py_TYPE(self);
    FVector3Glm vector;
    if (Py_TYPE(other) != cls)
    {
        auto c_other = pyobject_to_c_float(other);
        if (PyErr_Occurred()){ Py_RETURN_NOTIMPLEMENTED; }
        vector = (*self->glm) - c_other;
    }
    else
    {
        vector = (*self->glm) - (*((FVector3 *)other)->glm);
    }

    FVector3 *result = (FVector3 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new FVector3Glm(

            vector[0],

            vector[1],

            vector[2]

    );

    return (PyObject *)result;
}


static PyObject *
FVector3__mul__(FVector3 *self, PyObject *other)
{
    auto cls = Py_TYPE(self);
    FVector3Glm vector;
    if (Py_TYPE(other) != cls)
    {
        auto c_other = pyobject_to_c_float(other);
        if (PyErr_Occurred()){ Py_RETURN_NOTIMPLEMENTED; }
        vector = (*self->glm) * c_other;
    }
    else
    {
        vector = (*self->glm) * (*((FVector3 *)other)->glm);
    }

    FVector3 *result = (FVector3 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new FVector3Glm(

            vector[0],

            vector[1],

            vector[2]

    );

    return (PyObject *)result;
}


static PyObject *
FVector3__matmul__(FVector3 *self, FVector3 *other)
{
    auto cls = Py_TYPE(self);
    if (Py_TYPE(other) != cls){ Py_RETURN_NOTIMPLEMENTED; }
    auto c_result = glm::dot(*self->glm, *other->glm);
    return c_float_to_pyobject(c_result);
}


static PyObject *
FVector3__truediv__(FVector3 *self, PyObject *other)
{
    auto cls = Py_TYPE(self);
    FVector3Glm vector;
    if (Py_TYPE(other) != cls)
    {
        auto c_other = pyobject_to_c_float(other);
        if (PyErr_Occurred()){ Py_RETURN_NOTIMPLEMENTED; }
        vector = (*self->glm) / c_other;
    }
    else
    {
        vector = (*self->glm) / (*((FVector3 *)other)->glm);
    }

    FVector3 *result = (FVector3 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new FVector3Glm(

            vector[0],

            vector[1],

            vector[2]

    );

    return (PyObject *)result;
}


static PyObject *
FVector3__mod__(FVector3 *self, PyObject *other)
{
    auto cls = Py_TYPE(self);
    FVector3Glm vector;
    if (Py_TYPE(other) != cls)
    {
        auto c_other = pyobject_to_c_float(other);
        if (PyErr_Occurred()){ Py_RETURN_NOTIMPLEMENTED; }
        vector = glm::mod((*self->glm), c_other);
    }
    else
    {
        vector = glm::mod((*self->glm), (*((FVector3 *)other)->glm));
    }

    FVector3 *result = (FVector3 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new FVector3Glm(

            vector[0],

            vector[1],

            vector[2]

    );

    return (PyObject *)result;
}


static PyObject *
FVector3__pow__(FVector3 *self, PyObject *other)
{
    auto cls = Py_TYPE(self);
    FVector3Glm vector;
    if (Py_TYPE(other) != cls)
    {
        auto c_other = pyobject_to_c_float(other);
        if (PyErr_Occurred()){ Py_RETURN_NOTIMPLEMENTED; }
        vector = glm::pow((*self->glm), FVector3Glm(c_other));
    }
    else
    {
        vector = glm::pow((*self->glm), (*((FVector3 *)other)->glm));
    }

    FVector3 *result = (FVector3 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new FVector3Glm(

            vector[0],

            vector[1],

            vector[2]

    );

    return (PyObject *)result;
}


static PyObject *
FVector3__neg__(FVector3 *self)
{
    auto cls = Py_TYPE(self);
    FVector3Glm vector = -(*self->glm);

    FVector3 *result = (FVector3 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new FVector3Glm(

            vector[0],

            vector[1],

            vector[2]

    );

    return (PyObject *)result;
}


static PyObject *
FVector3__abs__(FVector3 *self)
{
    auto cls = Py_TYPE(self);
    FVector3Glm vector = glm::abs(*self->glm);

    FVector3 *result = (FVector3 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new FVector3Glm(

            vector[0],

            vector[1],

            vector[2]

    );

    return (PyObject *)result;
}


static int
FVector3__bool__(FVector3 *self)
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

    return 1;
}


static int
FVector3_getbufferproc(FVector3 *self, Py_buffer *view, int flags)
{
    if (flags & PyBUF_WRITABLE)
    {
        PyErr_SetString(PyExc_TypeError, "FVector3 is not read only");
        view->obj = 0;
        return -1;
    }
    view->buf = glm::value_ptr(*self->glm);
    view->obj = (PyObject *)self;
    view->len = sizeof(float) * 3;
    view->readonly = 1;
    view->itemsize = sizeof(float);
    view->format = "f";
    view->ndim = 1;
    static Py_ssize_t shape = 3;
    view->shape = &shape;
    view->strides = &view->itemsize;
    view->suboffsets = 0;
    view->internal = 0;
    Py_INCREF(self);
    return 0;
}



    static PyObject *
    FVector3_Getter_0(FVector3 *self, void *)
    {
        auto c = (*self->glm)[0];
        return c_float_to_pyobject(c);
    }

    static PyObject *
    FVector3_Getter_1(FVector3 *self, void *)
    {
        auto c = (*self->glm)[1];
        return c_float_to_pyobject(c);
    }

    static PyObject *
    FVector3_Getter_2(FVector3 *self, void *)
    {
        auto c = (*self->glm)[2];
        return c_float_to_pyobject(c);
    }



static PyObject *
FVector3_magnitude(FVector3 *self, void *)
{
    auto magnitude = glm::length(*self->glm);
    return c_float_to_pyobject(magnitude);
}


static PyGetSetDef FVector3_PyGetSetDef[] = {
    {"x", (getter)FVector3_Getter_0, 0, 0, 0},
    {"r", (getter)FVector3_Getter_0, 0, 0, 0},
    {"s", (getter)FVector3_Getter_0, 0, 0, 0},
    {"u", (getter)FVector3_Getter_0, 0, 0, 0},

        {"y", (getter)FVector3_Getter_1, 0, 0, 0},
        {"g", (getter)FVector3_Getter_1, 0, 0, 0},
        {"t", (getter)FVector3_Getter_1, 0, 0, 0},
        {"v", (getter)FVector3_Getter_1, 0, 0, 0},


        {"z", (getter)FVector3_Getter_2, 0, 0, 0},
        {"b", (getter)FVector3_Getter_2, 0, 0, 0},
        {"p", (getter)FVector3_Getter_2, 0, 0, 0},


    {"magnitude", (getter)FVector3_magnitude, 0, 0, 0},
    {0, 0, 0, 0, 0}
};


static PyObject *
FVector3__getattr__(FVector3 *self, PyObject *py_attr)
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


            default:
            {
                Py_DECREF(result);
                return 0;
            }
        }
        auto py_c = c_float_to_pyobject((*self->glm)[glm_index]);
        PyTuple_SET_ITEM(result, i, py_c);
    }

    PyErr_Clear();
    return result;
}


static PyMemberDef FVector3_PyMemberDef[] = {
    {"__weaklistoffset__", T_PYSSIZET, offsetof(FVector3, weakreflist), READONLY},
    {0}
};



    static FVector3 *
    FVector3_cross(FVector3 *self, FVector3 *other)
    {
        auto cls = Py_TYPE(self);
        if (Py_TYPE(other) != cls)
        {
            PyErr_Format(PyExc_TypeError, "%R is not FVector3", other);
            return 0;
        }
        auto vector = glm::cross(*self->glm, *other->glm);
        FVector3 *result = (FVector3 *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new FVector3Glm(

                vector[0],

                vector[1],

                vector[2]

        );
        return result;
    }



static FVector3 *
FVector3_normalize(FVector3 *self, void*)
{
    auto cls = Py_TYPE(self);
    auto vector = glm::normalize(*self->glm);
    FVector3 *result = (FVector3 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new FVector3Glm(

            vector[0],

            vector[1],

            vector[2]

    );
    return result;
}


static PyObject *
FVector3_distance(FVector3 *self, FVector3 *other)
{
    auto cls = Py_TYPE(self);
    if (Py_TYPE(other) != cls)
    {
        PyErr_Format(PyExc_TypeError, "%R is not FVector3", other);
        return 0;
    }
    auto result = glm::distance(*self->glm, *other->glm);
    return c_float_to_pyobject(result);
}


static PyMethodDef FVector3_PyMethodDef[] = {

        {"cross", (PyCFunction)FVector3_cross, METH_O, 0},

    {"normalize", (PyCFunction)FVector3_normalize, METH_NOARGS, 0},
    {"distance", (PyCFunction)FVector3_distance, METH_O, 0},
    {0, 0, 0, 0}
};


static PyType_Slot FVector3_PyType_Slots [] = {
    {Py_tp_new, (void*)FVector3__new__},
    {Py_tp_dealloc, (void*)FVector3__dealloc__},
    {Py_tp_hash, (void*)FVector3__hash__},
    {Py_tp_repr, (void*)FVector3__repr__},
    {Py_sq_length, (void*)FVector3__len__},
    {Py_sq_item, (void*)FVector3__getitem__},
    {Py_tp_richcompare, (void*)FVector3__richcmp__},
    {Py_nb_add, (void*)FVector3__add__},
    {Py_nb_subtract, (void*)FVector3__sub__},
    {Py_nb_multiply, (void*)FVector3__mul__},
    {Py_nb_matrix_multiply, (void*)FVector3__matmul__},
    {Py_nb_true_divide, (void*)FVector3__truediv__},
    {Py_nb_remainder, (void*)FVector3__mod__},
    {Py_nb_power, (void*)FVector3__pow__},
    {Py_nb_negative, (void*)FVector3__neg__},
    {Py_nb_absolute, (void*)FVector3__abs__},
    {Py_nb_bool, (void*)FVector3__bool__},
    {Py_bf_getbuffer, (void*)FVector3_getbufferproc},
    {Py_tp_getset, (void*)FVector3_PyGetSetDef},
    {Py_tp_getattro, (void*)FVector3__getattr__},
    {Py_tp_members, (void*)FVector3_PyMemberDef},
    {Py_tp_methods, (void*)FVector3_PyMethodDef},
    {0, 0},
};


static PyType_Spec FVector3_PyTypeSpec = {
    "gamut.math.FVector3",
    sizeof(FVector3),
    0,
    Py_TPFLAGS_DEFAULT,
    FVector3_PyType_Slots
};


static PyTypeObject *
define_FVector3_type(PyObject *module)
{
    PyTypeObject *type = (PyTypeObject *)PyType_FromModuleAndSpec(
        module,
        &FVector3_PyTypeSpec,
        0
    );
    if (!type){ return 0; }
    // Note:
    // Unlike other functions that steal references, PyModule_AddObject() only
    // decrements the reference count of value on success.
    if (PyModule_AddObject(module, "FVector3", (PyObject *)type) < 0)
    {
        Py_DECREF(type);
        return 0;
    }
    return type;
}