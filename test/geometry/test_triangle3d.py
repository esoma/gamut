
# gamut
from gamut.geometry import Triangle3d
from gamut.math import DVector3, FVector3, Vector4
# python
from typing import Any
# pytest
import pytest


def test_hash() -> None:
    t = Triangle3d(DVector3(0), DVector3(1), DVector3(2))
    assert hash(t) == hash(Triangle3d(DVector3(0), DVector3(1), DVector3(2)))
    assert hash(t) == hash(Triangle3d(DVector3(1), DVector3(2), DVector3(0)))
    assert hash(t) != hash(Triangle3d(DVector3(1), DVector3(0), DVector3(2)))


@pytest.mark.parametrize("vtype", [FVector3, DVector3])
def test_repr(vtype: Any) -> None:
    line = Triangle3d(vtype(0, 1, 2), vtype(3, 4, 5), vtype(6, 7, 8))
    assert (
        repr(line) ==
        f'<gamut.geometry.Triangle3d '
        f'((0.0, 1.0, 2.0), (3.0, 4.0, 5.0), (6.0, 7.0, 8.0))>'
    )


@pytest.mark.parametrize("a", [None, 'x', object(), Vector4(1)])
def test_invalid_a(a: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Triangle3d(a, DVector3(0), DVector3(0))
    assert str(excinfo.value) == 'point 0 must be FVector3 or DVector3'


@pytest.mark.parametrize("a, b, c", [
    (DVector3(0), None, DVector3(0)),
    (DVector3(0), 'x', DVector3(0)),
    (DVector3(0), object(), DVector3(0)),
    (DVector3(0), Vector4(1), DVector3(0)),
    (FVector3(0), DVector3(0), FVector3(0)),
    (DVector3(0), FVector3(0), DVector3(0)),
])
def test_invalid_b(a: Any, b: Any, c: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Triangle3d(a, b, c)
    assert str(excinfo.value) == 'point 1 must be the same type as point 0'


@pytest.mark.parametrize("a, c, b", [
    (DVector3(0), None, DVector3(0)),
    (DVector3(0), 'x', DVector3(0)),
    (DVector3(0), object(), DVector3(0)),
    (DVector3(0), Vector4(1), DVector3(0)),
    (FVector3(0), DVector3(0), FVector3(0)),
    (DVector3(0), FVector3(0), DVector3(0)),
])
def test_invalid_c(a: Any, b: Any, c: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Triangle3d(a, b, c)
    assert str(excinfo.value) == 'point 2 must be the same type as point 0'


@pytest.mark.parametrize("vtype", [FVector3, DVector3])
def test_points(vtype: Any) -> None:
    for line in [
        Triangle3d(vtype(0, 1, 2), vtype(3, 4, 5), vtype(6, 7, 8)),
        Triangle3d(vtype(3, 4, 5), vtype(6, 7, 8), vtype(0, 1, 2)),
        Triangle3d(vtype(6, 7, 8), vtype(0, 1, 2), vtype(3, 4, 5)),
    ]:
        assert line.positions == (
            vtype(0, 1, 2),
            vtype(3, 4, 5),
            vtype(6, 7, 8)
        )
        assert line.center == sum((
            vtype(0, 1, 2),
            vtype(3, 4, 5),
            vtype(6, 7, 8)
        )) / 3

    for line in [
        Triangle3d(vtype(3, 4, 5), vtype(0, 1, 2), vtype(6, 7, 8)),
        Triangle3d(vtype(6, 7, 8), vtype(3, 4, 5), vtype(0, 1, 2)),
        Triangle3d(vtype(0, 1, 2), vtype(6, 7, 8), vtype(3, 4, 5)),
    ]:
        assert line.positions == (
            vtype(0, 1, 2),
            vtype(6, 7, 8),
            vtype(3, 4, 5),
        )
        assert line.center == sum((
            vtype(0, 1, 2),
            vtype(3, 4, 5),
            vtype(6, 7, 8)
        )) / 3


@pytest.mark.parametrize("vtype", [FVector3, DVector3])
def test_equal(vtype: Any) -> None:
    assert (
        Triangle3d(vtype(0), vtype(0), vtype(0)) ==
        Triangle3d(vtype(0), vtype(0), vtype(0))
    )
    assert (
        Triangle3d(vtype(0), vtype(0), vtype(0)) !=
        Triangle3d(vtype(0, 1, 0), vtype(0), vtype(0))
    )
    assert (
        Triangle3d(vtype(0), vtype(0), vtype(0)) !=
        Triangle3d(vtype(0), vtype(1, 0, 0), vtype(0))
    )
    assert (
        Triangle3d(vtype(0), vtype(0), vtype(0)) !=
        Triangle3d(vtype(0), vtype(0), vtype(1, 0, 0))
    )
    assert (
        Triangle3d(vtype(0), vtype(1), vtype(2)) ==
        Triangle3d(vtype(2), vtype(0), vtype(1))
    )
    assert (
        Triangle3d(vtype(2), vtype(0), vtype(1)) ==
        Triangle3d(vtype(1), vtype(2), vtype(0))
    )
    assert (
        Triangle3d(vtype(0), vtype(2), vtype(1)) !=
        Triangle3d(vtype(1), vtype(2), vtype(0))
    )
    assert Triangle3d(vtype(0), vtype(0), vtype(0)) != object()
