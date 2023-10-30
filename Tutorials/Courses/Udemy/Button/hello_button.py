'''Tutorial about how to create a button in pygame'''
# import os
import pygame
from pygame.locals import * # pylint: disable=wildcard-import, unused-wildcard-import

pygame.init() # pylint: disable=no-member

screen = pygame.display.set_mode((500, 500), 0, 32) # 32 bit buffer depth
pygame.display.set_caption("Hello, Button!")
text_color = (255, 255, 255)
button_color = (0, 0, 170)
button_color_hover = (255, 50, 70)
button_width = 100 # pylint: disable=invalid-name
button_height = 50 # pylint: disable=invalid-name
button_rect = [screen.get_width() / 2 - button_width / 2, screen.get_height() / 2 - \
               button_height / 2, button_width, button_height]
button_font = pygame.font.SysFont("Arial", 20)
button_text = button_font.render("QUIT", True, text_color)
screen.fill((100, 100, 100))

RUNNING = True
clock = pygame.time.Clock()

while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # pylint: disable=no-member
            RUNNING = False
        if event.type == pygame.MOUSEBUTTONDOWN: # pylint: disable=no-member
            x, y = event.pos
            if button_rect[0] <= x <= button_rect[0] + button_rect[2] and \
                button_rect[1] <= y <= button_rect[1] + button_rect[3]:
                RUNNING = False
        if event.type == pygame.MOUSEMOTION: # pylint: disable=no-member
            x, y = event.pos
            if button_rect[0] <= x <= button_rect[0] + button_rect[2] and \
                button_rect[1] <= y <= button_rect[1] + button_rect[3]:
                button_color = button_color_hover
            else:
                button_color = (0, 0, 170)

    pygame.draw.rect(screen, button_color, button_rect)
    screen.blit(button_text, (button_rect[0] + button_width / 2 - button_text.get_width() / 2, \
                                button_rect[1] + button_height / 2 - button_text.get_height() / 2))

    pygame.display.update()

pygame.quit() # pylint: disable=no-member
