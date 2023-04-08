import pygame as pg
from random import choice
import sys

from Objects import Square, Direct

pg.init()


class Screen:
    def __init__(self):
        self.size_window = (500, 700)
        self.background_colour = (0, 0, 0)

        self.screen = pg.display.set_mode(self.size_window)
        self.FPS = 30
        self.clock = pg.time.Clock()
        self.game = True

        pg.display.set_caption("Adventure")
        # pg.display.set_icon(self.screen)


def check_click_button(hero_elem, size_window):
    keys_button = pg.key.get_pressed()

    if keys_button[pg.K_LEFT] and hero_elem.move_left(hero_elem.edge_left):
        hero_elem.cord_x -= hero_elem.speed

    if keys_button[pg.K_RIGHT] and hero_elem.move_right(size_window, hero_elem.edge_right):
        hero_elem.cord_x += hero_elem.speed

    if keys_button[pg.K_DOWN]:
        hero_elem.cord_y += hero_elem.speed


screen = Screen()
list_objects = [Square(), Direct()]
hero = choice(list_objects)

while screen.game:
    screen.clock.tick(screen.FPS)

    # проверяем нажатие на закрытие экрана
    for event in pg.event.get():
        if event.type == pg.QUIT:
            screen.game = False

    check_click_button(hero, screen.size_window)
    hero.moving(screen.size_window, hero.edge)

    # <----------- Обработаем здесь все изображения ----------->
    screen.screen.fill(screen.background_colour)
    hero.draw(screen.screen)
    pg.display.update()

pg.quit()
