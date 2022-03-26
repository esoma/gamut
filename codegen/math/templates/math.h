
// generated {{ when }} from codegen/math/templates/math.h

#ifndef GAMUT_MATH_API_HPP
#define GAMUT_MATH_API_HPP

// stdlib
#include <stdbool.h>
// python
#define PY_SSIZE_T_CLEAN
#include <Python.h>

#ifdef __cplusplus
extern "C" {
#endif

typedef PyTypeObject *(*GamutMathApi_GetType)();
typedef size_t (*GamutMathApi_GetArrayLength)(const PyObject *);

{% for type in vector_types %}
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
    typedef PyObject *(*GamutMathApi_Create{{ type }})(const {{ c_type }} *);
    typedef PyObject *(*GamutMathApi_Create{{ type }}Array)(size_t, const {{ c_type }} *);
    typedef {{ c_type }} *(*GamutMathApi_Get{{ type }}ValuePointer)(const PyObject *);
{% endwith %}
{% endfor %}

{% for type in matrix_types %}
{% with c_type={
    "F": 'float',
    "D": 'double',
}[type[:type.find('M')]] %}
    typedef PyObject *(*GamutMathApi_Create{{ type }})(const {{ c_type }} *);
    typedef PyObject *(*GamutMathApi_Create{{ type }}Array)(size_t, const {{ c_type }} *);
    typedef {{ c_type }} *(*GamutMathApi_Get{{ type }}ValuePointer)(const PyObject *);
{% endwith %}
{% endfor %}

{% for type in quaternion_types %}
{% with c_type={
    "F": 'float',
    "D": 'double',
}[type[:type.find('Q')]] %}
    typedef PyObject *(*GamutMathApi_Create{{ type }})(const {{ c_type }} *);
    typedef PyObject *(*GamutMathApi_Create{{ type }}Array)(size_t, const {{ c_type }} *);
    typedef {{ c_type }} *(*GamutMathApi_Get{{ type }}ValuePointer)(const PyObject *);
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
    typedef PyObject *(*GamutMathApi_Create{{ type }}Array)(size_t, const {{ c_type }} *);
    typedef {{ c_type }} *(*GamutMathApi_Get{{ type }}ValuePointer)(const PyObject *);
{% endwith %}
{% endfor %}


struct GamutMathApi
{
    const size_t version;
    {% for type in vector_types %}
        GamutMathApi_GetType {{ type }}_GetType;
        GamutMathApi_GetType {{ type }}Array_GetType;
        GamutMathApi_Create{{ type }} {{ type }}_Create;
        GamutMathApi_Create{{ type }}Array {{ type }}Array_Create;
        GamutMathApi_Get{{ type }}ValuePointer {{ type }}_GetValuePointer;
        GamutMathApi_Get{{ type }}ValuePointer {{ type }}Array_GetValuePointer;
        GamutMathApi_GetArrayLength {{ type }}Array_GetLength;
    {% endfor %}
    {% for type in matrix_types %}
        GamutMathApi_GetType {{ type }}_GetType;
        GamutMathApi_GetType {{ type }}Array_GetType;
        GamutMathApi_Create{{ type }} {{ type }}_Create;
        GamutMathApi_Create{{ type }}Array {{ type }}Array_Create;
        GamutMathApi_Get{{ type }}ValuePointer {{ type }}_GetValuePointer;
        GamutMathApi_Get{{ type }}ValuePointer {{ type }}Array_GetValuePointer;
        GamutMathApi_GetArrayLength {{ type }}Array_GetLength;
    {% endfor %}
    {% for type in quaternion_types %}
        GamutMathApi_GetType {{ type }}_GetType;
        GamutMathApi_GetType {{ type }}Array_GetType;
        GamutMathApi_Create{{ type }} {{ type }}_Create;
        GamutMathApi_Create{{ type }}Array {{ type }}Array_Create;
        GamutMathApi_Get{{ type }}ValuePointer {{ type }}_GetValuePointer;
        GamutMathApi_Get{{ type }}ValuePointer {{ type }}Array_GetValuePointer;
        GamutMathApi_GetArrayLength {{ type }}Array_GetLength;
    {% endfor %}
    {% for type in pod_types %}
        GamutMathApi_GetType {{ type }}Array_GetType;
        GamutMathApi_Create{{ type }}Array {{ type }}Array_Create;
        GamutMathApi_Get{{ type }}ValuePointer {{ type }}Array_GetValuePointer;
        GamutMathApi_GetArrayLength {{ type }}Array_GetLength;
    {% endfor %}
};

static struct GamutMathApi *
GamutMathApi_Get()
{
    if (!PyImport_ImportModule("gamut.math._math")){ return 0; }
    return (struct GamutMathApi *)PyCapsule_Import("gamut.math._math._api", 0);
}

static void
GamutMathApi_Release()
{
    PyObject *module = PyImport_ImportModule("gamut.math._math");
    if (!module){ return; }
    Py_DECREF(module);
    Py_DECREF(module);
}

#ifdef __cplusplus
}
#endif

#endif