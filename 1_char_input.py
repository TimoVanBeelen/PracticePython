# Exercise 1 from https://www.practicepython.org
# Written by:   Timo van Beelen
# Date:         10-04-2023

# Define global variables


# Define functions


# Main
if __name__ == "__main__":
    # Gather some information (name and age and how many times they want to hear how close they are to the 100)
    name = input("Hello! Who called me? What is your name? \n")
    age = int(input("Ah, well hello " + name + "! How old are you? \n"))
    repetition = int(input("How many times do I need to tell you how close to the 100 you are?\n"))

    # Calculate how long it will take for them to reach the age of 100
    x = 100-age

    # Print how long it will take
    i = 0
    while i < repetition:
        print("Geez... you have less than %s years left before you turn 100! I am not talking to people of that age! Byee!" %(str(x)))
        i = i+1

    print("Okay now I am really gone...")