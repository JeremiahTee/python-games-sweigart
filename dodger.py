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

# Core of game
while True:
    # Set up the start of the game
    baddies = []
    score = 0
    playerRect.topleft = (WINDOW_WIDTH / 2, WINDOW_HEIGHT - 50) # Position of player
    moveLeft = moveRight = moveUp = moveDown = False
    reverseCheat = slowCheat = False
    baddieAddCounter = 0
    pygame.mixer.music.play(-1, 0.0)

    while True: # The game loop runs while the game part is playing
        score += 1 # Increase score

        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

            if event.type == KEYDOWN:
                if event.key == K_z:
                    reverseCheat = True
                if event.key == K_x:
                    slowCheat = True
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

                if event.key == KEYUP:
                    if event.key == K_z:
                        reverseCheat = False
                        score = 0
                    if event.key == K_x:
                        slowCheat = False
                        score = 0
                    if event.key == K_ESCAPE:
                        terminate()

                    if event.key == K_LEFT or event.key == K_a:
                        moveLeft = False
                    if event.key == K_RIGHT or event.key == K_d:
                        moveRight = False
                    if event.key == K_UP or event.key == K_w:
                        moveUp = False
                    if event.key == K_DOWN or event.key == K_s:
                        moveDown = False

                if event.type == MOUSEMOTION:
                    # If the mouse moves, move the player to the cursor.
                    playerRect.centerx = event.pos[0]
                    playerRect.centery = event.pos[1]
                # Add new baddies at the to of the screen, if needed
                if not reverseCheat and not slowCheat:
                    baddieAddCounter += 1
                if baddieAddCounter == RATE_NEW_BADDIE:
                    baddieAddCounter = 0
                    baddieSize = random.randint(BADDIE_MIN_SIZE, BADDIE_MAX_SIZE)
                    newBaddie = {'rect': pygame.Rect(random.randint(0, WINDOW_WIDTH - baddieSize), 0 - baddieSize, baddieSize),
                                 'speed': random.randint(BADDIE_MIN_SPEED, BADDIE_MAX_SPEED),
                                 'surface': pygame.transform.scale(baddieImage, (baddieSize, baddieSize))
                    }
                    baddies.append(newBaddie)

            # Move the player around
            if moveLeft and playerRect.left > 0:
                playerRect.move_ip(-1 * PLAYER_MOVE_RATE, 0)
            if moveRight and playerRect.right < WINDOW_WIDTH:
                playerRect.move_ip(PLAYER_MOVE_RATE, 0)
            if moveUp and playerRect.top > 0:
                playerRect.move_ip(0, -1 * PLAYER_MOVE_RATE)
            if moveDown and playerRect.bottom < WINDOW_HEIGHT:
                playerRect.move_ip(0, PLAYER_MOVE_RATE)

            # Move the baddies down
            for b in baddies:
                if not reverseCheat and not slowCheat:
                    b['rect'].move_ip(0, b['speed'])
                elif reverseCheat:
                    b['rect'].move_ip(0, -5)
                elif slowCheat:
                    b['rect'].move_ip(0, 1)

            # Delete baddies that have fallen past the bottom
            for b in baddies:
                if b['rect'].top > WINDOW_HEIGHT:
                    baddies.remove(b)

            # Draw the game world on the window
            windowSurface.fill(BACKGROUND_COLOR)

            # Draw the score and top score
            drawText('Score: %s' % (score), font ,windowSurface, 10, 0)
            drawText('Top score: %s' % (topScore), font, windowSurface, 10, 40)

            # Draw the player's rectangle
            windowSurface.blit(playerImage, playerRect)

            # Draw each baddie
            for b in baddies:
                windowSurface.blit(b['surface'], b['rect'])

            pygame.display.update()

            # Check if any of the baddies have hit the player
            if playerHasHitBaddie(playerRect, baddies):
                if score > topScore:
                    topScore = score # Set new top score
                break

            mainClock.tick(FPS)

    # Stop the game and show the "Game Over" screen
    pygame.mixer.music.stop()
    gameOverSound.play()

    drawText('GAME OVER', font, windowSurface, (WINDOW_WIDTH / 3)), (WINDOW_HEIGHT / 3)
    drawText('Press a key to play again.', font, windowSurface, (WINDOW_WIDTH / 3) - 80, (WINDOW_HEIGHT / 3) + 50)
    pygame.display.update()
    waitForPlayerToPressKey()

    agameOverSound.stop()