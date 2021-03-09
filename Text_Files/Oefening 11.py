input_open = open("./files/output_file.txt")
output = open("./files/father_son.py", 'w')

lines = input_open.readlines()

for line in lines:
    output.write(line[5:])

input_open.close()
output.close()
