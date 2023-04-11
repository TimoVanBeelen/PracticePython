# Exercise 4 from https://www.practicepython.org
# Written by:   Timo van Beelen
# Date:         10-04-2023

# Define global variables

# Define functions

def get_input(): # Now input errors are solved as well
    try: num = int(input("Give me a number to find the divisor of:")) # Ask for a number to find the divisors for
    except: # If user does not give an integer
        print("I don't think that was an integer, please fill in an integer")
        num = get_input() # Make it recursive till the error is gone
    return num # Return the integer given as input


# Main
if __name__ == "__main__":
    num = get_input()
    
    # While loop to check all numbers
    i = 1
    divisors = []
    while i <= num:
        if num % i == 0: divisors.append(i) # No remainder -> divisable by i
        i = i+1                             # Go to the next iteration
    print("Divisors:" + str(divisors)) # Print the result