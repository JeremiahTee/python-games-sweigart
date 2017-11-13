import pygame, sys, time
from pygame.locals import *

# Set-up game
pygame.init()

# Set up window
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
pygame.display.set_caption('Animating Rectangles')

# Set up direction variables
DOWN_LEFT = 'downleft'
DOWN_RIGHT = 'downright'
UP_LEFT = 'upleft'
UP_RIGHT = 'upright'

MOVESPEED = 4

# Set up the colors.
WHITE = (255, 255, 255)
RED  = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up box data structure.
b1 = {'rect': pygame.rect(200, 80, 50, 100), 'color': RED, 'dir': UP_RIGHT}
b2 =  {'rect': pygame.rect(200, 200, 20, 20), 'color': GREEN, 'dir': UP_LEFT}
b3 =  {'rect': pygame.rect(100, 150, 60, 60), 'color': BLUE, 'dir': DOWN_LEFT}
boxes = [b1, b2, b3]

# Run the game loop.
while True:
    # 