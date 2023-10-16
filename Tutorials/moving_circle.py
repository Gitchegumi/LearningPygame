'''Example file showing a circle moving on screen'''
import pygame

# pygame setup
pygame.init() # pylint: disable=no-member
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
RUNNING = True
dt = 0 # pylint: disable=invalid-name

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while RUNNING:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # pylint: disable=no-member
            RUNNING = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]: # pylint: disable=no-member
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]: # pylint: disable=no-member
        player_pos.y += 300 * dt
    if keys[pygame.K_a]: # pylint: disable=no-member
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]: # pylint: disable=no-member
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit() # pylint: disable=no-member
