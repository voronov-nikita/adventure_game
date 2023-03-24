import pygame as pg

from Hero import MainHero

pg.init()


class OpenSpace:
    def __init__(self):
        self.background_colour = (0, 0, 0)
        self.screen = pg.display.set_mode((500, 500))
        self.FPS = 30
        self.clock = pg.time.Clock()
        self.work = True


def move_object_hero(speed):
    keys_button = pg.key.get_pressed()

    if keys_button[pg.K_LEFT]:
        hero.cord_x -= speed
    if keys_button[pg.K_RIGHT]:
        hero.cord_x += speed
    if keys_button[pg.K_UP]:
        hero.cord_y -= speed
    if keys_button[pg.K_DOWN]:
        hero.cord_y += speed


pg.display.set_caption("Adventure")

place = OpenSpace()
hero = MainHero()

while place.work:
    place.clock.tick(place.FPS)

    # проверка на закрытие экрана
    for event in pg.event.get():
        if event.type == pg.QUIT:
            place.work = False

    move_object_hero(hero.speed)

    #   <------------- Обработать все изображения -------------->
    place.screen.fill(place.background_colour)
    # отрисовка
    hero.drawing_hero(place.screen)

    pg.display.update()
pg.quit()
