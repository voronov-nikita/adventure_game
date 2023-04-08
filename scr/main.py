import pygame as pg
import sys

from Objects import Square

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


def check_click_button(hero, size_window):
    keys_button = pg.key.get_pressed()

    if keys_button[pg.K_LEFT] and hero.move_left(size_window):
        hero.cord_x -= hero.speed

    if keys_button[pg.K_RIGHT] and hero.move_right(size_window):
        hero.cord_x += hero.speed

    if keys_button[pg.K_DOWN]:
        hero.cord_y += hero.speed


screen = Screen()
hero = Square()

while screen.game:
    screen.clock.tick(screen.FPS)

    # проверяем нажатие на закрытие экрана
    for event in pg.event.get():
        if event.type == pg.QUIT:
            screen.game = False

    check_click_button(hero, screen.size_window)
    hero.moving(screen.size_window)

    # <----------- Обработаем здесь все изображения ----------->
    screen.screen.fill(screen.background_colour)
    hero.draw_square(screen.screen)
    pg.display.update()

pg.quit()
