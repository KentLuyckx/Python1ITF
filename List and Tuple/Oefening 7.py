import random  # Import random function.
begin_list = []  # Empty LIST for editing purposes
for i in range(random.randint(4, 5)):  # Determines the amount of numbers in the list
    begin_list.append(random.randint(0, 10))  # Determines which numbers to generate
print(begin_list)  # Print list

# Short solution
new_list = 2 * len(begin_list) * [0]  # New list twice as long as original, full of zeroes
new_list[-1] = begin_list[-1]  # Last number of new list is last number of original list
print(new_list)

# Long solution
last_number = begin_list[-1]  # Save last digit from original list
new_list = begin_list * 2  # Spawn new list that's twice as long as original list
for j in range(len(new_list)):  # Overgo new list
    if new_list[j] != 0:
        new_list[j] = 0  # Swap all numbers for zero
new_list.remove(0)  # Remove the first number (otherwise the new list = begin list x2 +1 in length
new_list.append(last_number)  # Add the saved number
print(new_list)
