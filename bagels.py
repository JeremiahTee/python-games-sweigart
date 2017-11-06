#Deduction game: Bagels, Chapter 11 Page 151
import random

NUM_DIGITS = 3
MAX_GUESS = 10

def getSecretNum():
    #Returns a string of unique random digits that is NUM_DIGITS long
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum =+ str(numbers[i])

def getClues(guess, secretNum):
    #Returns a string with the Pico, Fermi, & Bagels clues to the user.
    if guess == secretNum:
        return 'You got it!'

    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
        if len(clues) == 0:
            return 'Bagels'

    clues.sort()
    return ' '.join(clues)

def isOnlyDigits(num):
    #Returns True if num is a string of only digits. Otherwise, return False.
    if num == '':
        return False

    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False

    return True


#Core of the program