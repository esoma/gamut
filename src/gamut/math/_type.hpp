
#ifndef GAMUT_MATH_TYPE_HPP
#define GAMUT_MATH_TYPE_HPP

// python
#define PY_SSIZE_T_CLEAN
#include <Python.h>


double pyobject_to_c_double(PyObject *py)
{
    return PyFloat_AsDouble(py);
}


float pyobject_to_c_float(PyObject *py)
{
    return PyFloat_AsDouble(py);
}


PyObject *c_double_to_pyobject(double c)
{
    return PyFloat_FromDouble(c);
}


PyObject *c_float_to_pyobject(float c)
{
    return PyFloat_FromDouble(c);
}

#endif