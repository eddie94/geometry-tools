from collections.abc import Iterable
from typing import Optional


class Point2D:
    def __init__(self, *args: Iterable[float | int | Iterable[float | int]]):
        if len(args) > 2:
            raise ValueError(
                "point2D initialization must be an iterable object with length 2 , or 2 individual numbers"
            )
        if len(args) == 1:
            # iterable object type
            self.x = args[0][0]
            self.y = args[0][1]
        else:
            self.x = args[0]
            self.y = args[1]

    def __str__(self):
        return f"Point2D(x={self.x}, y={self.y})"

    def __eq__(self, value: object) -> bool:
        """Check equality between this point and another point or list.

        Args:
            value: Either a Point2D object or a list of two numeric values [x, y].

        Returns:
            True if the coordinates match, False otherwise.

        Example:
            >>> p1 = Point2D(1.0, 2.0)
            >>> p2 = Point2D(1.0, 2.0)
            >>> p1 == p2
            True
            >>> p1 == [1.0, 2.0]
            True
        """
        if self is value:
            return True
        if isinstance(value, Point2D):
            return self.x == value.x and self.y == value.y
        elif isinstance(value, (list, tuple)) and len(value) == 2:
            return self.x == value[0] and self.y == value[1]
        return False

    def __sub__(self, other: object) -> "Point2D":
        """Subtract another point from this point, returning a new point.

        Args:
            other: A Point2D object to subtract.

        Returns:
            A new Point2D representing the vector difference.

        Raises:
            ValueError: If other is not a Point2D instance.

        Example:
            >>> p1 = Point2D(5.0, 3.0)
            >>> p2 = Point2D(2.0, 1.0)
            >>> p1 - p2
            Point2D(x=3.0, y=2.0)
        """
        if not isinstance(other, Point2D):
            raise ValueError(
                "Subtraction is only supported between Point2D or 2D tuple, list instances."
            )
        return Point2D(self.x - other.x, self.y - other.y)

    def __add__(self, other: object) -> "Point2D":
        """Add another point to this point, returning a new point.

        Args:
            other: A Point2D object to add.

        Returns:
            A new Point2D representing the vector sum.

        Raises:
            ValueError: If other is not a Point2D instance.

        Example:
            >>> p1 = Point2D(5.0, 3.0)
            >>> p2 = Point2D(2.0, 1.0)
            >>> p1 + p2
            Point2D(x=7.0, y=4.0)
        """
        if not isinstance(other, Point2D):
            raise ValueError(
                "Addition is only supported between Point2D or 2D tuple, list instances."
            )
        return Point2D(self.x + other.x, self.y + other.y)


class Point3D:
    def __init__(self, *args: Iterable[float | int | Iterable[float | int]]):
        if len(args) > 2 or len(args) == 2:
            raise ValueError(
                "point2D initialization must be an iterable object with length 3 , or 3 individual numbers"
            )
        if len(args) == 1:
            self.x = args[0][0]
            self.y = args[0][1]
            self.z = args[0][2]
        else:
            self.x = args[0]
            self.y = args[1]
            self.z = args[2]

    def __str__(self):
        return f"Point3D(x={self.x}, y={self.y}, z={self.z})"

    def __eq__(self, value: object) -> bool:
        if self is value:
            return True
        if isinstance(value, Point3D):
            return self.x == value.x and self.y == value.y and self.z == value.z
        elif isinstance(value, (list, tuple)) and len(value) == 3:
            return self.x == value[0] and self.y == value[1] and self.z == value[2]
        return False


class PointList:
    def __init__(self, points: Iterable[object]):
        if _assert_point_type_in_list(points):
            self.points = self.convert_to_point(points=points)
        else:
            raise ValueError(
                "PointList must be initialized with a list of data which can be converted toPoint2D or Point3D objects."
            )

    def convert_to_point(self, points):
        if len(points[0]) == 2:
            return [Point2D(point) for point in points]
        elif len(points[0]) == 3:
            return [Point3D(point) for point in points]
        else:
            raise ValueError("point length must be 2 or 3")

    def __getitem__(self, idx):
        return self.points[idx]


def _assert_point_convertable(point: object) -> bool:
    if isinstance(point, Point2D) or isinstance(point, Point3D):
        return True
    elif (
        isinstance(point, (list, tuple))
        and len(point) == 2
        and all(isinstance(coord, (int, float)) for coord in point)
    ):
        # point2d cases
        return True
    elif (
        isinstance(point, (list, tuple))
        and len(point) == 3
        and all(isinstance(coord, (int, float)) for coord in point)
    ):
        # point3d cases
        return True
    else:
        return False


def _assert_point_type_in_list(point_list: Iterable[object]) -> bool:
    if isinstance(point_list, Iterable) and all(
        _assert_point_convertable(p) for p in point_list
    ):
        return True
    else:
        return False


def lexicographical_sort(points: list[Point2D | Point3D]) -> list[Point2D | Point3D]:
    """Sort a list of points in lexicographical order.

    For Point2D objects, sorts by (x, y) coordinates.
    For Point3D objects, sorts by (x, y, z) coordinates.

    Args:
        points: A list of Point2D or Point3D objects to be sorted.

    Returns:
        A new list containing the same points sorted in lexicographical order.

    Raises:
        ValueError: If the first element in the list is not a Point2D or Point3D object.

    Example:
        >>> p1 = Point2D(3, 2)
        >>> p2 = Point2D(1, 4)
        >>> p3 = Point2D(1, 2)
        >>> sorted_points = lexicographical_sort([p1, p2, p3])
        >>> # Result: [p3, p2, p1] (sorted by x first, then y)
    """
    if isinstance(points[0], Point2D):
        return sorted(points, key=lambda p: (p.x, p.y))
    elif isinstance(points[0], Point3D):
        return sorted(points, key=lambda p: (p.x, p.y, p.z))
    else:
        raise ValueError(
            f"Type {type(points[0])} is unsupported point type for lexicographical sorting."
        )


def cross_product(
    p1: Point2D | Point3D,
    p2: Point2D | Point3D,
    origin: Optional[Point2D | Point3D] = None,
) -> float | Point3D:
    if type(p1) is not type(p2) and (origin is None or type(origin) is not type(p1)):
        raise ValueError(
            "Both points and th origin point must be of the same type for cross product."
        )
    if isinstance(p1, Point2D):
        if origin is None:
            origin = Point2D(0, 0)
        return (p1.x - origin.x) * (p2.y - origin.y) - (p1.y - origin.y) * (
            p2.x - origin.x
        )
    elif isinstance(p1, Point3D):
        if origin is None:
            origin = Point3D(0, 0, 0)
        x = (p1.y - origin.y) * (p2.z - origin.z) - (p1.z - origin.z) * (
            p2.y - origin.y
        )
        y = (p1.z - origin.z) * (p2.x - origin.x) - (p1.x - origin.x) * (
            p2.z - origin.z
        )
        z = (p1.x - origin.x) * (p2.y - origin.y) - (p1.y - origin.y) * (
            p2.x - origin.x
        )
        return Point3D(x, y, z)
    else:
        raise ValueError(
            f"Unsupported point type {type(p1)} for cross product calculation."
        )


def is_counter_clockwise(
    a: Point2D, b: Point2D, origin: Optional[Point2D] = None
) -> bool:
    if origin is None:
        origin = Point2D(0, 0)
    if type(origin) is not Point2D or type(a) is not Point2D or type(b) is not Point2D:
        raise ValueError("All points must be Point2D for counter-clockwise check.")
    return cross_product(a - origin, b - origin) > 0
