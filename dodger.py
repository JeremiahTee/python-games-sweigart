import pygame, random, sys
from pygame.locals import *

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
TEXT_COLOR = (0, 0, 0) # Black
BACKGROUND_COLOR = (255, 255, 255)
FPS = 60
BADDIE_MIN_SIZE = 10
BADDIE_MAX_SIZE = 40
BADDIE_MIN_SPEED = 1
BADDIE_MAX_SPEED = 8
RATE_NEW_BADDIE = 6
PLAYER_MOVE_RATE = 5

def terminate():
    pygame.quit()
    sys.exit()

def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # Pressing ESC quits
                    terminate()
                return

def playerHasHitBaddie(playerRect, baddies):
    for b in baddies:
        if playerRect.colliderect(b['rect']):
            return True
    return False

def drawText(text, font, surface, x, y):
    textObj = font.render(text, 1, TEXT_COLOR)
    textRect = textObj.get_rect()
    surface.blit(textObj, textRect)