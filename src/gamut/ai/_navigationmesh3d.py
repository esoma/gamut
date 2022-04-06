
from __future__ import annotations

__all__ = ['NavigationMesh3d']

# gamut
from gamut.geometry import LineSegment2d, LineSegment3d, Triangle3d
from gamut.graph import Graph, SimplePathFinder
from gamut.math import DVector3, FVector3
# python
from math import copysign
from typing import Callable, Generator, TypeVar

T = TypeVar('T', FVector3, DVector3)


def sign(x: float) -> float:
    return copysign(1, x)


def default_calculate_weight(a: Triangle3d[T], b: Triangle3d[T]) -> float:
    return a.center.distance(b.center)


class NavigationMesh3d(Graph[Triangle3d[T], float]):

    def __init__(
        self,
        calculate_weight: Callable[
            [Triangle3d[T], Triangle3d[T]],
            float
        ] | None = None,
    ):
        if calculate_weight is None:
            self._calculate_weight = default_calculate_weight
        else:
            self._calculate_weight = calculate_weight
        self._graph: Graph[Triangle3d[T], float] = Graph()
        self._edge_triangle: dict[tuple[T, T], set[Triangle3d[T]]] = {}

    def _get_triangle_edges(
        self,
        triangle: Triangle3d[T]
    ) -> Generator[tuple[T, T], None, None]:
        yield tuple(sorted((triangle.positions[0], triangle.positions[1])))
        yield tuple(sorted((triangle.positions[1], triangle.positions[2])))
        yield tuple(sorted((triangle.positions[2], triangle.positions[0])))

    def _string_pull_path(
        self,
        start_point: T,
        path: tuple[Triangle3d[T], ...],
        end_point: T
    ) -> tuple[P, ...]:
        if len(path) == 1:
            return (start_point, end_point)

        apex = start_point
        start_i = 1
        left, right = set(path[0].positions) & set(path[1].positions)

        new_path: list[T] = [apex]
        tris_between: list[Triangle3d[T]] = []
        # funnel algorithm doesn't account for movement in the y axis, so
        # when adding a point to the path we draw a line over the tris between
        # the previous point and the new one, wherever the line intersects a
        # tri with a different y value we insert those interections as points
        # between the old point and new point
        def add_to_path(point: T) -> None:
            current_y = new_path[-1].y
            path_line = LineSegment2d(new_path[-1].xz, point.xz)
            for tri in tris_between:
                if all((p.y == current_y for p in set(tri.positions))):
                    continue
                intersections = [
                    (intersection, edge)
                    for intersection, edge in
                    (
                        (
                            path_line.get_line_segment_intersection(
                                LineSegment2d(edge[0].xz, edge[1].xz)
                            ),
                            edge
                        )
                        for edge in self._get_triangle_edges(tri)
                    )
                    if intersection is not None
                    if intersection[0] > 1e-6
                ]
                intersections.sort(key=lambda i: i[0][0])
                for (path_time, edge_time), edge in intersections:
                    edge_line = LineSegment3d(*edge)
                    new_point = edge_line.get_point_from_a_to_b(edge_time)
                    new_path.append(type(point)(*new_point))
                    current_y = new_point.y

                path_line = LineSegment2d(new_path[-1].xz, point.xz)

            tris_between.clear()
            new_path.append(point)
        # funnel algorithm
        try:
            path_iter = enumerate(path[start_i:])
            while True:
                i, triangle = next(path_iter)
                tris_between.append(triangle)
                triangle_positions = set(triangle.positions)

                if left == apex:
                    left, right = right, left
                area = ((left - apex).cross(right - apex)).y
                if area < 0:
                    left, right = right, left
                    area = -area

                try:
                    next_triangle = set(path[i + start_i + 1].positions)
                except IndexError:
                    next_triangle = {end_point, end_point, end_point}

                assert (
                    left in triangle_positions and
                    right in triangle_positions
                )
                next_points = triangle_positions - {left, right}
                assert len(next_points) == 1
                next_point = next(iter(next_points))

                if left in next_triangle and right in next_triangle:
                    continue

                if left in next_triangle:
                    new_area = ((left - apex).cross(next_point - apex)).y
                    if sign(new_area) != sign(area) or new_area <= 0:
                        add_to_path(left)
                        apex = left
                        while i < len(path) - 2:
                            left, right = next_triangle - {apex}
                            try:
                                next_next_triangle = set(
                                    path[i + start_i + 2].positions
                                )
                            except IndexError:
                                raise StopIteration()
                            if (left not in next_next_triangle or
                                right not in next_next_triangle):
                                i, _ = next(path_iter)
                                next_triangle = set(
                                    path[i + start_i + 1].positions
                                )
                                continue
                            break
                        next(path_iter)
                    else:
                        if ((next_point - apex).cross(right - apex)).y < 0:
                            add_to_path(right)
                        right = next_point

                else:
                    new_area = ((next_point - apex).cross(right - apex)).y
                    if sign(new_area) != sign(area) or new_area <= 0:
                        add_to_path(right)
                        apex = right
                        while i < len(path) - 2:
                            left, right = next_triangle - {apex}
                            try:
                                next_next_triangle = set(
                                    path[i + start_i + 2].positions
                                )
                            except IndexError:
                                raise StopIteration()
                            if (left not in next_next_triangle or
                                right not in next_next_triangle):
                                i, _ = next(path_iter)
                                next_triangle = set(
                                    path[i + start_i + 1].positions
                                )
                                continue
                            break
                        next(path_iter)
                    else:
                        if ((left - apex).cross(next_point - apex)).y < 0:
                            add_to_path(left)
                        left = next_point
        except StopIteration:
            pass

        add_to_path(end_point)

        return tuple(new_path)

    def add_triangle(self, triangle: Triangle3d[T]) -> None:
        if self._graph.contains_node(triangle):
            return
        self._graph.add_node(triangle)
        for edge in self._get_triangle_edges(triangle):
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

    def contains_triangle(self, triangle: Triangle3d[T]) -> bool:
        return self._graph.contains_node(triangle)

    def remove_triangle(self, triangle: Triangle3d[T]) -> None:
        self._graph.remove_node(triangle)
        for edge in self._get_triangle_edges(triangle):
            try:
                edge_triangles = self._edge_triangle[edge]
            except KeyError:
                continue
            if len(edge_triangles) == 1:
                del self._edge_triangle[edge]
            else:
                edge_triangles.remove(triangle)

    @property
    def triangles(self) -> Generator[Triangle3d[T], None, None]:
        yield from self._graph.nodes

    def find_path(
        self,
        start_point: T,
        start_triangle: Triangle3d[T],
        end_point: T,
        end_triangle: Triangle3d[T]
    ) -> tuple[P, ...] | None:
        finder = SimplePathFinder(self._graph, start_triangle, end_triangle)
        try:
            tri_path = next(finder)
        except StopIteration:
            return None
        # python
        import pprint
        pprint.pprint(tri_path)
        return self._string_pull_path(start_point, tri_path, end_point)
