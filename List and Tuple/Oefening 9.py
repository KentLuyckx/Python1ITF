print("Enter your name and the distance to school.")
print("Type stop if you want to close the entry.")
names_list = []
distances_list = []
name = input("Your name: ")
if name.lower() != "stop":
    while name.lower() != "stop":
        names_list.append(name)
        distance_to_school = float(input("Distance to school: "))
        distances_list.append(distance_to_school)
        name = input("Your name: ")
    print("Overview")
    for i in range(len(distances_list)):
        print(names_list[i], "\t", distances_list[i])
    longest_distance = max(distances_list)
    index_longest_distance = distances_list.index(max(distances_list))
    most_distant_person = names_list[index_longest_distance]
    print(most_distant_person, "lives furthest: ", longest_distance, "km")
    print("The average distance is", sum(distances_list) / float(len(distances_list)))
