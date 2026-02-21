from geometry_tools.lib.point import Point2D, PointList, lexicographical_sort


class Polygon:
    def __init__(self, vertices: PointList | list[Point2D]):
        if isinstance(vertices, PointList):
            self.vertices = vertices.points
        elif isinstance(vertices, list) and all(
            isinstance(v, Point2D) for v in vertices
        ):
            self.vertices = lexicographical_sort(vertices)
        else:
            raise ValueError("Unsupported vertices type for Polygon initialization.")
