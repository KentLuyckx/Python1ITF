string = input('Enter a text consisting only of letters and numbers: ')

# Go through string and put each element in a set if its a number
numbers = set([int(element) for element in string if element.isdigit()])

# Go through string and put each element in a set if its a letter
letters = set([str(element) for element in string if element.isalpha()])

print('The numbers')
for number in numbers:  # For each number in set numbers
    print(numbers)  # Print number
print('The letters:')
for letter in letters:  # For each letter' in set letters
    print(letter)  # Print letter
