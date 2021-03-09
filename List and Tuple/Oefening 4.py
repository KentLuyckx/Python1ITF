import random  # Import the random function.
original_list = []  # Start empty LIST, since we need to edit this one
for i in range(random.randint(6, 10)):  # Determines the amount of numbers in list
    original_list.append(random.randint(1, 10))  # Determines which numbers we enter in the list
print(original_list)  # Print the original list

if 4 in original_list:  # If the number 4 is in the list
    index_last_four = len(original_list) - 1 - original_list[::-1].index(4)
    # Search for the last instance of the number 4
    new_list = original_list[index_last_four + 1::]  # Create a new list from this last instance
    print(new_list)
else:  # If there is no 4 in the original list
    print("The number 4 does not exist in this list")
