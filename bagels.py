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