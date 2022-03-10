
// generated {{ when }} from codegen/math/templates/_vector.hpp

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
#include "_type.hpp"


static PyObject *
{{ name }}__new__(PyTypeObject *cls, PyObject *args, PyObject *kwds)
{
    {% for i in range(component_count) %}
        {{ c_type }} c_{{ i }} = 0;
    {% endfor %}

    if (kwds && PyDict_Size(kwds) != 0)
    {
        PyErr_SetString(
            PyExc_TypeError,
            "{{ name }} does accept any keyword arguments"
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
            {{ c_type }} arg_c = pyobject_to_c_{{ c_type.replace(' ', '_') }}(arg);
            auto error_occurred = PyErr_Occurred();
            if (error_occurred){ return 0; }
            {% for i in range(component_count) %}
                c_{{ i }} = arg_c;
            {% endfor %}
            break;
        }
        case {{ component_count }}:
        {
            {% for i in range(component_count) %}
            {
                auto arg = PyTuple_GET_ITEM(args, {{ i }});
                c_{{ i }} = pyobject_to_c_{{ c_type.replace(' ', '_') }}(arg);
                auto error_occurred = PyErr_Occurred();
                if (error_occurred){ return 0; }
            }
            {% endfor %}
            break;
        }
        default:
        {
            PyErr_Format(
                PyExc_TypeError,
                "invalid number of arguments supplied to {{ name }}, expected "
                "0, 1 or {{ component_count }} (got %zd)",
                arg_count
            );
            return 0;
        }
    }

    {{ name }} *self = ({{ name }}*)cls->tp_alloc(cls, 0);
    if (!self){ return 0; }
    self->glm = new {{ name }}Glm(
        {% for i in range(component_count) %}
            c_{{ i }}{% if i != component_count - 1 %}, {% endif %}
        {% endfor %}
    );

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
    for ({{ name }}Glm::length_type i = 0; i < len; i++)
    {
        Py_uhash_t lane = std::hash<{{ c_type }}>{}((*self->glm)[i]);
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
{{ name }}__repr__({{ name }} *self)
{
    PyObject *result = 0;
    {% for i in range(component_count) %}
        PyObject *py_{{ i }} = 0;
    {% endfor %}

    {% for i in range(component_count) %}
        py_{{ i }} = c_{{ c_type.replace(' ', '_') }}_to_pyobject((*self->glm)[{{ i }}]);
        if (!py_{{ i }}){ goto cleanup; }
    {% endfor %}
    result = PyUnicode_FromFormat(
        "{{ name }}("
        {% for i in range(component_count) %}
            "%R{% if i < component_count - 1 %}, {% endif %}"
        {% endfor %}
        ")",
        {% for i in range(component_count) %}
            py_{{ i }}{% if i < component_count - 1 %}, {% endif %}
        {% endfor %}
    );
cleanup:
    {% for i in range(component_count) %}
        Py_XDECREF(py_{{ i }});
    {% endfor %}
    return result;
}


static Py_ssize_t
{{ name }}__len__({{ name }} *self)
{
    return {{ component_count }};
}


static PyObject *
{{ name }}__getitem__({{ name }} *self, Py_ssize_t index)
{
    if (index < 0 || index > {{ component_count - 1 }})
    {
        PyErr_Format(PyExc_IndexError, "index out of range");
        return 0;
    }
    auto c = (*self->glm)[({{ name }}Glm::length_type)index];
    return c_{{ c_type.replace(' ', '_') }}_to_pyobject(c);
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

    {{ name }}Glm vector;
    if (Py_TYPE(left) == Py_TYPE(right))
    {
        vector = (*(({{name }} *)left)->glm) + (*(({{name }} *)right)->glm);
    }
    else
    {
        if (Py_TYPE(left) == cls)
        {
            auto c_right = pyobject_to_c_{{ c_type.replace(' ', '_') }}(right);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
            vector = (*(({{name }} *)left)->glm) + c_right;
        }
        else
        {
            auto c_left = pyobject_to_c_{{ c_type.replace(' ', '_') }}(left);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
            vector = c_left + (*(({{name }} *)right)->glm);
        }
    }

    {{ name }} *result = ({{ name }} *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new {{ name }}Glm(
        {% for i in range(component_count) %}
            vector[{{ i }}]{% if i < component_count - 1 %}, {% endif %}
        {% endfor %}
    );

    return (PyObject *)result;
}


static PyObject *
{{ name}}__sub__(PyObject *left, PyObject *right)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->{{ name }}_PyTypeObject;

    {{ name }}Glm vector;
    if (Py_TYPE(left) == Py_TYPE(right))
    {
        vector = (*(({{name }} *)left)->glm) - (*(({{name }} *)right)->glm);
    }
    else
    {
        if (Py_TYPE(left) == cls)
        {
            auto c_right = pyobject_to_c_{{ c_type.replace(' ', '_') }}(right);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
            vector = (*(({{name }} *)left)->glm) - c_right;
        }
        else
        {
            auto c_left = pyobject_to_c_{{ c_type.replace(' ', '_') }}(left);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
            vector = c_left - (*(({{name }} *)right)->glm);
        }
    }

    {{ name }} *result = ({{ name }} *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new {{ name }}Glm(
        {% for i in range(component_count) %}
            vector[{{ i }}]{% if i < component_count - 1 %}, {% endif %}
        {% endfor %}
    );

    return (PyObject *)result;
}


static PyObject *
{{ name}}__mul__(PyObject *left, PyObject *right)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->{{ name }}_PyTypeObject;

    {{ name }}Glm vector;
    if (Py_TYPE(left) == Py_TYPE(right))
    {
        vector = (*(({{name }} *)left)->glm) * (*(({{name }} *)right)->glm);
    }
    else
    {
        if (Py_TYPE(left) == cls)
        {
            auto c_right = pyobject_to_c_{{ c_type.replace(' ', '_') }}(right);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
            vector = (*(({{name }} *)left)->glm) * c_right;
        }
        else
        {
            auto c_left = pyobject_to_c_{{ c_type.replace(' ', '_') }}(left);
            if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
            vector = c_left * (*(({{name }} *)right)->glm);
        }
    }

    {{ name }} *result = ({{ name }} *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new {{ name }}Glm(
        {% for i in range(component_count) %}
            vector[{{ i }}]{% if i < component_count - 1 %}, {% endif %}
        {% endfor %}
    );

    return (PyObject *)result;
}


{% if c_type in ['float', 'double'] %}
    static PyObject *
    {{ name }}__matmul__({{ name }} *left, {{ name }} *right)
    {
        auto cls = Py_TYPE(left);
        if (Py_TYPE(left) != Py_TYPE(right)){ Py_RETURN_NOTIMPLEMENTED; }
        auto c_result = glm::dot(*left->glm, *right->glm);
        return c_{{ c_type.replace(' ', '_') }}_to_pyobject(c_result);
    }


    static PyObject *
    {{ name}}__mod__(PyObject *left, PyObject *right)
    {
        auto module_state = get_module_state();
        if (!module_state){ return 0; }
        auto cls = module_state->{{ name }}_PyTypeObject;

        {{ name }}Glm vector;
        if (Py_TYPE(left) == Py_TYPE(right))
        {
            vector = glm::mod(
                *(({{name }} *)left)->glm,
                *(({{name }} *)right)->glm
            );
        }
        else
        {
            if (Py_TYPE(left) == cls)
            {
                auto c_right = pyobject_to_c_{{ c_type.replace(' ', '_') }}(right);
                if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
                vector = glm::mod(*(({{name }} *)left)->glm, c_right);
            }
            else
            {
                auto c_left = pyobject_to_c_{{ c_type.replace(' ', '_') }}(left);
                if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
                vector = glm::mod({{ name }}Glm(c_left), *(({{name }} *)right)->glm);
            }
        }

        {{ name }} *result = ({{ name }} *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new {{ name }}Glm(
            {% for i in range(component_count) %}
                vector[{{ i }}]{% if i < component_count - 1 %}, {% endif %}
            {% endfor %}
        );

        return (PyObject *)result;
    }


    static PyObject *
    {{ name}}__pow__(PyObject *left, PyObject *right)
    {
        auto module_state = get_module_state();
        if (!module_state){ return 0; }
        auto cls = module_state->{{ name }}_PyTypeObject;

        {{ name }}Glm vector;
        if (Py_TYPE(left) == Py_TYPE(right))
        {
            vector = glm::pow(
                *(({{name }} *)left)->glm,
                *(({{name }} *)right)->glm
            );
        }
        else
        {
            if (Py_TYPE(left) == cls)
            {
                auto c_right = pyobject_to_c_{{ c_type.replace(' ', '_') }}(right);
                if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
                vector = glm::pow(*(({{name }} *)left)->glm, {{ name }}Glm(c_right));
            }
            else
            {
                auto c_left = pyobject_to_c_{{ c_type.replace(' ', '_') }}(left);
                if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
                vector = glm::pow({{ name }}Glm(c_left), *(({{name }} *)right)->glm);
            }
        }

        {{ name }} *result = ({{ name }} *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new {{ name }}Glm(
            {% for i in range(component_count) %}
                vector[{{ i }}]{% if i < component_count - 1 %}, {% endif %}
            {% endfor %}
        );

        return (PyObject *)result;
    }
{% endif %}


{% if c_type != 'bool' %}

    static PyObject *
    {{ name}}__truediv__(PyObject *left, PyObject *right)
    {
        auto module_state = get_module_state();
        if (!module_state){ return 0; }
        auto cls = module_state->{{ name }}_PyTypeObject;

        {{ name }}Glm vector;
        if (Py_TYPE(left) == Py_TYPE(right))
        {
            {% if c_type not in ['float', 'double'] %}
                if (
                    {% for i in range(component_count) %}
                        (*(({{name }} *)right)->glm)[{{ i }}] == 0{% if i < component_count - 1 %} || {% endif %}
                    {% endfor %}
                )
                {
                    PyErr_SetString(PyExc_ZeroDivisionError, "divide by zero");
                    return 0;
                }
            {% endif %}
            vector = (*(({{name }} *)left)->glm) / (*(({{name }} *)right)->glm);
        }
        else
        {
            if (Py_TYPE(left) == cls)
            {
                auto c_right = pyobject_to_c_{{ c_type.replace(' ', '_') }}(right);
                if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
                {% if c_type not in ['float', 'double'] %}
                    if (c_right == 0)
                    {
                        PyErr_SetString(PyExc_ZeroDivisionError, "divide by zero");
                        return 0;
                    }
                {% endif %}
                vector = (*(({{name }} *)left)->glm) / c_right;
            }
            else
            {
                auto c_left = pyobject_to_c_{{ c_type.replace(' ', '_') }}(left);
                if (PyErr_Occurred()){ PyErr_Clear(); Py_RETURN_NOTIMPLEMENTED; }
                {% if c_type not in ['float', 'double'] %}
                    if (
                        {% for i in range(component_count) %}
                            (*(({{name }} *)right)->glm)[{{ i }}] == 0{% if i < component_count - 1 %} || {% endif %}
                        {% endfor %}
                    )
                    {
                        PyErr_SetString(PyExc_ZeroDivisionError, "divide by zero");
                        return 0;
                    }
                {% endif %}
                vector = c_left / (*(({{name }} *)right)->glm);
            }
        }

        {{ name }} *result = ({{ name }} *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new {{ name }}Glm(
            {% for i in range(component_count) %}
                vector[{{ i }}]{% if i < component_count - 1 %}, {% endif %}
            {% endfor %}
        );

        return (PyObject *)result;
    }
{% endif %}


{% if 'unsigned' not in c_type and not (c_type.startswith('u') and c_type.endswith('_t')) %}
    static PyObject *
    {{ name}}__neg__({{ name }} *self)
    {
        auto cls = Py_TYPE(self);
        {% if c_type == 'bool' %}
            {{ name }}Glm vector = (*self->glm);
        {% else %}
            {{ name }}Glm vector = -(*self->glm);
        {% endif %}

        {{ name }} *result = ({{ name }} *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new {{ name }}Glm(
            {% for i in range(component_count) %}
                vector[{{ i }}]{% if i < component_count - 1 %}, {% endif %}
            {% endfor %}
        );

        return (PyObject *)result;
    }
{% endif %}


static PyObject *
{{ name}}__abs__({{ name }} *self)
{
    auto cls = Py_TYPE(self);
    {{ name }}Glm vector = glm::abs(*self->glm);

    {{ name }} *result = ({{ name }} *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new {{ name }}Glm(
        {% for i in range(component_count) %}
            vector[{{ i }}]{% if i < component_count - 1 %}, {% endif %}
        {% endfor %}
    );

    return (PyObject *)result;
}


static int
{{ name}}__bool__({{ name }} *self)
{
    {% for i in range(component_count) %}
        if ((*self->glm)[{{ i }}] == 0)
        {
            return 0;
        }
    {% endfor %}
    return 1;
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
    view->ndim = 1;
    static Py_ssize_t shape = {{ component_count }};
    view->shape = &shape;
    view->strides = &view->itemsize;
    view->suboffsets = 0;
    view->internal = 0;
    Py_INCREF(self);
    return 0;
}


{% for i in range(component_count) %}
    static PyObject *
    {{ name }}_Getter_{{ i }}({{ name }} *self, void *)
    {
        auto c = (*self->glm)[{{ i }}];
        return c_{{ c_type.replace(' ', '_') }}_to_pyobject(c);
    }
{% endfor %}


{% if c_type in ['float', 'double'] %}
    static PyObject *
    {{ name }}_magnitude({{ name }} *self, void *)
    {
        auto magnitude = glm::length(*self->glm);
        return c_{{ c_type.replace(' ', '_') }}_to_pyobject(magnitude);
    }
{% endif %}


static PyGetSetDef {{ name }}_PyGetSetDef[] = {
    {"x", (getter){{ name }}_Getter_0, 0, 0, 0},
    {"r", (getter){{ name }}_Getter_0, 0, 0, 0},
    {"s", (getter){{ name }}_Getter_0, 0, 0, 0},
    {"u", (getter){{ name }}_Getter_0, 0, 0, 0},
    {% if component_count > 1 %}
        {"y", (getter){{ name }}_Getter_1, 0, 0, 0},
        {"g", (getter){{ name }}_Getter_1, 0, 0, 0},
        {"t", (getter){{ name }}_Getter_1, 0, 0, 0},
        {"v", (getter){{ name }}_Getter_1, 0, 0, 0},
    {% endif %}
    {% if component_count > 2 %}
        {"z", (getter){{ name }}_Getter_2, 0, 0, 0},
        {"b", (getter){{ name }}_Getter_2, 0, 0, 0},
        {"p", (getter){{ name }}_Getter_2, 0, 0, 0},
    {% endif %}
    {% if component_count > 3 %}
        {"w", (getter){{ name }}_Getter_3, 0, 0, 0},
        {"a", (getter){{ name }}_Getter_3, 0, 0, 0},
        {"q", (getter){{ name }}_Getter_3, 0, 0, 0},
    {% endif %}
    {% if c_type in ['float', 'double'] %}
        {"magnitude", (getter){{ name }}_magnitude, 0, 0, 0},
    {% endif %}
    {0, 0, 0, 0, 0}
};

{% for swizzle_count in range(2, 5) %}
{% with result_type=name[:name.index('V')] + 'Vector' + str(swizzle_count) %}
    static PyObject *
    swizzle_{{ swizzle_count }}_{{ name }}({{name}} *self, PyObject *py_attr)
    {
        const char *attr = PyUnicode_AsUTF8(py_attr);
        if (!attr){ return 0; }

        {{ result_type }}Glm vec;
        for (int i = 0; i < {{ swizzle_count }}; i++)
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
                {% if component_count > 1 %}
                    case 'y':
                    case 'g':
                    case 't':
                    case 'v':
                        glm_index = 1;
                        break;
                {% endif %}
                {% if component_count > 2 %}
                    case 'z':
                    case 'b':
                    case 'p':
                        glm_index = 2;
                        break;
                {% endif %}
                {% if component_count > 3 %}
                    case 'w':
                    case 'a':
                    case 'q':
                        glm_index = 3;
                        break;
                {% endif %}
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
        auto cls = module_state->{{ result_type }}_PyTypeObject;

        {{ result_type }} *result = ({{ result_type }} *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new {{ result_type }}Glm(vec);

        return (PyObject *)result;
    }
{% endwith %}
{% endfor %}


static PyObject *
{{ name }}__getattr__({{name}} *self, PyObject *py_attr)
{
    PyObject *result = PyObject_GenericGetAttr((PyObject *)self, py_attr);
    if (result != 0){ return result; }

    auto attr_length = PyUnicode_GET_LENGTH(py_attr);
    switch(attr_length)
    {
        case 2:
        {
            PyErr_Clear();
            return swizzle_2_{{ name }}(self, py_attr);
        }
        case 3:
        {
            PyErr_Clear();
            return swizzle_3_{{ name }}(self, py_attr);
        }
        case 4:
        {
            PyErr_Clear();
            return swizzle_4_{{ name }}(self, py_attr);
        }
    }
    return 0;
}


static PyMemberDef {{ name }}_PyMemberDef[] = {
    {"__weaklistoffset__", T_PYSSIZET, offsetof({{ name }}, weakreflist), READONLY},
    {0}
};


{% if c_type in ['float', 'double'] %}
    {% if component_count == 3 %}
        static {{ name }} *
        {{ name }}_cross({{ name }} *self, {{ name }} *other)
        {
            auto cls = Py_TYPE(self);
            if (Py_TYPE(other) != cls)
            {
                PyErr_Format(PyExc_TypeError, "%R is not {{ name }}", other);
                return 0;
            }
            auto vector = glm::cross(*self->glm, *other->glm);
            {{ name }} *result = ({{ name }} *)cls->tp_alloc(cls, 0);
            if (!result){ return 0; }
            result->glm = new {{ name }}Glm(
                {% for i in range(component_count) %}
                    vector[{{ i }}]{% if i < component_count - 1 %}, {% endif %}
                {% endfor %}
            );
            return result;
        }
    {% endif %}

    static {{ name }} *
    {{ name }}_normalize({{ name }} *self, void*)
    {
        auto cls = Py_TYPE(self);
        auto vector = glm::normalize(*self->glm);
        {{ name }} *result = ({{ name }} *)cls->tp_alloc(cls, 0);
        if (!result){ return 0; }
        result->glm = new {{ name }}Glm(
            {% for i in range(component_count) %}
                vector[{{ i }}]{% if i < component_count - 1 %}, {% endif %}
            {% endfor %}
        );
        return result;
    }


    static PyObject *
    {{ name }}_distance({{ name }} *self, {{ name }} *other)
    {
        auto cls = Py_TYPE(self);
        if (Py_TYPE(other) != cls)
        {
            PyErr_Format(PyExc_TypeError, "%R is not {{ name }}", other);
            return 0;
        }
        auto result = glm::distance(*self->glm, *other->glm);
        return c_{{ c_type.replace(' ', '_') }}_to_pyobject(result);
    }
{% endif %}


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
    {% if c_type in ['float', 'double'] %}
        {% if component_count == 3 %}
            {"cross", (PyCFunction){{ name }}_cross, METH_O, 0},
        {% endif %}
        {"normalize", (PyCFunction){{ name }}_normalize, METH_NOARGS, 0},
        {"distance", (PyCFunction){{ name }}_distance, METH_O, 0},
    {% endif %}
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


static {{ name }} *
create_{{ name }}_from_glm(const {{ name }}Glm& glm)
{
    auto module_state = get_module_state();
    if (!module_state){ return 0; }
    auto cls = module_state->{{ name }}_PyTypeObject;

    {{ name }} *result = ({{ name }} *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new {{ name }}Glm(glm);

    return result;
}

#endif
