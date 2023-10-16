'''This is my first attmept at making a game in python. It will most likely be a snake clone.'''
import pygame
from pygame.locals import * # pylint: disable=wildcard-import,unused-wildcard-import

# pygame setup
pygame.init() # pylint: disable=no-member
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
