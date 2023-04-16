# Exercise 11 from https://www.practicepython.org
# Written by:   Timo van Beelen
# Date:         12-04-2023

# Define global variables


# Define functions
def get_input():
    try: 
        num = int(input("Insert a number to check if it is a prime:"))
    except: 
        print("That is not an integer, primes have to be integers!")
        get_input()
    return num


# Main
if __name__ == "__main__":
    prime = get_input()
    for i in range(2, int(prime/2)):
        if prime % i == 0 : # Check if the number has a divisor that is not 1 (1 is also not a prime number apparantly)
            print("That is not a prime number!")
            quit()
    print("%i is indeed a prime number!" %prime)
    