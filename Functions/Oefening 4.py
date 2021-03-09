import random


def generate_list(number, lower, upper):
    random_list = []
    for i in range(number):
        random_list.append(random.randint(lower, upper))
    return random_list


def filter_list(list_of_numbers):
    unique_values = []
    for item in list_of_numbers:
        if item not in unique_values:
            unique_values.append(item)
    return unique_values


# Basis oefening
# number_of_dice = int(input("How many dice do you want to roll?: "))
# random_values = generate_list(number_of_dice, 1, 6)

# print("You threw {}".format(random_values))
# print("Your unique rolls were: {}".format(filter_list(random_values)))

# Uitbreiding
random_values = generate_list(5, 1, 6)
counter = 0

while len(filter_list(random_values)) != 1:
    print("You threw {}".format(random_values))
    counter += 1
    random_values = generate_list(5, 1, 6)
print("You threw {}".format(random_values))
print("You threw poker after {} times".format(counter))
