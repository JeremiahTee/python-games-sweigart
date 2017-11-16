import pygame, sys, random
from pygame.locals import *

# Set up pygame
pygame.init()
mainClock = pygame.time.Clock()

# Set up the window
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0 , 32)
pygame.display.set_caption('Collision Detection')

# Set up the colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255 , 255)

# Set up the player and food data structures
foodCounter = 0
NEW_FOOD = 40
FOOD_SIZE = 20
player = pygame.Rect(300, 100, 50, 50)
foods = []
for i in range(20):
    foods.append(pygame.Rect(random.randint(0, WINDOW_WIDTH - FOOD_SIZE), random.randint(0, WINDOW_HEIGHT - FOOD_SIZE), FOOD_SIZE, FOOD_SIZE))

# Set up movement variables
moveLeft = False
moveRight = False
moveUp = False
moveDown = False

MOVE_SPEED = 6

# Run the game loop
while True:
    # Check for events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            # Change the keyboard variables
            if event.key == K_LEFT or event.key == K_a:
                moveRight = False
                moveLeft  = True
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
                player.bottom = random.randint(0, WINDOW_WIDTH - player.width)

        if event.type == MOUSEBUTTONUP:
            foods.append(pygame.Rect(event.pos[0], event.pos[1], FOOD_SIZE, FOOD_SIZE))

        foodCounter += 1
        if foodCounter >= NEW_FOOD:
            # Add new food.
            foodCounter = 0
            foods.append(pygame.Rect(random.randint(0, WINDOW_WIDTH - FOOD_SIZE), random.randint(0, WINDOW_HEIGHT - FOOD_SIZE), FOOD_SIZE, FOOD_SIZE))

        # Draw the white background onto the surface
        windowSurface.fill(WHITE)

        # Move the player
        if moveDown and player.bottom < WINDOW_HEIGHT:
            player.top += MOVE_SPEED
        if moveUp and player.top > 0:
            player.top -= MOVE_SPEED

        if moveLeft and player.left > 0:
            player.left -= MOVE_SPEED
        if moveRight and player.right < WINDOW_WIDTH:
            player.right += MOVE_SPEED

        # Draw the player onto the surface
        pygame.draw.rect(windowSurface, BLACK, player)

        # Check whether the player has intersected with any food squares
        for food in foods[:]:
            if player.colliderect(food):
                foods.remove(food)

        # Draw the food
        for i in range(len(foods)):
            pygame.draw.rect(windowSurface, GREEN, foods[i])

        # Draw the window onto the screen
        pygame.display.update()
        mainClock.tick(60)