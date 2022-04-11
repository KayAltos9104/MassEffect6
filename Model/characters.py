from physics import *


class Character:
    def __init__(self, pos):
        self.__pos = pos
        self.speed = 5

    def move(self, direction):
        new_pos = Vector2D.scalar_multiple(self.speed, direction.get_normalized())
        self.__pos += new_pos
