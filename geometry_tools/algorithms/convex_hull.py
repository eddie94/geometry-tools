from geometry_tools.lib.point import (
    Point2D,
    PointList,
    cross_product,
    lexicographical_sort,
)
from geometry_tools.lib.polygon import Polygon


def _get_half_convex_hull(points: list[Point2D]) -> list[Point2D]:
    initial_hull = [points[0], points[1]]
    for point in points[2:]:
        while (
            len(initial_hull) >= 2
            and cross_product(
                initial_hull[-1],
                point,
                origin=initial_hull[-2],
            )
            <= 0
        ):
            initial_hull.pop()
        initial_hull.append(point)
    return initial_hull


def convex_hull(points: list[Point2D] | PointList) -> Polygon:
    if isinstance(points, PointList):
        points = lexicographical_sort(points)
    elif isinstance(points, (list, tuple)) and all(
        isinstance(p, Point2D) for p in points
    ):
        points = lexicographical_sort(points)
    else:
        raise ValueError("Input must be a list of Point2D or a PointList.")

    upper_hull = _get_half_convex_hull(points=points)
    points.reverse()

    lower_hull = _get_half_convex_hull(points=points)
    lower_hull.pop()

    convex_hull = upper_hull + lower_hull

    return Polygon(convex_hull)
