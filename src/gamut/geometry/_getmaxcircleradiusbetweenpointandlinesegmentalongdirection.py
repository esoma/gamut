__all__ = [
    'get_max_circle_radius_between_point_and_line_segment_along_direction'
]

# gamut
from gamut.geometry import LineSegment2d
from gamut.math import DVector2, FVector2
# python
from math import inf
from typing import TypeVar

V = TypeVar('V', DVector2, FVector2)


def get_max_circle_radius_between_point_and_line_segment_along_direction(
    point: V,
    line_segment: LineSegment2d[V],
    direction: V
) -> float:
    if not isinstance(point, (DVector2, FVector2)):
        raise TypeError('point must be FVector2 or DVector2')
    if not isinstance(line_segment, LineSegment2d):
        raise TypeError('line segment must be LineSegment2d')
    if not isinstance(line_segment.a, type(point)):
        raise TypeError(
            f'line segment must be composed of {type(point).__name__}'
        )
    if not isinstance(direction, type(point)):
        raise TypeError(f'direction must be {type(point).__name__}')

    line_slope = line_segment.slope
    ray_slope = direction.normalize()
    distance = line_segment.get_distance_to_point(point)

    det = -line_slope.x * ray_slope.y + ray_slope.x * line_slope.y
    if det != 0:
        t = (
            (line_slope.x * (point.y - line_segment.a.y) -
            line_slope.y * (point.x - line_segment.a.x)) /
            det
        )
        if t < 0:
            return inf

    c = line_slope.normalize().xoy.cross(ray_slope.xoy).y
    c = 1 + abs(c)
    distance = distance / c
    return distance
