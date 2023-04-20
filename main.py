from random import randint

import sys

answer = randint(int(sys.argv[1]), int(sys.argv[2]))
tries = 0
while True:

    try:
        guess = int(input('Guess a number between 1-10: '))
        if 0 < guess < 11:
            tries = tries + 1
            if guess == answer:
                print('You are a genius!! ')
                print(f'Number of times you guessed: {tries}')
                break
        else:
            print('please enter a number between 1 - 10')
    except ValueError:
        print('Exception Please enter a Number!!!')