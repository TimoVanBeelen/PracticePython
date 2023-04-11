# Exercise 3 from https://www.practicepython.org
# Written by:   Timo van Beelen
# Date:         10-04-2023

# Define global variables
list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# Define functions


# Main
if __name__ == "__main__":
    print("Numbers in the list: %s" %list) # Print the list
    thresh = int(input("What number should the list not go over?\n"))
    for i in list: # Go over all the entries in the list
        if i < thresh: 
            print("Indeed, the entry %s is less than %i" %(list[i],thresh)) # Check the requirement (lower than 5)
print( [x for x in list if x<thresh] )