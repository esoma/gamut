// generated 2022-03-07 03:05:30.758375

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

typedef glm::vec<4, double, glm::defaultp> DVector4Glm;


struct DVector4
{
    PyObject_HEAD
    PyObject *weakreflist;
    DVector4Glm *glm;
};


static PyObject *
DVector4__new__(PyTypeObject *cls, PyObject *args, PyObject *kwds)
{

        double c_0 = 0;

        double c_1 = 0;

        double c_2 = 0;

        double c_3 = 0;


    if (kwds && PyDict_Size(kwds) != 0)
    {
        PyErr_SetString(
            PyExc_TypeError,
            "DVector4 does accept any keyword arguments"
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

                c_2 = arg_c;

                c_3 = arg_c;

            break;
        }
        case 4:
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

            {
                auto arg = PyTuple_GET_ITEM(args, 2);
                c_2 = pyobject_to_c_double(arg);
                auto error_occurred = PyErr_Occurred();
                if (error_occurred){ return 0; }
            }

            {
                auto arg = PyTuple_GET_ITEM(args, 3);
                c_3 = pyobject_to_c_double(arg);
                auto error_occurred = PyErr_Occurred();
                if (error_occurred){ return 0; }
            }

            break;
        }
        default:
        {
            PyErr_Format(
                PyExc_TypeError,
                "invalid number of arguments supplied to DVector4, expected "
                "0, 1 or 4 (got %zd)",
                arg_count
            );
            return 0;
        }
    }

    DVector4 *self = (DVector4*)cls->tp_alloc(cls, 0);
    if (!self){ return 0; }
    self->glm = new DVector4Glm(

            c_0,

            c_1,

            c_2,

            c_3

    );

    return (PyObject *)self;
}


static void
DVector4__dealloc__(DVector4 *self)
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
DVector4__hash__(DVector4 *self)
{
    Py_hash_t hash = 0;

        hash ^= (Py_hash_t)(*self->glm)[0];

        hash ^= (Py_hash_t)(*self->glm)[1];

        hash ^= (Py_hash_t)(*self->glm)[2];

        hash ^= (Py_hash_t)(*self->glm)[3];

    if (hash == -1){ hash = -123456789; }
    return hash;
}


static PyObject *
DVector4__repr__(DVector4 *self)
{
    PyObject *result = 0;

        PyObject *py_0 = 0;

        PyObject *py_1 = 0;

        PyObject *py_2 = 0;

        PyObject *py_3 = 0;



        py_0 = c_double_to_pyobject((*self->glm)[0]);
        if (!py_0){ goto cleanup; }

        py_1 = c_double_to_pyobject((*self->glm)[1]);
        if (!py_1){ goto cleanup; }

        py_2 = c_double_to_pyobject((*self->glm)[2]);
        if (!py_2){ goto cleanup; }

        py_3 = c_double_to_pyobject((*self->glm)[3]);
        if (!py_3){ goto cleanup; }

    result = PyUnicode_FromFormat(
        "DVector4("

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
DVector4__len__(DVector4 *self)
{
    return 4;
}


static PyObject *
DVector4__getitem__(DVector4 *self, Py_ssize_t index)
{
    if (index < 0 || index > 3)
    {
        PyErr_Format(PyExc_IndexError, "index out of range");
        return 0;
    }
    auto c = (*self->glm)[index];
    return c_double_to_pyobject(c);
}


static PyObject *
DVector4__richcmp__(DVector4 *self, DVector4 *other, int op)
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
DVector4__add__(DVector4 *self, PyObject *other)
{
    auto cls = Py_TYPE(self);
    DVector4Glm vector;
    if (Py_TYPE(other) != cls)
    {
        auto c_other = pyobject_to_c_double(other);
        if (PyErr_Occurred()){ Py_RETURN_NOTIMPLEMENTED; }
        vector = (*self->glm) + c_other;
    }
    else
    {
        vector = (*self->glm) + (*((DVector4 *)other)->glm);
    }

    DVector4 *result = (DVector4 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new DVector4Glm(

            vector[0],

            vector[1],

            vector[2],

            vector[3]

    );

    return (PyObject *)result;
}


static PyObject *
DVector4__sub__(DVector4 *self, PyObject *other)
{
    auto cls = Py_TYPE(self);
    DVector4Glm vector;
    if (Py_TYPE(other) != cls)
    {
        auto c_other = pyobject_to_c_double(other);
        if (PyErr_Occurred()){ Py_RETURN_NOTIMPLEMENTED; }
        vector = (*self->glm) - c_other;
    }
    else
    {
        vector = (*self->glm) - (*((DVector4 *)other)->glm);
    }

    DVector4 *result = (DVector4 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new DVector4Glm(

            vector[0],

            vector[1],

            vector[2],

            vector[3]

    );

    return (PyObject *)result;
}


static PyObject *
DVector4__mul__(DVector4 *self, PyObject *other)
{
    auto cls = Py_TYPE(self);
    DVector4Glm vector;
    if (Py_TYPE(other) != cls)
    {
        auto c_other = pyobject_to_c_double(other);
        if (PyErr_Occurred()){ Py_RETURN_NOTIMPLEMENTED; }
        vector = (*self->glm) * c_other;
    }
    else
    {
        vector = (*self->glm) * (*((DVector4 *)other)->glm);
    }

    DVector4 *result = (DVector4 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new DVector4Glm(

            vector[0],

            vector[1],

            vector[2],

            vector[3]

    );

    return (PyObject *)result;
}


static PyObject *
DVector4__matmul__(DVector4 *self, DVector4 *other)
{
    auto cls = Py_TYPE(self);
    if (Py_TYPE(other) != cls){ Py_RETURN_NOTIMPLEMENTED; }
    auto c_result = glm::dot(*self->glm, *other->glm);
    return c_double_to_pyobject(c_result);
}


static PyObject *
DVector4__truediv__(DVector4 *self, PyObject *other)
{
    auto cls = Py_TYPE(self);
    DVector4Glm vector;
    if (Py_TYPE(other) != cls)
    {
        auto c_other = pyobject_to_c_double(other);
        if (PyErr_Occurred()){ Py_RETURN_NOTIMPLEMENTED; }
        vector = (*self->glm) / c_other;
    }
    else
    {
        vector = (*self->glm) / (*((DVector4 *)other)->glm);
    }

    DVector4 *result = (DVector4 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new DVector4Glm(

            vector[0],

            vector[1],

            vector[2],

            vector[3]

    );

    return (PyObject *)result;
}


static PyObject *
DVector4__mod__(DVector4 *self, PyObject *other)
{
    auto cls = Py_TYPE(self);
    DVector4Glm vector;
    if (Py_TYPE(other) != cls)
    {
        auto c_other = pyobject_to_c_double(other);
        if (PyErr_Occurred()){ Py_RETURN_NOTIMPLEMENTED; }
        vector = glm::mod((*self->glm), c_other);
    }
    else
    {
        vector = glm::mod((*self->glm), (*((DVector4 *)other)->glm));
    }

    DVector4 *result = (DVector4 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new DVector4Glm(

            vector[0],

            vector[1],

            vector[2],

            vector[3]

    );

    return (PyObject *)result;
}


static PyObject *
DVector4__pow__(DVector4 *self, PyObject *other)
{
    auto cls = Py_TYPE(self);
    DVector4Glm vector;
    if (Py_TYPE(other) != cls)
    {
        auto c_other = pyobject_to_c_double(other);
        if (PyErr_Occurred()){ Py_RETURN_NOTIMPLEMENTED; }
        vector = glm::pow((*self->glm), DVector4Glm(c_other));
    }
    else
    {
        vector = glm::pow((*self->glm), (*((DVector4 *)other)->glm));
    }

    DVector4 *result = (DVector4 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new DVector4Glm(

            vector[0],

            vector[1],

            vector[2],

            vector[3]

    );

    return (PyObject *)result;
}


static PyObject *
DVector4__neg__(DVector4 *self)
{
    auto cls = Py_TYPE(self);
    DVector4Glm vector = -(*self->glm);

    DVector4 *result = (DVector4 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new DVector4Glm(

            vector[0],

            vector[1],

            vector[2],

            vector[3]

    );

    return (PyObject *)result;
}


static PyObject *
DVector4__abs__(DVector4 *self)
{
    auto cls = Py_TYPE(self);
    DVector4Glm vector = glm::abs(*self->glm);

    DVector4 *result = (DVector4 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new DVector4Glm(

            vector[0],

            vector[1],

            vector[2],

            vector[3]

    );

    return (PyObject *)result;
}


static int
DVector4__bool__(DVector4 *self)
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
DVector4_getbufferproc(DVector4 *self, Py_buffer *view, int flags)
{
    if (flags & PyBUF_WRITABLE)
    {
        PyErr_SetString(PyExc_TypeError, "DVector4 is not read only");
        view->obj = 0;
        return -1;
    }
    view->buf = glm::value_ptr(*self->glm);
    view->obj = (PyObject *)self;
    view->len = sizeof(double) * 4;
    view->readonly = 1;
    view->itemsize = sizeof(double);
    view->format = "d";
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
    DVector4_Getter_0(DVector4 *self, void *)
    {
        auto c = (*self->glm)[0];
        return c_double_to_pyobject(c);
    }

    static PyObject *
    DVector4_Getter_1(DVector4 *self, void *)
    {
        auto c = (*self->glm)[1];
        return c_double_to_pyobject(c);
    }

    static PyObject *
    DVector4_Getter_2(DVector4 *self, void *)
    {
        auto c = (*self->glm)[2];
        return c_double_to_pyobject(c);
    }

    static PyObject *
    DVector4_Getter_3(DVector4 *self, void *)
    {
        auto c = (*self->glm)[3];
        return c_double_to_pyobject(c);
    }



static PyObject *
DVector4_magnitude(DVector4 *self, void *)
{
    auto magnitude = glm::length(*self->glm);
    return c_double_to_pyobject(magnitude);
}


static PyGetSetDef DVector4_PyGetSetDef[] = {
    {"x", (getter)DVector4_Getter_0, 0, 0, 0},
    {"r", (getter)DVector4_Getter_0, 0, 0, 0},
    {"s", (getter)DVector4_Getter_0, 0, 0, 0},
    {"u", (getter)DVector4_Getter_0, 0, 0, 0},

        {"y", (getter)DVector4_Getter_1, 0, 0, 0},
        {"g", (getter)DVector4_Getter_1, 0, 0, 0},
        {"t", (getter)DVector4_Getter_1, 0, 0, 0},
        {"v", (getter)DVector4_Getter_1, 0, 0, 0},


        {"z", (getter)DVector4_Getter_2, 0, 0, 0},
        {"b", (getter)DVector4_Getter_2, 0, 0, 0},
        {"p", (getter)DVector4_Getter_2, 0, 0, 0},


        {"w", (getter)DVector4_Getter_3, 0, 0, 0},
        {"a", (getter)DVector4_Getter_3, 0, 0, 0},
        {"q", (getter)DVector4_Getter_3, 0, 0, 0},

    {"magnitude", (getter)DVector4_magnitude, 0, 0, 0},
    {0, 0, 0, 0, 0}
};


static PyObject *
DVector4__getattr__(DVector4 *self, PyObject *py_attr)
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
        auto py_c = c_double_to_pyobject((*self->glm)[glm_index]);
        PyTuple_SET_ITEM(result, i, py_c);
    }

    PyErr_Clear();
    return result;
}


static PyMemberDef DVector4_PyMemberDef[] = {
    {"__weaklistoffset__", T_PYSSIZET, offsetof(DVector4, weakreflist), READONLY},
    {0}
};





static DVector4 *
DVector4_normalize(DVector4 *self, void*)
{
    auto cls = Py_TYPE(self);
    auto vector = glm::normalize(*self->glm);
    DVector4 *result = (DVector4 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new DVector4Glm(

            vector[0],

            vector[1],

            vector[2],

            vector[3]

    );
    return result;
}


static PyObject *
DVector4_distance(DVector4 *self, DVector4 *other)
{
    auto cls = Py_TYPE(self);
    if (Py_TYPE(other) != cls)
    {
        PyErr_Format(PyExc_TypeError, "%R is not DVector4", other);
        return 0;
    }
    auto result = glm::distance(*self->glm, *other->glm);
    return c_double_to_pyobject(result);
}


static PyMethodDef DVector4_PyMethodDef[] = {

    {"normalize", (PyCFunction)DVector4_normalize, METH_NOARGS, 0},
    {"distance", (PyCFunction)DVector4_distance, METH_O, 0},
    {0, 0, 0, 0}
};


static PyType_Slot DVector4_PyType_Slots [] = {
    {Py_tp_new, (void*)DVector4__new__},
    {Py_tp_dealloc, (void*)DVector4__dealloc__},
    {Py_tp_hash, (void*)DVector4__hash__},
    {Py_tp_repr, (void*)DVector4__repr__},
    {Py_sq_length, (void*)DVector4__len__},
    {Py_sq_item, (void*)DVector4__getitem__},
    {Py_tp_richcompare, (void*)DVector4__richcmp__},
    {Py_nb_add, (void*)DVector4__add__},
    {Py_nb_subtract, (void*)DVector4__sub__},
    {Py_nb_multiply, (void*)DVector4__mul__},
    {Py_nb_matrix_multiply, (void*)DVector4__matmul__},
    {Py_nb_true_divide, (void*)DVector4__truediv__},
    {Py_nb_remainder, (void*)DVector4__mod__},
    {Py_nb_power, (void*)DVector4__pow__},
    {Py_nb_negative, (void*)DVector4__neg__},
    {Py_nb_absolute, (void*)DVector4__abs__},
    {Py_nb_bool, (void*)DVector4__bool__},
    {Py_bf_getbuffer, (void*)DVector4_getbufferproc},
    {Py_tp_getset, (void*)DVector4_PyGetSetDef},
    {Py_tp_getattro, (void*)DVector4__getattr__},
    {Py_tp_members, (void*)DVector4_PyMemberDef},
    {Py_tp_methods, (void*)DVector4_PyMethodDef},
    {0, 0},
};


static PyType_Spec DVector4_PyTypeSpec = {
    "gamut.math.DVector4",
    sizeof(DVector4),
    0,
    Py_TPFLAGS_DEFAULT,
    DVector4_PyType_Slots
};


static PyTypeObject *
define_DVector4_type(PyObject *module)
{
    PyTypeObject *type = (PyTypeObject *)PyType_FromModuleAndSpec(
        module,
        &DVector4_PyTypeSpec,
        0
    );
    if (!type){ return 0; }
    // Note:
    // Unlike other functions that steal references, PyModule_AddObject() only
    // decrements the reference count of value on success.
    if (PyModule_AddObject(module, "DVector4", (PyObject *)type) < 0)
    {
        Py_DECREF(type);
        return 0;
    }
    return type;
}