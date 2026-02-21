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


class PointND:
    def __init__(self, coordinates: list[float]):
        self.coordinates = coordinates

    def __str__(self):
        return f"PointND(coordinates={self.coordinates})"


class PointList:
    def __init__(self, points: list[Point2D | Point3D | PointND]):
        self.points = points

    def __str__(self):
        return f"PointList(points={self.points})"


class PointDict:
    def __init__(self, points: dict[str, Point2D | Point3D | PointND]):
        self.points = points

    def __str__(self):
        return f"PointDict(points={self.points})"
