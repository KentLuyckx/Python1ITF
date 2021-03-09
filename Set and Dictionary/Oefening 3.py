classrooms = set()

with open('./files/local_booking.txt', encoding='utf8') as file:
    line = file.readline()
    while line:
        record = line.split(';')
        classrooms.add(record[3])
        line = file.readline()

print('Classrooms:')
for room in sorted(classrooms):
    print(room)
