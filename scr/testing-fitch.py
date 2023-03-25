import pygame

pygame.init()

# установка окна
win_width = 500
win_height = 500
win = pygame.display.set_mode((win_width, win_height))

# создание кнопки
button_font = pygame.font.SysFont('Calibri', 30)
button_text = button_font.render('Go to next scene', True, (255, 255, 255))
button_rect = button_text.get_rect(center=(win_width//2, win_height//2))

# установка начальной сцены
current_scene = 'main'

# бесконечный цикл
while True:

    # получение информации о событиях в окне pygame
    for event in pygame.event.get():

        # проверка, является ли событие нажатием кнопки мыши
        if event.type == pygame.MOUSEBUTTONDOWN:

            # проверка, находится ли курсор на кнопке
            if button_rect.collidepoint(event.pos):

                # переход на следующую сцену
                current_scene = 'next'

        # проверка, является ли событие выходом из программы
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # отрисовка текущей сцены
    if current_scene == 'main':
        win.fill((0, 0, 0))
        pygame.draw.circle(win, (255, 255, 255), (win_width//2, win_height//2), 20)
        win.blit(button_text, button_rect)

    # переход на следующую сцену
    elif current_scene == 'next':
        win.fill((255, 0, 0))
        pygame.draw.rect(win, (255, 255, 255), (50, 50, win_width-100, win_height-100))
        pygame.display.update()

    pygame.display.update()

pygame.quit()
