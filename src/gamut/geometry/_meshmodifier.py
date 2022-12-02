
from __future__ import annotations

__all__ = ['MeshModifier']

# gamut
from ._linesegment3d import LineSegment3d
from ._mesh3d import Mesh3d
from ._triangle3d import Triangle3d
# gamut
from gamut.math import (DMatrix4, DVector3, DVector3Array, FMatrix4, FVector3,
                        FVector3Array, IVector3, IVector3Array, U8Vector3Array,
                        U16Vector3Array, U32Vector3Array, UVector3Array)
# python
from itertools import product
from typing import Generator, Generic, overload, TypeAlias, TypeVar
# numpy
from numpy import array_equal as np_array_equal
from numpy import frombuffer as np_from_buffer

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


EdgeIndices: TypeAlias = tuple[int, int]


class MeshModifier(Generic[VT, IT, MT, PT]):

    def __init__(self, mesh: Mesh3d[VT, IT, MT, PT]):
        self._vertex_type = mesh.positions.get_component_type()
        self._vertex_array_type = type(mesh.positions)
        self._tri_index_array_type = type(mesh.triangle_indices)

        self._positions = np_from_buffer(
            mesh.positions,
            dtype='f'
        ).reshape((len(mesh.positions), 3)).copy()
        self._triangle_indices = np_from_buffer(
            mesh.triangle_indices,
            dtype='I'
        ).reshape((len(mesh.triangle_indices), 3)).copy()

        self._vertices_edges: dict[int, set[EdgeIndices]] = {}
        self._vertices_position_duplicates: dict[int, set[int]] = {}

        self._edge_position_duplicates: dict[EdgeIndices, set[EdgeIndices]] = (
            {}
        )

        self._edges_tris: dict[tuple[int, int], dict[int, PT]] = {}
        self._verts_verts: dict[int, set[int]] = {}

    def _generate_edges_tris(self) -> None:
        if self._edges_tris:
            return
        for tri_index, tri_indices in enumerate(self._triangle_indices):
            tri = Triangle3d(*(
                self._vertex_type(*self._positions[i])
                for i in tri_indices
            ))
            for i, (vai, vbi) in enumerate(((0, 1), (1, 2), (2, 0))):
                vai_duplicates = self.get_vertex_position_duplicates(tri_indices[vai])
                vbi_duplicates = self.get_vertex_position_duplicates(tri_indices[vbi])
                edge = LineSegment3d(
                    self._vertex_type(*self._positions[tri_indices[vai]]),
                    self._vertex_type(*self._positions[tri_indices[vbi]])
                )
                vais = (tri_indices[vai], *vai_duplicates)
                vbis = (tri_indices[vbi], *vbi_duplicates)
                for v0, v1 in product(vais, vbis):
                    edge_indices = tuple(sorted((v0, v1)))
                    edge_tris = self._edges_tris.setdefault(edge_indices, {})
                    if tri_index not in edge_tris:
                        edge_tris[tri_index] = tri.get_edge_normal(edge)

    def get_edges_tris(self) -> Generator[
        tuple[tuple[int, int], tuple[int, ...]],
        None,
        None
    ]:
        self._generate_edges_tris()
        return ((e, tuple(t.keys())) for e, t in self._edges_tris.items())

    def get_edge_tris(
        self,
        edge: tuple[int, int]
    ) -> Generator[int, None, None]:
        self._generate_edges_tris()
        return self._edges_tris[edge].keys()

    def _generate_verts_verts(self) -> None:
        if self._verts_verts:
            return
        for tri_indices in self._triangle_indices:
            for vi in tri_indices:
                vert_verts = self.verts_verts.setdefault(vi, set())
                vert_verts.update(i for i in tri_indices if i != vi)

    def get_edge_normals(self, edge: tuple[int, int]) -> Generator[PT]:
        self._generate_edges_tris()
        return self._edges_tris[edge].values()

    def _generate_vertices_edges(self) -> None:
        if self._vertices_edges:
            return
        for tri_indices in self._triangle_indices:
            for vai, vbi in ((0, 1), (1, 2), (2, 0)):
                vai_duplicates = self.get_vertex_position_duplicates(tri_indices[vai])
                vbi_duplicates = self.get_vertex_position_duplicates(tri_indices[vbi])
                vais = (tri_indices[vai], *vai_duplicates)
                vbis = (tri_indices[vbi], *vbi_duplicates)
                for v0, v1 in product(vais, vbis):
                    edge_indices = tuple(sorted((v0, v1)))
                    for i in range(2):
                        edges = self._vertices_edges.setdefault(
                            edge_indices[i],
                            set()
                        )
                        edges.add(edge_indices)

    def get_vertex_edges(self,
        vertex_index: int
    ) -> Generator[EdgeIndices, None, None]:
        self._generate_vertices_edges()
        return iter(self._vertices_edges[vertex_index])

    def get_vertex_position_duplicates(
        self,
        vertex_index: int
    ) -> Generator[int, None, None]:
        try:
            return iter(self._vertices_position_duplicates[vertex_index])
        except KeyError:
            pass
        pos = self._positions[vertex_index]
        duplicates = set()
        for i, opos in enumerate(self._positions):
            if i == vertex_index:
                continue
            if np_array_equal(pos, opos):
                duplicates.add(i)
        self._vertices_position_duplicates[vertex_index] = duplicates
        return iter(duplicates)

    def get_edge_position_duplicates(
        self,
        edge: EdgeIndices
    ) -> Generator[EdgeIndices, None, None]:
        try:
            return iter(self._edge_position_duplicates[edge])
        except KeyError:
            pass

        duplicates = set()
        vai_duplicates = self.get_vertex_position_duplicates(edge[0])
        vbi_duplicates = self.get_vertex_position_duplicates(edge[1])
        vais = (edge[0], *vai_duplicates)
        vbis = (edge[1], *vbi_duplicates)
        for v0, v1 in product(vais, vbis):
            edge_indices = tuple(sorted((v0, v1)))
            if edge_indices == edge:
                continue
            duplicates.add(edge_indices)

        self._edge_position_duplicates[edge] = duplicates
        return iter(duplicates)

    # modifying methods

    def get_vertex_position(self, vertex_index: int) -> PT:
        return self._vertex_type(*self._positions[vertex_index])

    def set_vertex_position(self, vertex_index: int, position: PT) -> None:
        duplicates = self.get_vertex_position_duplicates(vertex_index)
        for vi in (vertex_index, *duplicates):
            self._positions[vi] = position

    def displace_border(self, amount: PT) -> None:
        vertices_to_displace = list(range(len(self._positions)))
        vertices_processed = set()
        while vertices_to_displace:
            vertex = vertices_to_displace.pop()
            if vertex in vertices_processed:
                continue
            duplicates = self.get_vertex_position_duplicates(vertex)
            vertex_indexes = (vertex, *duplicates)
            vertices_processed.update(vertex_indexes)

            normals = []
            edges_processed = set()
            __pos = self.get_vertex_position(vertex)
            if __pos == FVector3(-6, 2, 4):
                print(vertex)
            for edge in self.get_vertex_edges(vertex):
                edge_duplicates = self.get_edge_position_duplicates(edge)
                if edge in edges_processed:
                    continue
                if __pos == FVector3(-6, 2, 4):
                    print(edge)
                    print(self.get_vertex_position(edge[0]))
                    print(self.get_vertex_position(edge[1]))
                edges_processed.add(edge)
                edges_processed.update(edge_duplicates)
                if len(self.get_edge_tris(edge)) != 1:
                    continue
                for normal in self.get_edge_normals(edge):
                    #normals.append(normal.xoz.normalize())
                    normals.append(normal)
            if not normals:
                continue

            normal = (sum(normals) / len(normals)).normalize()
            new_position = self.get_vertex_position(vertex) + normal * amount
            self.set_vertex_position(vertex, new_position)

    def build(self) -> Mesh3d[VT, IT, MT, PT]:
        return Mesh3d(
            self._vertex_array_type.from_buffer(self._positions),
            self._tri_index_array_type.from_buffer(self._triangle_indices)
        )
