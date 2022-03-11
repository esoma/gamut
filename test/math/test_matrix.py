
# gamut
from gamut.math import (DMatrix2, DMatrix2x2, DMatrix2x3, DMatrix2x4, DMatrix3,
                        DMatrix3x2, DMatrix3x3, DMatrix3x4, DMatrix4,
                        DMatrix4x2, DMatrix4x3, DMatrix4x4, DVector2, DVector3,
                        DVector4, FMatrix2, FMatrix2x2, FMatrix2x3, FMatrix2x4,
                        FMatrix3, FMatrix3x2, FMatrix3x3, FMatrix3x4, FMatrix4,
                        FMatrix4x2, FMatrix4x3, FMatrix4x4, FVector2, FVector3,
                        FVector4, Matrix2, Matrix2x2, Matrix2x3, Matrix2x4,
                        Matrix3, Matrix3x2, Matrix3x3, Matrix3x4, Matrix4,
                        Matrix4x2, Matrix4x3, Matrix4x4)
# python
from math import inf, isnan
import struct
from weakref import ref
# pytest
import pytest


def test_alias():
    assert FMatrix2 is FMatrix2x2
    assert FMatrix3 is FMatrix3x3
    assert FMatrix4 is FMatrix4x4

    assert DMatrix2 is DMatrix2x2
    assert DMatrix3 is DMatrix3x3
    assert DMatrix4 is DMatrix4x4

    assert Matrix2 is DMatrix2x2
    assert Matrix3 is DMatrix3x3
    assert Matrix4 is DMatrix4x4

    assert Matrix2x2 is DMatrix2x2
    assert Matrix2x3 is DMatrix2x3
    assert Matrix2x4 is DMatrix2x4
    assert Matrix3x2 is DMatrix3x2
    assert Matrix3x3 is DMatrix3x3
    assert Matrix3x4 is DMatrix3x4
    assert Matrix4x2 is DMatrix4x2
    assert Matrix4x3 is DMatrix4x3
    assert Matrix4x4 is DMatrix4x4


class MatrixTest:

    def __init_subclass__(
        this_cls,
        *,
        cls,
        row_cls,
        column_cls,
        row_size,
        column_size,
        struct_format
    ):
        this_cls.cls = cls
        this_cls.row_cls = row_cls
        this_cls.column_cls = column_cls
        this_cls.row_size = row_size
        this_cls.column_size = column_size
        this_cls.component_count = row_size * column_size
        this_cls.type = float
        this_cls.struct_format = struct_format

    def test_empty_init(self) -> None:
        matrix = self.cls()
        for i in range(self.row_size):
            assert matrix[i] == self.column_cls()

    def test_init_keywords(self) -> None:
        with pytest.raises(TypeError):
            self.cls(x=0)

    def test_single_init(self) -> None:
        for arg in [-100, -1, 0, 1, 100]:
            matrix = self.cls(arg)
            for i in range(self.row_size):
                assert matrix[i] == self.column_cls(*(
                    arg if c == i else 0
                    for c in range(self.column_size)
                ))

        min, max = self.cls.get_limits()
        assert self.cls(min - 1) == self.cls(min)
        assert self.cls(max + 1) == self.cls(max)

    def test_column_init(self) -> None:
        matrix = self.cls(*(self.column_cls(i) for i in range(self.row_size)))
        for i in range(self.row_size):
            assert matrix[i] == self.column_cls(i)

        for e in range(self.row_size):
            with pytest.raises(TypeError):
                self.cls(*(
                    None if i == e else self.column_cls(i)
                    for i in range(self.row_size)
                ))

    def test_all_init(self) -> None:
        matrix = self.cls(*range(self.component_count))
        values = iter(range(self.component_count))
        for i in range(self.row_size):
            assert matrix[i] == self.column_cls(*(
                next(values) for _ in range(self.column_size)
            ))

    def test_invalid_arg_count(self) -> None:
        with pytest.raises(TypeError) as excinfo:
            self.cls(*range(self.component_count + 1))
        assert str(excinfo.value) == (
            f'invalid number of arguments supplied to '
            f'{ self.cls.__name__ }, expected 0, 1, { self.row_size} or '
            f'{ self.component_count } (got { self.component_count + 1 })'
        )

        for count in range(2, self.component_count):
            if count == self.row_size:
                continue
            with pytest.raises(TypeError) as excinfo:
                self.cls(*range(count))
            assert str(excinfo.value) == (
                f'invalid number of arguments supplied to '
                f'{ self.cls.__name__ }, expected 0, 1, { self.row_size} or '
                f'{ self.component_count } (got { count })'
            )

    def test_len(self) -> None:
        matrix = self.cls()
        assert len(matrix) == self.row_size

    def test_getitem(self) -> None:
        matrix = self.cls(*(self.column_cls(i) for i in range(self.row_size)))
        for i in range(self.row_size):
            assert isinstance(matrix[i], self.column_cls)
            assert matrix[i] == self.column_cls(i)
            assert isinstance(matrix[i - self.row_size], self.column_cls)
            assert matrix[i - self.row_size] == self.column_cls(i)

        with pytest.raises(IndexError) as excinfo:
            matrix[self.row_size]
        assert str(excinfo.value) == 'index out of range'

        with pytest.raises(IndexError) as excinfo:
            matrix[-(self.row_size + 1)]
        assert str(excinfo.value) == 'index out of range'

    def test_setitem(self) -> None:
        matrix = self.cls()
        for i in range(self.row_size):
            with pytest.raises(TypeError):
                matrix[i] = self.column_cls()
            with pytest.raises(TypeError):
                matrix[i - self.component_count] = self.column_cls()

    def test_hash(self) -> None:
        for i in range(-100, 100):
            assert hash(self.cls(i)) == hash(self.cls(i))

        assert hash(self.cls(0)) != hash(self.cls(-1))
        assert hash(self.cls(0)) != hash(self.cls(1))
        assert hash(self.cls(1)) != hash(self.cls(-1))
        assert hash(self.cls(0)) != hash(
            self.cls(*range(self.component_count))
        )

    def test_repr(self) -> None:
        matrix = self.cls(*range(self.component_count))
        assert repr(matrix) == (
            f'{matrix.__class__.__name__}(' +
            ', '.join(
                ('(' +
                ', '.join(str(i) for i in column) +
                ')')
                for column in matrix
            ) +
            f')'
        )

    def test_iterate(self) -> None:
        matrix = self.cls(*(self.column_cls(i) for i in range(self.row_size)))
        for i, c in enumerate(matrix):
            assert isinstance(matrix[i], self.column_cls)
            assert matrix[i] == self.column_cls(i)

    def test_weakref(self) -> None:
        matrix = self.cls()
        weak_matrix = ref(matrix)

    def test_equal(self) -> None:
        for i in range(-100, 100):
            assert self.cls(i) == self.cls(i)
        assert not (self.cls(0) == self.cls(1))
        assert not (self.cls(-1) == self.cls(1))

        assert not (self.cls() == 1)
        assert not (self.cls() == object())
        assert not (1 == self.cls())
        assert not (object() == self.cls())

    def test_not_equal(self) -> None:
        for i in range(-100, 100):
            assert not (self.cls(i) != self.cls(i))
        assert self.cls(0) != self.cls(1)
        assert self.cls(-1) != self.cls(1)

        assert self.cls() != 1
        assert self.cls() != object()
        assert 1 != self.cls()
        assert object() != self.cls()

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
        assert self.cls(0) + -1 == self.cls(*(
            -1 for _ in range(self.component_count)
        ))
        assert -1 + self.cls(*(
            -1 for _ in range(self.component_count)
        )) == self.cls(*(
            -2 for _ in range(self.component_count)
        ))
        assert self.cls(1) + self.cls(-1) == self.cls(0)
        self.cls(self.cls.get_limits()[1]) + self.cls(1)
        assert self.cls(1) + self.cls(1) == self.cls(2)
        assert self.cls(*(
            1 for _ in range(self.component_count)
        )) + 1 == self.cls(*(
            2 for _ in range(self.component_count)
        ))
        assert 1 + self.cls(*(
            1 for _ in range(self.component_count)
        )) == self.cls(*(
            2 for _ in range(self.component_count)
        ))

        matrix = self.cls(*range(self.component_count))
        assert matrix + matrix == self.cls(*(
            i + i for i in range(self.component_count)
        ))
        assert matrix + 1 == self.cls(*(
            i + 1 for i in range(self.component_count)
        ))
        assert 1 + matrix == self.cls(*(
            1 + i for i in range(self.component_count)
        ))

        i_mat = matrix
        i_mat += matrix
        assert i_mat is not matrix
        assert matrix == self.cls(*range(self.component_count))
        assert i_mat == self.cls(*(
            i + i for i in range(self.component_count)
        ))

        i_mat = matrix
        i_mat += 1
        assert i_mat is not matrix
        assert matrix == self.cls(*range(self.component_count))
        assert i_mat == self.cls(*(
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
                matrix + None
            with pytest.raises(TypeError):
                None + matrix
            with pytest.raises(TypeError):
                matrix + '123'
            with pytest.raises(TypeError):
                '123' + matrix
            with pytest.raises(TypeError):
                matrix + object()
            with pytest.raises(TypeError):
                object() + matrix

    def test_subtract(self) -> None:
        assert self.cls(-1) - self.cls(-1) == self.cls(0)
        assert self.cls(*(
            -1 for i in range(self.component_count)
        )) - -1 == self.cls(0)
        assert -1 - self.cls(*(
            -1 for i in range(self.component_count)
        )) == self.cls(0)
        assert self.cls(1) - self.cls(-1) == self.cls(
            self.type(1) - self.type(-1)
        )
        assert self.cls(*(
            1 for i in range(self.component_count)
        )) - -1 == self.cls(*(
            2 for i in range(self.component_count)
        ))
        assert -1 - self.cls(*(
            1 for i in range(self.component_count)
        )) == self.cls(*(
            -2 for i in range(self.component_count)
        ))
        self.cls(self.cls.get_limits()[1]) - self.cls(1)
        assert self.cls(1) - self.cls(1) == self.cls(0)
        assert self.cls(*(
            1 for i in range(self.component_count)
        )) - 1 == self.cls(0)
        assert 1 - self.cls(*(
            1 for i in range(self.component_count)
        )) == self.cls(0)

        matrix = self.cls(*range(1, self.component_count + 1))
        assert matrix - matrix == self.cls(*(
            i - i for i in range(1, self.component_count + 1)
        ))
        assert matrix - 1 == self.cls(*(
            self.type(i) - self.type(1)
            for i in range(1, self.component_count + 1)
        ))
        assert 5 - matrix == self.cls(*(
            self.type(5) - self.type(i)
            for i in range(1, self.component_count + 1)
        ))

        i_mat = matrix
        i_mat -= matrix
        assert i_mat is not matrix
        assert matrix == self.cls(*range(1, self.component_count + 1))
        assert i_mat == self.cls(*(
            i - i for i in range(1, self.component_count + 1)
        ))

        i_mat = matrix
        i_mat -= 1
        assert i_mat is not matrix
        assert matrix == self.cls(*range(1, self.component_count + 1))
        assert i_mat == self.cls(*(
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
                matrix - None
            with pytest.raises(TypeError):
                None - matrix
            with pytest.raises(TypeError):
                matrix - '123'
            with pytest.raises(TypeError):
                '123' - matrix
            with pytest.raises(TypeError):
                matrix - object()
            with pytest.raises(TypeError):
                object() - matrix

    def test_multiply(self) -> None:
        assert self.cls(1) * 0 == self.cls(0)
        assert 0 * self.cls(1) == self.cls(0)
        assert self.cls(*range(self.component_count)) * 2 == self.cls(*(
            i * 2 for i in range(self.component_count)
        ))
        assert 2 * self.cls(*range(self.component_count)) == self.cls(*(
            2 * i for i in range(self.component_count)
        ))
        assert -2 * self.cls(*range(self.component_count)) == self.cls(*(
            -2 * i for i in range(self.component_count)
        ))

        matrix = self.cls()

        with pytest.raises(TypeError):
            matrix * matrix
        with pytest.raises(TypeError):
            matrix * self.column_cls()
        with pytest.raises(TypeError):
            self.column_cls() * matrix
        with pytest.raises(TypeError):
            matrix * None
        with pytest.raises(TypeError):
            None * matrix
        with pytest.raises(TypeError):
            matrix * '123'
        with pytest.raises(TypeError):
            '123' * matrix
        with pytest.raises(TypeError):
            matrix * object()
        with pytest.raises(TypeError):
            object() * matrix

    def test_matrix_multiply(self) -> None:
        for c in range(2, 5):
            other_name = (
                f'{self.cls.__name__[0]}Matrix{c}x{ self.row_size }'
            )
            other_cls = globals()[other_name]
            result_name = (
                f'{self.cls.__name__[0]}Matrix{c}x{ self.column_size }'
            )
            result_cls = globals()[result_name]
            assert isinstance(self.cls() @ other_cls(), result_cls)

            mat_a = self.cls(*range(self.component_count))
            mat_b = other_cls(*range(c * self.row_size))
            result = mat_a @ mat_b
            assert isinstance(result, result_cls)
            assert result == result_cls(*(
                sum(
                    mat_a[ri][ci] * mat_b[ri2][ri]
                    for ri in range(self.row_size)
                )
                for ri2 in range(c)
                for ci in range(self.column_size)
            ))

            i_mat = mat_a
            i_mat @= mat_b
            assert i_mat is not mat_a
            assert isinstance(i_mat, result_cls)
            assert i_mat == result_cls(*(
                sum(
                    mat_a[ri][ci] * mat_b[ri2][ri]
                    for ri in range(self.row_size)
                )
                for ri2 in range(c)
                for ci in range(self.column_size)
            ))

        assert isinstance(self.cls() @ self.row_cls(), self.column_cls)
        assert isinstance(self.column_cls() @ self.cls(), self.row_cls)

        mat = self.cls(*range(self.component_count))
        vec = self.row_cls(*range(self.row_size))
        assert mat @ vec == self.column_cls(*(
            sum(c * mat[i][r] for i, c in enumerate(vec))
            for r in range(self.column_size)
        ))
        vec = self.column_cls(*range(self.column_size))
        assert vec @ mat == self.row_cls(*(
            sum(c * mat[r][i] for i, c in enumerate(vec))
            for r in range(self.row_size)
        ))

        matrix = self.cls()
        with pytest.raises(TypeError):
            matrix @ 1
        with pytest.raises(TypeError):
            matrix @ None
        with pytest.raises(TypeError):
            matrix @ '123'
        with pytest.raises(TypeError):
            matrix @ object()
        with pytest.raises(TypeError):
            1 @ matrix
        with pytest.raises(TypeError):
            None @ matrix
        with pytest.raises(TypeError):
            '123' @ matrix
        with pytest.raises(TypeError):
            object() @ matrix

    def test_division(self) -> None:
        assert isinstance(self.cls() / 0, self.cls)
        assert all(
            all(isnan(c) for c in v) for v in
            (self.cls() / 0)
        )
        assert all(
            all(isnan(c) for c in v) for v in
            (0 / self.cls())
        )
        assert self.cls(*(1 for _ in range(self.component_count))) / 0 == (
            self.cls(*(inf for _ in range(self.component_count)))
        )
        assert 1 / self.cls(*(0 for _ in range(self.component_count))) == (
            self.cls(*(inf for _ in range(self.component_count)))
        )
        assert self.cls(*(i for i in range(self.component_count))) / 2 == (
            self.cls(*(i / 2 for i in range(self.component_count)))
        )
        assert 2 / self.cls(
            *(i for i in range(1, self.component_count + 1))
        ) == (
            self.cls(*(2 / i for i in range(1, self.component_count + 1)))
        )

        if self.row_size == self.column_size:
            assert isinstance(self.cls() / self.row_cls(), self.row_cls)
            assert isinstance(self.row_cls() / self.cls(), self.row_cls)
            assert isinstance(self.cls() / self.cls(), self.cls)
            assert all(isnan(c) for c in (self.cls() / self.row_cls(1)))
            assert all(isnan(c) for c in (self.row_cls() / self.cls(
                *(1 for _ in range(self.component_count))
            )))
            assert all(isnan(c) for c in (self.cls(
                *(1 for _ in range(self.component_count))
            )) / self.row_cls(0))
            assert all(isnan(c) for c in (self.row_cls(1) / self.cls(
                *(0 for _ in range(self.component_count))
            )))

            vec = self.row_cls(*range(self.row_size))
            mat = self.cls(1)
            assert mat / vec == mat.inverse() @ vec
            assert vec / mat == vec @ mat.inverse()

            assert mat / mat == mat.inverse() @ mat

        matrix = self.cls()
        with pytest.raises(TypeError):
            matrix / None
        with pytest.raises(TypeError):
            matrix / '123'
        with pytest.raises(TypeError):
            matrix / object()
        with pytest.raises(TypeError):
            None / matrix
        with pytest.raises(TypeError):
            '123' / matrix
        with pytest.raises(TypeError):
            object() / matrix

    def test_negative(self) -> None:
        assert -self.cls(0) == self.cls(-0)
        assert -self.cls(1) == self.cls(-1)
        assert -self.cls(-1) == self.cls(1)

        matrix = self.cls(*range(self.component_count))
        assert -matrix == self.cls(*(
            -i for i in range(self.component_count)
        ))


    def test_buffer(self) -> None:
        assert bytes(self.cls(*range(self.component_count))) == struct.pack(
            self.struct_format * self.component_count,
            *range(self.component_count)
        )
        memory_view = memoryview(self.cls(0))
        assert memory_view.readonly
        assert memory_view.format == self.struct_format
        assert memory_view.itemsize == struct.calcsize(self.struct_format)
        assert memory_view.ndim == 2
        assert memory_view.shape == (self.row_size, self.column_size)
        assert memory_view.strides == (
            struct.calcsize(self.struct_format) * self.column_size,
            struct.calcsize(self.struct_format),
        )
        assert memory_view.suboffsets == tuple()

    def test_inverse(self) -> None:
        if self.row_size != self.column_size:
            with pytest.raises(AttributeError):
                self.cls().inverse()
            return
        assert all(
            isnan(c)
            for v in self.cls().inverse()
            for c in v
        )

    def test_transpose(self) -> None:
        transpose_cls_name = (
            f'{self.cls.__name__[0]}Matrix'
            f'{ self.column_size }x{ self.row_size }'
        )
        transpose_cls = globals()[transpose_cls_name]

        mat = self.cls(*range(self.component_count))
        t_mat = transpose_cls(*(
            mat[c][r]
            for r in range(self.column_size)
            for c in range(self.row_size)
        ))
        assert isinstance(mat.transpose(), transpose_cls)
        assert mat.transpose() == t_mat


class TestFMatrix2x2(
    MatrixTest,
    cls=FMatrix2x2,
    row_cls=FVector2,
    column_cls=FVector2,
    row_size=2,
    column_size=2,
    struct_format='f',
):
    pass


class TestFMatrix2x3(
    MatrixTest,
    cls=FMatrix2x3,
    row_cls=FVector2,
    column_cls=FVector3,
    row_size=2,
    column_size=3,
    struct_format='f',
):
    pass


class TestFMatrix2x4(
    MatrixTest,
    cls=FMatrix2x4,
    row_cls=FVector2,
    column_cls=FVector4,
    row_size=2,
    column_size=4,
    struct_format='f',
):
    pass


class TestFMatrix3x2(
    MatrixTest,
    cls=FMatrix3x2,
    row_cls=FVector3,
    column_cls=FVector2,
    row_size=3,
    column_size=2,
    struct_format='f',
):
    pass


class TestFMatrix3x3(
    MatrixTest,
    cls=FMatrix3x3,
    row_cls=FVector3,
    column_cls=FVector3,
    row_size=3,
    column_size=3,
    struct_format='f',
):
    pass


class TestFMatrix3x4(
    MatrixTest,
    cls=FMatrix3x4,
    row_cls=FVector3,
    column_cls=FVector4,
    row_size=3,
    column_size=4,
    struct_format='f',
):
    pass


class TestFMatrix4x2(
    MatrixTest,
    cls=FMatrix4x2,
    row_cls=FVector4,
    column_cls=FVector2,
    row_size=4,
    column_size=2,
    struct_format='f',
):
    pass


class TestFMatrix4x3(
    MatrixTest,
    cls=FMatrix4x3,
    row_cls=FVector4,
    column_cls=FVector3,
    row_size=4,
    column_size=3,
    struct_format='f',
):
    pass


class TestFMatrix4x4(
    MatrixTest,
    cls=FMatrix4x4,
    row_cls=FVector4,
    column_cls=FVector4,
    row_size=4,
    column_size=4,
    struct_format='f',
):
    pass

class TestDMatrix2x2(
    MatrixTest,
    cls=DMatrix2x2,
    row_cls=DVector2,
    column_cls=DVector2,
    row_size=2,
    column_size=2,
    struct_format='d',
):
    pass


class TestDMatrix2x3(
    MatrixTest,
    cls=DMatrix2x3,
    row_cls=DVector2,
    column_cls=DVector3,
    row_size=2,
    column_size=3,
    struct_format='d',
):
    pass


class TestDMatrix2x4(
    MatrixTest,
    cls=DMatrix2x4,
    row_cls=DVector2,
    column_cls=DVector4,
    row_size=2,
    column_size=4,
    struct_format='d',
):
    pass


class TestDMatrix3x2(
    MatrixTest,
    cls=DMatrix3x2,
    row_cls=DVector3,
    column_cls=DVector2,
    row_size=3,
    column_size=2,
    struct_format='d',
):
    pass


class TestDMatrix3x3(
    MatrixTest,
    cls=DMatrix3x3,
    row_cls=DVector3,
    column_cls=DVector3,
    row_size=3,
    column_size=3,
    struct_format='d',
):
    pass


class TestDMatrix3x4(
    MatrixTest,
    cls=DMatrix3x4,
    row_cls=DVector3,
    column_cls=DVector4,
    row_size=3,
    column_size=4,
    struct_format='d',
):
    pass


class TestDMatrix4x2(
    MatrixTest,
    cls=DMatrix4x2,
    row_cls=DVector4,
    column_cls=DVector2,
    row_size=4,
    column_size=2,
    struct_format='d',
):
    pass


class TestDMatrix4x3(
    MatrixTest,
    cls=DMatrix4x3,
    row_cls=DVector4,
    column_cls=DVector3,
    row_size=4,
    column_size=3,
    struct_format='d',
):
    pass


class TestDMatrix4x4(
    MatrixTest,
    cls=DMatrix4x4,
    row_cls=DVector4,
    column_cls=DVector4,
    row_size=4,
    column_size=4,
    struct_format='d',
):
    pass