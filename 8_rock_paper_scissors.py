# Exercise 8 from https://www.practicepython.org
# Written by:   Timo van Beelen
# Date:         11-04-2023

# Define global variables


# Define functions


# Main
if __name__ == "__main__":
    while True:
        # Get input from the players
        hand_a = input("Player 1, what do you choose? Rock, paper or scissors?\t")
        hand_b = input("Player 2, what do you choose? Rock, paper or scissors?\t")

        #Check who won
        if hand_a == hand_b: print("Draw!")
        elif hand_a == "Rock" and hand_b == "Paper": print("Player 2 has won!")
        elif hand_a == "Paper" and hand_b == "Scissors": print("Player 2 has won!")
        elif hand_a == "Scissors" and hand_b == "Rock": print("Player 2 has won!")
        else: print("Player 1 has won!")

        if input("Play again? [Y/n]") == 'n': break
    print("Till next time")
