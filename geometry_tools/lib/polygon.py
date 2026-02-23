from typing import Iterable

from geometry_tools.lib.point import PointList


class Polygon:
    def __init__(self, vertices: PointList | Iterable[int | float]):
        if isinstance(vertices, PointList):
            self.vertices = vertices.points
        else:
            self.vertices = PointList(vertices)

    def __eq__(self, value: object) -> bool:
        try:
            for vertex, target_vertex in zip(self.vertices, value):
                if vertex != target_vertex:
                    return False
            return True
        except Exception:
            return False

    def __repr__(self):
        repr_str = [p for p in self.vertices]
        return f"Polygon(vertices={repr_str})"
