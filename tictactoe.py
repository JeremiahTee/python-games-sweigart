#Tic-Tac-Toe

import random

def drawBoard(board):
    #This function prints out the board that it was passed

    #'board' is a list of 10 strings representing the board (ignore index 0)
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])

def inputPlayerLetter():
    #Lets the player type which letter they want to be
    #Returns a list with the player's letter as the first item and the
    #computer's letter as the second
    letter = ''
    while not (letter == 'X' or letter =='O'):
        print('Do you want to be X or O?')
        letter = input().upper()
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O','X']

def whoGoesFirst():
    #Randomly choose which player goes first
    if random.randint(0,1) == 0:
        return 'computer'
    else:
        return 'player'

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    # Given a board & player's letter, return True if that player has won
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # Across the top
            (bo[4] == le and bo[5] == le and bo[6] == le) or  # Across the middle
            (bo[1] == le and bo[2] == le and bo[3] == le) or  # Across the bottom
            (bo[7] == le and bo[4] == le and bo[1] == le) or  # 1st column
            (bo[8] == le and bo[5] == le and bo[2] == le) or  # 2nd column
            (bo[9] == le and bo[6] == le and bo[3] == le) or  # 3rd column
            (bo[7] == le and bo[5] == le and bo[3] == le) or  #Diagonal
            (bo[9] == le and bo[5] == le and bo[1] == le)     #Anti-diagonal
            )

def getBoardCopy(board):
    # Make a copy of the board list and return it
    boardCopy = []
    for i in board:
        boardCopy.append(i)

    return boardCopy

def isSpaceFree(board, move):
    # Return True if the assed move is free on the passed board.
    return board[move] == ' '

def getPlayerMove(board):
    # Let the player enter their move
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    # Returns a valid move from the passed list on the passed board
    # Returns None is there is no valid move.
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None