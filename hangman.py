import random
HANGMAN_PICS = ['''
    +---+
        |
        |
        |
       ===''','''
    +---+ 
    0   |
        |
        |
       ===''','''
    +---+ 
    0   |
   /|      |
       |
       ===''','''     
    +---+ 
    0   |
   /|\  |
        |
       ===''','''    
    +---+
    0   |
   /|\  |
   /    |
       ===''','''
   +---+
    0   |
   /|\  |
   / \  |
       ===''']
words = 'dog cat ant bat rat sloth python whale werewolf llama panda cougar lizard moose mouse'.split()

def getRandomWord(wordList):
    #This function returns a random string from the passed list of strings
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)] + "\n")

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end = '')
        print()

    blanks = '_' * len(secretWord)

    for i in range (len(secretWord)): # Replace blanks with correctly guessed letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: #Show the secret word with spaces in between each letter
        print(letter, end=' ')

def getGuess(alreadyGuessed):
    #Returns the letter the player entered. This function makes sure the player entered a single letter.
    while True:
        print('Guess a letter')
        guess = input().lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed
            print('You have already guessed that letter. Choose another one!')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER')
        else:
            return guess

def playAgain():
    #This function returns True if the player wants to play again, otherwise False
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')
