
# gamut
from gamut.math import (DQuaternion, DQuaternionArray, DVector3, DVector4,
                        FQuaternion, FQuaternionArray, FVector3, FVector4,
                        Quaternion, QuaternionArray)
# python
import ctypes
import itertools
from math import inf
from math import isclose as _isclose
from math import isnan, radians, sqrt
import struct
from typing import Final
from weakref import ref
# pytest
import pytest


def isclose(a, b):
    return _isclose(a, b, abs_tol=1e-6)


def test_alias():
    assert Quaternion is DQuaternion
    assert QuaternionArray is DQuaternionArray


class VectorTest:

    POSITION_ATTRIBUTES: Final = ('x', 'y', 'z', 'w')
    COLOR_ATTRIBUTES: Final = ('r', 'g', 'b', 'a')
    UV_ATTRIBUTES: Final = ('u', 'v')
    TEXTURE_ATTRIBUTES: Final = ('s', 't', 'p', 'q')

    def __init_subclass__(
        this_cls,
        *,
        cls,
        struct_format
    ):
        this_cls.cls = cls
        this_cls.array_cls = globals()[f'{cls.__name__}Array']
        this_cls.struct_format = struct_format

    def test_empty_init(self) -> None:
        quat = self.cls()
        for i in range(4):
            assert quat[i] == 0

    def test_array_init_empty(self) -> None:
        array = self.array_cls()
        assert len(array) == 0

    def test_init_keywords(self) -> None:
        with pytest.raises(TypeError):
            self.cls(x=0)

    def test_array_init_keywords(self) -> None:
        with pytest.raises(TypeError):
            self.array_cls(x=0)

    def test_single_init(self) -> None:
        for arg in [-100, -1, 0, 1, 100]:
            quat = self.cls(arg)
            assert quat.w == arg
            assert quat.x == 0
            assert quat.y == 0
            assert quat.z == 0
        min, max = self.cls.get_limits()
        assert self.cls(min - 1) == self.cls(min)
        assert self.cls(max + 1) == self.cls(max)

    def test_all_init(self) -> None:
        quat = self.cls(*range(4))
        for i in range(4):
            assert quat[i] == i

    def test_array_init(self) -> None:
        for i in range(10):
            array = self.array_cls(*(self.cls(j) for j in range(i)))
            assert len(array) == i
            for j, quat in enumerate(array):
                assert isinstance(quat, self.cls)
                assert quat == self.cls(j)

    def test_invalid_arg_count(self) -> None:
        with pytest.raises(TypeError) as excinfo:
            quat = self.cls(*range(5))
        assert str(excinfo.value) == (
            f'invalid number of arguments supplied to '
            f'{ self.cls.__name__ }, expected 0, 1 or '
            f'4 (got 5)'
        )

        for count in range(2, 4):
            with pytest.raises(TypeError) as excinfo:
                quat = self.cls(*range(count))
            assert str(excinfo.value) == (
                f'invalid number of arguments supplied to '
                f'{ self.cls.__name__ }, expected 0, 1 or '
                f'4 (got { count })'
            )

    def test_array_init_invalid_type(self):
        with pytest.raises(TypeError):
            self.array_cls(None)
        with pytest.raises(TypeError):
            self.array_cls(1)

    def test_len(self) -> None:
        quat = self.cls()
        assert len(quat) == 4

    def test_getitem(self) -> None:
        quat = self.cls(*range(4))
        for i in range(4):
            assert isinstance(quat[i], float)
            assert quat[i] == i
            assert isinstance(quat[i - 4], float)
            assert quat[i - 4] == i

        with pytest.raises(IndexError) as excinfo:
            quat[4]
        assert str(excinfo.value) == 'index out of range'

        with pytest.raises(IndexError) as excinfo:
            quat[-5]
        assert str(excinfo.value) == 'index out of range'

    def test_array_getitem(self) -> None:
        with pytest.raises(IndexError) as excinfo:
            self.array_cls()[0]
        assert str(excinfo.value) == 'index out of range'

        array = self.array_cls(*(self.cls(i) for i in range(10)))
        for i in range(10):
            assert isinstance(array[i], self.cls)
            assert array[i] == self.cls(i)
            assert isinstance(array[i - 10], self.cls)
            assert array[i - 10] == self.cls(i)

        with pytest.raises(IndexError) as excinfo:
            array[10]
        assert str(excinfo.value) == 'index out of range'

        with pytest.raises(IndexError) as excinfo:
            array[-11]
        assert str(excinfo.value) == 'index out of range'

    def test_setitem(self) -> None:
        quat = self.cls(*range(4))
        for i in range(4):
            with pytest.raises(TypeError):
                quat[i] = 99
            with pytest.raises(TypeError):
                quat[i - 4] = 99

    def test_array_setitem(self) -> None:
        array = self.array_cls(self.cls(1))
        with pytest.raises(TypeError):
            array[0] = self.cls(2)

    def test_component_attributes(self) -> None:
        quat = self.cls(*range(4))
        assert quat.w == 0
        assert quat.x == 1
        assert quat.y == 2
        assert quat.z == 3

        with pytest.raises(AttributeError):
            quat.w = 99
        with pytest.raises(AttributeError):
            quat.x = 99
        with pytest.raises(AttributeError):
            quat.y = 99
        with pytest.raises(AttributeError):
            quat.z = 99

    def test_hash(self) -> None:
        for i in range(-100, 100):
            assert hash(self.cls(i)) == hash(self.cls(i))
            assert hash(self.cls(*(i for _ in range(4)))) == hash(
                self.cls(*(i for _ in range(4)))
            )

        assert hash(self.cls(0)) != hash(self.cls(-1))
        assert hash(self.cls(0)) != hash(self.cls(1))
        assert hash(self.cls(1)) != hash(self.cls(-1))
        assert hash(self.cls(0)) != hash(
            self.cls(*range(4))
        )

    def test_array_hash(self) -> None:
        assert hash(self.array_cls()) != hash(self.array_cls(self.cls(0)))
        assert hash(self.array_cls(self.cls(0))) != hash(
            self.array_cls(self.cls(1))
        )
        assert hash(self.array_cls(self.cls(1))) == hash(
            self.array_cls(self.cls(1))
        )
        assert hash(self.array_cls(self.cls(-1))) != (
            hash(self.array_cls(self.cls(1)))
        )

    def test_repr(self) -> None:
        quat = self.cls(*range(4))
        assert repr(quat) == (
            f'{quat.__class__.__name__}(' +
            ', '.join(repr(quat[i]) for i in range(4)) +
            f')'
        )

    def test_array_repr(self) -> None:
        assert repr(self.array_cls()) == f'{self.array_cls.__name__}[0]'
        assert repr(self.array_cls(self.cls())) == (
            f'{self.array_cls.__name__}[1]'
        )
        assert repr(self.array_cls(*(self.cls() for _ in range(100)))) == (
            f'{self.array_cls.__name__}[100]'
        )

    def test_iterate(self) -> None:
        quat = self.cls(*range(4))
        for i, c in enumerate(quat):
            assert c == i
            assert isinstance(c, float)

    def test_weakref(self) -> None:
        quat = self.cls()
        weak_vector = ref(quat)

    def test_array_weakref(self) -> None:
        array = self.array_cls()
        weak_array = ref(array)

    def test_equal(self) -> None:
        for i in range(-100, 100):
            assert self.cls(i) == self.cls(i)
            assert self.cls(*(i for _ in range(4))) == self.cls(*(
                i for _ in range(4)
            ))

        assert not (self.cls(0) == self.cls(1))
        assert not (self.cls(-1) == self.cls(1))

        assert not (self.cls() == 1)
        assert not (self.cls() == object())
        assert not (1 == self.cls())
        assert not (object() == self.cls())

    def test_array_equal(self) -> None:
        assert self.array_cls() == self.array_cls()
        for i in range(-100, 100):
            assert self.array_cls(self.cls(i)) == self.array_cls(self.cls(i))
            assert not (
                self.array_cls(self.cls(i), self.cls(i)) ==
                self.array_cls(self.cls(i))
            )

        assert not (self.array_cls() == 1)
        assert not (self.array_cls() == object())
        assert not (1 == self.array_cls())
        assert not (object() == self.array_cls())

    def test_not_equal(self) -> None:
        for i in range(-100, 100):
            assert not (self.cls(i) != self.cls(i))
            assert not (self.cls(*(i for _ in range(4))) != self.cls(*(
                i for _ in range(4)
            )))
        assert self.cls(0) != self.cls(1)
        assert self.cls(-1) != self.cls(1)

        assert self.cls() != 1
        assert self.cls() != object()

    def test_array_not_equal(self) -> None:
        assert not (self.array_cls() != self.array_cls())
        for i in range(-100, 100):
            assert not (
                self.array_cls(self.cls(i)) != self.array_cls(self.cls(i))
            )
            assert (
                self.array_cls(self.cls(i), self.cls(i)) !=
                self.array_cls(self.cls(i))
            )

        assert self.array_cls() != 1
        assert self.array_cls() != object()
        assert 1 != self.array_cls()
        assert object() != self.array_cls()

    def test_comparisons_not_implemented(self) -> None:
        a = self.cls()
        b = self.cls()
        with pytest.raises(TypeError):
            a < b
        with pytest.raises(TypeError):
            a <= b
        with pytest.raises(TypeError):
            a > b
        with pytest.raises(TypeError):
            a >= b

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

    def test_add(self) -> None:
        assert self.cls(-1) + self.cls(-1) == self.cls(-2)
        assert self.cls(1) + self.cls(-1) == self.cls(0)
        self.cls(self.cls.get_limits()[1]) + self.cls(1)
        assert self.cls(1) + self.cls(1) == self.cls(2)

        quat = self.cls(*range(4))
        assert quat + quat == self.cls(*(i + i for i in range(4)))

        i_quat = quat
        i_quat += quat
        assert i_quat is not quat
        assert quat == self.cls(*range(4))
        assert i_quat == self.cls(*(i + i for i in range(4)))

        with pytest.raises(TypeError):
            quat + 1
        with pytest.raises(TypeError):
            1 + quat
        with pytest.raises(TypeError):
            quat + None
        with pytest.raises(TypeError):
            None + quat
        with pytest.raises(TypeError):
            quat + '123'
        with pytest.raises(TypeError):
            '123' + quat
        with pytest.raises(TypeError):
            quat + object()
        with pytest.raises(TypeError):
            object() + quat

    def test_sub(self) -> None:
        assert self.cls(-1) - self.cls(-1) == self.cls(0)
        assert self.cls(1) - self.cls(-1) == self.cls(2)
        self.cls(self.cls.get_limits()[0]) - self.cls(1)
        assert self.cls(1) - self.cls(1) == self.cls(0)

        quat = self.cls(*range(4))
        assert quat - quat == self.cls(*(i - i for i in range(4)))

        i_quat = quat
        i_quat -= quat
        assert i_quat is not quat
        assert quat == self.cls(*range(4))
        assert i_quat == self.cls(*(i - i for i in range(4)))

        with pytest.raises(TypeError):
            quat - 1
        with pytest.raises(TypeError):
            1 - quat
        with pytest.raises(TypeError):
            quat - None
        with pytest.raises(TypeError):
            None - quat
        with pytest.raises(TypeError):
            quat - '123'
        with pytest.raises(TypeError):
            '123' - quat
        with pytest.raises(TypeError):
            quat - object()
        with pytest.raises(TypeError):
            object() - quat

    def test_multiply(self) -> None:
        assert self.cls(1) * -1 == self.cls(-1)
        assert self.cls(1) * 0 == self.cls(0)
        assert self.cls(1) * 1 == self.cls(1)
        assert -1 * self.cls(1) == self.cls(-1)
        assert 0 * self.cls(1) == self.cls(0)
        assert 1 * self.cls(1) == self.cls(1)

        quat = self.cls(*range(4))
        assert quat * 2 == self.cls(*(i * 2 for i in range(4)))
        assert 2 * quat == self.cls(*(i * 2 for i in range(4)))

        i_quat = quat
        i_quat *= 2
        assert i_quat is not quat
        assert quat == self.cls(*range(4))
        assert i_quat == self.cls(*(i * 2 for i in range(4)))

        with pytest.raises(TypeError):
            quat * self.cls()
        with pytest.raises(TypeError):
            self.cls() * quat
        with pytest.raises(TypeError):
            quat * None
        with pytest.raises(TypeError):
            None * quat
        with pytest.raises(TypeError):
            quat * '123'
        with pytest.raises(TypeError):
            '123' * quat
        with pytest.raises(TypeError):
            quat * object()
        with pytest.raises(TypeError):
            object() * quat

    def test_matrix_multiply(self) -> None:
        vector3_cls = globals()[f'{self.cls.__name__[0]}Vector3']
        vector4_cls = globals()[f'{self.cls.__name__[0]}Vector4']

        assert self.cls() @ self.cls() == 0.0
        assert self.cls(1) @ self.cls(1) == sum(
            self.cls(1)[i] * self.cls(1)[i]
            for i in range(4)
        )
        assert self.cls(*range(4)) @ self.cls(*range(4)) == sum(
            self.cls(*range(4))[i] * self.cls(*range(4))[i]
            for i in range(4)
        )

        quat = vector3_cls(0, radians(90), 0).to_quaternion()
        rotated_vec = quat @ vector3_cls(1, 0, 0)
        assert isclose(rotated_vec.x, 0)
        assert isclose(rotated_vec.y, 0)
        assert isclose(rotated_vec.z, -1)
        rotated_vec = vector3_cls(1, 0, 0) @ quat
        assert isclose(rotated_vec.x, 0)
        assert isclose(rotated_vec.y, 0)
        assert isclose(rotated_vec.z, 1)
        rotated_vec = quat @ vector3_cls(0, 0, 1)
        assert isclose(rotated_vec.x, 1)
        assert isclose(rotated_vec.y, 0)
        assert isclose(rotated_vec.z, 0)
        rotated_vec = vector3_cls(0, 0, 1) @ quat
        assert isclose(rotated_vec.x, -1)
        assert isclose(rotated_vec.y, 0)
        assert isclose(rotated_vec.z, 0)
        rotated_vec = quat @ vector4_cls(1, 0, 0, 1)
        assert isclose(rotated_vec.x, 0)
        assert isclose(rotated_vec.y, 0)
        assert isclose(rotated_vec.z, -1)
        assert isclose(rotated_vec.w, 1)
        rotated_vec = vector4_cls(1, 0, 0, 1) @ quat
        assert isclose(rotated_vec.x, 0)
        assert isclose(rotated_vec.y, 0)
        assert isclose(rotated_vec.z, 1)
        assert isclose(rotated_vec.w, 1)
        rotated_vec = quat @ vector4_cls(0, 0, 1, 1)
        assert isclose(rotated_vec.x, 1)
        assert isclose(rotated_vec.y, 0)
        assert isclose(rotated_vec.z, 0)
        assert isclose(rotated_vec.w, 1)
        rotated_vec = vector4_cls(0, 0, 1, 1) @ quat
        assert isclose(rotated_vec.x, -1)
        assert isclose(rotated_vec.y, 0)
        assert isclose(rotated_vec.z, 0)
        assert isclose(rotated_vec.w, 1)

        with pytest.raises(TypeError):
            quat @ None
        with pytest.raises(TypeError):
            quat @ '123'
        with pytest.raises(TypeError):
            quat @ object()
        with pytest.raises(TypeError):
            None @ quat
        with pytest.raises(TypeError):
            '123' @ quat
        with pytest.raises(TypeError):
            object() @ quat

    '''
    def test_divide(self) -> None:
        if self.type == bool:
            with pytest.raises(TypeError):
                self.cls() / self.cls()
            return

        if not self.unsigned:
            assert self.cls(-1) / self.cls(-2) == self.cls(self.type(.5))
            assert self.cls(-1) / -2 == self.cls(self.type(.5))
            assert -1 / self.cls(-2) == self.cls(self.type(.5))
            assert self.cls(1) / self.cls(-2) == self.cls(self.type(-.5))
            assert self.cls(1) / -2 == self.cls(self.type(-.5))
            assert 1 / self.cls(-2) == self.cls(self.type(-.5))

        assert self.cls(1) / self.cls(2) == self.cls(self.type(.5))
        assert self.cls(1) / 2 == self.cls(self.type(.5))
        assert 1 / self.cls(2) == self.cls(self.type(.5))

        if self.type == float:
            assert self.cls(1) / 0 == self.cls(inf)
            assert 1 / self.cls(0) == self.cls(inf)
            assert self.cls(1) / self.cls(0) == self.cls(inf)
        else:
            with pytest.raises(ZeroDivisionError):
                assert self.cls(1) / 0
            with pytest.raises(ZeroDivisionError):
                assert 1 / self.cls(0)
            with pytest.raises(ZeroDivisionError):
                assert self.cls(1) / self.cls(0)

        vector = self.cls(*range(1, self.component_count + 1))
        assert vector / vector == self.cls(*(
            self.type(i / i) for i in range(1, self.component_count + 1)
        ))
        assert vector / 2 == self.cls(*(
            self.type(i / 2) for i in range(1, self.component_count + 1)
        ))
        assert 2 / vector == self.cls(*(
            self.type(2 / i) for i in range(1, self.component_count + 1)
        ))

        i_vec = vector
        i_vec /= vector
        assert i_vec is not vector
        assert vector == self.cls(*range(1, self.component_count + 1))
        assert i_vec == self.cls(*(
            self.type(i / i) for i in range(1, self.component_count + 1)
        ))

        i_vec = vector
        i_vec /= 2
        assert i_vec is not vector
        assert vector == self.cls(*range(1, self.component_count + 1))
        assert i_vec == self.cls(*(
            self.type(i / 2) for i in range(1, self.component_count + 1)
        ))

        with pytest.raises(TypeError):
            vector / None
        with pytest.raises(TypeError):
            None / vector
        with pytest.raises(TypeError):
            vector / '123'
        with pytest.raises(TypeError):
            '123' / vector
        with pytest.raises(TypeError):
            vector / object()
        with pytest.raises(TypeError):
            object() / vector


    def test_modulus(self) -> None:
        if self.type != float:
            with pytest.raises(TypeError):
                self.cls() % self.cls()
            return

        assert self.cls(-3) % self.cls(-2) == self.cls(-1)
        assert self.cls(-3) % -2 == self.cls(-1)
        assert -3 % self.cls(-2) == self.cls(-1)
        assert self.cls(3) % self.cls(-2) == self.cls(-1)
        assert self.cls(3) % -2 == self.cls(-1)
        assert 3 % self.cls(-2) == self.cls(-1)
        assert self.cls(3) % self.cls(2) == self.cls(1)
        assert self.cls(3) % 2 == self.cls(1)
        assert 3 % self.cls(2) == self.cls(1)

        assert all(isnan(c) for c in self.cls(1) % 0)
        assert all(isnan(c) for c in self.cls(1) % self.cls(0))

        vector = self.cls(*range(1, self.component_count + 1))
        assert vector % vector == self.cls(*(
            i % i for i in range(1, self.component_count + 1)
        ))
        assert vector % 2 == self.cls(*(
            i % 2 for i in range(1, self.component_count + 1)
        ))
        assert 2 % vector == self.cls(*(
            2 % i for i in range(1, self.component_count + 1)
        ))

        i_vec = vector
        i_vec %= vector
        assert i_vec is not vector
        assert vector == self.cls(*range(1, self.component_count + 1))
        assert i_vec == self.cls(*(
            i % i for i in range(1, self.component_count + 1)
        ))

        i_vec = vector
        i_vec %= 2
        assert i_vec is not vector
        assert vector == self.cls(*range(1, self.component_count + 1))
        assert i_vec == self.cls(*(
            i % 2 for i in range(1, self.component_count + 1)
        ))

        with pytest.raises(TypeError):
            vector % None
        with pytest.raises(TypeError):
            None % vector
        with pytest.raises(TypeError):
            vector % '123'
        with pytest.raises(TypeError):
            '123' % vector
        with pytest.raises(TypeError):
            vector % object()
        with pytest.raises(TypeError):
            object() % vector


    def test_power(self) -> None:
        if self.type != float:
            with pytest.raises(TypeError):
                self.cls() ** self.cls()
            return

        assert self.cls(-3) ** self.cls(-2) == self.cls(3 ** -2)
        assert self.cls(-3) ** -2 == self.cls(3 ** -2)
        assert (-3) ** self.cls(-2) == self.cls(3 ** -2)
        assert self.cls(3) ** self.cls(-2) == self.cls(3 ** -2)
        assert self.cls(3) ** -2 == self.cls(3 ** -2)
        assert 3 ** self.cls(-2) == self.cls(3 ** -2)
        assert self.cls(3) ** self.cls(2) == self.cls(9)
        assert self.cls(3) ** 2 == self.cls(9)
        assert 3 ** self.cls(2) == self.cls(9)

        assert self.cls(5) ** 0 == self.cls(1)
        assert 5 ** self.cls(0) == self.cls(1)
        assert self.cls(5) ** self.cls(0) == self.cls(1)

        vector = self.cls(*range(1, self.component_count + 1))
        assert vector ** vector == self.cls(*(
            i ** i for i in range(1, self.component_count + 1)
        ))
        assert vector ** 2 == self.cls(*(
            i ** 2 for i in range(1, self.component_count + 1)
        ))
        assert 2 ** vector == self.cls(*(
            2 ** i for i in range(1, self.component_count + 1)
        ))

        i_vec = vector
        i_vec **= vector
        assert i_vec is not vector
        assert vector == self.cls(*range(1, self.component_count + 1))
        assert i_vec == self.cls(*(
            i ** i for i in range(1, self.component_count + 1)
        ))

        i_vec = vector
        i_vec **= 2
        assert i_vec is not vector
        assert vector == self.cls(*range(1, self.component_count + 1))
        assert i_vec == self.cls(*(
            i ** 2 for i in range(1, self.component_count + 1)
        ))

        with pytest.raises(TypeError):
            vector ** None
        with pytest.raises(TypeError):
            vector ** '123'
        with pytest.raises(TypeError):
            vector ** object()
        with pytest.raises(TypeError):
            None ** vector
        with pytest.raises(TypeError):
            '123' ** vector
        with pytest.raises(TypeError):
            object() ** vector

    def test_negative(self) -> None:
        if self.unsigned:
            with pytest.raises(TypeError):
                -self.cls(0)
            return

        assert -self.cls(0) == self.cls(-0)
        assert -self.cls(1) == self.cls(-1)
        assert -self.cls(-1) == self.cls(1)

        vector = self.cls(*range(self.component_count))
        assert -vector == self.cls(*(
            -i for i in range(self.component_count)
        ))

    def test_abs(self) -> None:
        assert abs(self.cls(0)) == self.cls(0)
        assert abs(self.cls(1)) == self.cls(1)
        if not self.unsigned:
            assert abs(self.cls(-1)) == self.cls(1)

        vector = self.cls(*range(self.component_count))
        assert abs(vector) == self.cls(*(range(self.component_count)))
        if not self.unsigned:
            assert abs(-vector) == self.cls(*(range(self.component_count)))

    def test_bool(self) -> None:
        assert self.cls(1)
        if not self.unsigned:
            assert self.cls(-1)
        assert not self.cls(0)

        for i in range(self.component_count):
            components = [1] * self.component_count
            components[i] = 0
            assert not self.cls(*components)

    def test_array_bool(self) -> None:
        assert not self.array_cls()
        assert self.array_cls(self.cls())

    def test_buffer(self) -> None:
        assert bytes(self.cls(*range(self.component_count))) == struct.pack(
            self.struct_byte_order + (
                self.struct_format * self.component_count
            ),
            *range(self.component_count)
        )
        memory_view = memoryview(self.cls(0))
        assert memory_view.readonly
        assert memory_view.format == (
            self.struct_byte_order + self.struct_format
        )
        assert memory_view.itemsize == struct.calcsize(
            self.struct_byte_order + self.struct_format
        )
        assert memory_view.ndim == 1
        assert memory_view.shape == (self.component_count,)
        assert memory_view.strides == (struct.calcsize(
            self.struct_byte_order + self.struct_format
        ),)
        assert memory_view.suboffsets == tuple()
        assert memory_view.c_contiguous
        assert memory_view.f_contiguous
        assert memory_view.contiguous

    def test_array_buffer(self) -> None:
        assert bytes(self.array_cls()) == b''

        array = self.array_cls(
            self.cls(1),
            self.cls(*range(self.component_count)),
            self.cls(0),
        )
        assert bytes(array) == struct.pack(
            self.struct_byte_order + (
                self.struct_format * 3 * self.component_count
            ),
            *(1 for _ in range(self.component_count)),
            *range(self.component_count),
            *(0 for _ in range(self.component_count)),
        )
        memory_view = memoryview(array)
        assert memory_view.readonly
        assert memory_view.format == (
            self.struct_byte_order + self.struct_format
        )
        assert memory_view.itemsize == struct.calcsize(
            self.struct_byte_order + self.struct_format
        )
        assert memory_view.ndim == 2
        assert memory_view.shape == (3, self.component_count)
        assert memory_view.strides == (
            struct.calcsize(self.struct_byte_order + self.struct_format) *
            self.component_count,
            struct.calcsize(self.struct_byte_order + self.struct_format),
        )
        assert memory_view.suboffsets == tuple()
        assert memory_view.c_contiguous
        assert not memory_view.f_contiguous
        assert memory_view.contiguous

    def test_cross(self) -> None:
        if self.component_count != 3 or self.type != float:
            with pytest.raises(AttributeError):
                self.cls().cross(self.cls())
            return

        assert self.cls(1).cross(self.cls(1)) == self.cls(0)
        assert self.cls(0).cross(self.cls(1)) == self.cls(0)
        assert self.cls(1).cross(self.cls(0)) == self.cls(0)
        assert self.cls(1).cross(self.cls(-1)) == self.cls(0)
        assert self.cls(1, 2, 3).cross(self.cls(4, 5, 6)) == (
            self.cls(-3, 6, -3)
        )

        with pytest.raises(TypeError) as excinfo:
            self.cls(0).cross(None)
        assert str(excinfo.value) == f'{None!r} is not {self.cls.__name__}'
        with pytest.raises(TypeError) as excinfo:
            self.cls(0).cross(1)
        assert str(excinfo.value) == f'{1!r} is not {self.cls.__name__}'

    def test_magnitude(self) -> None:
        if self.type != float:
            with pytest.raises(AttributeError):
                self.cls().magnitude
            return

        assert isclose(
            self.cls(-1).magnitude,
            sqrt(sum(1 ** 2 for _ in range(self.component_count)))
        )
        assert isclose(
            self.cls(1).magnitude,
            sqrt(sum(1 ** 2 for _ in range(self.component_count)))
        )
        assert isclose(
            self.cls(-2).magnitude,
            sqrt(sum(2 ** 2 for _ in range(self.component_count)))
        )
        assert isclose(
            self.cls(2).magnitude,
            sqrt(sum(2 ** 2 for _ in range(self.component_count)))
        )
        assert isclose(
            self.cls(*range(self.component_count)).magnitude,
            sqrt(sum(i ** 2 for i in range(self.component_count)))
        )

        with pytest.raises(AttributeError):
            self.cls().magnitude = 1

    def test_normalize(self) -> None:
        if self.type != float:
            with pytest.raises(AttributeError):
                self.cls().normalize()
            return

        assert all(isnan(c) for c in self.cls(0).normalize())

        vector = self.cls(1)
        assert vector.normalize() == vector / vector.magnitude
        vector = self.cls(-1)
        assert vector.normalize() == vector / vector.magnitude

        vector = self.cls(*range(self.component_count))
        assert vector.normalize() == vector / vector.magnitude


    def test_distance(self) -> None:
        if self.type != float:
            with pytest.raises(AttributeError):
                self.cls().distance(self.cls())
            return

        assert self.cls(-1).distance(self.cls(-1)) == 0
        assert self.cls(0).distance(self.cls(0)) == 0
        assert self.cls(1).distance(self.cls(1)) == 0

        assert isclose(
            self.cls(0).distance(self.cls(1)),
            sqrt(sum((0 - 1) ** 2 for _ in range(self.component_count)))
        )

        vector_a = self.cls(*range(self.component_count))
        vector_b = self.cls(*(-i for i in range(self.component_count)))
        assert isclose(
            vector_a.distance(vector_b),
            sqrt(sum((a - b) ** 2 for a, b in zip(vector_a, vector_b)))
        )

        with pytest.raises(TypeError) as excinfo:
            self.cls(0).distance(None)
        assert str(excinfo.value) == f'{None!r} is not {self.cls.__name__}'
        with pytest.raises(TypeError) as excinfo:
            self.cls(0).distance(1)
        assert str(excinfo.value) == f'{1!r} is not {self.cls.__name__}'

    def test_pointer(self) -> None:
        real_type = {
            '?': ctypes.c_bool,
            'd': ctypes.c_double,
            'f': ctypes.c_float,
            '=b': ctypes.c_int8,
            '=B': ctypes.c_uint8,
            '=h': ctypes.c_int16,
            '=H': ctypes.c_uint16,
            '=i': ctypes.c_int32,
            '=I': ctypes.c_uint32,
            '=q': ctypes.c_int64,
            '=Q': ctypes.c_uint64,
            'i': ctypes.c_int,
            'I': ctypes.c_uint,
        }[self.struct_byte_order + self.struct_format]
        vector = self.cls(*range(self.component_count))
        assert isinstance(vector.pointer, ctypes.POINTER(real_type))
        for i in range(self.component_count):
            vector.pointer[i] == self.type(i)

    def test_array_pointer(self) -> None:
        real_type = {
            '?': ctypes.c_bool,
            'd': ctypes.c_double,
            'f': ctypes.c_float,
            '=b': ctypes.c_int8,
            '=B': ctypes.c_uint8,
            '=h': ctypes.c_int16,
            '=H': ctypes.c_uint16,
            '=i': ctypes.c_int32,
            '=I': ctypes.c_uint32,
            '=q': ctypes.c_int64,
            '=Q': ctypes.c_uint64,
            'i': ctypes.c_int,
            'I': ctypes.c_uint,
        }[self.struct_byte_order + self.struct_format]
        array = self.array_cls(
            self.cls(*range(self.component_count)),
            self.cls(0),
        )
        assert isinstance(array.pointer, ctypes.POINTER(real_type))
        for i in (
            *range(self.component_count),
            *(0 for _ in range(self.component_count))
        ):
            array.pointer[i] == self.type(i)
    '''

class TestFQuaternion(
    VectorTest,
    cls=FQuaternion,
    struct_format='f'
):
    pass


class TestDVector2(
    VectorTest,
    cls=DQuaternion,
    struct_format='d'
):
    pass

