import pygame as pg

pg.init()


class MainGame:
    def __init__(self, hero, place):
        self.hero = hero

        self.move_object_hero(self.hero.speed)

        #   <------------- Обработать все изображения -------------->
        place.screen.fill(place.background_colour)

        # отрисовка
        hero.drawing_hero(place.screen)

        pg.display.update()

    def move_object_hero(self, speed):

        keys_button = pg.key.get_pressed()

        if keys_button[pg.K_LEFT]:
            self.hero.cord_x -= speed
        if keys_button[pg.K_RIGHT]:
            self.hero.cord_x += speed
        if keys_button[pg.K_UP]:
            self.hero.cord_y -= speed
        if keys_button[pg.K_DOWN]:
            self.hero.cord_y += speed


class OpenGame:
    def __init__(self, current_scene, place):

        self.width_screen = place.width
        self.height_screen = place.height

        self.screen = place.screen

        self.button_font = pg.font.SysFont('Calibri', 30)
        self.button_text = self.button_font.render('Go to next scene', True, (255, 255, 255))
        self.button_rect = self.button_text.get_rect(center=(self.width_screen // 2, self.height_screen // 2))

        self.screen.fill((0, 0, 0))
        pg.draw.circle(self.screen, (255, 255, 255), (self.width_screen // 2, self.height_screen // 2), 20)
        self.screen.blit(self.button_text, self.button_rect)

        self.event_check(current_scene)

        pg.display.update()

    def event_check(self, current_scene):
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                if self.button_rect.collidepoint(event.pos):
                    # переход на следующую сцену
                    current_scene = 'game'
