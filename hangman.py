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
   /|   |
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
       ===''','''
   +---+
   [0   |
   /|\  |
   / \  |
       ===''','''
   +---+
   [0]  |
   /|\  |
   / \  |      
      ''']

#words = 'dog cat ant bat rat sloth python whale werewolf llama panda cougar lizard moose mouse'.split()
words = {'Colors': 'red orange yellow green blue indigo violet white black brown'.split(),
         'Shapes': 'square triangle rectangle circle ellipse trapezoid pentagon hexagon octagon'.split(),
         'Fruits': 'apples orange lemon lime pear watermelon banana mango tomato strawberry'.split(),
         'Animals': 'dog cat ant bat rat sloth python whale werewolf llama panda cougar lizard moose mouse'.split()}

'''
def getRandomWord(wordList):
    #This function returns a random string from the passed list of strings
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]
'''

def getRandomWord(wordDict): #updated function for dictionaries
    #This function returns a random string from the passed dictionary of lists fo strings and its key

    #First, randomly select a key from dictionary:
    wordKey = random.choice(list(wordDict.keys())) #using choice() from random

    #Second, randomly select a word from the key's list in the dictionary
    wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)

    return [wordDict[wordKey][wordIndex], wordKey]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)] + "\n")

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end = ' ')

    print()
    blanks = '_' * len(secretWord)

    for i in range (len(secretWord)): # Replace blanks with correctly guessed letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: #Show the secret word with spaces in between each letter
        print(letter, end=' ')

    #Check if it's last guess
    if len(missedLetters) == len(HANGMAN_PICS) - 2:
        print('\nCareful! This is your last guess.')

def getGuess(alreadyGuessed):
    #Returns the letter the player entered. This function makes sure the player entered a single letter.
    while True:
        print('Guess a letter')
        guess = input().lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose another one!')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER')
        else:
            return guess

def playAgain():
    #This function returns True if the player wants to play again, otherwise False
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

print('H A N G M A N')

difficulty = ''
while difficulty not in 'EMH':
    print('Enter difficulty: E - Easy, M - Medium, H - Hard')
    difficulty = input().upper()

if difficulty == 'M':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
if difficulty == 'H':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
    del HANGMAN_PICS[5]
    del HANGMAN_PICS[3]

missedLetters = ''
correctLetters = ''
secretWord,secretSet = getRandomWord(words) #multiple assignment, where secretSet is the key of the dictionary
isDone = False

while not isDone:
    print('The secret word is in the set: ' + secretSet.lower())
    displayBoard(missedLetters, correctLetters, secretWord)
    #Let the player enter a letter
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord: #add guess to correctLetters
        correctLetters = correctLetters + guess
        #Check if player has won
        foundAllLetters = True
        for i in range (len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
                print('Yes! The secret word is ' + secretWord + ". You have won!")
                isDone = True
    else:
        missedLetters = missedLetters + guess

    #Check if player has guessed too many times and lost
    if len(missedLetters) == len(HANGMAN_PICS) - 1:
        displayBoard(missedLetters, correctLetters, secretWord)
        print('You have run out of guesses!\nAfter ' +
              str(len(missedLetters)) + ' missed guesses and ' +
              str(len(correctLetters)) + ' correct guesses, the word was "' +
              secretWord + '"')
        isDone = True

    #Ask player to play again (only if game is done)
        if isDone:
            if playAgain(): #update variables
                missedLetters = ''
                correctLetters = ''
                isDone = False
                secretWord, secretSet= getRandomWord(words)
            else:
                print('Thank you for playing!')
                break