# Reversegam: a clone of Othello/Reversi, Chapter 15
import random
import sys
WIDTH, HEIGHT = 8 # Board is 8 spaces wide & 8 spaces tall
directions = [[0,1], [1,1], [1,0], [1,-1], [0,-1], [-1,-1], [1,0], [-1,1]]

def drawBoard(board):
    # Print the board passed to this function. Return None.
    print('     12345678')
    print('     +--------+')
    for y in range(HEIGHT):
        print('%s|' % (y+1), end='') # left column
        for x in range(WIDTH):
            print(board[x][y], end='')
        print('%s|' % (y + 1), end='') # right column
    print('     +--------+')
    print('     12345678')

def getNewBoard():
    # Create a brand-new, blank board data structure
    board = []
    for i in range (WIDTH):
        board.append([' ',' ',' ',' ',' ',' ',' ',' '])
    return board

def isValidMove(board, tile, xstart, ystart):
    # Return False if the player's move on space xstart, ystart is invalid
    # If it is a valid move, return a list of spaces that would become the player's if they move here
    if board[xstart][ystart] != ' ' or not isOnBoard(xstart, ystart):
        return False
    if tile == 'X':
        otherTile = 'O'
    else:
        otherTile = 'X'

    tilesToFlip = []
    for xdirection, ydirection in directions:
        x, y = xstart, ystart
        x += xdirection # First step in the x direction
        y += ydirection # First step in the y direction
        while isOnBoard(x, y) and board[x][y] == otherTile:
            # Keep moving in this x & y direction.
            x += xdirection
            y += ydirection
            if isOnBoard(x, y) and board[x][y] == tile:
                # There are pieces to flip over. Go in the reverse direction
                # until we reach the original space, noting all tiles along the way
            while True:
                x -= xdirection
                y -= ydirection
                if x == xstart and y == ystart:
                    break
                tilesToFlip.append([x,y])
    if len(tilesToFlip) == 0: # If no tiles were flipped, this is not a valid move.
        return False
    return tilesToFlip