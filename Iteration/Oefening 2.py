number = int(input("Enter a number: "))
amount_of_zeroes = 0
amount_of_sixes = 0
help_number = number

while help_number != 0:
    number = help_number % 10
    if number == 6:
        amount_of_sixes = amount_of_sixes + 1
    elif number == 0:
        amount_of_zeroes = amount_of_zeroes + 1
    help_number = help_number // 10
print("The number consists of", amount_of_zeroes, "zeroes and", amount_of_sixes, "sixes")
