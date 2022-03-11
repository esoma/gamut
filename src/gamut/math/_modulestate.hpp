
// generated 2022-03-11 03:01:13.082564 from codegen/math/templates/_modulestate.hpp

#ifndef GAMUT_MATH_MODULESTATE_HPP
#define GAMUT_MATH_MODULESTATE_HPP

// python
#define PY_SSIZE_T_CLEAN
#include <Python.h>
// gamut
#include "_module.hpp"

struct ModuleState
{

        PyTypeObject *BVector2_PyTypeObject;
        PyTypeObject *BVector2Array_PyTypeObject;

        PyTypeObject *DVector2_PyTypeObject;
        PyTypeObject *DVector2Array_PyTypeObject;

        PyTypeObject *FVector2_PyTypeObject;
        PyTypeObject *FVector2Array_PyTypeObject;

        PyTypeObject *I8Vector2_PyTypeObject;
        PyTypeObject *I8Vector2Array_PyTypeObject;

        PyTypeObject *U8Vector2_PyTypeObject;
        PyTypeObject *U8Vector2Array_PyTypeObject;

        PyTypeObject *I16Vector2_PyTypeObject;
        PyTypeObject *I16Vector2Array_PyTypeObject;

        PyTypeObject *U16Vector2_PyTypeObject;
        PyTypeObject *U16Vector2Array_PyTypeObject;

        PyTypeObject *I32Vector2_PyTypeObject;
        PyTypeObject *I32Vector2Array_PyTypeObject;

        PyTypeObject *U32Vector2_PyTypeObject;
        PyTypeObject *U32Vector2Array_PyTypeObject;

        PyTypeObject *IVector2_PyTypeObject;
        PyTypeObject *IVector2Array_PyTypeObject;

        PyTypeObject *UVector2_PyTypeObject;
        PyTypeObject *UVector2Array_PyTypeObject;

        PyTypeObject *I64Vector2_PyTypeObject;
        PyTypeObject *I64Vector2Array_PyTypeObject;

        PyTypeObject *U64Vector2_PyTypeObject;
        PyTypeObject *U64Vector2Array_PyTypeObject;

        PyTypeObject *BVector3_PyTypeObject;
        PyTypeObject *BVector3Array_PyTypeObject;

        PyTypeObject *DVector3_PyTypeObject;
        PyTypeObject *DVector3Array_PyTypeObject;

        PyTypeObject *FVector3_PyTypeObject;
        PyTypeObject *FVector3Array_PyTypeObject;

        PyTypeObject *I8Vector3_PyTypeObject;
        PyTypeObject *I8Vector3Array_PyTypeObject;

        PyTypeObject *U8Vector3_PyTypeObject;
        PyTypeObject *U8Vector3Array_PyTypeObject;

        PyTypeObject *I16Vector3_PyTypeObject;
        PyTypeObject *I16Vector3Array_PyTypeObject;

        PyTypeObject *U16Vector3_PyTypeObject;
        PyTypeObject *U16Vector3Array_PyTypeObject;

        PyTypeObject *I32Vector3_PyTypeObject;
        PyTypeObject *I32Vector3Array_PyTypeObject;

        PyTypeObject *U32Vector3_PyTypeObject;
        PyTypeObject *U32Vector3Array_PyTypeObject;

        PyTypeObject *IVector3_PyTypeObject;
        PyTypeObject *IVector3Array_PyTypeObject;

        PyTypeObject *UVector3_PyTypeObject;
        PyTypeObject *UVector3Array_PyTypeObject;

        PyTypeObject *I64Vector3_PyTypeObject;
        PyTypeObject *I64Vector3Array_PyTypeObject;

        PyTypeObject *U64Vector3_PyTypeObject;
        PyTypeObject *U64Vector3Array_PyTypeObject;

        PyTypeObject *BVector4_PyTypeObject;
        PyTypeObject *BVector4Array_PyTypeObject;

        PyTypeObject *DVector4_PyTypeObject;
        PyTypeObject *DVector4Array_PyTypeObject;

        PyTypeObject *FVector4_PyTypeObject;
        PyTypeObject *FVector4Array_PyTypeObject;

        PyTypeObject *I8Vector4_PyTypeObject;
        PyTypeObject *I8Vector4Array_PyTypeObject;

        PyTypeObject *U8Vector4_PyTypeObject;
        PyTypeObject *U8Vector4Array_PyTypeObject;

        PyTypeObject *I16Vector4_PyTypeObject;
        PyTypeObject *I16Vector4Array_PyTypeObject;

        PyTypeObject *U16Vector4_PyTypeObject;
        PyTypeObject *U16Vector4Array_PyTypeObject;

        PyTypeObject *I32Vector4_PyTypeObject;
        PyTypeObject *I32Vector4Array_PyTypeObject;

        PyTypeObject *U32Vector4_PyTypeObject;
        PyTypeObject *U32Vector4Array_PyTypeObject;

        PyTypeObject *IVector4_PyTypeObject;
        PyTypeObject *IVector4Array_PyTypeObject;

        PyTypeObject *UVector4_PyTypeObject;
        PyTypeObject *UVector4Array_PyTypeObject;

        PyTypeObject *I64Vector4_PyTypeObject;
        PyTypeObject *I64Vector4Array_PyTypeObject;

        PyTypeObject *U64Vector4_PyTypeObject;
        PyTypeObject *U64Vector4Array_PyTypeObject;

        PyTypeObject *DMatrix2x2_PyTypeObject;
        PyTypeObject *DMatrix2x2Array_PyTypeObject;

        PyTypeObject *FMatrix2x2_PyTypeObject;
        PyTypeObject *FMatrix2x2Array_PyTypeObject;

        PyTypeObject *DMatrix2x3_PyTypeObject;
        PyTypeObject *DMatrix2x3Array_PyTypeObject;

        PyTypeObject *FMatrix2x3_PyTypeObject;
        PyTypeObject *FMatrix2x3Array_PyTypeObject;

        PyTypeObject *DMatrix2x4_PyTypeObject;
        PyTypeObject *DMatrix2x4Array_PyTypeObject;

        PyTypeObject *FMatrix2x4_PyTypeObject;
        PyTypeObject *FMatrix2x4Array_PyTypeObject;

        PyTypeObject *DMatrix3x2_PyTypeObject;
        PyTypeObject *DMatrix3x2Array_PyTypeObject;

        PyTypeObject *FMatrix3x2_PyTypeObject;
        PyTypeObject *FMatrix3x2Array_PyTypeObject;

        PyTypeObject *DMatrix3x3_PyTypeObject;
        PyTypeObject *DMatrix3x3Array_PyTypeObject;

        PyTypeObject *FMatrix3x3_PyTypeObject;
        PyTypeObject *FMatrix3x3Array_PyTypeObject;

        PyTypeObject *DMatrix3x4_PyTypeObject;
        PyTypeObject *DMatrix3x4Array_PyTypeObject;

        PyTypeObject *FMatrix3x4_PyTypeObject;
        PyTypeObject *FMatrix3x4Array_PyTypeObject;

        PyTypeObject *DMatrix4x2_PyTypeObject;
        PyTypeObject *DMatrix4x2Array_PyTypeObject;

        PyTypeObject *FMatrix4x2_PyTypeObject;
        PyTypeObject *FMatrix4x2Array_PyTypeObject;

        PyTypeObject *DMatrix4x3_PyTypeObject;
        PyTypeObject *DMatrix4x3Array_PyTypeObject;

        PyTypeObject *FMatrix4x3_PyTypeObject;
        PyTypeObject *FMatrix4x3Array_PyTypeObject;

        PyTypeObject *DMatrix4x4_PyTypeObject;
        PyTypeObject *DMatrix4x4Array_PyTypeObject;

        PyTypeObject *FMatrix4x4_PyTypeObject;
        PyTypeObject *FMatrix4x4Array_PyTypeObject;

};


static int
ModuleState_traverse(
    struct ModuleState *self,
    visitproc visit,
    void *arg
)
{

        Py_VISIT(self->BVector2_PyTypeObject);
        Py_VISIT(self->BVector2Array_PyTypeObject);

        Py_VISIT(self->DVector2_PyTypeObject);
        Py_VISIT(self->DVector2Array_PyTypeObject);

        Py_VISIT(self->FVector2_PyTypeObject);
        Py_VISIT(self->FVector2Array_PyTypeObject);

        Py_VISIT(self->I8Vector2_PyTypeObject);
        Py_VISIT(self->I8Vector2Array_PyTypeObject);

        Py_VISIT(self->U8Vector2_PyTypeObject);
        Py_VISIT(self->U8Vector2Array_PyTypeObject);

        Py_VISIT(self->I16Vector2_PyTypeObject);
        Py_VISIT(self->I16Vector2Array_PyTypeObject);

        Py_VISIT(self->U16Vector2_PyTypeObject);
        Py_VISIT(self->U16Vector2Array_PyTypeObject);

        Py_VISIT(self->I32Vector2_PyTypeObject);
        Py_VISIT(self->I32Vector2Array_PyTypeObject);

        Py_VISIT(self->U32Vector2_PyTypeObject);
        Py_VISIT(self->U32Vector2Array_PyTypeObject);

        Py_VISIT(self->IVector2_PyTypeObject);
        Py_VISIT(self->IVector2Array_PyTypeObject);

        Py_VISIT(self->UVector2_PyTypeObject);
        Py_VISIT(self->UVector2Array_PyTypeObject);

        Py_VISIT(self->I64Vector2_PyTypeObject);
        Py_VISIT(self->I64Vector2Array_PyTypeObject);

        Py_VISIT(self->U64Vector2_PyTypeObject);
        Py_VISIT(self->U64Vector2Array_PyTypeObject);

        Py_VISIT(self->BVector3_PyTypeObject);
        Py_VISIT(self->BVector3Array_PyTypeObject);

        Py_VISIT(self->DVector3_PyTypeObject);
        Py_VISIT(self->DVector3Array_PyTypeObject);

        Py_VISIT(self->FVector3_PyTypeObject);
        Py_VISIT(self->FVector3Array_PyTypeObject);

        Py_VISIT(self->I8Vector3_PyTypeObject);
        Py_VISIT(self->I8Vector3Array_PyTypeObject);

        Py_VISIT(self->U8Vector3_PyTypeObject);
        Py_VISIT(self->U8Vector3Array_PyTypeObject);

        Py_VISIT(self->I16Vector3_PyTypeObject);
        Py_VISIT(self->I16Vector3Array_PyTypeObject);

        Py_VISIT(self->U16Vector3_PyTypeObject);
        Py_VISIT(self->U16Vector3Array_PyTypeObject);

        Py_VISIT(self->I32Vector3_PyTypeObject);
        Py_VISIT(self->I32Vector3Array_PyTypeObject);

        Py_VISIT(self->U32Vector3_PyTypeObject);
        Py_VISIT(self->U32Vector3Array_PyTypeObject);

        Py_VISIT(self->IVector3_PyTypeObject);
        Py_VISIT(self->IVector3Array_PyTypeObject);

        Py_VISIT(self->UVector3_PyTypeObject);
        Py_VISIT(self->UVector3Array_PyTypeObject);

        Py_VISIT(self->I64Vector3_PyTypeObject);
        Py_VISIT(self->I64Vector3Array_PyTypeObject);

        Py_VISIT(self->U64Vector3_PyTypeObject);
        Py_VISIT(self->U64Vector3Array_PyTypeObject);

        Py_VISIT(self->BVector4_PyTypeObject);
        Py_VISIT(self->BVector4Array_PyTypeObject);

        Py_VISIT(self->DVector4_PyTypeObject);
        Py_VISIT(self->DVector4Array_PyTypeObject);

        Py_VISIT(self->FVector4_PyTypeObject);
        Py_VISIT(self->FVector4Array_PyTypeObject);

        Py_VISIT(self->I8Vector4_PyTypeObject);
        Py_VISIT(self->I8Vector4Array_PyTypeObject);

        Py_VISIT(self->U8Vector4_PyTypeObject);
        Py_VISIT(self->U8Vector4Array_PyTypeObject);

        Py_VISIT(self->I16Vector4_PyTypeObject);
        Py_VISIT(self->I16Vector4Array_PyTypeObject);

        Py_VISIT(self->U16Vector4_PyTypeObject);
        Py_VISIT(self->U16Vector4Array_PyTypeObject);

        Py_VISIT(self->I32Vector4_PyTypeObject);
        Py_VISIT(self->I32Vector4Array_PyTypeObject);

        Py_VISIT(self->U32Vector4_PyTypeObject);
        Py_VISIT(self->U32Vector4Array_PyTypeObject);

        Py_VISIT(self->IVector4_PyTypeObject);
        Py_VISIT(self->IVector4Array_PyTypeObject);

        Py_VISIT(self->UVector4_PyTypeObject);
        Py_VISIT(self->UVector4Array_PyTypeObject);

        Py_VISIT(self->I64Vector4_PyTypeObject);
        Py_VISIT(self->I64Vector4Array_PyTypeObject);

        Py_VISIT(self->U64Vector4_PyTypeObject);
        Py_VISIT(self->U64Vector4Array_PyTypeObject);

        Py_VISIT(self->DMatrix2x2_PyTypeObject);
        Py_VISIT(self->DMatrix2x2Array_PyTypeObject);

        Py_VISIT(self->FMatrix2x2_PyTypeObject);
        Py_VISIT(self->FMatrix2x2Array_PyTypeObject);

        Py_VISIT(self->DMatrix2x3_PyTypeObject);
        Py_VISIT(self->DMatrix2x3Array_PyTypeObject);

        Py_VISIT(self->FMatrix2x3_PyTypeObject);
        Py_VISIT(self->FMatrix2x3Array_PyTypeObject);

        Py_VISIT(self->DMatrix2x4_PyTypeObject);
        Py_VISIT(self->DMatrix2x4Array_PyTypeObject);

        Py_VISIT(self->FMatrix2x4_PyTypeObject);
        Py_VISIT(self->FMatrix2x4Array_PyTypeObject);

        Py_VISIT(self->DMatrix3x2_PyTypeObject);
        Py_VISIT(self->DMatrix3x2Array_PyTypeObject);

        Py_VISIT(self->FMatrix3x2_PyTypeObject);
        Py_VISIT(self->FMatrix3x2Array_PyTypeObject);

        Py_VISIT(self->DMatrix3x3_PyTypeObject);
        Py_VISIT(self->DMatrix3x3Array_PyTypeObject);

        Py_VISIT(self->FMatrix3x3_PyTypeObject);
        Py_VISIT(self->FMatrix3x3Array_PyTypeObject);

        Py_VISIT(self->DMatrix3x4_PyTypeObject);
        Py_VISIT(self->DMatrix3x4Array_PyTypeObject);

        Py_VISIT(self->FMatrix3x4_PyTypeObject);
        Py_VISIT(self->FMatrix3x4Array_PyTypeObject);

        Py_VISIT(self->DMatrix4x2_PyTypeObject);
        Py_VISIT(self->DMatrix4x2Array_PyTypeObject);

        Py_VISIT(self->FMatrix4x2_PyTypeObject);
        Py_VISIT(self->FMatrix4x2Array_PyTypeObject);

        Py_VISIT(self->DMatrix4x3_PyTypeObject);
        Py_VISIT(self->DMatrix4x3Array_PyTypeObject);

        Py_VISIT(self->FMatrix4x3_PyTypeObject);
        Py_VISIT(self->FMatrix4x3Array_PyTypeObject);

        Py_VISIT(self->DMatrix4x4_PyTypeObject);
        Py_VISIT(self->DMatrix4x4Array_PyTypeObject);

        Py_VISIT(self->FMatrix4x4_PyTypeObject);
        Py_VISIT(self->FMatrix4x4Array_PyTypeObject);

    return 0;
}


static int
ModuleState_clear(struct ModuleState *self)
{

        Py_CLEAR(self->BVector2_PyTypeObject);
        Py_CLEAR(self->BVector2Array_PyTypeObject);

        Py_CLEAR(self->DVector2_PyTypeObject);
        Py_CLEAR(self->DVector2Array_PyTypeObject);

        Py_CLEAR(self->FVector2_PyTypeObject);
        Py_CLEAR(self->FVector2Array_PyTypeObject);

        Py_CLEAR(self->I8Vector2_PyTypeObject);
        Py_CLEAR(self->I8Vector2Array_PyTypeObject);

        Py_CLEAR(self->U8Vector2_PyTypeObject);
        Py_CLEAR(self->U8Vector2Array_PyTypeObject);

        Py_CLEAR(self->I16Vector2_PyTypeObject);
        Py_CLEAR(self->I16Vector2Array_PyTypeObject);

        Py_CLEAR(self->U16Vector2_PyTypeObject);
        Py_CLEAR(self->U16Vector2Array_PyTypeObject);

        Py_CLEAR(self->I32Vector2_PyTypeObject);
        Py_CLEAR(self->I32Vector2Array_PyTypeObject);

        Py_CLEAR(self->U32Vector2_PyTypeObject);
        Py_CLEAR(self->U32Vector2Array_PyTypeObject);

        Py_CLEAR(self->IVector2_PyTypeObject);
        Py_CLEAR(self->IVector2Array_PyTypeObject);

        Py_CLEAR(self->UVector2_PyTypeObject);
        Py_CLEAR(self->UVector2Array_PyTypeObject);

        Py_CLEAR(self->I64Vector2_PyTypeObject);
        Py_CLEAR(self->I64Vector2Array_PyTypeObject);

        Py_CLEAR(self->U64Vector2_PyTypeObject);
        Py_CLEAR(self->U64Vector2Array_PyTypeObject);

        Py_CLEAR(self->BVector3_PyTypeObject);
        Py_CLEAR(self->BVector3Array_PyTypeObject);

        Py_CLEAR(self->DVector3_PyTypeObject);
        Py_CLEAR(self->DVector3Array_PyTypeObject);

        Py_CLEAR(self->FVector3_PyTypeObject);
        Py_CLEAR(self->FVector3Array_PyTypeObject);

        Py_CLEAR(self->I8Vector3_PyTypeObject);
        Py_CLEAR(self->I8Vector3Array_PyTypeObject);

        Py_CLEAR(self->U8Vector3_PyTypeObject);
        Py_CLEAR(self->U8Vector3Array_PyTypeObject);

        Py_CLEAR(self->I16Vector3_PyTypeObject);
        Py_CLEAR(self->I16Vector3Array_PyTypeObject);

        Py_CLEAR(self->U16Vector3_PyTypeObject);
        Py_CLEAR(self->U16Vector3Array_PyTypeObject);

        Py_CLEAR(self->I32Vector3_PyTypeObject);
        Py_CLEAR(self->I32Vector3Array_PyTypeObject);

        Py_CLEAR(self->U32Vector3_PyTypeObject);
        Py_CLEAR(self->U32Vector3Array_PyTypeObject);

        Py_CLEAR(self->IVector3_PyTypeObject);
        Py_CLEAR(self->IVector3Array_PyTypeObject);

        Py_CLEAR(self->UVector3_PyTypeObject);
        Py_CLEAR(self->UVector3Array_PyTypeObject);

        Py_CLEAR(self->I64Vector3_PyTypeObject);
        Py_CLEAR(self->I64Vector3Array_PyTypeObject);

        Py_CLEAR(self->U64Vector3_PyTypeObject);
        Py_CLEAR(self->U64Vector3Array_PyTypeObject);

        Py_CLEAR(self->BVector4_PyTypeObject);
        Py_CLEAR(self->BVector4Array_PyTypeObject);

        Py_CLEAR(self->DVector4_PyTypeObject);
        Py_CLEAR(self->DVector4Array_PyTypeObject);

        Py_CLEAR(self->FVector4_PyTypeObject);
        Py_CLEAR(self->FVector4Array_PyTypeObject);

        Py_CLEAR(self->I8Vector4_PyTypeObject);
        Py_CLEAR(self->I8Vector4Array_PyTypeObject);

        Py_CLEAR(self->U8Vector4_PyTypeObject);
        Py_CLEAR(self->U8Vector4Array_PyTypeObject);

        Py_CLEAR(self->I16Vector4_PyTypeObject);
        Py_CLEAR(self->I16Vector4Array_PyTypeObject);

        Py_CLEAR(self->U16Vector4_PyTypeObject);
        Py_CLEAR(self->U16Vector4Array_PyTypeObject);

        Py_CLEAR(self->I32Vector4_PyTypeObject);
        Py_CLEAR(self->I32Vector4Array_PyTypeObject);

        Py_CLEAR(self->U32Vector4_PyTypeObject);
        Py_CLEAR(self->U32Vector4Array_PyTypeObject);

        Py_CLEAR(self->IVector4_PyTypeObject);
        Py_CLEAR(self->IVector4Array_PyTypeObject);

        Py_CLEAR(self->UVector4_PyTypeObject);
        Py_CLEAR(self->UVector4Array_PyTypeObject);

        Py_CLEAR(self->I64Vector4_PyTypeObject);
        Py_CLEAR(self->I64Vector4Array_PyTypeObject);

        Py_CLEAR(self->U64Vector4_PyTypeObject);
        Py_CLEAR(self->U64Vector4Array_PyTypeObject);

        Py_CLEAR(self->DMatrix2x2_PyTypeObject);
        Py_CLEAR(self->DMatrix2x2Array_PyTypeObject);

        Py_CLEAR(self->FMatrix2x2_PyTypeObject);
        Py_CLEAR(self->FMatrix2x2Array_PyTypeObject);

        Py_CLEAR(self->DMatrix2x3_PyTypeObject);
        Py_CLEAR(self->DMatrix2x3Array_PyTypeObject);

        Py_CLEAR(self->FMatrix2x3_PyTypeObject);
        Py_CLEAR(self->FMatrix2x3Array_PyTypeObject);

        Py_CLEAR(self->DMatrix2x4_PyTypeObject);
        Py_CLEAR(self->DMatrix2x4Array_PyTypeObject);

        Py_CLEAR(self->FMatrix2x4_PyTypeObject);
        Py_CLEAR(self->FMatrix2x4Array_PyTypeObject);

        Py_CLEAR(self->DMatrix3x2_PyTypeObject);
        Py_CLEAR(self->DMatrix3x2Array_PyTypeObject);

        Py_CLEAR(self->FMatrix3x2_PyTypeObject);
        Py_CLEAR(self->FMatrix3x2Array_PyTypeObject);

        Py_CLEAR(self->DMatrix3x3_PyTypeObject);
        Py_CLEAR(self->DMatrix3x3Array_PyTypeObject);

        Py_CLEAR(self->FMatrix3x3_PyTypeObject);
        Py_CLEAR(self->FMatrix3x3Array_PyTypeObject);

        Py_CLEAR(self->DMatrix3x4_PyTypeObject);
        Py_CLEAR(self->DMatrix3x4Array_PyTypeObject);

        Py_CLEAR(self->FMatrix3x4_PyTypeObject);
        Py_CLEAR(self->FMatrix3x4Array_PyTypeObject);

        Py_CLEAR(self->DMatrix4x2_PyTypeObject);
        Py_CLEAR(self->DMatrix4x2Array_PyTypeObject);

        Py_CLEAR(self->FMatrix4x2_PyTypeObject);
        Py_CLEAR(self->FMatrix4x2Array_PyTypeObject);

        Py_CLEAR(self->DMatrix4x3_PyTypeObject);
        Py_CLEAR(self->DMatrix4x3Array_PyTypeObject);

        Py_CLEAR(self->FMatrix4x3_PyTypeObject);
        Py_CLEAR(self->FMatrix4x3Array_PyTypeObject);

        Py_CLEAR(self->DMatrix4x4_PyTypeObject);
        Py_CLEAR(self->DMatrix4x4Array_PyTypeObject);

        Py_CLEAR(self->FMatrix4x4_PyTypeObject);
        Py_CLEAR(self->FMatrix4x4Array_PyTypeObject);

    return 0;
}


static ModuleState *
get_module_state()
{
    PyObject *module = get_module();
    if (!module){ return 0; }
    return (ModuleState *)PyModule_GetState(module);
}

#endif