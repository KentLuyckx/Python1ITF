import random

computer_number = random.randint(1, 10)
amount_of_turns = 0
player_choice = int(input("Enter a positive number (1 to 10): "))

while player_choice != computer_number:
    if player_choice < computer_number:
        print("Higher!")
        amount_of_turns += 1
        player_choice = int(input("Enter a positive number (1 to 10): "))
    elif player_choice > computer_number:
        print("Lower!")
        amount_of_turns += 1
        player_choice = int(input("Enter a positive number (1 to 10): "))
if player_choice == computer_number:
    amount_of_turns += 1
    print("Correct guess!")
    print("You have guessed the number", player_choice, "in", amount_of_turns, "turns")
