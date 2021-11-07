import math
class Sphere:

    def __init__(self, x, y, z, rad):
        self.x = x
        self.y = y
        self.z = z
        self.rad = rad

    def get_volume(self):
        return 4/3 * (pow(self.rad, 3)) * math.pi

    def get_square_(self):
        return 4 * pow(self.rad, 2) * math.pi

    def get_radius_(self):
        return self.rad

    def get_center_(self):
        a = (self.x, self.y, self.z)
        return a

    def set_radius_(self, r : float):
        self.rad = r

    def set_center(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def is_point_inside(self, x, y, z):
        if math.sqrt(pow((x - self.x),2) + pow((y - self.y),2) + pow((z - self.z),2)) > self.rad:
            return False
        else:
            return True

