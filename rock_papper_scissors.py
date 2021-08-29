#!/usr/bin/env python3

import random
from enum import IntEnum

wins = 0
draws = 0
losses = 0

class Move(IntEnum):
    rock = 0
    paper = 1
    scissors = 2

def get_user_input():
    choices = [f"{move.name}[{move.value}]" for move in Move]
    choices_str = ", ".join(choices)
    user_move = int(input(f"Enter a choice from {choices_str}: "))
    return user_move

def computer_input():
    computer_move = random.randint(0,2)
    return computer_move

def calculate_score(outcome):
    global wins
    global draws
    global losses
    
    if(outcome == 0):
        wins += 1
    elif(outcome == 1):
        draws += 1
    else:
        losses += 1

def determine_result(user_move, computer_move):
    if(user_move == computer_move):
        result = f"Game is a tie .. Both selected {Move(user_move).name}"
        calculate_score(1)
    elif(user_move == Move.rock):
        if(computer_move == Move.scissors):
            result = f"You win .. Rock smashes Scissors"
            calculate_score(0)
        else:
            result = f"You lose .. Paper covers Rock"
            calculate_score(2) 
    elif(user_move == Move.paper):
        if(computer_move == Move.scissors):
            result = f"You lose .. Scissors cuts Paper"
            calculate_score(2)
        else:
            result = f"You win .. Paper covers Rock"
            calculate_score(0)
    elif(user_move == Move.scissors):
        if(computer_move == Move.rock):
            result = f"You lose .. Rock smashes Scissors"
            calculate_score(2)
        else:
            result = f"You win .. Scissors cuts Paper"
            calculate_score(0)
    return result

print('************************************')
print('ROCK, PAPER, SCISSORS')
print('Enter 101 to quit')
print('************************************')

while True:
    try:
        user_move = get_user_input()
    except ValueError as e:
        print('That\'s not a number!')
    else:
        if(user_move == 101):
            print('Exiting Game now ... BYE')
            break
        if not ( -1 < user_move < 3):
            print(f"Invalid selection. Enter a value in range [0, 2]")
            continue
    computer_move = computer_input()
    result = determine_result(user_move, computer_move)
    print(f'{result} SCORE: WINS - {wins} DRAWS - {draws} LOSSES - {losses}')
    
    play_again = input("Press y to play again: ")
    if(play_again.lower() != 'y'):
        break