# Number Guessing Game
# -------------------

import random

number = random.randint(1,100)                                                       # This program generates a random number between 1 and 100.

while True:                                                                          # The user keeps guessing the number until they get it right.

    try:                                                                             # The program also handles invalid input using try-except to avoid crashing.
        choice = int(input("Guess the number between 1 and 100: "))

        if choice != number:                                                         # After each guess:
            if choice > number:                                                      # - If the guess is higher than the number, it prints "Too High!"
                print("Too High!")

            else:                                                                    # - If the guess is lower than the number, it prints "Too Low!"
                print("Too Low!")

        else:                                                                        # - If the guess is correct, it congratulates the user and ends the game.
            print("Congratulations! You guessed the number.")
            break
    
    except ValueError:
        print("Enter valid input")




# Concepts used:
# - random number generation
# - while loop
# - user input
# - if-else conditions
# - exception handling (try-except)
# - type conversion (int)