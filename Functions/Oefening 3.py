def draw_square(char, number):
    for x in range(number):
        print(char * number)


character = input("Which character must be used to form the lines (enter = stop): ")
while character != '':
    number_of_lines = int(input("Number of characters per line = number of lines: "))
    draw_square(character, number_of_lines)
    character = input("Which character must be used to form the lines (enter = stop): ")
