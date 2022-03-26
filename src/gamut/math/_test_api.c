
// generated 2022-03-26 21:40:50.308078 from codegen/math/templates/test_api.cpp

// stdlib
#include <stddef.h>
// python
#define PY_SSIZE_T_CLEAN
#include <Python.h>
// gamut
#include "gamut/math.h"

#define TEST(X) if (!(X)){ PyErr_Format(PyExc_AssertionError, #X " (line %i)", __LINE__); return 0; };
#define TEST_OFFSET(X, N) TEST(offsetof(struct GamutMathApi, X) == (sizeof(size_t) + (sizeof(void *) * (N))));


static PyObject *
test_GamutMathApi_Get(PyObject *self, PyObject *args)
{
    struct GamutMathApi *api = GamutMathApi_Get();
    if (!api){ return 0; }
    TEST(!PyErr_Occurred());

    TEST(offsetof(struct GamutMathApi, version) == 0);
    TEST(api->version == 0);

    TEST_OFFSET(BVector1_GetType, 0);
    TEST_OFFSET(BVector1Array_GetType, 1);
    TEST_OFFSET(BVector1_Create, 2);
    TEST_OFFSET(BVector1Array_Create, 3);
    TEST_OFFSET(BVector1_GetValuePointer, 4);
    TEST_OFFSET(BVector1Array_GetValuePointer, 5);
    TEST_OFFSET(BVector1Array_GetLength, 6);

    TEST_OFFSET(DVector1_GetType, 7);
    TEST_OFFSET(DVector1Array_GetType, 8);
    TEST_OFFSET(DVector1_Create, 9);
    TEST_OFFSET(DVector1Array_Create, 10);
    TEST_OFFSET(DVector1_GetValuePointer, 11);
    TEST_OFFSET(DVector1Array_GetValuePointer, 12);
    TEST_OFFSET(DVector1Array_GetLength, 13);

    TEST_OFFSET(FVector1_GetType, 14);
    TEST_OFFSET(FVector1Array_GetType, 15);
    TEST_OFFSET(FVector1_Create, 16);
    TEST_OFFSET(FVector1Array_Create, 17);
    TEST_OFFSET(FVector1_GetValuePointer, 18);
    TEST_OFFSET(FVector1Array_GetValuePointer, 19);
    TEST_OFFSET(FVector1Array_GetLength, 20);

    TEST_OFFSET(I8Vector1_GetType, 21);
    TEST_OFFSET(I8Vector1Array_GetType, 22);
    TEST_OFFSET(I8Vector1_Create, 23);
    TEST_OFFSET(I8Vector1Array_Create, 24);
    TEST_OFFSET(I8Vector1_GetValuePointer, 25);
    TEST_OFFSET(I8Vector1Array_GetValuePointer, 26);
    TEST_OFFSET(I8Vector1Array_GetLength, 27);

    TEST_OFFSET(U8Vector1_GetType, 28);
    TEST_OFFSET(U8Vector1Array_GetType, 29);
    TEST_OFFSET(U8Vector1_Create, 30);
    TEST_OFFSET(U8Vector1Array_Create, 31);
    TEST_OFFSET(U8Vector1_GetValuePointer, 32);
    TEST_OFFSET(U8Vector1Array_GetValuePointer, 33);
    TEST_OFFSET(U8Vector1Array_GetLength, 34);

    TEST_OFFSET(I16Vector1_GetType, 35);
    TEST_OFFSET(I16Vector1Array_GetType, 36);
    TEST_OFFSET(I16Vector1_Create, 37);
    TEST_OFFSET(I16Vector1Array_Create, 38);
    TEST_OFFSET(I16Vector1_GetValuePointer, 39);
    TEST_OFFSET(I16Vector1Array_GetValuePointer, 40);
    TEST_OFFSET(I16Vector1Array_GetLength, 41);

    TEST_OFFSET(U16Vector1_GetType, 42);
    TEST_OFFSET(U16Vector1Array_GetType, 43);
    TEST_OFFSET(U16Vector1_Create, 44);
    TEST_OFFSET(U16Vector1Array_Create, 45);
    TEST_OFFSET(U16Vector1_GetValuePointer, 46);
    TEST_OFFSET(U16Vector1Array_GetValuePointer, 47);
    TEST_OFFSET(U16Vector1Array_GetLength, 48);

    TEST_OFFSET(I32Vector1_GetType, 49);
    TEST_OFFSET(I32Vector1Array_GetType, 50);
    TEST_OFFSET(I32Vector1_Create, 51);
    TEST_OFFSET(I32Vector1Array_Create, 52);
    TEST_OFFSET(I32Vector1_GetValuePointer, 53);
    TEST_OFFSET(I32Vector1Array_GetValuePointer, 54);
    TEST_OFFSET(I32Vector1Array_GetLength, 55);

    TEST_OFFSET(U32Vector1_GetType, 56);
    TEST_OFFSET(U32Vector1Array_GetType, 57);
    TEST_OFFSET(U32Vector1_Create, 58);
    TEST_OFFSET(U32Vector1Array_Create, 59);
    TEST_OFFSET(U32Vector1_GetValuePointer, 60);
    TEST_OFFSET(U32Vector1Array_GetValuePointer, 61);
    TEST_OFFSET(U32Vector1Array_GetLength, 62);

    TEST_OFFSET(IVector1_GetType, 63);
    TEST_OFFSET(IVector1Array_GetType, 64);
    TEST_OFFSET(IVector1_Create, 65);
    TEST_OFFSET(IVector1Array_Create, 66);
    TEST_OFFSET(IVector1_GetValuePointer, 67);
    TEST_OFFSET(IVector1Array_GetValuePointer, 68);
    TEST_OFFSET(IVector1Array_GetLength, 69);

    TEST_OFFSET(UVector1_GetType, 70);
    TEST_OFFSET(UVector1Array_GetType, 71);
    TEST_OFFSET(UVector1_Create, 72);
    TEST_OFFSET(UVector1Array_Create, 73);
    TEST_OFFSET(UVector1_GetValuePointer, 74);
    TEST_OFFSET(UVector1Array_GetValuePointer, 75);
    TEST_OFFSET(UVector1Array_GetLength, 76);

    TEST_OFFSET(I64Vector1_GetType, 77);
    TEST_OFFSET(I64Vector1Array_GetType, 78);
    TEST_OFFSET(I64Vector1_Create, 79);
    TEST_OFFSET(I64Vector1Array_Create, 80);
    TEST_OFFSET(I64Vector1_GetValuePointer, 81);
    TEST_OFFSET(I64Vector1Array_GetValuePointer, 82);
    TEST_OFFSET(I64Vector1Array_GetLength, 83);

    TEST_OFFSET(U64Vector1_GetType, 84);
    TEST_OFFSET(U64Vector1Array_GetType, 85);
    TEST_OFFSET(U64Vector1_Create, 86);
    TEST_OFFSET(U64Vector1Array_Create, 87);
    TEST_OFFSET(U64Vector1_GetValuePointer, 88);
    TEST_OFFSET(U64Vector1Array_GetValuePointer, 89);
    TEST_OFFSET(U64Vector1Array_GetLength, 90);

    TEST_OFFSET(BVector2_GetType, 91);
    TEST_OFFSET(BVector2Array_GetType, 92);
    TEST_OFFSET(BVector2_Create, 93);
    TEST_OFFSET(BVector2Array_Create, 94);
    TEST_OFFSET(BVector2_GetValuePointer, 95);
    TEST_OFFSET(BVector2Array_GetValuePointer, 96);
    TEST_OFFSET(BVector2Array_GetLength, 97);

    TEST_OFFSET(DVector2_GetType, 98);
    TEST_OFFSET(DVector2Array_GetType, 99);
    TEST_OFFSET(DVector2_Create, 100);
    TEST_OFFSET(DVector2Array_Create, 101);
    TEST_OFFSET(DVector2_GetValuePointer, 102);
    TEST_OFFSET(DVector2Array_GetValuePointer, 103);
    TEST_OFFSET(DVector2Array_GetLength, 104);

    TEST_OFFSET(FVector2_GetType, 105);
    TEST_OFFSET(FVector2Array_GetType, 106);
    TEST_OFFSET(FVector2_Create, 107);
    TEST_OFFSET(FVector2Array_Create, 108);
    TEST_OFFSET(FVector2_GetValuePointer, 109);
    TEST_OFFSET(FVector2Array_GetValuePointer, 110);
    TEST_OFFSET(FVector2Array_GetLength, 111);

    TEST_OFFSET(I8Vector2_GetType, 112);
    TEST_OFFSET(I8Vector2Array_GetType, 113);
    TEST_OFFSET(I8Vector2_Create, 114);
    TEST_OFFSET(I8Vector2Array_Create, 115);
    TEST_OFFSET(I8Vector2_GetValuePointer, 116);
    TEST_OFFSET(I8Vector2Array_GetValuePointer, 117);
    TEST_OFFSET(I8Vector2Array_GetLength, 118);

    TEST_OFFSET(U8Vector2_GetType, 119);
    TEST_OFFSET(U8Vector2Array_GetType, 120);
    TEST_OFFSET(U8Vector2_Create, 121);
    TEST_OFFSET(U8Vector2Array_Create, 122);
    TEST_OFFSET(U8Vector2_GetValuePointer, 123);
    TEST_OFFSET(U8Vector2Array_GetValuePointer, 124);
    TEST_OFFSET(U8Vector2Array_GetLength, 125);

    TEST_OFFSET(I16Vector2_GetType, 126);
    TEST_OFFSET(I16Vector2Array_GetType, 127);
    TEST_OFFSET(I16Vector2_Create, 128);
    TEST_OFFSET(I16Vector2Array_Create, 129);
    TEST_OFFSET(I16Vector2_GetValuePointer, 130);
    TEST_OFFSET(I16Vector2Array_GetValuePointer, 131);
    TEST_OFFSET(I16Vector2Array_GetLength, 132);

    TEST_OFFSET(U16Vector2_GetType, 133);
    TEST_OFFSET(U16Vector2Array_GetType, 134);
    TEST_OFFSET(U16Vector2_Create, 135);
    TEST_OFFSET(U16Vector2Array_Create, 136);
    TEST_OFFSET(U16Vector2_GetValuePointer, 137);
    TEST_OFFSET(U16Vector2Array_GetValuePointer, 138);
    TEST_OFFSET(U16Vector2Array_GetLength, 139);

    TEST_OFFSET(I32Vector2_GetType, 140);
    TEST_OFFSET(I32Vector2Array_GetType, 141);
    TEST_OFFSET(I32Vector2_Create, 142);
    TEST_OFFSET(I32Vector2Array_Create, 143);
    TEST_OFFSET(I32Vector2_GetValuePointer, 144);
    TEST_OFFSET(I32Vector2Array_GetValuePointer, 145);
    TEST_OFFSET(I32Vector2Array_GetLength, 146);

    TEST_OFFSET(U32Vector2_GetType, 147);
    TEST_OFFSET(U32Vector2Array_GetType, 148);
    TEST_OFFSET(U32Vector2_Create, 149);
    TEST_OFFSET(U32Vector2Array_Create, 150);
    TEST_OFFSET(U32Vector2_GetValuePointer, 151);
    TEST_OFFSET(U32Vector2Array_GetValuePointer, 152);
    TEST_OFFSET(U32Vector2Array_GetLength, 153);

    TEST_OFFSET(IVector2_GetType, 154);
    TEST_OFFSET(IVector2Array_GetType, 155);
    TEST_OFFSET(IVector2_Create, 156);
    TEST_OFFSET(IVector2Array_Create, 157);
    TEST_OFFSET(IVector2_GetValuePointer, 158);
    TEST_OFFSET(IVector2Array_GetValuePointer, 159);
    TEST_OFFSET(IVector2Array_GetLength, 160);

    TEST_OFFSET(UVector2_GetType, 161);
    TEST_OFFSET(UVector2Array_GetType, 162);
    TEST_OFFSET(UVector2_Create, 163);
    TEST_OFFSET(UVector2Array_Create, 164);
    TEST_OFFSET(UVector2_GetValuePointer, 165);
    TEST_OFFSET(UVector2Array_GetValuePointer, 166);
    TEST_OFFSET(UVector2Array_GetLength, 167);

    TEST_OFFSET(I64Vector2_GetType, 168);
    TEST_OFFSET(I64Vector2Array_GetType, 169);
    TEST_OFFSET(I64Vector2_Create, 170);
    TEST_OFFSET(I64Vector2Array_Create, 171);
    TEST_OFFSET(I64Vector2_GetValuePointer, 172);
    TEST_OFFSET(I64Vector2Array_GetValuePointer, 173);
    TEST_OFFSET(I64Vector2Array_GetLength, 174);

    TEST_OFFSET(U64Vector2_GetType, 175);
    TEST_OFFSET(U64Vector2Array_GetType, 176);
    TEST_OFFSET(U64Vector2_Create, 177);
    TEST_OFFSET(U64Vector2Array_Create, 178);
    TEST_OFFSET(U64Vector2_GetValuePointer, 179);
    TEST_OFFSET(U64Vector2Array_GetValuePointer, 180);
    TEST_OFFSET(U64Vector2Array_GetLength, 181);

    TEST_OFFSET(BVector3_GetType, 182);
    TEST_OFFSET(BVector3Array_GetType, 183);
    TEST_OFFSET(BVector3_Create, 184);
    TEST_OFFSET(BVector3Array_Create, 185);
    TEST_OFFSET(BVector3_GetValuePointer, 186);
    TEST_OFFSET(BVector3Array_GetValuePointer, 187);
    TEST_OFFSET(BVector3Array_GetLength, 188);

    TEST_OFFSET(DVector3_GetType, 189);
    TEST_OFFSET(DVector3Array_GetType, 190);
    TEST_OFFSET(DVector3_Create, 191);
    TEST_OFFSET(DVector3Array_Create, 192);
    TEST_OFFSET(DVector3_GetValuePointer, 193);
    TEST_OFFSET(DVector3Array_GetValuePointer, 194);
    TEST_OFFSET(DVector3Array_GetLength, 195);

    TEST_OFFSET(FVector3_GetType, 196);
    TEST_OFFSET(FVector3Array_GetType, 197);
    TEST_OFFSET(FVector3_Create, 198);
    TEST_OFFSET(FVector3Array_Create, 199);
    TEST_OFFSET(FVector3_GetValuePointer, 200);
    TEST_OFFSET(FVector3Array_GetValuePointer, 201);
    TEST_OFFSET(FVector3Array_GetLength, 202);

    TEST_OFFSET(I8Vector3_GetType, 203);
    TEST_OFFSET(I8Vector3Array_GetType, 204);
    TEST_OFFSET(I8Vector3_Create, 205);
    TEST_OFFSET(I8Vector3Array_Create, 206);
    TEST_OFFSET(I8Vector3_GetValuePointer, 207);
    TEST_OFFSET(I8Vector3Array_GetValuePointer, 208);
    TEST_OFFSET(I8Vector3Array_GetLength, 209);

    TEST_OFFSET(U8Vector3_GetType, 210);
    TEST_OFFSET(U8Vector3Array_GetType, 211);
    TEST_OFFSET(U8Vector3_Create, 212);
    TEST_OFFSET(U8Vector3Array_Create, 213);
    TEST_OFFSET(U8Vector3_GetValuePointer, 214);
    TEST_OFFSET(U8Vector3Array_GetValuePointer, 215);
    TEST_OFFSET(U8Vector3Array_GetLength, 216);

    TEST_OFFSET(I16Vector3_GetType, 217);
    TEST_OFFSET(I16Vector3Array_GetType, 218);
    TEST_OFFSET(I16Vector3_Create, 219);
    TEST_OFFSET(I16Vector3Array_Create, 220);
    TEST_OFFSET(I16Vector3_GetValuePointer, 221);
    TEST_OFFSET(I16Vector3Array_GetValuePointer, 222);
    TEST_OFFSET(I16Vector3Array_GetLength, 223);

    TEST_OFFSET(U16Vector3_GetType, 224);
    TEST_OFFSET(U16Vector3Array_GetType, 225);
    TEST_OFFSET(U16Vector3_Create, 226);
    TEST_OFFSET(U16Vector3Array_Create, 227);
    TEST_OFFSET(U16Vector3_GetValuePointer, 228);
    TEST_OFFSET(U16Vector3Array_GetValuePointer, 229);
    TEST_OFFSET(U16Vector3Array_GetLength, 230);

    TEST_OFFSET(I32Vector3_GetType, 231);
    TEST_OFFSET(I32Vector3Array_GetType, 232);
    TEST_OFFSET(I32Vector3_Create, 233);
    TEST_OFFSET(I32Vector3Array_Create, 234);
    TEST_OFFSET(I32Vector3_GetValuePointer, 235);
    TEST_OFFSET(I32Vector3Array_GetValuePointer, 236);
    TEST_OFFSET(I32Vector3Array_GetLength, 237);

    TEST_OFFSET(U32Vector3_GetType, 238);
    TEST_OFFSET(U32Vector3Array_GetType, 239);
    TEST_OFFSET(U32Vector3_Create, 240);
    TEST_OFFSET(U32Vector3Array_Create, 241);
    TEST_OFFSET(U32Vector3_GetValuePointer, 242);
    TEST_OFFSET(U32Vector3Array_GetValuePointer, 243);
    TEST_OFFSET(U32Vector3Array_GetLength, 244);

    TEST_OFFSET(IVector3_GetType, 245);
    TEST_OFFSET(IVector3Array_GetType, 246);
    TEST_OFFSET(IVector3_Create, 247);
    TEST_OFFSET(IVector3Array_Create, 248);
    TEST_OFFSET(IVector3_GetValuePointer, 249);
    TEST_OFFSET(IVector3Array_GetValuePointer, 250);
    TEST_OFFSET(IVector3Array_GetLength, 251);

    TEST_OFFSET(UVector3_GetType, 252);
    TEST_OFFSET(UVector3Array_GetType, 253);
    TEST_OFFSET(UVector3_Create, 254);
    TEST_OFFSET(UVector3Array_Create, 255);
    TEST_OFFSET(UVector3_GetValuePointer, 256);
    TEST_OFFSET(UVector3Array_GetValuePointer, 257);
    TEST_OFFSET(UVector3Array_GetLength, 258);

    TEST_OFFSET(I64Vector3_GetType, 259);
    TEST_OFFSET(I64Vector3Array_GetType, 260);
    TEST_OFFSET(I64Vector3_Create, 261);
    TEST_OFFSET(I64Vector3Array_Create, 262);
    TEST_OFFSET(I64Vector3_GetValuePointer, 263);
    TEST_OFFSET(I64Vector3Array_GetValuePointer, 264);
    TEST_OFFSET(I64Vector3Array_GetLength, 265);

    TEST_OFFSET(U64Vector3_GetType, 266);
    TEST_OFFSET(U64Vector3Array_GetType, 267);
    TEST_OFFSET(U64Vector3_Create, 268);
    TEST_OFFSET(U64Vector3Array_Create, 269);
    TEST_OFFSET(U64Vector3_GetValuePointer, 270);
    TEST_OFFSET(U64Vector3Array_GetValuePointer, 271);
    TEST_OFFSET(U64Vector3Array_GetLength, 272);

    TEST_OFFSET(BVector4_GetType, 273);
    TEST_OFFSET(BVector4Array_GetType, 274);
    TEST_OFFSET(BVector4_Create, 275);
    TEST_OFFSET(BVector4Array_Create, 276);
    TEST_OFFSET(BVector4_GetValuePointer, 277);
    TEST_OFFSET(BVector4Array_GetValuePointer, 278);
    TEST_OFFSET(BVector4Array_GetLength, 279);

    TEST_OFFSET(DVector4_GetType, 280);
    TEST_OFFSET(DVector4Array_GetType, 281);
    TEST_OFFSET(DVector4_Create, 282);
    TEST_OFFSET(DVector4Array_Create, 283);
    TEST_OFFSET(DVector4_GetValuePointer, 284);
    TEST_OFFSET(DVector4Array_GetValuePointer, 285);
    TEST_OFFSET(DVector4Array_GetLength, 286);

    TEST_OFFSET(FVector4_GetType, 287);
    TEST_OFFSET(FVector4Array_GetType, 288);
    TEST_OFFSET(FVector4_Create, 289);
    TEST_OFFSET(FVector4Array_Create, 290);
    TEST_OFFSET(FVector4_GetValuePointer, 291);
    TEST_OFFSET(FVector4Array_GetValuePointer, 292);
    TEST_OFFSET(FVector4Array_GetLength, 293);

    TEST_OFFSET(I8Vector4_GetType, 294);
    TEST_OFFSET(I8Vector4Array_GetType, 295);
    TEST_OFFSET(I8Vector4_Create, 296);
    TEST_OFFSET(I8Vector4Array_Create, 297);
    TEST_OFFSET(I8Vector4_GetValuePointer, 298);
    TEST_OFFSET(I8Vector4Array_GetValuePointer, 299);
    TEST_OFFSET(I8Vector4Array_GetLength, 300);

    TEST_OFFSET(U8Vector4_GetType, 301);
    TEST_OFFSET(U8Vector4Array_GetType, 302);
    TEST_OFFSET(U8Vector4_Create, 303);
    TEST_OFFSET(U8Vector4Array_Create, 304);
    TEST_OFFSET(U8Vector4_GetValuePointer, 305);
    TEST_OFFSET(U8Vector4Array_GetValuePointer, 306);
    TEST_OFFSET(U8Vector4Array_GetLength, 307);

    TEST_OFFSET(I16Vector4_GetType, 308);
    TEST_OFFSET(I16Vector4Array_GetType, 309);
    TEST_OFFSET(I16Vector4_Create, 310);
    TEST_OFFSET(I16Vector4Array_Create, 311);
    TEST_OFFSET(I16Vector4_GetValuePointer, 312);
    TEST_OFFSET(I16Vector4Array_GetValuePointer, 313);
    TEST_OFFSET(I16Vector4Array_GetLength, 314);

    TEST_OFFSET(U16Vector4_GetType, 315);
    TEST_OFFSET(U16Vector4Array_GetType, 316);
    TEST_OFFSET(U16Vector4_Create, 317);
    TEST_OFFSET(U16Vector4Array_Create, 318);
    TEST_OFFSET(U16Vector4_GetValuePointer, 319);
    TEST_OFFSET(U16Vector4Array_GetValuePointer, 320);
    TEST_OFFSET(U16Vector4Array_GetLength, 321);

    TEST_OFFSET(I32Vector4_GetType, 322);
    TEST_OFFSET(I32Vector4Array_GetType, 323);
    TEST_OFFSET(I32Vector4_Create, 324);
    TEST_OFFSET(I32Vector4Array_Create, 325);
    TEST_OFFSET(I32Vector4_GetValuePointer, 326);
    TEST_OFFSET(I32Vector4Array_GetValuePointer, 327);
    TEST_OFFSET(I32Vector4Array_GetLength, 328);

    TEST_OFFSET(U32Vector4_GetType, 329);
    TEST_OFFSET(U32Vector4Array_GetType, 330);
    TEST_OFFSET(U32Vector4_Create, 331);
    TEST_OFFSET(U32Vector4Array_Create, 332);
    TEST_OFFSET(U32Vector4_GetValuePointer, 333);
    TEST_OFFSET(U32Vector4Array_GetValuePointer, 334);
    TEST_OFFSET(U32Vector4Array_GetLength, 335);

    TEST_OFFSET(IVector4_GetType, 336);
    TEST_OFFSET(IVector4Array_GetType, 337);
    TEST_OFFSET(IVector4_Create, 338);
    TEST_OFFSET(IVector4Array_Create, 339);
    TEST_OFFSET(IVector4_GetValuePointer, 340);
    TEST_OFFSET(IVector4Array_GetValuePointer, 341);
    TEST_OFFSET(IVector4Array_GetLength, 342);

    TEST_OFFSET(UVector4_GetType, 343);
    TEST_OFFSET(UVector4Array_GetType, 344);
    TEST_OFFSET(UVector4_Create, 345);
    TEST_OFFSET(UVector4Array_Create, 346);
    TEST_OFFSET(UVector4_GetValuePointer, 347);
    TEST_OFFSET(UVector4Array_GetValuePointer, 348);
    TEST_OFFSET(UVector4Array_GetLength, 349);

    TEST_OFFSET(I64Vector4_GetType, 350);
    TEST_OFFSET(I64Vector4Array_GetType, 351);
    TEST_OFFSET(I64Vector4_Create, 352);
    TEST_OFFSET(I64Vector4Array_Create, 353);
    TEST_OFFSET(I64Vector4_GetValuePointer, 354);
    TEST_OFFSET(I64Vector4Array_GetValuePointer, 355);
    TEST_OFFSET(I64Vector4Array_GetLength, 356);

    TEST_OFFSET(U64Vector4_GetType, 357);
    TEST_OFFSET(U64Vector4Array_GetType, 358);
    TEST_OFFSET(U64Vector4_Create, 359);
    TEST_OFFSET(U64Vector4Array_Create, 360);
    TEST_OFFSET(U64Vector4_GetValuePointer, 361);
    TEST_OFFSET(U64Vector4Array_GetValuePointer, 362);
    TEST_OFFSET(U64Vector4Array_GetLength, 363);

    TEST_OFFSET(DMatrix2x2_GetType, 364);
    TEST_OFFSET(DMatrix2x2Array_GetType, 365);
    TEST_OFFSET(DMatrix2x2_Create, 366);
    TEST_OFFSET(DMatrix2x2Array_Create, 367);
    TEST_OFFSET(DMatrix2x2_GetValuePointer, 368);
    TEST_OFFSET(DMatrix2x2Array_GetValuePointer, 369);
    TEST_OFFSET(DMatrix2x2Array_GetLength, 370);

    TEST_OFFSET(FMatrix2x2_GetType, 371);
    TEST_OFFSET(FMatrix2x2Array_GetType, 372);
    TEST_OFFSET(FMatrix2x2_Create, 373);
    TEST_OFFSET(FMatrix2x2Array_Create, 374);
    TEST_OFFSET(FMatrix2x2_GetValuePointer, 375);
    TEST_OFFSET(FMatrix2x2Array_GetValuePointer, 376);
    TEST_OFFSET(FMatrix2x2Array_GetLength, 377);

    TEST_OFFSET(DMatrix2x3_GetType, 378);
    TEST_OFFSET(DMatrix2x3Array_GetType, 379);
    TEST_OFFSET(DMatrix2x3_Create, 380);
    TEST_OFFSET(DMatrix2x3Array_Create, 381);
    TEST_OFFSET(DMatrix2x3_GetValuePointer, 382);
    TEST_OFFSET(DMatrix2x3Array_GetValuePointer, 383);
    TEST_OFFSET(DMatrix2x3Array_GetLength, 384);

    TEST_OFFSET(FMatrix2x3_GetType, 385);
    TEST_OFFSET(FMatrix2x3Array_GetType, 386);
    TEST_OFFSET(FMatrix2x3_Create, 387);
    TEST_OFFSET(FMatrix2x3Array_Create, 388);
    TEST_OFFSET(FMatrix2x3_GetValuePointer, 389);
    TEST_OFFSET(FMatrix2x3Array_GetValuePointer, 390);
    TEST_OFFSET(FMatrix2x3Array_GetLength, 391);

    TEST_OFFSET(DMatrix2x4_GetType, 392);
    TEST_OFFSET(DMatrix2x4Array_GetType, 393);
    TEST_OFFSET(DMatrix2x4_Create, 394);
    TEST_OFFSET(DMatrix2x4Array_Create, 395);
    TEST_OFFSET(DMatrix2x4_GetValuePointer, 396);
    TEST_OFFSET(DMatrix2x4Array_GetValuePointer, 397);
    TEST_OFFSET(DMatrix2x4Array_GetLength, 398);

    TEST_OFFSET(FMatrix2x4_GetType, 399);
    TEST_OFFSET(FMatrix2x4Array_GetType, 400);
    TEST_OFFSET(FMatrix2x4_Create, 401);
    TEST_OFFSET(FMatrix2x4Array_Create, 402);
    TEST_OFFSET(FMatrix2x4_GetValuePointer, 403);
    TEST_OFFSET(FMatrix2x4Array_GetValuePointer, 404);
    TEST_OFFSET(FMatrix2x4Array_GetLength, 405);

    TEST_OFFSET(DMatrix3x2_GetType, 406);
    TEST_OFFSET(DMatrix3x2Array_GetType, 407);
    TEST_OFFSET(DMatrix3x2_Create, 408);
    TEST_OFFSET(DMatrix3x2Array_Create, 409);
    TEST_OFFSET(DMatrix3x2_GetValuePointer, 410);
    TEST_OFFSET(DMatrix3x2Array_GetValuePointer, 411);
    TEST_OFFSET(DMatrix3x2Array_GetLength, 412);

    TEST_OFFSET(FMatrix3x2_GetType, 413);
    TEST_OFFSET(FMatrix3x2Array_GetType, 414);
    TEST_OFFSET(FMatrix3x2_Create, 415);
    TEST_OFFSET(FMatrix3x2Array_Create, 416);
    TEST_OFFSET(FMatrix3x2_GetValuePointer, 417);
    TEST_OFFSET(FMatrix3x2Array_GetValuePointer, 418);
    TEST_OFFSET(FMatrix3x2Array_GetLength, 419);

    TEST_OFFSET(DMatrix3x3_GetType, 420);
    TEST_OFFSET(DMatrix3x3Array_GetType, 421);
    TEST_OFFSET(DMatrix3x3_Create, 422);
    TEST_OFFSET(DMatrix3x3Array_Create, 423);
    TEST_OFFSET(DMatrix3x3_GetValuePointer, 424);
    TEST_OFFSET(DMatrix3x3Array_GetValuePointer, 425);
    TEST_OFFSET(DMatrix3x3Array_GetLength, 426);

    TEST_OFFSET(FMatrix3x3_GetType, 427);
    TEST_OFFSET(FMatrix3x3Array_GetType, 428);
    TEST_OFFSET(FMatrix3x3_Create, 429);
    TEST_OFFSET(FMatrix3x3Array_Create, 430);
    TEST_OFFSET(FMatrix3x3_GetValuePointer, 431);
    TEST_OFFSET(FMatrix3x3Array_GetValuePointer, 432);
    TEST_OFFSET(FMatrix3x3Array_GetLength, 433);

    TEST_OFFSET(DMatrix3x4_GetType, 434);
    TEST_OFFSET(DMatrix3x4Array_GetType, 435);
    TEST_OFFSET(DMatrix3x4_Create, 436);
    TEST_OFFSET(DMatrix3x4Array_Create, 437);
    TEST_OFFSET(DMatrix3x4_GetValuePointer, 438);
    TEST_OFFSET(DMatrix3x4Array_GetValuePointer, 439);
    TEST_OFFSET(DMatrix3x4Array_GetLength, 440);

    TEST_OFFSET(FMatrix3x4_GetType, 441);
    TEST_OFFSET(FMatrix3x4Array_GetType, 442);
    TEST_OFFSET(FMatrix3x4_Create, 443);
    TEST_OFFSET(FMatrix3x4Array_Create, 444);
    TEST_OFFSET(FMatrix3x4_GetValuePointer, 445);
    TEST_OFFSET(FMatrix3x4Array_GetValuePointer, 446);
    TEST_OFFSET(FMatrix3x4Array_GetLength, 447);

    TEST_OFFSET(DMatrix4x2_GetType, 448);
    TEST_OFFSET(DMatrix4x2Array_GetType, 449);
    TEST_OFFSET(DMatrix4x2_Create, 450);
    TEST_OFFSET(DMatrix4x2Array_Create, 451);
    TEST_OFFSET(DMatrix4x2_GetValuePointer, 452);
    TEST_OFFSET(DMatrix4x2Array_GetValuePointer, 453);
    TEST_OFFSET(DMatrix4x2Array_GetLength, 454);

    TEST_OFFSET(FMatrix4x2_GetType, 455);
    TEST_OFFSET(FMatrix4x2Array_GetType, 456);
    TEST_OFFSET(FMatrix4x2_Create, 457);
    TEST_OFFSET(FMatrix4x2Array_Create, 458);
    TEST_OFFSET(FMatrix4x2_GetValuePointer, 459);
    TEST_OFFSET(FMatrix4x2Array_GetValuePointer, 460);
    TEST_OFFSET(FMatrix4x2Array_GetLength, 461);

    TEST_OFFSET(DMatrix4x3_GetType, 462);
    TEST_OFFSET(DMatrix4x3Array_GetType, 463);
    TEST_OFFSET(DMatrix4x3_Create, 464);
    TEST_OFFSET(DMatrix4x3Array_Create, 465);
    TEST_OFFSET(DMatrix4x3_GetValuePointer, 466);
    TEST_OFFSET(DMatrix4x3Array_GetValuePointer, 467);
    TEST_OFFSET(DMatrix4x3Array_GetLength, 468);

    TEST_OFFSET(FMatrix4x3_GetType, 469);
    TEST_OFFSET(FMatrix4x3Array_GetType, 470);
    TEST_OFFSET(FMatrix4x3_Create, 471);
    TEST_OFFSET(FMatrix4x3Array_Create, 472);
    TEST_OFFSET(FMatrix4x3_GetValuePointer, 473);
    TEST_OFFSET(FMatrix4x3Array_GetValuePointer, 474);
    TEST_OFFSET(FMatrix4x3Array_GetLength, 475);

    TEST_OFFSET(DMatrix4x4_GetType, 476);
    TEST_OFFSET(DMatrix4x4Array_GetType, 477);
    TEST_OFFSET(DMatrix4x4_Create, 478);
    TEST_OFFSET(DMatrix4x4Array_Create, 479);
    TEST_OFFSET(DMatrix4x4_GetValuePointer, 480);
    TEST_OFFSET(DMatrix4x4Array_GetValuePointer, 481);
    TEST_OFFSET(DMatrix4x4Array_GetLength, 482);

    TEST_OFFSET(FMatrix4x4_GetType, 483);
    TEST_OFFSET(FMatrix4x4Array_GetType, 484);
    TEST_OFFSET(FMatrix4x4_Create, 485);
    TEST_OFFSET(FMatrix4x4Array_Create, 486);
    TEST_OFFSET(FMatrix4x4_GetValuePointer, 487);
    TEST_OFFSET(FMatrix4x4Array_GetValuePointer, 488);
    TEST_OFFSET(FMatrix4x4Array_GetLength, 489);

    TEST_OFFSET(DQuaternion_GetType, 490);
    TEST_OFFSET(DQuaternionArray_GetType, 491);
    TEST_OFFSET(DQuaternion_Create, 492);
    TEST_OFFSET(DQuaternionArray_Create, 493);
    TEST_OFFSET(DQuaternion_GetValuePointer, 494);
    TEST_OFFSET(DQuaternionArray_GetValuePointer, 495);
    TEST_OFFSET(DQuaternionArray_GetLength, 496);

    TEST_OFFSET(FQuaternion_GetType, 497);
    TEST_OFFSET(FQuaternionArray_GetType, 498);
    TEST_OFFSET(FQuaternion_Create, 499);
    TEST_OFFSET(FQuaternionArray_Create, 500);
    TEST_OFFSET(FQuaternion_GetValuePointer, 501);
    TEST_OFFSET(FQuaternionArray_GetValuePointer, 502);
    TEST_OFFSET(FQuaternionArray_GetLength, 503);

    TEST_OFFSET(BArray_GetType, 504);
    TEST_OFFSET(BArray_Create, 505);
    TEST_OFFSET(BArray_GetValuePointer, 506);
    TEST_OFFSET(BArray_GetLength, 507);

    TEST_OFFSET(DArray_GetType, 508);
    TEST_OFFSET(DArray_Create, 509);
    TEST_OFFSET(DArray_GetValuePointer, 510);
    TEST_OFFSET(DArray_GetLength, 511);

    TEST_OFFSET(FArray_GetType, 512);
    TEST_OFFSET(FArray_Create, 513);
    TEST_OFFSET(FArray_GetValuePointer, 514);
    TEST_OFFSET(FArray_GetLength, 515);

    TEST_OFFSET(I8Array_GetType, 516);
    TEST_OFFSET(I8Array_Create, 517);
    TEST_OFFSET(I8Array_GetValuePointer, 518);
    TEST_OFFSET(I8Array_GetLength, 519);

    TEST_OFFSET(U8Array_GetType, 520);
    TEST_OFFSET(U8Array_Create, 521);
    TEST_OFFSET(U8Array_GetValuePointer, 522);
    TEST_OFFSET(U8Array_GetLength, 523);

    TEST_OFFSET(I16Array_GetType, 524);
    TEST_OFFSET(I16Array_Create, 525);
    TEST_OFFSET(I16Array_GetValuePointer, 526);
    TEST_OFFSET(I16Array_GetLength, 527);

    TEST_OFFSET(U16Array_GetType, 528);
    TEST_OFFSET(U16Array_Create, 529);
    TEST_OFFSET(U16Array_GetValuePointer, 530);
    TEST_OFFSET(U16Array_GetLength, 531);

    TEST_OFFSET(I32Array_GetType, 532);
    TEST_OFFSET(I32Array_Create, 533);
    TEST_OFFSET(I32Array_GetValuePointer, 534);
    TEST_OFFSET(I32Array_GetLength, 535);

    TEST_OFFSET(U32Array_GetType, 536);
    TEST_OFFSET(U32Array_Create, 537);
    TEST_OFFSET(U32Array_GetValuePointer, 538);
    TEST_OFFSET(U32Array_GetLength, 539);

    TEST_OFFSET(IArray_GetType, 540);
    TEST_OFFSET(IArray_Create, 541);
    TEST_OFFSET(IArray_GetValuePointer, 542);
    TEST_OFFSET(IArray_GetLength, 543);

    TEST_OFFSET(UArray_GetType, 544);
    TEST_OFFSET(UArray_Create, 545);
    TEST_OFFSET(UArray_GetValuePointer, 546);
    TEST_OFFSET(UArray_GetLength, 547);

    TEST_OFFSET(I64Array_GetType, 548);
    TEST_OFFSET(I64Array_Create, 549);
    TEST_OFFSET(I64Array_GetValuePointer, 550);
    TEST_OFFSET(I64Array_GetLength, 551);

    TEST_OFFSET(U64Array_GetType, 552);
    TEST_OFFSET(U64Array_Create, 553);
    TEST_OFFSET(U64Array_GetValuePointer, 554);
    TEST_OFFSET(U64Array_GetLength, 555);



            TEST(api->BVector1_GetType != 0);
            TEST(api->BVector1_Create != 0);
            TEST(api->BVector1_GetValuePointer != 0);

        TEST(api->BVector1Array_Create != 0);
        TEST(api->BVector1Array_GetType != 0);
        TEST(api->BVector1Array_GetValuePointer != 0);
        TEST(api->BVector1Array_GetLength != 0);


            TEST(api->DVector1_GetType != 0);
            TEST(api->DVector1_Create != 0);
            TEST(api->DVector1_GetValuePointer != 0);

        TEST(api->DVector1Array_Create != 0);
        TEST(api->DVector1Array_GetType != 0);
        TEST(api->DVector1Array_GetValuePointer != 0);
        TEST(api->DVector1Array_GetLength != 0);


            TEST(api->FVector1_GetType != 0);
            TEST(api->FVector1_Create != 0);
            TEST(api->FVector1_GetValuePointer != 0);

        TEST(api->FVector1Array_Create != 0);
        TEST(api->FVector1Array_GetType != 0);
        TEST(api->FVector1Array_GetValuePointer != 0);
        TEST(api->FVector1Array_GetLength != 0);


            TEST(api->I8Vector1_GetType != 0);
            TEST(api->I8Vector1_Create != 0);
            TEST(api->I8Vector1_GetValuePointer != 0);

        TEST(api->I8Vector1Array_Create != 0);
        TEST(api->I8Vector1Array_GetType != 0);
        TEST(api->I8Vector1Array_GetValuePointer != 0);
        TEST(api->I8Vector1Array_GetLength != 0);


            TEST(api->U8Vector1_GetType != 0);
            TEST(api->U8Vector1_Create != 0);
            TEST(api->U8Vector1_GetValuePointer != 0);

        TEST(api->U8Vector1Array_Create != 0);
        TEST(api->U8Vector1Array_GetType != 0);
        TEST(api->U8Vector1Array_GetValuePointer != 0);
        TEST(api->U8Vector1Array_GetLength != 0);


            TEST(api->I16Vector1_GetType != 0);
            TEST(api->I16Vector1_Create != 0);
            TEST(api->I16Vector1_GetValuePointer != 0);

        TEST(api->I16Vector1Array_Create != 0);
        TEST(api->I16Vector1Array_GetType != 0);
        TEST(api->I16Vector1Array_GetValuePointer != 0);
        TEST(api->I16Vector1Array_GetLength != 0);


            TEST(api->U16Vector1_GetType != 0);
            TEST(api->U16Vector1_Create != 0);
            TEST(api->U16Vector1_GetValuePointer != 0);

        TEST(api->U16Vector1Array_Create != 0);
        TEST(api->U16Vector1Array_GetType != 0);
        TEST(api->U16Vector1Array_GetValuePointer != 0);
        TEST(api->U16Vector1Array_GetLength != 0);


            TEST(api->I32Vector1_GetType != 0);
            TEST(api->I32Vector1_Create != 0);
            TEST(api->I32Vector1_GetValuePointer != 0);

        TEST(api->I32Vector1Array_Create != 0);
        TEST(api->I32Vector1Array_GetType != 0);
        TEST(api->I32Vector1Array_GetValuePointer != 0);
        TEST(api->I32Vector1Array_GetLength != 0);


            TEST(api->U32Vector1_GetType != 0);
            TEST(api->U32Vector1_Create != 0);
            TEST(api->U32Vector1_GetValuePointer != 0);

        TEST(api->U32Vector1Array_Create != 0);
        TEST(api->U32Vector1Array_GetType != 0);
        TEST(api->U32Vector1Array_GetValuePointer != 0);
        TEST(api->U32Vector1Array_GetLength != 0);


            TEST(api->IVector1_GetType != 0);
            TEST(api->IVector1_Create != 0);
            TEST(api->IVector1_GetValuePointer != 0);

        TEST(api->IVector1Array_Create != 0);
        TEST(api->IVector1Array_GetType != 0);
        TEST(api->IVector1Array_GetValuePointer != 0);
        TEST(api->IVector1Array_GetLength != 0);


            TEST(api->UVector1_GetType != 0);
            TEST(api->UVector1_Create != 0);
            TEST(api->UVector1_GetValuePointer != 0);

        TEST(api->UVector1Array_Create != 0);
        TEST(api->UVector1Array_GetType != 0);
        TEST(api->UVector1Array_GetValuePointer != 0);
        TEST(api->UVector1Array_GetLength != 0);


            TEST(api->I64Vector1_GetType != 0);
            TEST(api->I64Vector1_Create != 0);
            TEST(api->I64Vector1_GetValuePointer != 0);

        TEST(api->I64Vector1Array_Create != 0);
        TEST(api->I64Vector1Array_GetType != 0);
        TEST(api->I64Vector1Array_GetValuePointer != 0);
        TEST(api->I64Vector1Array_GetLength != 0);


            TEST(api->U64Vector1_GetType != 0);
            TEST(api->U64Vector1_Create != 0);
            TEST(api->U64Vector1_GetValuePointer != 0);

        TEST(api->U64Vector1Array_Create != 0);
        TEST(api->U64Vector1Array_GetType != 0);
        TEST(api->U64Vector1Array_GetValuePointer != 0);
        TEST(api->U64Vector1Array_GetLength != 0);


            TEST(api->BVector2_GetType != 0);
            TEST(api->BVector2_Create != 0);
            TEST(api->BVector2_GetValuePointer != 0);

        TEST(api->BVector2Array_Create != 0);
        TEST(api->BVector2Array_GetType != 0);
        TEST(api->BVector2Array_GetValuePointer != 0);
        TEST(api->BVector2Array_GetLength != 0);


            TEST(api->DVector2_GetType != 0);
            TEST(api->DVector2_Create != 0);
            TEST(api->DVector2_GetValuePointer != 0);

        TEST(api->DVector2Array_Create != 0);
        TEST(api->DVector2Array_GetType != 0);
        TEST(api->DVector2Array_GetValuePointer != 0);
        TEST(api->DVector2Array_GetLength != 0);


            TEST(api->FVector2_GetType != 0);
            TEST(api->FVector2_Create != 0);
            TEST(api->FVector2_GetValuePointer != 0);

        TEST(api->FVector2Array_Create != 0);
        TEST(api->FVector2Array_GetType != 0);
        TEST(api->FVector2Array_GetValuePointer != 0);
        TEST(api->FVector2Array_GetLength != 0);


            TEST(api->I8Vector2_GetType != 0);
            TEST(api->I8Vector2_Create != 0);
            TEST(api->I8Vector2_GetValuePointer != 0);

        TEST(api->I8Vector2Array_Create != 0);
        TEST(api->I8Vector2Array_GetType != 0);
        TEST(api->I8Vector2Array_GetValuePointer != 0);
        TEST(api->I8Vector2Array_GetLength != 0);


            TEST(api->U8Vector2_GetType != 0);
            TEST(api->U8Vector2_Create != 0);
            TEST(api->U8Vector2_GetValuePointer != 0);

        TEST(api->U8Vector2Array_Create != 0);
        TEST(api->U8Vector2Array_GetType != 0);
        TEST(api->U8Vector2Array_GetValuePointer != 0);
        TEST(api->U8Vector2Array_GetLength != 0);


            TEST(api->I16Vector2_GetType != 0);
            TEST(api->I16Vector2_Create != 0);
            TEST(api->I16Vector2_GetValuePointer != 0);

        TEST(api->I16Vector2Array_Create != 0);
        TEST(api->I16Vector2Array_GetType != 0);
        TEST(api->I16Vector2Array_GetValuePointer != 0);
        TEST(api->I16Vector2Array_GetLength != 0);


            TEST(api->U16Vector2_GetType != 0);
            TEST(api->U16Vector2_Create != 0);
            TEST(api->U16Vector2_GetValuePointer != 0);

        TEST(api->U16Vector2Array_Create != 0);
        TEST(api->U16Vector2Array_GetType != 0);
        TEST(api->U16Vector2Array_GetValuePointer != 0);
        TEST(api->U16Vector2Array_GetLength != 0);


            TEST(api->I32Vector2_GetType != 0);
            TEST(api->I32Vector2_Create != 0);
            TEST(api->I32Vector2_GetValuePointer != 0);

        TEST(api->I32Vector2Array_Create != 0);
        TEST(api->I32Vector2Array_GetType != 0);
        TEST(api->I32Vector2Array_GetValuePointer != 0);
        TEST(api->I32Vector2Array_GetLength != 0);


            TEST(api->U32Vector2_GetType != 0);
            TEST(api->U32Vector2_Create != 0);
            TEST(api->U32Vector2_GetValuePointer != 0);

        TEST(api->U32Vector2Array_Create != 0);
        TEST(api->U32Vector2Array_GetType != 0);
        TEST(api->U32Vector2Array_GetValuePointer != 0);
        TEST(api->U32Vector2Array_GetLength != 0);


            TEST(api->IVector2_GetType != 0);
            TEST(api->IVector2_Create != 0);
            TEST(api->IVector2_GetValuePointer != 0);

        TEST(api->IVector2Array_Create != 0);
        TEST(api->IVector2Array_GetType != 0);
        TEST(api->IVector2Array_GetValuePointer != 0);
        TEST(api->IVector2Array_GetLength != 0);


            TEST(api->UVector2_GetType != 0);
            TEST(api->UVector2_Create != 0);
            TEST(api->UVector2_GetValuePointer != 0);

        TEST(api->UVector2Array_Create != 0);
        TEST(api->UVector2Array_GetType != 0);
        TEST(api->UVector2Array_GetValuePointer != 0);
        TEST(api->UVector2Array_GetLength != 0);


            TEST(api->I64Vector2_GetType != 0);
            TEST(api->I64Vector2_Create != 0);
            TEST(api->I64Vector2_GetValuePointer != 0);

        TEST(api->I64Vector2Array_Create != 0);
        TEST(api->I64Vector2Array_GetType != 0);
        TEST(api->I64Vector2Array_GetValuePointer != 0);
        TEST(api->I64Vector2Array_GetLength != 0);


            TEST(api->U64Vector2_GetType != 0);
            TEST(api->U64Vector2_Create != 0);
            TEST(api->U64Vector2_GetValuePointer != 0);

        TEST(api->U64Vector2Array_Create != 0);
        TEST(api->U64Vector2Array_GetType != 0);
        TEST(api->U64Vector2Array_GetValuePointer != 0);
        TEST(api->U64Vector2Array_GetLength != 0);


            TEST(api->BVector3_GetType != 0);
            TEST(api->BVector3_Create != 0);
            TEST(api->BVector3_GetValuePointer != 0);

        TEST(api->BVector3Array_Create != 0);
        TEST(api->BVector3Array_GetType != 0);
        TEST(api->BVector3Array_GetValuePointer != 0);
        TEST(api->BVector3Array_GetLength != 0);


            TEST(api->DVector3_GetType != 0);
            TEST(api->DVector3_Create != 0);
            TEST(api->DVector3_GetValuePointer != 0);

        TEST(api->DVector3Array_Create != 0);
        TEST(api->DVector3Array_GetType != 0);
        TEST(api->DVector3Array_GetValuePointer != 0);
        TEST(api->DVector3Array_GetLength != 0);


            TEST(api->FVector3_GetType != 0);
            TEST(api->FVector3_Create != 0);
            TEST(api->FVector3_GetValuePointer != 0);

        TEST(api->FVector3Array_Create != 0);
        TEST(api->FVector3Array_GetType != 0);
        TEST(api->FVector3Array_GetValuePointer != 0);
        TEST(api->FVector3Array_GetLength != 0);


            TEST(api->I8Vector3_GetType != 0);
            TEST(api->I8Vector3_Create != 0);
            TEST(api->I8Vector3_GetValuePointer != 0);

        TEST(api->I8Vector3Array_Create != 0);
        TEST(api->I8Vector3Array_GetType != 0);
        TEST(api->I8Vector3Array_GetValuePointer != 0);
        TEST(api->I8Vector3Array_GetLength != 0);


            TEST(api->U8Vector3_GetType != 0);
            TEST(api->U8Vector3_Create != 0);
            TEST(api->U8Vector3_GetValuePointer != 0);

        TEST(api->U8Vector3Array_Create != 0);
        TEST(api->U8Vector3Array_GetType != 0);
        TEST(api->U8Vector3Array_GetValuePointer != 0);
        TEST(api->U8Vector3Array_GetLength != 0);


            TEST(api->I16Vector3_GetType != 0);
            TEST(api->I16Vector3_Create != 0);
            TEST(api->I16Vector3_GetValuePointer != 0);

        TEST(api->I16Vector3Array_Create != 0);
        TEST(api->I16Vector3Array_GetType != 0);
        TEST(api->I16Vector3Array_GetValuePointer != 0);
        TEST(api->I16Vector3Array_GetLength != 0);


            TEST(api->U16Vector3_GetType != 0);
            TEST(api->U16Vector3_Create != 0);
            TEST(api->U16Vector3_GetValuePointer != 0);

        TEST(api->U16Vector3Array_Create != 0);
        TEST(api->U16Vector3Array_GetType != 0);
        TEST(api->U16Vector3Array_GetValuePointer != 0);
        TEST(api->U16Vector3Array_GetLength != 0);


            TEST(api->I32Vector3_GetType != 0);
            TEST(api->I32Vector3_Create != 0);
            TEST(api->I32Vector3_GetValuePointer != 0);

        TEST(api->I32Vector3Array_Create != 0);
        TEST(api->I32Vector3Array_GetType != 0);
        TEST(api->I32Vector3Array_GetValuePointer != 0);
        TEST(api->I32Vector3Array_GetLength != 0);


            TEST(api->U32Vector3_GetType != 0);
            TEST(api->U32Vector3_Create != 0);
            TEST(api->U32Vector3_GetValuePointer != 0);

        TEST(api->U32Vector3Array_Create != 0);
        TEST(api->U32Vector3Array_GetType != 0);
        TEST(api->U32Vector3Array_GetValuePointer != 0);
        TEST(api->U32Vector3Array_GetLength != 0);


            TEST(api->IVector3_GetType != 0);
            TEST(api->IVector3_Create != 0);
            TEST(api->IVector3_GetValuePointer != 0);

        TEST(api->IVector3Array_Create != 0);
        TEST(api->IVector3Array_GetType != 0);
        TEST(api->IVector3Array_GetValuePointer != 0);
        TEST(api->IVector3Array_GetLength != 0);


            TEST(api->UVector3_GetType != 0);
            TEST(api->UVector3_Create != 0);
            TEST(api->UVector3_GetValuePointer != 0);

        TEST(api->UVector3Array_Create != 0);
        TEST(api->UVector3Array_GetType != 0);
        TEST(api->UVector3Array_GetValuePointer != 0);
        TEST(api->UVector3Array_GetLength != 0);


            TEST(api->I64Vector3_GetType != 0);
            TEST(api->I64Vector3_Create != 0);
            TEST(api->I64Vector3_GetValuePointer != 0);

        TEST(api->I64Vector3Array_Create != 0);
        TEST(api->I64Vector3Array_GetType != 0);
        TEST(api->I64Vector3Array_GetValuePointer != 0);
        TEST(api->I64Vector3Array_GetLength != 0);


            TEST(api->U64Vector3_GetType != 0);
            TEST(api->U64Vector3_Create != 0);
            TEST(api->U64Vector3_GetValuePointer != 0);

        TEST(api->U64Vector3Array_Create != 0);
        TEST(api->U64Vector3Array_GetType != 0);
        TEST(api->U64Vector3Array_GetValuePointer != 0);
        TEST(api->U64Vector3Array_GetLength != 0);


            TEST(api->BVector4_GetType != 0);
            TEST(api->BVector4_Create != 0);
            TEST(api->BVector4_GetValuePointer != 0);

        TEST(api->BVector4Array_Create != 0);
        TEST(api->BVector4Array_GetType != 0);
        TEST(api->BVector4Array_GetValuePointer != 0);
        TEST(api->BVector4Array_GetLength != 0);


            TEST(api->DVector4_GetType != 0);
            TEST(api->DVector4_Create != 0);
            TEST(api->DVector4_GetValuePointer != 0);

        TEST(api->DVector4Array_Create != 0);
        TEST(api->DVector4Array_GetType != 0);
        TEST(api->DVector4Array_GetValuePointer != 0);
        TEST(api->DVector4Array_GetLength != 0);


            TEST(api->FVector4_GetType != 0);
            TEST(api->FVector4_Create != 0);
            TEST(api->FVector4_GetValuePointer != 0);

        TEST(api->FVector4Array_Create != 0);
        TEST(api->FVector4Array_GetType != 0);
        TEST(api->FVector4Array_GetValuePointer != 0);
        TEST(api->FVector4Array_GetLength != 0);


            TEST(api->I8Vector4_GetType != 0);
            TEST(api->I8Vector4_Create != 0);
            TEST(api->I8Vector4_GetValuePointer != 0);

        TEST(api->I8Vector4Array_Create != 0);
        TEST(api->I8Vector4Array_GetType != 0);
        TEST(api->I8Vector4Array_GetValuePointer != 0);
        TEST(api->I8Vector4Array_GetLength != 0);


            TEST(api->U8Vector4_GetType != 0);
            TEST(api->U8Vector4_Create != 0);
            TEST(api->U8Vector4_GetValuePointer != 0);

        TEST(api->U8Vector4Array_Create != 0);
        TEST(api->U8Vector4Array_GetType != 0);
        TEST(api->U8Vector4Array_GetValuePointer != 0);
        TEST(api->U8Vector4Array_GetLength != 0);


            TEST(api->I16Vector4_GetType != 0);
            TEST(api->I16Vector4_Create != 0);
            TEST(api->I16Vector4_GetValuePointer != 0);

        TEST(api->I16Vector4Array_Create != 0);
        TEST(api->I16Vector4Array_GetType != 0);
        TEST(api->I16Vector4Array_GetValuePointer != 0);
        TEST(api->I16Vector4Array_GetLength != 0);


            TEST(api->U16Vector4_GetType != 0);
            TEST(api->U16Vector4_Create != 0);
            TEST(api->U16Vector4_GetValuePointer != 0);

        TEST(api->U16Vector4Array_Create != 0);
        TEST(api->U16Vector4Array_GetType != 0);
        TEST(api->U16Vector4Array_GetValuePointer != 0);
        TEST(api->U16Vector4Array_GetLength != 0);


            TEST(api->I32Vector4_GetType != 0);
            TEST(api->I32Vector4_Create != 0);
            TEST(api->I32Vector4_GetValuePointer != 0);

        TEST(api->I32Vector4Array_Create != 0);
        TEST(api->I32Vector4Array_GetType != 0);
        TEST(api->I32Vector4Array_GetValuePointer != 0);
        TEST(api->I32Vector4Array_GetLength != 0);


            TEST(api->U32Vector4_GetType != 0);
            TEST(api->U32Vector4_Create != 0);
            TEST(api->U32Vector4_GetValuePointer != 0);

        TEST(api->U32Vector4Array_Create != 0);
        TEST(api->U32Vector4Array_GetType != 0);
        TEST(api->U32Vector4Array_GetValuePointer != 0);
        TEST(api->U32Vector4Array_GetLength != 0);


            TEST(api->IVector4_GetType != 0);
            TEST(api->IVector4_Create != 0);
            TEST(api->IVector4_GetValuePointer != 0);

        TEST(api->IVector4Array_Create != 0);
        TEST(api->IVector4Array_GetType != 0);
        TEST(api->IVector4Array_GetValuePointer != 0);
        TEST(api->IVector4Array_GetLength != 0);


            TEST(api->UVector4_GetType != 0);
            TEST(api->UVector4_Create != 0);
            TEST(api->UVector4_GetValuePointer != 0);

        TEST(api->UVector4Array_Create != 0);
        TEST(api->UVector4Array_GetType != 0);
        TEST(api->UVector4Array_GetValuePointer != 0);
        TEST(api->UVector4Array_GetLength != 0);


            TEST(api->I64Vector4_GetType != 0);
            TEST(api->I64Vector4_Create != 0);
            TEST(api->I64Vector4_GetValuePointer != 0);

        TEST(api->I64Vector4Array_Create != 0);
        TEST(api->I64Vector4Array_GetType != 0);
        TEST(api->I64Vector4Array_GetValuePointer != 0);
        TEST(api->I64Vector4Array_GetLength != 0);


            TEST(api->U64Vector4_GetType != 0);
            TEST(api->U64Vector4_Create != 0);
            TEST(api->U64Vector4_GetValuePointer != 0);

        TEST(api->U64Vector4Array_Create != 0);
        TEST(api->U64Vector4Array_GetType != 0);
        TEST(api->U64Vector4Array_GetValuePointer != 0);
        TEST(api->U64Vector4Array_GetLength != 0);


            TEST(api->DMatrix2x2_GetType != 0);
            TEST(api->DMatrix2x2_Create != 0);
            TEST(api->DMatrix2x2_GetValuePointer != 0);

        TEST(api->DMatrix2x2Array_Create != 0);
        TEST(api->DMatrix2x2Array_GetType != 0);
        TEST(api->DMatrix2x2Array_GetValuePointer != 0);
        TEST(api->DMatrix2x2Array_GetLength != 0);


            TEST(api->FMatrix2x2_GetType != 0);
            TEST(api->FMatrix2x2_Create != 0);
            TEST(api->FMatrix2x2_GetValuePointer != 0);

        TEST(api->FMatrix2x2Array_Create != 0);
        TEST(api->FMatrix2x2Array_GetType != 0);
        TEST(api->FMatrix2x2Array_GetValuePointer != 0);
        TEST(api->FMatrix2x2Array_GetLength != 0);


            TEST(api->DMatrix2x3_GetType != 0);
            TEST(api->DMatrix2x3_Create != 0);
            TEST(api->DMatrix2x3_GetValuePointer != 0);

        TEST(api->DMatrix2x3Array_Create != 0);
        TEST(api->DMatrix2x3Array_GetType != 0);
        TEST(api->DMatrix2x3Array_GetValuePointer != 0);
        TEST(api->DMatrix2x3Array_GetLength != 0);


            TEST(api->FMatrix2x3_GetType != 0);
            TEST(api->FMatrix2x3_Create != 0);
            TEST(api->FMatrix2x3_GetValuePointer != 0);

        TEST(api->FMatrix2x3Array_Create != 0);
        TEST(api->FMatrix2x3Array_GetType != 0);
        TEST(api->FMatrix2x3Array_GetValuePointer != 0);
        TEST(api->FMatrix2x3Array_GetLength != 0);


            TEST(api->DMatrix2x4_GetType != 0);
            TEST(api->DMatrix2x4_Create != 0);
            TEST(api->DMatrix2x4_GetValuePointer != 0);

        TEST(api->DMatrix2x4Array_Create != 0);
        TEST(api->DMatrix2x4Array_GetType != 0);
        TEST(api->DMatrix2x4Array_GetValuePointer != 0);
        TEST(api->DMatrix2x4Array_GetLength != 0);


            TEST(api->FMatrix2x4_GetType != 0);
            TEST(api->FMatrix2x4_Create != 0);
            TEST(api->FMatrix2x4_GetValuePointer != 0);

        TEST(api->FMatrix2x4Array_Create != 0);
        TEST(api->FMatrix2x4Array_GetType != 0);
        TEST(api->FMatrix2x4Array_GetValuePointer != 0);
        TEST(api->FMatrix2x4Array_GetLength != 0);


            TEST(api->DMatrix3x2_GetType != 0);
            TEST(api->DMatrix3x2_Create != 0);
            TEST(api->DMatrix3x2_GetValuePointer != 0);

        TEST(api->DMatrix3x2Array_Create != 0);
        TEST(api->DMatrix3x2Array_GetType != 0);
        TEST(api->DMatrix3x2Array_GetValuePointer != 0);
        TEST(api->DMatrix3x2Array_GetLength != 0);


            TEST(api->FMatrix3x2_GetType != 0);
            TEST(api->FMatrix3x2_Create != 0);
            TEST(api->FMatrix3x2_GetValuePointer != 0);

        TEST(api->FMatrix3x2Array_Create != 0);
        TEST(api->FMatrix3x2Array_GetType != 0);
        TEST(api->FMatrix3x2Array_GetValuePointer != 0);
        TEST(api->FMatrix3x2Array_GetLength != 0);


            TEST(api->DMatrix3x3_GetType != 0);
            TEST(api->DMatrix3x3_Create != 0);
            TEST(api->DMatrix3x3_GetValuePointer != 0);

        TEST(api->DMatrix3x3Array_Create != 0);
        TEST(api->DMatrix3x3Array_GetType != 0);
        TEST(api->DMatrix3x3Array_GetValuePointer != 0);
        TEST(api->DMatrix3x3Array_GetLength != 0);


            TEST(api->FMatrix3x3_GetType != 0);
            TEST(api->FMatrix3x3_Create != 0);
            TEST(api->FMatrix3x3_GetValuePointer != 0);

        TEST(api->FMatrix3x3Array_Create != 0);
        TEST(api->FMatrix3x3Array_GetType != 0);
        TEST(api->FMatrix3x3Array_GetValuePointer != 0);
        TEST(api->FMatrix3x3Array_GetLength != 0);


            TEST(api->DMatrix3x4_GetType != 0);
            TEST(api->DMatrix3x4_Create != 0);
            TEST(api->DMatrix3x4_GetValuePointer != 0);

        TEST(api->DMatrix3x4Array_Create != 0);
        TEST(api->DMatrix3x4Array_GetType != 0);
        TEST(api->DMatrix3x4Array_GetValuePointer != 0);
        TEST(api->DMatrix3x4Array_GetLength != 0);


            TEST(api->FMatrix3x4_GetType != 0);
            TEST(api->FMatrix3x4_Create != 0);
            TEST(api->FMatrix3x4_GetValuePointer != 0);

        TEST(api->FMatrix3x4Array_Create != 0);
        TEST(api->FMatrix3x4Array_GetType != 0);
        TEST(api->FMatrix3x4Array_GetValuePointer != 0);
        TEST(api->FMatrix3x4Array_GetLength != 0);


            TEST(api->DMatrix4x2_GetType != 0);
            TEST(api->DMatrix4x2_Create != 0);
            TEST(api->DMatrix4x2_GetValuePointer != 0);

        TEST(api->DMatrix4x2Array_Create != 0);
        TEST(api->DMatrix4x2Array_GetType != 0);
        TEST(api->DMatrix4x2Array_GetValuePointer != 0);
        TEST(api->DMatrix4x2Array_GetLength != 0);


            TEST(api->FMatrix4x2_GetType != 0);
            TEST(api->FMatrix4x2_Create != 0);
            TEST(api->FMatrix4x2_GetValuePointer != 0);

        TEST(api->FMatrix4x2Array_Create != 0);
        TEST(api->FMatrix4x2Array_GetType != 0);
        TEST(api->FMatrix4x2Array_GetValuePointer != 0);
        TEST(api->FMatrix4x2Array_GetLength != 0);


            TEST(api->DMatrix4x3_GetType != 0);
            TEST(api->DMatrix4x3_Create != 0);
            TEST(api->DMatrix4x3_GetValuePointer != 0);

        TEST(api->DMatrix4x3Array_Create != 0);
        TEST(api->DMatrix4x3Array_GetType != 0);
        TEST(api->DMatrix4x3Array_GetValuePointer != 0);
        TEST(api->DMatrix4x3Array_GetLength != 0);


            TEST(api->FMatrix4x3_GetType != 0);
            TEST(api->FMatrix4x3_Create != 0);
            TEST(api->FMatrix4x3_GetValuePointer != 0);

        TEST(api->FMatrix4x3Array_Create != 0);
        TEST(api->FMatrix4x3Array_GetType != 0);
        TEST(api->FMatrix4x3Array_GetValuePointer != 0);
        TEST(api->FMatrix4x3Array_GetLength != 0);


            TEST(api->DMatrix4x4_GetType != 0);
            TEST(api->DMatrix4x4_Create != 0);
            TEST(api->DMatrix4x4_GetValuePointer != 0);

        TEST(api->DMatrix4x4Array_Create != 0);
        TEST(api->DMatrix4x4Array_GetType != 0);
        TEST(api->DMatrix4x4Array_GetValuePointer != 0);
        TEST(api->DMatrix4x4Array_GetLength != 0);


            TEST(api->FMatrix4x4_GetType != 0);
            TEST(api->FMatrix4x4_Create != 0);
            TEST(api->FMatrix4x4_GetValuePointer != 0);

        TEST(api->FMatrix4x4Array_Create != 0);
        TEST(api->FMatrix4x4Array_GetType != 0);
        TEST(api->FMatrix4x4Array_GetValuePointer != 0);
        TEST(api->FMatrix4x4Array_GetLength != 0);


            TEST(api->DQuaternion_GetType != 0);
            TEST(api->DQuaternion_Create != 0);
            TEST(api->DQuaternion_GetValuePointer != 0);

        TEST(api->DQuaternionArray_Create != 0);
        TEST(api->DQuaternionArray_GetType != 0);
        TEST(api->DQuaternionArray_GetValuePointer != 0);
        TEST(api->DQuaternionArray_GetLength != 0);


            TEST(api->FQuaternion_GetType != 0);
            TEST(api->FQuaternion_Create != 0);
            TEST(api->FQuaternion_GetValuePointer != 0);

        TEST(api->FQuaternionArray_Create != 0);
        TEST(api->FQuaternionArray_GetType != 0);
        TEST(api->FQuaternionArray_GetValuePointer != 0);
        TEST(api->FQuaternionArray_GetLength != 0);


        TEST(api->BArray_Create != 0);
        TEST(api->BArray_GetType != 0);
        TEST(api->BArray_GetValuePointer != 0);
        TEST(api->BArray_GetLength != 0);


        TEST(api->DArray_Create != 0);
        TEST(api->DArray_GetType != 0);
        TEST(api->DArray_GetValuePointer != 0);
        TEST(api->DArray_GetLength != 0);


        TEST(api->FArray_Create != 0);
        TEST(api->FArray_GetType != 0);
        TEST(api->FArray_GetValuePointer != 0);
        TEST(api->FArray_GetLength != 0);


        TEST(api->I8Array_Create != 0);
        TEST(api->I8Array_GetType != 0);
        TEST(api->I8Array_GetValuePointer != 0);
        TEST(api->I8Array_GetLength != 0);


        TEST(api->U8Array_Create != 0);
        TEST(api->U8Array_GetType != 0);
        TEST(api->U8Array_GetValuePointer != 0);
        TEST(api->U8Array_GetLength != 0);


        TEST(api->I16Array_Create != 0);
        TEST(api->I16Array_GetType != 0);
        TEST(api->I16Array_GetValuePointer != 0);
        TEST(api->I16Array_GetLength != 0);


        TEST(api->U16Array_Create != 0);
        TEST(api->U16Array_GetType != 0);
        TEST(api->U16Array_GetValuePointer != 0);
        TEST(api->U16Array_GetLength != 0);


        TEST(api->I32Array_Create != 0);
        TEST(api->I32Array_GetType != 0);
        TEST(api->I32Array_GetValuePointer != 0);
        TEST(api->I32Array_GetLength != 0);


        TEST(api->U32Array_Create != 0);
        TEST(api->U32Array_GetType != 0);
        TEST(api->U32Array_GetValuePointer != 0);
        TEST(api->U32Array_GetLength != 0);


        TEST(api->IArray_Create != 0);
        TEST(api->IArray_GetType != 0);
        TEST(api->IArray_GetValuePointer != 0);
        TEST(api->IArray_GetLength != 0);


        TEST(api->UArray_Create != 0);
        TEST(api->UArray_GetType != 0);
        TEST(api->UArray_GetValuePointer != 0);
        TEST(api->UArray_GetLength != 0);


        TEST(api->I64Array_Create != 0);
        TEST(api->I64Array_GetType != 0);
        TEST(api->I64Array_GetValuePointer != 0);
        TEST(api->I64Array_GetLength != 0);


        TEST(api->U64Array_Create != 0);
        TEST(api->U64Array_GetType != 0);
        TEST(api->U64Array_GetValuePointer != 0);
        TEST(api->U64Array_GetLength != 0);


    GamutMathApi_Release();
    TEST(!PyErr_Occurred());

    Py_RETURN_NONE;
}





    static PyObject *
    test_BVector1(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->BVector1_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            bool components[1] = {

                    0

            };
            PyObject *obj = api->BVector1_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            bool *value_ptr = api->BVector1_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (bool)0);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        bool *value_ptr = api->BVector1_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_BVector1Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->BVector1Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        bool components[10] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->BVector1Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->BVector1Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            bool *value_ptr = api->BVector1Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 1; j++)
            {
                TEST(value_ptr[j] == (bool)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->BVector1Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        bool *value_ptr = api->BVector1Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }





    static PyObject *
    test_DVector1(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->DVector1_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            double components[1] = {

                    0

            };
            PyObject *obj = api->DVector1_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            double *value_ptr = api->DVector1_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (double)0);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        double *value_ptr = api->DVector1_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_DVector1Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->DVector1Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        double components[10] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->DVector1Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->DVector1Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            double *value_ptr = api->DVector1Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 1; j++)
            {
                TEST(value_ptr[j] == (double)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->DVector1Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        double *value_ptr = api->DVector1Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }





    static PyObject *
    test_FVector1(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->FVector1_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            float components[1] = {

                    0

            };
            PyObject *obj = api->FVector1_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            float *value_ptr = api->FVector1_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (float)0);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        float *value_ptr = api->FVector1_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_FVector1Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->FVector1Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        float components[10] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->FVector1Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->FVector1Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            float *value_ptr = api->FVector1Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 1; j++)
            {
                TEST(value_ptr[j] == (float)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->FVector1Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        float *value_ptr = api->FVector1Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }





    static PyObject *
    test_I8Vector1(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->I8Vector1_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            int8_t components[1] = {

                    0

            };
            PyObject *obj = api->I8Vector1_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            int8_t *value_ptr = api->I8Vector1_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (int8_t)0);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        int8_t *value_ptr = api->I8Vector1_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_I8Vector1Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->I8Vector1Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        int8_t components[10] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->I8Vector1Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->I8Vector1Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            int8_t *value_ptr = api->I8Vector1Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 1; j++)
            {
                TEST(value_ptr[j] == (int8_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->I8Vector1Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        int8_t *value_ptr = api->I8Vector1Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }





    static PyObject *
    test_U8Vector1(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->U8Vector1_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            uint8_t components[1] = {

                    0

            };
            PyObject *obj = api->U8Vector1_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            uint8_t *value_ptr = api->U8Vector1_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (uint8_t)0);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        uint8_t *value_ptr = api->U8Vector1_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_U8Vector1Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->U8Vector1Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        uint8_t components[10] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->U8Vector1Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->U8Vector1Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            uint8_t *value_ptr = api->U8Vector1Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 1; j++)
            {
                TEST(value_ptr[j] == (uint8_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->U8Vector1Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        uint8_t *value_ptr = api->U8Vector1Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }





    static PyObject *
    test_I16Vector1(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->I16Vector1_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            int16_t components[1] = {

                    0

            };
            PyObject *obj = api->I16Vector1_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            int16_t *value_ptr = api->I16Vector1_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (int16_t)0);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        int16_t *value_ptr = api->I16Vector1_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_I16Vector1Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->I16Vector1Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        int16_t components[10] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->I16Vector1Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->I16Vector1Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            int16_t *value_ptr = api->I16Vector1Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 1; j++)
            {
                TEST(value_ptr[j] == (int16_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->I16Vector1Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        int16_t *value_ptr = api->I16Vector1Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }





    static PyObject *
    test_U16Vector1(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->U16Vector1_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            uint16_t components[1] = {

                    0

            };
            PyObject *obj = api->U16Vector1_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            uint16_t *value_ptr = api->U16Vector1_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (uint16_t)0);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        uint16_t *value_ptr = api->U16Vector1_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_U16Vector1Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->U16Vector1Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        uint16_t components[10] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->U16Vector1Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->U16Vector1Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            uint16_t *value_ptr = api->U16Vector1Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 1; j++)
            {
                TEST(value_ptr[j] == (uint16_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->U16Vector1Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        uint16_t *value_ptr = api->U16Vector1Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }





    static PyObject *
    test_I32Vector1(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->I32Vector1_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            int32_t components[1] = {

                    0

            };
            PyObject *obj = api->I32Vector1_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            int32_t *value_ptr = api->I32Vector1_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (int32_t)0);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        int32_t *value_ptr = api->I32Vector1_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_I32Vector1Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->I32Vector1Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        int32_t components[10] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->I32Vector1Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->I32Vector1Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            int32_t *value_ptr = api->I32Vector1Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 1; j++)
            {
                TEST(value_ptr[j] == (int32_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->I32Vector1Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        int32_t *value_ptr = api->I32Vector1Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }





    static PyObject *
    test_U32Vector1(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->U32Vector1_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            uint32_t components[1] = {

                    0

            };
            PyObject *obj = api->U32Vector1_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            uint32_t *value_ptr = api->U32Vector1_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (uint32_t)0);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        uint32_t *value_ptr = api->U32Vector1_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_U32Vector1Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->U32Vector1Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        uint32_t components[10] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->U32Vector1Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->U32Vector1Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            uint32_t *value_ptr = api->U32Vector1Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 1; j++)
            {
                TEST(value_ptr[j] == (uint32_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->U32Vector1Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        uint32_t *value_ptr = api->U32Vector1Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }





    static PyObject *
    test_IVector1(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->IVector1_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            int components[1] = {

                    0

            };
            PyObject *obj = api->IVector1_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            int *value_ptr = api->IVector1_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (int)0);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        int *value_ptr = api->IVector1_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_IVector1Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->IVector1Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        int components[10] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->IVector1Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->IVector1Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            int *value_ptr = api->IVector1Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 1; j++)
            {
                TEST(value_ptr[j] == (int)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->IVector1Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        int *value_ptr = api->IVector1Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }





    static PyObject *
    test_UVector1(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->UVector1_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            unsigned int components[1] = {

                    0

            };
            PyObject *obj = api->UVector1_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            unsigned int *value_ptr = api->UVector1_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (unsigned int)0);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        unsigned int *value_ptr = api->UVector1_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_UVector1Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->UVector1Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        unsigned int components[10] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->UVector1Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->UVector1Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            unsigned int *value_ptr = api->UVector1Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 1; j++)
            {
                TEST(value_ptr[j] == (unsigned int)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->UVector1Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        unsigned int *value_ptr = api->UVector1Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }





    static PyObject *
    test_I64Vector1(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->I64Vector1_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            int64_t components[1] = {

                    0

            };
            PyObject *obj = api->I64Vector1_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            int64_t *value_ptr = api->I64Vector1_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (int64_t)0);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        int64_t *value_ptr = api->I64Vector1_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_I64Vector1Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->I64Vector1Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        int64_t components[10] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->I64Vector1Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->I64Vector1Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            int64_t *value_ptr = api->I64Vector1Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 1; j++)
            {
                TEST(value_ptr[j] == (int64_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->I64Vector1Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        int64_t *value_ptr = api->I64Vector1Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }





    static PyObject *
    test_U64Vector1(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->U64Vector1_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            uint64_t components[1] = {

                    0

            };
            PyObject *obj = api->U64Vector1_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            uint64_t *value_ptr = api->U64Vector1_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (uint64_t)0);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        uint64_t *value_ptr = api->U64Vector1_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_U64Vector1Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->U64Vector1Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        uint64_t components[10] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->U64Vector1Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->U64Vector1Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            uint64_t *value_ptr = api->U64Vector1Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 1; j++)
            {
                TEST(value_ptr[j] == (uint64_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->U64Vector1Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        uint64_t *value_ptr = api->U64Vector1Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }





    static PyObject *
    test_BVector2(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->BVector2_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            bool components[2] = {

                    0,

                    1

            };
            PyObject *obj = api->BVector2_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            bool *value_ptr = api->BVector2_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (bool)0);

                TEST(value_ptr[1] == (bool)1);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        bool *value_ptr = api->BVector2_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_BVector2Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->BVector2Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        bool components[20] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->BVector2Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->BVector2Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            bool *value_ptr = api->BVector2Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 2; j++)
            {
                TEST(value_ptr[j] == (bool)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->BVector2Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        bool *value_ptr = api->BVector2Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }





    static PyObject *
    test_DVector2(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->DVector2_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            double components[2] = {

                    0,

                    1

            };
            PyObject *obj = api->DVector2_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            double *value_ptr = api->DVector2_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (double)0);

                TEST(value_ptr[1] == (double)1);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        double *value_ptr = api->DVector2_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_DVector2Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->DVector2Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        double components[20] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->DVector2Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->DVector2Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            double *value_ptr = api->DVector2Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 2; j++)
            {
                TEST(value_ptr[j] == (double)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->DVector2Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        double *value_ptr = api->DVector2Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }





    static PyObject *
    test_FVector2(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->FVector2_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            float components[2] = {

                    0,

                    1

            };
            PyObject *obj = api->FVector2_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            float *value_ptr = api->FVector2_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (float)0);

                TEST(value_ptr[1] == (float)1);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        float *value_ptr = api->FVector2_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_FVector2Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->FVector2Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        float components[20] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->FVector2Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->FVector2Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            float *value_ptr = api->FVector2Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 2; j++)
            {
                TEST(value_ptr[j] == (float)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->FVector2Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        float *value_ptr = api->FVector2Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }





    static PyObject *
    test_I8Vector2(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->I8Vector2_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            int8_t components[2] = {

                    0,

                    1

            };
            PyObject *obj = api->I8Vector2_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            int8_t *value_ptr = api->I8Vector2_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (int8_t)0);

                TEST(value_ptr[1] == (int8_t)1);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        int8_t *value_ptr = api->I8Vector2_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_I8Vector2Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->I8Vector2Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        int8_t components[20] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->I8Vector2Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->I8Vector2Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            int8_t *value_ptr = api->I8Vector2Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 2; j++)
            {
                TEST(value_ptr[j] == (int8_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->I8Vector2Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        int8_t *value_ptr = api->I8Vector2Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }





    static PyObject *
    test_U8Vector2(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->U8Vector2_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            uint8_t components[2] = {

                    0,

                    1

            };
            PyObject *obj = api->U8Vector2_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            uint8_t *value_ptr = api->U8Vector2_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (uint8_t)0);

                TEST(value_ptr[1] == (uint8_t)1);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        uint8_t *value_ptr = api->U8Vector2_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_U8Vector2Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->U8Vector2Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        uint8_t components[20] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->U8Vector2Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->U8Vector2Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            uint8_t *value_ptr = api->U8Vector2Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 2; j++)
            {
                TEST(value_ptr[j] == (uint8_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->U8Vector2Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        uint8_t *value_ptr = api->U8Vector2Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }





    static PyObject *
    test_I16Vector2(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->I16Vector2_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            int16_t components[2] = {

                    0,

                    1

            };
            PyObject *obj = api->I16Vector2_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            int16_t *value_ptr = api->I16Vector2_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (int16_t)0);

                TEST(value_ptr[1] == (int16_t)1);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        int16_t *value_ptr = api->I16Vector2_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_I16Vector2Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->I16Vector2Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        int16_t components[20] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->I16Vector2Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->I16Vector2Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            int16_t *value_ptr = api->I16Vector2Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 2; j++)
            {
                TEST(value_ptr[j] == (int16_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->I16Vector2Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        int16_t *value_ptr = api->I16Vector2Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }





    static PyObject *
    test_U16Vector2(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->U16Vector2_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            uint16_t components[2] = {

                    0,

                    1

            };
            PyObject *obj = api->U16Vector2_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            uint16_t *value_ptr = api->U16Vector2_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (uint16_t)0);

                TEST(value_ptr[1] == (uint16_t)1);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        uint16_t *value_ptr = api->U16Vector2_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_U16Vector2Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->U16Vector2Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        uint16_t components[20] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->U16Vector2Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->U16Vector2Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            uint16_t *value_ptr = api->U16Vector2Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 2; j++)
            {
                TEST(value_ptr[j] == (uint16_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->U16Vector2Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        uint16_t *value_ptr = api->U16Vector2Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }





    static PyObject *
    test_I32Vector2(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->I32Vector2_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            int32_t components[2] = {

                    0,

                    1

            };
            PyObject *obj = api->I32Vector2_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            int32_t *value_ptr = api->I32Vector2_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (int32_t)0);

                TEST(value_ptr[1] == (int32_t)1);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        int32_t *value_ptr = api->I32Vector2_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_I32Vector2Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->I32Vector2Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        int32_t components[20] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->I32Vector2Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->I32Vector2Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            int32_t *value_ptr = api->I32Vector2Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 2; j++)
            {
                TEST(value_ptr[j] == (int32_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->I32Vector2Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        int32_t *value_ptr = api->I32Vector2Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }





    static PyObject *
    test_U32Vector2(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->U32Vector2_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            uint32_t components[2] = {

                    0,

                    1

            };
            PyObject *obj = api->U32Vector2_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            uint32_t *value_ptr = api->U32Vector2_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (uint32_t)0);

                TEST(value_ptr[1] == (uint32_t)1);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        uint32_t *value_ptr = api->U32Vector2_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_U32Vector2Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->U32Vector2Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        uint32_t components[20] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->U32Vector2Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->U32Vector2Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            uint32_t *value_ptr = api->U32Vector2Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 2; j++)
            {
                TEST(value_ptr[j] == (uint32_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->U32Vector2Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        uint32_t *value_ptr = api->U32Vector2Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }





    static PyObject *
    test_IVector2(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->IVector2_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            int components[2] = {

                    0,

                    1

            };
            PyObject *obj = api->IVector2_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            int *value_ptr = api->IVector2_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (int)0);

                TEST(value_ptr[1] == (int)1);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        int *value_ptr = api->IVector2_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_IVector2Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->IVector2Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        int components[20] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->IVector2Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->IVector2Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            int *value_ptr = api->IVector2Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 2; j++)
            {
                TEST(value_ptr[j] == (int)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->IVector2Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        int *value_ptr = api->IVector2Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }





    static PyObject *
    test_UVector2(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->UVector2_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            unsigned int components[2] = {

                    0,

                    1

            };
            PyObject *obj = api->UVector2_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            unsigned int *value_ptr = api->UVector2_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (unsigned int)0);

                TEST(value_ptr[1] == (unsigned int)1);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        unsigned int *value_ptr = api->UVector2_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_UVector2Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->UVector2Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        unsigned int components[20] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->UVector2Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->UVector2Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            unsigned int *value_ptr = api->UVector2Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 2; j++)
            {
                TEST(value_ptr[j] == (unsigned int)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->UVector2Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        unsigned int *value_ptr = api->UVector2Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }





    static PyObject *
    test_I64Vector2(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->I64Vector2_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            int64_t components[2] = {

                    0,

                    1

            };
            PyObject *obj = api->I64Vector2_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            int64_t *value_ptr = api->I64Vector2_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (int64_t)0);

                TEST(value_ptr[1] == (int64_t)1);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        int64_t *value_ptr = api->I64Vector2_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_I64Vector2Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->I64Vector2Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        int64_t components[20] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->I64Vector2Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->I64Vector2Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            int64_t *value_ptr = api->I64Vector2Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 2; j++)
            {
                TEST(value_ptr[j] == (int64_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->I64Vector2Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        int64_t *value_ptr = api->I64Vector2Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }





    static PyObject *
    test_U64Vector2(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->U64Vector2_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            uint64_t components[2] = {

                    0,

                    1

            };
            PyObject *obj = api->U64Vector2_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            uint64_t *value_ptr = api->U64Vector2_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (uint64_t)0);

                TEST(value_ptr[1] == (uint64_t)1);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        uint64_t *value_ptr = api->U64Vector2_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_U64Vector2Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->U64Vector2Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        uint64_t components[20] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->U64Vector2Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->U64Vector2Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            uint64_t *value_ptr = api->U64Vector2Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 2; j++)
            {
                TEST(value_ptr[j] == (uint64_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->U64Vector2Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        uint64_t *value_ptr = api->U64Vector2Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }





    static PyObject *
    test_BVector3(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->BVector3_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            bool components[3] = {

                    0,

                    1,

                    2

            };
            PyObject *obj = api->BVector3_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            bool *value_ptr = api->BVector3_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (bool)0);

                TEST(value_ptr[1] == (bool)1);

                TEST(value_ptr[2] == (bool)2);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        bool *value_ptr = api->BVector3_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_BVector3Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->BVector3Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        bool components[30] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->BVector3Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->BVector3Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            bool *value_ptr = api->BVector3Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 3; j++)
            {
                TEST(value_ptr[j] == (bool)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->BVector3Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        bool *value_ptr = api->BVector3Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }





    static PyObject *
    test_DVector3(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->DVector3_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            double components[3] = {

                    0,

                    1,

                    2

            };
            PyObject *obj = api->DVector3_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            double *value_ptr = api->DVector3_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (double)0);

                TEST(value_ptr[1] == (double)1);

                TEST(value_ptr[2] == (double)2);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        double *value_ptr = api->DVector3_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_DVector3Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->DVector3Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        double components[30] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->DVector3Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->DVector3Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            double *value_ptr = api->DVector3Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 3; j++)
            {
                TEST(value_ptr[j] == (double)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->DVector3Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        double *value_ptr = api->DVector3Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }





    static PyObject *
    test_FVector3(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->FVector3_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            float components[3] = {

                    0,

                    1,

                    2

            };
            PyObject *obj = api->FVector3_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            float *value_ptr = api->FVector3_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (float)0);

                TEST(value_ptr[1] == (float)1);

                TEST(value_ptr[2] == (float)2);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        float *value_ptr = api->FVector3_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_FVector3Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->FVector3Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        float components[30] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->FVector3Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->FVector3Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            float *value_ptr = api->FVector3Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 3; j++)
            {
                TEST(value_ptr[j] == (float)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->FVector3Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        float *value_ptr = api->FVector3Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }





    static PyObject *
    test_I8Vector3(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->I8Vector3_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            int8_t components[3] = {

                    0,

                    1,

                    2

            };
            PyObject *obj = api->I8Vector3_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            int8_t *value_ptr = api->I8Vector3_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (int8_t)0);

                TEST(value_ptr[1] == (int8_t)1);

                TEST(value_ptr[2] == (int8_t)2);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        int8_t *value_ptr = api->I8Vector3_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_I8Vector3Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->I8Vector3Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        int8_t components[30] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->I8Vector3Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->I8Vector3Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            int8_t *value_ptr = api->I8Vector3Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 3; j++)
            {
                TEST(value_ptr[j] == (int8_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->I8Vector3Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        int8_t *value_ptr = api->I8Vector3Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }





    static PyObject *
    test_U8Vector3(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->U8Vector3_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            uint8_t components[3] = {

                    0,

                    1,

                    2

            };
            PyObject *obj = api->U8Vector3_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            uint8_t *value_ptr = api->U8Vector3_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (uint8_t)0);

                TEST(value_ptr[1] == (uint8_t)1);

                TEST(value_ptr[2] == (uint8_t)2);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        uint8_t *value_ptr = api->U8Vector3_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_U8Vector3Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->U8Vector3Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        uint8_t components[30] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->U8Vector3Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->U8Vector3Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            uint8_t *value_ptr = api->U8Vector3Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 3; j++)
            {
                TEST(value_ptr[j] == (uint8_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->U8Vector3Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        uint8_t *value_ptr = api->U8Vector3Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }





    static PyObject *
    test_I16Vector3(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->I16Vector3_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            int16_t components[3] = {

                    0,

                    1,

                    2

            };
            PyObject *obj = api->I16Vector3_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            int16_t *value_ptr = api->I16Vector3_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (int16_t)0);

                TEST(value_ptr[1] == (int16_t)1);

                TEST(value_ptr[2] == (int16_t)2);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        int16_t *value_ptr = api->I16Vector3_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_I16Vector3Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->I16Vector3Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        int16_t components[30] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->I16Vector3Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->I16Vector3Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            int16_t *value_ptr = api->I16Vector3Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 3; j++)
            {
                TEST(value_ptr[j] == (int16_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->I16Vector3Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        int16_t *value_ptr = api->I16Vector3Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }





    static PyObject *
    test_U16Vector3(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->U16Vector3_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            uint16_t components[3] = {

                    0,

                    1,

                    2

            };
            PyObject *obj = api->U16Vector3_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            uint16_t *value_ptr = api->U16Vector3_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (uint16_t)0);

                TEST(value_ptr[1] == (uint16_t)1);

                TEST(value_ptr[2] == (uint16_t)2);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        uint16_t *value_ptr = api->U16Vector3_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_U16Vector3Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->U16Vector3Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        uint16_t components[30] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->U16Vector3Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->U16Vector3Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            uint16_t *value_ptr = api->U16Vector3Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 3; j++)
            {
                TEST(value_ptr[j] == (uint16_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->U16Vector3Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        uint16_t *value_ptr = api->U16Vector3Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }





    static PyObject *
    test_I32Vector3(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->I32Vector3_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            int32_t components[3] = {

                    0,

                    1,

                    2

            };
            PyObject *obj = api->I32Vector3_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            int32_t *value_ptr = api->I32Vector3_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (int32_t)0);

                TEST(value_ptr[1] == (int32_t)1);

                TEST(value_ptr[2] == (int32_t)2);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        int32_t *value_ptr = api->I32Vector3_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_I32Vector3Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->I32Vector3Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        int32_t components[30] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->I32Vector3Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->I32Vector3Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            int32_t *value_ptr = api->I32Vector3Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 3; j++)
            {
                TEST(value_ptr[j] == (int32_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->I32Vector3Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        int32_t *value_ptr = api->I32Vector3Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }





    static PyObject *
    test_U32Vector3(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->U32Vector3_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            uint32_t components[3] = {

                    0,

                    1,

                    2

            };
            PyObject *obj = api->U32Vector3_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            uint32_t *value_ptr = api->U32Vector3_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (uint32_t)0);

                TEST(value_ptr[1] == (uint32_t)1);

                TEST(value_ptr[2] == (uint32_t)2);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        uint32_t *value_ptr = api->U32Vector3_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_U32Vector3Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->U32Vector3Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        uint32_t components[30] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->U32Vector3Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->U32Vector3Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            uint32_t *value_ptr = api->U32Vector3Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 3; j++)
            {
                TEST(value_ptr[j] == (uint32_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->U32Vector3Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        uint32_t *value_ptr = api->U32Vector3Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }





    static PyObject *
    test_IVector3(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->IVector3_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            int components[3] = {

                    0,

                    1,

                    2

            };
            PyObject *obj = api->IVector3_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            int *value_ptr = api->IVector3_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (int)0);

                TEST(value_ptr[1] == (int)1);

                TEST(value_ptr[2] == (int)2);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        int *value_ptr = api->IVector3_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_IVector3Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->IVector3Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        int components[30] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->IVector3Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->IVector3Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            int *value_ptr = api->IVector3Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 3; j++)
            {
                TEST(value_ptr[j] == (int)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->IVector3Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        int *value_ptr = api->IVector3Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }





    static PyObject *
    test_UVector3(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->UVector3_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            unsigned int components[3] = {

                    0,

                    1,

                    2

            };
            PyObject *obj = api->UVector3_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            unsigned int *value_ptr = api->UVector3_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (unsigned int)0);

                TEST(value_ptr[1] == (unsigned int)1);

                TEST(value_ptr[2] == (unsigned int)2);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        unsigned int *value_ptr = api->UVector3_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_UVector3Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->UVector3Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        unsigned int components[30] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->UVector3Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->UVector3Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            unsigned int *value_ptr = api->UVector3Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 3; j++)
            {
                TEST(value_ptr[j] == (unsigned int)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->UVector3Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        unsigned int *value_ptr = api->UVector3Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }





    static PyObject *
    test_I64Vector3(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->I64Vector3_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            int64_t components[3] = {

                    0,

                    1,

                    2

            };
            PyObject *obj = api->I64Vector3_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            int64_t *value_ptr = api->I64Vector3_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (int64_t)0);

                TEST(value_ptr[1] == (int64_t)1);

                TEST(value_ptr[2] == (int64_t)2);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        int64_t *value_ptr = api->I64Vector3_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_I64Vector3Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->I64Vector3Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        int64_t components[30] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->I64Vector3Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->I64Vector3Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            int64_t *value_ptr = api->I64Vector3Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 3; j++)
            {
                TEST(value_ptr[j] == (int64_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->I64Vector3Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        int64_t *value_ptr = api->I64Vector3Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }





    static PyObject *
    test_U64Vector3(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->U64Vector3_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            uint64_t components[3] = {

                    0,

                    1,

                    2

            };
            PyObject *obj = api->U64Vector3_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            uint64_t *value_ptr = api->U64Vector3_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (uint64_t)0);

                TEST(value_ptr[1] == (uint64_t)1);

                TEST(value_ptr[2] == (uint64_t)2);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        uint64_t *value_ptr = api->U64Vector3_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_U64Vector3Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->U64Vector3Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        uint64_t components[30] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->U64Vector3Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->U64Vector3Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            uint64_t *value_ptr = api->U64Vector3Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 3; j++)
            {
                TEST(value_ptr[j] == (uint64_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->U64Vector3Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        uint64_t *value_ptr = api->U64Vector3Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }





    static PyObject *
    test_BVector4(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->BVector4_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            bool components[4] = {

                    0,

                    1,

                    2,

                    3

            };
            PyObject *obj = api->BVector4_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            bool *value_ptr = api->BVector4_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (bool)0);

                TEST(value_ptr[1] == (bool)1);

                TEST(value_ptr[2] == (bool)2);

                TEST(value_ptr[3] == (bool)3);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        bool *value_ptr = api->BVector4_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_BVector4Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->BVector4Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        bool components[40] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29,

                30,

                31,

                32,

                33,

                34,

                35,

                36,

                37,

                38,

                39

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->BVector4Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->BVector4Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            bool *value_ptr = api->BVector4Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 4; j++)
            {
                TEST(value_ptr[j] == (bool)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->BVector4Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        bool *value_ptr = api->BVector4Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }





    static PyObject *
    test_DVector4(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->DVector4_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            double components[4] = {

                    0,

                    1,

                    2,

                    3

            };
            PyObject *obj = api->DVector4_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            double *value_ptr = api->DVector4_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (double)0);

                TEST(value_ptr[1] == (double)1);

                TEST(value_ptr[2] == (double)2);

                TEST(value_ptr[3] == (double)3);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        double *value_ptr = api->DVector4_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_DVector4Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->DVector4Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        double components[40] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29,

                30,

                31,

                32,

                33,

                34,

                35,

                36,

                37,

                38,

                39

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->DVector4Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->DVector4Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            double *value_ptr = api->DVector4Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 4; j++)
            {
                TEST(value_ptr[j] == (double)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->DVector4Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        double *value_ptr = api->DVector4Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }





    static PyObject *
    test_FVector4(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->FVector4_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            float components[4] = {

                    0,

                    1,

                    2,

                    3

            };
            PyObject *obj = api->FVector4_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            float *value_ptr = api->FVector4_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (float)0);

                TEST(value_ptr[1] == (float)1);

                TEST(value_ptr[2] == (float)2);

                TEST(value_ptr[3] == (float)3);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        float *value_ptr = api->FVector4_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_FVector4Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->FVector4Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        float components[40] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29,

                30,

                31,

                32,

                33,

                34,

                35,

                36,

                37,

                38,

                39

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->FVector4Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->FVector4Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            float *value_ptr = api->FVector4Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 4; j++)
            {
                TEST(value_ptr[j] == (float)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->FVector4Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        float *value_ptr = api->FVector4Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }





    static PyObject *
    test_I8Vector4(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->I8Vector4_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            int8_t components[4] = {

                    0,

                    1,

                    2,

                    3

            };
            PyObject *obj = api->I8Vector4_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            int8_t *value_ptr = api->I8Vector4_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (int8_t)0);

                TEST(value_ptr[1] == (int8_t)1);

                TEST(value_ptr[2] == (int8_t)2);

                TEST(value_ptr[3] == (int8_t)3);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        int8_t *value_ptr = api->I8Vector4_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_I8Vector4Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->I8Vector4Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        int8_t components[40] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29,

                30,

                31,

                32,

                33,

                34,

                35,

                36,

                37,

                38,

                39

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->I8Vector4Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->I8Vector4Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            int8_t *value_ptr = api->I8Vector4Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 4; j++)
            {
                TEST(value_ptr[j] == (int8_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->I8Vector4Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        int8_t *value_ptr = api->I8Vector4Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }





    static PyObject *
    test_U8Vector4(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->U8Vector4_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            uint8_t components[4] = {

                    0,

                    1,

                    2,

                    3

            };
            PyObject *obj = api->U8Vector4_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            uint8_t *value_ptr = api->U8Vector4_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (uint8_t)0);

                TEST(value_ptr[1] == (uint8_t)1);

                TEST(value_ptr[2] == (uint8_t)2);

                TEST(value_ptr[3] == (uint8_t)3);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        uint8_t *value_ptr = api->U8Vector4_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_U8Vector4Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->U8Vector4Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        uint8_t components[40] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29,

                30,

                31,

                32,

                33,

                34,

                35,

                36,

                37,

                38,

                39

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->U8Vector4Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->U8Vector4Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            uint8_t *value_ptr = api->U8Vector4Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 4; j++)
            {
                TEST(value_ptr[j] == (uint8_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->U8Vector4Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        uint8_t *value_ptr = api->U8Vector4Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }





    static PyObject *
    test_I16Vector4(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->I16Vector4_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            int16_t components[4] = {

                    0,

                    1,

                    2,

                    3

            };
            PyObject *obj = api->I16Vector4_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            int16_t *value_ptr = api->I16Vector4_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (int16_t)0);

                TEST(value_ptr[1] == (int16_t)1);

                TEST(value_ptr[2] == (int16_t)2);

                TEST(value_ptr[3] == (int16_t)3);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        int16_t *value_ptr = api->I16Vector4_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_I16Vector4Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->I16Vector4Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        int16_t components[40] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29,

                30,

                31,

                32,

                33,

                34,

                35,

                36,

                37,

                38,

                39

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->I16Vector4Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->I16Vector4Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            int16_t *value_ptr = api->I16Vector4Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 4; j++)
            {
                TEST(value_ptr[j] == (int16_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->I16Vector4Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        int16_t *value_ptr = api->I16Vector4Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }





    static PyObject *
    test_U16Vector4(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->U16Vector4_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            uint16_t components[4] = {

                    0,

                    1,

                    2,

                    3

            };
            PyObject *obj = api->U16Vector4_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            uint16_t *value_ptr = api->U16Vector4_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (uint16_t)0);

                TEST(value_ptr[1] == (uint16_t)1);

                TEST(value_ptr[2] == (uint16_t)2);

                TEST(value_ptr[3] == (uint16_t)3);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        uint16_t *value_ptr = api->U16Vector4_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_U16Vector4Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->U16Vector4Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        uint16_t components[40] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29,

                30,

                31,

                32,

                33,

                34,

                35,

                36,

                37,

                38,

                39

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->U16Vector4Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->U16Vector4Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            uint16_t *value_ptr = api->U16Vector4Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 4; j++)
            {
                TEST(value_ptr[j] == (uint16_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->U16Vector4Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        uint16_t *value_ptr = api->U16Vector4Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }





    static PyObject *
    test_I32Vector4(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->I32Vector4_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            int32_t components[4] = {

                    0,

                    1,

                    2,

                    3

            };
            PyObject *obj = api->I32Vector4_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            int32_t *value_ptr = api->I32Vector4_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (int32_t)0);

                TEST(value_ptr[1] == (int32_t)1);

                TEST(value_ptr[2] == (int32_t)2);

                TEST(value_ptr[3] == (int32_t)3);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        int32_t *value_ptr = api->I32Vector4_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_I32Vector4Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->I32Vector4Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        int32_t components[40] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29,

                30,

                31,

                32,

                33,

                34,

                35,

                36,

                37,

                38,

                39

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->I32Vector4Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->I32Vector4Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            int32_t *value_ptr = api->I32Vector4Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 4; j++)
            {
                TEST(value_ptr[j] == (int32_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->I32Vector4Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        int32_t *value_ptr = api->I32Vector4Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }





    static PyObject *
    test_U32Vector4(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->U32Vector4_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            uint32_t components[4] = {

                    0,

                    1,

                    2,

                    3

            };
            PyObject *obj = api->U32Vector4_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            uint32_t *value_ptr = api->U32Vector4_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (uint32_t)0);

                TEST(value_ptr[1] == (uint32_t)1);

                TEST(value_ptr[2] == (uint32_t)2);

                TEST(value_ptr[3] == (uint32_t)3);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        uint32_t *value_ptr = api->U32Vector4_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_U32Vector4Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->U32Vector4Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        uint32_t components[40] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29,

                30,

                31,

                32,

                33,

                34,

                35,

                36,

                37,

                38,

                39

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->U32Vector4Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->U32Vector4Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            uint32_t *value_ptr = api->U32Vector4Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 4; j++)
            {
                TEST(value_ptr[j] == (uint32_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->U32Vector4Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        uint32_t *value_ptr = api->U32Vector4Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }





    static PyObject *
    test_IVector4(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->IVector4_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            int components[4] = {

                    0,

                    1,

                    2,

                    3

            };
            PyObject *obj = api->IVector4_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            int *value_ptr = api->IVector4_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (int)0);

                TEST(value_ptr[1] == (int)1);

                TEST(value_ptr[2] == (int)2);

                TEST(value_ptr[3] == (int)3);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        int *value_ptr = api->IVector4_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_IVector4Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->IVector4Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        int components[40] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29,

                30,

                31,

                32,

                33,

                34,

                35,

                36,

                37,

                38,

                39

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->IVector4Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->IVector4Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            int *value_ptr = api->IVector4Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 4; j++)
            {
                TEST(value_ptr[j] == (int)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->IVector4Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        int *value_ptr = api->IVector4Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }





    static PyObject *
    test_UVector4(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->UVector4_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            unsigned int components[4] = {

                    0,

                    1,

                    2,

                    3

            };
            PyObject *obj = api->UVector4_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            unsigned int *value_ptr = api->UVector4_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (unsigned int)0);

                TEST(value_ptr[1] == (unsigned int)1);

                TEST(value_ptr[2] == (unsigned int)2);

                TEST(value_ptr[3] == (unsigned int)3);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        unsigned int *value_ptr = api->UVector4_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_UVector4Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->UVector4Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        unsigned int components[40] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29,

                30,

                31,

                32,

                33,

                34,

                35,

                36,

                37,

                38,

                39

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->UVector4Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->UVector4Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            unsigned int *value_ptr = api->UVector4Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 4; j++)
            {
                TEST(value_ptr[j] == (unsigned int)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->UVector4Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        unsigned int *value_ptr = api->UVector4Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }





    static PyObject *
    test_I64Vector4(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->I64Vector4_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            int64_t components[4] = {

                    0,

                    1,

                    2,

                    3

            };
            PyObject *obj = api->I64Vector4_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            int64_t *value_ptr = api->I64Vector4_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (int64_t)0);

                TEST(value_ptr[1] == (int64_t)1);

                TEST(value_ptr[2] == (int64_t)2);

                TEST(value_ptr[3] == (int64_t)3);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        int64_t *value_ptr = api->I64Vector4_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_I64Vector4Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->I64Vector4Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        int64_t components[40] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29,

                30,

                31,

                32,

                33,

                34,

                35,

                36,

                37,

                38,

                39

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->I64Vector4Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->I64Vector4Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            int64_t *value_ptr = api->I64Vector4Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 4; j++)
            {
                TEST(value_ptr[j] == (int64_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->I64Vector4Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        int64_t *value_ptr = api->I64Vector4Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }





    static PyObject *
    test_U64Vector4(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->U64Vector4_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            uint64_t components[4] = {

                    0,

                    1,

                    2,

                    3

            };
            PyObject *obj = api->U64Vector4_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            uint64_t *value_ptr = api->U64Vector4_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (uint64_t)0);

                TEST(value_ptr[1] == (uint64_t)1);

                TEST(value_ptr[2] == (uint64_t)2);

                TEST(value_ptr[3] == (uint64_t)3);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        uint64_t *value_ptr = api->U64Vector4_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_U64Vector4Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->U64Vector4Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        uint64_t components[40] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29,

                30,

                31,

                32,

                33,

                34,

                35,

                36,

                37,

                38,

                39

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->U64Vector4Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->U64Vector4Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            uint64_t *value_ptr = api->U64Vector4Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 4; j++)
            {
                TEST(value_ptr[j] == (uint64_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->U64Vector4Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        uint64_t *value_ptr = api->U64Vector4Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }










    static PyObject *
    test_DMatrix2x2(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->DMatrix2x2_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            double components[4] = {

                    0,

                    1,

                    2,

                    3

            };
            PyObject *obj = api->DMatrix2x2_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            double *value_ptr = api->DMatrix2x2_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (double)0);

                TEST(value_ptr[1] == (double)1);

                TEST(value_ptr[2] == (double)2);

                TEST(value_ptr[3] == (double)3);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        double *value_ptr = api->DMatrix2x2_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_DMatrix2x2Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->DMatrix2x2Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        double components[40] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29,

                30,

                31,

                32,

                33,

                34,

                35,

                36,

                37,

                38,

                39

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->DMatrix2x2Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->DMatrix2x2Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            double *value_ptr = api->DMatrix2x2Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 4; j++)
            {
                TEST(value_ptr[j] == (double)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->DMatrix2x2Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        double *value_ptr = api->DMatrix2x2Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }









    static PyObject *
    test_FMatrix2x2(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->FMatrix2x2_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            float components[4] = {

                    0,

                    1,

                    2,

                    3

            };
            PyObject *obj = api->FMatrix2x2_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            float *value_ptr = api->FMatrix2x2_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (float)0);

                TEST(value_ptr[1] == (float)1);

                TEST(value_ptr[2] == (float)2);

                TEST(value_ptr[3] == (float)3);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        float *value_ptr = api->FMatrix2x2_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_FMatrix2x2Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->FMatrix2x2Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        float components[40] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29,

                30,

                31,

                32,

                33,

                34,

                35,

                36,

                37,

                38,

                39

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->FMatrix2x2Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->FMatrix2x2Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            float *value_ptr = api->FMatrix2x2Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 4; j++)
            {
                TEST(value_ptr[j] == (float)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->FMatrix2x2Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        float *value_ptr = api->FMatrix2x2Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }









    static PyObject *
    test_DMatrix2x3(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->DMatrix2x3_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            double components[6] = {

                    0,

                    1,

                    2,

                    3,

                    4,

                    5

            };
            PyObject *obj = api->DMatrix2x3_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            double *value_ptr = api->DMatrix2x3_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (double)0);

                TEST(value_ptr[1] == (double)1);

                TEST(value_ptr[2] == (double)2);

                TEST(value_ptr[3] == (double)3);

                TEST(value_ptr[4] == (double)4);

                TEST(value_ptr[5] == (double)5);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        double *value_ptr = api->DMatrix2x3_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_DMatrix2x3Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->DMatrix2x3Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        double components[60] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29,

                30,

                31,

                32,

                33,

                34,

                35,

                36,

                37,

                38,

                39,

                40,

                41,

                42,

                43,

                44,

                45,

                46,

                47,

                48,

                49,

                50,

                51,

                52,

                53,

                54,

                55,

                56,

                57,

                58,

                59

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->DMatrix2x3Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->DMatrix2x3Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            double *value_ptr = api->DMatrix2x3Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 6; j++)
            {
                TEST(value_ptr[j] == (double)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->DMatrix2x3Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        double *value_ptr = api->DMatrix2x3Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }









    static PyObject *
    test_FMatrix2x3(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->FMatrix2x3_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            float components[6] = {

                    0,

                    1,

                    2,

                    3,

                    4,

                    5

            };
            PyObject *obj = api->FMatrix2x3_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            float *value_ptr = api->FMatrix2x3_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (float)0);

                TEST(value_ptr[1] == (float)1);

                TEST(value_ptr[2] == (float)2);

                TEST(value_ptr[3] == (float)3);

                TEST(value_ptr[4] == (float)4);

                TEST(value_ptr[5] == (float)5);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        float *value_ptr = api->FMatrix2x3_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_FMatrix2x3Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->FMatrix2x3Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        float components[60] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29,

                30,

                31,

                32,

                33,

                34,

                35,

                36,

                37,

                38,

                39,

                40,

                41,

                42,

                43,

                44,

                45,

                46,

                47,

                48,

                49,

                50,

                51,

                52,

                53,

                54,

                55,

                56,

                57,

                58,

                59

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->FMatrix2x3Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->FMatrix2x3Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            float *value_ptr = api->FMatrix2x3Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 6; j++)
            {
                TEST(value_ptr[j] == (float)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->FMatrix2x3Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        float *value_ptr = api->FMatrix2x3Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }









    static PyObject *
    test_DMatrix2x4(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->DMatrix2x4_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            double components[8] = {

                    0,

                    1,

                    2,

                    3,

                    4,

                    5,

                    6,

                    7

            };
            PyObject *obj = api->DMatrix2x4_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            double *value_ptr = api->DMatrix2x4_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (double)0);

                TEST(value_ptr[1] == (double)1);

                TEST(value_ptr[2] == (double)2);

                TEST(value_ptr[3] == (double)3);

                TEST(value_ptr[4] == (double)4);

                TEST(value_ptr[5] == (double)5);

                TEST(value_ptr[6] == (double)6);

                TEST(value_ptr[7] == (double)7);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        double *value_ptr = api->DMatrix2x4_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_DMatrix2x4Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->DMatrix2x4Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        double components[80] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29,

                30,

                31,

                32,

                33,

                34,

                35,

                36,

                37,

                38,

                39,

                40,

                41,

                42,

                43,

                44,

                45,

                46,

                47,

                48,

                49,

                50,

                51,

                52,

                53,

                54,

                55,

                56,

                57,

                58,

                59,

                60,

                61,

                62,

                63,

                64,

                65,

                66,

                67,

                68,

                69,

                70,

                71,

                72,

                73,

                74,

                75,

                76,

                77,

                78,

                79

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->DMatrix2x4Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->DMatrix2x4Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            double *value_ptr = api->DMatrix2x4Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 8; j++)
            {
                TEST(value_ptr[j] == (double)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->DMatrix2x4Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        double *value_ptr = api->DMatrix2x4Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }









    static PyObject *
    test_FMatrix2x4(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->FMatrix2x4_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            float components[8] = {

                    0,

                    1,

                    2,

                    3,

                    4,

                    5,

                    6,

                    7

            };
            PyObject *obj = api->FMatrix2x4_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            float *value_ptr = api->FMatrix2x4_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (float)0);

                TEST(value_ptr[1] == (float)1);

                TEST(value_ptr[2] == (float)2);

                TEST(value_ptr[3] == (float)3);

                TEST(value_ptr[4] == (float)4);

                TEST(value_ptr[5] == (float)5);

                TEST(value_ptr[6] == (float)6);

                TEST(value_ptr[7] == (float)7);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        float *value_ptr = api->FMatrix2x4_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_FMatrix2x4Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->FMatrix2x4Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        float components[80] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29,

                30,

                31,

                32,

                33,

                34,

                35,

                36,

                37,

                38,

                39,

                40,

                41,

                42,

                43,

                44,

                45,

                46,

                47,

                48,

                49,

                50,

                51,

                52,

                53,

                54,

                55,

                56,

                57,

                58,

                59,

                60,

                61,

                62,

                63,

                64,

                65,

                66,

                67,

                68,

                69,

                70,

                71,

                72,

                73,

                74,

                75,

                76,

                77,

                78,

                79

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->FMatrix2x4Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->FMatrix2x4Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            float *value_ptr = api->FMatrix2x4Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 8; j++)
            {
                TEST(value_ptr[j] == (float)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->FMatrix2x4Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        float *value_ptr = api->FMatrix2x4Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }









    static PyObject *
    test_DMatrix3x2(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->DMatrix3x2_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            double components[6] = {

                    0,

                    1,

                    2,

                    3,

                    4,

                    5

            };
            PyObject *obj = api->DMatrix3x2_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            double *value_ptr = api->DMatrix3x2_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (double)0);

                TEST(value_ptr[1] == (double)1);

                TEST(value_ptr[2] == (double)2);

                TEST(value_ptr[3] == (double)3);

                TEST(value_ptr[4] == (double)4);

                TEST(value_ptr[5] == (double)5);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        double *value_ptr = api->DMatrix3x2_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_DMatrix3x2Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->DMatrix3x2Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        double components[60] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29,

                30,

                31,

                32,

                33,

                34,

                35,

                36,

                37,

                38,

                39,

                40,

                41,

                42,

                43,

                44,

                45,

                46,

                47,

                48,

                49,

                50,

                51,

                52,

                53,

                54,

                55,

                56,

                57,

                58,

                59

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->DMatrix3x2Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->DMatrix3x2Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            double *value_ptr = api->DMatrix3x2Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 6; j++)
            {
                TEST(value_ptr[j] == (double)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->DMatrix3x2Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        double *value_ptr = api->DMatrix3x2Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }









    static PyObject *
    test_FMatrix3x2(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->FMatrix3x2_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            float components[6] = {

                    0,

                    1,

                    2,

                    3,

                    4,

                    5

            };
            PyObject *obj = api->FMatrix3x2_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            float *value_ptr = api->FMatrix3x2_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (float)0);

                TEST(value_ptr[1] == (float)1);

                TEST(value_ptr[2] == (float)2);

                TEST(value_ptr[3] == (float)3);

                TEST(value_ptr[4] == (float)4);

                TEST(value_ptr[5] == (float)5);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        float *value_ptr = api->FMatrix3x2_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_FMatrix3x2Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->FMatrix3x2Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        float components[60] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29,

                30,

                31,

                32,

                33,

                34,

                35,

                36,

                37,

                38,

                39,

                40,

                41,

                42,

                43,

                44,

                45,

                46,

                47,

                48,

                49,

                50,

                51,

                52,

                53,

                54,

                55,

                56,

                57,

                58,

                59

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->FMatrix3x2Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->FMatrix3x2Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            float *value_ptr = api->FMatrix3x2Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 6; j++)
            {
                TEST(value_ptr[j] == (float)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->FMatrix3x2Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        float *value_ptr = api->FMatrix3x2Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }









    static PyObject *
    test_DMatrix3x3(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->DMatrix3x3_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            double components[9] = {

                    0,

                    1,

                    2,

                    3,

                    4,

                    5,

                    6,

                    7,

                    8

            };
            PyObject *obj = api->DMatrix3x3_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            double *value_ptr = api->DMatrix3x3_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (double)0);

                TEST(value_ptr[1] == (double)1);

                TEST(value_ptr[2] == (double)2);

                TEST(value_ptr[3] == (double)3);

                TEST(value_ptr[4] == (double)4);

                TEST(value_ptr[5] == (double)5);

                TEST(value_ptr[6] == (double)6);

                TEST(value_ptr[7] == (double)7);

                TEST(value_ptr[8] == (double)8);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        double *value_ptr = api->DMatrix3x3_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_DMatrix3x3Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->DMatrix3x3Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        double components[90] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29,

                30,

                31,

                32,

                33,

                34,

                35,

                36,

                37,

                38,

                39,

                40,

                41,

                42,

                43,

                44,

                45,

                46,

                47,

                48,

                49,

                50,

                51,

                52,

                53,

                54,

                55,

                56,

                57,

                58,

                59,

                60,

                61,

                62,

                63,

                64,

                65,

                66,

                67,

                68,

                69,

                70,

                71,

                72,

                73,

                74,

                75,

                76,

                77,

                78,

                79,

                80,

                81,

                82,

                83,

                84,

                85,

                86,

                87,

                88,

                89

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->DMatrix3x3Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->DMatrix3x3Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            double *value_ptr = api->DMatrix3x3Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 9; j++)
            {
                TEST(value_ptr[j] == (double)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->DMatrix3x3Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        double *value_ptr = api->DMatrix3x3Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }









    static PyObject *
    test_FMatrix3x3(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->FMatrix3x3_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            float components[9] = {

                    0,

                    1,

                    2,

                    3,

                    4,

                    5,

                    6,

                    7,

                    8

            };
            PyObject *obj = api->FMatrix3x3_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            float *value_ptr = api->FMatrix3x3_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (float)0);

                TEST(value_ptr[1] == (float)1);

                TEST(value_ptr[2] == (float)2);

                TEST(value_ptr[3] == (float)3);

                TEST(value_ptr[4] == (float)4);

                TEST(value_ptr[5] == (float)5);

                TEST(value_ptr[6] == (float)6);

                TEST(value_ptr[7] == (float)7);

                TEST(value_ptr[8] == (float)8);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        float *value_ptr = api->FMatrix3x3_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_FMatrix3x3Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->FMatrix3x3Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        float components[90] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29,

                30,

                31,

                32,

                33,

                34,

                35,

                36,

                37,

                38,

                39,

                40,

                41,

                42,

                43,

                44,

                45,

                46,

                47,

                48,

                49,

                50,

                51,

                52,

                53,

                54,

                55,

                56,

                57,

                58,

                59,

                60,

                61,

                62,

                63,

                64,

                65,

                66,

                67,

                68,

                69,

                70,

                71,

                72,

                73,

                74,

                75,

                76,

                77,

                78,

                79,

                80,

                81,

                82,

                83,

                84,

                85,

                86,

                87,

                88,

                89

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->FMatrix3x3Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->FMatrix3x3Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            float *value_ptr = api->FMatrix3x3Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 9; j++)
            {
                TEST(value_ptr[j] == (float)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->FMatrix3x3Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        float *value_ptr = api->FMatrix3x3Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }









    static PyObject *
    test_DMatrix3x4(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->DMatrix3x4_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            double components[12] = {

                    0,

                    1,

                    2,

                    3,

                    4,

                    5,

                    6,

                    7,

                    8,

                    9,

                    10,

                    11

            };
            PyObject *obj = api->DMatrix3x4_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            double *value_ptr = api->DMatrix3x4_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (double)0);

                TEST(value_ptr[1] == (double)1);

                TEST(value_ptr[2] == (double)2);

                TEST(value_ptr[3] == (double)3);

                TEST(value_ptr[4] == (double)4);

                TEST(value_ptr[5] == (double)5);

                TEST(value_ptr[6] == (double)6);

                TEST(value_ptr[7] == (double)7);

                TEST(value_ptr[8] == (double)8);

                TEST(value_ptr[9] == (double)9);

                TEST(value_ptr[10] == (double)10);

                TEST(value_ptr[11] == (double)11);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        double *value_ptr = api->DMatrix3x4_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_DMatrix3x4Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->DMatrix3x4Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        double components[120] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29,

                30,

                31,

                32,

                33,

                34,

                35,

                36,

                37,

                38,

                39,

                40,

                41,

                42,

                43,

                44,

                45,

                46,

                47,

                48,

                49,

                50,

                51,

                52,

                53,

                54,

                55,

                56,

                57,

                58,

                59,

                60,

                61,

                62,

                63,

                64,

                65,

                66,

                67,

                68,

                69,

                70,

                71,

                72,

                73,

                74,

                75,

                76,

                77,

                78,

                79,

                80,

                81,

                82,

                83,

                84,

                85,

                86,

                87,

                88,

                89,

                90,

                91,

                92,

                93,

                94,

                95,

                96,

                97,

                98,

                99,

                100,

                101,

                102,

                103,

                104,

                105,

                106,

                107,

                108,

                109,

                110,

                111,

                112,

                113,

                114,

                115,

                116,

                117,

                118,

                119

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->DMatrix3x4Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->DMatrix3x4Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            double *value_ptr = api->DMatrix3x4Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 12; j++)
            {
                TEST(value_ptr[j] == (double)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->DMatrix3x4Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        double *value_ptr = api->DMatrix3x4Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }









    static PyObject *
    test_FMatrix3x4(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->FMatrix3x4_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            float components[12] = {

                    0,

                    1,

                    2,

                    3,

                    4,

                    5,

                    6,

                    7,

                    8,

                    9,

                    10,

                    11

            };
            PyObject *obj = api->FMatrix3x4_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            float *value_ptr = api->FMatrix3x4_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (float)0);

                TEST(value_ptr[1] == (float)1);

                TEST(value_ptr[2] == (float)2);

                TEST(value_ptr[3] == (float)3);

                TEST(value_ptr[4] == (float)4);

                TEST(value_ptr[5] == (float)5);

                TEST(value_ptr[6] == (float)6);

                TEST(value_ptr[7] == (float)7);

                TEST(value_ptr[8] == (float)8);

                TEST(value_ptr[9] == (float)9);

                TEST(value_ptr[10] == (float)10);

                TEST(value_ptr[11] == (float)11);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        float *value_ptr = api->FMatrix3x4_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_FMatrix3x4Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->FMatrix3x4Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        float components[120] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29,

                30,

                31,

                32,

                33,

                34,

                35,

                36,

                37,

                38,

                39,

                40,

                41,

                42,

                43,

                44,

                45,

                46,

                47,

                48,

                49,

                50,

                51,

                52,

                53,

                54,

                55,

                56,

                57,

                58,

                59,

                60,

                61,

                62,

                63,

                64,

                65,

                66,

                67,

                68,

                69,

                70,

                71,

                72,

                73,

                74,

                75,

                76,

                77,

                78,

                79,

                80,

                81,

                82,

                83,

                84,

                85,

                86,

                87,

                88,

                89,

                90,

                91,

                92,

                93,

                94,

                95,

                96,

                97,

                98,

                99,

                100,

                101,

                102,

                103,

                104,

                105,

                106,

                107,

                108,

                109,

                110,

                111,

                112,

                113,

                114,

                115,

                116,

                117,

                118,

                119

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->FMatrix3x4Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->FMatrix3x4Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            float *value_ptr = api->FMatrix3x4Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 12; j++)
            {
                TEST(value_ptr[j] == (float)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->FMatrix3x4Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        float *value_ptr = api->FMatrix3x4Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }









    static PyObject *
    test_DMatrix4x2(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->DMatrix4x2_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            double components[8] = {

                    0,

                    1,

                    2,

                    3,

                    4,

                    5,

                    6,

                    7

            };
            PyObject *obj = api->DMatrix4x2_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            double *value_ptr = api->DMatrix4x2_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (double)0);

                TEST(value_ptr[1] == (double)1);

                TEST(value_ptr[2] == (double)2);

                TEST(value_ptr[3] == (double)3);

                TEST(value_ptr[4] == (double)4);

                TEST(value_ptr[5] == (double)5);

                TEST(value_ptr[6] == (double)6);

                TEST(value_ptr[7] == (double)7);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        double *value_ptr = api->DMatrix4x2_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_DMatrix4x2Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->DMatrix4x2Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        double components[80] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29,

                30,

                31,

                32,

                33,

                34,

                35,

                36,

                37,

                38,

                39,

                40,

                41,

                42,

                43,

                44,

                45,

                46,

                47,

                48,

                49,

                50,

                51,

                52,

                53,

                54,

                55,

                56,

                57,

                58,

                59,

                60,

                61,

                62,

                63,

                64,

                65,

                66,

                67,

                68,

                69,

                70,

                71,

                72,

                73,

                74,

                75,

                76,

                77,

                78,

                79

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->DMatrix4x2Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->DMatrix4x2Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            double *value_ptr = api->DMatrix4x2Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 8; j++)
            {
                TEST(value_ptr[j] == (double)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->DMatrix4x2Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        double *value_ptr = api->DMatrix4x2Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }









    static PyObject *
    test_FMatrix4x2(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->FMatrix4x2_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            float components[8] = {

                    0,

                    1,

                    2,

                    3,

                    4,

                    5,

                    6,

                    7

            };
            PyObject *obj = api->FMatrix4x2_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            float *value_ptr = api->FMatrix4x2_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (float)0);

                TEST(value_ptr[1] == (float)1);

                TEST(value_ptr[2] == (float)2);

                TEST(value_ptr[3] == (float)3);

                TEST(value_ptr[4] == (float)4);

                TEST(value_ptr[5] == (float)5);

                TEST(value_ptr[6] == (float)6);

                TEST(value_ptr[7] == (float)7);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        float *value_ptr = api->FMatrix4x2_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_FMatrix4x2Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->FMatrix4x2Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        float components[80] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29,

                30,

                31,

                32,

                33,

                34,

                35,

                36,

                37,

                38,

                39,

                40,

                41,

                42,

                43,

                44,

                45,

                46,

                47,

                48,

                49,

                50,

                51,

                52,

                53,

                54,

                55,

                56,

                57,

                58,

                59,

                60,

                61,

                62,

                63,

                64,

                65,

                66,

                67,

                68,

                69,

                70,

                71,

                72,

                73,

                74,

                75,

                76,

                77,

                78,

                79

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->FMatrix4x2Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->FMatrix4x2Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            float *value_ptr = api->FMatrix4x2Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 8; j++)
            {
                TEST(value_ptr[j] == (float)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->FMatrix4x2Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        float *value_ptr = api->FMatrix4x2Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }









    static PyObject *
    test_DMatrix4x3(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->DMatrix4x3_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            double components[12] = {

                    0,

                    1,

                    2,

                    3,

                    4,

                    5,

                    6,

                    7,

                    8,

                    9,

                    10,

                    11

            };
            PyObject *obj = api->DMatrix4x3_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            double *value_ptr = api->DMatrix4x3_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (double)0);

                TEST(value_ptr[1] == (double)1);

                TEST(value_ptr[2] == (double)2);

                TEST(value_ptr[3] == (double)3);

                TEST(value_ptr[4] == (double)4);

                TEST(value_ptr[5] == (double)5);

                TEST(value_ptr[6] == (double)6);

                TEST(value_ptr[7] == (double)7);

                TEST(value_ptr[8] == (double)8);

                TEST(value_ptr[9] == (double)9);

                TEST(value_ptr[10] == (double)10);

                TEST(value_ptr[11] == (double)11);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        double *value_ptr = api->DMatrix4x3_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_DMatrix4x3Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->DMatrix4x3Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        double components[120] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29,

                30,

                31,

                32,

                33,

                34,

                35,

                36,

                37,

                38,

                39,

                40,

                41,

                42,

                43,

                44,

                45,

                46,

                47,

                48,

                49,

                50,

                51,

                52,

                53,

                54,

                55,

                56,

                57,

                58,

                59,

                60,

                61,

                62,

                63,

                64,

                65,

                66,

                67,

                68,

                69,

                70,

                71,

                72,

                73,

                74,

                75,

                76,

                77,

                78,

                79,

                80,

                81,

                82,

                83,

                84,

                85,

                86,

                87,

                88,

                89,

                90,

                91,

                92,

                93,

                94,

                95,

                96,

                97,

                98,

                99,

                100,

                101,

                102,

                103,

                104,

                105,

                106,

                107,

                108,

                109,

                110,

                111,

                112,

                113,

                114,

                115,

                116,

                117,

                118,

                119

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->DMatrix4x3Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->DMatrix4x3Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            double *value_ptr = api->DMatrix4x3Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 12; j++)
            {
                TEST(value_ptr[j] == (double)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->DMatrix4x3Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        double *value_ptr = api->DMatrix4x3Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }









    static PyObject *
    test_FMatrix4x3(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->FMatrix4x3_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            float components[12] = {

                    0,

                    1,

                    2,

                    3,

                    4,

                    5,

                    6,

                    7,

                    8,

                    9,

                    10,

                    11

            };
            PyObject *obj = api->FMatrix4x3_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            float *value_ptr = api->FMatrix4x3_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (float)0);

                TEST(value_ptr[1] == (float)1);

                TEST(value_ptr[2] == (float)2);

                TEST(value_ptr[3] == (float)3);

                TEST(value_ptr[4] == (float)4);

                TEST(value_ptr[5] == (float)5);

                TEST(value_ptr[6] == (float)6);

                TEST(value_ptr[7] == (float)7);

                TEST(value_ptr[8] == (float)8);

                TEST(value_ptr[9] == (float)9);

                TEST(value_ptr[10] == (float)10);

                TEST(value_ptr[11] == (float)11);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        float *value_ptr = api->FMatrix4x3_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_FMatrix4x3Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->FMatrix4x3Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        float components[120] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29,

                30,

                31,

                32,

                33,

                34,

                35,

                36,

                37,

                38,

                39,

                40,

                41,

                42,

                43,

                44,

                45,

                46,

                47,

                48,

                49,

                50,

                51,

                52,

                53,

                54,

                55,

                56,

                57,

                58,

                59,

                60,

                61,

                62,

                63,

                64,

                65,

                66,

                67,

                68,

                69,

                70,

                71,

                72,

                73,

                74,

                75,

                76,

                77,

                78,

                79,

                80,

                81,

                82,

                83,

                84,

                85,

                86,

                87,

                88,

                89,

                90,

                91,

                92,

                93,

                94,

                95,

                96,

                97,

                98,

                99,

                100,

                101,

                102,

                103,

                104,

                105,

                106,

                107,

                108,

                109,

                110,

                111,

                112,

                113,

                114,

                115,

                116,

                117,

                118,

                119

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->FMatrix4x3Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->FMatrix4x3Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            float *value_ptr = api->FMatrix4x3Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 12; j++)
            {
                TEST(value_ptr[j] == (float)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->FMatrix4x3Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        float *value_ptr = api->FMatrix4x3Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }









    static PyObject *
    test_DMatrix4x4(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->DMatrix4x4_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            double components[16] = {

                    0,

                    1,

                    2,

                    3,

                    4,

                    5,

                    6,

                    7,

                    8,

                    9,

                    10,

                    11,

                    12,

                    13,

                    14,

                    15

            };
            PyObject *obj = api->DMatrix4x4_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            double *value_ptr = api->DMatrix4x4_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (double)0);

                TEST(value_ptr[1] == (double)1);

                TEST(value_ptr[2] == (double)2);

                TEST(value_ptr[3] == (double)3);

                TEST(value_ptr[4] == (double)4);

                TEST(value_ptr[5] == (double)5);

                TEST(value_ptr[6] == (double)6);

                TEST(value_ptr[7] == (double)7);

                TEST(value_ptr[8] == (double)8);

                TEST(value_ptr[9] == (double)9);

                TEST(value_ptr[10] == (double)10);

                TEST(value_ptr[11] == (double)11);

                TEST(value_ptr[12] == (double)12);

                TEST(value_ptr[13] == (double)13);

                TEST(value_ptr[14] == (double)14);

                TEST(value_ptr[15] == (double)15);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        double *value_ptr = api->DMatrix4x4_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_DMatrix4x4Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->DMatrix4x4Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        double components[160] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29,

                30,

                31,

                32,

                33,

                34,

                35,

                36,

                37,

                38,

                39,

                40,

                41,

                42,

                43,

                44,

                45,

                46,

                47,

                48,

                49,

                50,

                51,

                52,

                53,

                54,

                55,

                56,

                57,

                58,

                59,

                60,

                61,

                62,

                63,

                64,

                65,

                66,

                67,

                68,

                69,

                70,

                71,

                72,

                73,

                74,

                75,

                76,

                77,

                78,

                79,

                80,

                81,

                82,

                83,

                84,

                85,

                86,

                87,

                88,

                89,

                90,

                91,

                92,

                93,

                94,

                95,

                96,

                97,

                98,

                99,

                100,

                101,

                102,

                103,

                104,

                105,

                106,

                107,

                108,

                109,

                110,

                111,

                112,

                113,

                114,

                115,

                116,

                117,

                118,

                119,

                120,

                121,

                122,

                123,

                124,

                125,

                126,

                127,

                128,

                129,

                130,

                131,

                132,

                133,

                134,

                135,

                136,

                137,

                138,

                139,

                140,

                141,

                142,

                143,

                144,

                145,

                146,

                147,

                148,

                149,

                150,

                151,

                152,

                153,

                154,

                155,

                156,

                157,

                158,

                159

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->DMatrix4x4Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->DMatrix4x4Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            double *value_ptr = api->DMatrix4x4Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 16; j++)
            {
                TEST(value_ptr[j] == (double)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->DMatrix4x4Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        double *value_ptr = api->DMatrix4x4Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }









    static PyObject *
    test_FMatrix4x4(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->FMatrix4x4_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            float components[16] = {

                    0,

                    1,

                    2,

                    3,

                    4,

                    5,

                    6,

                    7,

                    8,

                    9,

                    10,

                    11,

                    12,

                    13,

                    14,

                    15

            };
            PyObject *obj = api->FMatrix4x4_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            float *value_ptr = api->FMatrix4x4_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (float)0);

                TEST(value_ptr[1] == (float)1);

                TEST(value_ptr[2] == (float)2);

                TEST(value_ptr[3] == (float)3);

                TEST(value_ptr[4] == (float)4);

                TEST(value_ptr[5] == (float)5);

                TEST(value_ptr[6] == (float)6);

                TEST(value_ptr[7] == (float)7);

                TEST(value_ptr[8] == (float)8);

                TEST(value_ptr[9] == (float)9);

                TEST(value_ptr[10] == (float)10);

                TEST(value_ptr[11] == (float)11);

                TEST(value_ptr[12] == (float)12);

                TEST(value_ptr[13] == (float)13);

                TEST(value_ptr[14] == (float)14);

                TEST(value_ptr[15] == (float)15);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        float *value_ptr = api->FMatrix4x4_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_FMatrix4x4Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->FMatrix4x4Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        float components[160] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29,

                30,

                31,

                32,

                33,

                34,

                35,

                36,

                37,

                38,

                39,

                40,

                41,

                42,

                43,

                44,

                45,

                46,

                47,

                48,

                49,

                50,

                51,

                52,

                53,

                54,

                55,

                56,

                57,

                58,

                59,

                60,

                61,

                62,

                63,

                64,

                65,

                66,

                67,

                68,

                69,

                70,

                71,

                72,

                73,

                74,

                75,

                76,

                77,

                78,

                79,

                80,

                81,

                82,

                83,

                84,

                85,

                86,

                87,

                88,

                89,

                90,

                91,

                92,

                93,

                94,

                95,

                96,

                97,

                98,

                99,

                100,

                101,

                102,

                103,

                104,

                105,

                106,

                107,

                108,

                109,

                110,

                111,

                112,

                113,

                114,

                115,

                116,

                117,

                118,

                119,

                120,

                121,

                122,

                123,

                124,

                125,

                126,

                127,

                128,

                129,

                130,

                131,

                132,

                133,

                134,

                135,

                136,

                137,

                138,

                139,

                140,

                141,

                142,

                143,

                144,

                145,

                146,

                147,

                148,

                149,

                150,

                151,

                152,

                153,

                154,

                155,

                156,

                157,

                158,

                159

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->FMatrix4x4Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->FMatrix4x4Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            float *value_ptr = api->FMatrix4x4Array_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 16; j++)
            {
                TEST(value_ptr[j] == (float)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->FMatrix4x4Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        float *value_ptr = api->FMatrix4x4Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }









    static PyObject *
    test_DQuaternion(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->DQuaternion_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            double components[4] = {

                    0,

                    1,

                    2,

                    3

            };
            PyObject *obj = api->DQuaternion_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            double *value_ptr = api->DQuaternion_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (double)0);

                TEST(value_ptr[1] == (double)1);

                TEST(value_ptr[2] == (double)2);

                TEST(value_ptr[3] == (double)3);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        double *value_ptr = api->DQuaternion_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_DQuaternionArray(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->DQuaternionArray_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        double components[40] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29,

                30,

                31,

                32,

                33,

                34,

                35,

                36,

                37,

                38,

                39

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->DQuaternionArray_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->DQuaternionArray_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            double *value_ptr = api->DQuaternionArray_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 4; j++)
            {
                TEST(value_ptr[j] == (double)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->DQuaternionArray_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        double *value_ptr = api->DQuaternionArray_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }



    static PyObject *
    test_FQuaternion(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->FQuaternion_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        {
            float components[4] = {

                    0,

                    1,

                    2,

                    3

            };
            PyObject *obj = api->FQuaternion_Create(components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            float *value_ptr = api->FQuaternion_GetValuePointer(obj);
            TEST(value_ptr != 0);
            TEST(!PyErr_Occurred());

                TEST(value_ptr[0] == (float)0);

                TEST(value_ptr[1] == (float)1);

                TEST(value_ptr[2] == (float)2);

                TEST(value_ptr[3] == (float)3);


            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        float *value_ptr = api->FQuaternion_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }

    static PyObject *
    test_FQuaternionArray(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->FQuaternionArray_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        float components[40] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9,

                10,

                11,

                12,

                13,

                14,

                15,

                16,

                17,

                18,

                19,

                20,

                21,

                22,

                23,

                24,

                25,

                26,

                27,

                28,

                29,

                30,

                31,

                32,

                33,

                34,

                35,

                36,

                37,

                38,

                39

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->FQuaternionArray_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->FQuaternionArray_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            float *value_ptr = api->FQuaternionArray_GetValuePointer(obj);
            if (i == 0)
            {
                TEST(value_ptr == 0);
            }
            else
            {
                TEST(value_ptr != 0);
            }
            TEST(!PyErr_Occurred());
            for (size_t j = 0; j < i * 4; j++)
            {
                TEST(value_ptr[j] == (float)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->FQuaternionArray_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        float *value_ptr = api->FQuaternionArray_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }






    static PyObject *
    test_BArray(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->BArray_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        bool components[10] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->BArray_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->BArray_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            bool *value_ptr = api->BArray_GetValuePointer(obj);
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
                TEST(value_ptr[j] == (bool)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->BArray_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        bool *value_ptr = api->BArray_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }



    static PyObject *
    test_DArray(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->DArray_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        double components[10] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->DArray_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->DArray_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            double *value_ptr = api->DArray_GetValuePointer(obj);
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
                TEST(value_ptr[j] == (double)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->DArray_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        double *value_ptr = api->DArray_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }



    static PyObject *
    test_FArray(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->FArray_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        float components[10] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->FArray_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->FArray_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            float *value_ptr = api->FArray_GetValuePointer(obj);
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
                TEST(value_ptr[j] == (float)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->FArray_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        float *value_ptr = api->FArray_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }



    static PyObject *
    test_I8Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->I8Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        int8_t components[10] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->I8Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->I8Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            int8_t *value_ptr = api->I8Array_GetValuePointer(obj);
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
                TEST(value_ptr[j] == (int8_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->I8Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        int8_t *value_ptr = api->I8Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }



    static PyObject *
    test_U8Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->U8Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        uint8_t components[10] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->U8Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->U8Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            uint8_t *value_ptr = api->U8Array_GetValuePointer(obj);
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
                TEST(value_ptr[j] == (uint8_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->U8Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        uint8_t *value_ptr = api->U8Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }



    static PyObject *
    test_I16Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->I16Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        int16_t components[10] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->I16Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->I16Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            int16_t *value_ptr = api->I16Array_GetValuePointer(obj);
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
                TEST(value_ptr[j] == (int16_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->I16Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        int16_t *value_ptr = api->I16Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }



    static PyObject *
    test_U16Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->U16Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        uint16_t components[10] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->U16Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->U16Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            uint16_t *value_ptr = api->U16Array_GetValuePointer(obj);
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
                TEST(value_ptr[j] == (uint16_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->U16Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        uint16_t *value_ptr = api->U16Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }



    static PyObject *
    test_I32Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->I32Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        int32_t components[10] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->I32Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->I32Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            int32_t *value_ptr = api->I32Array_GetValuePointer(obj);
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
                TEST(value_ptr[j] == (int32_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->I32Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        int32_t *value_ptr = api->I32Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }



    static PyObject *
    test_U32Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->U32Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        uint32_t components[10] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->U32Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->U32Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            uint32_t *value_ptr = api->U32Array_GetValuePointer(obj);
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
                TEST(value_ptr[j] == (uint32_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->U32Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        uint32_t *value_ptr = api->U32Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }



    static PyObject *
    test_IArray(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->IArray_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        int components[10] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->IArray_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->IArray_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            int *value_ptr = api->IArray_GetValuePointer(obj);
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
                TEST(value_ptr[j] == (int)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->IArray_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        int *value_ptr = api->IArray_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }



    static PyObject *
    test_UArray(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->UArray_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        unsigned int components[10] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->UArray_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->UArray_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            unsigned int *value_ptr = api->UArray_GetValuePointer(obj);
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
                TEST(value_ptr[j] == (unsigned int)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->UArray_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        unsigned int *value_ptr = api->UArray_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }



    static PyObject *
    test_I64Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->I64Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        int64_t components[10] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->I64Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->I64Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            int64_t *value_ptr = api->I64Array_GetValuePointer(obj);
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
                TEST(value_ptr[j] == (int64_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->I64Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        int64_t *value_ptr = api->I64Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }



    static PyObject *
    test_U64Array(PyObject *self, PyObject *args)
    {
        struct GamutMathApi *api = GamutMathApi_Get();
        if (!api){ return 0; }
        TEST(!PyErr_Occurred());

        PyTypeObject *type = api->U64Array_GetType();
        TEST(type != 0);
        TEST(!PyErr_Occurred());

        uint64_t components[10] = {

                0,

                1,

                2,

                3,

                4,

                5,

                6,

                7,

                8,

                9

        };
        for (size_t i = 0; i < 10; i++)
        {
            PyObject *obj = api->U64Array_Create(i, components);
            TEST(obj != 0);
            TEST(!PyErr_Occurred());
            TEST(Py_TYPE(obj) == type);

            size_t length = api->U64Array_GetLength(obj);
            TEST(length == i);
            TEST(!PyErr_Occurred());

            uint64_t *value_ptr = api->U64Array_GetValuePointer(obj);
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
                TEST(value_ptr[j] == (uint64_t)j);
            }

            Py_DECREF(obj);
        }

        Py_INCREF(Py_None);
        size_t length = api->U64Array_GetLength(Py_None);
        TEST(length == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        uint64_t *value_ptr = api->U64Array_GetValuePointer(Py_None);
        TEST(value_ptr == 0);
        TEST(PyErr_Occurred());
        PyErr_Clear();
        Py_DECREF(Py_None);

        GamutMathApi_Release();
        TEST(!PyErr_Occurred());

        Py_RETURN_NONE;
    }




static PyMethodDef module_methods[] = {
    {"test_GamutMathApi_Get", test_GamutMathApi_Get, METH_NOARGS, 0},

        {"test_BVector1", test_BVector1, METH_NOARGS, 0},
        {"test_BVector1Array", test_BVector1Array, METH_NOARGS, 0},

        {"test_DVector1", test_DVector1, METH_NOARGS, 0},
        {"test_DVector1Array", test_DVector1Array, METH_NOARGS, 0},

        {"test_FVector1", test_FVector1, METH_NOARGS, 0},
        {"test_FVector1Array", test_FVector1Array, METH_NOARGS, 0},

        {"test_I8Vector1", test_I8Vector1, METH_NOARGS, 0},
        {"test_I8Vector1Array", test_I8Vector1Array, METH_NOARGS, 0},

        {"test_U8Vector1", test_U8Vector1, METH_NOARGS, 0},
        {"test_U8Vector1Array", test_U8Vector1Array, METH_NOARGS, 0},

        {"test_I16Vector1", test_I16Vector1, METH_NOARGS, 0},
        {"test_I16Vector1Array", test_I16Vector1Array, METH_NOARGS, 0},

        {"test_U16Vector1", test_U16Vector1, METH_NOARGS, 0},
        {"test_U16Vector1Array", test_U16Vector1Array, METH_NOARGS, 0},

        {"test_I32Vector1", test_I32Vector1, METH_NOARGS, 0},
        {"test_I32Vector1Array", test_I32Vector1Array, METH_NOARGS, 0},

        {"test_U32Vector1", test_U32Vector1, METH_NOARGS, 0},
        {"test_U32Vector1Array", test_U32Vector1Array, METH_NOARGS, 0},

        {"test_IVector1", test_IVector1, METH_NOARGS, 0},
        {"test_IVector1Array", test_IVector1Array, METH_NOARGS, 0},

        {"test_UVector1", test_UVector1, METH_NOARGS, 0},
        {"test_UVector1Array", test_UVector1Array, METH_NOARGS, 0},

        {"test_I64Vector1", test_I64Vector1, METH_NOARGS, 0},
        {"test_I64Vector1Array", test_I64Vector1Array, METH_NOARGS, 0},

        {"test_U64Vector1", test_U64Vector1, METH_NOARGS, 0},
        {"test_U64Vector1Array", test_U64Vector1Array, METH_NOARGS, 0},

        {"test_BVector2", test_BVector2, METH_NOARGS, 0},
        {"test_BVector2Array", test_BVector2Array, METH_NOARGS, 0},

        {"test_DVector2", test_DVector2, METH_NOARGS, 0},
        {"test_DVector2Array", test_DVector2Array, METH_NOARGS, 0},

        {"test_FVector2", test_FVector2, METH_NOARGS, 0},
        {"test_FVector2Array", test_FVector2Array, METH_NOARGS, 0},

        {"test_I8Vector2", test_I8Vector2, METH_NOARGS, 0},
        {"test_I8Vector2Array", test_I8Vector2Array, METH_NOARGS, 0},

        {"test_U8Vector2", test_U8Vector2, METH_NOARGS, 0},
        {"test_U8Vector2Array", test_U8Vector2Array, METH_NOARGS, 0},

        {"test_I16Vector2", test_I16Vector2, METH_NOARGS, 0},
        {"test_I16Vector2Array", test_I16Vector2Array, METH_NOARGS, 0},

        {"test_U16Vector2", test_U16Vector2, METH_NOARGS, 0},
        {"test_U16Vector2Array", test_U16Vector2Array, METH_NOARGS, 0},

        {"test_I32Vector2", test_I32Vector2, METH_NOARGS, 0},
        {"test_I32Vector2Array", test_I32Vector2Array, METH_NOARGS, 0},

        {"test_U32Vector2", test_U32Vector2, METH_NOARGS, 0},
        {"test_U32Vector2Array", test_U32Vector2Array, METH_NOARGS, 0},

        {"test_IVector2", test_IVector2, METH_NOARGS, 0},
        {"test_IVector2Array", test_IVector2Array, METH_NOARGS, 0},

        {"test_UVector2", test_UVector2, METH_NOARGS, 0},
        {"test_UVector2Array", test_UVector2Array, METH_NOARGS, 0},

        {"test_I64Vector2", test_I64Vector2, METH_NOARGS, 0},
        {"test_I64Vector2Array", test_I64Vector2Array, METH_NOARGS, 0},

        {"test_U64Vector2", test_U64Vector2, METH_NOARGS, 0},
        {"test_U64Vector2Array", test_U64Vector2Array, METH_NOARGS, 0},

        {"test_BVector3", test_BVector3, METH_NOARGS, 0},
        {"test_BVector3Array", test_BVector3Array, METH_NOARGS, 0},

        {"test_DVector3", test_DVector3, METH_NOARGS, 0},
        {"test_DVector3Array", test_DVector3Array, METH_NOARGS, 0},

        {"test_FVector3", test_FVector3, METH_NOARGS, 0},
        {"test_FVector3Array", test_FVector3Array, METH_NOARGS, 0},

        {"test_I8Vector3", test_I8Vector3, METH_NOARGS, 0},
        {"test_I8Vector3Array", test_I8Vector3Array, METH_NOARGS, 0},

        {"test_U8Vector3", test_U8Vector3, METH_NOARGS, 0},
        {"test_U8Vector3Array", test_U8Vector3Array, METH_NOARGS, 0},

        {"test_I16Vector3", test_I16Vector3, METH_NOARGS, 0},
        {"test_I16Vector3Array", test_I16Vector3Array, METH_NOARGS, 0},

        {"test_U16Vector3", test_U16Vector3, METH_NOARGS, 0},
        {"test_U16Vector3Array", test_U16Vector3Array, METH_NOARGS, 0},

        {"test_I32Vector3", test_I32Vector3, METH_NOARGS, 0},
        {"test_I32Vector3Array", test_I32Vector3Array, METH_NOARGS, 0},

        {"test_U32Vector3", test_U32Vector3, METH_NOARGS, 0},
        {"test_U32Vector3Array", test_U32Vector3Array, METH_NOARGS, 0},

        {"test_IVector3", test_IVector3, METH_NOARGS, 0},
        {"test_IVector3Array", test_IVector3Array, METH_NOARGS, 0},

        {"test_UVector3", test_UVector3, METH_NOARGS, 0},
        {"test_UVector3Array", test_UVector3Array, METH_NOARGS, 0},

        {"test_I64Vector3", test_I64Vector3, METH_NOARGS, 0},
        {"test_I64Vector3Array", test_I64Vector3Array, METH_NOARGS, 0},

        {"test_U64Vector3", test_U64Vector3, METH_NOARGS, 0},
        {"test_U64Vector3Array", test_U64Vector3Array, METH_NOARGS, 0},

        {"test_BVector4", test_BVector4, METH_NOARGS, 0},
        {"test_BVector4Array", test_BVector4Array, METH_NOARGS, 0},

        {"test_DVector4", test_DVector4, METH_NOARGS, 0},
        {"test_DVector4Array", test_DVector4Array, METH_NOARGS, 0},

        {"test_FVector4", test_FVector4, METH_NOARGS, 0},
        {"test_FVector4Array", test_FVector4Array, METH_NOARGS, 0},

        {"test_I8Vector4", test_I8Vector4, METH_NOARGS, 0},
        {"test_I8Vector4Array", test_I8Vector4Array, METH_NOARGS, 0},

        {"test_U8Vector4", test_U8Vector4, METH_NOARGS, 0},
        {"test_U8Vector4Array", test_U8Vector4Array, METH_NOARGS, 0},

        {"test_I16Vector4", test_I16Vector4, METH_NOARGS, 0},
        {"test_I16Vector4Array", test_I16Vector4Array, METH_NOARGS, 0},

        {"test_U16Vector4", test_U16Vector4, METH_NOARGS, 0},
        {"test_U16Vector4Array", test_U16Vector4Array, METH_NOARGS, 0},

        {"test_I32Vector4", test_I32Vector4, METH_NOARGS, 0},
        {"test_I32Vector4Array", test_I32Vector4Array, METH_NOARGS, 0},

        {"test_U32Vector4", test_U32Vector4, METH_NOARGS, 0},
        {"test_U32Vector4Array", test_U32Vector4Array, METH_NOARGS, 0},

        {"test_IVector4", test_IVector4, METH_NOARGS, 0},
        {"test_IVector4Array", test_IVector4Array, METH_NOARGS, 0},

        {"test_UVector4", test_UVector4, METH_NOARGS, 0},
        {"test_UVector4Array", test_UVector4Array, METH_NOARGS, 0},

        {"test_I64Vector4", test_I64Vector4, METH_NOARGS, 0},
        {"test_I64Vector4Array", test_I64Vector4Array, METH_NOARGS, 0},

        {"test_U64Vector4", test_U64Vector4, METH_NOARGS, 0},
        {"test_U64Vector4Array", test_U64Vector4Array, METH_NOARGS, 0},


        {"test_DMatrix2x2", test_DMatrix2x2, METH_NOARGS, 0},
        {"test_DMatrix2x2Array", test_DMatrix2x2Array, METH_NOARGS, 0},

        {"test_FMatrix2x2", test_FMatrix2x2, METH_NOARGS, 0},
        {"test_FMatrix2x2Array", test_FMatrix2x2Array, METH_NOARGS, 0},

        {"test_DMatrix2x3", test_DMatrix2x3, METH_NOARGS, 0},
        {"test_DMatrix2x3Array", test_DMatrix2x3Array, METH_NOARGS, 0},

        {"test_FMatrix2x3", test_FMatrix2x3, METH_NOARGS, 0},
        {"test_FMatrix2x3Array", test_FMatrix2x3Array, METH_NOARGS, 0},

        {"test_DMatrix2x4", test_DMatrix2x4, METH_NOARGS, 0},
        {"test_DMatrix2x4Array", test_DMatrix2x4Array, METH_NOARGS, 0},

        {"test_FMatrix2x4", test_FMatrix2x4, METH_NOARGS, 0},
        {"test_FMatrix2x4Array", test_FMatrix2x4Array, METH_NOARGS, 0},

        {"test_DMatrix3x2", test_DMatrix3x2, METH_NOARGS, 0},
        {"test_DMatrix3x2Array", test_DMatrix3x2Array, METH_NOARGS, 0},

        {"test_FMatrix3x2", test_FMatrix3x2, METH_NOARGS, 0},
        {"test_FMatrix3x2Array", test_FMatrix3x2Array, METH_NOARGS, 0},

        {"test_DMatrix3x3", test_DMatrix3x3, METH_NOARGS, 0},
        {"test_DMatrix3x3Array", test_DMatrix3x3Array, METH_NOARGS, 0},

        {"test_FMatrix3x3", test_FMatrix3x3, METH_NOARGS, 0},
        {"test_FMatrix3x3Array", test_FMatrix3x3Array, METH_NOARGS, 0},

        {"test_DMatrix3x4", test_DMatrix3x4, METH_NOARGS, 0},
        {"test_DMatrix3x4Array", test_DMatrix3x4Array, METH_NOARGS, 0},

        {"test_FMatrix3x4", test_FMatrix3x4, METH_NOARGS, 0},
        {"test_FMatrix3x4Array", test_FMatrix3x4Array, METH_NOARGS, 0},

        {"test_DMatrix4x2", test_DMatrix4x2, METH_NOARGS, 0},
        {"test_DMatrix4x2Array", test_DMatrix4x2Array, METH_NOARGS, 0},

        {"test_FMatrix4x2", test_FMatrix4x2, METH_NOARGS, 0},
        {"test_FMatrix4x2Array", test_FMatrix4x2Array, METH_NOARGS, 0},

        {"test_DMatrix4x3", test_DMatrix4x3, METH_NOARGS, 0},
        {"test_DMatrix4x3Array", test_DMatrix4x3Array, METH_NOARGS, 0},

        {"test_FMatrix4x3", test_FMatrix4x3, METH_NOARGS, 0},
        {"test_FMatrix4x3Array", test_FMatrix4x3Array, METH_NOARGS, 0},

        {"test_DMatrix4x4", test_DMatrix4x4, METH_NOARGS, 0},
        {"test_DMatrix4x4Array", test_DMatrix4x4Array, METH_NOARGS, 0},

        {"test_FMatrix4x4", test_FMatrix4x4, METH_NOARGS, 0},
        {"test_FMatrix4x4Array", test_FMatrix4x4Array, METH_NOARGS, 0},


        {"test_DQuaternion", test_DQuaternion, METH_NOARGS, 0},
        {"test_DQuaternionArray", test_DQuaternionArray, METH_NOARGS, 0},

        {"test_FQuaternion", test_FQuaternion, METH_NOARGS, 0},
        {"test_FQuaternionArray", test_FQuaternionArray, METH_NOARGS, 0},


        {"test_BArray", test_BArray, METH_NOARGS, 0},

        {"test_DArray", test_DArray, METH_NOARGS, 0},

        {"test_FArray", test_FArray, METH_NOARGS, 0},

        {"test_I8Array", test_I8Array, METH_NOARGS, 0},

        {"test_U8Array", test_U8Array, METH_NOARGS, 0},

        {"test_I16Array", test_I16Array, METH_NOARGS, 0},

        {"test_U16Array", test_U16Array, METH_NOARGS, 0},

        {"test_I32Array", test_I32Array, METH_NOARGS, 0},

        {"test_U32Array", test_U32Array, METH_NOARGS, 0},

        {"test_IArray", test_IArray, METH_NOARGS, 0},

        {"test_UArray", test_UArray, METH_NOARGS, 0},

        {"test_I64Array", test_I64Array, METH_NOARGS, 0},

        {"test_U64Array", test_U64Array, METH_NOARGS, 0},

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