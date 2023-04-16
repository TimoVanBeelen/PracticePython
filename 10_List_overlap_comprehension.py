# Exercise 10 from https://www.practicepython.org
# Written by:   Timo van Beelen
# Date:         12-04-2023

# Define global variables
list_a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# Define functions
def comprehension_lists(l):
    """
    This function comprehends lists to not include double entries
    """
    comp_l = []
    for x in l: 
        if x not in comp_l: comp_l.append(x)
    return comp_l


# Main
if __name__ == "__main__":
    list_c = comprehension_lists(list_a)
    list_d = comprehension_lists(list_b)
    print([x for x in list_c if x in list_d])