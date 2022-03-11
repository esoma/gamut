
# gamut
from gamut.math import (BArray, DArray, FArray, I8Array, I16Array, I32Array,
                        I64Array, IArray, U8Array, U16Array, U32Array,
                        U64Array, UArray)
# python
from math import isclose as _isclose
import struct
from weakref import ref
# pytest
import pytest


def isclose(a, b):
    return _isclose(a, b, rel_tol=1e-07)


class PodTest:

    def __init_subclass__(
        this_cls,
        *,
        array_cls,
        type,
        struct_format,
        struct_byte_order='',
        unsigned=False
    ):
        this_cls.array_cls = array_cls
        this_cls.type = type
        this_cls.struct_byte_order = struct_byte_order
        this_cls.struct_format = struct_format
        this_cls.unsigned = unsigned

    def test_array_init_empty(self) -> None:
        array = self.array_cls()
        assert len(array) == 0

    def test_array_init_keywords(self) -> None:
        with pytest.raises(TypeError):
            self.array_cls(x=0)

    def test_array_init(self) -> None:
        for i in range(10):
            array = self.array_cls(*range(i))
            assert len(array) == i
            for j, pod in enumerate(array):
                assert isinstance(pod, self.type)
                assert pod == self.type(j)

    def test_array_init_invalid_type(self):
        if self.type is bool:
            return
        with pytest.raises(TypeError):
            self.array_cls(None)
        with pytest.raises(TypeError):
            self.array_cls('abc')

    def test_array_getitem(self) -> None:
        with pytest.raises(IndexError) as excinfo:
            self.array_cls()[0]
        assert str(excinfo.value) == 'index out of range'

        array = self.array_cls(*range(10))
        for i in range(10):
            assert isinstance(array[i], self.type)
            assert array[i] == self.type(i)
            assert isinstance(array[i - 10], self.type)
            assert array[i - 10] == self.type(i)

        with pytest.raises(IndexError) as excinfo:
            array[10]
        assert str(excinfo.value) == 'index out of range'

        with pytest.raises(IndexError) as excinfo:
            array[-11]
        assert str(excinfo.value) == 'index out of range'

    def test_array_setitem(self) -> None:
        array = self.array_cls(self.type(1))
        with pytest.raises(TypeError):
            array[0] = self.type(2)

    def test_array_hash(self) -> None:
        assert hash(self.array_cls()) != hash(self.array_cls(self.type(0)))
        assert hash(self.array_cls(self.type(0))) != hash(
            self.array_cls(self.type(1))
        )
        assert hash(self.array_cls(self.type(1))) == hash(
            self.array_cls(self.type(1))
        )
        if self.type != bool and not self.unsigned:
            assert hash(self.array_cls(self.type(-1))) != (
                hash(self.array_cls(self.type(1)))
            )

    def test_array_repr(self) -> None:
        assert repr(self.array_cls()) == f'{self.array_cls.__name__}[0]'
        assert repr(self.array_cls(self.type())) == (
            f'{self.array_cls.__name__}[1]'
        )
        assert repr(self.array_cls(*(self.type() for _ in range(100)))) == (
            f'{self.array_cls.__name__}[100]'
        )

    def test_array_weakref(self) -> None:
        array = self.array_cls()
        weak_array = ref(array)

    def test_array_equal(self) -> None:
        assert self.array_cls() == self.array_cls()
        for i in range(0 if self.unsigned else -100, 100):
            assert self.array_cls(self.type(i)) == self.array_cls(self.type(i))
            assert not (
                self.array_cls(self.type(i), self.type(i)) ==
                self.array_cls(self.type(i))
            )

        assert not (self.array_cls() == 1)
        assert not (self.array_cls() == object())
        assert not (1 == self.array_cls())
        assert not (object() == self.array_cls())

    def test_array_equal(self) -> None:
        assert not (self.array_cls() != self.array_cls())
        for i in range(0 if self.unsigned else -100, 100):
            assert not (
                self.array_cls(self.type(i)) != self.array_cls(self.type(i))
            )
            assert (
                self.array_cls(self.type(i), self.type(i)) !=
                self.array_cls(self.type(i))
            )

        assert self.array_cls() != 1
        assert self.array_cls() != object()
        assert 1 != self.array_cls()
        assert object() != self.array_cls()

    def test_array_comparisons_not_implemented(self) -> None:
        a = self.array_cls()
        b = self.array_cls()
        with pytest.raises(TypeError):
            a < b
        with pytest.raises(TypeError):
            a <= b
        with pytest.raises(TypeError):
            a > b
        with pytest.raises(TypeError):
            a >= b

    def test_array_bool(self) -> None:
        assert not self.array_cls()
        assert self.array_cls(self.type())

    def test_array_buffer(self) -> None:
        assert bytes(self.array_cls()) == b''

        array = self.array_cls(
            self.type(1),
            self.type(5),
            self.type(0),
        )
        assert bytes(array) == struct.pack(
            self.struct_byte_order + (self.struct_format * 3),
            1, 5, 0
        )
        memory_view = memoryview(array)
        assert memory_view.readonly
        assert memory_view.format == (
            self.struct_byte_order + self.struct_format
        )
        assert memory_view.itemsize == struct.calcsize(
            self.struct_byte_order + self.struct_format
        )
        assert memory_view.ndim == 1
        assert memory_view.shape == (3,)
        assert memory_view.strides == (
            struct.calcsize(self.struct_byte_order + self.struct_format),
        )
        assert memory_view.suboffsets == tuple()
        assert memory_view.c_contiguous
        assert memory_view.f_contiguous
        assert memory_view.contiguous


class TestB(
    PodTest,
    array_cls=BArray,
    type=bool,
    struct_format='?'
):
    pass


class TestD(
    PodTest,
    array_cls=DArray,
    type=float,
    struct_format='d'
):
    pass


class TestF(
    PodTest,
    array_cls=FArray,
    type=float,
    struct_format='f'
):
    pass


class TestI8(
    PodTest,
    array_cls=I8Array,
    type=int,
    struct_byte_order='=',
    struct_format='b'
):
    pass


class TestU8(
    PodTest,
    array_cls=U8Array,
    type=int,
    struct_byte_order='=',
    struct_format='B',
    unsigned=True
):
    pass


class TestI16(
    PodTest,
    array_cls=I16Array,
    type=int,
    struct_byte_order='=',
    struct_format='h'
):
    pass


class TestU16(
    PodTest,
    array_cls=U16Array,
    type=int,
    struct_byte_order='=',
    struct_format='H',
    unsigned=True
):
    pass


class TestI32(
    PodTest,
    array_cls=I32Array,
    type=int,
    struct_byte_order='=',
    struct_format='i'
):
    pass


class TestU32(
    PodTest,
    array_cls=U32Array,
    type=int,
    struct_byte_order='=',
    struct_format='I',
    unsigned=True
):
    pass


class TestI(
    PodTest,
    array_cls=IArray,
    type=int,
    struct_format='i'
):
    pass


class TestU(
    PodTest,
    array_cls=UArray,
    type=int,
    struct_format='I',
    unsigned=True
):
    pass


class TestI64(
    PodTest,
    array_cls=I64Array,
    type=int,
    struct_byte_order='=',
    struct_format='q'
):
    pass


class TestU64(
    PodTest,
    array_cls=U64Array,
    type=int,
    struct_byte_order='=',
    struct_format='Q',
    unsigned=True
):
    pass
