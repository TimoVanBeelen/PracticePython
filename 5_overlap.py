# Exercise 5 from https://www.practicepython.org
# Written by:   Timo van Beelen
# Date:         10-04-2023

# Define global variables
list_a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# Define functions


# Main
if __name__ == "__main__":
    print([*set([j for j in list_b if j in list_a])])
    # For if anyone (especially for myself) looks back at this, we first check with the inner []-brackets if the item in list_b is in list_a (which is which does not matter)
    # Then we transform this new list obtained by the inner []-brackets into a set (which does not allow duplicates) and transform it back to a list, which is printed 
    # That this works, is both beautiful and disgusting at the same time