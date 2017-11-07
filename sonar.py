#Sonar Treasure Hunt, Chapter 13
#Topics covered: data structures, Pythagorean theorem, remove(), isdigit(), sys.exit()

import random
import sys
import math

def getNewBoard():
    #Create a new 60x15 board data structure.
    board = []
    for x in range(60): # The main list is a list of 60 lists
        board.append([])
        for y in range(15): # Each list in the main list has 15 single-character strings.
                            # Use different characters for the ocean to make it more readable
        if random.randint(0,1) == 0:
            board[x].append('~')
        else:
            board[x].append('^')
    return board

def drawBoard(board):
    #Draw the board data structure.
    tensDigitsLine = '   ' # Initial space for the numbers down the left side of the board
    for i in range(1,6):
        tensDigitsLine += (' ' * 9) + str(i)

    # Print the numbers across the top of the board.
    print(tensDigitsLine)
    print('     ' + ('0123456789' * 6))
    print()

    # Print each of the 15 rows
    for row in range(15):
        # Single-digit numbers need to be padded with an extra space.
        if row < 10:
            extraSpace = ' '
        else:
            extraSpace = ''

        #Create the string for this row on the board.
        boardRow = ''
        for column in range(60):
            boardRow += board[column][row]

        print('%s%s %s %s' % (extraSpace, row, boardRow, row))

    #Print the numbers across the bottom of the board.
    print()
    print('     ' + ('0123456789' * 6))
    print(tensDigitsLine)

def getRandomChests(numChests):
    # Create a list of chest data structures (two-item lists of x,y int coordinates)
    chests = []
    while len(chests) < numChests:
        newChest = [random.randint(0,59), random.randint(0,14)]
        if newChest not in chests: # Make sure a chest is not already here
            chests.append(newChest)
    return chests

def isOnBoard(x,y):
    # Return True if the coordinates are on the board; otherwise, return False
    return x >= 0 and x <= 59 and y >= 0 and y <= 14

def makeMove(board, chests, x, y):