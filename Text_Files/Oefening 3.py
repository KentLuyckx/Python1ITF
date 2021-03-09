with open('./files/first_names.txt') as file:
    first_names = file.readlines()
    counter = 0
    for first_name in first_names:  # For every field in record
        counter += 1  # Counter for 10 names
        print(first_name.rstrip().ljust(13, ' '), end='')
        if counter % 10 == 0:  # After 10 names
            print()  # New line
