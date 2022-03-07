// generated {{ when }}

#include <stdio.h>
#include <iostream>

// python
#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <structmember.h>
// glm
#include <glm/glm.hpp>
#include <glm/ext.hpp>
#include <glm/detail/type_vec3.hpp>
// gamut
#include "_type.hpp"

typedef glm::vec<{{ component_count }}, {{ c_type }}, glm::defaultp> {{ name }}Glm;


struct {{ name }}
{
    PyObject_HEAD
    PyObject *weakreflist;
    {{ name }}Glm *glm;
};


static PyObject *
{{ name }}__new__(PyTypeObject *cls, PyObject *args, PyObject *kwds)
{
    {% for i in range(component_count) %}
        {{ c_type }} c_{{i}} = 0;
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
            {{ c_type }} arg_c = pyobject_to_c_{{ c_type }}(arg);
            auto error_occurred = PyErr_Occurred();
            if (error_occurred){ return 0; }
            {% for i in range(component_count) %}
                c_{{i}} = arg_c;
            {% endfor %}
            break;
        }
        case {{ component_count }}:
        {
            {% for i in range(component_count) %}
            {
                auto arg = PyTuple_GET_ITEM(args, {{i}});
                c_{{i}} = pyobject_to_c_{{ c_type }}(arg);
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
            c_{{i}}{% if i != component_count - 1 %}, {% endif %}
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


static Py_hash_t
{{ name }}__hash__({{ name }} *self)
{
    Py_hash_t hash = 0;
    {% for i in range(component_count) %}
        hash ^= (Py_hash_t)(*self->glm)[{{i}}];
    {% endfor %}
    if (hash == -1){ hash = -123456789; }
    return hash;
}


static PyObject *
{{ name }}__repr__({{ name }} *self)
{
    PyObject *result = 0;
    {% for i in range(component_count) %}
        PyObject *py_{{i}} = 0;
    {% endfor %}

    {% for i in range(component_count) %}
        py_{{i}} = c_{{ c_type }}_to_pyobject((*self->glm)[{{i}}]);
        if (!py_{{i}}){ goto cleanup; }
    {% endfor %}
    result = PyUnicode_FromFormat(
        "{{ name }}("
        {% for i in range(component_count) %}
            "%R{% if i < component_count - 1 %}, {% endif %}"
        {% endfor %}
        ")",
        {% for i in range(component_count) %}
            py_{{i}}{% if i < component_count - 1 %}, {% endif %}
        {% endfor %}
    );
cleanup:
    {% for i in range(component_count) %}
        Py_XDECREF(py_{{i}});
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
    auto c = (*self->glm)[index];
    return c_{{ c_type }}_to_pyobject(c);
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
{{ name}}__add__({{ name }} *self, PyObject *other)
{
    auto cls = Py_TYPE(self);
    {{ name }}Glm vector;
    if (Py_TYPE(other) != cls)
    {
        auto c_other = pyobject_to_c_{{ c_type }}(other);
        if (PyErr_Occurred()){ Py_RETURN_NOTIMPLEMENTED; }
        vector = (*self->glm) + c_other;
    }
    else
    {
        vector = (*self->glm) + (*(({{name }} *)other)->glm);
    }

    {{ name }} *result = ({{ name }} *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new {{ name }}Glm(
        {% for i in range(component_count) %}
            vector[{{i}}]{% if i < component_count - 1 %}, {% endif %}
        {% endfor %}
    );

    return (PyObject *)result;
}


static PyObject *
{{ name}}__sub__({{ name }} *self, PyObject *other)
{
    auto cls = Py_TYPE(self);
    {{ name }}Glm vector;
    if (Py_TYPE(other) != cls)
    {
        auto c_other = pyobject_to_c_{{ c_type }}(other);
        if (PyErr_Occurred()){ Py_RETURN_NOTIMPLEMENTED; }
        vector = (*self->glm) - c_other;
    }
    else
    {
        vector = (*self->glm) - (*(({{name }} *)other)->glm);
    }

    {{ name }} *result = ({{ name }} *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new {{ name }}Glm(
        {% for i in range(component_count) %}
            vector[{{i}}]{% if i < component_count - 1 %}, {% endif %}
        {% endfor %}
    );

    return (PyObject *)result;
}


static PyObject *
{{ name}}__mul__({{ name }} *self, PyObject *other)
{
    auto cls = Py_TYPE(self);
    {{ name }}Glm vector;
    if (Py_TYPE(other) != cls)
    {
        auto c_other = pyobject_to_c_{{ c_type }}(other);
        if (PyErr_Occurred()){ Py_RETURN_NOTIMPLEMENTED; }
        vector = (*self->glm) * c_other;
    }
    else
    {
        vector = (*self->glm) * (*(({{name }} *)other)->glm);
    }

    {{ name }} *result = ({{ name }} *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new {{ name }}Glm(
        {% for i in range(component_count) %}
            vector[{{i}}]{% if i < component_count - 1 %}, {% endif %}
        {% endfor %}
    );

    return (PyObject *)result;
}


static PyObject *
{{ name }}__matmul__({{ name }} *self, {{ name }} *other)
{
    auto cls = Py_TYPE(self);
    if (Py_TYPE(other) != cls){ Py_RETURN_NOTIMPLEMENTED; }
    auto c_result = glm::dot(*self->glm, *other->glm);
    return c_{{ c_type }}_to_pyobject(c_result);
}


static PyObject *
{{ name}}__truediv__({{ name }} *self, PyObject *other)
{
    auto cls = Py_TYPE(self);
    {{ name }}Glm vector;
    if (Py_TYPE(other) != cls)
    {
        auto c_other = pyobject_to_c_{{ c_type }}(other);
        if (PyErr_Occurred()){ Py_RETURN_NOTIMPLEMENTED; }
        vector = (*self->glm) / c_other;
    }
    else
    {
        vector = (*self->glm) / (*(({{name }} *)other)->glm);
    }

    {{ name }} *result = ({{ name }} *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new {{ name }}Glm(
        {% for i in range(component_count) %}
            vector[{{i}}]{% if i < component_count - 1 %}, {% endif %}
        {% endfor %}
    );

    return (PyObject *)result;
}


static PyObject *
{{ name}}__mod__({{ name }} *self, PyObject *other)
{
    auto cls = Py_TYPE(self);
    {{ name }}Glm vector;
    if (Py_TYPE(other) != cls)
    {
        auto c_other = pyobject_to_c_{{ c_type }}(other);
        if (PyErr_Occurred()){ Py_RETURN_NOTIMPLEMENTED; }
        vector = glm::mod((*self->glm), c_other);
    }
    else
    {
        vector = glm::mod((*self->glm), (*(({{name }} *)other)->glm));
    }

    {{ name }} *result = ({{ name }} *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new {{ name }}Glm(
        {% for i in range(component_count) %}
            vector[{{i}}]{% if i < component_count - 1 %}, {% endif %}
        {% endfor %}
    );

    return (PyObject *)result;
}


static PyObject *
{{ name}}__pow__({{ name }} *self, PyObject *other)
{
    auto cls = Py_TYPE(self);
    {{ name }}Glm vector;
    if (Py_TYPE(other) != cls)
    {
        auto c_other = pyobject_to_c_{{ c_type }}(other);
        if (PyErr_Occurred()){ Py_RETURN_NOTIMPLEMENTED; }
        vector = glm::pow((*self->glm), {{ name }}Glm(c_other));
    }
    else
    {
        vector = glm::pow((*self->glm), (*(({{name }} *)other)->glm));
    }

    {{ name }} *result = ({{ name }} *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new {{ name }}Glm(
        {% for i in range(component_count) %}
            vector[{{i}}]{% if i < component_count - 1 %}, {% endif %}
        {% endfor %}
    );

    return (PyObject *)result;
}


static PyObject *
{{ name}}__neg__({{ name }} *self)
{
    auto cls = Py_TYPE(self);
    {{ name }}Glm vector = -(*self->glm);

    {{ name }} *result = ({{ name }} *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new {{ name }}Glm(
        {% for i in range(component_count) %}
            vector[{{i}}]{% if i < component_count - 1 %}, {% endif %}
        {% endfor %}
    );

    return (PyObject *)result;
}


static PyObject *
{{ name}}__abs__({{ name }} *self)
{
    auto cls = Py_TYPE(self);
    {{ name }}Glm vector = glm::abs(*self->glm);

    {{ name }} *result = ({{ name }} *)cls->tp_alloc(cls, 0);
    if (!result){ return 0; }
    result->glm = new {{ name }}Glm(
        {% for i in range(component_count) %}
            vector[{{i}}]{% if i < component_count - 1 %}, {% endif %}
        {% endfor %}
    );

    return (PyObject *)result;
}


static int
{{ name}}__bool__({{ name }} *self)
{
    {% for i in range(component_count) %}
        if ((*self->glm)[{{i}}] == 0)
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
        PyErr_SetString(PyExc_TypeError, "{{ name }} is not read only");
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
    {{ name }}_Getter_{{i}}({{ name }} *self, void *)
    {
        auto c = (*self->glm)[{{i}}];
        return c_{{ c_type }}_to_pyobject(c);
    }
{% endfor %}


static PyObject *
{{ name }}_magnitude({{ name }} *self, void *)
{
    auto magnitude = glm::length(*self->glm);
    return c_{{ c_type }}_to_pyobject(magnitude);
}


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
    {"magnitude", (getter){{ name }}_magnitude, 0, 0, 0},
    {0, 0, 0, 0, 0}
};


static PyObject *
{{ name }}__getattr__({{name}} *self, PyObject *py_attr)
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
                Py_DECREF(result);
                return 0;
            }
        }
        auto py_c = c_{{ c_type }}_to_pyobject((*self->glm)[glm_index]);
        PyTuple_SET_ITEM(result, i, py_c);
    }

    PyErr_Clear();
    return result;
}


static PyMemberDef {{ name }}_PyMemberDef[] = {
    {"__weaklistoffset__", T_PYSSIZET, offsetof({{ name }}, weakreflist), READONLY},
    {0}
};


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
                vector[{{i}}]{% if i < component_count - 1 %}, {% endif %}
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
            vector[{{i}}]{% if i < component_count - 1 %}, {% endif %}
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
    return c_{{ c_type }}_to_pyobject(result);
}


static PyMethodDef {{ name }}_PyMethodDef[] = {
    {% if component_count == 3 %}
        {"cross", (PyCFunction){{ name }}_cross, METH_O, 0},
    {% endif %}
    {"normalize", (PyCFunction){{ name }}_normalize, METH_NOARGS, 0},
    {"distance", (PyCFunction){{ name }}_distance, METH_O, 0},
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
    {Py_nb_remainder, (void*){{ name }}__mod__},
    {Py_nb_power, (void*){{ name }}__pow__},
    {Py_nb_negative, (void*){{ name }}__neg__},
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
