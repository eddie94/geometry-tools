class Point2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point2D(x={self.x}, y={self.y})"


class Point3D:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"Point3D(x={self.x}, y={self.y}, z={self.z})"


class PointList:
    def __init__(self, points: list[Point2D | Point3D]):
        self.points = points

    def __str__(self):
        return f"PointList(points={self.points})"
    
    def sort_by_x(self):
        self.points.sort(key=lambda p: p.x if isinstance(p, (Point2D, Point3D)) else p.coordinates[0])
    
    def sort_by_y(self):
        self.points.sort(key=lambda p: p.y if isinstance(p, (Point2D, Point3D)) else p.coordinates[1])
    
    def lexicographical_sort(self):
        self.points.sort(key=lambda p: (p.x, p.y) if isinstance(p, (Point2D, Point3D)) else tuple(p.coordinates))


class PointDict:
    def __init__(self, points: dict[str, Point2D | Point3D]):
        self.points = points

    def __str__(self):
        return f"PointDict(points={self.points})"
