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

# Set up pygame, the window, and the mouse cursor
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Dodger')
pygame.mouse.set_visible(False)

# Set up the game fonts
font = pygame.font.SysFont("comicsansms", 48)

# Set up sounds
gameOverSound = pygame.mixer.Sound('gameover.wav')
pygame.mixer.music.load('background.mid')

# Set up images
playerImage = pygame.image.load('player.png')
playerRect = playerImage.get_rect()
baddieImage = pygame.image.load('baddie.png')

# Show the "Start" screen.
windowSurface.fill(BACKGROUND_COLOR)
drawText('Dodger', font, windowSurface, (WINDOW_WIDTH / 3), (WINDOW_HEIGHT / 3))
drawText('Press a key to start', font, windowSurface, (WINDOW_WIDTH / 3) - 30, (WINDOW_HEIGHT / 3) + 50)
pygame.display.update()
waitForPlayerToPressKey()

topScore = 0
