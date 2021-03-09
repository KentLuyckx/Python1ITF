import random

player_choice = input("What do you choose? rock, paper, or scissors: ")
move_list = ["rock", "paper", "scissors"]
computer_choice = random.choice(move_list)

if computer_choice == "rock" and player_choice == "rock":
    print("The computer chooses: ", computer_choice)
    print("This is a tie.")
elif computer_choice == "rock" and player_choice == "scissors":
    print("The computer chooses: ", computer_choice)
    print("The computer wins.")
elif computer_choice == "rock" and player_choice == "paper":
    print("The computer chooses: ", computer_choice)
    print("You win.")
elif computer_choice == "scissors" and player_choice == "scissors":
    print("The computer chooses: ", computer_choice)
    print("This is a tie.")
elif computer_choice == "scissors" and player_choice == "paper":
    print("The computer chooses: ", computer_choice)
    print("The computer wins.")
elif computer_choice == "scissors" and player_choice == "rock":
    print("The computer chooses: ", computer_choice)
    print("You win.")
elif computer_choice == "paper" and player_choice == "paper":
    print("The computer chooses: ", computer_choice)
    print("This is a tie.")
elif computer_choice == "paper" and player_choice == "rock":
    print("The computer chooses: ", computer_choice)
    print("The computer wins.")
else:
    print("The computer chooses: ", computer_choice)
    print("You win.")
