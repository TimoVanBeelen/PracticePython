# Exercise 15 from https://www.practicepython.org
# Written by:   Timo van Beelen
# Date:         16-04-2023

# Add libraries


# Define global variables


# Define functions


# Main
if __name__ == "__main__":
    string = input("Which sentence do you want backwards?\n")
    str_list = string.split()
    list_backwards = []
    for x in str_list: 
        list_backwards.append(str_list[len(str_list)-str_list.index(x)-1])
    print(' '.join(list_backwards))
    print(' '.join(string.split()[::-1])) # This does the same as above only in one line (::-1 reverses the order of a list)
