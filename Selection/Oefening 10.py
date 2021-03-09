first_number = int(input("First number: "))
second_number = int(input("Second number: "))
array = [65, 72, 83, 90]

if ((30 <= first_number <= 40) and (30 <= second_number <= 40)) or (first_number in array and second_number in array):
    print("Both numbers are ok.")
else:
    print("They are NOT ok.")
