import random

number = random.randint(1, 10)
output_file = "./files/table_"+str(number)+'.txt'

with open(output_file, 'w') as file:
    for counter in range(1, 11):
        file.write('{}x{}={}\n'.format(counter, number, counter*number))
