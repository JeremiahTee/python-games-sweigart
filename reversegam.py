# Reversegam: a clone of Othello/Reversi, Chapter 15
import random
import sys
WIDTH, HEIGHT = 8 # Board is 8 spaces wide & 8 spaces tall

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