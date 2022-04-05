
from __future__ import annotations

__all__ = ['NavigationMesh3d']

# gamut
from gamut.geometry import LineSegment2d, LineSegment3d
from gamut.graph import Graph, SimplePathFinder
from gamut.math import DVector3, FVector3
# python
from math import copysign
from typing import Callable, Generator, TypeVar

P = TypeVar('P', FVector3, DVector3)


def sign(x: float) -> float:
    return copysign(1, x)


def default_calculate_weight(a: tuple[P, P, P], b: tuple[P, P, P]) -> float:
    return (sum(a) / 3).distance(sum(b) / 3)


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
        print("________________________")
        # python
        import pprint
        pprint.pprint(path)
        # it's possible that the start point is in multiple tris along the path
        # so we find the last tri that contains it and use that as the starting
        # tri
        print(start_point)
        apex = start_point
        start_i = 0
        left, right = set(path[0]) & set(path[1])

        """
        for start_i, triangle in enumerate(path[:-1]):
            next_triangle = path[start_i + 1]
            if start_point not in next_triangle:
                print(triangle)
                left, right = set(triangle) - {apex}
                break
        start_i += 1
        """

        new_path: list[P] = [apex]
        tris_between: list[tuple[P, P, P]] = []
        # funnel algorithm doesn't account for movement in the y axis, so
        # when adding a point to the path we draw a line over the tris between
        # the previous point and the new one, wherever the line intersects a
        # tri with a different y value we insert those interections as points
        # between the old point and new point
        def add_to_path(point: P) -> None:
            current_y = new_path[-1].y
            path_line = LineSegment2d(new_path[-1].xz, point.xz)
            for tri in tris_between:
                if all((p.y == current_y for p in tri)):
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
                        for edge in (
                            (tri[0], tri[1]),
                            (tri[1], tri[2]),
                            (tri[2], tri[0]),
                        )
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
            path_iter = enumerate(path[start_i:-1])
            while True:
                i, triangle = next(path_iter)
                tris_between.append(triangle)

                area = ((left - apex).cross(right - apex)).y
                if area < 0:
                    left, right = right, left
                    area = -area
                next_triangle = set(path[i + start_i + 1])
                assert left in triangle and right in triangle
                next_points = set(triangle) - {left, right}
                assert len(next_points) == 1
                next_point = next(iter(next_points))

                if left in next_triangle and right in next_triangle:
                    continue

                print("--------------------------")
                print(left)
                print(right)
                print(next_triangle)

                if left in next_triangle:
                    new_area = ((left - apex).cross(next_point - apex)).y
                    if sign(new_area) != sign(area) or new_area <= 0:
                        add_to_path(left)
                        apex = left
                        while True:
                            left, right = next_triangle - {apex}
                            try:
                                next_next_triangle = set(path[i + start_i + 2])
                            except IndexError:
                                raise StopIteration()
                            if (left not in next_next_triangle or
                                right not in next_next_triangle):
                                i, _ = next(path_iter)
                                next_triangle = set(path[i + start_i + 1])
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
                        while True:
                            left, right = next_triangle - {apex}
                            try:
                                next_next_triangle = set(path[i + start_i + 2])
                            except IndexError:
                                raise StopIteration()
                            if (left not in next_next_triangle or
                                right not in next_next_triangle):
                                i, _ = next(path_iter)
                                next_triangle = set(path[i + start_i + 1])
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
        start_point: P,
        start_triangle: tuple[P, P, P],
        end_point: P,
        end_triangle: tuple[P, P, P]
    ) -> tuple[P, ...] | None:
        start_triangle = self._triangle(*start_triangle)
        end_triangle = self._triangle(*end_triangle)

        """
        temporary_triangles: list[tuple[P, P, P]] = []
        for new_point, new_triangle in (
            (start_point, start_triangle),
            (end_point, end_triangle)
        ):
            if not self._graph.contains_node(new_triangle):
                raise ValueError('triangle not in navigation mesh')
            if new_point in new_triangle:
                continue
            for temp_triangle in (
                self._triangle(new_point, new_triangle[0], new_triangle[1]),
                self._triangle(new_point, new_triangle[0], new_triangle[2]),
                self._triangle(new_point, new_triangle[1], new_triangle[2]),
            ):
                self.add_triangle(*temp_triangle)
                temporary_triangles.append(temp_triangle)
            if new_point is start_point:
                start_triangle = temp_triangle
            else:
                assert new_point is end_point
                end_triangle = temp_triangle
        """
        finder = SimplePathFinder(self._graph, start_triangle, end_triangle)
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

        """
        for temporary_triangle in temporary_triangles:
            self.remove_triangle(*temporary_triangle)
        """

        return point_path
