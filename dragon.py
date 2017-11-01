import random
import time

def displayIntro(): #this is a multi-line
    print('''You are in a land full of dragons. In front of you are two caves.
    In one cave, the dragon is blind and will not attack you. The other dragon is blood-thirsty
    and will eat you on sight.''')
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        cave = input()

        return cave

def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)
    print('WRAHHHH!\nThe dragon ')

    friendlyCave = random.randint(1,2)

    if chosenCave == str(friendlyCave):
        print('''does not see you. 
        You remain ALIVE.''')
    else:
        print('opens his mouth and eats you. '
              'YOU DIED.''')

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print('Do you want to play again? (yes or no)')
    playAgain = input()

print('Thank you for playing!')