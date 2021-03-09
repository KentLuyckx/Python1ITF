task_distribution = {}

with open('./files/tasks.csv') as file:
    next(file)  # Drop csv header
    line = file.readline().rstrip()
    while line:
        names = line.split(';')
        for i in range(1, len(names)):
            if names[i] in task_distribution:
                task_distribution[names[i]] += 1
            else:
                task_distribution[names[i]] = 1
            line = file.readline().rstrip()

print('Task distribution:')
for person in task_distribution:
    print(person, task_distribution[names[i]])
