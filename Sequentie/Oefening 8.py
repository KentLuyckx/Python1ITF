current_time = int(input("Enter the current hour: "))
wait_time = int(input("How long do you want to wait: "))

print("The alarm will sound at: ", (current_time + wait_time) % 24, "h")