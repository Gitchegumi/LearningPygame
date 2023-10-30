'''A simple program that moves a butterfly sprite around the screen using the arrow keys.'''
import os
import pygame
from pygame.locals import * # pylint: disable=wildcard-import, unused-wildcard-import

pygame.init() # pylint: disable=no-member

screen = pygame.display.set_mode((700, 700), 0, 32) # 32 bit buffer depth
sprite1 = pygame.image.load(os.path.join("image","butterfly.png")).convert_alpha()
sprite1 = pygame.transform.scale(sprite1, (32, 32))
sprite1_width = sprite1.get_width()
sprite1_height = sprite1.get_height()
pygame.display.set_caption("Hello, Butterfly!")
screen.fill((0, 0, 0))

GAME_OVER = False
x, y = 0, 0
clock = pygame.time.Clock()
MOVEMENT = 0.5

while not GAME_OVER:
    dt = clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # pylint: disable=no-member
            GAME_OVER = True

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: # pylint: disable=no-member
        y -= MOVEMENT * dt
    if pressed[pygame.K_DOWN]: # pylint: disable=no-member
        y += MOVEMENT * dt
    if pressed[pygame.K_LEFT]: # pylint: disable=no-member
        x -= MOVEMENT * dt
    if pressed[pygame.K_RIGHT]: # pylint: disable=no-member
        x += MOVEMENT * dt
    if pressed[pygame.K_SPACE]: # pylint: disable=no-member
        x, y = 0, 0

    x = max(x, 0)
    y = max(y, 0)
    x = min(x, screen.get_width() - sprite1_width)
    y = min(y, screen.get_height() - sprite1_height)

    screen.fill((0, 0, 0))

    screen.blit(sprite1, (x, y))
    pygame.display.update()
pygame.quit() # pylint: disable=no-member
