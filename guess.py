#This is a Guess the Number game.
import random
import math

counter = 0
guess = 0

print('Hello! What is your name?')
myName = input()

number = random.randint(1, 20)
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')

while guess!= number:
    print('Take a guess...')
    guess = input()
    guess = int(guess)

    if guess < number:
        print('Your guess is too low.')
        counter = counter + 1
    if guess > number:
        print('Your guess is too high.')
        counter = counter + 1
    if guess == number:
        counter = str(counter + 1)
        print('Good job! ' + myName + '! You guessed my number in ' +
              counter + ' guesses!')