name = input("Your name (Press ENTER to quit): ")

while name != '':
    print("Menu \n**********\nU Uppercase\nL Lowercase\nA Alternating\n***********")
    choice = input("Make your choice(U-L-A): ")
    while (choice != "U") and (choice != "L") and (choice != "A"):
        choice = input("Make your choice(U-L-A): ")
    if choice == "U":
        print(name.upper())
    elif choice == "L":
        print(name.lower())
    elif choice == "A":
        output = ''
        i = 0
        while i < len(name):
            if i % 2 == 0:
                output = output + name[i].upper()
            else:
                output = output + name[i].lower()
            i = i + 1
        print(output)
    name = input("Your name (Press ENTER to quit): ")
