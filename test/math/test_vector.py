
# gamut
from gamut.math import DVector3
# pytest
import pytest


class VectorTest:

    def __init_subclass__(this_cls, *, cls, component_count, type):
        this_cls.cls = cls
        this_cls.component_count = component_count
        this_cls.type = type

    def test_empty_init(self) -> None:
        vector = self.cls()
        for i in range(self.component_count):
            assert vector[i] == 0

    @pytest.mark.parametrize("arg", [-1, 0, 1])
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


class TestDVector3(VectorTest, cls=DVector3, component_count=3, type=float):
    pass
