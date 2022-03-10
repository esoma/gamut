
// generated 2022-03-10 18:59:39.035560 from codegen/math/templates/_vector.hpp

#ifndef GAMUT_MATH_U8VECTOR4_HPP
#define GAMUT_MATH_U8VECTOR4_HPP

// stdlib
#include <limits>
#include <functional>
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

typedef glm::vec<4, uint8_t, glm::defaultp> U8Vector4Glm;


struct U8Vector4
{
    PyObject_HEAD
    PyObject *weakreflist;
    U8Vector4Glm *glm;
};


static PyObject *
U8Vector4__new__(PyTypeObject *cls, PyObject *args, PyObject *kwds)
{

        uint8_t c_0 = 0;

        uint8_t c_1 = 0;

        uint8_t c_2 = 0;

        uint8_t c_3 = 0;


    if (kwds && PyDict_Size(kwds) != 0)
    {
        PyErr_SetString(
            PyExc_TypeError,
            "U8Vector4 does accept any keyword arguments"
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
            uint8_t arg_c = pyobject_to_c_uint8_t(arg);
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
                c_0 = pyobject_to_c_uint8_t(arg);
                auto error_occurred = PyErr_Occurred();
                if (error_occurred){ return 0; }
            }

            {
                auto arg = PyTuple_GET_ITEM(args, 1);
                c_1 = pyobject_to_c_uint8_t(arg);
                auto error_occurred = PyErr_Occurred();
                if (error_occurred){ return 0; }
            }

            {
                auto arg = PyTuple_GET_ITEM(args, 2);
                c_2 = pyobject_to_c_uint8_t(arg);
                auto error_occurred = PyErr_Occurred();
                if (error_occurred){ return 0; }
            }

            {
                auto arg = PyTuple_GET_ITEM(args, 3);
                c_3 = pyobject_to_c_uint8_t(arg);
                auto error_occurred = PyErr_Occurred();
                if (error_occurred){ return 0; }
            }

            break;
        }
        default:
        {
            PyErr_Format(
                PyExc_TypeError,
                "invalid number of arguments supplied to U8Vector4, expected "
                "0, 1 or 4 (got %zd)",
                arg_count
            );
            return 0;
        }
    }

    U8Vector4 *self = (U8Vector4*)cls->tp_alloc(cls, 0);
    if (!self){ return 0; }
    self->glm = new U8Vector4Glm(

            c_0,

            c_1,

            c_2,

            c_3

    );

    return (PyObject *)self;
}


static void
U8Vector4__dealloc__(U8Vector4 *self)
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
U8Vector4__hash__(U8Vector4 *self)
{
    Py_ssize_t len = 4;
    Py_uhash_t acc = _HASH_XXPRIME_5;
    for (U8Vector4Glm::length_type i = 0; i < len; i++)
    {
        Py_uhash_t lane = std::hash<uint8_t>{}((*self->glm)[i]);
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
U8Vector4__repr__(U8Vector4 *self)
{
    PyObject *result = 0;

        PyObject *py_0 = 0;

        PyObject *py_1 = 0;

        PyObject *py_2 = 0;

        PyObject *py_3 = 0;



        py_0 = c_uint8_t_to_pyobject((*self->glm)[0]);
        if (!py_0){ goto cleanup; }

        py_1 = c_uint8_t_to_pyobject((*self->glm)[1]);
        if (!py_1){ goto cleanup; }

        py_2 = c_uint8_t_to_pyobject((*self->glm)[2]);
        if (!py_2){ goto cleanup; }

        py_3 = c_uint8_t_to_pyobject((*self->glm)[3]);
        if (!py_3){ goto cleanup; }

    result = PyUnicode_FromFormat(
        "U8Vector4("

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
U8Vector4__len__(U8Vector4 *self)
{
    return 4;
}


static PyObject *
U8Vector4__getitem__(U8Vector4 *self, Py_ssize_t index)
{
    if (index < 0 || index > 3)
    {
        PyErr_Format(PyExc_IndexError, "index out of range");
        return 0;
    }
    auto c = (*self->glm)[(U8Vector4Glm::length_type)index];
    return c_uint8_t_to_pyobject(c);
}


static PyObject *
U8Vector4__richcmp__(U8Vector4 *self, U8Vector4 *other, int op)
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
U8Vector4__add__(PyObject *left, PyObject *right)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->U8Vector4_PyTypeObject;

    U8Vector4Glm vector;
    if (Py_TYPE(left) == Py_TYPE(right))
    {
        vector = (*((U8Vector4 *)left)->glm) + (*((U8Vector4 *)right)->glm);
    }
    else
    {
        if (Py_TYPE(left) == cls)
        {
            auto c_right = pyobject_to_c_uint8_t(right);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
            vector = (*((U8Vector4 *)left)->glm) + c_right;
        }
        else
        {
            auto c_left = pyobject_to_c_uint8_t(left);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
            vector = c_left + (*((U8Vector4 *)right)->glm);
        }
    }

    U8Vector4 *result = (U8Vector4 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new U8Vector4Glm(

            vector[0],

            vector[1],

            vector[2],

            vector[3]

    );

    return (PyObject *)result;
}


static PyObject *
U8Vector4__sub__(PyObject *left, PyObject *right)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->U8Vector4_PyTypeObject;

    U8Vector4Glm vector;
    if (Py_TYPE(left) == Py_TYPE(right))
    {
        vector = (*((U8Vector4 *)left)->glm) - (*((U8Vector4 *)right)->glm);
    }
    else
    {
        if (Py_TYPE(left) == cls)
        {
            auto c_right = pyobject_to_c_uint8_t(right);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
            vector = (*((U8Vector4 *)left)->glm) - c_right;
        }
        else
        {
            auto c_left = pyobject_to_c_uint8_t(left);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
            vector = c_left - (*((U8Vector4 *)right)->glm);
        }
    }

    U8Vector4 *result = (U8Vector4 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new U8Vector4Glm(

            vector[0],

            vector[1],

            vector[2],

            vector[3]

    );

    return (PyObject *)result;
}


static PyObject *
U8Vector4__mul__(PyObject *left, PyObject *right)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->U8Vector4_PyTypeObject;

    U8Vector4Glm vector;
    if (Py_TYPE(left) == Py_TYPE(right))
    {
        vector = (*((U8Vector4 *)left)->glm) * (*((U8Vector4 *)right)->glm);
    }
    else
    {
        if (Py_TYPE(left) == cls)
        {
            auto c_right = pyobject_to_c_uint8_t(right);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
            vector = (*((U8Vector4 *)left)->glm) * c_right;
        }
        else
        {
            auto c_left = pyobject_to_c_uint8_t(left);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
            vector = c_left * (*((U8Vector4 *)right)->glm);
        }
    }

    U8Vector4 *result = (U8Vector4 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new U8Vector4Glm(

            vector[0],

            vector[1],

            vector[2],

            vector[3]

    );

    return (PyObject *)result;
}







    static PyObject *
    U8Vector4__truediv__(PyObject *left, PyObject *right)
    {
        auto module_state = get_module_state();
        if (!module_state){ return 0; }
        auto cls = module_state->U8Vector4_PyTypeObject;

        U8Vector4Glm vector;
        if (Py_TYPE(left) == Py_TYPE(right))
        {

                if (

                        (*((U8Vector4 *)right)->glm)[0] == 0 ||

                        (*((U8Vector4 *)right)->glm)[1] == 0 ||

                        (*((U8Vector4 *)right)->glm)[2] == 0 ||

                        (*((U8Vector4 *)right)->glm)[3] == 0

                )
                {
                    PyErr_SetString(PyExc_ZeroDivisionError, "divide by zero");
                    return 0;
                }

            vector = (*((U8Vector4 *)left)->glm) / (*((U8Vector4 *)right)->glm);
        }
        else
        {
            if (Py_TYPE(left) == cls)
            {
                auto c_right = pyobject_to_c_uint8_t(right);
                if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }

                    if (c_right == 0)
                    {
                        PyErr_SetString(PyExc_ZeroDivisionError, "divide by zero");
                        return 0;
                    }

                vector = (*((U8Vector4 *)left)->glm) / c_right;
            }
            else
            {
                auto c_left = pyobject_to_c_uint8_t(left);
                if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }

                    if (

                            (*((U8Vector4 *)right)->glm)[0] == 0 ||

                            (*((U8Vector4 *)right)->glm)[1] == 0 ||

                            (*((U8Vector4 *)right)->glm)[2] == 0 ||

                            (*((U8Vector4 *)right)->glm)[3] == 0

                    )
                    {
                        PyErr_SetString(PyExc_ZeroDivisionError, "divide by zero");
                        return 0;
                    }

                vector = c_left / (*((U8Vector4 *)right)->glm);
            }
        }

        U8Vector4 *result = (U8Vector4 *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new U8Vector4Glm(

                vector[0],

                vector[1],

                vector[2],

                vector[3]

        );

        return (PyObject *)result;
    }






static PyObject *
U8Vector4__abs__(U8Vector4 *self)
{
    auto cls = Py_TYPE(self);
    U8Vector4Glm vector = glm::abs(*self->glm);

    U8Vector4 *result = (U8Vector4 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new U8Vector4Glm(

            vector[0],

            vector[1],

            vector[2],

            vector[3]

    );

    return (PyObject *)result;
}


static int
U8Vector4__bool__(U8Vector4 *self)
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
U8Vector4_getbufferproc(U8Vector4 *self, Py_buffer *view, int flags)
{
    if (flags & PyBUF_WRITABLE)
    {
        PyErr_SetString(PyExc_TypeError, "U8Vector4 is read only");
        view->obj = 0;
        return -1;
    }
    view->buf = glm::value_ptr(*self->glm);
    view->obj = (PyObject *)self;
    view->len = sizeof(uint8_t) * 4;
    view->readonly = 1;
    view->itemsize = sizeof(uint8_t);
    view->format = "=B";
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
    U8Vector4_Getter_0(U8Vector4 *self, void *)
    {
        auto c = (*self->glm)[0];
        return c_uint8_t_to_pyobject(c);
    }

    static PyObject *
    U8Vector4_Getter_1(U8Vector4 *self, void *)
    {
        auto c = (*self->glm)[1];
        return c_uint8_t_to_pyobject(c);
    }

    static PyObject *
    U8Vector4_Getter_2(U8Vector4 *self, void *)
    {
        auto c = (*self->glm)[2];
        return c_uint8_t_to_pyobject(c);
    }

    static PyObject *
    U8Vector4_Getter_3(U8Vector4 *self, void *)
    {
        auto c = (*self->glm)[3];
        return c_uint8_t_to_pyobject(c);
    }






static PyGetSetDef U8Vector4_PyGetSetDef[] = {
    {"x", (getter)U8Vector4_Getter_0, 0, 0, 0},
    {"r", (getter)U8Vector4_Getter_0, 0, 0, 0},
    {"s", (getter)U8Vector4_Getter_0, 0, 0, 0},
    {"u", (getter)U8Vector4_Getter_0, 0, 0, 0},

        {"y", (getter)U8Vector4_Getter_1, 0, 0, 0},
        {"g", (getter)U8Vector4_Getter_1, 0, 0, 0},
        {"t", (getter)U8Vector4_Getter_1, 0, 0, 0},
        {"v", (getter)U8Vector4_Getter_1, 0, 0, 0},


        {"z", (getter)U8Vector4_Getter_2, 0, 0, 0},
        {"b", (getter)U8Vector4_Getter_2, 0, 0, 0},
        {"p", (getter)U8Vector4_Getter_2, 0, 0, 0},


        {"w", (getter)U8Vector4_Getter_3, 0, 0, 0},
        {"a", (getter)U8Vector4_Getter_3, 0, 0, 0},
        {"q", (getter)U8Vector4_Getter_3, 0, 0, 0},


    {0, 0, 0, 0, 0}
};


static PyObject *
U8Vector4__getattr__(U8Vector4 *self, PyObject *py_attr)
{
    PyObject *result = PyObject_GenericGetAttr((PyObject *)self, py_attr);
    if (result != 0){ return result; }

    auto attr_length = PyUnicode_GET_LENGTH(py_attr);
    if (attr_length == 1){ return 0; }

    result = PyTuple_New(attr_length);
    if (!result){ return 0; }

    const char *attr = PyUnicode_AsUTF8(py_attr);
    if (!attr){ return 0; }
    for (U8Vector4Glm::length_type i = 0; i < attr_length; i++)
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
        auto py_c = c_uint8_t_to_pyobject((*self->glm)[glm_index]);
        PyTuple_SET_ITEM(result, i, py_c);
    }

    PyErr_Clear();
    return result;
}


static PyMemberDef U8Vector4_PyMemberDef[] = {
    {"__weaklistoffset__", T_PYSSIZET, offsetof(U8Vector4, weakreflist), READONLY},
    {0}
};





static PyObject *
U8Vector4_get_limits(U8Vector4 *self, void *)
{
    auto c_min = std::numeric_limits<uint8_t>::lowest();
    auto c_max = std::numeric_limits<uint8_t>::max();
    auto py_min = c_uint8_t_to_pyobject(c_min);
    if (!py_min){ return 0; }
    auto py_max = c_uint8_t_to_pyobject(c_max);
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


static PyMethodDef U8Vector4_PyMethodDef[] = {

    {"get_limits", (PyCFunction)U8Vector4_get_limits, METH_NOARGS | METH_STATIC, 0},
    {0, 0, 0, 0}
};


static PyType_Slot U8Vector4_PyType_Slots [] = {
    {Py_tp_new, (void*)U8Vector4__new__},
    {Py_tp_dealloc, (void*)U8Vector4__dealloc__},
    {Py_tp_hash, (void*)U8Vector4__hash__},
    {Py_tp_repr, (void*)U8Vector4__repr__},
    {Py_sq_length, (void*)U8Vector4__len__},
    {Py_sq_item, (void*)U8Vector4__getitem__},
    {Py_tp_richcompare, (void*)U8Vector4__richcmp__},
    {Py_nb_add, (void*)U8Vector4__add__},
    {Py_nb_subtract, (void*)U8Vector4__sub__},
    {Py_nb_multiply, (void*)U8Vector4__mul__},


        {Py_nb_true_divide, (void*)U8Vector4__truediv__},


    {Py_nb_absolute, (void*)U8Vector4__abs__},
    {Py_nb_bool, (void*)U8Vector4__bool__},
    {Py_bf_getbuffer, (void*)U8Vector4_getbufferproc},
    {Py_tp_getset, (void*)U8Vector4_PyGetSetDef},
    {Py_tp_getattro, (void*)U8Vector4__getattr__},
    {Py_tp_members, (void*)U8Vector4_PyMemberDef},
    {Py_tp_methods, (void*)U8Vector4_PyMethodDef},
    {0, 0},
};


static PyType_Spec U8Vector4_PyTypeSpec = {
    "gamut.math.U8Vector4",
    sizeof(U8Vector4),
    0,
    Py_TPFLAGS_DEFAULT,
    U8Vector4_PyType_Slots
};


static PyTypeObject *
define_U8Vector4_type(PyObject *module)
{
    PyTypeObject *type = (PyTypeObject *)PyType_FromModuleAndSpec(
        module,
        &U8Vector4_PyTypeSpec,
        0
    );
    if (!type){ return 0; }
    // Note:
    // Unlike other functions that steal references, PyModule_AddObject() only
    // decrements the reference count of value on success.
    if (PyModule_AddObject(module, "U8Vector4", (PyObject *)type) < 0)
    {
        Py_DECREF(type);
        return 0;
    }
    return type;
}




#endif