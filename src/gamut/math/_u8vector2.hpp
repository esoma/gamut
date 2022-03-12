
// generated 2022-03-12 19:37:09.760143 from codegen/math/templates/_vector.hpp

#ifndef GAMUT_MATH_U8VECTOR2_HPP
#define GAMUT_MATH_U8VECTOR2_HPP

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
U8Vector2__new__(PyTypeObject *cls, PyObject *args, PyObject *kwds)
{

        uint8_t c_0 = 0;

        uint8_t c_1 = 0;


    if (kwds && PyDict_Size(kwds) != 0)
    {
        PyErr_SetString(
            PyExc_TypeError,
            "U8Vector2 does accept any keyword arguments"
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

            break;
        }
        case 2:
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

            break;
        }
        default:
        {
            PyErr_Format(
                PyExc_TypeError,
                "invalid number of arguments supplied to U8Vector2, expected "
                "0, 1 or 2 (got %zd)",
                arg_count
            );
            return 0;
        }
    }

    U8Vector2 *self = (U8Vector2*)cls->tp_alloc(cls, 0);
    if (!self){ return 0; }
    self->glm = new U8Vector2Glm(

            c_0,

            c_1

    );

    return (PyObject *)self;
}


static void
U8Vector2__dealloc__(U8Vector2 *self)
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
U8Vector2__hash__(U8Vector2 *self)
{
    Py_ssize_t len = 2;
    Py_uhash_t acc = _HASH_XXPRIME_5;
    for (U8Vector2Glm::length_type i = 0; i < len; i++)
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
U8Vector2__repr__(U8Vector2 *self)
{
    PyObject *result = 0;

        PyObject *py_0 = 0;

        PyObject *py_1 = 0;



        py_0 = c_uint8_t_to_pyobject((*self->glm)[0]);
        if (!py_0){ goto cleanup; }

        py_1 = c_uint8_t_to_pyobject((*self->glm)[1]);
        if (!py_1){ goto cleanup; }

    result = PyUnicode_FromFormat(
        "U8Vector2("

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
U8Vector2__len__(U8Vector2 *self)
{
    return 2;
}


static PyObject *
U8Vector2__getitem__(U8Vector2 *self, Py_ssize_t index)
{
    if (index < 0 || index > 1)
    {
        PyErr_Format(PyExc_IndexError, "index out of range");
        return 0;
    }
    auto c = (*self->glm)[(U8Vector2Glm::length_type)index];
    return c_uint8_t_to_pyobject(c);
}


static PyObject *
U8Vector2__richcmp__(U8Vector2 *self, U8Vector2 *other, int op)
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
U8Vector2__add__(PyObject *left, PyObject *right)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->U8Vector2_PyTypeObject;

    U8Vector2Glm vector;
    if (Py_TYPE(left) == Py_TYPE(right))
    {
        vector = (*((U8Vector2 *)left)->glm) + (*((U8Vector2 *)right)->glm);
    }
    else
    {
        if (Py_TYPE(left) == cls)
        {
            auto c_right = pyobject_to_c_uint8_t(right);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
            vector = (*((U8Vector2 *)left)->glm) + c_right;
        }
        else
        {
            auto c_left = pyobject_to_c_uint8_t(left);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
            vector = c_left + (*((U8Vector2 *)right)->glm);
        }
    }

    U8Vector2 *result = (U8Vector2 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new U8Vector2Glm(

            vector[0],

            vector[1]

    );

    return (PyObject *)result;
}


static PyObject *
U8Vector2__sub__(PyObject *left, PyObject *right)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->U8Vector2_PyTypeObject;

    U8Vector2Glm vector;
    if (Py_TYPE(left) == Py_TYPE(right))
    {
        vector = (*((U8Vector2 *)left)->glm) - (*((U8Vector2 *)right)->glm);
    }
    else
    {
        if (Py_TYPE(left) == cls)
        {
            auto c_right = pyobject_to_c_uint8_t(right);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
            vector = (*((U8Vector2 *)left)->glm) - c_right;
        }
        else
        {
            auto c_left = pyobject_to_c_uint8_t(left);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
            vector = c_left - (*((U8Vector2 *)right)->glm);
        }
    }

    U8Vector2 *result = (U8Vector2 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new U8Vector2Glm(

            vector[0],

            vector[1]

    );

    return (PyObject *)result;
}


static PyObject *
U8Vector2__mul__(PyObject *left, PyObject *right)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->U8Vector2_PyTypeObject;

    U8Vector2Glm vector;
    if (Py_TYPE(left) == Py_TYPE(right))
    {
        vector = (*((U8Vector2 *)left)->glm) * (*((U8Vector2 *)right)->glm);
    }
    else
    {
        if (Py_TYPE(left) == cls)
        {
            auto c_right = pyobject_to_c_uint8_t(right);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
            vector = (*((U8Vector2 *)left)->glm) * c_right;
        }
        else
        {
            auto c_left = pyobject_to_c_uint8_t(left);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
            vector = c_left * (*((U8Vector2 *)right)->glm);
        }
    }

    U8Vector2 *result = (U8Vector2 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new U8Vector2Glm(

            vector[0],

            vector[1]

    );

    return (PyObject *)result;
}







    static PyObject *
    U8Vector2__truediv__(PyObject *left, PyObject *right)
    {
        auto module_state = get_module_state();
        if (!module_state){ return 0; }
        auto cls = module_state->U8Vector2_PyTypeObject;

        U8Vector2Glm vector;
        if (Py_TYPE(left) == Py_TYPE(right))
        {

                if (

                        (*((U8Vector2 *)right)->glm)[0] == 0 ||

                        (*((U8Vector2 *)right)->glm)[1] == 0

                )
                {
                    PyErr_SetString(PyExc_ZeroDivisionError, "divide by zero");
                    return 0;
                }

            vector = (*((U8Vector2 *)left)->glm) / (*((U8Vector2 *)right)->glm);
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

                vector = (*((U8Vector2 *)left)->glm) / c_right;
            }
            else
            {
                auto c_left = pyobject_to_c_uint8_t(left);
                if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }

                    if (

                            (*((U8Vector2 *)right)->glm)[0] == 0 ||

                            (*((U8Vector2 *)right)->glm)[1] == 0

                    )
                    {
                        PyErr_SetString(PyExc_ZeroDivisionError, "divide by zero");
                        return 0;
                    }

                vector = c_left / (*((U8Vector2 *)right)->glm);
            }
        }

        U8Vector2 *result = (U8Vector2 *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new U8Vector2Glm(

                vector[0],

                vector[1]

        );

        return (PyObject *)result;
    }






static PyObject *
U8Vector2__abs__(U8Vector2 *self)
{
    auto cls = Py_TYPE(self);
    U8Vector2Glm vector = glm::abs(*self->glm);

    U8Vector2 *result = (U8Vector2 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new U8Vector2Glm(

            vector[0],

            vector[1]

    );

    return (PyObject *)result;
}


static int
U8Vector2__bool__(U8Vector2 *self)
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
U8Vector2_getbufferproc(U8Vector2 *self, Py_buffer *view, int flags)
{
    if (flags & PyBUF_WRITABLE)
    {
        PyErr_SetString(PyExc_TypeError, "U8Vector2 is read only");
        view->obj = 0;
        return -1;
    }
    view->buf = glm::value_ptr(*self->glm);
    view->obj = (PyObject *)self;
    view->len = sizeof(uint8_t) * 2;
    view->readonly = 1;
    view->itemsize = sizeof(uint8_t);
    view->format = "=B";
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
    U8Vector2_Getter_0(U8Vector2 *self, void *)
    {
        auto c = (*self->glm)[0];
        return c_uint8_t_to_pyobject(c);
    }

    static PyObject *
    U8Vector2_Getter_1(U8Vector2 *self, void *)
    {
        auto c = (*self->glm)[1];
        return c_uint8_t_to_pyobject(c);
    }






static PyObject *
U8Vector2_pointer(U8Vector2 *self, void *)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto c_void_p = module_state->ctypes_c_void_p;
    return PyObject_CallFunction(c_void_p, "n", (Py_ssize_t)self->glm);
}


static PyGetSetDef U8Vector2_PyGetSetDef[] = {
    {"x", (getter)U8Vector2_Getter_0, 0, 0, 0},
    {"r", (getter)U8Vector2_Getter_0, 0, 0, 0},
    {"s", (getter)U8Vector2_Getter_0, 0, 0, 0},
    {"u", (getter)U8Vector2_Getter_0, 0, 0, 0},

        {"y", (getter)U8Vector2_Getter_1, 0, 0, 0},
        {"g", (getter)U8Vector2_Getter_1, 0, 0, 0},
        {"t", (getter)U8Vector2_Getter_1, 0, 0, 0},
        {"v", (getter)U8Vector2_Getter_1, 0, 0, 0},




    {"pointer", (getter)U8Vector2_pointer, 0, 0, 0},
    {0, 0, 0, 0, 0}
};



    static PyObject *
    swizzle_2_U8Vector2(U8Vector2 *self, PyObject *py_attr)
    {
        const char *attr = PyUnicode_AsUTF8(py_attr);
        if (!attr){ return 0; }

        U8Vector2Glm vec;
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
        auto cls = module_state->U8Vector2_PyTypeObject;

        U8Vector2 *result = (U8Vector2 *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new U8Vector2Glm(vec);

        return (PyObject *)result;
    }



    static PyObject *
    swizzle_3_U8Vector2(U8Vector2 *self, PyObject *py_attr)
    {
        const char *attr = PyUnicode_AsUTF8(py_attr);
        if (!attr){ return 0; }

        U8Vector3Glm vec;
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
        auto cls = module_state->U8Vector3_PyTypeObject;

        U8Vector3 *result = (U8Vector3 *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new U8Vector3Glm(vec);

        return (PyObject *)result;
    }



    static PyObject *
    swizzle_4_U8Vector2(U8Vector2 *self, PyObject *py_attr)
    {
        const char *attr = PyUnicode_AsUTF8(py_attr);
        if (!attr){ return 0; }

        U8Vector4Glm vec;
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
        auto cls = module_state->U8Vector4_PyTypeObject;

        U8Vector4 *result = (U8Vector4 *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new U8Vector4Glm(vec);

        return (PyObject *)result;
    }




static PyObject *
U8Vector2__getattr__(U8Vector2 *self, PyObject *py_attr)
{
    PyObject *result = PyObject_GenericGetAttr((PyObject *)self, py_attr);
    if (result != 0){ return result; }

    auto attr_length = PyUnicode_GET_LENGTH(py_attr);
    switch(attr_length)
    {
        case 2:
        {
            PyErr_Clear();
            return swizzle_2_U8Vector2(self, py_attr);
        }
        case 3:
        {
            PyErr_Clear();
            return swizzle_3_U8Vector2(self, py_attr);
        }
        case 4:
        {
            PyErr_Clear();
            return swizzle_4_U8Vector2(self, py_attr);
        }
    }
    return 0;
}


static PyMemberDef U8Vector2_PyMemberDef[] = {
    {"__weaklistoffset__", T_PYSSIZET, offsetof(U8Vector2, weakreflist), READONLY},
    {0}
};





static PyObject *
U8Vector2_get_limits(U8Vector2 *self, void *)
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


static PyMethodDef U8Vector2_PyMethodDef[] = {

    {"get_limits", (PyCFunction)U8Vector2_get_limits, METH_NOARGS | METH_STATIC, 0},
    {0, 0, 0, 0}
};


static PyType_Slot U8Vector2_PyType_Slots [] = {
    {Py_tp_new, (void*)U8Vector2__new__},
    {Py_tp_dealloc, (void*)U8Vector2__dealloc__},
    {Py_tp_hash, (void*)U8Vector2__hash__},
    {Py_tp_repr, (void*)U8Vector2__repr__},
    {Py_sq_length, (void*)U8Vector2__len__},
    {Py_sq_item, (void*)U8Vector2__getitem__},
    {Py_tp_richcompare, (void*)U8Vector2__richcmp__},
    {Py_nb_add, (void*)U8Vector2__add__},
    {Py_nb_subtract, (void*)U8Vector2__sub__},
    {Py_nb_multiply, (void*)U8Vector2__mul__},


        {Py_nb_true_divide, (void*)U8Vector2__truediv__},


    {Py_nb_absolute, (void*)U8Vector2__abs__},
    {Py_nb_bool, (void*)U8Vector2__bool__},
    {Py_bf_getbuffer, (void*)U8Vector2_getbufferproc},
    {Py_tp_getset, (void*)U8Vector2_PyGetSetDef},
    {Py_tp_getattro, (void*)U8Vector2__getattr__},
    {Py_tp_members, (void*)U8Vector2_PyMemberDef},
    {Py_tp_methods, (void*)U8Vector2_PyMethodDef},
    {0, 0},
};


static PyType_Spec U8Vector2_PyTypeSpec = {
    "gamut.math.U8Vector2",
    sizeof(U8Vector2),
    0,
    Py_TPFLAGS_DEFAULT,
    U8Vector2_PyType_Slots
};


static PyTypeObject *
define_U8Vector2_type(PyObject *module)
{
    PyTypeObject *type = (PyTypeObject *)PyType_FromModuleAndSpec(
        module,
        &U8Vector2_PyTypeSpec,
        0
    );
    if (!type){ return 0; }
    // Note:
    // Unlike other functions that steal references, PyModule_AddObject() only
    // decrements the reference count of value on success.
    if (PyModule_AddObject(module, "U8Vector2", (PyObject *)type) < 0)
    {
        Py_DECREF(type);
        return 0;
    }
    return type;
}




static PyObject *
U8Vector2Array__new__(PyTypeObject *cls, PyObject *args, PyObject *kwds)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto element_cls = module_state->U8Vector2_PyTypeObject;

    if (kwds && PyDict_Size(kwds) != 0)
    {
        PyErr_SetString(
            PyExc_TypeError,
            "U8Vector2 does accept any keyword arguments"
        );
        return 0;
    }

    auto arg_count = PyTuple_GET_SIZE(args);
    if (arg_count == 0)
    {
        auto self = (U8Vector2Array *)cls->tp_alloc(cls, 0);
        if (!self){ return 0; }
        self->length = 0;
        self->glm = 0;
        return (PyObject *)self;
    }

    auto *self = (U8Vector2Array *)cls->tp_alloc(cls, 0);
    if (!self){ return 0; }
    self->length = arg_count;
    self->glm = new U8Vector2Glm[arg_count];

    for (int i = 0; i < arg_count; i++)
    {
        auto arg = PyTuple_GET_ITEM(args, i);
        if (Py_TYPE(arg) == element_cls)
        {
            self->glm[i] = *(((U8Vector2*)arg)->glm);
        }
        else
        {
            Py_DECREF(self);
            PyErr_Format(
                PyExc_TypeError,
                "invalid type %R, expected %R",
                arg,
                element_cls
            );
            return 0;
        }
    }

    return (PyObject *)self;
}


static void
U8Vector2Array__dealloc__(U8Vector2Array *self)
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
U8Vector2Array__hash__(U8Vector2Array *self)
{
    Py_ssize_t len = self->length * 2;
    Py_uhash_t acc = _HASH_XXPRIME_5;
    for (Py_ssize_t i = 0; i < (Py_ssize_t)self->length; i++)
    {
        for (U8Vector2Glm::length_type j = 0; j < 2; j++)
        {
            Py_uhash_t lane = std::hash<uint8_t>{}(self->glm[i][j]);
            acc += lane * _HASH_XXPRIME_2;
            acc = _HASH_XXROTATE(acc);
            acc *= _HASH_XXPRIME_1;
        }
        acc += len ^ (_HASH_XXPRIME_5 ^ 3527539UL);
    }

    if (acc == (Py_uhash_t)-1) {
        return 1546275796;
    }
    return acc;
}


static PyObject *
U8Vector2Array__repr__(U8Vector2Array *self)
{
    return PyUnicode_FromFormat("U8Vector2Array[%zu]", self->length);
}


static Py_ssize_t
U8Vector2Array__len__(U8Vector2Array *self)
{
    return self->length;
}


static PyObject *
U8Vector2Array__getitem__(U8Vector2Array *self, Py_ssize_t index)
{
    if (index < 0 || index > (Py_ssize_t)self->length - 1)
    {
        PyErr_Format(PyExc_IndexError, "index out of range");
        return 0;
    }

    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto element_cls = module_state->U8Vector2_PyTypeObject;

    U8Vector2 *result = (U8Vector2 *)element_cls->tp_alloc(element_cls, 0);
    if (!result){ return 0; }
    result->glm = new U8Vector2Glm(self->glm[index]);

    return (PyObject *)result;
}


static PyObject *
U8Vector2Array__richcmp__(
    U8Vector2Array *self,
    U8Vector2Array *other,
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
                    if (self->glm[i] != other->glm[i])
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
                    if (self->glm[i] != other->glm[i])
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
U8Vector2Array__bool__(U8Vector2Array *self)
{
    return self->length ? 1 : 0;
}


static int
U8Vector2Array_getbufferproc(U8Vector2Array *self, Py_buffer *view, int flags)
{
    if (flags & PyBUF_WRITABLE)
    {
        PyErr_SetString(PyExc_TypeError, "U8Vector2 is read only");
        view->obj = 0;
        return -1;
    }
    view->buf = self->glm;
    view->obj = (PyObject *)self;
    view->len = sizeof(uint8_t) * 2 * self->length;
    view->readonly = 1;
    view->itemsize = sizeof(uint8_t);
    view->format = "=B";
    view->ndim = 2;
    view->shape = new Py_ssize_t[2] {
        (Py_ssize_t)self->length,
        2
    };
    static Py_ssize_t strides[] = {
        sizeof(uint8_t) * 2,
        sizeof(uint8_t)
    };
    view->strides = &strides[0];
    view->suboffsets = 0;
    view->internal = 0;
    Py_INCREF(self);
    return 0;
}


static void
U8Vector2Array_releasebufferproc(U8Vector2Array *self, Py_buffer *view)
{
    delete view->shape;
}


static PyMemberDef U8Vector2Array_PyMemberDef[] = {
    {"__weaklistoffset__", T_PYSSIZET, offsetof(U8Vector2Array, weakreflist), READONLY},
    {0}
};


static PyObject *
U8Vector2Array_pointer(U8Vector2Array *self, void *)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto c_void_p = module_state->ctypes_c_void_p;
    return PyObject_CallFunction(c_void_p, "n", (Py_ssize_t)self->glm);
}


static PyGetSetDef U8Vector2Array_PyGetSetDef[] = {
    {"pointer", (getter)U8Vector2Array_pointer, 0, 0, 0},
    {0, 0, 0, 0, 0}
};


static PyType_Slot U8Vector2Array_PyType_Slots [] = {
    {Py_tp_new, (void*)U8Vector2Array__new__},
    {Py_tp_dealloc, (void*)U8Vector2Array__dealloc__},
    {Py_tp_hash, (void*)U8Vector2Array__hash__},
    {Py_tp_repr, (void*)U8Vector2Array__repr__},
    {Py_sq_length, (void*)U8Vector2Array__len__},
    {Py_sq_item, (void*)U8Vector2Array__getitem__},
    {Py_tp_richcompare, (void*)U8Vector2Array__richcmp__},
    {Py_nb_bool, (void*)U8Vector2Array__bool__},
    {Py_bf_getbuffer, (void*)U8Vector2Array_getbufferproc},
    {Py_bf_releasebuffer, (void*)U8Vector2Array_releasebufferproc},
    {Py_tp_getset, (void*)U8Vector2Array_PyGetSetDef},
    {Py_tp_members, (void*)U8Vector2Array_PyMemberDef},
    {0, 0},
};


static PyType_Spec U8Vector2Array_PyTypeSpec = {
    "gamut.math.U8Vector2Array",
    sizeof(U8Vector2Array),
    0,
    Py_TPFLAGS_DEFAULT,
    U8Vector2Array_PyType_Slots
};


static PyTypeObject *
define_U8Vector2Array_type(PyObject *module)
{
    PyTypeObject *type = (PyTypeObject *)PyType_FromModuleAndSpec(
        module,
        &U8Vector2Array_PyTypeSpec,
        0
    );
    if (!type){ return 0; }
    // Note:
    // Unlike other functions that steal references, PyModule_AddObject() only
    // decrements the reference count of value on success.
    if (PyModule_AddObject(module, "U8Vector2Array", (PyObject *)type) < 0)
    {
        Py_DECREF(type);
        return 0;
    }
    return type;
}


static PyTypeObject *
get_U8Vector2_type()
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    return module_state->U8Vector2_PyTypeObject;
}


static PyTypeObject *
get_U8Vector2Array_type()
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    return module_state->U8Vector2Array_PyTypeObject;
}


static PyObject *
create_U8Vector2(const uint8_t *value)
{
    auto cls = get_U8Vector2_type();
    auto result = (U8Vector2 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new U8Vector2Glm(*(U8Vector2Glm *)value);
    return (PyObject *)result;
}


static PyObject *
create_U8Vector2Array(size_t length, const uint8_t *value)
{
    auto cls = get_U8Vector2Array_type();
    auto result = (U8Vector2Array *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->length = length;
    if (length > 0)
    {
        result->glm = new U8Vector2Glm[length];
        for (size_t i = 0; i < length; i++)
        {
            result->glm[i] = ((U8Vector2Glm *)value)[i];
        }
    }
    else
    {
        result->glm = 0;
    }
    return (PyObject *)result;
}


static uint8_t *
get_U8Vector2_value_ptr(const PyObject *self)
{
    if (Py_TYPE(self) != get_U8Vector2_type())
    {
        PyErr_Format(PyExc_TypeError, "expected U8Vector2, got %R", self);
        return 0;
    }
    return (uint8_t *)((U8Vector2 *)self)->glm;
}


static uint8_t *
get_U8Vector2Array_value_ptr(const PyObject *self)
{
    if (Py_TYPE(self) != get_U8Vector2Array_type())
    {
        PyErr_Format(
            PyExc_TypeError,
            "expected U8Vector2Array, got %R",
            self
        );
        return 0;
    }
    return (uint8_t *)((U8Vector2Array *)self)->glm;
}


static size_t
get_U8Vector2Array_length(const PyObject *self)
{
    if (Py_TYPE(self) != get_U8Vector2Array_type())
    {
        PyErr_Format(
            PyExc_TypeError,
            "expected U8Vector2Array, got %R",
            self
        );
        return 0;
    }
    return ((U8Vector2Array *)self)->length;
}

#endif