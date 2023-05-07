# Exercise 6 from https://www.practicepython.org
# Written by:   Timo van Beelen
# Date:         11-04-2023

# Define global variables


# Define functions


# Main
if __name__ == "__main__":
    str = list(input("Please give me a palindrome.\n"))
    i=1
    palindrome = True
    for char in str:
        if not char == str[len(str)-i]:
            palindrome = False 
        else: i=i+1
    if palindrome: print("Thanks!")
    else: print("Wait, that is not a palindrome!")