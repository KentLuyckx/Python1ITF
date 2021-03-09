import random  # Import random
original_list = []
for i in range(random.randint(5, 15)):  # Set the amount of numbers in the list
    original_list.append(random.randint(0, 20))  # Determines the numbers in the list
print(original_list)  # Print list

for j in range(len(original_list)):  # Overgo the list
    if original_list[j] == 0:  # Searching for the number 0
        largest_uneven_number = 0  # Help variable for the largest uneven number
        for k in range(j+1, len(original_list)):  # Search the next number
            if (original_list[k] % 2 != 0) and (original_list[k] > largest_uneven_number):
                # If its an uneven number larger than 0
                largest_uneven_number = original_list[k]  # Save this number in a separate variable
        original_list[j] = largest_uneven_number  # Placing said number on the position of 0
print(original_list)