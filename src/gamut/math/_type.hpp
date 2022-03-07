
#ifndef GAMUT_MATH_TYPE_HPP
#define GAMUT_MATH_TYPE_HPP

// python
#define PY_SSIZE_T_CLEAN
#include <Python.h>


bool pyobject_to_c_bool(PyObject *py)
{
    return PyObject_IsTrue(py);
}


double pyobject_to_c_double(PyObject *py)
{
    return PyFloat_AsDouble(py);
}


float pyobject_to_c_float(PyObject *py)
{
    return PyFloat_AsDouble(py);
    // todo: check for overflow
}


int8_t pyobject_to_c_int8_t(PyObject *py)
{
    return PyLong_AsLong(py);
    // todo: check for overflow
}


uint8_t pyobject_to_c_uint8_t(PyObject *py)
{
    return PyLong_AsUnsignedLong(py);
    // todo: check for overflow
}


int16_t pyobject_to_c_int16_t(PyObject *py)
{
    return PyLong_AsLong(py);
    // todo: check for overflow
}


uint16_t pyobject_to_c_uint16_t(PyObject *py)
{
    return PyLong_AsUnsignedLong(py);
    // todo: check for overflow
}


int32_t pyobject_to_c_int32_t(PyObject *py)
{
    return PyLong_AsLong(py);
    // todo: check for overflow
}


uint32_t pyobject_to_c_uint32_t(PyObject *py)
{
    return PyLong_AsUnsignedLong(py);
    // todo: check for overflow
}


int pyobject_to_c_int(PyObject *py)
{
    return PyLong_AsLong(py);
    // todo: check for overflow
}


unsigned int pyobject_to_c_unsigned_int(PyObject *py)
{
    return PyLong_AsUnsignedLong(py);
    // todo: check for overflow
}


int64_t pyobject_to_c_int64_t(PyObject *py)
{
    if (sizeof(int64_t) > sizeof(long))
    {
        return PyLong_AsLongLong(py);
    }
    else
    {
        return PyLong_AsLong(py);
    }
    // todo: check for overflow
}


uint64_t pyobject_to_c_uint64_t(PyObject *py)
{
    if (sizeof(uint64_t) > sizeof(long))
    {
        return PyLong_AsUnsignedLongLong(py);
    }
    else
    {
        return PyLong_AsUnsignedLong(py);
    }
    // todo: check for overflow
}


PyObject *c_bool_to_pyobject(bool c)
{
    return PyBool_FromLong(c);
}


PyObject *c_double_to_pyobject(double c)
{
    return PyFloat_FromDouble(c);
}


PyObject *c_float_to_pyobject(float c)
{
    return PyFloat_FromDouble(c);
}


PyObject *c_int8_t_to_pyobject(int8_t c)
{
    return PyLong_FromLong(c);
}


PyObject *c_uint8_t_to_pyobject(uint8_t c)
{
    return PyLong_FromUnsignedLong(c);
}


PyObject *c_int16_t_to_pyobject(int16_t c)
{
    return PyLong_FromLong(c);
}


PyObject *c_uint16_t_to_pyobject(uint16_t c)
{
    return PyLong_FromUnsignedLong(c);
}


PyObject *c_int32_t_to_pyobject(int32_t c)
{
    return PyLong_FromLong(c);
}


PyObject *c_uint32_t_to_pyobject(uint32_t c)
{
    return PyLong_FromUnsignedLong(c);
}


PyObject *c_int_to_pyobject(int c)
{
    return PyLong_FromLong(c);
}


PyObject *c_unsigned_int_to_pyobject(unsigned int c)
{
    return PyLong_FromUnsignedLong(c);
}

PyObject *c_int64_t_to_pyobject(int64_t c)
{
    if (sizeof(int64_t) > sizeof(long))
    {
        return PyLong_FromLongLong(c);
    }
    else
    {
        return PyLong_FromLong(c);
    }
}


PyObject *c_uint64_t_to_pyobject(uint64_t c)
{
    if (sizeof(uint64_t) > sizeof(unsigned long))
    {
        return PyLong_FromUnsignedLongLong(c);
    }
    else
    {
        return PyLong_FromUnsignedLong(c);
    }
}

#endif