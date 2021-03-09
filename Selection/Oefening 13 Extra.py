import random

win = 0
loss = 0
draw = 0
total_guess = 0
characters = ["rock", "paper", "scissors", "lizard", "spock"]


def valid(text, flag):
    error_message = ""
    while True:
        var = input(error_message + text)
        if flag == "s":
            if var.isalpha() is True:
                break
            else:
                error_message = "This is not valid, "
        elif flag == "i":
            if var.isdigit() is True:
                var = int(var)
                break
            else:
                error_message = user_name + " this is not a number, "
        elif flag == "g":
            if var == "rock" or var == "paper" or var == "scissors" or var == "lizard" or var == "spock":
                break
            else:
                error_message = user_name + " this is not a valid move! "
    return var


user_name = valid("What is your name? ", "s").upper()

while True:
    num_rounds = valid(user_name + " how many rounds do you want to play? ", "i")
    while num_rounds > total_guess:
        player = valid(user_name + """, what do you want as your character: 
            rock, paper, scissors, lizard or spock: """, "g")
        total_guess = total_guess + 1
        computer = characters[random.randint(0, 4)]
        print("COMPUTER CHOSE", computer.upper())
        if player == computer:
            draw = draw + 1
            print("Draw!")
        #   --------------------------------------------
        elif player == "rock":
            if computer == "paper" or computer == "spock":
                loss = loss + 1
                print(' '.join(("You lost", computer, "beats", player)))

            if computer == "scissors" or computer == "lizard":
                win = win + 1
                print(' '.join(("You win", player, "beats", computer)))

        elif player == "paper":
            if computer == "scissors" or computer == "lizard":
                loss = loss + 1
                print(' '.join(("You lost", computer, "beats", player)))

            if computer == "rock" or computer == "spock":
                win = win + 1
                print(' '.join(("You win", player, "beats", computer)))

        elif player == "scissors":
            if computer == "Spock" or computer == "rock":
                loss = loss + 1
                print(' '.join(("You lost", computer, " beats ", player)))

            if computer == "paper" or computer == "lizard":
                win = win + 1
                print(' '.join(("You win", player, "beats", computer)))

        elif player == "lizard":
            if computer == "scissors" or computer == "rock":
                loss = loss + 1
                print(' '.join(("You lost", computer, "beats", player)))

            if computer == "paper" or computer == "spock":
                win = win + 1
                print(' '.join(("You win", player, "beats", computer)))

        elif player == "spock":
            if computer == "lizard" or computer == "paper":
                loss = loss + 1
                print(' '.join(("You lost", computer, "beats", player)))

            if computer == "rock" or computer == "scissors":
                win = win + 1
                print(' '.join(("You win", player, "beats", computer)))

    end_game = input("To exit enter N, to play again enter any key ")
    if end_game == 'n' or end_game == 'N':
        print("THANKS FOR PLAYING " + user_name + '!')
        print("Your score is:")
        if win < 2:
            print(win, "win")
        else:
            print(win, "wins")
        if loss < 2:
            print(loss, "loss")
        else:
            print(loss, "losses")
        if draw < 2:
            print(draw, "draw")
        else:
            print(draw, "draws")
        break
    total_guess = 0
