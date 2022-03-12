
// generated {{ when }} from codegen/math/templates/test_api.cpp

// python
#define PY_SSIZE_T_CLEAN
#include <Python.h>
// gamut
#include "gamut/math.h"

#define TEST(X) if (!(X)){ PyErr_Format(PyExc_AssertionError, #X " (line %i)", __LINE__); return 0; };


static PyObject *
test_GamutMathApi_Get(PyObject *self, PyObject *args)
{
    struct GamutMathApi *api = GamutMathApi_Get();
    if (!api){ return 0; }
    TEST(!PyErr_Occurred());
    {% for type in vector_types + matrix_types + pod_types %}
        {% if type not in pod_types %}
            TEST(api->GamutMath{{ type }}_GetType != 0);
            TEST(api->GamutMath{{ type }}_Create != 0);
            TEST(api->GamutMath{{ type }}_GetValuePointer != 0);
        {% endif %}
        TEST(api->GamutMath{{ type }}Array_Create != 0);
        TEST(api->GamutMath{{ type }}Array_GetType != 0);
        TEST(api->GamutMath{{ type }}Array_GetValuePointer != 0);
        TEST(api->GamutMath{{ type }}Array_GetLength != 0);
    {% endfor %}
    Py_RETURN_NONE;
}


{% for type in vector_types %}
{% with component_count=int(type[-1]) %}
{% with c_type={
    "B": 'bool',
    "F": 'float',
    "D": 'double',
    "I": 'int',
    "I8": 'int8_t',
    "I16": 'int16_t',
    "I32": 'int32_t',
    "I64": 'int64_t',
    "U": 'unsigned int',
    "U8": 'uint8_t',
    "U16": 'uint16_t',
    "U32": 'uint32_t',
    "U64": 'uint64_t',
}[type[:type.find('V')]] %}
    static PyObject *
    test_{{ type }}(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMath{{ type }}_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            {{ c_type }} components[{{ component_count }}] = {
                {% for i in range(component_count) %}
                    {{ i }}{% if i != component_count - 1 %}, {% endif %}
                {% endfor %}
            };
            PyObject *obj = api->GamutMath{{ type }}_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            {{ c_type }} *value_ptr = api->GamutMath{{ type }}_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());
            {% for i in range(component_count) %}
                TEST(value_ptr[{{ i }}] == ({{ c_type }}){{ i }});
            {% endfor %}

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        {{ c_type }} *value_ptr = api->GamutMath{{ type }}_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }

    static PyObject *
    test_{{ type }}Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMath{{ type }}Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {{ c_type }} components[{{ component_count * 10 }}] = {
            {% for i in range(component_count * 10) %}
                {{ i }}{% if i != (component_count * 10) - 1 %}, {% endif %}
            {% endfor %}
        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMath{{ type }}Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMath{{ type }}Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            {{ c_type }} *value_ptr = api->GamutMath{{ type }}Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * {{ component_count }}; j++)
            {
                TEST(value_ptr[j] == ({{ c_type }})j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMath{{ type }}Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        {{ c_type }} *value_ptr = api->GamutMath{{ type }}Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }
{% endwith %}
{% endwith %}
{% endfor %}


{% for type in matrix_types %}
{% with row_size=int(type[-3]) %}
{% with column_size=int(type[-1]) %}
{% with component_count=row_size * column_size %}
{% with c_type={
    "B": 'bool',
    "F": 'float',
    "D": 'double',
    "I": 'int',
    "I8": 'int8_t',
    "I16": 'int16_t',
    "I32": 'int32_t',
    "I64": 'int64_t',
    "U": 'unsigned int',
    "U8": 'uint8_t',
    "U16": 'uint16_t',
    "U32": 'uint32_t',
    "U64": 'uint64_t',
}[type[:type.find('M')]] %}
    static PyObject *
    test_{{ type }}(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMath{{ type }}_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            {{ c_type }} components[{{ component_count }}] = {
                {% for i in range(component_count) %}
                    {{ i }}{% if i != component_count - 1 %}, {% endif %}
                {% endfor %}
            };
            PyObject *obj = api->GamutMath{{ type }}_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            {{ c_type }} *value_ptr = api->GamutMath{{ type }}_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());
            {% for i in range(component_count) %}
                TEST(value_ptr[{{ i }}] == ({{ c_type }}){{ i }});
            {% endfor %}

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        {{ c_type }} *value_ptr = api->GamutMath{{ type }}_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }

    static PyObject *
    test_{{ type }}Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMath{{ type }}Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {{ c_type }} components[{{ component_count * 10 }}] = {
            {% for i in range(component_count * 10) %}
                {{ i }}{% if i != (component_count * 10) - 1 %}, {% endif %}
            {% endfor %}
        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMath{{ type }}Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMath{{ type }}Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            {{ c_type }} *value_ptr = api->GamutMath{{ type }}Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * {{ component_count }}; j++)
            {
                TEST(value_ptr[j] == ({{ c_type }})j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMath{{ type }}Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        {{ c_type }} *value_ptr = api->GamutMath{{ type }}Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }
{% endwith %}
{% endwith %}
{% endwith %}
{% endwith %}
{% endfor %}


{% for type in pod_types %}
{% with c_type={
    "B": 'bool',
    "F": 'float',
    "D": 'double',
    "I": 'int',
    "I8": 'int8_t',
    "I16": 'int16_t',
    "I32": 'int32_t',
    "I64": 'int64_t',
    "U": 'unsigned int',
    "U8": 'uint8_t',
    "U16": 'uint16_t',
    "U32": 'uint32_t',
    "U64": 'uint64_t',
}[type] %}
    static PyObject *
    test_{{ type }}Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->GamutMath{{ type }}Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {{ c_type }} components[10] = {
            {% for i in range(10) %}
                {{ i }}{% if i != 9 %}, {% endif %}
            {% endfor %}
        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->GamutMath{{ type }}Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->GamutMath{{ type }}Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            {{ c_type }} *value_ptr = api->GamutMath{{ type }}Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i; j++)
            {
                TEST(value_ptr[j] == ({{ c_type }})j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->GamutMath{{ type }}Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        {{ c_type }} *value_ptr = api->GamutMath{{ type }}Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        Py_RETURN_NONE;
    }
{% endwith %}
{% endfor %}


static PyMethodDef module_methods[] = {
    {"test_GamutMathApi_Get", test_GamutMathApi_Get, METH_NOARGS, 0},
    {% for type in vector_types %}
        {"test_{{ type }}", test_{{ type }}, METH_NOARGS, 0},
        {"test_{{ type }}Array", test_{{ type }}Array, METH_NOARGS, 0},
    {% endfor %}
    {% for type in matrix_types %}
        {"test_{{ type }}", test_{{ type }}, METH_NOARGS, 0},
        {"test_{{ type }}Array", test_{{ type }}Array, METH_NOARGS, 0},
    {% endfor %}
    {% for type in pod_types %}
        {"test_{{ type }}Array", test_{{ type }}Array, METH_NOARGS, 0},
    {% endfor %}
    {0, 0, 0, 0}
};


static struct PyModuleDef module_PyModuleDef = {
    PyModuleDef_HEAD_INIT,
    "gamut.math._test_api",
    0,
    0,
    module_methods,
    0,
    0,
    0
};


PyMODINIT_FUNC
PyInit__test_api()
{
    return PyModule_Create(&module_PyModuleDef);
}
