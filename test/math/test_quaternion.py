
# gamut
from gamut.math import (DMatrix3x3, DMatrix4x4, DQuaternion, DQuaternionArray,
                        DVector3, DVector4, FMatrix3x3, FMatrix4x4,
                        FQuaternion, FQuaternionArray, FVector3, FVector4)
# python
import ctypes
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


class QuaternionTest:

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

        assert isinstance(array[1:3], self.array_cls)
        assert array[1:3] == self.array_cls(
            self.cls(1),
            self.cls(2),
        )
        assert array[-3:-1] == self.array_cls(
            self.cls(7),
            self.cls(8),
        )
        assert array[::2] == self.array_cls(
            self.cls(0),
            self.cls(2),
            self.cls(4),
            self.cls(6),
            self.cls(8),
        )

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
        vector3_cls = globals()[f'{self.cls.__name__[0]}Vector3']

        assert self.cls(1) * -1 == self.cls(-1)
        assert self.cls(1) * 0 == self.cls(0)
        assert self.cls(1) * 1 == self.cls(1)
        assert -1 * self.cls(1) == self.cls(-1)
        assert 0 * self.cls(1) == self.cls(0)
        assert 1 * self.cls(1) == self.cls(1)

        assert self.cls(1) * self.cls(1) == self.cls(1)
        assert (
            self.cls(1) *
            self.cls(1).rotate(radians(90), vector3_cls(1, 0, 0)) ==
            self.cls(1).rotate(radians(90), vector3_cls(1, 0, 0))
        )
        assert (
            self.cls(1).rotate(radians(90), vector3_cls(1, 0, 0)) *
            self.cls(1) ==
            self.cls(1).rotate(radians(90), vector3_cls(1, 0, 0))
        )
        assert (
            self.cls(1).rotate(radians(90), vector3_cls(1, 0, 0)) *
            self.cls(1).rotate(radians(90), vector3_cls(0, 1, 0)) ==
            self.cls(1)
                .rotate(radians(90), vector3_cls(1, 0, 0))
                .rotate(radians(90), vector3_cls(0, 1, 0))
        )

        quat = self.cls(*range(4))
        assert quat * 2 == self.cls(*(i * 2 for i in range(4)))
        assert 2 * quat == self.cls(*(i * 2 for i in range(4)))

        i_quat = quat
        i_quat *= 2
        assert i_quat is not quat
        assert quat == self.cls(*range(4))
        assert i_quat == self.cls(*(i * 2 for i in range(4)))

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

    def test_divide(self) -> None:
        assert self.cls(-1) / -1 == self.cls(1)
        assert self.cls(1) / 1 == self.cls(1)
        zero_div = self.cls(1) / 0
        assert zero_div.w == inf
        assert isnan(zero_div.x)
        assert isnan(zero_div.y)
        assert isnan(zero_div.z)

        quat = self.cls(*range(4))
        assert quat / 2 == self.cls(*(i / 2 for i in range(4)))

        i_quat = quat
        i_quat /= 2
        assert i_quat is not quat
        assert quat == self.cls(*range(4))
        assert i_quat == self.cls(*(i / 2 for i in range(4)))

        with pytest.raises(TypeError):
            quat / quat
        with pytest.raises(TypeError):
            quat / None
        with pytest.raises(TypeError):
            None / quat
        with pytest.raises(TypeError):
            quat / '123'
        with pytest.raises(TypeError):
            '123' / quat
        with pytest.raises(TypeError):
            quat / object()
        with pytest.raises(TypeError):
            object() / quat

    def test_negative(self) -> None:
        assert -self.cls(0) == self.cls(-0)
        assert -self.cls(1) == self.cls(-1)
        assert -self.cls(-1) == self.cls(1)

        quat = self.cls(*range(4))
        assert -quat == self.cls(*(-i for i in range(4)))

    def test_bool(self) -> None:
        assert self.cls(1)
        assert self.cls(-1)
        assert self.cls(0)

    def test_array_bool(self) -> None:
        assert not self.array_cls()
        assert self.array_cls(self.cls())

    def test_buffer(self) -> None:
        assert bytes(self.cls(*range(4))) == struct.pack(
            self.struct_format * 4,
            *range(4)
        )
        memory_view = memoryview(self.cls(0))
        assert memory_view.readonly
        assert memory_view.format == self.struct_format
        assert memory_view.itemsize == struct.calcsize(self.struct_format)
        assert memory_view.ndim == 1
        assert memory_view.shape == (4,)
        assert memory_view.strides == (struct.calcsize(self.struct_format),)
        assert memory_view.suboffsets == tuple()
        assert memory_view.c_contiguous
        assert memory_view.f_contiguous
        assert memory_view.contiguous

    def test_array_buffer(self) -> None:
        assert bytes(self.array_cls()) == b''

        array = self.array_cls(
            self.cls(1, 1, 1, 1),
            self.cls(*range(4)),
            self.cls(0),
        )
        assert bytes(array) == struct.pack(
            self.struct_format * 3 * 4,
            *(1 for _ in range(4)),
            *range(4),
            *(0 for _ in range(4)),
        )
        memory_view = memoryview(array)
        assert memory_view.readonly
        assert memory_view.format == self.struct_format
        assert memory_view.itemsize == struct.calcsize(self.struct_format)
        assert memory_view.ndim == 2
        assert memory_view.shape == (3, 4)
        assert memory_view.strides == (
            struct.calcsize(self.struct_format) * 4,
            struct.calcsize(self.struct_format),
        )
        assert memory_view.suboffsets == tuple()
        assert memory_view.c_contiguous
        assert not memory_view.f_contiguous
        assert memory_view.contiguous

    def test_cross(self) -> None:
        vector3_cls = globals()[f'{self.cls.__name__[0]}Vector3']
        result = self.cls(1, 2, 3, 4).cross(self.cls(5, 6, 7, 8))
        assert result == self.cls(
            1 * 5 - (vector3_cls(2, 3, 4) @ vector3_cls(6, 7, 8)),
            *(1 * vector3_cls(6, 7, 8) + 5 * vector3_cls(2, 3, 4) + (
                vector3_cls(2, 3, 4).cross(vector3_cls(6, 7, 8))
            ))
        )

        with pytest.raises(TypeError) as excinfo:
            self.cls(0).cross(None)
        assert str(excinfo.value) == f'{None!r} is not {self.cls.__name__}'
        with pytest.raises(TypeError) as excinfo:
            self.cls(0).cross(1)
        assert str(excinfo.value) == f'{1!r} is not {self.cls.__name__}'

    def test_magnitude(self) -> None:
        assert isclose(
            self.cls(-1, -1, -1, -1).magnitude,
            sqrt(sum(1 ** 2 for _ in range(4)))
        )
        assert isclose(
            self.cls(1, 1, 1, 1).magnitude,
            sqrt(sum(1 ** 2 for _ in range(4)))
        )
        assert isclose(
            self.cls(-2, -2, -2, -2).magnitude,
            sqrt(sum(2 ** 2 for _ in range(4)))
        )
        assert isclose(
            self.cls(2, 2, 2, 2).magnitude,
            sqrt(sum(2 ** 2 for _ in range(4)))
        )
        assert isclose(
            self.cls(*range(4)).magnitude,
            sqrt(sum(i ** 2 for i in range(4)))
        )

        with pytest.raises(AttributeError):
            self.cls().magnitude = 1

    def test_normalize(self) -> None:
        assert self.cls(0).normalize() == self.cls(1)

        quat = self.cls(1)
        assert quat.normalize() == quat / quat.magnitude
        quat = self.cls(-1)
        assert quat.normalize() == quat / quat.magnitude

        quat = self.cls(*range(4))
        assert quat.normalize() == quat / quat.magnitude

    def test_pointer(self) -> None:
        real_type = {
            'd': ctypes.c_double,
            'f': ctypes.c_float,
        }[self.struct_format]
        quat = self.cls(*range(4))
        assert isinstance(quat.pointer, ctypes.POINTER(real_type))
        for i in range(4):
            quat.pointer[i] == i

    def test_array_pointer(self) -> None:
        real_type = {
            'd': ctypes.c_double,
            'f': ctypes.c_float,
        }[self.struct_format]
        array = self.array_cls(
            self.cls(*range(4)),
            self.cls(0),
        )
        assert isinstance(array.pointer, ctypes.POINTER(real_type))
        for i in (
            *range(4),
            *(0 for _ in range(4))
        ):
            array.pointer[i] == i

    def test_inverse(self) -> None:
        assert self.cls(1).inverse() == self.cls(1, -0, -0, -0)

    def test_rotate(self) -> None:
        vector3_cls = globals()[f'{self.cls.__name__[0]}Vector3']

        with pytest.raises(TypeError):
            self.cls(1).rotate(radians(90))
        with pytest.raises(TypeError):
            self.cls(1).rotate(radians(90), vector3_cls(), None)
        with pytest.raises(TypeError):
            self.cls(1).rotate(None, vector3_cls())
        with pytest.raises(TypeError):
            self.cls(1).rotate(1, None)

        rotation = self.cls(1).rotate(radians(90), vector3_cls(0, 1, 0))
        assert isclose(rotation.w, 0.7071067690849304)
        assert isclose(rotation.x, 0)
        assert isclose(rotation.y, 0.7071067690849304)
        assert isclose(rotation.z, 0)

    def test_to_matrix3(self) -> None:
        vector3_cls = globals()[f'{self.cls.__name__[0]}Vector3']
        matrix3_cls = globals()[f'{self.cls.__name__[0]}Matrix3x3']
        assert isinstance(self.cls(1).to_matrix3(), matrix3_cls)
        assert self.cls(1).to_matrix3() == matrix3_cls(1)

        rot_quat = self.cls(1).rotate(radians(90), vector3_cls(0, 1, 0))
        rot_mat = rot_quat.to_matrix3()
        assert isclose(rot_mat[0].x, 0)
        assert isclose(rot_mat[0].y, 0)
        assert isclose(rot_mat[0].z, -1)
        assert isclose(rot_mat[1].x, 0)
        assert isclose(rot_mat[1].y, 1)
        assert isclose(rot_mat[1].z, 0)
        assert isclose(rot_mat[2].x, 1)
        assert isclose(rot_mat[2].y, 0)
        assert isclose(rot_mat[2].z, 0)

    def test_to_matrix4(self) -> None:
        vector3_cls = globals()[f'{self.cls.__name__[0]}Vector3']
        matrix4_cls = globals()[f'{self.cls.__name__[0]}Matrix4x4']
        assert isinstance(self.cls(1).to_matrix4(), matrix4_cls)
        assert self.cls(1).to_matrix4() == matrix4_cls(1)

        rot_quat = self.cls(1).rotate(radians(90), vector3_cls(0, 1, 0))
        rot_mat = rot_quat.to_matrix4()
        assert isclose(rot_mat[0].x, 0)
        assert isclose(rot_mat[0].y, 0)
        assert isclose(rot_mat[0].z, -1)
        assert isclose(rot_mat[0].w, 0)
        assert isclose(rot_mat[1].x, 0)
        assert isclose(rot_mat[1].y, 1)
        assert isclose(rot_mat[1].z, 0)
        assert isclose(rot_mat[1].w, 0)
        assert isclose(rot_mat[2].x, 1)
        assert isclose(rot_mat[2].y, 0)
        assert isclose(rot_mat[2].z, 0)
        assert isclose(rot_mat[2].w, 0)
        assert isclose(rot_mat[3].x, 0)
        assert isclose(rot_mat[3].y, 0)
        assert isclose(rot_mat[3].z, 0)
        assert isclose(rot_mat[3].w, 1)

    def test_get_size(self) -> None:
        assert self.cls.get_size() == (
            struct.calcsize('=' + self.struct_format) *
            4
        )

    def test_array_size(self) -> None:
        assert self.array_cls().size == 0
        assert self.array_cls(self.cls()).size == (
            struct.calcsize('=' + self.struct_format) *
            4
        )
        assert self.array_cls(self.cls(), self.cls()).size == (
            struct.calcsize('=' + self.struct_format) *
            4 * 2
        )
    def test_from_buffer(self) -> None:
        for v in (
            self.cls(),
            self.cls(1),
            self.cls(*range(4))
        ):
            bv = self.cls.from_buffer(v)
            assert isinstance(bv, self.cls)
            assert bv == v
            assert self.cls.from_buffer(bytes(v)) == v

        with pytest.raises(TypeError):
            self.cls.from_buffer(None)
        with pytest.raises(BufferError):
            self.cls.from_buffer(b'')

    def test_from_array_buffer(self) -> None:
        for a in (
            self.array_cls(),
            self.array_cls(self.cls(1)),
            self.array_cls(
                self.cls(1),
                self.cls(*range(4))
            ),
        ):
            ba = self.array_cls.from_buffer(a)
            assert isinstance(ba, self.array_cls)
            assert ba == a
            assert self.array_cls.from_buffer(bytes(a)) == a

        with pytest.raises(TypeError):
            self.array_cls.from_buffer(None)
        with pytest.raises(BufferError):
            self.array_cls.from_buffer(b'\x00')

    def test_lerp(self) -> None:
        assert self.cls(0).lerp(self.cls(1), .5) == self.cls(1) * .5

    def test_array_get_array_type(self) -> None:
        assert self.cls.get_array_type() is self.array_cls

    def test_array_get_component_type(self) -> None:
        assert self.array_cls.get_component_type() is self.cls


class TestFQuaternion(
    QuaternionTest,
    cls=FQuaternion,
    struct_format='f'
):
    pass


class TestDQuaternion2(
    QuaternionTest,
    cls=DQuaternion,
    struct_format='d'
):
    pass
