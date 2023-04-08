import pygame as pg
from random import choice, randint

list_color = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 0, 247), (255, 255, 0), (0, 255, 255)]


class CheckMove:
    def __init__(self):
        self.cord_x = 100
        self.cord_y = 0
        self.size = 10
        self.speed = 10

        self.dist = 4

        self.color = choice(list_color)

        self.move = True

    def moving(self, size:tuple, edge:tuple):
        if size[1]-self.speed > edge[1] + self.size + 10 and self.move:
            self.cord_y += self.speed

    def move_left(self, edge:tuple):
        if edge[0] > 10 and self.move:
            return True
        return False

    def move_right(self, size:tuple, edge:tuple):
        if edge[0] + 2*self.speed + 10 < size[0] and self.move:
            return True
        return False


class Square(CheckMove):
    def __init__(self):
        super().__init__()
        self.edge = (self.cord_x, self.cord_y)
        self.edge_left = (self.cord_x, self.cord_y)
        self.edge_right = (self.cord_x, self.cord_y)

    def draw(self, window):
        self.edge = (self.cord_x, self.cord_y)
        self.edge_left = (self.cord_x, self.cord_y)
        self.edge_right = (self.cord_x, self.cord_y)

        color = self.color
        pg.draw.rect(window, color, (self.cord_x, self.cord_y, self.size, self.size))
        pg.draw.rect(window, color, (self.cord_x + self.speed + self.dist, self.cord_y, self.size, self.size))
        pg.draw.rect(window, color, (self.cord_x, self.cord_y + self.speed + self.dist, self.size, self.size))
        pg.draw.rect(window, color, (self.cord_x + self.speed + self.dist, self.cord_y + self.speed + self.dist, self.size, self.size))


class Direct(CheckMove):
    def __init__(self):
        super().__init__()
        self.pos = randint(0, 1)
        self.edge = (0, 0)
        self.edge_right = (0, 0)
        self.edge_left = (0, 0)

    def draw(self, window):
        color = self.color
        # рисовать горизонтально
        if self.pos == 0:
            self.edge_left = (self.cord_x, self.cord_y)
            self.edge_right = (self.cord_x + self.dist*3 + self.size*3, self.cord_y)
            self.edge = self.edge_right
            for i in range(4):
                pg.draw.rect(window, color, (self.cord_x + self.dist*i + self.size*i,
                                             self.cord_y,
                                             self.size,
                                             self.size))
        else:
            # рисовать вертикально
            self.edge_left = (self.cord_x, self.cord_y)
            self.edge_right = (self.cord_x, self.cord_y)
            self.edge = (self.cord_x, self.cord_y + self.dist * 3 + self.size * 3)
            for i in range(4):
                pg.draw.rect(window, color, (self.cord_x,
                                             self.cord_y + self.dist * i + self.size * i,
                                             self.size,
                                             self.size))

