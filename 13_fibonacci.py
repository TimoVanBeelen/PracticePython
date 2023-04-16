# Exercise 13 from https://www.practicepython.org
# Written by:   Timo van Beelen
# Date:         16-04-2023

# Add libraries


# Define global variables


# Define functions
def get_input():
    try: 
        num = int(input("Which length of the fibonacci sequence do you want? "))
    except: 
        print("The length of a sequence has to be an integer!")
        get_input()
    return num


# Main
if __name__ == "__main__":
    seq_length = get_input()
    fib_sequence = []
    for x in range(seq_length):
        if x < 2: fib_sequence.append(1)
        else: fib_sequence.append(fib_sequence[x-2] + fib_sequence[x-1])
    print(fib_sequence)
