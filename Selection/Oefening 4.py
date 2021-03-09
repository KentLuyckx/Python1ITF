number_one = int(input("Number 1: "))
number_two = int(input("Number 2: "))
number_three = int(input("Number 3: "))

if number_one + number_two == number_three:
    print("This works.")
elif number_two + number_three == number_one:
    print("This works.")
elif number_one + number_three == number_two:
    print("This works.")
else:
    print("This won't work.")