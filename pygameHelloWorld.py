import pygame, sys
from pygame.locals import *

# Set up pygame.
pygame.init()

# Set up the window
windowSurface = pygame.display.set_mode((500,400), 0, 32)
pygame.display.set_caption('Hello world')

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255 ,255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up the fonts
basicFont = pygame.font.SysFont(None, 48)

# Set up the text
text = basicFont.render('Hello world!', True, WHITE, BLUE)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

# Draw the white background onto the surface
windowSurface.fill(WHITE)

# Draw a green polygon onto the surface.
pygame.draw.line(windowSurface, BLUE, (60,60), (120,60), 4)
pygame.draw.line(windowSurface, BLUE, (120, 60), (60,120))
pygame.draw.line(windowSurface, BLUE, (60,120), (120,120), 4)