# Exercise 16 from https://www.practicepython.org
# Written by:   Timo van Beelen
# Date:         06-05-2023

# Add libraries
import secrets
import string
import sys


# Define functions
def int_input(string_prompt):
    try: return int(input(string_prompt))
    except ValueError as e: 
        sys.stderr.write(str(e))
        sys.exit(1)


# Main
if __name__ == "__main__":
    length = int_input("Length of password: ")
    password = ''.join(secrets.choice(string.ascii_letters+string.digits+string.punctuation) for i in range(length))
    print(password)
