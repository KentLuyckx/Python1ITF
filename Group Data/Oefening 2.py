input_file = open('./files/courses.csv')
output_file = open('./files/students.csv', 'w')

next(input_file)  # Skip the csv header line
line = input_file.readline().rstrip()
record = line.split(';')

while line:
    student_id = record[3]
    output_line = student_id + ';' + record[4] + ';' + record[5]

    while line and record[3] == student_id:
        output_line += ';' + record[1] + '(' + record[2] + ')'
        line = input_file.readline().rstrip()
        record = line.split(';')
    output_file.write(output_line + '\n')
    print(output_line)

input_file.close()
output_file.close()
