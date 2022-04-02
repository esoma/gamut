
from __future__ import annotations

__all__ = ['NavigationMesh3d']

# gamut
from ._graph import Graph
from ._simplepathfinder import SimplePathFinder
# gamut
from gamut.math import DVector3, FVector3
# python
from math import copysign
from typing import Callable, Generator, TypeVar

P = TypeVar('P', FVector3, DVector3)


def sign(x: float) -> float:
    return copysign(1, x)


def default_calculate_weight(a: tuple[P, P, P], b: tuple[P, P, P]) -> float:
    return sum((sum(a) / 3) - (sum(b) / 3)) ** 2


class NavigationMesh3d(Graph[tuple[P, P, P], float]):

    def __init__(
        self,
        calculate_weight: Callable[
            [tuple[P, P, P], tuple[P, P, P]],
            float
        ] | None = None,
    ):
        if calculate_weight is None:
            self._calculate_weight = default_calculate_weight
        else:
            self._calculate_weight = calculate_weight
        self._graph: Graph[tuple[P, P, P], float] = Graph()
        self._edge_triangle: dict[tuple[P, P], set[tuple[P, P, P]]] = {}

    def _triangle(self, a: P, b: P, c: P) -> tuple[P, P, P]:
        return tuple(sorted((a, b, c), key=lambda p: hash(p)))

    def _string_pull_path(
        self,
        start_point: P,
        path: tuple[tuple[P, P, P], ...],
        end_point: P
    ) -> tuple[P, ...]:
        apex = start_point
        left, right = set(path[0]) - {apex}
        new_path: list[P] = [apex]

        try:
            path_iter = enumerate(path[1:-1])
            while True:
                i, triangle = next(path_iter)
                area = ((left - apex).cross(right - apex)).y
                if area < 0:
                    left, right = right, left
                    area = -area

                next_triangle = set(path[i + 2])
                assert left in triangle and right in triangle
                next_points = set(triangle) - {left, right}
                assert len(next_points) == 1
                next_point = next(iter(next_points))

                if left in next_triangle:
                    assert right not in next_triangle
                    new_area = ((left - apex).cross(next_point - apex)).y
                    if sign(new_area) != sign(area) or new_area <= 0:
                        new_path.append(left)
                        apex = left
                        while True:
                            left, right = next_triangle - {apex}
                            try:
                                next_next_triangle = set(path[i + 3])
                            except IndexError:
                                raise StopIteration()
                            if (left not in next_next_triangle or
                                right not in next_next_triangle):
                                i, _ = next(path_iter)
                                next_triangle = set(path[i + 2])
                                continue
                            break
                        next(path_iter)
                    else:
                        if ((next_point - apex).cross(right - apex)).y < 0:
                            new_path.append(right)
                        right = next_point

                else:
                    assert right in next_triangle
                    new_area = ((next_point - apex).cross(right - apex)).y
                    if sign(new_area) != sign(area) or new_area <= 0:
                        new_path.append(right)
                        apex = right
                        while True:
                            left, right = next_triangle - {apex}
                            try:
                                next_next_triangle = set(path[i + 3])
                            except IndexError:
                                raise StopIteration()
                            if (left not in next_next_triangle or
                                right not in next_next_triangle):
                                i, _ = next(path_iter)
                                next_triangle = set(path[i + 2])
                                continue
                            break
                        next(path_iter)
                    else:
                        if ((left - apex).cross(next_point - apex)).y < 0:
                            new_path.append(left)
                        left = next_point
        except StopIteration:
            pass

        new_path.append(end_point)

        return tuple(new_path)

    def add_triangle(self, a: P, b: P, c: P) -> None:
        triangle = self._triangle(a, b, c)
        if self._graph.contains_node(triangle):
            return
        self._graph.add_node(triangle)
        for edge in (
            (triangle[0], triangle[1]),
            (triangle[1], triangle[2]),
            (triangle[0], triangle[2]),
        ):
            try:
                edge_triangles = self._edge_triangle[edge]
            except KeyError:
                edge_triangles = self._edge_triangle[edge] = set()
            for edge_triangle in edge_triangles:
                self._graph.add_edge(
                    triangle,
                    edge_triangle,
                    self._calculate_weight(triangle, edge_triangle)
                )
            edge_triangles.add(triangle)

    def contains_triangle(self, a: P, b: P, c: P) -> bool:
        triangle = self._triangle(a, b, c)
        return self._graph.contains_node(triangle)

    def remove_triangle(self, a: P, b: P, c: P) -> None:
        triangle = self._triangle(a, b, c)
        self._graph.remove_node(triangle)
        for edge in (
            (triangle[0], triangle[1]),
            (triangle[1], triangle[2]),
            (triangle[0], triangle[2]),
        ):
            try:
                edge_triangles = self._edge_triangle[edge]
            except KeyError:
                continue
            if len(edge_triangles) == 1:
                del self._edge_triangle[edge]
            else:
                edge_triangles.remove(triangle)

    @property
    def triangles(self) -> Generator[tuple[P, P, P], None, None]:
        yield from self._graph.nodes

    def find_path(
        self,
        start: tuple[P, P, P],
        end: tuple[P, P, P]
    ) -> tuple[P, ...] | None:
        start_point = start[0]
        end_point = end[0]
        start = self._triangle(*start)
        end = self._triangle(*end)

        temporary_triangles: list[tuple[P, P, P]] = []
        for new_triangle in (start, end):
            if not self._graph.contains_node(new_triangle):
                self.add_triangle(*new_triangle)
                temporary_triangles.append(new_triangle)

        finder = SimplePathFinder(self._graph, start, end)
        try:
            tri_path = next(finder)
        except StopIteration:
            tri_path = None
        if tri_path is not None:
            point_path = self._string_pull_path(
                start_point,
                tri_path,
                end_point
            )
        else:
            point_path = None

        for temporary_triangle in temporary_triangles:
            self.remove_triangle(*temporary_triangle)

        return point_path
