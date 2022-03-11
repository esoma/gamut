
// generated 2022-03-10 23:24:28.425432 from codegen/math/templates/_vector.hpp

#ifndef GAMUT_MATH_UVECTOR3_HPP
#define GAMUT_MATH_UVECTOR3_HPP

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
#include "_vectortype.hpp"
#include "_type.hpp"


static PyObject *
UVector3__new__(PyTypeObject *cls, PyObject *args, PyObject *kwds)
{

        unsigned int c_0 = 0;

        unsigned int c_1 = 0;

        unsigned int c_2 = 0;


    if (kwds && PyDict_Size(kwds) != 0)
    {
        PyErr_SetString(
            PyExc_TypeError,
            "UVector3 does accept any keyword arguments"
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
            unsigned int arg_c = pyobject_to_c_unsigned_int(arg);
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
                c_0 = pyobject_to_c_unsigned_int(arg);
                auto error_occurred = PyErr_Occurred();
                if (error_occurred){ return 0; }
            }

            {
                auto arg = PyTuple_GET_ITEM(args, 1);
                c_1 = pyobject_to_c_unsigned_int(arg);
                auto error_occurred = PyErr_Occurred();
                if (error_occurred){ return 0; }
            }

            {
                auto arg = PyTuple_GET_ITEM(args, 2);
                c_2 = pyobject_to_c_unsigned_int(arg);
                auto error_occurred = PyErr_Occurred();
                if (error_occurred){ return 0; }
            }

            break;
        }
        default:
        {
            PyErr_Format(
                PyExc_TypeError,
                "invalid number of arguments supplied to UVector3, expected "
                "0, 1 or 3 (got %zd)",
                arg_count
            );
            return 0;
        }
    }

    UVector3 *self = (UVector3*)cls->tp_alloc(cls, 0);
    if (!self){ return 0; }
    self->glm = new UVector3Glm(

            c_0,

            c_1,

            c_2

    );

    return (PyObject *)self;
}


static void
UVector3__dealloc__(UVector3 *self)
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
UVector3__hash__(UVector3 *self)
{
    Py_ssize_t len = 3;
    Py_uhash_t acc = _HASH_XXPRIME_5;
    for (UVector3Glm::length_type i = 0; i < len; i++)
    {
        Py_uhash_t lane = std::hash<unsigned int>{}((*self->glm)[i]);
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
UVector3__repr__(UVector3 *self)
{
    PyObject *result = 0;

        PyObject *py_0 = 0;

        PyObject *py_1 = 0;

        PyObject *py_2 = 0;



        py_0 = c_unsigned_int_to_pyobject((*self->glm)[0]);
        if (!py_0){ goto cleanup; }

        py_1 = c_unsigned_int_to_pyobject((*self->glm)[1]);
        if (!py_1){ goto cleanup; }

        py_2 = c_unsigned_int_to_pyobject((*self->glm)[2]);
        if (!py_2){ goto cleanup; }

    result = PyUnicode_FromFormat(
        "UVector3("

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
UVector3__len__(UVector3 *self)
{
    return 3;
}


static PyObject *
UVector3__getitem__(UVector3 *self, Py_ssize_t index)
{
    if (index < 0 || index > 2)
    {
        PyErr_Format(PyExc_IndexError, "index out of range");
        return 0;
    }
    auto c = (*self->glm)[(UVector3Glm::length_type)index];
    return c_unsigned_int_to_pyobject(c);
}


static PyObject *
UVector3__richcmp__(UVector3 *self, UVector3 *other, int op)
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
UVector3__add__(PyObject *left, PyObject *right)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->UVector3_PyTypeObject;

    UVector3Glm vector;
    if (Py_TYPE(left) == Py_TYPE(right))
    {
        vector = (*((UVector3 *)left)->glm) + (*((UVector3 *)right)->glm);
    }
    else
    {
        if (Py_TYPE(left) == cls)
        {
            auto c_right = pyobject_to_c_unsigned_int(right);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
            vector = (*((UVector3 *)left)->glm) + c_right;
        }
        else
        {
            auto c_left = pyobject_to_c_unsigned_int(left);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
            vector = c_left + (*((UVector3 *)right)->glm);
        }
    }

    UVector3 *result = (UVector3 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new UVector3Glm(

            vector[0],

            vector[1],

            vector[2]

    );

    return (PyObject *)result;
}


static PyObject *
UVector3__sub__(PyObject *left, PyObject *right)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->UVector3_PyTypeObject;

    UVector3Glm vector;
    if (Py_TYPE(left) == Py_TYPE(right))
    {
        vector = (*((UVector3 *)left)->glm) - (*((UVector3 *)right)->glm);
    }
    else
    {
        if (Py_TYPE(left) == cls)
        {
            auto c_right = pyobject_to_c_unsigned_int(right);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
            vector = (*((UVector3 *)left)->glm) - c_right;
        }
        else
        {
            auto c_left = pyobject_to_c_unsigned_int(left);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
            vector = c_left - (*((UVector3 *)right)->glm);
        }
    }

    UVector3 *result = (UVector3 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new UVector3Glm(

            vector[0],

            vector[1],

            vector[2]

    );

    return (PyObject *)result;
}


static PyObject *
UVector3__mul__(PyObject *left, PyObject *right)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->UVector3_PyTypeObject;

    UVector3Glm vector;
    if (Py_TYPE(left) == Py_TYPE(right))
    {
        vector = (*((UVector3 *)left)->glm) * (*((UVector3 *)right)->glm);
    }
    else
    {
        if (Py_TYPE(left) == cls)
        {
            auto c_right = pyobject_to_c_unsigned_int(right);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
            vector = (*((UVector3 *)left)->glm) * c_right;
        }
        else
        {
            auto c_left = pyobject_to_c_unsigned_int(left);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
            vector = c_left * (*((UVector3 *)right)->glm);
        }
    }

    UVector3 *result = (UVector3 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new UVector3Glm(

            vector[0],

            vector[1],

            vector[2]

    );

    return (PyObject *)result;
}







    static PyObject *
    UVector3__truediv__(PyObject *left, PyObject *right)
    {
        auto module_state = get_module_state();
        if (!module_state){ return 0; }
        auto cls = module_state->UVector3_PyTypeObject;

        UVector3Glm vector;
        if (Py_TYPE(left) == Py_TYPE(right))
        {

                if (

                        (*((UVector3 *)right)->glm)[0] == 0 ||

                        (*((UVector3 *)right)->glm)[1] == 0 ||

                        (*((UVector3 *)right)->glm)[2] == 0

                )
                {
                    PyErr_SetString(PyExc_ZeroDivisionError, "divide by zero");
                    return 0;
                }

            vector = (*((UVector3 *)left)->glm) / (*((UVector3 *)right)->glm);
        }
        else
        {
            if (Py_TYPE(left) == cls)
            {
                auto c_right = pyobject_to_c_unsigned_int(right);
                if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }

                    if (c_right == 0)
                    {
                        PyErr_SetString(PyExc_ZeroDivisionError, "divide by zero");
                        return 0;
                    }

                vector = (*((UVector3 *)left)->glm) / c_right;
            }
            else
            {
                auto c_left = pyobject_to_c_unsigned_int(left);
                if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }

                    if (

                            (*((UVector3 *)right)->glm)[0] == 0 ||

                            (*((UVector3 *)right)->glm)[1] == 0 ||

                            (*((UVector3 *)right)->glm)[2] == 0

                    )
                    {
                        PyErr_SetString(PyExc_ZeroDivisionError, "divide by zero");
                        return 0;
                    }

                vector = c_left / (*((UVector3 *)right)->glm);
            }
        }

        UVector3 *result = (UVector3 *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new UVector3Glm(

                vector[0],

                vector[1],

                vector[2]

        );

        return (PyObject *)result;
    }






static PyObject *
UVector3__abs__(UVector3 *self)
{
    auto cls = Py_TYPE(self);
    UVector3Glm vector = glm::abs(*self->glm);

    UVector3 *result = (UVector3 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new UVector3Glm(

            vector[0],

            vector[1],

            vector[2]

    );

    return (PyObject *)result;
}


static int
UVector3__bool__(UVector3 *self)
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
UVector3_getbufferproc(UVector3 *self, Py_buffer *view, int flags)
{
    if (flags & PyBUF_WRITABLE)
    {
        PyErr_SetString(PyExc_TypeError, "UVector3 is read only");
        view->obj = 0;
        return -1;
    }
    view->buf = glm::value_ptr(*self->glm);
    view->obj = (PyObject *)self;
    view->len = sizeof(unsigned int) * 3;
    view->readonly = 1;
    view->itemsize = sizeof(unsigned int);
    view->format = "I";
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
    UVector3_Getter_0(UVector3 *self, void *)
    {
        auto c = (*self->glm)[0];
        return c_unsigned_int_to_pyobject(c);
    }

    static PyObject *
    UVector3_Getter_1(UVector3 *self, void *)
    {
        auto c = (*self->glm)[1];
        return c_unsigned_int_to_pyobject(c);
    }

    static PyObject *
    UVector3_Getter_2(UVector3 *self, void *)
    {
        auto c = (*self->glm)[2];
        return c_unsigned_int_to_pyobject(c);
    }






static PyGetSetDef UVector3_PyGetSetDef[] = {
    {"x", (getter)UVector3_Getter_0, 0, 0, 0},
    {"r", (getter)UVector3_Getter_0, 0, 0, 0},
    {"s", (getter)UVector3_Getter_0, 0, 0, 0},
    {"u", (getter)UVector3_Getter_0, 0, 0, 0},

        {"y", (getter)UVector3_Getter_1, 0, 0, 0},
        {"g", (getter)UVector3_Getter_1, 0, 0, 0},
        {"t", (getter)UVector3_Getter_1, 0, 0, 0},
        {"v", (getter)UVector3_Getter_1, 0, 0, 0},


        {"z", (getter)UVector3_Getter_2, 0, 0, 0},
        {"b", (getter)UVector3_Getter_2, 0, 0, 0},
        {"p", (getter)UVector3_Getter_2, 0, 0, 0},



    {0, 0, 0, 0, 0}
};



    static PyObject *
    swizzle_2_UVector3(UVector3 *self, PyObject *py_attr)
    {
        const char *attr = PyUnicode_AsUTF8(py_attr);
        if (!attr){ return 0; }

        UVector2Glm vec;
        for (int i = 0; i < 2; i++)
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
                    PyErr_Format(
                        PyExc_AttributeError,
                        "invalid swizzle: %R", py_attr
                    );
                    return 0;
                }
            }
            vec[i] = (*self->glm)[glm_index];
        }

        auto module_state = get_module_state();
        if (!module_state){ return 0; }
        auto cls = module_state->UVector2_PyTypeObject;

        UVector2 *result = (UVector2 *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new UVector2Glm(vec);

        return (PyObject *)result;
    }



    static PyObject *
    swizzle_3_UVector3(UVector3 *self, PyObject *py_attr)
    {
        const char *attr = PyUnicode_AsUTF8(py_attr);
        if (!attr){ return 0; }

        UVector3Glm vec;
        for (int i = 0; i < 3; i++)
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
                    PyErr_Format(
                        PyExc_AttributeError,
                        "invalid swizzle: %R", py_attr
                    );
                    return 0;
                }
            }
            vec[i] = (*self->glm)[glm_index];
        }

        auto module_state = get_module_state();
        if (!module_state){ return 0; }
        auto cls = module_state->UVector3_PyTypeObject;

        UVector3 *result = (UVector3 *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new UVector3Glm(vec);

        return (PyObject *)result;
    }



    static PyObject *
    swizzle_4_UVector3(UVector3 *self, PyObject *py_attr)
    {
        const char *attr = PyUnicode_AsUTF8(py_attr);
        if (!attr){ return 0; }

        UVector4Glm vec;
        for (int i = 0; i < 4; i++)
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
                    PyErr_Format(
                        PyExc_AttributeError,
                        "invalid swizzle: %R", py_attr
                    );
                    return 0;
                }
            }
            vec[i] = (*self->glm)[glm_index];
        }

        auto module_state = get_module_state();
        if (!module_state){ return 0; }
        auto cls = module_state->UVector4_PyTypeObject;

        UVector4 *result = (UVector4 *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new UVector4Glm(vec);

        return (PyObject *)result;
    }




static PyObject *
UVector3__getattr__(UVector3 *self, PyObject *py_attr)
{
    PyObject *result = PyObject_GenericGetAttr((PyObject *)self, py_attr);
    if (result != 0){ return result; }

    auto attr_length = PyUnicode_GET_LENGTH(py_attr);
    switch(attr_length)
    {
        case 2:
        {
            PyErr_Clear();
            return swizzle_2_UVector3(self, py_attr);
        }
        case 3:
        {
            PyErr_Clear();
            return swizzle_3_UVector3(self, py_attr);
        }
        case 4:
        {
            PyErr_Clear();
            return swizzle_4_UVector3(self, py_attr);
        }
    }
    return 0;
}


static PyMemberDef UVector3_PyMemberDef[] = {
    {"__weaklistoffset__", T_PYSSIZET, offsetof(UVector3, weakreflist), READONLY},
    {0}
};





static PyObject *
UVector3_get_limits(UVector3 *self, void *)
{
    auto c_min = std::numeric_limits<unsigned int>::lowest();
    auto c_max = std::numeric_limits<unsigned int>::max();
    auto py_min = c_unsigned_int_to_pyobject(c_min);
    if (!py_min){ return 0; }
    auto py_max = c_unsigned_int_to_pyobject(c_max);
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


static PyMethodDef UVector3_PyMethodDef[] = {

    {"get_limits", (PyCFunction)UVector3_get_limits, METH_NOARGS | METH_STATIC, 0},
    {0, 0, 0, 0}
};


static PyType_Slot UVector3_PyType_Slots [] = {
    {Py_tp_new, (void*)UVector3__new__},
    {Py_tp_dealloc, (void*)UVector3__dealloc__},
    {Py_tp_hash, (void*)UVector3__hash__},
    {Py_tp_repr, (void*)UVector3__repr__},
    {Py_sq_length, (void*)UVector3__len__},
    {Py_sq_item, (void*)UVector3__getitem__},
    {Py_tp_richcompare, (void*)UVector3__richcmp__},
    {Py_nb_add, (void*)UVector3__add__},
    {Py_nb_subtract, (void*)UVector3__sub__},
    {Py_nb_multiply, (void*)UVector3__mul__},


        {Py_nb_true_divide, (void*)UVector3__truediv__},


    {Py_nb_absolute, (void*)UVector3__abs__},
    {Py_nb_bool, (void*)UVector3__bool__},
    {Py_bf_getbuffer, (void*)UVector3_getbufferproc},
    {Py_tp_getset, (void*)UVector3_PyGetSetDef},
    {Py_tp_getattro, (void*)UVector3__getattr__},
    {Py_tp_members, (void*)UVector3_PyMemberDef},
    {Py_tp_methods, (void*)UVector3_PyMethodDef},
    {0, 0},
};


static PyType_Spec UVector3_PyTypeSpec = {
    "gamut.math.UVector3",
    sizeof(UVector3),
    0,
    Py_TPFLAGS_DEFAULT,
    UVector3_PyType_Slots
};


static PyTypeObject *
define_UVector3_type(PyObject *module)
{
    PyTypeObject *type = (PyTypeObject *)PyType_FromModuleAndSpec(
        module,
        &UVector3_PyTypeSpec,
        0
    );
    if (!type){ return 0; }
    // Note:
    // Unlike other functions that steal references, PyModule_AddObject() only
    // decrements the reference count of value on success.
    if (PyModule_AddObject(module, "UVector3", (PyObject *)type) < 0)
    {
        Py_DECREF(type);
        return 0;
    }
    return type;
}


static UVector3 *
create_UVector3_from_glm(const UVector3Glm& glm)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->UVector3_PyTypeObject;

    UVector3 *result = (UVector3 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new UVector3Glm(glm);

    return result;
}

#endif