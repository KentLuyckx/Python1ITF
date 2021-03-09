import random
pile_one = random.randint(20, 40)
pile_two = random.randint(20, 40)
win_condition = False

while (pile_one > 0) and (pile_two > 0) and win_condition is False:

    # PLAYER
    choice = int(input("Select a pile (1 or 2): "))
    amount = int(input("How many matches do you want to take? (between 3 and 8): "))
    if choice == 1:
        pile_one = pile_one - amount
    else:
        pile_two = pile_two - amount
    if (pile_one <= 0) or (pile_two <= 0):
        win_condition = True
        print("Congratulations, you win.")

    # COMPUTER
    if win_condition is False:
        choice = random.randint(1, 2)
        print("The computer selects pile: ", choice)
        amount = random.randint(3, 8)
        if choice == 1:
            pile_one = pile_one - amount
        else:
            pile_two = pile_two - amount
        print("The computer takes", amount, "matches")
        if (pile_one <= 0) or (pile_two <= 0):
            win_condition = True
            print("I win.")
