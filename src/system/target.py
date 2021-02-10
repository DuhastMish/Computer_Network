from src.geometry import Point3d
from src.system.mirror import Mirror
from typing import Tuple
from math import sqrt


class Target:
    def __init__(self, init_coords: Point3d, radius: float):
        self.location: Point3d = init_coords
        self.radius = radius


class MirrorTarget:
    def __init__(self, mirror: Mirror):
        self.mirror = mirror
        # Init points and their coordinates.
        point_a, point_b, point_c = mirror.triangle.get_points()
        side_ab = self.calculate_side_length(point_b, point_c)
        side_bc = self.calculate_side_length(point_a, point_c)
        side_ca = self.calculate_side_length(point_a, point_b)
        self.inradius = self.get_inradius(side_ab, side_bc, side_ca)

    def calculate_side_length(self, point_1: Tuple, point_2: Tuple):
        p1_x, p1_y, p1_z = point_1
        p2_x, p2_y, p2_z = point_2
        side_length = sqrt((p1_x - p2_x)**2 + (p1_y - p2_y)**2 + (p1_z - p2_z)**2)
        return side_length

    def get_semiperimeter(self, side_1: float, side_2: float, side_3: float) -> float:
        return (side_1 + side_2 + side_3) / 2

    def get_triangle_area(self, side_1: float, side_2: float, side_3: float) -> float:
        semiperimeter = self.get_semiperimeter(side_1, side_2, side_3)
        return sqrt(semiperimeter * (semiperimeter - side_1) * (semiperimeter - side_2) * (semiperimeter - side_3))

    def get_inradius(self, side_1: float, side_2: float, side_3: float):
        semiperimeter = self.get_semiperimeter(side_1, side_2, side_3)
        area = self.get_triangle_area(side_1, side_2, side_3)
        return area / semiperimeter
