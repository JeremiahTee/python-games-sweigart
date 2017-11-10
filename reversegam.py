# Reversegam: a clone of Othello/Reversi, Chapter 15
import random
import sys
WIDTH, HEIGHT = 8 # Board is 8 spaces wide & 8 spaces tall

def drawBoard(board):
    # Print the board passed to this function. Return None.
    print('     12345678')
    print('     +--------+')
    for y in range(HEIGHT):
        print('%s|' % (y+1), end='') 
        for x in range(WIDTH):
            print(board[x][y], end='')