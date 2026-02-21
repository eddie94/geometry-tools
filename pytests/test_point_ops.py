from geometry_tools.lib.point import (
    Point2D,
    Point3D,
    cross_product,
    is_counter_clockwise,
)


class TestPointOperations:
    def test_addition(self):
        p1 = Point2D(1, 2)
        p2 = Point2D(3, 4)
        result = p1 + p2
        assert result == Point2D(4, 6)
        assert result == (4, 6)
        assert result == [4, 6]

    def test_subtraction(self):
        p1 = Point2D(5, 7)
        p2 = Point2D(2, 3)
        result = p1 - p2
        assert result == Point2D(3, 4)
        assert result == (3, 4)
        assert result == [3, 4]


class TestCrossProduct:
    def test_cross_product_2d(self):
        p1 = Point2D(2, 0)
        p2 = Point2D(2, 2)
        result = cross_product(p1, p2)

        assert result == 4

    def test_cross_product_3d(self):
        p1 = Point3D(-1, 2, 3)
        p2 = Point3D(0, -1, 1)
        result = cross_product(p1, p2)
        assert result == (5, 1, 1)


class TestIsCounterClockwise:
    def test_is_counter_clockwise(self):
        origin = Point2D(0, 0)
        p2 = Point2D(2, 2)
        p3 = Point2D(4, 0)
        assert not is_counter_clockwise(p2, p3, origin)

    def test_is_not_counter_clockwise(self):
        origin = Point2D(-2, -1)
        p2 = Point2D(1, 3)
        p3 = Point2D(-4, 2)
        assert is_counter_clockwise(p2, p3, origin)
