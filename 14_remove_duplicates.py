# Exercise 14 from https://www.practicepython.org
# Written by:   Timo van Beelen
# Date:         16-04-2023

# Add libraries
import random


# Define global variables
a = [1, 2, 1, 1, 5, 2, 6, 7, 8, 2, 3, 4, 1]


# Define functions


# Main
if __name__ == "__main__":
    b = [] # Needed to get the loop working
    for x in a:
        if not x in b: b.append(x)
    c = [*set(a)] # A set automatically removes all duplicates
    print(a,'\n', b,'\n', c)
