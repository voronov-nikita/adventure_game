import pygame as pg

from Hero import MainHero
from Scenes import MainGame, OpenGame

pg.init()


class OpenSpace:
    def __init__(self):
        self.background_colour = (0, 0, 0)
        self.width = 500
        self.height = 500
        self.screen = pg.display.set_mode((self.width, self.height))
        self.FPS = 30
        self.clock = pg.time.Clock()
        self.work = True


place = OpenSpace()
hero = MainHero()

pg.display.set_caption("Adventure")
pg.display.set_icon(place.screen)

current_scene = "main"

while place.work:
    place.clock.tick(place.FPS)

    # проверка на закрытие экрана
    for event in pg.event.get():
        if event.type == pg.QUIT:
            place.work = False

    if current_scene == "game":
        MainGame(hero, place)

    if current_scene == "main":
        OpenGame(current_scene, place)

pg.quit()
