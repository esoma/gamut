
// python
#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <structmember.h>
// glm
#include <glm/detail/type_vec3.hpp>
#include <stdio.h>
// gamut
#include "_type.hpp"

typedef glm::vec<{{ component_count }}, {{ c_type }}, glm::defaultp> {{ name }}Glm;


struct {{ name }}
{
    PyObject_HEAD
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
            Py_DECREF(arg);
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
                Py_DECREF(arg);
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
    delete self->glm;

    PyTypeObject *type = Py_TYPE(self);
    type->tp_free(self);
    Py_DECREF(type);
}


static Py_ssize_t
{{ name }}__len__({{ name }} *self)
{
    return {{ component_count }};
}


static PyObject *
{{ name }}__getitem__({{ name }} *self, Py_ssize_t index)
{
    if (index < {{ -component_count }} || index > {{ component_count - 1 }})
    {
        PyErr_Format(PyExc_IndexError, "invalid index %zd", index);
        return 0;
    }
    if (index < 0)
    {
        index = {{ component_count }} - index;
    }

    auto c = (*self->glm)[index];
    return c_{{ c_type }}_to_pyobject(c);
}


{% for i in range(component_count) %}
    static PyObject *
    {{ name }}_Getter_{{i}}({{ name }} *self, void *)
    {
        auto c = (*self->glm)[{{i}}];
        return c_{{ c_type }}_to_pyobject(c);
    }
{% endfor %}


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
    {0, 0, 0, 0, 0}
};


static PyType_Slot {{ name }}_PyType_Slots [] = {
    {Py_tp_new, (void*){{ name }}__new__},
    {Py_tp_dealloc, (void*){{ name }}__dealloc__},
    {Py_sq_length, (void*){{ name }}__len__},
    {Py_sq_item, (void*){{ name }}__getitem__},
    {Py_tp_getset, (void*){{ name }}_PyGetSetDef},
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
