'''Example file showing a basic pygame "game loop"'''
import pygame

# pygame setup
pygame.init() # pylint: disable=no-member
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True # pylint: disable=invalid-name

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # pylint: disable=no-member
            running = False # pylint: disable=invalid-name

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit() # pylint: disable=no-member
