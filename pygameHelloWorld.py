import pygame, sys
from pygame.locals import *

# Set up pygame.
pygame.init()

# Set up the window
windowSurface = pygame.display.set_mode((500,400), 0, 32)
pygame.display.set_caption('Hello world')