
# gamut
from gamut.geometry import Mesh3d
from gamut.math import (DMatrix4, DVector3, DVector3Array, FMatrix4, FVector3,
                        FVector3Array, U8Vector3, U8Vector3Array, U16Vector3,
                        U16Vector3Array, U32Vector3, U32Vector3Array, UVector3,
                        UVector3Array, Vector2, Vector4)
# python
from math import radians
from typing import Any
# pytest
import pytest


def test_hash() -> None:
    positions = DVector3Array(DVector3(1, 2, 3))
    triangle_indexes = UVector3Array(UVector3(0))
    m1 = Mesh3d(positions, triangle_indexes)
    m2 = Mesh3d(positions, triangle_indexes)
    assert hash(m1) != hash(m2)


def test_repr() -> None:
    m = Mesh3d(DVector3Array(DVector3(1, 2, 3)), UVector3Array(UVector3(0)))
    assert repr(m) == '<gamut.geometry.Mesh3d>'


def test_no_positions() -> None:
    with pytest.raises(ValueError) as excinfo:
        Mesh3d(DVector3Array(), UVector3Array(UVector3(0)))
    assert str(excinfo.value) == 'must have at least 1 vertex position'


def test_no_normals() -> None:
    with pytest.raises(ValueError) as excinfo:
        Mesh3d(
            DVector3Array(DVector3(0)),
            UVector3Array(UVector3(0)),
            normals=DVector3Array()
        )
    assert str(excinfo.value) == 'must have at least 1 vertex normal'


@pytest.mark.parametrize("positions", [
    [None],
    [1],
    ['123'],
    [Vector2(1)],
    [Vector4(1)],
])
def test_positions_invalid_type(positions: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Mesh3d(positions, [UVector3(0)])
    assert str(excinfo.value) == (
        'positions must be FVector3Array or DVector3Array'
    )


@pytest.mark.parametrize("normals", [
    [None],
    [1],
    ['123'],
    [Vector2(1)],
    [Vector4(1)],
])
def test_normals_invalid_type(normals: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Mesh3d(DVector3Array(DVector3(0)), [UVector3(0)], normals=normals)
    assert str(excinfo.value) == 'normals must be DVector3Array'


def test_normals_wrong_type():
    with pytest.raises(TypeError) as excinfo:
        DMatrix4(1) @ Mesh3d(
            FVector3Array(FVector3(0, 1, 2)),
            UVector3Array(UVector3(0)),
            normals=DVector3Array(DVector3(0, 1, 2)),
        )
    assert str(excinfo.value) == 'normals must be FVector3Array'

    with pytest.raises(TypeError) as excinfo:
        FMatrix4(1) @ Mesh3d(
            DVector3Array(DVector3(0, 1, 2)),
            UVector3Array(UVector3(0)),
            normals=FVector3Array(FVector3(0, 1, 2)),
        )
    assert str(excinfo.value) == 'normals must be DVector3Array'


def test_no_triangle_indices() -> None:
    with pytest.raises(ValueError) as excinfo:
        Mesh3d(DVector3Array(DVector3(0)), UVector3Array())
    assert str(excinfo.value) == 'must have at least 1 triangle'


@pytest.mark.parametrize("indices", [
    [None],
    [1],
    ['123'],
    [Vector2(1)],
    [Vector4(1)],
])
def test_triangle_indices_invalid_type(indices: Any) -> None:
    with pytest.raises(TypeError) as excinfo:
        Mesh3d(DVector3Array(DVector3(0)), indices)
    assert str(excinfo.value) == 'indices must be UVector3Array'


@pytest.mark.parametrize("positions, triangle_indices, normals", [
    (
        DVector3Array(DVector3(0)),
        UVector3Array(UVector3(1, 0, 0)),
        None
    ),
    (
        DVector3Array(DVector3(0)),
        UVector3Array(UVector3(1, 0, 0)),
        DVector3Array(DVector3(0)),
    ),
    (
        DVector3Array(DVector3(0), DVector3(0)),
        UVector3Array(UVector3(1, 0, 0)),
        DVector3Array(DVector3(0)),
    ),
    (
        DVector3Array(DVector3(0)),
        UVector3Array(UVector3(1, 0, 0)),
        DVector3Array(DVector3(0), DVector3(0)),
    ),
])
def test_triangle_indices_invalid_value(
    positions: Any,
    triangle_indices: Any,
    normals: Any
) -> None:
    with pytest.raises(ValueError) as excinfo:
        Mesh3d(positions, triangle_indices, normals=normals)
    assert (
        str(excinfo.value) ==
        'triangle indices must be between 0 and the number of vertices'
    )


@pytest.mark.parametrize("positions", [
    DVector3Array(DVector3(0, 1, 2), DVector3(3, 4, 5)),
    DVector3Array(DVector3(0), DVector3(1), DVector3(2)),
])
def test_positions(positions: Any) -> None:
    m = Mesh3d(positions, UVector3Array(UVector3(0)))
    assert m.positions == positions


@pytest.mark.parametrize("triangle_indices", [
    UVector3Array(UVector3(0)),
    UVector3Array(UVector3(0, 1, 2)),
    UVector3Array(UVector3(0, 1, 2), UVector3(1, 2, 3), UVector3(2, 3, 0)),
    U8Vector3Array(U8Vector3(0, 1, 2)),
    U16Vector3Array(U16Vector3(0, 1, 2)),
    U32Vector3Array(U32Vector3(0, 1, 2)),
])
def test_triangle_indices(triangle_indices: Any) -> None:
    m = Mesh3d(
        DVector3Array(DVector3(0), DVector3(1), DVector3(2), DVector3(3)),
        triangle_indices
    )
    assert m.triangle_indices == triangle_indices


@pytest.mark.parametrize("normals", [
    DVector3Array(DVector3(0, 1, 2), DVector3(3, 4, 5)),
    DVector3Array(DVector3(0), DVector3(1), DVector3(2)),
])
def test_normals(normals: Any) -> None:
    m = Mesh3d(
        DVector3Array(DVector3(0)),
        UVector3Array(UVector3(0)),
        normals=normals
    )
    assert m.normals == normals


@pytest.mark.parametrize("mesh", [
    Mesh3d(DVector3Array(DVector3(0, 1, 2)), UVector3Array(UVector3(0))),
    Mesh3d(
        DVector3Array(DVector3(0, 1, 2), DVector3(3, 4, 5)),
        UVector3Array(UVector3(0))
    ),
    Mesh3d(
        DVector3Array(DVector3(0, 1, 2), DVector3(3, 4, 5)),
        UVector3Array(UVector3(0)),
        normals=DVector3Array(DVector3(0, 1, 2), DVector3(3, 4, 5)),
    ),
])
@pytest.mark.parametrize("transform", [
    DMatrix4(1).translate(DVector3(1, 0, 0)),
    DMatrix4(1).translate(DVector3(0, 1, 0)),
    DMatrix4(1).translate(DVector3(0, 0, 1)),
    DMatrix4(1).rotate(radians(90), DVector3(1, 0, 0)),
    DMatrix4(1).rotate(radians(90), DVector3(0, 1, 0)),
    DMatrix4(1).rotate(radians(90), DVector3(0, 0, 1)),
    DMatrix4(1).scale(DVector3(2, 3, 4)),
])
def test_d_transform(mesh: Mesh3d, transform: DMatrix4) -> None:
    new_ch = transform @ mesh
    assert new_ch is not mesh
    assert new_ch.positions == DVector3Array(*(
        transform @ v for v in mesh.positions
    ))
    assert new_ch.triangle_indices == mesh.triangle_indices
    if mesh.normals is None:
        assert new_ch.normals is None
    else:
        normal_transform = transform.inverse().transpose().to_matrix3()
        assert new_ch.normals == DVector3Array(*(
            normal_transform @ v for v in mesh.normals
        ))


@pytest.mark.parametrize("mesh", [
    Mesh3d(FVector3Array(FVector3(0, 1, 2)), UVector3Array(UVector3(0))),
    Mesh3d(
        FVector3Array(FVector3(0, 1, 2), FVector3(3, 4, 5)),
        UVector3Array(UVector3(0))
    ),
    Mesh3d(
        FVector3Array(FVector3(0, 1, 2), FVector3(3, 4, 5)),
        UVector3Array(UVector3(0)),
        normals=FVector3Array(FVector3(0, 1, 2), FVector3(3, 4, 5)),
    ),
])
@pytest.mark.parametrize("transform", [
    FMatrix4(1).translate(FVector3(1, 0, 0)),
    FMatrix4(1).translate(FVector3(0, 1, 0)),
    FMatrix4(1).translate(FVector3(0, 0, 1)),
    FMatrix4(1).rotate(radians(90), FVector3(1, 0, 0)),
    FMatrix4(1).rotate(radians(90), FVector3(0, 1, 0)),
    FMatrix4(1).rotate(radians(90), FVector3(0, 0, 1)),
    FMatrix4(1).scale(FVector3(2, 3, 4)),
])
def test_f_transform(mesh: Mesh3d, transform: FMatrix4) -> None:
    new_ch = transform @ mesh
    assert new_ch is not mesh
    assert new_ch.positions == FVector3Array(*(
        transform @ v for v in mesh.positions
    ))
    assert new_ch.triangle_indices == mesh.triangle_indices
    if mesh.normals is None:
        assert new_ch.normals is None
    else:
        normal_transform = transform.inverse().transpose().to_matrix3()
        assert new_ch.normals == FVector3Array(*(
            normal_transform @ v for v in mesh.normals
        ))


@pytest.mark.parametrize("mesh", [
    Mesh3d(FVector3Array(FVector3(0, 1, 2)), UVector3Array(UVector3(0))),
    Mesh3d(DVector3Array(DVector3(0, 1, 2)), UVector3Array(UVector3(0))),
])
@pytest.mark.parametrize("transform", [None, 123, Vector4(1), Vector2(1)])
def test_transform_invalid(
    mesh: Mesh3d,
    transform: Any
) -> None:
    with pytest.raises(TypeError) as excinfo:
        transform @ mesh
    assert str(excinfo.value).startswith('unsupported operand type(s) for @:')


def test_transform_wrong_type():
    with pytest.raises(TypeError) as excinfo:
        DMatrix4(1) @ Mesh3d(
            FVector3Array(FVector3(0, 1, 2)),
            UVector3Array(UVector3(0))
        )
    assert str(excinfo.value).startswith('unsupported operand type(s) for @:')

    with pytest.raises(TypeError) as excinfo:
        FMatrix4(1) @ Mesh3d(
            DVector3Array(DVector3(0, 1, 2)),
            UVector3Array(UVector3(0))
        )
    assert str(excinfo.value).startswith('unsupported operand type(s) for @:')


def test_equal() -> None:
    assert Mesh3d(DVector3Array(DVector3(0)), UVector3Array(UVector3(0))) == (
        Mesh3d(DVector3Array(DVector3(0)), UVector3Array(UVector3(0)))
    )
    assert Mesh3d(
        DVector3Array(DVector3(0)),
        U8Vector3Array(U8Vector3(0))
    ) == Mesh3d(DVector3Array(DVector3(0)), U8Vector3Array(U8Vector3(0)))
    assert Mesh3d(FVector3Array(FVector3(0)), UVector3Array(UVector3(0))) == (
        Mesh3d(FVector3Array(FVector3(0)), UVector3Array(UVector3(0)))
    )
    assert Mesh3d(DVector3Array(DVector3(0)), UVector3Array(UVector3(0))) != (
        Mesh3d(FVector3Array(FVector3(0)), UVector3Array(UVector3(0)))
    )
    assert Mesh3d(DVector3Array(DVector3(0)), UVector3Array(UVector3(0))) != (
        Mesh3d(DVector3Array(DVector3(0)), U8Vector3Array(U8Vector3(0)))
    )
    assert Mesh3d(DVector3Array(DVector3(0)), UVector3Array(UVector3(0))) != (
        Mesh3d(
            DVector3Array(DVector3(0), DVector3(0)),
            UVector3Array(UVector3(0))
        )
    )
    assert Mesh3d(DVector3Array(DVector3(0)), UVector3Array(UVector3(0))) != (
        Mesh3d(
            DVector3Array(DVector3(0)),
            UVector3Array(UVector3(0), UVector3(0))
        )
    )
    assert Mesh3d(DVector3Array(DVector3(0)), UVector3Array(UVector3(0))) != (
        Mesh3d(DVector3Array(DVector3(1, 0, 0)), UVector3Array(UVector3(0)))
    )
    assert Mesh3d(DVector3Array(DVector3(0)), UVector3Array(UVector3(0))) != (
        Mesh3d(DVector3Array(DVector3(0, 1, 0)), UVector3Array(UVector3(0)))
    )
    assert Mesh3d(DVector3Array(DVector3(0)), UVector3Array(UVector3(0))) != (
        Mesh3d(DVector3Array(DVector3(0, 0, 1)), UVector3Array(UVector3(0)))
    )
    positions = DVector3Array(DVector3(0), DVector3(0))
    assert (
        Mesh3d(positions, UVector3Array(UVector3(0))) !=
        Mesh3d(positions, UVector3Array(UVector3(1, 0, 0)))
    )
    assert (
        Mesh3d(positions, UVector3Array(UVector3(0))) !=
        Mesh3d(positions, UVector3Array(UVector3(0, 1, 0)))
    )
    assert (
        Mesh3d(positions, UVector3Array(UVector3(0))) !=
        Mesh3d(positions, UVector3Array(UVector3(0, 0, 1)))
    )
    assert Mesh3d(DVector3Array(DVector3(0)), UVector3Array(UVector3(0))) != (
        object()
    )
    assert Mesh3d(
        DVector3Array(DVector3(0)),
        UVector3Array(UVector3(0)),
        normals=DVector3Array(DVector3(0))
    ) == Mesh3d(
        DVector3Array(DVector3(0)),
        UVector3Array(UVector3(0)),
        normals=DVector3Array(DVector3(0))
    )
    assert Mesh3d(
        DVector3Array(DVector3(0)),
        UVector3Array(UVector3(0)),
        normals=DVector3Array(DVector3(0))
    ) != Mesh3d(
        DVector3Array(DVector3(0)),
        UVector3Array(UVector3(0)),
        normals=DVector3Array(DVector3(1))
    )


@pytest.mark.parametrize("invalid_value", [None, object(), '1'])
@pytest.mark.parametrize("pos_array, pos_vector", [
    (FVector3Array, FVector3),
    (DVector3Array, DVector3),
])
def test_raycast_invalid_start_end(
    pos_array: Any,
    pos_vector: Any,
    invalid_value: Any
) -> None:
    mesh = Mesh3d(
        pos_array(
            pos_vector(-1, -1, 0),
            pos_vector(1, -1, 0),
            pos_vector(1, 1, 0),
            pos_vector(-1, 1, 0),
        ),
        UVector3Array(
            UVector3(0, 1, 3),
            UVector3(3, 1, 2),
        )
    )
    with pytest.raises(TypeError) as ex:
        mesh.raycast(invalid_value, pos_vector(0))
    assert str(ex.value) == f'start must be {pos_vector.__name__}'

    with pytest.raises(TypeError) as ex:
        mesh.raycast(pos_vector(0), invalid_value)
    assert str(ex.value) == f'end must be {pos_vector.__name__}'


@pytest.mark.parametrize("pos_array, pos_vector", [
    (FVector3Array, FVector3),
    (DVector3Array, DVector3),
])
@pytest.mark.parametrize("index_array, index_vector", [
    (UVector3Array, UVector3),
    (U8Vector3Array, U8Vector3),
    (U16Vector3Array, U16Vector3),
    (U32Vector3Array, U32Vector3),
])
def test_raycast_no_normals(
    pos_array: Any,
    pos_vector: Any,
    index_array: Any,
    index_vector: Any
) -> None:
    mesh = Mesh3d(
        pos_array(
            pos_vector(-1, -1, 0),
            pos_vector(1, -1, 0),
            pos_vector(1, 1, 0),
            pos_vector(-1, 1, 0),
        ),
        index_array(
            index_vector(0, 1, 3),
            index_vector(3, 1, 2),
        )
    )

    result = mesh.raycast(pos_vector(-.5, -.5, 1), pos_vector(-.5, -.5, -1))
    assert result is not None
    assert result.position == pos_vector(-.5, -.5, 0)
    assert result.normal == pos_vector(0, 0, 1)
    assert result.triangle_index == 0
    assert result.time == .5

    result = mesh.raycast(pos_vector(-.5, -.5, -1), pos_vector(-.5, -.5, 1))
    assert result is not None
    assert result.position == pos_vector(-.5, -.5, 0)
    assert result.normal == pos_vector(0, 0, -1)
    assert result.triangle_index == 0
    assert result.time == .5

    result = mesh.raycast(pos_vector(.5, .5, 1), pos_vector(.5, .5, -1))
    assert result is not None
    assert result.position == pos_vector(.5, .5, 0)
    assert result.normal == pos_vector(0, 0, 1)
    assert result.triangle_index == 1
    assert result.time == .5

    result = mesh.raycast(pos_vector(.5, .5, -1), pos_vector(.5, .5, 1))
    assert result is not None
    assert result.position == pos_vector(.5, .5, 0)
    assert result.normal == pos_vector(0, 0, -1)
    assert result.triangle_index == 1
    assert result.time == .5

    result = mesh.raycast(
        pos_vector(-.75, -.75, 1),
        pos_vector(-.25, -.25, -1)
    )
    assert result is not None
    assert result.position == pos_vector(-.5, -.5, 0)
    assert result.normal == pos_vector(0, 0, 1)
    assert result.triangle_index == 0
    assert result.time == .5

    result = mesh.raycast(pos_vector(-.5, -.5, 2), pos_vector(-.5, -.5, -1))
    assert result is not None
    assert result.position == pos_vector(-.5, -.5, 0)
    assert result.normal == pos_vector(0, 0, 1)
    assert result.triangle_index == 0
    assert result.time == .6666666666666666


@pytest.mark.parametrize("pos_array, pos_vector", [
    (FVector3Array, FVector3),
    (DVector3Array, DVector3),
])
@pytest.mark.parametrize("index_array, index_vector", [
    (UVector3Array, UVector3),
    (U8Vector3Array, U8Vector3),
    (U16Vector3Array, U16Vector3),
    (U32Vector3Array, U32Vector3),
])
def test_raycast_normals(
    pos_array: Any,
    pos_vector: Any,
    index_array: Any,
    index_vector: Any
) -> None:
    mesh = Mesh3d(
        pos_array(
            pos_vector(-1, -1, 0),
            pos_vector(1, -1, 0),
            pos_vector(1, 1, 0),
            pos_vector(-1, 1, 0),
        ),
        index_array(
            index_vector(0, 1, 3),
            index_vector(3, 1, 2),
        ),
        normals=pos_array(
            pos_vector(0, .5, 1).normalize(),
            pos_vector(0, .5, 1).normalize(),
            pos_vector(0, -.5, 1).normalize(),
            pos_vector(0, -.5, 1).normalize(),
        )
    )

    result = mesh.raycast(pos_vector(-.5, -.5, 1), pos_vector(-.5, -.5, -1))
    assert result is not None
    assert result.position == pos_vector(-.5, -.5, 0)
    assert result.normal == pos_vector(
        0,
        0.242535625036333,
        0.9701425001453319
    )
    assert result.triangle_index == 0
    assert result.time == .5

    result = mesh.raycast(pos_vector(-.5, -.5, -1), pos_vector(-.5, -.5, 1))
    assert result is None

    result = mesh.raycast(pos_vector(0, 0, 1), pos_vector(0, 0, -1))
    assert result is not None
    assert result.position == pos_vector(0, 0, 0)
    assert result.normal == pos_vector(0, 0, 1)
    assert result.time == .5

    result = mesh.raycast(pos_vector(-1, -1, 1), pos_vector(-1, -1, -1))
    assert result is not None
    assert result.position == pos_vector(-1, -1, 0)
    assert result.normal == pos_vector(
        0,
        0.44721359549995804,
        0.8944271909999161
    )
    assert result.time == .5

    result = mesh.raycast(pos_vector(1, 1, 1), pos_vector(1, 1, -1))
    assert result is not None
    assert result.position == pos_vector(1, 1, 0)
    assert result.normal == pos_vector(
        0,
        -0.44721359549995804,
        0.8944271909999161
    )
    assert result.time == .5
