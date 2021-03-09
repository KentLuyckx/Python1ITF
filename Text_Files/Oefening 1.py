with open('./files/first_names.txt') as file:
    first_names = file.readline()
    number_of_names = 0
    while first_names:
        if first_names != '\n':
            print(first_names.rstrip('\n'))
            number_of_names += 1
        first_names = file.readline()
    print('There are', number_of_names, 'first names in the file.')

# Aanpassing voor namen met letter "Z"
with open('./files/first_names.txt') as file:
    first_names = file.readline()
    number_of_names = 0
    amount_with_z = 0
    while first_names:
        if first_names != '\n':
            if 'z' in first_names.lower():
                print(first_names.rstrip('\n'))
                amount_with_z += 1
            number_of_names += 1
        first_names = file.readline()
    print('There are', number_of_names, 'first names in the file.')
    print(amount_with_z, 'of which contain a letter z.')
