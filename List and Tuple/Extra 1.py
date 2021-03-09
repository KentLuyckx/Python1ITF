numbers_list = []  # List for numbers
letters_list = []  # List for letters

text = input("Pass your string of characters: ")
for character in text:
    if character.isdigit():  # If character is a number . . .
        numbers_list.append(character)  # Add to numbers list
    elif character.islower():  # If character is lower case . . .
        letters_list.insert(0, character)  # Add to start of letter list
    elif character.isupper():  # If character is upper case . . .
        letters_list.append(character)  # Add to back of letter list
new_list = numbers_list + letters_list  # New list is combo of both lists
print(new_list)
