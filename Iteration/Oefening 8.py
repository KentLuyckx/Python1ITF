end_digit = int(input("What final digit do you want to check the numbers on? "))
amount_of_numbers = 0

for counter in range(10):
    number = int(input("Enter a number: "))
    if end_digit == number % 10:
        amount_of_numbers = amount_of_numbers + 1

if amount_of_numbers == 1:
    print(amount_of_numbers, "out of the 10 numbers ends on", end_digit)
else:
    print(amount_of_numbers, "out of the 10 numbers end on", end_digit)
