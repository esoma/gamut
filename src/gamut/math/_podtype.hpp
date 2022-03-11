
// generated 2022-03-11 18:37:26.839966 from codegen/math/templates/_podtype.hpp

#ifndef GAMUT_MATH_PODTYPE_HPP
#define GAMUT_MATH_PODTYPE_HPP

// python
#define PY_SSIZE_T_CLEAN
#include <Python.h>



struct BArray
{
    PyObject_HEAD
    PyObject *weakreflist;
    size_t length;
    bool *pod;
};



struct DArray
{
    PyObject_HEAD
    PyObject *weakreflist;
    size_t length;
    double *pod;
};



struct FArray
{
    PyObject_HEAD
    PyObject *weakreflist;
    size_t length;
    float *pod;
};



struct I8Array
{
    PyObject_HEAD
    PyObject *weakreflist;
    size_t length;
    int8_t *pod;
};



struct U8Array
{
    PyObject_HEAD
    PyObject *weakreflist;
    size_t length;
    uint8_t *pod;
};



struct I16Array
{
    PyObject_HEAD
    PyObject *weakreflist;
    size_t length;
    int16_t *pod;
};



struct U16Array
{
    PyObject_HEAD
    PyObject *weakreflist;
    size_t length;
    uint16_t *pod;
};



struct I32Array
{
    PyObject_HEAD
    PyObject *weakreflist;
    size_t length;
    int32_t *pod;
};



struct U32Array
{
    PyObject_HEAD
    PyObject *weakreflist;
    size_t length;
    uint32_t *pod;
};



struct IArray
{
    PyObject_HEAD
    PyObject *weakreflist;
    size_t length;
    int *pod;
};



struct UArray
{
    PyObject_HEAD
    PyObject *weakreflist;
    size_t length;
    unsigned int *pod;
};



struct I64Array
{
    PyObject_HEAD
    PyObject *weakreflist;
    size_t length;
    int64_t *pod;
};



struct U64Array
{
    PyObject_HEAD
    PyObject *weakreflist;
    size_t length;
    uint64_t *pod;
};



#endif