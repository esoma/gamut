
from __future__ import annotations

__all__ = ['NavigationMesh3d']

# gamut
from gamut.geometry import LineSegment2d, Triangle3d
from gamut.graph import Graph, SimplePathFinder
from gamut.math import DVector3, FVector3
# python
from math import copysign
from typing import Callable, Generator, Generic, TypeVar

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
        sp = StringPuller(start_point, tri_path, end_point)
        return sp.calculate()


class StringPuller(Generic[T]):

    def __init__(
        self,
        start_point: T,
        triangle_path: tuple[Triangle3d[T], ...],
        end_point: T
    ):
        self.start_point = start_point
        self.end_point = end_point
        # eliminate triangles that truly degenerate to a line or point
        triangle_path = tuple(
            tri for tri in triangle_path
            if len(set(tri.positions)) == 3
        )

        self.path: List[T] = []
        self.triangle_path = triangle_path
        self.triangle_buffer: List[Triangle3d[T]] = []

        if len(triangle_path) == 1:
            self.path = [start_point]
            self.path_iter = iter([])
        else:
            assert triangle_path
            self.apex = start_point
            self.left, self.right = (
                set(triangle_path[0].positions) &
                set(triangle_path[1].positions)
            )
            self.path = [start_point]
            self.path_iter = iter(enumerate(triangle_path[1:]))

    def calculate(self) -> tuple[T, ...]:
        assert self.path_iter is not None
        try:
            while True:
                self._calculate_inner()
        except StopIteration:
            pass
        self.path_iter = None
        self._add_to_path(self.end_point)
        return tuple(self.path)

    def _calculate_inner(self) -> None:
        i, triangle = next(self.path_iter)
        i += 1
        self.triangle_buffer.append(triangle)
        triangle_positions = set(triangle.positions)

        if self.left == self.apex:
            self.left, self.right = self.right, self.left
        area = self._get_funnel_area(self.left, self.right)
        if area < 0:
            self.left, self.right = self.right, self.left
            area = -area

        try:
            next_triangle = set(self.triangle_path[i + 1].positions)
        except IndexError:
            next_triangle = {
                self.end_point,
                self.end_point,
                self.end_point
            }

        assert (
            self.left in triangle_positions and
            self.right in triangle_positions
        )
        next_points = triangle_positions - {self.left, self.right}
        assert len(next_points) == 1
        next_point = next(iter(next_points))

        if self.left in next_triangle:
            funnel_left, funnel_right = self.left, next_point
            funnel_target = self.left
            line_left, line_right = next_point, self.right
            line_target_name = "right"
        else:
            funnel_left, funnel_right = next_point, self.right
            funnel_target = self.right
            line_left, line_right = self.left, next_point
            line_target_name = "left"

        new_area = self._get_funnel_area(funnel_left, funnel_right)
        if sign(new_area) != sign(area) or new_area < 0:
            self._add_to_path(funnel_target)
            self.apex = funnel_target
            while i < len(self.triangle_path) - 1:
                self.left, self.right = next_triangle - {self.apex}
                try:
                    next_next_triangle = set(
                        self.triangle_path[i + 2].positions
                    )
                except IndexError:
                    raise StopIteration()
                if (self.left not in next_next_triangle or
                    self.right not in next_next_triangle):
                    i, _ = next(self.path_iter)
                    i += 1
                    next_triangle = set(self.triangle_path[i + 1].positions)
                    continue
                break
            next(self.path_iter)
        else:
            target = getattr(self, line_target_name)
            if self._get_funnel_area(line_left, line_right) < 0:
                self._add_to_path(target)
                self.apex = target
            setattr(self, line_target_name, next_point)

    def _get_funnel_area(self, left: T, right: T) -> None:
        return ((left - self.apex).cross(right - self.apex)).y

    def _add_to_path(self, point: T) -> None:
        current_y = self.path[-1].y
        path_line = LineSegment2d(self.path[-1].xz, point.xz)

        for triangle in self.triangle_buffer:
            if all((p.y == current_y for p in triangle.positions)):
                continue
            intersections = [
                (intersection, edge)
                for intersection, edge in
                (
                    (
                        path_line.when_line_segments_intersect(
                            LineSegment2d(edge.a.xz, edge.b.xz)
                        ),
                        edge
                    )
                    for edge in triangle.edges
                )
                if intersection is not None
                if intersection[0] > 1e-6
            ]
            intersections.sort(key=lambda i: i[0][0])
            for (path_time, edge_time), edge in intersections:
                new_point = edge.get_point_from_a_to_b(edge_time)
                self.path.append(type(point)(*new_point))
                current_y = new_point.y
            path_line = LineSegment2d(self.path[-1].xz, point.xz)

        self.triangle_buffer.clear()
        self.path.append(point)
