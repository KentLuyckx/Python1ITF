with open('./files/classrooms.txt') as file:
    line = file.readline().rstrip()
    record = line.split(';')

    while line:
        classroom = record[2]
        number_of_students = 0
        print(classroom)

        # <editor-fold desc="With list (currently in comments)">
        # room_list = []
        # while line and record[2] == classroom:
            # student_name = '\t'+record[1]+' '+record[0]
            # room_list.append(student_name)
            # number_of_students += 1
            # line = file.readline().rstrip()
            # record = line.split(';')
        # print(*room_list, sep='\n')
        # print("Number of students in classroom", classroom, '=', number_of_students)
        # </editor-fold>

        # <editor-fold desc="Without list">
        while line and record[2] == classroom:
            number_of_students += 1
            print("{} {} {}".format('\t', record[1], record[0]))
            line = file.readline().rstrip()
            record = line.split(';')
        print("Number of students in classroom {} = {}".format(classroom, number_of_students))
        # </editor-fold>
