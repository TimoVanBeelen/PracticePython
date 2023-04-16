# Exercise 12 from https://www.practicepython.org
# Written by:   Timo van Beelen
# Date:         12-04-2023

# Add libraries
import random

# Define global variables
a = random.sample(range(1,30), 12)

# Define functions


# Main
if __name__ == "__main__":
    print(a) # So that we know the list we start with
    print([a[0], a[len(a)-1]]) # Print the item at place 0 (start) and at the end (len(a) -1) where -1 is to prevent the list index going out of range