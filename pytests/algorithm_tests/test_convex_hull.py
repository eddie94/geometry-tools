from geometry_tools.algorithms.convex_hull import convex_hull, PointList


class TestConvexHull:
    def test_convex_hull(self):
        points = PointList(
            [
                (0, 0),
                (3, -2),
                (-1, 1),
                (4, 1),
                (-3, -2),
                (0, -2),
                (1, 4),
                (1, 1),
                (-2, 3),
                (2, 0),
            ]
        )

        convex_hull_polygon = convex_hull(points=points)

        assert convex_hull_polygon == [
            (-3, -2),
            (3, -2),
            (4, 1),
            (1, 4),
            (-2, 3),
        ]
