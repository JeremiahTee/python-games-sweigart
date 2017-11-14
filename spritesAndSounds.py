import pygame, sys, time, random
from pygame.locals import *

# Set up pygame.
pygame.init()
mainClock = pygame.time.clock()

# Set up the window
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
windowSurface = pygame.display.set_mode(WINDOW_WIDTH, WINDOW_HEIGHT, 0, 32)
pygame.display.set_caption('Trump eats Hilary')

# Set up the colors
WHITE = (255, 255, 255)

# Set up the block data structure
player = pygame.Rect(300, 100, 72, 103)
playerImage = pygame.image.load('donald.png')
playerStretchedImage = pygame.transform.scale(playerImage, (72, 103))
foodImage = pygame.image.load('hilary.png')
foods = []
for i in range(20):
    foods.append(pygame.Rect(random.randint(0, WINDOW_WIDTH - 36), random.randint(0, WINDOW_HEIGHT - 36), 36, 36))

foodCounter = 0
NEWFOOD = 40

# Set up keyboard variables
moveLeft = False
moveRight = False
moveUp = False
moveDown = False

MOVESPEED = 6

# Set up the music
pickUpSound = pygame.mixer.Sound('pickup.wav')
pygame.mixer.music.load('background.mid')
pygame.mixer.music.play(-1,0.0)
musicPlaying = True

