import pygame as pg


class MainHero():
    def __init__(self):

        self.cord_x = 0
        self.cord_y = 0
        self.hero_size = 10
        self.color = (255, 255, 102)

        self.surface = pg.Surface((self.hero_size, self.hero_size))
        self.rect = self.surface.get_rect()

        self.speed = 10

    def drawing_hero(self, place):
        position = (self.cord_x, self.cord_y, self.hero_size, self.hero_size)

        pg.draw.rect(place, self.color, position)
        self.surface.fill(self.color)
        self.rect.x = self.cord_x
        self.rect.y = self.cord_y
        place.blit(self.surface, self.rect)

