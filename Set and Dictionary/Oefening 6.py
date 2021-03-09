# animals = {'horse': 'whinnying', 'cat': 'meows', 'dog': 'barks', 'cow': 'mooing'}
animals = {}
counter = 0

with open('./files/animal_sounds.txt', encoding='utf8') as file:
    line = file.readline().rstrip()
    while line:
        record = line.split(';')
#       key = record [0]
#       value = record [1]
#       animals[key] = value
        animals[record[0]] = record[1]  # adds key-value couple to dictionary
        line = file.readline().rstrip()

print('Do you know the animal sounds?')
for animal in animals:
    sound = input('What is the sound of a {}: '.format(animal))
    if sound == animals[animal]:
        counter += 1
print('You have {} correct answers.'.format(counter))
