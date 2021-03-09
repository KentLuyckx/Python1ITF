with open("./files/contacts.csv") as file:
    list_men = []
    list_women = []
    line = file.readline()
    while line:
        record = line.split(";")
        if record[3].rstrip() == "M":
            list_men.append(record[1] + " " + record[0])
        else:
            list_women.append(record[1] + " " + record[0])
        line = file.readline()
    list_men.sort()
    list_women.sort()
    print(len(list_women), "girls: ")
    for name in list_women:
        print("\t", name)
    print(len(list_men), "boys: ")
    for name in list_men:
        print("\t", name)
