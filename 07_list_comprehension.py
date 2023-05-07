# Exercise 7 from https://www.practicepython.org
# Written by:   Timo van Beelen
# Date:         11-04-2023

# Define global variables
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Define functions


# Main
if __name__ == "__main__":
    list_even = [i for i in a if i%2==0] # make a list of all elements in list a that are divisable by 2
    print(list_even)