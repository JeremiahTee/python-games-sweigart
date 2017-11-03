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

