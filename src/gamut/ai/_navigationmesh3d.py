
from __future__ import annotations

__all__ = ['NavigationMesh3d']

# gamut
from gamut.geometry import (
    get_max_circle_radius_between_point_and_line_segment_along_direction,
    LineSegment2d, LineSegment3d, Triangle3d)
from gamut.graph import Graph, SimplePathFinder
from gamut.graphics import (BufferView, BufferViewMap, DepthTest,
                            execute_shader, FaceCull, PrimitiveMode, Shader,
                            TextureRenderTarget, WindowRenderTarget)
from gamut.math import DVector3, FMatrix4, FVector3, FVector3Array
# python
from math import copysign, inf
from typing import Callable, Final, Generator, Generic, TYPE_CHECKING, TypeVar

T = TypeVar('T', FVector3, DVector3)


def sign(x: float) -> float:
    return copysign(1, x)


def default_calculate_weight(a: Triangle3d[T], b: Triangle3d[T]) -> float:
    return a.center.distance(b.center)


check_radius = (
    get_max_circle_radius_between_point_and_line_segment_along_direction
)


def get_triangle_edges(
    triangle: Triangle3d[T]
) -> Generator[tuple[T, T], None, None]:
    yield tuple(sorted((triangle.positions[0], triangle.positions[1])))
    yield tuple(sorted((triangle.positions[1], triangle.positions[2])))
    yield tuple(sorted((triangle.positions[2], triangle.positions[0])))


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
        self._point_triangle: dict[T, set[Triangle3d[T]]] = {}
        self._edge_triangle: dict[tuple[T, T], set[Triangle3d[T]]] = {}
        self._point_normal: dict[T, T] = {}
        self._point_max_radius: dict[T, float] = {}
        self._edge_max_radius: dict[tuple[T, T], tuple[float, float]] = {}
        self._edge_normal: dict[tuple[T, T], T] = {}

    def _recalculate_point_max_radius(self) -> None:
        self._point_max_radius = {}
        for point in self._point_triangle:
            normal = self._get_point_normal(point)
            max_radius = inf
            for tri in self._graph.nodes:
                for edge in get_triangle_edges(tri):
                    if len(self._edge_triangle[edge]) > 1:
                        continue
                    if (
                        point in edge or
                        (edge[0].y != point.y and edge[1].y != point.y)
                    ):
                        continue
                    edge_2d = LineSegment2d(edge[0].xz, edge[1].xz)
                    r = check_radius(point.xz, edge_2d, normal.xz)
                    max_radius = min(max_radius, r)
            self._point_max_radius[point] = max_radius

    def _recalculate_edge_max_radius(self) -> None:
        self._edge_max_radius = {}
        for edge in self._edge_triangle:
            max_radius_a = max_radius_b = inf
            a_slope = (edge[1] - edge[0]).xz
            b_slope = (edge[0] - edge[1]).xz
            for tri in self._graph.nodes:
                for tri_edge in get_triangle_edges(tri):
                    if len(self._edge_triangle[tri_edge]) > 1:
                        continue
                    tri_edge_2d = LineSegment2d(tri_edge[0].xz, tri_edge[1].xz)
                    if edge[0] not in tri_edge:
                        r = check_radius(edge[0].xz, tri_edge_2d, a_slope)
                        max_radius_a = min(max_radius_a, r)
                    if edge[1] not in tri_edge:
                        r = check_radius(edge[1].xz, tri_edge_2d, b_slope)
                        max_radius_b = min(max_radius_b, r)
            self._edge_max_radius[edge] = (max_radius_a, max_radius_b)

    def add_triangle(self, triangle: Triangle3d[T]) -> None:
        if self._graph.contains_node(triangle):
            return
        self._graph.add_node(triangle)
        for edge in get_triangle_edges(triangle):
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
        for point in triangle.positions:
            try:
                point_triangles = self._point_triangle[point]
            except KeyError:
                point_triangles = self._point_triangle[point] = set()
            point_triangles.add(triangle)
            # clear normal cache for the point
            try:
                del self._point_normal[point]
            except KeyError:
                pass

    def _get_point_normal(self, point: T) -> T:
        try:
            return self._point_normal[point]
        except KeyError:
            pass
        tris = self._point_triangle[point]
        normals = []
        for tri in tris:
            for edge, normal in zip(get_triangle_edges(tri), tri.edge_normals):
                if point not in edge:
                    continue
                if len(self._edge_triangle[edge]) == 1:
                    normals.append(-normal.xoz)
        normal = (sum(normals) / len(normals)).normalize()
        self._point_normal[point] = normal
        return normal

    def contains_triangle(self, triangle: Triangle3d[T]) -> bool:
        return self._graph.contains_node(triangle)

    def remove_triangle(self, triangle: Triangle3d[T]) -> None:
        self._graph.remove_node(triangle)
        for edge in get_triangle_edges(triangle):
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

    @property
    def walls(self) -> Generator[Tuple[T, T], None, None]:
        for tri in self._graph.nodes:
            for edge in get_triangle_edges(tri):
                if len(self._edge_triangle[edge]) > 1:
                    continue
                yield edge

    def find_path(
        self,
        start_point: T,
        start_triangle: Triangle3d[T],
        end_point: T,
        end_triangle: Triangle3d[T],
        *,
        radius: float = 0,
        footprint_radius: float | None = None,
        squeeze: bool = False,
        debug: Debug | Optional = None
    ) -> tuple[P, ...] | None:
        radius = float(radius)
        if footprint_radius is None:
            footprint_radius = radius
        else:
            footprint_radius = float(footprint_radius)

        if radius > 0 or footprint_radius > 0:
            self._recalculate_point_max_radius()
            self._recalculate_edge_max_radius()

        finder = SimplePathFinder(self._graph, start_triangle, end_triangle)
        if debug:
            debug.clear_path_points()
            debug.clear_path_tris()
            debug.set_start_triangle(start_triangle)
            debug.set_start_point(start_point)
            debug.set_end_triangle(end_triangle)
            debug.set_end_point(end_point)

        while True:
            try:
                tri_path = next(finder)
            except StopIteration:
                return None

            sp = StringPuller(
                start_point,
                tri_path,
                end_point,
                radius,
                footprint_radius,
                self._point_normal,
                self._point_max_radius,
                self._edge_max_radius,
                squeeze,
                debug
            )
            try:
                return sp.calculate()
            except StringPuller.Squeezed as squeezed:
                finder.ignore_node(squeezed.triangle)
                continue


class StringPuller(Generic[T]):

    class _PointSqueezed(BaseException):
        pass

    class Squeezed(BaseException):
        def __init__(self, triangle: Triangle3d[T]):
            super().__init__()
            self.triangle = triangle

    def __init__(
        self,
        start_point: T,
        triangle_path: tuple[Triangle3d[T], ...],
        end_point: T,
        radius: float,
        footprint_radius: float,
        point_normal: dict[T, T],
        point_max_radius: dict[T, float],
        edge_max_radius: dict[tuple[T, T], tuple[float, float]],
        squeeze: bool,
        debug: Debug | None
    ):
        print("-----------------------------------")
        self.start_point = start_point
        self.end_point = end_point
        self.radius = radius
        self.footprint_radius = footprint_radius
        self.point_normal = point_normal
        self.point_max_radius = point_max_radius
        self.edge_max_radius = edge_max_radius
        self.squeeze = squeeze
        self.debug = debug
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
            self.last_normal = triangle_path[0].normal
            self.path_iter = iter(enumerate(triangle_path[1:]))

    def calculate(self) -> tuple[T, ...]:
        assert self.path_iter is not None
        try:
            while True:
                self._calculate_inner()
        except StopIteration:
            pass
        self.path_iter = None

        self._add_to_path(
            self.end_point,
            self.radius,
            normal=type(self.end_point)(0)
        )

        if self.debug:
            for tri in self.triangle_path:
                self.debug.add_path_tri(tri)
            for point in self.path:
                self.debug.add_path_point(point)

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
            try:
                self._add_to_path(funnel_target, self.radius)
            except self._PointSqueezed:
                raise self.Squeezed(triangle)
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
                try:
                    self._add_to_path(target, self.radius)
                except self._PointSqueezed:
                    raise self.Squeezed(triangle)
                self.apex = target
            setattr(self, line_target_name, next_point)

    def _get_funnel_area(self, left: T, right: T) -> None:
        return ((left - self.apex).cross(right - self.apex)).y

    def _add_to_path(
        self,
        point: T,
        radius: float,
        *,
        normal: T | None = None
    ) -> None:
        # the triangle buffer will contain all tris within the funnel area,
        # including any that share the point
        #
        # normally this is fine, but because we offset the position of the
        # point by the radius it can cause undesirable behaviors where one of
        # the tris is part of a future path and has a different normal than
        # what would visually be apparent from the offset position
        #
        # so we only include the first tri that includes the point, the next
        # point can deal with the remaining tris
        for i, tri in enumerate(self.triangle_buffer):
            if point in tri.positions:
                break
        triangles = self.triangle_buffer[:i + 1]
        self.triangle_buffer = self.triangle_buffer[i + 1:]

        if radius != 0:
            if normal is None:
                normal = self.point_normal[point]
            # eliminate normals that are very close to 0, since they probably
            # are theoretically zero, but floating point inaccuracy doesn't
            # represent them as such
            if sum(abs(normal)) > 0.0001:
                max_radius = self.point_max_radius[point]
                if radius > max_radius:
                    if self.squeeze:
                        radius = max_radius
                    else:
                        raise self._PointSqueezed()
                offset = normal * radius
                point += offset

        path_line = LineSegment2d(self.path[-1].xz, point.xz)
        if triangles:
            for triangle in triangles:
                # we can skip tris that have the same normal since any
                # intersections would produce redundant points that don't
                # actually alter the path
                if triangle.normal == self.last_normal:
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
                        for edge in get_triangle_edges(triangle)
                    )
                    if intersection is not None
                    if intersection[0] > 1e-6
                ]
                intersections.sort(key=lambda i: i[0][0])
                for (path_time, edge_time), edge in intersections:
                    edge_3d = LineSegment3d(*edge)
                    new_point = edge_3d.get_point_from_a_to_b(edge_time)

                    try:
                        max_radius_a, max_radius_b = self.edge_max_radius[edge]
                    except KeyError:
                        max_radius_a = max_radius_b = 0
                    if radius > max_radius_a or radius > max_radius_b:
                        if not self.squeeze:
                            raise self.Squeezed(triangle)

                    a_distance = new_point.xz.distance(edge[0].xz) + radius
                    b_distance = new_point.xz.distance(edge[1].xz) + radius
                    if a_distance > max_radius_a:
                        if b_distance > max_radius_b:
                            new_point = edge_3d.get_point_from_a_to_b(.5)
                        else:
                            new_point = edge_3d.get_point_from_a_to_b(max_radius_a)
                    elif b_distance > max_radius_b:
                        new_point = edge_3d.get_point_from_a_to_b(1 - max_radius_b)

                    if self.path[-1] != new_point:
                        self.path.append(new_point)
                    self.last_normal = triangle.normal
                    # only the first intersection matters since any others
                    # would be along the same triangle normal
                    break
                path_line = LineSegment2d(self.path[-1].xz, point.xz)

        if self.path[-1] != point:
            self.path.append(point)
            if triangles:
                self.last_normal = triangles[-1].normal


class Debug(Generic[T]):

    def __init__(
        self,
        navmesh: NavigationMesh3d[T],
        *,
        normal_magnitude: float = 1.0
    ) -> None:
        self._navmesh = navmesh
        self._shader = Shader(
            vertex=self._VERTEX_SHADER,
            fragment=self._FRAGMENT_SHADER
        )
        self.set_start_triangle(None)
        self.set_start_point(None)
        self.set_end_triangle(None)
        self.set_end_point(None)
        self.clear_path_tris()
        self.clear_path_points()

        self.refresh(normal_magnitude=normal_magnitude)

    def refresh(self, *, normal_magnitude: float = 1.0) -> None:
        self._navmesh._recalculate_point_max_radius()
        self._navmesh._recalculate_edge_max_radius()

        self._tris = BufferViewMap({
            "pos": BufferView.from_array(FVector3Array(*(
                tri.positions[i]
                for tri in self._navmesh.triangles
                for i in [0, 1, 1, 2, 2, 0]
            )))
        })
        self._walls = BufferViewMap({
            "pos": BufferView.from_array(FVector3Array(*(
                point
                for wall in self._navmesh.walls
                for point in wall
            )))
        })
        self._point_normals = BufferViewMap({
            "pos": BufferView.from_array(FVector3Array(*(
                point + (self._navmesh._get_point_normal(point) * magnitude)
                for point in self._navmesh._point_triangle
                for magnitude in (
                    0,
                    normal_magnitude * self._navmesh._point_max_radius[point]
                )
            )))
        })

    def set_start_point(self, point: T | None) -> None:
        if point is None:
            self._start_point = None
            return
        self._start_point = BufferViewMap({
            "pos": BufferView.from_array(FVector3Array(point))
        })

    def set_end_point(self, point: T | None) -> None:
        if point is None:
            self._end_point = None
            return
        self._end_point = BufferViewMap({
            "pos": BufferView.from_array(FVector3Array(point))
        })

    def set_start_triangle(self, tri: Triangle3d[T] | None) -> None:
        if tri is None:
            self._start_triangle = None
            return
        self._start_triangle = BufferViewMap({
            "pos": BufferView.from_array(FVector3Array(*tri.positions))
        })

    def set_end_triangle(self, tri: Triangle3d[T] | None) -> None:
        if tri is None:
            self._end_triangle = None
            return
        self._end_triangle = BufferViewMap({
            "pos": BufferView.from_array(FVector3Array(*tri.positions))
        })

    def add_path_tri(self, tri: Triangle3d[T]) -> None:
        self._raw_path_tris.append(tri)

    def clear_path_tris(self) -> None:
        self._raw_path_tris = []
        self._path_tris = None

    def add_path_point(self, point: T) -> None:
        self._raw_path_points.append(point)

    def clear_path_points(self) -> None:
        self._raw_path_points = []
        self._path_points = None

    def draw(
        self,
        render_target: TextureRenderTarget | WindowRenderTarget,
        view_projection_transform: FMatrix4,
    ) -> None:
        execute_shader(
            render_target,
            self._shader,
            PrimitiveMode.LINE,
            self._walls,
            {
                "camera_transform": view_projection_transform,
                "color": FVector3(0, 1, 1),
            },
            index_range=(0, len(self._walls["pos"])),
            depth_write=True,
            depth_test=DepthTest.LESS,
        )
        execute_shader(
            render_target,
            self._shader,
            PrimitiveMode.LINE,
            self._point_normals,
            {
                "camera_transform": view_projection_transform,
                "color": FVector3(1, 0, 1),
            },
            index_range=(0, len(self._point_normals["pos"])),
            depth_write=True,
            depth_test=DepthTest.LESS,
        )
        """
        execute_shader(
            render_target,
            self._shader,
            PrimitiveMode.LINE,
            self._tris,
            {
                "camera_transform": view_projection_transform,
                "color": FVector3(1, 1, 1),
            },
            index_range=(0, len(self._tris["pos"])),
            depth_write=True,
            depth_test=DepthTest.LESS,
        )
        """
        if self._start_point:
            execute_shader(
                render_target,
                self._shader,
                PrimitiveMode.POINT,
                self._start_point,
                {
                    "camera_transform": view_projection_transform,
                    "color": FVector3(0, 1, 0),
                },
                index_range=(0, len(self._start_point["pos"])),
                depth_write=True,
                depth_test=DepthTest.LESS,
            )
        if self._end_point:
            execute_shader(
                render_target,
                self._shader,
                PrimitiveMode.POINT,
                self._end_point,
                {
                    "camera_transform": view_projection_transform,
                    "color": FVector3(1, 0, 0),
                },
                index_range=(0, len(self._end_point["pos"])),
                depth_write=True,
                depth_test=DepthTest.LESS,
            )
        if self._start_triangle:
            execute_shader(
                render_target,
                self._shader,
                PrimitiveMode.TRIANGLE,
                self._start_triangle,
                {
                    "camera_transform": view_projection_transform,
                    "color": FVector3(0, .5, 0),
                },
                index_range=(0, len(self._start_triangle["pos"])),
                depth_write=True,
                depth_test=DepthTest.LESS,
            )
        if self._end_triangle:
            execute_shader(
                render_target,
                self._shader,
                PrimitiveMode.TRIANGLE,
                self._end_triangle,
                {
                    "camera_transform": view_projection_transform,
                    "color": FVector3(.5, 0, 0),
                },
                index_range=(0, len(self._end_triangle["pos"])),
                depth_write=True,
                depth_test=DepthTest.LESS,
            )
        if self._raw_path_points:
            if self._path_points is None:
                self._path_points = BufferViewMap({
                    "pos": BufferView.from_array(FVector3Array(*
                        self._raw_path_points
                    ))
                })
            execute_shader(
                render_target,
                self._shader,
                PrimitiveMode.POINT,
                self._path_points,
                {
                    "camera_transform": view_projection_transform,
                    "color": FVector3(1, 1, 0),
                },
                index_range=(0, len(self._path_points["pos"])),
                depth_write=True,
                depth_test=DepthTest.LESS,
            )
            execute_shader(
                render_target,
                self._shader,
                PrimitiveMode.LINE_STRIP,
                self._path_points,
                {
                    "camera_transform": view_projection_transform,
                    "color": FVector3(1, 1, 0),
                },
                index_range=(0, len(self._path_points["pos"])),
                depth_write=True,
                depth_test=DepthTest.LESS,
            )
        if self._raw_path_tris:
            if self._path_tris is None:
                self._path_tris = BufferViewMap({
                    "pos": BufferView.from_array(FVector3Array(*(
                        vert
                        for tri in self._raw_path_tris
                        for vert in tri.positions
                    )))
                })
            execute_shader(
                render_target,
                self._shader,
                PrimitiveMode.TRIANGLE,
                self._path_tris,
                {
                    "camera_transform": view_projection_transform,
                    "color": FVector3(.5, .5, 0),
                },
                index_range=(0, len(self._path_tris["pos"])),
                depth_write=True,
                depth_test=DepthTest.LESS,
            )

    _VERTEX_SHADER: Final = b"""
        #version 140
        in vec3 pos;
        uniform mat4 camera_transform;
        void main()
        {
            gl_Position = camera_transform * vec4(pos, 1.0);
        }
    """

    _FRAGMENT_SHADER: Final = b"""
        #version 140
        uniform vec3 color;
        out vec4 output_color;

        void main()
        {
            output_color = vec4(color, 1);
        }
    """
