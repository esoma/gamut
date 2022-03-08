// generated 2022-03-08 02:13:12.875570 from codegen/math/templates/_vector.hpp

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

typedef glm::vec<2, float, glm::defaultp> FVector2Glm;


struct FVector2
{
    PyObject_HEAD
    PyObject *weakreflist;
    FVector2Glm *glm;
};


static PyObject *
FVector2__new__(PyTypeObject *cls, PyObject *args, PyObject *kwds)
{

        float c_0 = 0;

        float c_1 = 0;


    if (kwds && PyDict_Size(kwds) != 0)
    {
        PyErr_SetString(
            PyExc_TypeError,
            "FVector2 does accept any keyword arguments"
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

            break;
        }
        case 2:
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

            break;
        }
        default:
        {
            PyErr_Format(
                PyExc_TypeError,
                "invalid number of arguments supplied to FVector2, expected "
                "0, 1 or 2 (got %zd)",
                arg_count
            );
            return 0;
        }
    }

    FVector2 *self = (FVector2*)cls->tp_alloc(cls, 0);
    if (!self){ return 0; }
    self->glm = new FVector2Glm(

            c_0,

            c_1

    );

    return (PyObject *)self;
}


static void
FVector2__dealloc__(FVector2 *self)
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
FVector2__hash__(FVector2 *self)
{
    Py_ssize_t i, len = 2;
    Py_uhash_t acc = _HASH_XXPRIME_5;
    for (i = 0; i < len; i++)
    {
        Py_uhash_t lane = std::hash<float>{}((*self->glm)[i]);
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
FVector2__repr__(FVector2 *self)
{
    PyObject *result = 0;

        PyObject *py_0 = 0;

        PyObject *py_1 = 0;



        py_0 = c_float_to_pyobject((*self->glm)[0]);
        if (!py_0){ goto cleanup; }

        py_1 = c_float_to_pyobject((*self->glm)[1]);
        if (!py_1){ goto cleanup; }

    result = PyUnicode_FromFormat(
        "FVector2("

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
FVector2__len__(FVector2 *self)
{
    return 2;
}


static PyObject *
FVector2__getitem__(FVector2 *self, Py_ssize_t index)
{
    if (index < 0 || index > 1)
    {
        PyErr_Format(PyExc_IndexError, "index out of range");
        return 0;
    }
    auto c = (*self->glm)[index];
    return c_float_to_pyobject(c);
}


static PyObject *
FVector2__richcmp__(FVector2 *self, FVector2 *other, int op)
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
FVector2__add__(PyObject *left, PyObject *right)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->FVector2_PyTypeObject;

    FVector2Glm vector;
    if (Py_TYPE(left) == Py_TYPE(right))
    {
        vector = (*((FVector2 *)left)->glm) + (*((FVector2 *)right)->glm);
    }
    else
    {
        if (Py_TYPE(left) == cls)
        {
            auto c_right = pyobject_to_c_float(right);
            if (PyErr_Occurred()){ Py_RETURN_NOTIMPLEMENTED; }
            vector = (*((FVector2 *)left)->glm) + c_right;
        }
        else
        {
            auto c_left = pyobject_to_c_float(left);
            if (PyErr_Occurred()){ Py_RETURN_NOTIMPLEMENTED; }
            vector = c_left + (*((FVector2 *)right)->glm);
        }
    }

    FVector2 *result = (FVector2 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new FVector2Glm(

            vector[0],

            vector[1]

    );

    return (PyObject *)result;
}


static PyObject *
FVector2__sub__(PyObject *left, PyObject *right)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->FVector2_PyTypeObject;

    FVector2Glm vector;
    if (Py_TYPE(left) == Py_TYPE(right))
    {
        vector = (*((FVector2 *)left)->glm) - (*((FVector2 *)right)->glm);
    }
    else
    {
        if (Py_TYPE(left) == cls)
        {
            auto c_right = pyobject_to_c_float(right);
            if (PyErr_Occurred()){ Py_RETURN_NOTIMPLEMENTED; }
            vector = (*((FVector2 *)left)->glm) - c_right;
        }
        else
        {
            auto c_left = pyobject_to_c_float(left);
            if (PyErr_Occurred()){ Py_RETURN_NOTIMPLEMENTED; }
            vector = c_left - (*((FVector2 *)right)->glm);
        }
    }

    FVector2 *result = (FVector2 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new FVector2Glm(

            vector[0],

            vector[1]

    );

    return (PyObject *)result;
}


static PyObject *
FVector2__mul__(PyObject *left, PyObject *right)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->FVector2_PyTypeObject;

    FVector2Glm vector;
    if (Py_TYPE(left) == Py_TYPE(right))
    {
        vector = (*((FVector2 *)left)->glm) * (*((FVector2 *)right)->glm);
    }
    else
    {
        if (Py_TYPE(left) == cls)
        {
            auto c_right = pyobject_to_c_float(right);
            if (PyErr_Occurred()){ Py_RETURN_NOTIMPLEMENTED; }
            vector = (*((FVector2 *)left)->glm) * c_right;
        }
        else
        {
            auto c_left = pyobject_to_c_float(left);
            if (PyErr_Occurred()){ Py_RETURN_NOTIMPLEMENTED; }
            vector = c_left * (*((FVector2 *)right)->glm);
        }
    }

    FVector2 *result = (FVector2 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new FVector2Glm(

            vector[0],

            vector[1]

    );

    return (PyObject *)result;
}



    static PyObject *
    FVector2__matmul__(FVector2 *left, FVector2 *right)
    {
        auto cls = Py_TYPE(left);
        if (Py_TYPE(left) != Py_TYPE(right)){ Py_RETURN_NOTIMPLEMENTED; }
        auto c_result = glm::dot(*left->glm, *right->glm);
        return c_float_to_pyobject(c_result);
    }


    static PyObject *
    FVector2__mod__(PyObject *left, PyObject *right)
    {
        auto module_state = get_module_state();
        if (!module_state){ return 0; }
        auto cls = module_state->FVector2_PyTypeObject;

        FVector2Glm vector;
        if (Py_TYPE(left) == Py_TYPE(right))
        {
            vector = glm::mod(
                *((FVector2 *)left)->glm,
                *((FVector2 *)right)->glm
            );
        }
        else
        {
            if (Py_TYPE(left) == cls)
            {
                auto c_right = pyobject_to_c_float(right);
                if (PyErr_Occurred()){ Py_RETURN_NOTIMPLEMENTED; }
                vector = glm::mod(*((FVector2 *)left)->glm, c_right);
            }
            else
            {
                auto c_left = pyobject_to_c_float(left);
                if (PyErr_Occurred()){ Py_RETURN_NOTIMPLEMENTED; }
                vector = glm::mod(FVector2Glm(c_left), *((FVector2 *)right)->glm);
            }
        }

        FVector2 *result = (FVector2 *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new FVector2Glm(

                vector[0],

                vector[1]

        );

        return (PyObject *)result;
    }


    static PyObject *
    FVector2__pow__(PyObject *left, PyObject *right)
    {
        auto module_state = get_module_state();
        if (!module_state){ return 0; }
        auto cls = module_state->FVector2_PyTypeObject;

        FVector2Glm vector;
        if (Py_TYPE(left) == Py_TYPE(right))
        {
            vector = glm::pow(
                *((FVector2 *)left)->glm,
                *((FVector2 *)right)->glm
            );
        }
        else
        {
            if (Py_TYPE(left) == cls)
            {
                auto c_right = pyobject_to_c_float(right);
                if (PyErr_Occurred()){ Py_RETURN_NOTIMPLEMENTED; }
                vector = glm::pow(*((FVector2 *)left)->glm, FVector2Glm(c_right));
            }
            else
            {
                auto c_left = pyobject_to_c_float(left);
                if (PyErr_Occurred()){ Py_RETURN_NOTIMPLEMENTED; }
                vector = glm::pow(FVector2Glm(c_left), *((FVector2 *)right)->glm);
            }
        }

        FVector2 *result = (FVector2 *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new FVector2Glm(

                vector[0],

                vector[1]

        );

        return (PyObject *)result;
    }





    static PyObject *
    FVector2__truediv__(PyObject *left, PyObject *right)
    {
        auto module_state = get_module_state();
        if (!module_state){ return 0; }
        auto cls = module_state->FVector2_PyTypeObject;

        FVector2Glm vector;
        if (Py_TYPE(left) == Py_TYPE(right))
        {

            vector = (*((FVector2 *)left)->glm) / (*((FVector2 *)right)->glm);
        }
        else
        {
            if (Py_TYPE(left) == cls)
            {
                auto c_right = pyobject_to_c_float(right);
                if (PyErr_Occurred()){ Py_RETURN_NOTIMPLEMENTED; }

                vector = (*((FVector2 *)left)->glm) / c_right;
            }
            else
            {
                auto c_left = pyobject_to_c_float(left);
                if (PyErr_Occurred()){ Py_RETURN_NOTIMPLEMENTED; }

                vector = c_left / (*((FVector2 *)right)->glm);
            }
        }

        FVector2 *result = (FVector2 *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new FVector2Glm(

                vector[0],

                vector[1]

        );

        return (PyObject *)result;
    }




    static PyObject *
    FVector2__neg__(FVector2 *self)
    {
        auto cls = Py_TYPE(self);

            FVector2Glm vector = -(*self->glm);


        FVector2 *result = (FVector2 *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new FVector2Glm(

                vector[0],

                vector[1]

        );

        return (PyObject *)result;
    }



static PyObject *
FVector2__abs__(FVector2 *self)
{
    auto cls = Py_TYPE(self);
    FVector2Glm vector = glm::abs(*self->glm);

    FVector2 *result = (FVector2 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new FVector2Glm(

            vector[0],

            vector[1]

    );

    return (PyObject *)result;
}


static int
FVector2__bool__(FVector2 *self)
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
FVector2_getbufferproc(FVector2 *self, Py_buffer *view, int flags)
{
    if (flags & PyBUF_WRITABLE)
    {
        PyErr_SetString(PyExc_TypeError, "FVector2 is not read only");
        view->obj = 0;
        return -1;
    }
    view->buf = glm::value_ptr(*self->glm);
    view->obj = (PyObject *)self;
    view->len = sizeof(float) * 2;
    view->readonly = 1;
    view->itemsize = sizeof(float);
    view->format = "f";
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
    FVector2_Getter_0(FVector2 *self, void *)
    {
        auto c = (*self->glm)[0];
        return c_float_to_pyobject(c);
    }

    static PyObject *
    FVector2_Getter_1(FVector2 *self, void *)
    {
        auto c = (*self->glm)[1];
        return c_float_to_pyobject(c);
    }




    static PyObject *
    FVector2_magnitude(FVector2 *self, void *)
    {
        auto magnitude = glm::length(*self->glm);
        return c_float_to_pyobject(magnitude);
    }



static PyGetSetDef FVector2_PyGetSetDef[] = {
    {"x", (getter)FVector2_Getter_0, 0, 0, 0},
    {"r", (getter)FVector2_Getter_0, 0, 0, 0},
    {"s", (getter)FVector2_Getter_0, 0, 0, 0},
    {"u", (getter)FVector2_Getter_0, 0, 0, 0},

        {"y", (getter)FVector2_Getter_1, 0, 0, 0},
        {"g", (getter)FVector2_Getter_1, 0, 0, 0},
        {"t", (getter)FVector2_Getter_1, 0, 0, 0},
        {"v", (getter)FVector2_Getter_1, 0, 0, 0},




        {"magnitude", (getter)FVector2_magnitude, 0, 0, 0},

    {0, 0, 0, 0, 0}
};


static PyObject *
FVector2__getattr__(FVector2 *self, PyObject *py_attr)
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
        auto py_c = c_float_to_pyobject((*self->glm)[glm_index]);
        PyTuple_SET_ITEM(result, i, py_c);
    }

    PyErr_Clear();
    return result;
}


static PyMemberDef FVector2_PyMemberDef[] = {
    {"__weaklistoffset__", T_PYSSIZET, offsetof(FVector2, weakreflist), READONLY},
    {0}
};





    static FVector2 *
    FVector2_normalize(FVector2 *self, void*)
    {
        auto cls = Py_TYPE(self);
        auto vector = glm::normalize(*self->glm);
        FVector2 *result = (FVector2 *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new FVector2Glm(

                vector[0],

                vector[1]

        );
        return result;
    }


    static PyObject *
    FVector2_distance(FVector2 *self, FVector2 *other)
    {
        auto cls = Py_TYPE(self);
        if (Py_TYPE(other) != cls)
        {
            PyErr_Format(PyExc_TypeError, "%R is not FVector2", other);
            return 0;
        }
        auto result = glm::distance(*self->glm, *other->glm);
        return c_float_to_pyobject(result);
    }



static PyObject *
FVector2_get_limits(FVector2 *self, void *)
{
    auto c_min = std::numeric_limits<float>::min();
    auto c_max = std::numeric_limits<float>::max();
    auto py_min = c_float_to_pyobject(c_min);
    if (!py_min){ return 0; }
    auto py_max = c_float_to_pyobject(c_max);
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


static PyMethodDef FVector2_PyMethodDef[] = {


        {"normalize", (PyCFunction)FVector2_normalize, METH_NOARGS, 0},
        {"distance", (PyCFunction)FVector2_distance, METH_O, 0},

    {"get_limits", (PyCFunction)FVector2_get_limits, METH_NOARGS | METH_STATIC, 0},
    {0, 0, 0, 0}
};


static PyType_Slot FVector2_PyType_Slots [] = {
    {Py_tp_new, (void*)FVector2__new__},
    {Py_tp_dealloc, (void*)FVector2__dealloc__},
    {Py_tp_hash, (void*)FVector2__hash__},
    {Py_tp_repr, (void*)FVector2__repr__},
    {Py_sq_length, (void*)FVector2__len__},
    {Py_sq_item, (void*)FVector2__getitem__},
    {Py_tp_richcompare, (void*)FVector2__richcmp__},
    {Py_nb_add, (void*)FVector2__add__},
    {Py_nb_subtract, (void*)FVector2__sub__},
    {Py_nb_multiply, (void*)FVector2__mul__},

        {Py_nb_matrix_multiply, (void*)FVector2__matmul__},
        {Py_nb_remainder, (void*)FVector2__mod__},
        {Py_nb_power, (void*)FVector2__pow__},


        {Py_nb_true_divide, (void*)FVector2__truediv__},


        {Py_nb_negative, (void*)FVector2__neg__},

    {Py_nb_absolute, (void*)FVector2__abs__},
    {Py_nb_bool, (void*)FVector2__bool__},
    {Py_bf_getbuffer, (void*)FVector2_getbufferproc},
    {Py_tp_getset, (void*)FVector2_PyGetSetDef},
    {Py_tp_getattro, (void*)FVector2__getattr__},
    {Py_tp_members, (void*)FVector2_PyMemberDef},
    {Py_tp_methods, (void*)FVector2_PyMethodDef},
    {0, 0},
};


static PyType_Spec FVector2_PyTypeSpec = {
    "gamut.math.FVector2",
    sizeof(FVector2),
    0,
    Py_TPFLAGS_DEFAULT,
    FVector2_PyType_Slots
};


static PyTypeObject *
define_FVector2_type(PyObject *module)
{
    PyTypeObject *type = (PyTypeObject *)PyType_FromModuleAndSpec(
        module,
        &FVector2_PyTypeSpec,
        0
    );
    if (!type){ return 0; }
    // Note:
    // Unlike other functions that steal references, PyModule_AddObject() only
    // decrements the reference count of value on success.
    if (PyModule_AddObject(module, "FVector2", (PyObject *)type) < 0)
    {
        Py_DECREF(type);
        return 0;
    }
    return type;
}