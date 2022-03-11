
// generated 2022-03-10 23:24:28.437931 from codegen/math/templates/_vectortype.hpp

#ifndef GAMUT_MATH_VECTORTYPE_HPP
#define GAMUT_MATH_VECTORTYPE_HPP

// python
#define PY_SSIZE_T_CLEAN
#include <Python.h>
// glm
#include <glm/glm.hpp>
#include <glm/ext.hpp>



typedef glm::vec<2, bool, glm::defaultp> BVector2Glm;

struct BVector2
{
    PyObject_HEAD
    PyObject *weakreflist;
    BVector2Glm *glm;
};

static BVector2 *
create_BVector2_from_glm(const BVector2Glm& glm);



typedef glm::vec<2, double, glm::defaultp> DVector2Glm;

struct DVector2
{
    PyObject_HEAD
    PyObject *weakreflist;
    DVector2Glm *glm;
};

static DVector2 *
create_DVector2_from_glm(const DVector2Glm& glm);



typedef glm::vec<2, float, glm::defaultp> FVector2Glm;

struct FVector2
{
    PyObject_HEAD
    PyObject *weakreflist;
    FVector2Glm *glm;
};

static FVector2 *
create_FVector2_from_glm(const FVector2Glm& glm);



typedef glm::vec<2, int8_t, glm::defaultp> I8Vector2Glm;

struct I8Vector2
{
    PyObject_HEAD
    PyObject *weakreflist;
    I8Vector2Glm *glm;
};

static I8Vector2 *
create_I8Vector2_from_glm(const I8Vector2Glm& glm);



typedef glm::vec<2, uint8_t, glm::defaultp> U8Vector2Glm;

struct U8Vector2
{
    PyObject_HEAD
    PyObject *weakreflist;
    U8Vector2Glm *glm;
};

static U8Vector2 *
create_U8Vector2_from_glm(const U8Vector2Glm& glm);



typedef glm::vec<2, int16_t, glm::defaultp> I16Vector2Glm;

struct I16Vector2
{
    PyObject_HEAD
    PyObject *weakreflist;
    I16Vector2Glm *glm;
};

static I16Vector2 *
create_I16Vector2_from_glm(const I16Vector2Glm& glm);



typedef glm::vec<2, uint16_t, glm::defaultp> U16Vector2Glm;

struct U16Vector2
{
    PyObject_HEAD
    PyObject *weakreflist;
    U16Vector2Glm *glm;
};

static U16Vector2 *
create_U16Vector2_from_glm(const U16Vector2Glm& glm);



typedef glm::vec<2, int32_t, glm::defaultp> I32Vector2Glm;

struct I32Vector2
{
    PyObject_HEAD
    PyObject *weakreflist;
    I32Vector2Glm *glm;
};

static I32Vector2 *
create_I32Vector2_from_glm(const I32Vector2Glm& glm);



typedef glm::vec<2, uint32_t, glm::defaultp> U32Vector2Glm;

struct U32Vector2
{
    PyObject_HEAD
    PyObject *weakreflist;
    U32Vector2Glm *glm;
};

static U32Vector2 *
create_U32Vector2_from_glm(const U32Vector2Glm& glm);



typedef glm::vec<2, int, glm::defaultp> IVector2Glm;

struct IVector2
{
    PyObject_HEAD
    PyObject *weakreflist;
    IVector2Glm *glm;
};

static IVector2 *
create_IVector2_from_glm(const IVector2Glm& glm);



typedef glm::vec<2, unsigned int, glm::defaultp> UVector2Glm;

struct UVector2
{
    PyObject_HEAD
    PyObject *weakreflist;
    UVector2Glm *glm;
};

static UVector2 *
create_UVector2_from_glm(const UVector2Glm& glm);



typedef glm::vec<2, int64_t, glm::defaultp> I64Vector2Glm;

struct I64Vector2
{
    PyObject_HEAD
    PyObject *weakreflist;
    I64Vector2Glm *glm;
};

static I64Vector2 *
create_I64Vector2_from_glm(const I64Vector2Glm& glm);



typedef glm::vec<2, uint64_t, glm::defaultp> U64Vector2Glm;

struct U64Vector2
{
    PyObject_HEAD
    PyObject *weakreflist;
    U64Vector2Glm *glm;
};

static U64Vector2 *
create_U64Vector2_from_glm(const U64Vector2Glm& glm);



typedef glm::vec<3, bool, glm::defaultp> BVector3Glm;

struct BVector3
{
    PyObject_HEAD
    PyObject *weakreflist;
    BVector3Glm *glm;
};

static BVector3 *
create_BVector3_from_glm(const BVector3Glm& glm);



typedef glm::vec<3, double, glm::defaultp> DVector3Glm;

struct DVector3
{
    PyObject_HEAD
    PyObject *weakreflist;
    DVector3Glm *glm;
};

static DVector3 *
create_DVector3_from_glm(const DVector3Glm& glm);



typedef glm::vec<3, float, glm::defaultp> FVector3Glm;

struct FVector3
{
    PyObject_HEAD
    PyObject *weakreflist;
    FVector3Glm *glm;
};

static FVector3 *
create_FVector3_from_glm(const FVector3Glm& glm);



typedef glm::vec<3, int8_t, glm::defaultp> I8Vector3Glm;

struct I8Vector3
{
    PyObject_HEAD
    PyObject *weakreflist;
    I8Vector3Glm *glm;
};

static I8Vector3 *
create_I8Vector3_from_glm(const I8Vector3Glm& glm);



typedef glm::vec<3, uint8_t, glm::defaultp> U8Vector3Glm;

struct U8Vector3
{
    PyObject_HEAD
    PyObject *weakreflist;
    U8Vector3Glm *glm;
};

static U8Vector3 *
create_U8Vector3_from_glm(const U8Vector3Glm& glm);



typedef glm::vec<3, int16_t, glm::defaultp> I16Vector3Glm;

struct I16Vector3
{
    PyObject_HEAD
    PyObject *weakreflist;
    I16Vector3Glm *glm;
};

static I16Vector3 *
create_I16Vector3_from_glm(const I16Vector3Glm& glm);



typedef glm::vec<3, uint16_t, glm::defaultp> U16Vector3Glm;

struct U16Vector3
{
    PyObject_HEAD
    PyObject *weakreflist;
    U16Vector3Glm *glm;
};

static U16Vector3 *
create_U16Vector3_from_glm(const U16Vector3Glm& glm);



typedef glm::vec<3, int32_t, glm::defaultp> I32Vector3Glm;

struct I32Vector3
{
    PyObject_HEAD
    PyObject *weakreflist;
    I32Vector3Glm *glm;
};

static I32Vector3 *
create_I32Vector3_from_glm(const I32Vector3Glm& glm);



typedef glm::vec<3, uint32_t, glm::defaultp> U32Vector3Glm;

struct U32Vector3
{
    PyObject_HEAD
    PyObject *weakreflist;
    U32Vector3Glm *glm;
};

static U32Vector3 *
create_U32Vector3_from_glm(const U32Vector3Glm& glm);



typedef glm::vec<3, int, glm::defaultp> IVector3Glm;

struct IVector3
{
    PyObject_HEAD
    PyObject *weakreflist;
    IVector3Glm *glm;
};

static IVector3 *
create_IVector3_from_glm(const IVector3Glm& glm);



typedef glm::vec<3, unsigned int, glm::defaultp> UVector3Glm;

struct UVector3
{
    PyObject_HEAD
    PyObject *weakreflist;
    UVector3Glm *glm;
};

static UVector3 *
create_UVector3_from_glm(const UVector3Glm& glm);



typedef glm::vec<3, int64_t, glm::defaultp> I64Vector3Glm;

struct I64Vector3
{
    PyObject_HEAD
    PyObject *weakreflist;
    I64Vector3Glm *glm;
};

static I64Vector3 *
create_I64Vector3_from_glm(const I64Vector3Glm& glm);



typedef glm::vec<3, uint64_t, glm::defaultp> U64Vector3Glm;

struct U64Vector3
{
    PyObject_HEAD
    PyObject *weakreflist;
    U64Vector3Glm *glm;
};

static U64Vector3 *
create_U64Vector3_from_glm(const U64Vector3Glm& glm);



typedef glm::vec<4, bool, glm::defaultp> BVector4Glm;

struct BVector4
{
    PyObject_HEAD
    PyObject *weakreflist;
    BVector4Glm *glm;
};

static BVector4 *
create_BVector4_from_glm(const BVector4Glm& glm);



typedef glm::vec<4, double, glm::defaultp> DVector4Glm;

struct DVector4
{
    PyObject_HEAD
    PyObject *weakreflist;
    DVector4Glm *glm;
};

static DVector4 *
create_DVector4_from_glm(const DVector4Glm& glm);



typedef glm::vec<4, float, glm::defaultp> FVector4Glm;

struct FVector4
{
    PyObject_HEAD
    PyObject *weakreflist;
    FVector4Glm *glm;
};

static FVector4 *
create_FVector4_from_glm(const FVector4Glm& glm);



typedef glm::vec<4, int8_t, glm::defaultp> I8Vector4Glm;

struct I8Vector4
{
    PyObject_HEAD
    PyObject *weakreflist;
    I8Vector4Glm *glm;
};

static I8Vector4 *
create_I8Vector4_from_glm(const I8Vector4Glm& glm);



typedef glm::vec<4, uint8_t, glm::defaultp> U8Vector4Glm;

struct U8Vector4
{
    PyObject_HEAD
    PyObject *weakreflist;
    U8Vector4Glm *glm;
};

static U8Vector4 *
create_U8Vector4_from_glm(const U8Vector4Glm& glm);



typedef glm::vec<4, int16_t, glm::defaultp> I16Vector4Glm;

struct I16Vector4
{
    PyObject_HEAD
    PyObject *weakreflist;
    I16Vector4Glm *glm;
};

static I16Vector4 *
create_I16Vector4_from_glm(const I16Vector4Glm& glm);



typedef glm::vec<4, uint16_t, glm::defaultp> U16Vector4Glm;

struct U16Vector4
{
    PyObject_HEAD
    PyObject *weakreflist;
    U16Vector4Glm *glm;
};

static U16Vector4 *
create_U16Vector4_from_glm(const U16Vector4Glm& glm);



typedef glm::vec<4, int32_t, glm::defaultp> I32Vector4Glm;

struct I32Vector4
{
    PyObject_HEAD
    PyObject *weakreflist;
    I32Vector4Glm *glm;
};

static I32Vector4 *
create_I32Vector4_from_glm(const I32Vector4Glm& glm);



typedef glm::vec<4, uint32_t, glm::defaultp> U32Vector4Glm;

struct U32Vector4
{
    PyObject_HEAD
    PyObject *weakreflist;
    U32Vector4Glm *glm;
};

static U32Vector4 *
create_U32Vector4_from_glm(const U32Vector4Glm& glm);



typedef glm::vec<4, int, glm::defaultp> IVector4Glm;

struct IVector4
{
    PyObject_HEAD
    PyObject *weakreflist;
    IVector4Glm *glm;
};

static IVector4 *
create_IVector4_from_glm(const IVector4Glm& glm);



typedef glm::vec<4, unsigned int, glm::defaultp> UVector4Glm;

struct UVector4
{
    PyObject_HEAD
    PyObject *weakreflist;
    UVector4Glm *glm;
};

static UVector4 *
create_UVector4_from_glm(const UVector4Glm& glm);



typedef glm::vec<4, int64_t, glm::defaultp> I64Vector4Glm;

struct I64Vector4
{
    PyObject_HEAD
    PyObject *weakreflist;
    I64Vector4Glm *glm;
};

static I64Vector4 *
create_I64Vector4_from_glm(const I64Vector4Glm& glm);



typedef glm::vec<4, uint64_t, glm::defaultp> U64Vector4Glm;

struct U64Vector4
{
    PyObject_HEAD
    PyObject *weakreflist;
    U64Vector4Glm *glm;
};

static U64Vector4 *
create_U64Vector4_from_glm(const U64Vector4Glm& glm);



#endif