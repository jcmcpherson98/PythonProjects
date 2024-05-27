# Number guessing

import random

"""
1. Random number in a range
2. Capture guess
3. Evaluate user guess

Command line game - provide user messages

Python modules -> https://docs.python.org/3/tutorial/modules.html
"""

game_random_number = random.randint(1, 100)
game_active = True

while game_active:
    game_start_message = "Guess a number between 1 - 100:"
    print(game_start_message)
    user_guess = int(input())
    if user_guess == game_random_number:
        game_active = False
        print("You guessed correctly")
    elif user_guess < game_random_number:
        print("Your guess is too low")
    else:
        print("Your guess is too high")
