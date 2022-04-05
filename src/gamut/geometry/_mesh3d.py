
from __future__ import annotations

__all__ = ['Mesh3d', 'Mesh3dRaycastHit']

# gamut
from gamut._bullet import Shape
from gamut.math import Matrix4, UVector3Array, Vector3, Vector3Array
# python
from ctypes import c_void_p
from ctypes import cast as c_cast


class Mesh3d:

    def __init__(
        self,
        positions: Vector3Array,
        triangle_indices: UVector3Array,
        *,
        normals: Vector3Array | None = None
    ):
        if not isinstance(positions, Vector3Array):
            raise TypeError('positions must be Vector3Array')
        if not positions:
            raise ValueError('must have at least 1 vertex position')
        self._positions = positions

        self._normals = normals
        if normals is not None:
            if not isinstance(normals, Vector3Array):
                raise TypeError('normals must be Vector3Array')
            if not normals:
                raise ValueError('must have at least 1 vertex normal')

        if not isinstance(triangle_indices, UVector3Array):
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

    def __hash__(self) -> int:
        return id(self)

    def __eq__(self, other: Mesh3d) -> bool:
        if not isinstance(other, Mesh3d):
            return False
        return (
            self._positions == other._positions and
            self._triangle_indices == other._triangle_indices and
            self._normals == other._normals
        )

    def __repr__(self) -> str:
        return f'<gamut.geometry.Mesh3d>'

    def __rmatmul__(self, transform: Matrix4) -> Mesh3d:
        if not isinstance(transform, Matrix4):
            return NotImplemented

        normals: Vector3Array | None = None
        if self._normals is not None:
            normal_transform = transform.inverse().transpose().to_matrix3()
            normals = Vector3Array(*(
                normal_transform @ n for n in self._normals
            ))

        return Mesh3d(
            Vector3Array(*(transform @ p for p in self._positions)),
            self._triangle_indices,
            normals=normals
        )

    def _get_bullet_shape(self) -> Shape:
        if self._bt is None:
            self._bt = Shape(False)
            self._bt_mesh = self._bt.add_mesh((
                len(self._positions),
                c_cast(self._positions.pointer, c_void_p).value,
                len(self._triangle_indices),
                c_cast(self._triangle_indices.pointer, c_void_p).value,
                c_cast(self._normals.pointer, c_void_p).value
                if self._normals else 0,
            ))
        return self._bt

    @property
    def normals(self) -> Vector3Array | None:
        return self._normals

    @property
    def positions(self) -> Vector3Array:
        return self._positions

    @property
    def triangle_indices(self) -> UVector3Array:
        return self._triangle_indices

    def raycast(self, start: Vector3, end: Vector3) -> Mesh3dRaycastHit | None:
        if not isinstance(start, Vector3):
            raise TypeError('start must be Vector3')
        if not isinstance(end, Vector3):
            raise TypeError('end must be Vector3')

        bt = self._get_bullet_shape()
        result = bt.mesh_raycast(start, end)
        if result is None:
            return None
        return Mesh3dRaycastHit(*result)


class Mesh3dRaycastHit:

    def __init__(
        self,
        position: Vector3,
        normal: Vector3,
        triangle_index: int,
        time: float
    ):
        self.position = position
        self.normal = normal
        self.triangle_index = triangle_index
        self.time = time
