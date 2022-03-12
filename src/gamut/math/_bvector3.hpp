
// generated 2022-03-12 02:08:08.733893 from codegen/math/templates/_vector.hpp

#ifndef GAMUT_MATH_BVECTOR3_HPP
#define GAMUT_MATH_BVECTOR3_HPP

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
BVector3__new__(PyTypeObject *cls, PyObject *args, PyObject *kwds)
{

        bool c_0 = 0;

        bool c_1 = 0;

        bool c_2 = 0;


    if (kwds && PyDict_Size(kwds) != 0)
    {
        PyErr_SetString(
            PyExc_TypeError,
            "BVector3 does accept any keyword arguments"
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

                c_2 = arg_c;

            break;
        }
        case 3:
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

            {
                auto arg = PyTuple_GET_ITEM(args, 2);
                c_2 = pyobject_to_c_bool(arg);
                auto error_occurred = PyErr_Occurred();
                if (error_occurred){ return 0; }
            }

            break;
        }
        default:
        {
            PyErr_Format(
                PyExc_TypeError,
                "invalid number of arguments supplied to BVector3, expected "
                "0, 1 or 3 (got %zd)",
                arg_count
            );
            return 0;
        }
    }

    BVector3 *self = (BVector3*)cls->tp_alloc(cls, 0);
    if (!self){ return 0; }
    self->glm = new BVector3Glm(

            c_0,

            c_1,

            c_2

    );

    return (PyObject *)self;
}


static void
BVector3__dealloc__(BVector3 *self)
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
BVector3__hash__(BVector3 *self)
{
    Py_ssize_t len = 3;
    Py_uhash_t acc = _HASH_XXPRIME_5;
    for (BVector3Glm::length_type i = 0; i < len; i++)
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
BVector3__repr__(BVector3 *self)
{
    PyObject *result = 0;

        PyObject *py_0 = 0;

        PyObject *py_1 = 0;

        PyObject *py_2 = 0;



        py_0 = c_bool_to_pyobject((*self->glm)[0]);
        if (!py_0){ goto cleanup; }

        py_1 = c_bool_to_pyobject((*self->glm)[1]);
        if (!py_1){ goto cleanup; }

        py_2 = c_bool_to_pyobject((*self->glm)[2]);
        if (!py_2){ goto cleanup; }

    result = PyUnicode_FromFormat(
        "BVector3("

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
BVector3__len__(BVector3 *self)
{
    return 3;
}


static PyObject *
BVector3__getitem__(BVector3 *self, Py_ssize_t index)
{
    if (index < 0 || index > 2)
    {
        PyErr_Format(PyExc_IndexError, "index out of range");
        return 0;
    }
    auto c = (*self->glm)[(BVector3Glm::length_type)index];
    return c_bool_to_pyobject(c);
}


static PyObject *
BVector3__richcmp__(BVector3 *self, BVector3 *other, int op)
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
BVector3__add__(PyObject *left, PyObject *right)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->BVector3_PyTypeObject;

    BVector3Glm vector;
    if (Py_TYPE(left) == Py_TYPE(right))
    {
        vector = (*((BVector3 *)left)->glm) + (*((BVector3 *)right)->glm);
    }
    else
    {
        if (Py_TYPE(left) == cls)
        {
            auto c_right = pyobject_to_c_bool(right);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
            vector = (*((BVector3 *)left)->glm) + c_right;
        }
        else
        {
            auto c_left = pyobject_to_c_bool(left);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
            vector = c_left + (*((BVector3 *)right)->glm);
        }
    }

    BVector3 *result = (BVector3 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new BVector3Glm(

            vector[0],

            vector[1],

            vector[2]

    );

    return (PyObject *)result;
}


static PyObject *
BVector3__sub__(PyObject *left, PyObject *right)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->BVector3_PyTypeObject;

    BVector3Glm vector;
    if (Py_TYPE(left) == Py_TYPE(right))
    {
        vector = (*((BVector3 *)left)->glm) - (*((BVector3 *)right)->glm);
    }
    else
    {
        if (Py_TYPE(left) == cls)
        {
            auto c_right = pyobject_to_c_bool(right);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
            vector = (*((BVector3 *)left)->glm) - c_right;
        }
        else
        {
            auto c_left = pyobject_to_c_bool(left);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
            vector = c_left - (*((BVector3 *)right)->glm);
        }
    }

    BVector3 *result = (BVector3 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new BVector3Glm(

            vector[0],

            vector[1],

            vector[2]

    );

    return (PyObject *)result;
}


static PyObject *
BVector3__mul__(PyObject *left, PyObject *right)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->BVector3_PyTypeObject;

    BVector3Glm vector;
    if (Py_TYPE(left) == Py_TYPE(right))
    {
        vector = (*((BVector3 *)left)->glm) * (*((BVector3 *)right)->glm);
    }
    else
    {
        if (Py_TYPE(left) == cls)
        {
            auto c_right = pyobject_to_c_bool(right);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
            vector = (*((BVector3 *)left)->glm) * c_right;
        }
        else
        {
            auto c_left = pyobject_to_c_bool(left);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
            vector = c_left * (*((BVector3 *)right)->glm);
        }
    }

    BVector3 *result = (BVector3 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new BVector3Glm(

            vector[0],

            vector[1],

            vector[2]

    );

    return (PyObject *)result;
}









    static PyObject *
    BVector3__neg__(BVector3 *self)
    {
        auto cls = Py_TYPE(self);

            BVector3Glm vector = (*self->glm);


        BVector3 *result = (BVector3 *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new BVector3Glm(

                vector[0],

                vector[1],

                vector[2]

        );

        return (PyObject *)result;
    }



static PyObject *
BVector3__abs__(BVector3 *self)
{
    auto cls = Py_TYPE(self);
    BVector3Glm vector = glm::abs(*self->glm);

    BVector3 *result = (BVector3 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new BVector3Glm(

            vector[0],

            vector[1],

            vector[2]

    );

    return (PyObject *)result;
}


static int
BVector3__bool__(BVector3 *self)
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
BVector3_getbufferproc(BVector3 *self, Py_buffer *view, int flags)
{
    if (flags & PyBUF_WRITABLE)
    {
        PyErr_SetString(PyExc_TypeError, "BVector3 is read only");
        view->obj = 0;
        return -1;
    }
    view->buf = glm::value_ptr(*self->glm);
    view->obj = (PyObject *)self;
    view->len = sizeof(bool) * 3;
    view->readonly = 1;
    view->itemsize = sizeof(bool);
    view->format = "?";
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
    BVector3_Getter_0(BVector3 *self, void *)
    {
        auto c = (*self->glm)[0];
        return c_bool_to_pyobject(c);
    }

    static PyObject *
    BVector3_Getter_1(BVector3 *self, void *)
    {
        auto c = (*self->glm)[1];
        return c_bool_to_pyobject(c);
    }

    static PyObject *
    BVector3_Getter_2(BVector3 *self, void *)
    {
        auto c = (*self->glm)[2];
        return c_bool_to_pyobject(c);
    }






static PyGetSetDef BVector3_PyGetSetDef[] = {
    {"x", (getter)BVector3_Getter_0, 0, 0, 0},
    {"r", (getter)BVector3_Getter_0, 0, 0, 0},
    {"s", (getter)BVector3_Getter_0, 0, 0, 0},
    {"u", (getter)BVector3_Getter_0, 0, 0, 0},

        {"y", (getter)BVector3_Getter_1, 0, 0, 0},
        {"g", (getter)BVector3_Getter_1, 0, 0, 0},
        {"t", (getter)BVector3_Getter_1, 0, 0, 0},
        {"v", (getter)BVector3_Getter_1, 0, 0, 0},


        {"z", (getter)BVector3_Getter_2, 0, 0, 0},
        {"b", (getter)BVector3_Getter_2, 0, 0, 0},
        {"p", (getter)BVector3_Getter_2, 0, 0, 0},



    {0, 0, 0, 0, 0}
};



    static PyObject *
    swizzle_2_BVector3(BVector3 *self, PyObject *py_attr)
    {
        const char *attr = PyUnicode_AsUTF8(py_attr);
        if (!attr){ return 0; }

        BVector2Glm vec;
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
        auto cls = module_state->BVector2_PyTypeObject;

        BVector2 *result = (BVector2 *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new BVector2Glm(vec);

        return (PyObject *)result;
    }



    static PyObject *
    swizzle_3_BVector3(BVector3 *self, PyObject *py_attr)
    {
        const char *attr = PyUnicode_AsUTF8(py_attr);
        if (!attr){ return 0; }

        BVector3Glm vec;
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
        auto cls = module_state->BVector3_PyTypeObject;

        BVector3 *result = (BVector3 *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new BVector3Glm(vec);

        return (PyObject *)result;
    }



    static PyObject *
    swizzle_4_BVector3(BVector3 *self, PyObject *py_attr)
    {
        const char *attr = PyUnicode_AsUTF8(py_attr);
        if (!attr){ return 0; }

        BVector4Glm vec;
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
        auto cls = module_state->BVector4_PyTypeObject;

        BVector4 *result = (BVector4 *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new BVector4Glm(vec);

        return (PyObject *)result;
    }




static PyObject *
BVector3__getattr__(BVector3 *self, PyObject *py_attr)
{
    PyObject *result = PyObject_GenericGetAttr((PyObject *)self, py_attr);
    if (result != 0){ return result; }

    auto attr_length = PyUnicode_GET_LENGTH(py_attr);
    switch(attr_length)
    {
        case 2:
        {
            PyErr_Clear();
            return swizzle_2_BVector3(self, py_attr);
        }
        case 3:
        {
            PyErr_Clear();
            return swizzle_3_BVector3(self, py_attr);
        }
        case 4:
        {
            PyErr_Clear();
            return swizzle_4_BVector3(self, py_attr);
        }
    }
    return 0;
}


static PyMemberDef BVector3_PyMemberDef[] = {
    {"__weaklistoffset__", T_PYSSIZET, offsetof(BVector3, weakreflist), READONLY},
    {0}
};





static PyObject *
BVector3_get_limits(BVector3 *self, void *)
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


static PyMethodDef BVector3_PyMethodDef[] = {

    {"get_limits", (PyCFunction)BVector3_get_limits, METH_NOARGS | METH_STATIC, 0},
    {0, 0, 0, 0}
};


static PyType_Slot BVector3_PyType_Slots [] = {
    {Py_tp_new, (void*)BVector3__new__},
    {Py_tp_dealloc, (void*)BVector3__dealloc__},
    {Py_tp_hash, (void*)BVector3__hash__},
    {Py_tp_repr, (void*)BVector3__repr__},
    {Py_sq_length, (void*)BVector3__len__},
    {Py_sq_item, (void*)BVector3__getitem__},
    {Py_tp_richcompare, (void*)BVector3__richcmp__},
    {Py_nb_add, (void*)BVector3__add__},
    {Py_nb_subtract, (void*)BVector3__sub__},
    {Py_nb_multiply, (void*)BVector3__mul__},



        {Py_nb_negative, (void*)BVector3__neg__},

    {Py_nb_absolute, (void*)BVector3__abs__},
    {Py_nb_bool, (void*)BVector3__bool__},
    {Py_bf_getbuffer, (void*)BVector3_getbufferproc},
    {Py_tp_getset, (void*)BVector3_PyGetSetDef},
    {Py_tp_getattro, (void*)BVector3__getattr__},
    {Py_tp_members, (void*)BVector3_PyMemberDef},
    {Py_tp_methods, (void*)BVector3_PyMethodDef},
    {0, 0},
};


static PyType_Spec BVector3_PyTypeSpec = {
    "gamut.math.BVector3",
    sizeof(BVector3),
    0,
    Py_TPFLAGS_DEFAULT,
    BVector3_PyType_Slots
};


static PyTypeObject *
define_BVector3_type(PyObject *module)
{
    PyTypeObject *type = (PyTypeObject *)PyType_FromModuleAndSpec(
        module,
        &BVector3_PyTypeSpec,
        0
    );
    if (!type){ return 0; }
    // Note:
    // Unlike other functions that steal references, PyModule_AddObject() only
    // decrements the reference count of value on success.
    if (PyModule_AddObject(module, "BVector3", (PyObject *)type) < 0)
    {
        Py_DECREF(type);
        return 0;
    }
    return type;
}




static PyObject *
BVector3Array__new__(PyTypeObject *cls, PyObject *args, PyObject *kwds)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto element_cls = module_state->BVector3_PyTypeObject;

    if (kwds && PyDict_Size(kwds) != 0)
    {
        PyErr_SetString(
            PyExc_TypeError,
            "BVector3 does accept any keyword arguments"
        );
        return 0;
    }

    auto arg_count = PyTuple_GET_SIZE(args);
    if (arg_count == 0)
    {
        auto self = (BVector3Array *)cls->tp_alloc(cls, 0);
        if (!self){ return 0; }
        self->length = 0;
        self->glm = 0;
        return (PyObject *)self;
    }

    auto *self = (BVector3Array *)cls->tp_alloc(cls, 0);
    if (!self){ return 0; }
    self->length = arg_count;
    self->glm = new BVector3Glm[arg_count];

    for (int i = 0; i < arg_count; i++)
    {
        auto arg = PyTuple_GET_ITEM(args, i);
        if (Py_TYPE(arg) == element_cls)
        {
            self->glm[i] = *(((BVector3*)arg)->glm);
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
BVector3Array__dealloc__(BVector3Array *self)
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
BVector3Array__hash__(BVector3Array *self)
{
    Py_ssize_t len = self->length * 3;
    Py_uhash_t acc = _HASH_XXPRIME_5;
    for (Py_ssize_t i = 0; i < (Py_ssize_t)self->length; i++)
    {
        for (BVector3Glm::length_type j = 0; j < 3; j++)
        {
            Py_uhash_t lane = std::hash<bool>{}(self->glm[i][j]);
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
BVector3Array__repr__(BVector3Array *self)
{
    return PyUnicode_FromFormat("BVector3Array[%zu]", self->length);
}


static Py_ssize_t
BVector3Array__len__(BVector3Array *self)
{
    return self->length;
}


static PyObject *
BVector3Array__getitem__(BVector3Array *self, Py_ssize_t index)
{
    if (index < 0 || index > (Py_ssize_t)self->length - 1)
    {
        PyErr_Format(PyExc_IndexError, "index out of range");
        return 0;
    }

    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto element_cls = module_state->BVector3_PyTypeObject;

    BVector3 *result = (BVector3 *)element_cls->tp_alloc(element_cls, 0);
    if (!result){ return 0; }
    result->glm = new BVector3Glm(self->glm[index]);

    return (PyObject *)result;
}


static PyObject *
BVector3Array__richcmp__(
    BVector3Array *self,
    BVector3Array *other,
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
BVector3Array__bool__(BVector3Array *self)
{
    return self->length ? 1 : 0;
}


static int
BVector3Array_getbufferproc(BVector3Array *self, Py_buffer *view, int flags)
{
    if (flags & PyBUF_WRITABLE)
    {
        PyErr_SetString(PyExc_TypeError, "BVector3 is read only");
        view->obj = 0;
        return -1;
    }
    view->buf = self->glm;
    view->obj = (PyObject *)self;
    view->len = sizeof(bool) * 3 * self->length;
    view->readonly = 1;
    view->itemsize = sizeof(bool);
    view->format = "?";
    view->ndim = 2;
    view->shape = new Py_ssize_t[2] {
        (Py_ssize_t)self->length,
        3
    };
    static Py_ssize_t strides[] = {
        sizeof(bool) * 3,
        sizeof(bool)
    };
    view->strides = &strides[0];
    view->suboffsets = 0;
    view->internal = 0;
    Py_INCREF(self);
    return 0;
}


static void
BVector3Array_releasebufferproc(BVector3Array *self, Py_buffer *view)
{
    delete view->shape;
}


static PyMemberDef BVector3Array_PyMemberDef[] = {
    {"__weaklistoffset__", T_PYSSIZET, offsetof(BVector3Array, weakreflist), READONLY},
    {0}
};


static PyType_Slot BVector3Array_PyType_Slots [] = {
    {Py_tp_new, (void*)BVector3Array__new__},
    {Py_tp_dealloc, (void*)BVector3Array__dealloc__},
    {Py_tp_hash, (void*)BVector3Array__hash__},
    {Py_tp_repr, (void*)BVector3Array__repr__},
    {Py_sq_length, (void*)BVector3Array__len__},
    {Py_sq_item, (void*)BVector3Array__getitem__},
    {Py_tp_richcompare, (void*)BVector3Array__richcmp__},
    {Py_nb_bool, (void*)BVector3Array__bool__},
    {Py_bf_getbuffer, (void*)BVector3Array_getbufferproc},
    {Py_bf_releasebuffer, (void*)BVector3Array_releasebufferproc},
    {Py_tp_members, (void*)BVector3Array_PyMemberDef},
    {0, 0},
};


static PyType_Spec BVector3Array_PyTypeSpec = {
    "gamut.math.BVector3Array",
    sizeof(BVector3Array),
    0,
    Py_TPFLAGS_DEFAULT,
    BVector3Array_PyType_Slots
};


static PyTypeObject *
define_BVector3Array_type(PyObject *module)
{
    PyTypeObject *type = (PyTypeObject *)PyType_FromModuleAndSpec(
        module,
        &BVector3Array_PyTypeSpec,
        0
    );
    if (!type){ return 0; }
    // Note:
    // Unlike other functions that steal references, PyModule_AddObject() only
    // decrements the reference count of value on success.
    if (PyModule_AddObject(module, "BVector3Array", (PyObject *)type) < 0)
    {
        Py_DECREF(type);
        return 0;
    }
    return type;
}


static PyTypeObject *
get_BVector3_type()
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    return module_state->BVector3_PyTypeObject;
}


static PyTypeObject *
get_BVector3Array_type()
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    return module_state->BVector3Array_PyTypeObject;
}


static PyObject *
create_BVector3(bool *value)
{
    auto cls = get_BVector3_type();
    auto result = (BVector3 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new BVector3Glm(*(BVector3Glm *)value);
    return (PyObject *)result;
}


static PyObject *
create_BVector3Array(size_t length, bool *value)
{
    auto cls = get_BVector3Array_type();
    auto result = (BVector3Array *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->length = length;
    if (length > 0)
    {
        result->glm = new BVector3Glm[length];
        for (size_t i = 0; i < length; i++)
        {
            result->glm[i] = ((BVector3Glm *)value)[i];
        }
    }
    else
    {
        result->glm = 0;
    }
    return (PyObject *)result;
}


static bool *
get_BVector3_value_ptr(PyObject *self)
{
    if (Py_TYPE(self) != get_BVector3_type())
    {
        PyErr_Format(PyExc_TypeError, "expected BVector3, got %R", self);
        return 0;
    }
    return (bool *)((BVector3 *)self)->glm;
}


static bool *
get_BVector3Array_value_ptr(PyObject *self)
{
    if (Py_TYPE(self) != get_BVector3Array_type())
    {
        PyErr_Format(
            PyExc_TypeError,
            "expected BVector3Array, got %R",
            self
        );
        return 0;
    }
    return (bool *)((BVector3Array *)self)->glm;
}


static size_t
get_BVector3Array_length(PyObject *self)
{
    if (Py_TYPE(self) != get_BVector3Array_type())
    {
        PyErr_Format(
            PyExc_TypeError,
            "expected BVector3Array, got %R",
            self
        );
        return 0;
    }
    return ((BVector3Array *)self)->length;
}

#endif