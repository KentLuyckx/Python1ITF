string = input("What do you want to eat for lunch: ")

if (string.find("sandwich") >= 0) and string.rfind("sandwich"):
    something = string[string.find("sandwich") + 5: string.rfind("sandwich")]
    # For the characters between the first instance of sandwich and the second - you use ":"
    print("You have", something, "between your sandwich")
else:
    print('')

# "0" in python is falsey.
# If the string starts with sandwich, the starting position of the first sandwich is "0"
# So your if statement sees nothing and jumps to the else statement
# Find returns -1 if the value is not found - so this will run through the if segment
