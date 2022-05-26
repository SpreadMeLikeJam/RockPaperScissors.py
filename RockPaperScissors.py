import random
from sys import argv

user_score = 0
op_score = 0
user = 0


while True:
    user_input = input("rock[r], paper[p], scissors[s]: ")

    opponent = random.randint(1, 3)
    opponent_choice = ""
    print("Player: %s" %user_input)

    if opponent == 1:
        opponent_choice = "r"
        print("Opponent: %s" %opponent_choice)
    if opponent == 2:
        opponent_choice = "p"
        print("Opponent: %s" %opponent_choice)
    if opponent == 3:
        opponent_choice = "s"
        print("Opponent: %s" %opponent_choice)
    
    if user_input == "r":
        user = 1
    if user_input == "p":
        user = 2
    if user_input == "s":
        user = 3

    
    if user == 1:
        if opponent == 2:
            op_score += 1
        if opponent == 3:
            user_score += 1

    if user == 2:
        if opponent == 1:
            user_score += 1
        if opponent == 3:
            op_score += 1

    if user == 3:
        if opponent == 1:
            op_score += 1
        if opponent == 2:
            user_score += 1

    print("Opponent: %s | Player: %s \n\n" %(op_score, user_score))
