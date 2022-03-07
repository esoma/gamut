
# gamut
from gamut.math import (DVector2, DVector3, DVector4, FVector2, FVector3,
                        FVector4)
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
        struct_format
    ):
        this_cls.cls = cls
        this_cls.component_count = component_count
        this_cls.type = type
        this_cls.struct_format = struct_format

    def test_empty_init(self) -> None:
        vector = self.cls()
        for i in range(self.component_count):
            assert vector[i] == 0

    @pytest.mark.parametrize("arg", [-100, -1, 0, 1, 100])
    def test_single_init(self, arg: int) -> None:
        vector = self.cls(arg)
        for i in range(self.component_count):
            assert vector[i] == arg

    def test_all_init(self) -> None:
        vector = self.cls(*range(self.component_count))
        for i in range(self.component_count):
            assert vector[i] == i

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
            assert vector[i] == i
            assert vector[i - self.component_count] == i

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
                    assert result == i
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
        for i in range(-100, 100):
            assert hash(self.cls(i)) == hash(self.cls(i))
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
            assert c == i

    def test_weakref(self) -> None:
        vector = self.cls()
        weak_vector = ref(vector)

    def test_equal(self) -> None:
        for i in range(-100, 100):
            assert self.cls(i) == self.cls(i)
        assert not (self.cls(0) == self.cls(1))
        assert not (self.cls(-1) == self.cls(1))

        assert not (self.cls() == 1)
        assert not (self.cls() == object())

    def test_not_equal(self) -> None:
        for i in range(-100, 100):
            assert not (self.cls(i) != self.cls(i))
        assert self.cls(0) != self.cls(1)
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
        assert self.cls(-1) + self.cls(-1) == self.cls(-2)
        assert self.cls(-1) + -1 == self.cls(-2)
        assert self.cls(1) + self.cls(-1) == self.cls(0)
        assert self.cls(1) + -1 == self.cls(0)
        assert self.cls(1) + self.cls(1) == self.cls(2)
        assert self.cls(1) + 1 == self.cls(2)

        vector = self.cls(*range(self.component_count))
        assert vector + vector == self.cls(*(
            i + i for i in range(self.component_count)
        ))
        assert vector + 1 == self.cls(*(
            i + 1 for i in range(self.component_count)
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

        with pytest.raises(TypeError):
            vector + None
        with pytest.raises(TypeError):
            vector + '123'
        with pytest.raises(TypeError):
            vector + object()

    def test_subtract(self) -> None:
        assert self.cls(-1) - self.cls(-1) == self.cls(0)
        assert self.cls(-1) - -1 == self.cls(0)
        assert self.cls(1) - self.cls(-1) == self.cls(2)
        assert self.cls(1) - -1 == self.cls(2)
        assert self.cls(1) - self.cls(1) == self.cls(0)
        assert self.cls(1) - 1 == self.cls(0)

        vector = self.cls(*range(self.component_count))
        assert vector - vector == self.cls(*(
            i - i for i in range(self.component_count)
        ))
        assert vector - 1 == self.cls(*(
            i - 1 for i in range(self.component_count)
        ))

        i_vec = vector
        i_vec -= vector
        assert i_vec is not vector
        assert vector == self.cls(*range(self.component_count))
        assert i_vec == self.cls(*(
            i - i for i in range(self.component_count)
        ))

        i_vec = vector
        i_vec -= 1
        assert i_vec is not vector
        assert vector == self.cls(*range(self.component_count))
        assert i_vec == self.cls(*(
            i - 1 for i in range(self.component_count)
        ))

        with pytest.raises(TypeError):
            vector - None
        with pytest.raises(TypeError):
            vector - '123'
        with pytest.raises(TypeError):
            vector - object()

    def test_multiply(self) -> None:
        assert self.cls(-1) * self.cls(-2) == self.cls(2)
        assert self.cls(-1) * -2 == self.cls(2)
        assert self.cls(1) * self.cls(-2) == self.cls(-2)
        assert self.cls(1) * -2 == self.cls(-2)
        assert self.cls(1) * self.cls(2) == self.cls(2)
        assert self.cls(1) * 2 == self.cls(2)

        vector = self.cls(*range(self.component_count))
        assert vector * vector == self.cls(*(
            i * i for i in range(self.component_count)
        ))
        assert vector * 2 == self.cls(*(
            i * 2 for i in range(self.component_count)
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

        with pytest.raises(TypeError):
            vector * None
        with pytest.raises(TypeError):
            vector * '123'
        with pytest.raises(TypeError):
            vector * object()

    def test_matrix_multiply(self) -> None:
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

    def test_divide(self) -> None:
        assert self.cls(-1) / self.cls(-2) == self.cls(.5)
        assert self.cls(-1) / -2 == self.cls(.5)
        assert self.cls(1) / self.cls(-2) == self.cls(-.5)
        assert self.cls(1) / -2 == self.cls(-.5)
        assert self.cls(1) / self.cls(2) == self.cls(.5)
        assert self.cls(1) / 2 == self.cls(.5)

        assert self.cls(1) / 0 == self.cls(inf)
        assert self.cls(1) / self.cls(0) == self.cls(inf)

        vector = self.cls(*range(1, self.component_count + 1))
        assert vector / vector == self.cls(*(
            i / i for i in range(1, self.component_count + 1)
        ))
        assert vector / 2 == self.cls(*(
            i / 2 for i in range(1, self.component_count + 1)
        ))

        i_vec = vector
        i_vec /= vector
        assert i_vec is not vector
        assert vector == self.cls(*range(1, self.component_count + 1))
        assert i_vec == self.cls(*(
            i / i for i in range(1, self.component_count + 1)
        ))

        i_vec = vector
        i_vec /= 2
        assert i_vec is not vector
        assert vector == self.cls(*range(1, self.component_count + 1))
        assert i_vec == self.cls(*(
            i / 2 for i in range(1, self.component_count + 1)
        ))

        with pytest.raises(TypeError):
            vector / None
        with pytest.raises(TypeError):
            vector / '123'
        with pytest.raises(TypeError):
            vector / object()


    def test_modulus(self) -> None:
        assert self.cls(-3) % self.cls(-2) == self.cls(-1)
        assert self.cls(-3) % -2 == self.cls(-1)
        assert self.cls(3) % self.cls(-2) == self.cls(-1)
        assert self.cls(3) % -2 == self.cls(-1)
        assert self.cls(3) % self.cls(2) == self.cls(1)
        assert self.cls(3) % 2 == self.cls(1)

        assert all(isnan(c) for c in self.cls(1) % 0)
        assert all(isnan(c) for c in self.cls(1) % self.cls(0))

        vector = self.cls(*range(1, self.component_count + 1))
        assert vector % vector == self.cls(*(
            i % i for i in range(1, self.component_count + 1)
        ))
        assert vector % 2 == self.cls(*(
            i % 2 for i in range(1, self.component_count + 1)
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
            vector % '123'
        with pytest.raises(TypeError):
            vector % object()


    def test_power(self) -> None:
        assert self.cls(-3) ** self.cls(-2) == self.cls(3 ** -2)
        assert self.cls(-3) ** -2 == self.cls(3 ** -2)
        assert self.cls(3) ** self.cls(-2) == self.cls(3 ** -2)
        assert self.cls(3) ** -2 == self.cls(3 ** -2)
        assert self.cls(3) ** self.cls(2) == self.cls(9)
        assert self.cls(3) ** 2 == self.cls(9)

        assert self.cls(5) ** 0 == self.cls(1)
        assert self.cls(5) ** self.cls(0) == self.cls(1)

        vector = self.cls(*range(1, self.component_count + 1))
        assert vector ** vector == self.cls(*(
            i ** i for i in range(1, self.component_count + 1)
        ))
        assert vector ** 2 == self.cls(*(
            i ** 2 for i in range(1, self.component_count + 1)
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

    def test_negative(self) -> None:
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
        assert abs(self.cls(-1)) == self.cls(1)

        vector = self.cls(*range(self.component_count))
        assert abs(vector) == self.cls(*(range(self.component_count)))
        assert abs(-vector) == self.cls(*(range(self.component_count)))

    def test_bool(self) -> None:
        assert self.cls(1)
        assert self.cls(-1)
        assert not self.cls(0)

        for i in range(self.component_count):
            components = [1] * self.component_count
            components[i] = 0
            assert not self.cls(*components)

    def test_buffer(self) -> None:
        assert bytes(self.cls(*range(self.component_count))) == struct.pack(
            self.struct_format * self.component_count,
            *range(self.component_count)
        )
        memory_view = memoryview(self.cls(0))
        assert memory_view.readonly
        assert memory_view.format == self.struct_format
        assert memory_view.itemsize == struct.calcsize(self.struct_format)
        assert memory_view.ndim == 1
        assert memory_view.shape == (self.component_count,)
        assert memory_view.strides == (struct.calcsize(self.struct_format),)
        assert memory_view.suboffsets == tuple()
        assert memory_view.c_contiguous
        assert memory_view.f_contiguous
        assert memory_view.contiguous

    def test_cross(self) -> None:
        if self.component_count != 3:
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

    def test_normalize(self) -> None:
        assert all(isnan(c) for c in self.cls(0).normalize())

        vector = self.cls(1)
        assert vector.normalize() == vector / vector.magnitude
        vector = self.cls(-1)
        assert vector.normalize() == vector / vector.magnitude

        vector = self.cls(*range(self.component_count))
        assert vector.normalize() == vector / vector.magnitude


    def test_distance(self) -> None:
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
