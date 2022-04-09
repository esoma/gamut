
from __future__ import annotations

__all__ = ['Mesh2d']

# gamut
from ._mesh3d import Mesh3d
# gamut
from gamut.math import (DMatrix4, DVector2Array, DVector3, DVector3Array,
                        FMatrix4, FVector2Array, FVector3, FVector3Array,
                        U8Vector3Array, U16Vector3Array, U32Vector3Array,
                        UVector3Array)
# python
from typing import Generic, overload, TypeVar

VT = TypeVar('VT', FVector3Array, DVector3Array)
IT = TypeVar(
    'IT',
    U8Vector3Array,
    U16Vector3Array,
    U32Vector3Array,
    UVector3Array
)


class Mesh2d(Generic[VT, IT]):

    def __init__(
        self,
        positions: VT,
        triangle_indices: IT,
    ):
        if not isinstance(positions, (FVector2Array, DVector2Array)):
            raise TypeError('positions must be FVector2Array or DVector2Array')
        if not positions:
            raise ValueError('must have at least 1 vertex position')
        self._positions = positions

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
        for triangle in self._triangle_indices:
            if (triangle.x >= length or
                triangle.y >= length or
                triangle.z >= length):
                raise ValueError(
                    'triangle indices must be between 0 and the number of '
                    'vertices'
                )

    def __hash__(self) -> int:
        return id(self)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Mesh2d):
            return False
        return (
            self._positions == other._positions and
            self._triangle_indices == other._triangle_indices
        )

    def __repr__(self) -> str:
        return f'<gamut.geometry.Mesh2d>'

    @property
    def positions(self) -> DVector2Array:
        return self._positions

    @property
    def triangle_indices(self) -> UVector3Array:
        return self._triangle_indices

    def _parse_swizzle(self, name: str) -> tuple[float, str]:
        if len(name) == 1:
            name = '+' + name
        if len(name) != 2:
            raise ValueError(f'invalid sign/swizzle {name}')
        if name[0] not in '+-':
            raise ValueError(f'invalid sign {name[0]}')
        if name[1] not in 'xy':
            raise ValueError(f'invalid swizzle {name[1]}')
        return (-1 if name[0] == '-' else 1, name[1])

    @overload
    def to_mesh3d(
        self: Mesh2d[FVector2Array, IT],
        x: str | float | int = 'x',
        y: str | float | int = 'y',
        z: str | float | int = 0,
    ) -> Mesh3d[FVector3Array, IT, FMatrix4, FVector3]:
        ...

    @overload
    def to_mesh3d(
        self: Mesh2d[DVector2Array, IT],
        x: str | float | int = 'x',
        y: str | float | int = 'y',
        z: str | float | int = 0,
    ) -> Mesh3d[DVector3Array, IT, DMatrix4, DVector3]:
        ...

    def to_mesh3d(
        self,
        x: str | float | int = 'x',
        y: str | float | int = 'y',
        z: str | float | int = 0,
    ) -> Mesh3d:
        if isinstance(x, (float, int)):
            def get_x(v: VT) -> float | int:
                return x
        elif isinstance(x, str):
            x_sign, x_name = self._parse_swizzle(x)
            def get_x(v: VT) -> float:
                return x_sign * getattr(v, x_name)
        else:
            raise TypeError(f'x must be str or float, got {x}')

        if isinstance(y, (float, int)):
            def get_y(v: VT) -> float | int:
                return y
        elif isinstance(y, str):
            y_sign, y_name = self._parse_swizzle(y)
            def get_y(v: VT) -> float:
                return y_sign * getattr(v, y_name)
        else:
            raise TypeError(f'y must be str or float, got {y}')

        if isinstance(z, (float, int)):
            def get_z(v: VT) -> float | int:
                return z
        elif isinstance(z, str):
            z_sign, z_name = self._parse_swizzle(z)
            def get_z(v: VT) -> float:
                return z_sign * getattr(v, z_name)
        else:
            raise TypeError(f'z must be str or float, got {z}')

        if isinstance(self._positions, DVector2Array):
            array_3 = DVector3Array
            vec_3 = DVector3
        else:
            array_3 = FVector3Array
            vec_3 = FVector3
        positions_3d = array_3(*(
            vec_3(get_x(p), get_y(p), get_z(p))
            for p in self._positions
        ))
        return Mesh3d(positions_3d, self.triangle_indices)
