
// python
#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <structmember.h>
// glm
#include <glm/detail/type_vec3.hpp>
#include <stdio.h>
// gamut
#include "_type.hpp"

typedef glm::vec<3, double, glm::defaultp> DVector3Glm;


struct DVector3
{
    PyObject_HEAD
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
            Py_DECREF(arg);
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
                Py_DECREF(arg);
                if (error_occurred){ return 0; }
            }

            {
                auto arg = PyTuple_GET_ITEM(args, 1);
                c_1 = pyobject_to_c_double(arg);
                auto error_occurred = PyErr_Occurred();
                Py_DECREF(arg);
                if (error_occurred){ return 0; }
            }

            {
                auto arg = PyTuple_GET_ITEM(args, 2);
                c_2 = pyobject_to_c_double(arg);
                auto error_occurred = PyErr_Occurred();
                Py_DECREF(arg);
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
    delete self->glm;

    PyTypeObject *type = Py_TYPE(self);
    type->tp_free(self);
    Py_DECREF(type);
}


static Py_ssize_t
DVector3__len__(DVector3 *self)
{
    return 3;
}


static PyObject *
DVector3__getitem__(DVector3 *self, Py_ssize_t index)
{
    if (index < -3 || index > 2)
    {
        PyErr_Format(PyExc_IndexError, "invalid index %zd", index);
        return 0;
    }
    if (index < 0)
    {
        index = 3 - index;
    }

    auto c = (*self->glm)[index];
    return c_double_to_pyobject(c);
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


    {0, 0, 0, 0, 0}
};


static PyType_Slot DVector3_PyType_Slots [] = {
    {Py_tp_new, (void*)DVector3__new__},
    {Py_tp_dealloc, (void*)DVector3__dealloc__},
    {Py_sq_length, (void*)DVector3__len__},
    {Py_sq_item, (void*)DVector3__getitem__},
    {Py_tp_getset, (void*)DVector3_PyGetSetDef},
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