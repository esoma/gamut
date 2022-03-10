
// generated {{ when }} from codegen/math/templates/_matrixtype.hpp

#ifndef GAMUT_MATH_MATRIXTYPE_HPP
#define GAMUT_MATH_MATRIXTYPE_HPP

// python
#define PY_SSIZE_T_CLEAN
#include <Python.h>
// glm
#include <glm/glm.hpp>
#include <glm/ext.hpp>

{% for name, column_size, row_size, c_type in types %}

typedef glm::tmat{{ row_size }}x{{ column_size }}<{{ c_type }}, glm::defaultp> {{ name }}Glm;

struct {{ name }}
{
    PyObject_HEAD
    PyObject *weakreflist;
    {{ name }}Glm *glm;
};

{% endfor %}

#endif