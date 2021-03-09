word = input("Enter a word: ")
number_of_characters = int(input("Enter a number: "))

first_letter = word[:1]
last_letters = word[-number_of_characters:]
print(first_letter + last_letters)
