# Exercise 9 from https://www.practicepython.org
# Written by:   Timo van Beelen
# Date:         11-04-2023

# Import libraries
import random

# Define global variables


# Define functions


# Main
if __name__ == "__main__":
    a = random.randint(1, 9)    # Generate a random integer
    x = 0                       # Set the guessed x to 0 to start
    tries = 1                   # Always 1 try at least

    while x != a:
        x = input("""Guess the random number between (and including) 1 to 9! To stop, type: exit\n""")  # Get the guess from the user
        if x == "exit": break   # Stop if the user types exit
        elif a == int(x): 
            print("Yes that is it! This took only %i tries." %tries)
            break   # Stop when it is correct
        elif int(x)<a: 
            print("Ohw, that is too low! Try again!")
            tries = tries+1 # Another try is needed
        elif int(x)>a: 
            print("Nooo, that is too high! Give it another shot.")
            tries = tries+1
