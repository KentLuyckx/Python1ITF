input_open = open("../iteration/oefening 3.py")
output = open('./files/output_file.txt', 'w')

lines = input_open.readlines()
counter = 1

for line in lines:
    output.write("{:4} {}".format(counter, line))
    counter += 1

input_open.close()
output.close()
