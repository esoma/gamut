
// generated 2022-03-08 23:43:08.584689 from codegen/math/templates/_vector.hpp

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

typedef glm::vec<3, double, glm::defaultp> DVector3Glm;


struct DVector3
{
    PyObject_HEAD
    PyObject *weakreflist;
    DVector3Glm *glm;
};


static PyObject *
DVector3__new__(PyTypeObject *cls, PyObject *args, PyObject *kwds)
{

        double c_0 = 0;

        double c_1 = 0;

        double c_2 = 0;


    if (kwds && PyDict_Size(kwds) != 0)
    {
        PyErr_SetString(
            PyExc_TypeError,
            "DVector3 does accept any keyword arguments"
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

            break;
        }
        case 3:
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

            break;
        }
        default:
        {
            PyErr_Format(
                PyExc_TypeError,
                "invalid number of arguments supplied to DVector3, expected "
                "0, 1 or 3 (got %zd)",
                arg_count
            );
            return 0;
        }
    }

    DVector3 *self = (DVector3*)cls->tp_alloc(cls, 0);
    if (!self){ return 0; }
    self->glm = new DVector3Glm(

            c_0,

            c_1,

            c_2

    );

    return (PyObject *)self;
}


static void
DVector3__dealloc__(DVector3 *self)
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
DVector3__hash__(DVector3 *self)
{
    Py_ssize_t i, len = 3;
    Py_uhash_t acc = _HASH_XXPRIME_5;
    for (i = 0; i < len; i++)
    {
        Py_uhash_t lane = std::hash<double>{}((*self->glm)[i]);
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
DVector3__repr__(DVector3 *self)
{
    PyObject *result = 0;

        PyObject *py_0 = 0;

        PyObject *py_1 = 0;

        PyObject *py_2 = 0;



        py_0 = c_double_to_pyobject((*self->glm)[0]);
        if (!py_0){ goto cleanup; }

        py_1 = c_double_to_pyobject((*self->glm)[1]);
        if (!py_1){ goto cleanup; }

        py_2 = c_double_to_pyobject((*self->glm)[2]);
        if (!py_2){ goto cleanup; }

    result = PyUnicode_FromFormat(
        "DVector3("

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
DVector3__len__(DVector3 *self)
{
    return 3;
}


static PyObject *
DVector3__getitem__(DVector3 *self, Py_ssize_t index)
{
    if (index < 0 || index > 2)
    {
        PyErr_Format(PyExc_IndexError, "index out of range");
        return 0;
    }
    auto c = (*self->glm)[index];
    return c_double_to_pyobject(c);
}


static PyObject *
DVector3__richcmp__(DVector3 *self, DVector3 *other, int op)
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
DVector3__add__(PyObject *left, PyObject *right)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->DVector3_PyTypeObject;

    DVector3Glm vector;
    if (Py_TYPE(left) == Py_TYPE(right))
    {
        vector = (*((DVector3 *)left)->glm) + (*((DVector3 *)right)->glm);
    }
    else
    {
        if (Py_TYPE(left) == cls)
        {
            auto c_right = pyobject_to_c_double(right);
            if (PyErr_Occurred()){ Py_RETURN_NOTIMPLEMENTED; }
            vector = (*((DVector3 *)left)->glm) + c_right;
        }
        else
        {
            auto c_left = pyobject_to_c_double(left);
            if (PyErr_Occurred()){ Py_RETURN_NOTIMPLEMENTED; }
            vector = c_left + (*((DVector3 *)right)->glm);
        }
    }

    DVector3 *result = (DVector3 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new DVector3Glm(

            vector[0],

            vector[1],

            vector[2]

    );

    return (PyObject *)result;
}


static PyObject *
DVector3__sub__(PyObject *left, PyObject *right)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->DVector3_PyTypeObject;

    DVector3Glm vector;
    if (Py_TYPE(left) == Py_TYPE(right))
    {
        vector = (*((DVector3 *)left)->glm) - (*((DVector3 *)right)->glm);
    }
    else
    {
        if (Py_TYPE(left) == cls)
        {
            auto c_right = pyobject_to_c_double(right);
            if (PyErr_Occurred()){ Py_RETURN_NOTIMPLEMENTED; }
            vector = (*((DVector3 *)left)->glm) - c_right;
        }
        else
        {
            auto c_left = pyobject_to_c_double(left);
            if (PyErr_Occurred()){ Py_RETURN_NOTIMPLEMENTED; }
            vector = c_left - (*((DVector3 *)right)->glm);
        }
    }

    DVector3 *result = (DVector3 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new DVector3Glm(

            vector[0],

            vector[1],

            vector[2]

    );

    return (PyObject *)result;
}


static PyObject *
DVector3__mul__(PyObject *left, PyObject *right)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->DVector3_PyTypeObject;

    DVector3Glm vector;
    if (Py_TYPE(left) == Py_TYPE(right))
    {
        vector = (*((DVector3 *)left)->glm) * (*((DVector3 *)right)->glm);
    }
    else
    {
        if (Py_TYPE(left) == cls)
        {
            auto c_right = pyobject_to_c_double(right);
            if (PyErr_Occurred()){ Py_RETURN_NOTIMPLEMENTED; }
            vector = (*((DVector3 *)left)->glm) * c_right;
        }
        else
        {
            auto c_left = pyobject_to_c_double(left);
            if (PyErr_Occurred()){ Py_RETURN_NOTIMPLEMENTED; }
            vector = c_left * (*((DVector3 *)right)->glm);
        }
    }

    DVector3 *result = (DVector3 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new DVector3Glm(

            vector[0],

            vector[1],

            vector[2]

    );

    return (PyObject *)result;
}



    static PyObject *
    DVector3__matmul__(DVector3 *left, DVector3 *right)
    {
        auto cls = Py_TYPE(left);
        if (Py_TYPE(left) != Py_TYPE(right)){ Py_RETURN_NOTIMPLEMENTED; }
        auto c_result = glm::dot(*left->glm, *right->glm);
        return c_double_to_pyobject(c_result);
    }


    static PyObject *
    DVector3__mod__(PyObject *left, PyObject *right)
    {
        auto module_state = get_module_state();
        if (!module_state){ return 0; }
        auto cls = module_state->DVector3_PyTypeObject;

        DVector3Glm vector;
        if (Py_TYPE(left) == Py_TYPE(right))
        {
            vector = glm::mod(
                *((DVector3 *)left)->glm,
                *((DVector3 *)right)->glm
            );
        }
        else
        {
            if (Py_TYPE(left) == cls)
            {
                auto c_right = pyobject_to_c_double(right);
                if (PyErr_Occurred()){ Py_RETURN_NOTIMPLEMENTED; }
                vector = glm::mod(*((DVector3 *)left)->glm, c_right);
            }
            else
            {
                auto c_left = pyobject_to_c_double(left);
                if (PyErr_Occurred()){ Py_RETURN_NOTIMPLEMENTED; }
                vector = glm::mod(DVector3Glm(c_left), *((DVector3 *)right)->glm);
            }
        }

        DVector3 *result = (DVector3 *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new DVector3Glm(

                vector[0],

                vector[1],

                vector[2]

        );

        return (PyObject *)result;
    }


    static PyObject *
    DVector3__pow__(PyObject *left, PyObject *right)
    {
        auto module_state = get_module_state();
        if (!module_state){ return 0; }
        auto cls = module_state->DVector3_PyTypeObject;

        DVector3Glm vector;
        if (Py_TYPE(left) == Py_TYPE(right))
        {
            vector = glm::pow(
                *((DVector3 *)left)->glm,
                *((DVector3 *)right)->glm
            );
        }
        else
        {
            if (Py_TYPE(left) == cls)
            {
                auto c_right = pyobject_to_c_double(right);
                if (PyErr_Occurred()){ Py_RETURN_NOTIMPLEMENTED; }
                vector = glm::pow(*((DVector3 *)left)->glm, DVector3Glm(c_right));
            }
            else
            {
                auto c_left = pyobject_to_c_double(left);
                if (PyErr_Occurred()){ Py_RETURN_NOTIMPLEMENTED; }
                vector = glm::pow(DVector3Glm(c_left), *((DVector3 *)right)->glm);
            }
        }

        DVector3 *result = (DVector3 *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new DVector3Glm(

                vector[0],

                vector[1],

                vector[2]

        );

        return (PyObject *)result;
    }





    static PyObject *
    DVector3__truediv__(PyObject *left, PyObject *right)
    {
        auto module_state = get_module_state();
        if (!module_state){ return 0; }
        auto cls = module_state->DVector3_PyTypeObject;

        DVector3Glm vector;
        if (Py_TYPE(left) == Py_TYPE(right))
        {

            vector = (*((DVector3 *)left)->glm) / (*((DVector3 *)right)->glm);
        }
        else
        {
            if (Py_TYPE(left) == cls)
            {
                auto c_right = pyobject_to_c_double(right);
                if (PyErr_Occurred()){ Py_RETURN_NOTIMPLEMENTED; }

                vector = (*((DVector3 *)left)->glm) / c_right;
            }
            else
            {
                auto c_left = pyobject_to_c_double(left);
                if (PyErr_Occurred()){ Py_RETURN_NOTIMPLEMENTED; }

                vector = c_left / (*((DVector3 *)right)->glm);
            }
        }

        DVector3 *result = (DVector3 *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new DVector3Glm(

                vector[0],

                vector[1],

                vector[2]

        );

        return (PyObject *)result;
    }




    static PyObject *
    DVector3__neg__(DVector3 *self)
    {
        auto cls = Py_TYPE(self);

            DVector3Glm vector = -(*self->glm);


        DVector3 *result = (DVector3 *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new DVector3Glm(

                vector[0],

                vector[1],

                vector[2]

        );

        return (PyObject *)result;
    }



static PyObject *
DVector3__abs__(DVector3 *self)
{
    auto cls = Py_TYPE(self);
    DVector3Glm vector = glm::abs(*self->glm);

    DVector3 *result = (DVector3 *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new DVector3Glm(

            vector[0],

            vector[1],

            vector[2]

    );

    return (PyObject *)result;
}


static int
DVector3__bool__(DVector3 *self)
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
DVector3_getbufferproc(DVector3 *self, Py_buffer *view, int flags)
{
    if (flags & PyBUF_WRITABLE)
    {
        PyErr_SetString(PyExc_TypeError, "DVector3 is not read only");
        view->obj = 0;
        return -1;
    }
    view->buf = glm::value_ptr(*self->glm);
    view->obj = (PyObject *)self;
    view->len = sizeof(double) * 3;
    view->readonly = 1;
    view->itemsize = sizeof(double);
    view->format = "d";
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
    DVector3_Getter_0(DVector3 *self, void *)
    {
        auto c = (*self->glm)[0];
        return c_double_to_pyobject(c);
    }

    static PyObject *
    DVector3_Getter_1(DVector3 *self, void *)
    {
        auto c = (*self->glm)[1];
        return c_double_to_pyobject(c);
    }

    static PyObject *
    DVector3_Getter_2(DVector3 *self, void *)
    {
        auto c = (*self->glm)[2];
        return c_double_to_pyobject(c);
    }




    static PyObject *
    DVector3_magnitude(DVector3 *self, void *)
    {
        auto magnitude = glm::length(*self->glm);
        return c_double_to_pyobject(magnitude);
    }



static PyGetSetDef DVector3_PyGetSetDef[] = {
    {"x", (getter)DVector3_Getter_0, 0, 0, 0},
    {"r", (getter)DVector3_Getter_0, 0, 0, 0},
    {"s", (getter)DVector3_Getter_0, 0, 0, 0},
    {"u", (getter)DVector3_Getter_0, 0, 0, 0},

        {"y", (getter)DVector3_Getter_1, 0, 0, 0},
        {"g", (getter)DVector3_Getter_1, 0, 0, 0},
        {"t", (getter)DVector3_Getter_1, 0, 0, 0},
        {"v", (getter)DVector3_Getter_1, 0, 0, 0},


        {"z", (getter)DVector3_Getter_2, 0, 0, 0},
        {"b", (getter)DVector3_Getter_2, 0, 0, 0},
        {"p", (getter)DVector3_Getter_2, 0, 0, 0},



        {"magnitude", (getter)DVector3_magnitude, 0, 0, 0},

    {0, 0, 0, 0, 0}
};


static PyObject *
DVector3__getattr__(DVector3 *self, PyObject *py_attr)
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
        auto py_c = c_double_to_pyobject((*self->glm)[glm_index]);
        PyTuple_SET_ITEM(result, i, py_c);
    }

    PyErr_Clear();
    return result;
}


static PyMemberDef DVector3_PyMemberDef[] = {
    {"__weaklistoffset__", T_PYSSIZET, offsetof(DVector3, weakreflist), READONLY},
    {0}
};




        static DVector3 *
        DVector3_cross(DVector3 *self, DVector3 *other)
        {
            auto cls = Py_TYPE(self);
            if (Py_TYPE(other) != cls)
            {
                PyErr_Format(PyExc_TypeError, "%R is not DVector3", other);
                return 0;
            }
            auto vector = glm::cross(*self->glm, *other->glm);
            DVector3 *result = (DVector3 *)cls->tp_alloc(cls, 0);
            if (!result){ return 0; }
            result->glm = new DVector3Glm(

                    vector[0],

                    vector[1],

                    vector[2]

            );
            return result;
        }


    static DVector3 *
    DVector3_normalize(DVector3 *self, void*)
    {
        auto cls = Py_TYPE(self);
        auto vector = glm::normalize(*self->glm);
        DVector3 *result = (DVector3 *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new DVector3Glm(

                vector[0],

                vector[1],

                vector[2]

        );
        return result;
    }


    static PyObject *
    DVector3_distance(DVector3 *self, DVector3 *other)
    {
        auto cls = Py_TYPE(self);
        if (Py_TYPE(other) != cls)
        {
            PyErr_Format(PyExc_TypeError, "%R is not DVector3", other);
            return 0;
        }
        auto result = glm::distance(*self->glm, *other->glm);
        return c_double_to_pyobject(result);
    }



static PyObject *
DVector3_get_limits(DVector3 *self, void *)
{
    auto c_min = std::numeric_limits<double>::lowest();
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


static PyMethodDef DVector3_PyMethodDef[] = {


            {"cross", (PyCFunction)DVector3_cross, METH_O, 0},

        {"normalize", (PyCFunction)DVector3_normalize, METH_NOARGS, 0},
        {"distance", (PyCFunction)DVector3_distance, METH_O, 0},

    {"get_limits", (PyCFunction)DVector3_get_limits, METH_NOARGS | METH_STATIC, 0},
    {0, 0, 0, 0}
};


static PyType_Slot DVector3_PyType_Slots [] = {
    {Py_tp_new, (void*)DVector3__new__},
    {Py_tp_dealloc, (void*)DVector3__dealloc__},
    {Py_tp_hash, (void*)DVector3__hash__},
    {Py_tp_repr, (void*)DVector3__repr__},
    {Py_sq_length, (void*)DVector3__len__},
    {Py_sq_item, (void*)DVector3__getitem__},
    {Py_tp_richcompare, (void*)DVector3__richcmp__},
    {Py_nb_add, (void*)DVector3__add__},
    {Py_nb_subtract, (void*)DVector3__sub__},
    {Py_nb_multiply, (void*)DVector3__mul__},

        {Py_nb_matrix_multiply, (void*)DVector3__matmul__},
        {Py_nb_remainder, (void*)DVector3__mod__},
        {Py_nb_power, (void*)DVector3__pow__},


        {Py_nb_true_divide, (void*)DVector3__truediv__},


        {Py_nb_negative, (void*)DVector3__neg__},

    {Py_nb_absolute, (void*)DVector3__abs__},
    {Py_nb_bool, (void*)DVector3__bool__},
    {Py_bf_getbuffer, (void*)DVector3_getbufferproc},
    {Py_tp_getset, (void*)DVector3_PyGetSetDef},
    {Py_tp_getattro, (void*)DVector3__getattr__},
    {Py_tp_members, (void*)DVector3_PyMemberDef},
    {Py_tp_methods, (void*)DVector3_PyMethodDef},
    {0, 0},
};


static PyType_Spec DVector3_PyTypeSpec = {
    "gamut.math.DVector3",
    sizeof(DVector3),
    0,
    Py_TPFLAGS_DEFAULT,
    DVector3_PyType_Slots
};


static PyTypeObject *
define_DVector3_type(PyObject *module)
{
    PyTypeObject *type = (PyTypeObject *)PyType_FromModuleAndSpec(
        module,
        &DVector3_PyTypeSpec,
        0
    );
    if (!type){ return 0; }
    // Note:
    // Unlike other functions that steal references, PyModule_AddObject() only
    // decrements the reference count of value on success.
    if (PyModule_AddObject(module, "DVector3", (PyObject *)type) < 0)
    {
        Py_DECREF(type);
        return 0;
    }
    return type;
}