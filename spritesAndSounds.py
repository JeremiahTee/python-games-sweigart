import pygame, sys, time, random
from pygame.locals import *

# Set up pygame.
pygame.init()
mainClock = pygame.time.Clock()

# Set up the window
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
windowSurface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
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

# Run the game loop
while True:
    # Check for the QUIT event
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            # Change the keyboard variables
            if event.key == K_LEFT or event.key == K_a:
                moveRight = False
                moveLeft = True
            if event.key == K_RIGHT or event.key == K_d:
                moveLeft = False
                moveRight = True
            if event.key == K_UP or event.key == K_w:
                moveDown = False
                moveUp = True
            if event.key == K_DOWN or event.key == K_s:
                moveUp = False
                moveDown = True
        if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_LEFT or event.key == K_a:
                    moveLeft = False
                if event.key == K_RIGHT or event.key == K_d:
                    moveRight = False
                if event.key == K_UP or event.key == K_w:
                    moveUp = False
                if event.key == K_DOWN or event.key == K_s:
                    moveDown = False
                if event.key == K_x:
                    player.top = random.randint(0, WINDOW_HEIGHT - player.height)
                    player.left = random.randint(0, WINDOW_WIDTH - player.width)
                if event.key == K_m:
                    if musicPlaying:
                        pygame.mixer.music.stop()
                    else:
                        pygame.mixer.music.play(-1, 0.0)
                    musicPlaying = not musicPlaying

        if event.type == MOUSEBUTTONUP:
            foods.append(pygame.Rect(event.pos[0] - 10, event.pos[1] - 10, 36, 36))

        foodCounter += 1
        if foodCounter >= NEWFOOD:
            # Add new food
            foodCounter = 0
            foods.append(pygame.Rect(random.randint(0, WINDOW_WIDTH - 36), random.randint(0, WINDOW_HEIGHT - 36), 36, 36))

        # Draw the white background onto the surface
        windowSurface.blit(playerStretchedImage, player)
        

        # Check whether the block has intersected with any food squares
        for food in foods[:]:
            if player.colliderect(food):
                foods.remove(food)
                player = pygame.Rect(player.left, player.top, player.width + 2, player.height + 2)
                playerStretchedImage = pygame.transform.scale(playerImage, (player.width, player.height))
                if musicPlaying:
                    pickUpSound.play()

        # Draw the food
        for food in foods:
            windowSurface.blit(foodImage, food)

        # Draw window onto the screen
        pygame.display.update()
        mainClock.tick(40)








