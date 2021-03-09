winning = "keep looking up"
masked_string = "#### ####### ##"

print("You have to guess this quote:", masked_string)
guess = input("Guess a letter or press / if you know the answer: ")
while guess is not "/":
    if guess in winning:
        for i in range(len(winning)):
            if winning[i] == guess:
                masked_string = masked_string[:i] + guess + masked_string[i+1:]
    print("You already have this result:", masked_string)
    guess = input("Guess a letter or press / if you know the answer: ")
answer = input("OK. You think you know, just say it: ")
if answer == winning:
    print("Yes, you win!")
else:
    print("Bad luck, wrong guess!")
