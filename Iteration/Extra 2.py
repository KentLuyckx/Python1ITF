print("Press ENTER for each new striker you see")
print("If you want to pass a group, enter the amount")
print("Press 'S' and ENTER to stop")

stop = False
total = 0

while not stop:
    choice = input(">> ")
    if choice == "S" or choice == "s":
        stop_confirmation = input("Do you really want to stop?(Y/N): ")
        if stop_confirmation == "Y" or stop_confirmation == "y":
            stop = True
            print("Total amount of strikers =", total)
    else:
        if choice == '':
            total += 1
        else:
            total += int(choice)
