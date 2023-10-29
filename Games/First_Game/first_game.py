'''This is my first attmept at making a game in python. It will most likely be a snake clone.'''
import os
import pygame
from pygame.locals import * # pylint: disable=wildcard-import,unused-wildcard-import


# pygame setup
pygame.init() # pylint: disable=no-member
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
background = pygame.image.load(os.path.join('Images', 'background.jpg')).convert()
background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))
player = pygame.image.load(os.path.join('Images', 'player_v2.png')).convert_alpha()
RUNNING = True
dt = 0 # pylint: disable=invalid-name

player_pos = pygame.Vector2(screen.get_width() / 2 - player.get_width() / 2, \
                            screen.get_height() / 2 - player.get_height() / 2) # pylint: disable=no-member
player_speed = 300 # pylint: disable=invalid-name

while RUNNING:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # pylint: disable=no-member
            RUNNING = False

    # fill the screen with a color to wipe away anything from last frame
    screen.blit(background, (0,0), (0, 0, screen.get_width(), screen.get_height()))

    screen.blit(player, player_pos)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]: # pylint: disable=no-member
        player_pos.y -= player_speed * dt
    if keys[pygame.K_s]: # pylint: disable=no-member
        player_pos.y += player_speed * dt
    if keys[pygame.K_a]: # pylint: disable=no-member
        player_pos.x -= player_speed * dt
    if keys[pygame.K_d]: # pylint: disable=no-member
        player_pos.x += player_speed * dt

    # keep player on screen
    x = max(player_pos.x, 0)
    y = max(player_pos.y, 0)
    player_pos.x = min(x, screen.get_width() - player.get_width())
    player_pos.y = min(y, screen.get_height() - player.get_height())

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 120
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(120) / 1000

pygame.quit() # pylint: disable=no-member
