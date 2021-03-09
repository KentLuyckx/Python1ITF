number_one = int(input("Enter a number. Enter 0 to stop: "))
number_two = 1
amount_of_numbers = 0

while number_one != 0:
    amount_of_numbers = amount_of_numbers + 1
    product = number_one * number_two
    number_two = product
    number_one = int(input("Enter a number. Enter 0 to stop: "))
print("The product of the", amount_of_numbers, "numbers is", product)
