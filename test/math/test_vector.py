
# gamut
from gamut.math import (BVector2, BVector3, BVector4, DVector2, DVector3,
                        DVector4, FVector2, FVector3, FVector4, I8Vector2,
                        I8Vector3, I8Vector4, I16Vector2, I16Vector3,
                        I16Vector4, I32Vector2, I32Vector3, I32Vector4,
                        I64Vector2, I64Vector3, I64Vector4, IVector2, IVector3,
                        IVector4, U8Vector2, U8Vector3, U8Vector4, U16Vector2,
                        U16Vector3, U16Vector4, U32Vector2, U32Vector3,
                        U32Vector4, U64Vector2, U64Vector3, U64Vector4,
                        UVector2, UVector3, UVector4)
# python
import itertools
from math import inf
from math import isclose as _isclose
from math import isnan, sqrt
import struct
from typing import Final
from weakref import ref
# pytest
import pytest


def isclose(a, b):
    return _isclose(a, b, rel_tol=1e-07)


class VectorTest:

    POSITION_ATTRIBUTES: Final = ('x', 'y', 'z', 'w')
    COLOR_ATTRIBUTES: Final = ('r', 'g', 'b', 'a')
    UV_ATTRIBUTES: Final = ('u', 'v')
    TEXTURE_ATTRIBUTES: Final = ('s', 't', 'p', 'q')

    def __init_subclass__(
        this_cls,
        *,
        cls,
        component_count,
        type,
        struct_format,
        struct_byte_order='',
        unsigned=False
    ):
        this_cls.cls = cls
        this_cls.component_count = component_count
        this_cls.type = type
        this_cls.struct_byte_order = struct_byte_order
        this_cls.struct_format = struct_format
        this_cls.unsigned = unsigned

    def test_empty_init(self) -> None:
        vector = self.cls()
        for i in range(self.component_count):
            assert vector[i] == 0

    def test_single_init(self) -> None:
        for arg in [-100, -1, 0, 1, 100]:
            if arg < 0 and self.unsigned:
                with pytest.raises(OverflowError):
                    self.cls(arg)
            else:
                vector = self.cls(arg)
                for i in range(self.component_count):
                    assert vector[i] == self.type(arg)
        if self.type is not bool:
            min, max = self.cls.get_limits()
            if self.type is float:
                assert self.cls(min - 1) == self.cls(min)
                assert self.cls(max + 1) == self.cls(max)
            else:
                with pytest.raises(OverflowError):
                    self.cls(min - 1)
                with pytest.raises(OverflowError):
                    self.cls(max + 1)

    def test_all_init(self) -> None:
        vector = self.cls(*range(self.component_count))
        for i in range(self.component_count):
            assert vector[i] == self.type(i)

    def test_invalid_arg_count(self) -> None:
        with pytest.raises(TypeError) as excinfo:
            vector = self.cls(*range(self.component_count + 1))
        assert str(excinfo.value) == (
            f'invalid number of arguments supplied to '
            f'{ self.cls.__name__ }, expected 0, 1 or '
            f'{ self.component_count } (got { self.component_count + 1 })'
        )

        for count in range(2, self.component_count):
            with pytest.raises(TypeError) as excinfo:
                vector = self.cls(*range(count))
            assert str(excinfo.value) == (
                f'invalid number of arguments supplied to '
                f'{ self.cls.__name__ }, expected 0, 1 or '
                f'{ self.component_count } (got { count })'
            )

    def test_len(self) -> None:
        vector = self.cls()
        assert len(vector) == self.component_count

    def test_getitem(self) -> None:
        vector = self.cls(*range(self.component_count))
        for i in range(self.component_count):
            assert isinstance(vector[i], self.type)
            assert vector[i] == self.type(i)
            assert isinstance(vector[i - self.component_count], self.type)
            assert vector[i - self.component_count] == self.type(i)

        with pytest.raises(IndexError) as excinfo:
            vector[self.component_count]
        assert str(excinfo.value) == 'index out of range'

        with pytest.raises(IndexError) as excinfo:
            vector[-(self.component_count + 1)]
        assert str(excinfo.value) == 'index out of range'

    def test_setitem(self) -> None:
        vector = self.cls(*range(self.component_count))
        for i in range(self.component_count):
            with pytest.raises(TypeError):
                vector[i] = 99
            with pytest.raises(TypeError):
                vector[i - self.component_count] = 99

    def test_component_attributes(self) -> None:
        vector = self.cls(*range(self.component_count))
        for attributes in (
            self.POSITION_ATTRIBUTES,
            self.COLOR_ATTRIBUTES,
            self.UV_ATTRIBUTES,
            self.TEXTURE_ATTRIBUTES
        ):
            for i, attr_name in enumerate(attributes):
                if i < self.component_count:
                    result = getattr(vector, attr_name)
                    assert result == self.type(i)
                    assert isinstance(result, self.type)
                    with pytest.raises(AttributeError):
                        setattr(vector, attr_name, i)
                else:
                    with pytest.raises(AttributeError):
                        getattr(vector, attr_name)

    def test_swizzle(self) -> None:
        vector = self.cls(*range(self.component_count))
        good = [
            *self.POSITION_ATTRIBUTES[:self.component_count],
            *self.COLOR_ATTRIBUTES[:self.component_count],
            *self.UV_ATTRIBUTES[:self.component_count],
            *self.TEXTURE_ATTRIBUTES[:self.component_count],
        ]
        bad = [
            *self.POSITION_ATTRIBUTES[self.component_count:],
            *self.COLOR_ATTRIBUTES[self.component_count:],
            *self.UV_ATTRIBUTES[self.component_count:],
            *self.TEXTURE_ATTRIBUTES[self.component_count:],
        ]

        for i in range(2, 6):
            for attrs in itertools.combinations_with_replacement(good, i):
                swizzle = ''.join(attrs)
                result = getattr(vector, swizzle)
                assert isinstance(result, tuple)
                assert all(isinstance(c, self.type) for c in result)
                assert result == tuple(getattr(vector, attr) for attr in attrs)

        for i in range(2, 6):
            for attrs in itertools.combinations_with_replacement(bad, i):
                swizzle = ''.join(attrs)
                with pytest.raises(AttributeError):
                    getattr(vector, swizzle)

        with pytest.raises(AttributeError):
            vector.not_a_swizzle

    def test_hash(self) -> None:
        for i in range(0 if self.unsigned else -100, 100):
            assert hash(self.cls(i)) == hash(self.cls(i))

        if not self.unsigned:
            assert hash(self.cls(0)) != hash(self.cls(-1))
        assert hash(self.cls(0)) != hash(self.cls(1))
        if self.type != bool and not self.unsigned:
            assert hash(self.cls(1)) != hash(self.cls(-1))
        assert hash(self.cls(0)) != hash(
            self.cls(*range(self.component_count))
        )

    def test_repr(self) -> None:
        vector = self.cls(*range(self.component_count))
        assert repr(vector) == (
            f'{vector.__class__.__name__}(' +
            ', '.join(repr(vector[i]) for i in range(self.component_count)) +
            f')'
        )

    def test_iterate(self) -> None:
        vector = self.cls(*range(self.component_count))
        for i, c in enumerate(vector):
            assert c == self.type(i)
            assert isinstance(c, self.type)

    def test_weakref(self) -> None:
        vector = self.cls()
        weak_vector = ref(vector)

    def test_equal(self) -> None:
        for i in range(0 if self.unsigned else -100, 100):
            assert self.cls(i) == self.cls(i)
        assert not (self.cls(0) == self.cls(1))
        if self.type != bool and not self.unsigned:
            assert not (self.cls(-1) == self.cls(1))

        assert not (self.cls() == 1)
        assert not (self.cls() == object())

    def test_not_equal(self) -> None:
        for i in range(0 if self.unsigned else -100, 100):
            assert not (self.cls(i) != self.cls(i))
        assert self.cls(0) != self.cls(1)
        if self.type != bool and not self.unsigned:
            assert self.cls(-1) != self.cls(1)

        assert self.cls() != 1
        assert self.cls() != object()

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

    def test_add(self) -> None:
        if not self.unsigned:
            assert self.cls(-1) + self.cls(-1) == self.cls(-2)
            assert self.cls(-1) + -1 == self.cls(-2)
            assert -1 + self.cls(-1) == self.cls(-2)
            assert self.cls(1) + self.cls(-1) == self.cls(
                self.type(1) + self.type(-1)
            )
            assert self.cls(1) + -1 == self.cls(self.type(1) + self.type(-1))
            assert -1 + self.cls(1) == self.cls(self.type(-1) + self.type(1))
            self.cls(self.cls.get_limits()[1]) + self.cls(1)
        else:
            assert (
                self.cls(self.cls.get_limits()[1]) + self.cls(1) ==
                self.cls(self.cls.get_limits()[0])
            )
        assert self.cls(1) + self.cls(1) == self.cls(2)
        assert self.cls(1) + 1 == self.cls(2)
        assert 1 + self.cls(1) == self.cls(2)

        vector = self.cls(*range(self.component_count))
        assert vector + vector == self.cls(*(
            i + i for i in range(self.component_count)
        ))
        assert vector + 1 == self.cls(*(
            i + 1 for i in range(self.component_count)
        ))
        assert 1 + vector == self.cls(*(
            1 + i for i in range(self.component_count)
        ))

        i_vec = vector
        i_vec += vector
        assert i_vec is not vector
        assert vector == self.cls(*range(self.component_count))
        assert i_vec == self.cls(*(
            i + i for i in range(self.component_count)
        ))

        i_vec = vector
        i_vec += 1
        assert i_vec is not vector
        assert vector == self.cls(*range(self.component_count))
        assert i_vec == self.cls(*(
            i + 1 for i in range(self.component_count)
        ))

        if self.type == bool:
            assert (self.cls(1) + None) == self.cls(1)
            assert (self.cls(0) + '123') == self.cls(1)
            assert (self.cls(0) + object()) == self.cls(1)
            assert (None + self.cls(1)) == self.cls(1)
            assert ('123' + self.cls(0)) == self.cls(1)
            assert (object() + self.cls(0)) == self.cls(1)
        else:
            with pytest.raises(TypeError):
                vector + None
            with pytest.raises(TypeError):
                None + vector
            with pytest.raises(TypeError):
                vector + '123'
            with pytest.raises(TypeError):
                '123' + vector
            with pytest.raises(TypeError):
                vector + object()
            with pytest.raises(TypeError):
                object() + vector

    def test_subtract(self) -> None:
        if not self.unsigned:
            assert self.cls(-1) - self.cls(-1) == self.cls(0)
            assert self.cls(-1) - -1 == self.cls(0)
            assert -1 - self.cls(-1) == self.cls(0)
            assert self.cls(1) - self.cls(-1) == self.cls(
                self.type(1) - self.type(-1)
            )
            assert self.cls(1) - -1 == self.cls(self.type(1) - self.type(-1))
            assert -1 - self.cls(1) == self.cls(self.type(-1) - self.type(1))
            self.cls(self.cls.get_limits()[1]) - self.cls(1)
        else:
            assert (
                self.cls(0) - self.cls(1) ==
                self.cls(self.cls.get_limits()[1])
            )
        assert self.cls(1) - self.cls(1) == self.cls(0)
        assert self.cls(1) - 1 == self.cls(0)
        assert 1 - self.cls(1) == self.cls(0)

        vector = self.cls(*range(1, self.component_count + 1))
        assert vector - vector == self.cls(*(
            i - i for i in range(1, self.component_count + 1)
        ))
        assert vector - 1 == self.cls(*(
            self.type(i) - self.type(1)
            for i in range(1, self.component_count + 1)
        ))
        assert 5 - vector == self.cls(*(
            self.type(5) - self.type(i)
            for i in range(1, self.component_count + 1)
        ))

        i_vec = vector
        i_vec -= vector
        assert i_vec is not vector
        assert vector == self.cls(*range(1, self.component_count + 1))
        assert i_vec == self.cls(*(
            i - i for i in range(1, self.component_count + 1)
        ))

        i_vec = vector
        i_vec -= 1
        assert i_vec is not vector
        assert vector == self.cls(*range(1, self.component_count + 1))
        assert i_vec == self.cls(*(
            self.type(i) - self.type(1)
            for i in range(1, self.component_count + 1)
        ))

        if self.type == bool:
            assert (self.cls(1) - None) == self.cls(1)
            assert (self.cls(0) - '123') == self.cls(1)
            assert (self.cls(0) - object()) == self.cls(1)
            assert (None - self.cls(1)) == self.cls(1)
            assert ('123' - self.cls(0)) == self.cls(1)
            assert (object() - self.cls(0)) == self.cls(1)
        else:
            with pytest.raises(TypeError):
                vector - None
            with pytest.raises(TypeError):
                None - vector
            with pytest.raises(TypeError):
                vector - '123'
            with pytest.raises(TypeError):
                '123' - vector
            with pytest.raises(TypeError):
                vector - object()
            with pytest.raises(TypeError):
                object() - vector

    def test_multiply(self) -> None:
        if not self.unsigned:
            assert self.cls(-1) * self.cls(-2) == self.cls(2)
            assert self.cls(-1) * -2 == self.cls(2)
            assert -2 * self.cls(-1) == self.cls(2)
            assert self.cls(1) * self.cls(-2) == self.cls(-2)
            assert self.cls(1) * -2 == self.cls(-2)
            assert -2 * self.cls(1) == self.cls(-2)
        else:
            assert (
                self.cls(self.cls.get_limits()[1]) * self.cls(2) ==
                self.cls(self.cls.get_limits()[1] - 1)
            )
        assert self.cls(1) * self.cls(2) == self.cls(2)
        assert self.cls(1) * 2 == self.cls(2)
        assert 2 * self.cls(1) == self.cls(2)

        vector = self.cls(*range(self.component_count))
        assert vector * vector == self.cls(*(
            i * i for i in range(self.component_count)
        ))
        assert vector * 2 == self.cls(*(
            i * 2 for i in range(self.component_count)
        ))
        assert 2 * vector == self.cls(*(
            2 * i for i in range(self.component_count)
        ))

        i_vec = vector
        i_vec *= vector
        assert i_vec is not vector
        assert vector == self.cls(*range(self.component_count))
        assert i_vec == self.cls(*(
            i * i for i in range(self.component_count)
        ))

        i_vec = vector
        i_vec *= 2
        assert i_vec is not vector
        assert vector == self.cls(*range(self.component_count))
        assert i_vec == self.cls(*(
            i * 2 for i in range(self.component_count)
        ))

        if self.type == bool:
            assert (self.cls(1) * None) == self.cls(0)
            assert (None * self.cls(1)) == self.cls(0)
            assert (self.cls(0) * '123') == self.cls(0)
            assert ('123' * self.cls(0)) == self.cls(0)
            assert (self.cls(0) * object()) == self.cls(0)
            assert (object() * self.cls(0)) == self.cls(0)
            assert (self.cls(1) * '123') == self.cls(1)
            assert ('123' * self.cls(1)) == self.cls(1)
            assert (self.cls(1) * object()) == self.cls(1)
            assert (object() * self.cls(1)) == self.cls(1)
        else:
            with pytest.raises(TypeError):
                vector * None
            with pytest.raises(TypeError):
                None * vector
            with pytest.raises(TypeError):
                vector * '123'
            with pytest.raises(TypeError):
                '123' * vector
            with pytest.raises(TypeError):
                vector * object()
            with pytest.raises(TypeError):
                object() * vector

    def test_matrix_multiply(self) -> None:
        if self.type != float:
            with pytest.raises(TypeError):
                self.cls() @ self.cls()
            return

        assert self.cls(0) @ self.cls(0) == 0
        assert self.cls(1) @ self.cls(1) == sum(
            self.cls(1)[i] * self.cls(1)[i]
            for i in range(self.component_count)
        )
        assert self.cls(2) @ self.cls(2) == sum(
            self.cls(2)[i] * self.cls(2)[i]
            for i in range(self.component_count)
        )

        vector = self.cls(*range(self.component_count))

        i_vec = vector
        i_vec @= vector
        assert i_vec is not vector
        assert vector == self.cls(*range(self.component_count))
        assert i_vec == sum(
            vector[i] * vector[i]
            for i in range(self.component_count)
        )

        with pytest.raises(TypeError):
            vector @ None
        with pytest.raises(TypeError):
            vector @ '123'
        with pytest.raises(TypeError):
            vector @ object()
        with pytest.raises(TypeError):
            None @ vector
        with pytest.raises(TypeError):
            '123' @ vector
        with pytest.raises(TypeError):
            object() @ vector

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


class TestBVector2(
    VectorTest,
    cls=BVector2,
    component_count=2,
    type=bool,
    struct_format='?'
):
    pass


class TestDVector2(
    VectorTest,
    cls=DVector2,
    component_count=2,
    type=float,
    struct_format='d'
):
    pass


class TestFVector2(
    VectorTest,
    cls=FVector2,
    component_count=2,
    type=float,
    struct_format='f'
):
    pass


class TestI8Vector2(
    VectorTest,
    cls=I8Vector2,
    component_count=2,
    type=int,
    struct_byte_order='=',
    struct_format='b'
):
    pass


class TestU8Vector2(
    VectorTest,
    cls=U8Vector2,
    component_count=2,
    type=int,
    struct_byte_order='=',
    struct_format='B',
    unsigned=True
):
    pass


class TestI16Vector2(
    VectorTest,
    cls=I16Vector2,
    component_count=2,
    type=int,
    struct_byte_order='=',
    struct_format='h'
):
    pass


class TestU16Vector2(
    VectorTest,
    cls=U16Vector2,
    component_count=2,
    type=int,
    struct_byte_order='=',
    struct_format='H',
    unsigned=True
):
    pass


class TestI32Vector2(
    VectorTest,
    cls=I32Vector2,
    component_count=2,
    type=int,
    struct_byte_order='=',
    struct_format='i'
):
    pass


class TestU32Vector2(
    VectorTest,
    cls=U32Vector2,
    component_count=2,
    type=int,
    struct_byte_order='=',
    struct_format='I',
    unsigned=True
):
    pass


class TestIVector2(
    VectorTest,
    cls=IVector2,
    component_count=2,
    type=int,
    struct_format='i'
):
    pass


class TestUVector2(
    VectorTest,
    cls=UVector2,
    component_count=2,
    type=int,
    struct_format='I',
    unsigned=True
):
    pass


class TestI64Vector2(
    VectorTest,
    cls=I64Vector2,
    component_count=2,
    type=int,
    struct_byte_order='=',
    struct_format='q'
):
    pass


class TestU64Vector2(
    VectorTest,
    cls=U64Vector2,
    component_count=2,
    type=int,
    struct_byte_order='=',
    struct_format='Q',
    unsigned=True
):
    pass


class TestBVector3(
    VectorTest,
    cls=BVector3,
    component_count=3,
    type=bool,
    struct_format='?'
):
    pass


class TestDVector3(
    VectorTest,
    cls=DVector3,
    component_count=3,
    type=float,
    struct_format='d'
):
    pass


class TestFVector3(
    VectorTest,
    cls=FVector3,
    component_count=3,
    type=float,
    struct_format='f'
):
    pass


class TestI8Vector3(
    VectorTest,
    cls=I8Vector3,
    component_count=3,
    type=int,
    struct_byte_order='=',
    struct_format='b'
):
    pass


class TestU8Vector3(
    VectorTest,
    cls=U8Vector3,
    component_count=3,
    type=int,
    struct_byte_order='=',
    struct_format='B',
    unsigned=True
):
    pass


class TestI16Vector3(
    VectorTest,
    cls=I16Vector3,
    component_count=3,
    type=int,
    struct_byte_order='=',
    struct_format='h'
):
    pass


class TestU16Vector3(
    VectorTest,
    cls=U16Vector3,
    component_count=3,
    type=int,
    struct_byte_order='=',
    struct_format='H',
    unsigned=True
):
    pass


class TestI32Vector3(
    VectorTest,
    cls=I32Vector3,
    component_count=3,
    type=int,
    struct_byte_order='=',
    struct_format='i'
):
    pass


class TestU32Vector3(
    VectorTest,
    cls=U32Vector3,
    component_count=3,
    type=int,
    struct_byte_order='=',
    struct_format='I',
    unsigned=True
):
    pass


class TestIVector3(
    VectorTest,
    cls=IVector3,
    component_count=3,
    type=int,
    struct_format='i'
):
    pass


class TestUVector3(
    VectorTest,
    cls=UVector3,
    component_count=3,
    type=int,
    struct_format='I',
    unsigned=True
):
    pass


class TestI64Vector3(
    VectorTest,
    cls=I64Vector3,
    component_count=3,
    type=int,
    struct_byte_order='=',
    struct_format='q'
):
    pass


class TestU64Vector3(
    VectorTest,
    cls=U64Vector3,
    component_count=3,
    type=int,
    struct_byte_order='=',
    struct_format='Q',
    unsigned=True
):
    pass


class TestBVector4(
    VectorTest,
    cls=BVector4,
    component_count=4,
    type=bool,
    struct_format='?'
):
    pass


class TestDVector4(
    VectorTest,
    cls=DVector4,
    component_count=4,
    type=float,
    struct_format='d'
):
    pass


class TestFVector4(
    VectorTest,
    cls=FVector4,
    component_count=4,
    type=float,
    struct_format='f'
):
    pass


class TestI8Vector4(
    VectorTest,
    cls=I8Vector4,
    component_count=4,
    type=int,
    struct_byte_order='=',
    struct_format='b'
):
    pass


class TestU8Vector4(
    VectorTest,
    cls=U8Vector4,
    component_count=4,
    type=int,
    struct_byte_order='=',
    struct_format='B',
    unsigned=True
):
    pass


class TestI16Vector4(
    VectorTest,
    cls=I16Vector4,
    component_count=4,
    type=int,
    struct_byte_order='=',
    struct_format='h'
):
    pass


class TestU16Vector4(
    VectorTest,
    cls=U16Vector4,
    component_count=4,
    type=int,
    struct_byte_order='=',
    struct_format='H',
    unsigned=True
):
    pass



class TestI32Vector4(
    VectorTest,
    cls=I32Vector4,
    component_count=4,
    type=int,
    struct_byte_order='=',
    struct_format='i'
):
    pass


class TestU32Vector4(
    VectorTest,
    cls=U32Vector4,
    component_count=4,
    type=int,
    struct_byte_order='=',
    struct_format='I',
    unsigned=True
):
    pass


class TestIVector4(
    VectorTest,
    cls=IVector4,
    component_count=4,
    type=int,
    struct_format='i'
):
    pass


class TestUVector4(
    VectorTest,
    cls=UVector4,
    component_count=4,
    type=int,
    struct_format='I',
    unsigned=True
):
    pass


class TestI64Vector4(
    VectorTest,
    cls=I64Vector4,
    component_count=4,
    type=int,
    struct_byte_order='=',
    struct_format='q'
):
    pass


class TestU64Vector4(
    VectorTest,
    cls=U64Vector4,
    component_count=4,
    type=int,
    struct_byte_order='=',
    struct_format='Q',
    unsigned=True
):
    pass
