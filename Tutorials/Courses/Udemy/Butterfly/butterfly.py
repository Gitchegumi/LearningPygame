import pygame
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
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    screen.blit(sprite1, ((screen.get_width() / 2) - (sprite1_height / 2), (screen.get_height() / 2) - (sprite1_width / 2)))
    pygame.display.update()
pygame.quit()