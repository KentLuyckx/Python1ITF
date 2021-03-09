input_file = open('./files/hamlet.txt', 'r')
output_file= open('./files/hamlet2.txt','w')

lines = input_file.readlines()

for line in lines:
    for punctuation in ',.;:?!':
        line = line.replace(punctuation+'  ', punctuation+' ')
    output_file.write(line)

output_file.close()
input_file.close()

# Deel 2
input_file = open('./files/hamlet2.txt', 'r')
output_file = open('./files/hamlet3.txt', 'w')

lines = input_file.readlines()

for line in lines:
    for vowel in 'aeiou':
        line = line.replace(vowel, '')
    output_file.write(line)

output_file.close()
input_file.close()
