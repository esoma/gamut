
from __future__ import annotations

__all__ = ['Mesh3d', 'Mesh3dRaycastHit']

# gamut
from gamut._bullet import Shape
from gamut.math import (DMatrix4, DVector3, DVector3Array, FMatrix4, FVector3,
                        FVector3Array, IVector3, IVector3Array, U8Vector3Array,
                        U16Vector3Array, U32Vector3Array, UVector3Array)
# python
# DVector4
from ctypes import c_void_p
from ctypes import cast as c_cast
from typing import Generic, overload, TypeVar

VT = TypeVar('VT', FVector3Array, DVector3Array)
IT = TypeVar(
    'IT',
    U8Vector3Array,
    U16Vector3Array,
    U32Vector3Array,
    UVector3Array
)
MT = TypeVar('MT', FMatrix4, DMatrix4)
PT = TypeVar('PT', FVector3, DVector3)


class Mesh3d(Generic[VT, IT, MT, PT]):

    @overload
    def __init__(
        self: Mesh3d[FVector3Array, IT, FMatrix4, FVector3],
        positions: FVector3Array,
        triangle_indices: IT,
        *,
        normals: FVector3Array | None = None
    ):
        ...

    @overload
    def __init__(
        self: Mesh3d[DVector3Array, IT, DMatrix4, DVector3],
        positions: DVector3Array,
        triangle_indices: IT,
        *,
        normals: DVector3Array | None = None
    ):
        ...

    def __init__(
        self,
        positions: FVector3Array | DVector3Array,
        triangle_indices:
            U8Vector3Array |
            U16Vector3Array |
            U32Vector3Array |
            UVector3Array,
        *,
        normals: FVector3Array | DVector3Array | None = None
    ):
        if not isinstance(positions, (FVector3Array, DVector3Array)):
            raise TypeError('positions must be FVector3Array or DVector3Array')
        if not positions:
            raise ValueError('must have at least 1 vertex position')
        self._positions = positions

        self._normals = normals
        if normals is not None:
            if not isinstance(normals, type(self._positions)):
                raise TypeError(
                    f'normals must be {type(self._positions).__name__}'
                )
            if not normals:
                raise ValueError('must have at least 1 vertex normal')

        if not isinstance(
            triangle_indices, (
                U8Vector3Array,
                U16Vector3Array,
                U32Vector3Array,
                UVector3Array
            )
        ):
            raise TypeError('indices must be UVector3Array')
        if not triangle_indices:
            raise ValueError('must have at least 1 triangle')
        self._triangle_indices = triangle_indices

        length = len(positions)
        if normals is not None:
            length = min(length, len(normals))
        for triangle in self._triangle_indices:
            if (triangle.x >= length or
                triangle.y >= length or
                triangle.z >= length):
                raise ValueError(
                    'triangle indices must be between 0 and the number of '
                    'vertices'
                )

        self._bt: Shape | None = None
        self._bt_mesh: Any = None
        self._bt_mesh_data: Any = None

    def __hash__(self) -> int:
        return id(self)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Mesh3d):
            return False
        return (
            self._positions == other._positions and
            self._triangle_indices == other._triangle_indices and
            self._normals == other._normals
        )

    def __repr__(self) -> str:
        return f'<gamut.geometry.Mesh3d>'

    def __rmatmul__(self, transform: MT) -> Mesh3d:
        if not isinstance(transform, (FMatrix4, DMatrix4)):
            return NotImplemented

        normals: VT | None = None
        if self._normals is not None:
            normal_transform = transform.inverse().transpose().to_matrix3()
            normals = type(self._normals)(*(
                normal_transform @ n for n in self._normals
            ))

        return Mesh3d(
            type(self._positions)(*(transform @ p for p in self._positions)),
            self._triangle_indices,
            normals=normals
        )

    def _get_bullet_shape(self) -> Shape:
        if self._bt is None:
            try:
                self._bt = Shape(False)

                if isinstance(self._positions, DVector3Array):
                    positions = self._positions
                else:
                    positions = DVector3Array(*(
                        DVector3(*p) for p in self._positions
                    ))

                triangle_indices = IVector3Array(*(
                    IVector3(*tri)
                    for tri in self._triangle_indices
                ))

                if self._normals is None:
                    normals = None
                else:
                    if isinstance(self._normals, DVector3Array):
                        normals = self._normals
                    else:
                        normals = DVector3Array(*(
                            DVector3(*p) for p in self._normals
                        ))

                self._bt_mesh_data = (positions, triangle_indices, normals)
                self._bt_mesh = self._bt.add_mesh((
                    len(positions),
                    c_cast(positions.pointer, c_void_p).value,
                    len(triangle_indices),
                    c_cast(triangle_indices.pointer, c_void_p).value,
                    c_cast(normals.pointer, c_void_p).value
                    if normals else 0,
                ))
            except BaseException:
                self._bt = None
                self._bt_mesh_data = None
                self._bt_mesh = None
                raise
        return self._bt

    @property
    def normals(self) -> VT | None:
        return self._normals

    @property
    def positions(self) -> VT:
        return self._positions

    @property
    def triangle_indices(self) -> IT:
        return self._triangle_indices

    def raycast(self, start: PT, end: PT) -> Mesh3dRaycastHit[PT] | None:
        v_type = self._positions.get_component_type()
        if not isinstance(start, v_type):
            raise TypeError(f'start must be {v_type.__name__}')
        if not isinstance(end, v_type):
            raise TypeError(f'end must be {v_type.__name__}')

        bt = self._get_bullet_shape()
        result = bt.mesh_raycast(*start, *end)
        if result is None:
            return None
        return Mesh3dRaycastHit(
            v_type(result[0], result[1], result[2]),
            v_type(result[3], result[4], result[5]),
            result[6],
            result[7]
        )


class Mesh3dRaycastHit(Generic[PT]):

    def __init__(
        self,
        position: PT,
        normal: PT,
        triangle_index: int,
        time: float
    ):
        self.position = position
        self.normal = normal
        self.triangle_index = triangle_index
        self.time = time
