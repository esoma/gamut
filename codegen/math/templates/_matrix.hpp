
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
#include "_type.hpp"
#include "_{{ column_type.lower() }}.hpp"

typedef glm::tmat{{ column_count }}x{{ row_count }}<{{ c_type }}, glm::defaultp> {{ name }}Glm;


struct {{ name }}
{
    PyObject_HEAD
    PyObject *weakreflist;
    {{ name }}Glm *glm;
};


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
        case {{ column_count }}:
        {
            auto module_state = get_module_state();
            if (!module_state){ return 0; }
            auto column_cls = module_state->{{ column_type }}_PyTypeObject;
            {% for i in range(column_count) %}
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
                {% for i in range(column_count) %}
                    *(({{ column_type }} *)p_{{ i }})->glm{% if i != column_count - 1 %}, {% endif %}
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
                "0, 1, {{ column_count }} or {{ component_count }} (got %zd)",
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
    for (size_t c = 0; c < {{ column_count }}; c++)
    {
        for (size_t r = 0; r < {{ row_count }}; r++)
        {
            Py_uhash_t lane = std::hash<{{ c_type }}>{}((*self->glm)[c][r]);
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
    {% for c in range(column_count) %}
    {% for r in range(row_count) %}
        PyObject *py_{{ c }}_{{ r }} = 0;
    {% endfor %}
    {% endfor %}

    {% for c in range(column_count) %}
    {% for r in range(row_count) %}
        py_{{ c }}_{{ r }} = c_{{ c_type.replace(' ', '_') }}_to_pyobject((*self->glm)[{{ c }}][{{ r }}]);
        if (!py_{{ c }}_{{ r }}){ goto cleanup; }
    {% endfor %}
    {% endfor %}

    result = PyUnicode_FromFormat(
        "{{ name }}("
        {% for c in range(column_count) %}
        "("
        {% for r in range(row_count) %}
            "%R"
            {% if r != row_count - 1 %}", "{% endif %}
        {% endfor %}
        ")"
        {% if c != column_count - 1 %}
        ", "
        {% endif %}
        {% endfor %}
        ")",
        {% for c in range(column_count) %}
        {% for r in range(row_count) %}
            py_{{ c }}_{{ r }}
            {% if c == column_count - 1 and r == row_count - 1 %}{% else %}, {% endif %}
        {% endfor %}
        {% endfor %}
    );
cleanup:
    {% for c in range(column_count) %}
    {% for r in range(row_count) %}
        Py_XDECREF(py_{{ c }}_{{ r }});
    {% endfor %}
    {% endfor %}
    return result;
}


static Py_ssize_t
{{ name }}__len__({{ name }} *self)
{
    return {{ column_count }};
}


static PyObject *
{{ name }}__getitem__({{ name }} *self, Py_ssize_t index)
{
    if (index < 0 || index > {{ column_count - 1 }})
    {
        PyErr_Format(PyExc_IndexError, "index out of range");
        return 0;
    }
    const auto& v = (*self->glm)[index];
    return (PyObject *)create_{{ column_type }}_from_glm(v);
}


static PyType_Slot {{ name }}_PyType_Slots [] = {
    {Py_tp_new, (void*){{ name }}__new__},
    {Py_tp_dealloc, (void*){{ name }}__dealloc__},
    {Py_tp_hash, (void*){{ name }}__hash__},
    {Py_tp_repr, (void*){{ name }}__repr__},
    {Py_sq_length, (void*){{ name }}__len__},
    {Py_sq_item, (void*){{ name }}__getitem__},
    /*{Py_tp_richcompare, (void*){{ name }}__richcmp__},
    {Py_nb_add, (void*){{ name }}__add__},
    {Py_nb_subtract, (void*){{ name }}__sub__},
    {Py_nb_multiply, (void*){{ name }}__mul__},
    {% if c_type in ['float', 'double'] %}
        {Py_nb_matrix_multiply, (void*){{ name }}__matmul__},
        {Py_nb_remainder, (void*){{ name }}__mod__},
        {Py_nb_power, (void*){{ name }}__pow__},
    {% endif %}
    {% if c_type != 'bool' %}
        {Py_nb_true_divide, (void*){{ name }}__truediv__},
    {% endif %}
    {% if 'unsigned' not in c_type and not (c_type.startswith('u') and c_type.endswith('_t')) %}
        {Py_nb_negative, (void*){{ name }}__neg__},
    {% endif %}
    {Py_nb_absolute, (void*){{ name }}__abs__},
    {Py_nb_bool, (void*){{ name }}__bool__},
    {Py_bf_getbuffer, (void*){{ name }}_getbufferproc},
    {Py_tp_getset, (void*){{ name }}_PyGetSetDef},
    {Py_tp_getattro, (void*){{ name }}__getattr__},
    {Py_tp_members, (void*){{ name }}_PyMemberDef},
    {Py_tp_methods, (void*){{ name }}_PyMethodDef},
    */
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
