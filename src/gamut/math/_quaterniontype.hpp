
// generated 2022-03-13 14:05:23.351345 from codegen/math/templates/_quaterniontype.hpp

#ifndef GAMUT_MATH_QUATERNIONTYPE_HPP
#define GAMUT_MATH_QUATERNIONTYPE_HPP

// python
#define PY_SSIZE_T_CLEAN
#include <Python.h>
// glm
#include <glm/glm.hpp>
#include <glm/ext.hpp>



typedef glm::tquat<double> DQuaternionGlm;

struct DQuaternion
{
    PyObject_HEAD
    PyObject *weakreflist;
    DQuaternionGlm *glm;
};

struct DQuaternionArray
{
    PyObject_HEAD
    PyObject *weakreflist;
    size_t length;
    DQuaternionGlm *glm;
};



typedef glm::tquat<float> FQuaternionGlm;

struct FQuaternion
{
    PyObject_HEAD
    PyObject *weakreflist;
    FQuaternionGlm *glm;
};

struct FQuaternionArray
{
    PyObject_HEAD
    PyObject *weakreflist;
    size_t length;
    FQuaternionGlm *glm;
};



#endif