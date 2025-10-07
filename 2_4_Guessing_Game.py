import random

num = random.randint(1, 100)
flag = True
guess = 0

print('Guess my number between 1 and 100 : ', end=' ')

while flag:  # While flag remains True / Until the number is guessed correctly
    guess = input()
    if not guess.isdigit():
        print('Invalid! Please enter a number between 1 and 100')
        break
    elif int(guess) < num:
        print('Too low! Try a higher number', end=' ')
    elif int(guess) > num:
        print('Too high! Try a lower number', end=' ')
    else:
        print('Correct... My number is ' + guess)
        flag = False