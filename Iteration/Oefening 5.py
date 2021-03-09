number = int(input("Enter a number (0 to stop): "))
largest_number = number
smallest_number = number
amount_of_numbers = 0
difference = 0

while number != 0:
    help_number = number
    number = int(input("Enter a number (0 to stop): "))
    amount_of_numbers += 1
    if help_number > number:
        largest_number = help_number
    else:
        smallest_number = help_number
difference = largest_number - smallest_number

if amount_of_numbers > 1:
    print("The difference between the largest number", largest_number, "and the smallest number", smallest_number,
          "=", difference)

if amount_of_numbers == 0:
    print("No numbers were entered.")
