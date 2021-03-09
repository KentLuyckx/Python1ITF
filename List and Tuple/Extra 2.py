python_classes = [['1ITFA', 35]]

for i in range(1, 8):  # Count from list position 2 till 8
    number_of_students = int(input("Number of students in 1ITF"+chr(ord('A')+i)+": "))  # Ask a number for 1ITFi
    python_classes.append(["1ITF"+chr(ord('A')+i), number_of_students])  # Append "1ITFi, number" to list

# print(*python_classes, sep="\n")
# Using an asterisk allows you to pull data from the entire array

sum_of_students = 0
for j in python_classes:  # Iterate over list
    print(j)   # Print class names and number of students
    sum_of_students += j[1]
print(sum_of_students, "students follow the python course")  # Sum of number of students
