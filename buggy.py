#purpose of this program is to learn how to debug with Pycharm
import random
number1 = random.randint(1,10)
number2 = random.randint(1,10)
print('What is ' + str(number1) + ' + ' + str(number2) + '?')
answer = input()
if answer == number1 + number2:
    print('Correct!')
else: #debugger skipped to this line (9) therefore, if statement was false!
    print('Nope! The answer is ' + str(number1 + number2))