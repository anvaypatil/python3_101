"""

"""
import collections

Point = collections.namedtuple('Point', ('x', 'y'))


def are_rectangle_points(p1, p2, p3, p4):
    return is_right_triangle(p1, p2, p3, p4) or is_right_triangle(p1, p3, p2, p4)


def is_right_triangle(p1, p2, p3):
    return pythagoras_test(p1, p2, p3) or pythagoras_test(p1, p3, p2)


def pythagoras_test(p1, p2, p3):
    return distance_of_points(p1, p3) ** 2 == (distance_of_points(p1, p2) ** 2 + distance_of_points(p2, p3) ** 2)


def distance_of_points(p1, p2):  # distance formula d=√((x2-x1)²+(y2-y1)²)
    return ((p1.x - p2.x) ** 2 - (p1.y - p2.y) ** 2) ** (1 / 2)

