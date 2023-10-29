import pygame 
from pygame.locals import *
import os
pygame.init()

screen = pygame.display.set_mode((700, 700), 0, 32) # 32 bit buffer depth
sprite1 = pygame.image.load(os.path.join("image","butterfly.png")).convert_alpha()
sprite1 = pygame.transform.scale(sprite1, (32, 32))
sprite1_width = sprite1.get_width()
sprite1_height = sprite1.get_height()
pygame.display.set_caption("Hello, Butterfly!")
screen.fill((0, 0, 0))

game_over = False
x, y = 0, 0
clock = pygame.time.Clock()
movement = 0.5

while not game_over:
    dt = clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        y -= movement * dt
    if pressed[pygame.K_DOWN]:
        y += movement * dt
    if pressed[pygame.K_LEFT]:
        x -= movement * dt
    if pressed[pygame.K_RIGHT]:
        x += movement * dt
    if pressed[pygame.K_SPACE]:
        x, y = 0, 0
    
    screen.fill((0, 0, 0))
    
    screen.blit(sprite1, (x, y))
    pygame.display.update()
pygame.quit()
