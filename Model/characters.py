from .physics import *
import pygame


class Sprite(pygame.sprite.Sprite):
    def __init__(self, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()


class Character:
    def __init__(self, pos, filename, length, width):
        self.__pos = pos
        self.speed = 5
        self.sprite = Sprite(filename)
        self.collider = pygame.Rect((self.__pos.x, self.__pos.y, length, width))

    @property
    def Pos(self):
        return self.__pos

    def move(self, direction):
        new_pos = Vector2D.scalar_multiple(self.speed, direction.get_normalized())
        self.__pos = Vector2D.sum(self.__pos, new_pos)
        self.collider.move_ip(new_pos.x, new_pos.y)


class Bullet:
    def __init__(self, pos, dir):
        self.__pos = pos
        self.speed = 3
        self.collider = pygame.Rect((self.__pos.x, self.__pos.y, 5, 5))
        self.direction = dir

    @property
    def Pos(self):
        return self.__pos

    def move(self):
        new_pos = Vector2D.scalar_multiple(self.speed, self.direction.get_normalized())
        self.__pos = Vector2D.sum(self.__pos, new_pos)
        self.collider.move_ip(new_pos.x, new_pos.y)