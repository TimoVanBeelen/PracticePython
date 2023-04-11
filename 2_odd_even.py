# Exercise 2 from https://www.practicepython.org
# Written by:   Timo van Beelen
# Date:         10-04-2023

# Define global variables


# Define functions


# Main
if __name__ == "__main__":
    num = int(input("Give me a number please:\n")) # Ask the user for a number
    denom = int(input("With what number should we be able to divide it?\n")) # Ask the user for the denominator

    # Check whether it is odd or not and answer appropriately
    if num % 2 == 1: print("Hmmm that's odd...")
    elif num % 4 == 0: print("Going for multiples of 4, are we now?")
    else: print("Ah, now we're even on the first number!")

    # Check if it is divisible by the denominator
    if num % denom == 0: print("The number %i is indeed divisable by %i" %(num,denom))
    else: print("These numbers do not divide to an integer!")