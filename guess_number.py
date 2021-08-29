#!/usr/bin/env python3
# This is a guess the number game.

import random

secret_number = random.randint(1,20)
print("Guess what number I'm thinking (between 1 and 20): ")
print("You have 6 chances ...")
# Ask user to guess 6 times
for i in range(1,7):
    while True:
        guess = input(f'Guess {i}: ')
        try:
            guessed_value = int(guess)
            break
        except ValueError:
            print("Input only numbers please!")

    if (guessed_value < secret_number):
        print("Guessed number is too low! Try higher")
    elif (guessed_value > secret_number):
        print("Guessed number is too high! Try lower")
    else:
        break

if (guessed_value == secret_number):
    print(f'You have guessed the correct number in {i} attempts ...')
else:
    print(f'Sorry! I guessed {secret_number}')