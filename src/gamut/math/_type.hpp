// python
#define PY_SSIZE_T_CLEAN
#include <Python.h>


double pyobject_to_c_double(PyObject *py)
{
    return PyFloat_AsDouble(py);
}


PyObject *c_double_to_pyobject(double c)
{
    return PyFloat_FromDouble(c);
}