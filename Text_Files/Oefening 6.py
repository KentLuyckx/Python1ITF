import random

choice = random.randint(1, 10)
print("Wish", choice)
file_name = "./files/wish" + str(choice) + ".txt"
with open(file_name) as file:
    lines = file.readline()
    while lines:
        if lines != '\n':
            print(lines, end='')
        lines = file.readline()