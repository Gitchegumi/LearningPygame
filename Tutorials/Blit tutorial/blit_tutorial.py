'''This file represents the minimal code required to run a game using pygame'''
import pygame
from pygame.locals import * # this is additiional to what was in the tutorial, pylint: disable=unused-wildcard-import,wildcard-import

# define a main function
def main():
    '''This is the main function'''
    # initialize the pygame module
    pygame.init() # pylint: disable=no-member
    # load and set the logo
    logo = pygame.image.load("pygame_powered.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")

    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((240,180)) # pylint: disable=unused-variable

    # define a variable to control the main loop
    running = True

    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == QUIT: # pylint: disable=undefined-variable
                # change the value to False, to exit the main loop
                running = False

# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
