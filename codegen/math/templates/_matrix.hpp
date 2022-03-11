
// generated {{ when }} from codegen/math/templates/_matrix.hpp

#ifndef GAMUT_MATH_{{ name.upper() }}_HPP
#define GAMUT_MATH_{{ name.upper() }}_HPP

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
#include "_matrixtype.hpp"
#include "_type.hpp"


static PyObject *
{{ name }}__new__(PyTypeObject *cls, PyObject *args, PyObject *kwds)
{
    if (kwds && PyDict_Size(kwds) != 0)
    {
        PyErr_SetString(
            PyExc_TypeError,
            "{{ name }} does accept any keyword arguments"
        );
        return 0;
    }

    {{ name }}Glm *glm = 0;
    auto arg_count = PyTuple_GET_SIZE(args);
    switch (PyTuple_GET_SIZE(args))
    {
        case 0:
        {
            glm = new {{ name }}Glm();
            break;
        }
        case 1:
        {
            auto arg = PyTuple_GET_ITEM(args, 0);
            {{ c_type }} arg_c = pyobject_to_c_{{ c_type.replace(' ', '_') }}(arg);
            auto error_occurred = PyErr_Occurred();
            if (error_occurred){ return 0; }
            glm = new {{ name }}Glm(arg_c);
            break;
        }
        case {{ row_size }}:
        {
            auto module_state = get_module_state();
            if (!module_state){ return 0; }
            auto column_cls = module_state->{{ column_type }}_PyTypeObject;
            {% for i in range(row_size) %}
                PyObject *p_{{ i }} = PyTuple_GET_ITEM(args, {{ i }});
                if (Py_TYPE(p_{{ i }}) != column_cls)
                {
                    PyErr_Format(
                        PyExc_TypeError,
                        "invalid column supplied, expected %R, (got %R)",
                        column_cls,
                        p_{{ i }}
                    );
                    return 0;
                }
            {% endfor %}
            glm = new {{ name }}Glm(
                {% for i in range(row_size) %}
                    *(({{ column_type }} *)p_{{ i }})->glm{% if i != row_size - 1 %}, {% endif %}
                {% endfor %}
            );

            break;
        }
        case {{ component_count }}:
        {
            {% for i in range(component_count) %}
                {{ c_type }} c_{{ i }} = 0;
            {% endfor %}
            {% for i in range(component_count) %}
            {
                auto arg = PyTuple_GET_ITEM(args, {{ i }});
                c_{{ i }} = pyobject_to_c_{{ c_type.replace(' ', '_') }}(arg);
                auto error_occurred = PyErr_Occurred();
                if (error_occurred){ return 0; }
            }
            {% endfor %}
            glm = new {{ name }}Glm(
                {% for i in range(component_count) %}
                    c_{{ i }}{% if i != component_count - 1 %}, {% endif %}
                {% endfor %}
            );
            break;
        }
        default:
        {
            PyErr_Format(
                PyExc_TypeError,
                "invalid number of arguments supplied to {{ name }}, expected "
                "0, 1, {{ row_size }} or {{ component_count }} (got %zd)",
                arg_count
            );
            return 0;
        }
    }

    {{ name }} *self = ({{ name }}*)cls->tp_alloc(cls, 0);
    if (!self)
    {
        delete glm;
        return 0;
    }
    self->glm = glm;

    return (PyObject *)self;
}


static void
{{ name }}__dealloc__({{ name }} *self)
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
{{ name }}__hash__({{ name }} *self)
{
    Py_ssize_t len = {{ component_count }};
    Py_uhash_t acc = _HASH_XXPRIME_5;
    for ({{ name }}Glm::length_type c = 0; c < {{ column_size }}; c++)
    {
        for ({{ name }}Glm::length_type r = 0; r < {{ row_size }}; r++)
        {
            Py_uhash_t lane = std::hash<{{ c_type }}>{}((*self->glm)[r][c]);
            acc += lane * _HASH_XXPRIME_2;
            acc = _HASH_XXROTATE(acc);
            acc *= _HASH_XXPRIME_1;
        }
    }
    acc += len ^ (_HASH_XXPRIME_5 ^ 3527539UL);

    if (acc == (Py_uhash_t)-1) {
        return 1546275796;
    }
    return acc;
}


static PyObject *
{{ name }}__repr__({{ name }} *self)
{
    PyObject *result = 0;
    {% for c in range(column_size) %}
    {% for r in range(row_size) %}
        PyObject *py_{{ c }}_{{ r }} = 0;
    {% endfor %}
    {% endfor %}

    {% for c in range(column_size) %}
    {% for r in range(row_size) %}
        py_{{ c }}_{{ r }} = c_{{ c_type.replace(' ', '_') }}_to_pyobject((*self->glm)[{{ r }}][{{ c }}]);
        if (!py_{{ c }}_{{ r }}){ goto cleanup; }
    {% endfor %}
    {% endfor %}

    result = PyUnicode_FromFormat(
        "{{ name }}("
        {% for r in range(row_size) %}
        "("
        {% for c in range(column_size) %}
            "%R"
            {% if c != column_size - 1 %}", "{% endif %}
        {% endfor %}
        ")"
        {% if r != row_size - 1 %}
        ", "
        {% endif %}
        {% endfor %}
        ")",
        {% for r in range(row_size) %}
        {% for c in range(column_size) %}
            py_{{ c }}_{{ r }}
            {% if r == row_size - 1 and c == column_size - 1 %}{% else %}, {% endif %}
        {% endfor %}
        {% endfor %}
    );
cleanup:
    {% for c in range(column_size) %}
    {% for r in range(row_size) %}
        Py_XDECREF(py_{{ c }}_{{ r }});
    {% endfor %}
    {% endfor %}
    return result;
}


static Py_ssize_t
{{ name }}__len__({{ name }} *self)
{
    return {{ row_size }};
}


static PyObject *
{{ name }}__getitem__({{ name }} *self, Py_ssize_t index)
{
    if (index < 0 || index > {{ row_size - 1 }})
    {
        PyErr_Format(PyExc_IndexError, "index out of range");
        return 0;
    }
    const auto& v = (*self->glm)[({{ name }}Glm::length_type)index];
    return (PyObject *)create_{{ column_type }}_from_glm(v);
}


static PyObject *
{{ name}}__richcmp__({{ name }} *self, {{ name }} *other, int op)
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
{{ name}}__add__(PyObject *left, PyObject *right)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->{{ name }}_PyTypeObject;

    {{ name }}Glm matrix;
    if (Py_TYPE(left) == Py_TYPE(right))
    {
        matrix = (*(({{ name }} *)left)->glm) + (*(({{ name }} *)right)->glm);
    }
    else
    {
        if (Py_TYPE(left) == cls)
        {
            auto c_right = pyobject_to_c_{{ c_type.replace(' ', '_') }}(right);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
            matrix = (*(({{ name }} *)left)->glm) + c_right;
        }
        else
        {
            auto c_left = pyobject_to_c_{{ c_type.replace(' ', '_') }}(left);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
            matrix = (*(({{ name }} *)right)->glm) + c_left;
        }
    }

    {{ name }} *result = ({{ name }} *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new {{ name }}Glm(matrix);

    return (PyObject *)result;
}


static PyObject *
{{ name}}__sub__(PyObject *left, PyObject *right)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->{{ name }}_PyTypeObject;

    {{ name }}Glm matrix;
    if (Py_TYPE(left) == Py_TYPE(right))
    {
        matrix = (*(({{ name }} *)left)->glm) - (*(({{ name }} *)right)->glm);
    }
    else
    {
        if (Py_TYPE(left) == cls)
        {
            auto c_right = pyobject_to_c_{{ c_type.replace(' ', '_') }}(right);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
            matrix = (*(({{ name }} *)left)->glm) - c_right;
        }
        else
        {
            auto c_left = pyobject_to_c_{{ c_type.replace(' ', '_') }}(left);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
            {% if column_size == row_size %}
                matrix = c_left - (*(({{ name }} *)right)->glm);
            {% else %}
                matrix = {{ name }}Glm(
                    {% for i in range(component_count) %}
                        c_left{% if i < component_count - 1 %}, {% endif %}
                    {% endfor %}
                ) - (*(({{ name }} *)right)->glm);
            {% endif %}
        }
    }

    {{ name }} *result = ({{ name }} *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new {{ name }}Glm(matrix);

    return (PyObject *)result;
}


static PyObject *
{{ name}}__mul__(PyObject *left, PyObject *right)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->{{ name }}_PyTypeObject;

    {{ name }}Glm matrix;
    if (Py_TYPE(left) == cls)
    {
        auto c_right = pyobject_to_c_{{ c_type.replace(' ', '_') }}(right);
        if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
        matrix = (*(({{name }} *)left)->glm) * c_right;
    }
    else
    {
        auto c_left = pyobject_to_c_{{ c_type.replace(' ', '_') }}(left);
        if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
        matrix = c_left * (*(({{name }} *)right)->glm);
    }

    {{ name }} *result = ({{ name }} *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new {{ name }}Glm(matrix);

    return (PyObject *)result;
}


static PyObject *
{{ name}}__matmul__(PyObject *left, PyObject *right)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->{{ name }}_PyTypeObject;

    if (Py_TYPE(left) == cls)
    {
        {% for c in range(2, 5) %}
        {% with right_name=(('D' if c_type == 'double' else 'F') + 'Matrix' + str(c) + 'x' + str(row_size)) %}
        {% with result_name=(('D' if c_type == 'double' else 'F') + 'Matrix' + str(c) + 'x' + str(column_size)) %}
        {
            auto right_cls = module_state->{{ right_name }}_PyTypeObject;
            auto result_cls = module_state->{{ result_name }}_PyTypeObject;
            if (Py_TYPE(right) == right_cls)
            {
                {{ result_name }} *result = ({{ result_name }} *)result_cls->tp_alloc(result_cls, 0);
                if (!result){ return 0; }
                result->glm = new {{ result_name }}Glm(
                    (*(({{ name }} *)left)->glm) * (*(({{ right_name }} *)right)->glm)
                );
                return (PyObject *)result;
            }
        }
        {% endwith %}
        {% endwith %}
        {% endfor %}

        {
            auto row_cls = module_state->{{ row_type }}_PyTypeObject;
            auto column_cls = module_state->{{ column_type }}_PyTypeObject;
            if (Py_TYPE(right) == row_cls)
            {
                {{ column_type }} *result = ({{ column_type }} *)column_cls->tp_alloc(column_cls, 0);
                if (!result){ return 0; }
                result->glm = new {{ column_type }}Glm(
                    (*(({{ name }} *)left)->glm) * (*(({{ row_type }} *)right)->glm)
                );
                return (PyObject *)result;
            }
        }
    }
    else
    {
        auto row_cls = module_state->{{ row_type }}_PyTypeObject;
        auto column_cls = module_state->{{ column_type }}_PyTypeObject;
        if (Py_TYPE(left) == column_cls)
        {
            {{ row_type }} *result = ({{ row_type }} *)row_cls->tp_alloc(row_cls, 0);
            if (!result){ return 0; }
            result->glm = new {{ row_type }}Glm(
                (*(({{ column_type }} *)left)->glm) * (*(({{ name }} *)right)->glm)
            );
            return (PyObject *)result;
        }
    }

    Py_RETURN_NOTIMPLEMENTED;
}

static PyObject *
{{ name}}__truediv__(PyObject *left, PyObject *right)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->{{ name }}_PyTypeObject;

    {{ name }}Glm matrix;
    if (Py_TYPE(left) == cls)
    {
        {% if row_size == column_size %}
        if (Py_TYPE(right) == cls)
        {
            {{ name }} *result = ({{ name }} *)cls->tp_alloc(cls, 0);
            if (!result){ return 0; }
            result->glm = new {{ name }}Glm(
                (*(({{ name }} *)left)->glm) / (*(({{ name }} *)right)->glm)
            );
            return (PyObject *)result;
        }

        {
            auto row_cls = module_state->{{ row_type }}_PyTypeObject;
            if (Py_TYPE(right) == row_cls)
            {
                {{ row_type }} *result = ({{ row_type }} *)row_cls->tp_alloc(row_cls, 0);
                if (!result){ return 0; }
                result->glm = new {{ row_type }}Glm(
                    (*(({{ name }} *)left)->glm) / (*(({{ row_type }} *)right)->glm)
                );
                return (PyObject *)result;
            }
        }
        {% endif %}

        auto c_right = pyobject_to_c_{{ c_type.replace(' ', '_') }}(right);
        if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
        matrix = (*(({{ name }} *)left)->glm) / c_right;
    }
    else
    {
        {% if row_size == column_size %}
        {
            auto row_cls = module_state->{{ row_type }}_PyTypeObject;
            if (Py_TYPE(left) == row_cls)
            {
                {{ row_type }} *result = ({{ row_type }} *)row_cls->tp_alloc(row_cls, 0);
                if (!result){ return 0; }
                result->glm = new {{ row_type }}Glm(
                    (*(({{ row_type }} *)left)->glm) / (*(({{ name }} *)right)->glm)
                );
                return (PyObject *)result;
            }
        }
        {% endif %}

        auto c_left = pyobject_to_c_{{ c_type.replace(' ', '_') }}(left);
        if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
        matrix = c_left / (*(({{ name }} *)right)->glm);
    }

    {{ name }} *result = ({{ name }} *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new {{ name }}Glm(matrix);

    return (PyObject *)result;
}


static PyObject *
{{ name}}__neg__({{ name }} *self)
{
    auto cls = Py_TYPE(self);

    {{ name }} *result = ({{ name }} *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new {{ name }}Glm(-(*self->glm));

    return (PyObject *)result;
}


static int
{{ name}}_getbufferproc({{ name }} *self, Py_buffer *view, int flags)
{
    if (flags & PyBUF_WRITABLE)
    {
        PyErr_SetString(PyExc_TypeError, "{{ name }} is read only");
        view->obj = 0;
        return -1;
    }
    view->buf = glm::value_ptr(*self->glm);
    view->obj = (PyObject *)self;
    view->len = sizeof({{ c_type }}) * {{ component_count }};
    view->readonly = 1;
    view->itemsize = sizeof({{ c_type }});
    view->format = "{{ struct_format }}";
    view->ndim = 2;
    static Py_ssize_t shape[] = { {{ row_size }}, {{ column_size }} };
    view->shape = &shape[0];
    static Py_ssize_t strides[] = {
        sizeof({{ c_type }}) * {{ column_size }},
        sizeof({{ c_type }})
    };
    view->strides = &strides[0];
    view->suboffsets = 0;
    view->internal = 0;
    Py_INCREF(self);
    return 0;
}


static PyMemberDef {{ name }}_PyMemberDef[] = {
    {"__weaklistoffset__", T_PYSSIZET, offsetof({{ name }}, weakreflist), READONLY},
    {0}
};


{% if row_size == column_size %}
    static {{ name }} *
    {{ name }}_inverse({{ name }} *self, void*)
    {
        auto cls = Py_TYPE(self);
        auto matrix = glm::inverse(*self->glm);
        {{ name }} *result = ({{ name }} *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new {{ name }}Glm(matrix);
        return result;
    }
{% endif %}


{% with transpose_name=(('D' if c_type == 'double' else 'F') + 'Matrix' + str(column_size) + 'x' + str(row_size)) %}
static {{ transpose_name }} *
{{ name }}_transpose({{ name }} *self, void*)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->{{ transpose_name }}_PyTypeObject;

    {{ transpose_name }}Glm matrix = glm::transpose(*self->glm);
    {{ transpose_name }} *result = ({{ transpose_name }} *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new {{ transpose_name }}Glm(matrix);
    return result;
}
{% endwith %}


static PyObject *
{{ name }}_get_limits({{ name }} *self, void *)
{
    auto c_min = std::numeric_limits<{{ c_type }}>::lowest();
    auto c_max = std::numeric_limits<{{ c_type }}>::max();
    auto py_min = c_{{ c_type.replace(' ', '_') }}_to_pyobject(c_min);
    if (!py_min){ return 0; }
    auto py_max = c_{{ c_type.replace(' ', '_') }}_to_pyobject(c_max);
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


static PyMethodDef {{ name }}_PyMethodDef[] = {
    {% if row_size == column_size %}
        {"inverse", (PyCFunction){{ name }}_inverse, METH_NOARGS, 0},
    {% endif %}
    {"transpose", (PyCFunction){{ name }}_transpose, METH_NOARGS, 0},
    {"get_limits", (PyCFunction){{ name }}_get_limits, METH_NOARGS | METH_STATIC, 0},
    {0, 0, 0, 0}
};


static PyType_Slot {{ name }}_PyType_Slots [] = {
    {Py_tp_new, (void*){{ name }}__new__},
    {Py_tp_dealloc, (void*){{ name }}__dealloc__},
    {Py_tp_hash, (void*){{ name }}__hash__},
    {Py_tp_repr, (void*){{ name }}__repr__},
    {Py_sq_length, (void*){{ name }}__len__},
    {Py_sq_item, (void*){{ name }}__getitem__},
    {Py_tp_richcompare, (void*){{ name }}__richcmp__},
    {Py_nb_add, (void*){{ name }}__add__},
    {Py_nb_subtract, (void*){{ name }}__sub__},
    {Py_nb_multiply, (void*){{ name }}__mul__},
    {Py_nb_matrix_multiply, (void*){{ name }}__matmul__},
    {Py_nb_true_divide, (void*){{ name }}__truediv__},
    {Py_nb_negative, (void*){{ name }}__neg__},
    {Py_bf_getbuffer, (void*){{ name }}_getbufferproc},
    {Py_tp_members, (void*){{ name }}_PyMemberDef},
    {Py_tp_methods, (void*){{ name }}_PyMethodDef},
    {0, 0},
};


static PyType_Spec {{ name }}_PyTypeSpec = {
    "gamut.math.{{ name }}",
    sizeof({{ name }}),
    0,
    Py_TPFLAGS_DEFAULT,
    {{ name }}_PyType_Slots
};


static PyTypeObject *
define_{{ name }}_type(PyObject *module)
{
    PyTypeObject *type = (PyTypeObject *)PyType_FromModuleAndSpec(
        module,
        &{{ name }}_PyTypeSpec,
        0
    );
    if (!type){ return 0; }
    // Note:
    // Unlike other functions that steal references, PyModule_AddObject() only
    // decrements the reference count of value on success.
    if (PyModule_AddObject(module, "{{ name }}", (PyObject *)type) < 0)
    {
        Py_DECREF(type);
        return 0;
    }
    return type;
}

#endif
