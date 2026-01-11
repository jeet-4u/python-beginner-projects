# Dice Rolling Game
# -----------------
# This program simulates rolling two dice.

import random

while True:
    choice=input("Roll the dice? (y/n): ").lower()         # The user is asked if they want to roll the dice.

    if choice == 'y':                                      # If the user enters 'y', two random numbers between 1 and 6 are generated
        dice1=random.randint(1,6)
        dice2=random.randint(1,6)
        print(f"({dice1},{dice2})")                        # to represent the dice values and printed on the screen.

    elif choice == 'n':                                    # If the user enters 'n', the program thanks the user and exits.
        print("Thanks for playing!")
        break
 
    else:                                                  # Any other input is treated as invalid and the user is asked again.
        print("Invalid Choice!")                         



# Concepts used:
# - while loop
# - user input
# - if-elif-else conditions
# - random module
# - basic string handling (.lower())