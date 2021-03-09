number_one = int(input("Number 1 (0, 1 or 2): "))
number_two = int(input("Number 2 (0, 1 or 2): "))
number_three = int(input("Number 3 (0, 1 or 2): "))

if number_one == 2 and number_two == 2 and number_three == 2:
    print(10)
elif number_one == number_two == number_three:
    print(5)
elif (number_two == number_three) != number_one:
    print(1)
else:
    print(0)