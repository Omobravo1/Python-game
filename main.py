#ROCK, PAPER SCISSORS GAME
# R = ROCK, P = PAPER, S = SCISSORS

import random

comp_wins = 0
player_wins = 0

def Choose_Option():
    user_choice = input("Choose R, P or S: ")
    if user_choice in ["Rock", "rock", "R", "r"]:
        user_choice = "R"
    elif user_choice in ["Paper", "paper", "P", "p"]:
        user_choice = "P"
    elif user_choice in ["Scissors", "scissors", "S", "s"]:
        user_choice = "S"
    else:
        print("I don't understand, try again.")
        Choose_Option()
    return user_choice

def Computer_Option():
    comp_choice = random.choice([1,3])
    if comp_choice == 1:
        comp_choice = "R"
    elif comp_choice == 2:
        comp_choice = "P"
    else:
        comp_choice = "S"
    return comp_choice

while True:
    print("")
    user_choice = Choose_Option()
    comp_choice = Computer_Option()
    print("")

    if user_choice == "R":
        if comp_choice == "R":
            print ("Player (Rock) : Computer (Rock). Tied.")
        elif comp_choice == "P":
            print ("Player (Rock) : The computer (Paper). Player lose, Computer win.")
            comp_wins += 1
            
        elif comp_choice == "S":
            print ("Player (Rock) : Computer (Scissors). Player win, Computer lose.")
            player_wins += 1

    elif user_choice == "P":
        if comp_choice == "R":
            print ("Player (Paper) : Computer (Rock). Player win, Computer lose.")
            player_wins += 1

        elif comp_choice == "P":
            print ("Player (Paper) : Computer (Paper). Tied.")

        elif comp_choice == "S":
            print ("Player (Paper) : Computer (Scissors). Player lose, Computer win.")
            comp_wins += 1

    elif user_choice == "S":
        if comp_choice == "R":
            print ("Player (Scissors) : Computer (Rock). Player lose, Computer win.")
            comp_wins += 1

        elif comp_choice == "P":
            print ("Player (Scissors) : Computer (Paper). Player win, Computer lose.")
            player_wins += 1

        elif comp_choice == "S":
            print("Player (Scissors) : Computer (Scissors). Tied.")

    print("")
    print("Player wins: " + str(player_wins),  "Computer wins: " + str(comp_wins))
    print("")

    user_choice = input ("Do you want to play again? (y/n)")
    if user_choice in ["Yes", "yes", "Y", "y"]:
        pass
    elif user_choice in ["No", "no", "N", "n"]:
        break
    else:
        break
