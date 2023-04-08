import pygame as pg
from random import choice, randint

list_color = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 0, 247), (255, 255, 0), (0, 255, 255)]


class Square:
    def __init__(self):
        self.cord_x = 100
        self.cord_y = 0
        self.size = 10
        self.speed = 10

        self.dist = 4

        self.color = choice(list_color)

        self.move = True

    def draw_square(self, window):
        color = self.color
        pg.draw.rect(window, color, (self.cord_x, self.cord_y, self.size, self.size))
        pg.draw.rect(window, color, (self.cord_x + self.speed + self.dist, self.cord_y, self.size, self.size))
        pg.draw.rect(window, color, (self.cord_x, self.cord_y + self.speed + self.dist, self.size, self.size))
        pg.draw.rect(window, color, (self.cord_x + self.speed + self.dist, self.cord_y + self.speed + self.dist, self.size, self.size))

    def moving(self, size:tuple):
        if size[1]-self.speed > self.cord_y + self.size + 10 and self.move:
            self.cord_y += self.speed

    def move_left(self, size:tuple):
        if self.cord_x > 10 and self.move:
            return True
        return False

    def move_right(self, size:tuple):
        if self.cord_x + 2*self.speed + 10 < size[0] and self.move:
            return True
        return False


