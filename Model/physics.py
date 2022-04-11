import math
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_module(self):
        return math.sqrt(self.x*self.x+self.y*self.y)

    def get_normalized(self):
        if self.get_module() != 0:
            return Vector2D(self.x/self.get_module(), self.y/self.get_module())
        else:
            return Vector2D(0, 0)

    @staticmethod
    def sum(v1, v2):
        return Vector2D(v1.x + v2.x, v1.y + v2.y)

    @staticmethod
    def dif(v1, v2):
        return Vector2D(v1.x - v2.x, v1.y - v2.y)

    @staticmethod
    def scalar_multiple(n, v):
        return Vector2D(n*v.x, n*v.y)
